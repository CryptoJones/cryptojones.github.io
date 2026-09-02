#!/usr/bin/env python3
"""Cut the Veto Variable narration into one MP3 per chapter, plus a manifest.

    python3 papers/split-narration.py <narration.mp3> <narration.jsonl> <source.pdf>

Why split at all: the reading runs about three hours, and NarratorTool encodes at
LAME VBR q2, which puts the single file near 100 MB -- GitHub's hard per-file
ceiling. Split by chapter, each part is a few MB, nothing approaches the limit,
and a reader can jump to the section they want instead of scrubbing a 3-hour bar.

The cuts are lossless (-c copy). The run log records an exact offset_seconds for
every chunk, including the silences the pipeline inserts between chunks and
chapters, so chapter boundaries are read off the log rather than guessed.

One correction has to be applied to those offsets. With the chatterbox backend
--speed is not a synthesis parameter; it is a time stretch ffmpeg applies while
encoding the finished audio. The log therefore records PRE-STRETCH positions and
the MP3 runs longer than the log says by exactly 1/speed. Cutting on the raw
offsets drifts progressively -- at 0.9x the last chapter lands about twenty
minutes early. The factor is recovered from the file itself rather than from a
--speed value nobody passes to this script.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
OUTDIR = SITE / "audio" / "papers"
SLUG = "the-veto-variable"


def chapter_titles(pdf: Path) -> dict[int, str]:
    """Titles for the chapters the run log numbers 0..N.

    These must come from the extractor, not from the raw PDF outline. This paper's
    outline carries 31 bookmarks but extraction yields 22 chapters -- an h1 whose
    first subsection starts on the same page spans no pages of its own and drops
    out. Numbering off the outline mislabels almost every part.

    One offset to apply: the extractor now keeps front matter as an untitled
    leading chapter (it did not when this narration was rendered), so the log's
    chapter i is chapters[i + 1] here.
    """
    sys.path.insert(0, "/home/hermes/Source/repos/NarratorTool")
    from narratortool.extract import extract

    chapters = extract(pdf).chapters
    if chapters and chapters[0].title is None:
        chapters = chapters[1:]
    return {i: (c.title or f"Part {i + 1}") for i, c in enumerate(chapters)}


def chapter_spans(log: Path) -> list[tuple[int, float, float]]:
    """(chapter, start, end) in seconds, from the run log's recorded offsets."""
    chunks = [json.loads(line) for line in log.read_text().splitlines()]
    chunks = [c for c in chunks if c.get("event") == "chunk"]
    if not chunks:
        sys.exit("run log contains no chunks")

    starts: dict[int, float] = {}
    ends: dict[int, float] = {}
    for c in chunks:
        ch = c["chapter"]
        start = c["offset_seconds"]
        end = start + c["seconds"]
        starts[ch] = min(starts.get(ch, start), start)
        ends[ch] = max(ends.get(ch, end), end)

    return [(ch, starts[ch], ends[ch]) for ch in sorted(starts)]


def true_duration(mp3: Path) -> float:
    """Decoded length in seconds. A VBR header estimate is not good enough to cut
    on, so the frames are actually counted."""
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "a", "-count_frames",
         "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(mp3)],
        capture_output=True, text=True,
    )
    if out.returncode != 0 or not out.stdout.strip():
        sys.exit(f"ffprobe could not read {mp3}")
    return float(out.stdout.strip().splitlines()[0])


def stretch_factor(mp3: Path, spans: list[tuple[int, float, float]]) -> float:
    """How much longer the encoded file is than the log's own timeline."""
    logged = max(end for _, _, end in spans)
    actual = true_duration(mp3)
    factor = actual / logged
    if not 0.5 <= factor <= 2.0:
        sys.exit(f"implausible stretch factor {factor:.3f} "
                 f"(log {logged:.0f}s vs file {actual:.0f}s) -- refusing to cut")
    return factor


def hhmmss(seconds: float) -> str:
    m, s = divmod(int(round(seconds)), 60)
    h, m = divmod(m, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def main() -> int:
    if len(sys.argv) not in (4, 5):
        sys.exit(__doc__)
    mp3, log, pdf = (Path(a) for a in sys.argv[1:4])
    # The main render predates the extractor fix, so it opens three quarters of
    # the way through the abstract. The title and abstract are rendered
    # separately and lead the playlist rather than re-running the whole 100
    # minutes.
    front = Path(sys.argv[4]) if len(sys.argv) == 5 else None
    for p in (mp3, log, pdf, *(x for x in (front,) if x)):
        if not p.is_file():
            sys.exit(f"missing: {p}")

    titles = chapter_titles(pdf)
    spans = chapter_spans(log)
    # A count mismatch means the titles are numbered on a different basis than the
    # log's chapters, and every part after the first divergence carries the wrong
    # heading. Silent mislabelling is worse than no labels, so stop.
    if len(titles) != len(spans):
        sys.exit(f"{len(titles)} chapter titles vs {len(spans)} chapters in the run "
                 f"log -- titles would be misaligned; refusing to write a manifest")
    factor = stretch_factor(mp3, spans)
    print(f"speed stretch: {factor:.6f}x  "
          f"(offsets scaled; last chapter would be "
          f"{(max(e for _, _, e in spans) * (factor - 1)) / 60:.0f} min out otherwise)\n")
    spans = [(ch, start * factor, end * factor) for ch, start, end in spans]
    OUTDIR.mkdir(parents=True, exist_ok=True)

    manifest = []
    if front:
        import shutil
        dest = OUTDIR / f"{SLUG}-00.mp3"
        shutil.copyfile(front, dest)
        manifest.append({
            "src": f"/audio/papers/{dest.name}",
            "title": "Title and Abstract",
            "duration": hhmmss(true_duration(dest)),
            "bytes": dest.stat().st_size,
        })
        print(f"  {0:2d}. {'Title and Abstract':<52} "
              f"{manifest[0]['duration']:>7}  {dest.stat().st_size // 1024:>5} KB")

    for ch, start, end in spans:
        name = f"{SLUG}-{ch + 1:02d}.mp3"
        out = OUTDIR / name
        cmd = [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            # -ss before -i seeks on the input, which keeps the copy fast and the
            # cut on a frame boundary.
            "-ss", f"{start:.3f}", "-to", f"{end:.3f}", "-i", str(mp3),
            "-c", "copy", str(out),
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            sys.exit(f"ffmpeg failed on chapter {ch}: {result.stderr.strip()[:300]}")

        manifest.append({
            "src": f"/audio/papers/{name}",
            "title": titles.get(ch, f"Part {ch + 1}"),
            "duration": hhmmss(end - start),
            "bytes": out.stat().st_size,
        })
        print(f"  {ch + 1:2d}. {manifest[-1]['title'][:52]:<52} "
              f"{manifest[-1]['duration']:>7}  {out.stat().st_size // 1024:>5} KB")

    (OUTDIR / f"{SLUG}.json").write_text(json.dumps(manifest, indent=2) + "\n")
    total = sum(m["bytes"] for m in manifest)
    print(f"\n{len(manifest)} parts, {total / 1024 / 1024:.1f} MB total, "
          f"largest {max(m['bytes'] for m in manifest) / 1024 / 1024:.1f} MB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
