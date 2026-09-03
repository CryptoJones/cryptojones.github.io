#!/usr/bin/env python3
"""Render the-veto-variable.tex as a dark, readable web paper.

    python3 papers/build-reading-page.py

The page is DERIVED, never hand-edited: re-run this after any manuscript change
and commit the result. Pandoc does the LaTeX; everything here is the part pandoc
gets wrong or does not know about.

Three things pandoc leaves undone:

  * \\cite{key} becomes an EMPTY <span class="citation">. With a plain
    thebibliography (no .bib, no citeproc) pandoc has no numbering to insert, so
    the citations render as nothing at all. We number the \\bibitem keys in
    source order and write real [N] links back to the reference list.
  * The title block and abstract live in metadata, not in the body.
  * Claim/Definition environments come out as undifferentiated paragraphs.

Everything else -- section nesting, math, emphasis, the bibliography prose -- is
pandoc's, and is left alone.
"""
from __future__ import annotations

import html
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE = HERE.parent
TEX = HERE / "the-veto-variable.tex"
OUT = HERE / "the-veto-variable.html"
# Written by split-narration.py once the render lands. Absent, the page ships
# without a player rather than with a dock pointing at a 404.
MANIFEST = SITE / "audio" / "papers" / "the-veto-variable.json"

# The site's cyberdeck palette, verbatim from qwen3.8.html. A light background is
# a hard defect here, not a style preference -- see the theme note.
PALETTE = """
  --bg:#07090f; --panel:#0c1018; --panel2:#0e1622; --hair:#141a26;
  --fg:#cfd8e3; --dim:#8a97a8; --dim2:#5a6678; --bright:#e8eef6;
  --accent:#27d4ff; --green:#55ff99; --amber:#ff9b3d; --red:#ff6e6e;
"""


def run_pandoc() -> str:
    """LaTeX -> HTML fragment. --section-divs gives us nestable landmarks.

    --wrap=none is load-bearing, not cosmetic: pandoc's default hard-wraps at 72
    columns and will happily split `<span class="citation"` across a newline,
    which silently defeats every attribute regex below.
    """
    try:
        proc = subprocess.run(
            ["pandoc", "-f", "latex", "-t", "html5", "--mathjax",
             "--section-divs", "--id-prefix=p-", "--wrap=none", str(TEX)],
            capture_output=True, text=True, check=True,
        )
    except FileNotFoundError:
        sys.exit("pandoc is not installed -- `apt install pandoc` or see pandoc.org")
    except subprocess.CalledProcessError as exc:
        sys.exit(f"pandoc failed:\n{exc.stderr}")
    return proc.stdout


def tex_source() -> str:
    return TEX.read_text(encoding="utf-8")


def bib_order(tex: str) -> list[str]:
    """The \\bibitem keys in source order -- that order IS the citation numbering."""
    return re.findall(r"\\bibitem\{([^}]+)\}", tex)


def title_and_abstract(tex: str) -> tuple[str, str, str, str]:
    title = re.search(r"\\title\{\\textbf\{(.+?)\}\}", tex, re.S)
    author = re.search(r"\\author\{(.+?)\}", tex)
    abstract = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", tex, re.S)
    return (
        detex(title.group(1)) if title else "The Veto Variable",
        detex(author.group(1)) if author else "",
        affiliation(tex),
        tex_to_html(abstract.group(1).strip()) if abstract else "",
    )


def affiliation(tex: str) -> str:
    r"""The \affil block as HTML, keeping the paper's own line break.

    authblk's \\ splits school from institution on the title page, and the
    narration reads it the same way, so the break is preserved rather than
    flattened onto one line.
    """
    match = re.search(r"\\affil\{(.+?)\}\s*$", tex, re.M)
    if not match:
        print("  ! no \\affil found -- the page will carry no affiliation",
              file=sys.stderr)
        return ""
    parts = [detex(p) for p in match.group(1).split("\\\\")]
    return "<br>".join(html.escape(p) for p in parts if p)


def detex(s: str) -> str:
    s = re.sub(r"\\[a-zA-Z]+\{(.*?)\}", r"\1", s)
    return re.sub(r"\s+", " ", s).replace("~", " ").strip()


def tex_to_html(s: str) -> str:
    """Enough LaTeX for the abstract: emphasis, dashes, and inline math.

    Not a general converter -- pandoc handles the body. The abstract does not go
    through pandoc, so its $...$ math has to be rewritten to the \\(...\\)
    delimiters MathJax is configured for; left as $, it renders as literal
    dollar signs in the one paragraph everybody reads.
    """
    s = re.sub(r"(?<!\\)\$(.+?)(?<!\\)\$", r"\\(\1\\)", s, flags=re.S)
    s = s.replace("---", "&mdash;").replace("--", "&ndash;")
    s = re.sub(r"\\emph\{(.*?)\}", r"<em>\1</em>", s)
    s = re.sub(r"\\textbf\{(.*?)\}", r"<strong>\1</strong>", s)
    return re.sub(r"\s+", " ", s).strip()


def number_citations(body: str, keys: list[str]) -> str:
    """Empty <span class="citation" data-cites="a b"> -> linked [1, 2]."""
    index = {k: i + 1 for i, k in enumerate(keys)}

    def repl(match: re.Match) -> str:
        cited = match.group(1).split()
        links = []
        for key in cited:
            n = index.get(key)
            if n is None:  # a \cite with no \bibitem: show it rather than hide it
                links.append('<span class="cite cite--missing">[?]</span>')
                continue
            links.append(f'<a class="cite" href="#ref-{n}" title="{html.escape(key)}">{n}</a>')
        return '<span class="cites">[' + ", ".join(links) + "]</span>"

    return re.sub(r'<span class="citation" data-cites="([^"]*)"></span>', repl, body)


def number_bibliography(body: str, count: int) -> str:
    """thebibliography arrives as bare <p>s in a trailing div, with no heading of
    its own. Number them so the [N] links have somewhere to land, and give the
    block a real section so it appears in the contents."""
    match = re.search(r'<div class="thebibliography">(.*?)</div>', body, re.S)
    if not match:
        print("  ! no thebibliography block found -- citations will not resolve",
              file=sys.stderr)
        return body

    entries = re.findall(r"<p>(.*?)</p>", match.group(1), re.S)
    # \begin{thebibliography}{99} -- pandoc renders the widest-label argument as a
    # leading paragraph of its own. Left in place it becomes reference [1] and
    # shifts every real entry down one, so every [N] in the text cites the work
    # before the one it means.
    while entries and re.fullmatch(r"\d+", re.sub(r"<[^>]+>", "", entries[0]).strip()):
        entries.pop(0)
    if not entries:
        return body
    if len(entries) != count:
        print(f"  ! {len(entries)} rendered references vs {count} \\bibitem keys",
              file=sys.stderr)

    rows = "".join(
        f'<li class="ref" id="ref-{i + 1}"><span class="ref__n">{i + 1}</span>'
        f'<span class="ref__body">{e.strip()}</span></li>'
        for i, e in enumerate(entries)
    )
    section = ('<section id="p-references" class="level1"><h1>References</h1>'
               f'<ol class="refs">{rows}</ol></section>')
    return body.replace(match.group(0), section)


def mark_claims(body: str) -> str:
    """Claim/Definition/Condition paragraphs become panels. The LaTeX theorem
    environments flatten to <p><strong>Claim 1</strong>...; the label is the hook."""
    pattern = re.compile(
        r"<p><strong>(Claim|Definition|Condition|Proposition|Lemma)\s*"
        r"(\d+[^<]*)</strong>", re.I)
    return pattern.sub(
        lambda m: f'<p class="box box--{m.group(1).lower()}">'
                  f'<strong class="box__label">{m.group(1)} {m.group(2)}</strong>',
        body)


def build_toc(body: str) -> str:
    """Sidebar contents from the h1/h2s pandoc already gave ids."""
    heads = re.findall(r'<section id="(p-[^"]+)" class="level([12])">\s*<h[12][^>]*>(.*?)</h[12]>',
                       body, re.S)
    items = []
    for anchor, level, label in heads:
        text = re.sub(r"<[^>]+>", "", label).strip()
        items.append(f'<li class="toc__l{level}"><a href="#{anchor}">{text}</a></li>')
    return "<ol class='toc__list'>" + "".join(items) + "</ol>"


def build_dock() -> str:
    """The narration player, or nothing at all when the audio has not been split
    yet. A 3-hour reading is ~120 MB as one 96 kbps file, which is over GitHub's
    100 MB per-file ceiling -- so it ships as one file per chapter, and the dock
    is a playlist rather than a single <audio src>."""
    if not MANIFEST.is_file():
        return "<!-- no narration manifest yet; run split-narration.py -->"

    import json
    parts = json.loads(MANIFEST.read_text())
    options = "".join(
        f'<option value="{html.escape(p["src"])}">{i + 1}. {html.escape(p["title"])}'
        f' &middot; {p["duration"]}</option>'
        for i, p in enumerate(parts)
    )
    return f"""<div class="dock">
  <span class="dock__label">Narration</span>
  <select class="dock__select" aria-label="Choose a section to hear">{options}</select>
  <audio controls preload="none"></audio>
  <span class="dock__note">local TTS &middot; author's voice</span>
</div>
<script>
(function () {{
  var sel = document.querySelector('.dock__select');
  var au = document.querySelector('.dock audio');
  if (!sel || !au) return;
  function load(play) {{
    au.src = sel.value;
    if (play) au.play();
  }}
  sel.addEventListener('change', function () {{ load(true); }});
  // Roll into the next section rather than stopping dead between chapters.
  au.addEventListener('ended', function () {{
    if (sel.selectedIndex < sel.options.length - 1) {{
      sel.selectedIndex++;
      load(true);
    }}
  }});
  load(false);
}})();
</script>"""


def page(title: str, author: str, affil: str, abstract: str, body: str,
         toc: str, dock: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(re.sub(r'<[^>]+>', '', abstract)[:200])}">
<meta name="author" content="{html.escape(author)}">
<style>
:root {{{PALETTE}
  --mono: ui-monospace, "SF Mono", "JetBrains Mono", Menlo, Consolas, monospace;
  --prose: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
}}
* {{ box-sizing: border-box; }}
html {{ scroll-behavior: smooth; scroll-padding-top: 5rem; }}
body {{
  margin: 0; background: var(--bg); color: var(--fg);
  font-family: var(--prose); font-size: 18px; line-height: 1.7;
  -webkit-text-size-adjust: 100%;
}}
/* The glow is fixed, not on <body>: a gradient on a 45-page body stretches into
   an invisible smear. */
.glow {{
  position: fixed; inset: 0; z-index: -1; pointer-events: none;
  background: radial-gradient(120% 80% at 80% -10%, rgba(39,212,255,.06), transparent 60%);
}}
#progress {{
  position: fixed; top: 0; left: 0; height: 2px; width: 0;
  background: var(--accent); z-index: 60; transition: width .1s linear;
  box-shadow: 0 0 10px rgba(39,212,255,.6);
}}

.wrap {{ display: grid; grid-template-columns: minmax(0,1fr); max-width: 1200px; margin: 0 auto; }}
@media (min-width: 1000px) {{
  .wrap {{ grid-template-columns: 260px minmax(0,1fr); gap: 3rem; }}
}}

/* ---- sidebar ---- */
.side {{ font-family: var(--mono); font-size: 13px; }}
@media (min-width: 1000px) {{
  .side {{ position: sticky; top: 0; height: 100vh; overflow-y: auto;
           padding: 2rem 0 6rem 1.5rem; }}
}}
@media (max-width: 999px) {{
  .side {{ border-bottom: 1px solid var(--hair); padding: 1rem 1.25rem; }}
  .toc__list {{ display: none; }}
  .side[open] .toc__list {{ display: block; }}
}}
.side__home {{ color: var(--dim); text-decoration: none; letter-spacing: .14em;
               text-transform: uppercase; font-size: 11px; }}
.side__home:hover {{ color: var(--accent); }}
.toc__list {{ list-style: none; margin: 1.5rem 0 0; padding: 0; }}
.toc__list a {{ color: var(--dim); text-decoration: none; display: block;
                padding: .3rem 0 .3rem .75rem; border-left: 1px solid var(--hair);
                line-height: 1.35; }}
.toc__list a:hover {{ color: var(--accent); border-left-color: var(--accent); }}
.toc__list a.active {{ color: var(--bright); border-left-color: var(--accent);
                       background: linear-gradient(90deg, rgba(39,212,255,.08), transparent); }}
.toc__l2 a {{ padding-left: 1.75rem; font-size: 12px; color: var(--dim2); }}

/* ---- paper ---- */
.paper {{ padding: 2rem 1.25rem 8rem; max-width: 74ch; }}
.badge {{
  display: inline-block; font-family: var(--mono); font-size: 11px;
  letter-spacing: .14em; text-transform: uppercase; color: var(--amber);
  border: 1px solid #3a2a14; background: #160f06; border-radius: 6px;
  padding: 3px 10px; margin-bottom: 1rem;
}}
h1.paper__title {{
  font-family: var(--mono); font-size: clamp(1.6rem, 4vw, 2.3rem);
  line-height: 1.25; color: var(--accent); margin: .2rem 0 .6rem;
  text-shadow: 0 0 14px rgba(39,212,255,.35);
}}
.paper__author {{ font-family: var(--mono); color: var(--dim); font-size: 14px;
                  margin-bottom: .35rem; }}
.paper__affil {{ font-family: var(--mono); color: var(--dim2); font-size: 13px;
                 line-height: 1.5; margin: 0 0 2rem; }}
.abstract {{
  border: 1px solid var(--hair); background: var(--panel); border-radius: 8px;
  padding: 1.25rem 1.5rem; margin: 0 0 2.5rem; font-size: 16.5px;
}}
.abstract__label {{
  font-family: var(--mono); font-size: 11px; letter-spacing: .16em;
  text-transform: uppercase; color: var(--green); display: block; margin-bottom: .6rem;
}}
.paper h1 {{
  font-family: var(--mono); font-size: 1.35rem; color: var(--accent);
  margin: 3.5rem 0 .8rem; padding-bottom: .4rem; border-bottom: 1px solid var(--hair);
}}
.paper h2 {{ font-family: var(--mono); font-size: 1.08rem; color: var(--green);
             margin: 2.5rem 0 .6rem; }}
.paper h3 {{ font-family: var(--mono); font-size: .95rem; color: var(--amber);
             margin: 2rem 0 .5rem; }}
.paper p {{ margin: 0 0 1.15rem; }}
.paper em {{ color: var(--bright); }}
.paper strong {{ color: var(--bright); }}
.paper a {{ color: var(--accent); }}
blockquote {{ border-left: 3px solid var(--hair); margin: 1.5rem 0;
              padding: .3rem 0 .3rem 1.25rem; color: var(--dim); }}
code {{ font-family: var(--mono); background: var(--panel2); border: 1px solid var(--hair);
        border-radius: 4px; padding: 1px 6px; font-size: .85em; color: #bfe6ff; }}

/* Claim / Definition panels */
.box {{ border: 1px solid var(--hair); border-left: 3px solid var(--accent);
        background: var(--panel); border-radius: 0 8px 8px 0;
        padding: 1rem 1.25rem; margin: 1.75rem 0; }}
.box--definition {{ border-left-color: var(--green); }}
.box--condition {{ border-left-color: var(--amber); }}
.box__label {{ font-family: var(--mono); font-size: 12px; letter-spacing: .1em;
               text-transform: uppercase; color: var(--accent); display: block;
               margin-bottom: .4rem; }}
.box--definition .box__label {{ color: var(--green); }}
.box--condition .box__label {{ color: var(--amber); }}

/* Citations */
.cites {{ font-family: var(--mono); font-size: .78em; color: var(--dim2);
          white-space: nowrap; }}
a.cite {{ color: var(--dim); text-decoration: none; padding: 0 1px; }}
a.cite:hover {{ color: var(--accent); }}
.cite--missing {{ color: var(--red); }}

/* References */
.refs {{ list-style: none; padding: 0; margin: 1.5rem 0 0; font-size: 15px; }}
.ref {{ display: flex; gap: .9rem; padding: .55rem 0; border-bottom: 1px solid var(--hair);
        color: var(--dim); }}
.ref:target {{ background: rgba(39,212,255,.07); }}
.ref__n {{ font-family: var(--mono); color: var(--dim2); font-size: 12px;
           min-width: 2.2rem; text-align: right; padding-top: .25rem; }}

/* Math must scroll on its own, never widen the page. */
mjx-container[display="true"] {{ overflow-x: auto; overflow-y: hidden;
                                 max-width: 100%; padding: .3rem 0; }}
table {{ display: block; overflow-x: auto; max-width: 100%; border-collapse: collapse; }}

/* ---- audio dock ---- */
.dock {{
  position: fixed; left: 0; right: 0; bottom: 0; z-index: 50;
  background: rgba(7,9,15,.94); backdrop-filter: blur(8px);
  border-top: 1px solid var(--hair); padding: .6rem 1rem;
  display: flex; align-items: center; gap: .9rem; flex-wrap: wrap;
  font-family: var(--mono); font-size: 12px;
}}
.dock__label {{ color: var(--green); letter-spacing: .12em; text-transform: uppercase;
                font-size: 10px; }}
.dock audio {{ flex: 1 1 260px; min-width: 0; height: 34px; }}
.dock__note {{ color: var(--dim2); }}
footer {{ font-family: var(--mono); font-size: 12px; color: var(--dim2);
          border-top: 1px solid var(--hair); margin-top: 4rem; padding: 1.5rem 0 0; }}
footer a {{ color: var(--dim); }}
</style>
<script>
  window.MathJax = {{
    tex: {{ inlineMath: [['\\\\(', '\\\\)']], displayMath: [['\\\\[', '\\\\]']] }},
    options: {{ renderActions: {{ addMenu: [] }} }},
    chtml: {{ scale: 0.95 }}
  }};
</script>
<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-chtml.js"></script>
</head>
<body>
<div class="glow"></div>
<div id="progress"></div>
<div class="wrap">
  <details class="side" open>
    <summary class="side__home"><a class="side__home" href="/">&larr; cryptojones</a></summary>
    <nav aria-label="Contents">{toc}</nav>
  </details>
  <main class="paper">
    <span class="badge">Preprint &middot; arXiv</span>
    <h1 class="paper__title">{html.escape(title)}</h1>
    <p class="paper__author">{html.escape(author)}</p>
    <p class="paper__affil">{affil}</p>
    <div class="abstract"><span class="abstract__label">Abstract</span>{abstract}</div>
    {body}
    <footer>
      <p>Read it as the publisher intended:
         <a href="/papers/the-veto-variable.pdf">PDF</a> &middot;
         <a href="/papers/the-veto-variable.tex">LaTeX source</a></p>
      <p>This page is generated from the manuscript by
         <code>papers/build-reading-page.py</code>. Narration rendered locally with
         <a href="https://github.com/CryptoJones/NarratorTool">NarratorTool</a>.</p>
    </footer>
  </main>
</div>
{dock}
<script>
(function () {{
  var bar = document.getElementById('progress');
  var main = document.querySelector('.paper');
  function onScroll() {{
    var top = main.offsetTop;
    var span = main.offsetHeight - window.innerHeight;
    var pct = span > 0 ? (window.scrollY - top) / span : 0;
    bar.style.width = Math.max(0, Math.min(1, pct)) * 100 + '%';
  }}
  addEventListener('scroll', onScroll, {{ passive: true }});
  onScroll();

  // Highlight the section being read. Only sections that pandoc gave an id.
  var links = {{}};
  document.querySelectorAll('.toc__list a').forEach(function (a) {{
    links[a.getAttribute('href').slice(1)] = a;
  }});
  var current = null;
  var io = new IntersectionObserver(function (entries) {{
    entries.forEach(function (e) {{
      if (!e.isIntersecting) return;
      var a = links[e.target.id];
      if (!a || a === current) return;
      if (current) current.classList.remove('active');
      a.classList.add('active');
      current = a;
    }});
  }}, {{ rootMargin: '-10% 0px -80% 0px' }});
  document.querySelectorAll('section[id]').forEach(function (s) {{ io.observe(s); }});
}})();
</script>
</body>
</html>
"""


def main() -> int:
    tex = tex_source()
    keys = bib_order(tex)
    title, author, affil, abstract = title_and_abstract(tex)

    body = run_pandoc()
    body = number_citations(body, keys)
    body = number_bibliography(body, len(keys))
    body = mark_claims(body)
    toc = build_toc(body)

    OUT.write_text(page(title, author, affil, abstract, body, toc, build_dock()),
                   encoding="utf-8")
    print(f"wrote {OUT.relative_to(HERE.parent)}  "
          f"({OUT.stat().st_size // 1024} KB, {len(keys)} references)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
