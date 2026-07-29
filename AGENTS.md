# Repository Instructions

This repository is CryptoJones's personal blog site.

## Git workflow

- Direct commits to `master` or `main` are explicitly authorized for this repository.
- Push completed changes directly to the corresponding `origin/master` or `origin/main` branch; a feature branch and pull request are not required.
- Keep changes scoped to the requested blog-site work, and verify the working tree before committing or pushing.

## Writing

- **Target an eighth-grade reading level for blog posts.** Prefer short sentences and
  common words. It's fine to use technical terms, but define each one in plain language
  the first time it appears (a short blockquote works well).
- Do not use em dashes in blog posts.

## Index descriptions

- Add a plain-text `description` field to the YAML front matter of every new post.
- Write one or two short sentences that explain the post in about 20 to 30 words.
- Keep the description at an eighth-grade reading level. Do not put HTML, Markdown,
  Liquid tags, or media embeds in it.
- The home page in `index.html` must display `post.description` when it exists and
  fall back to the generated excerpt for older posts.
- Build the site and check the new post card before publishing. A post that begins
  with a video or other embed must still have a useful text description on the index.

## Article narration

- Create narration for every new blog post before publishing it.
- Use the canonical voice tools and reference files in the adjacent
  `../aaronkclark-voicemodel` repository:
  - `qwen_narrate_longform.py`
  - `dataset/reference/aaron_reference.wav`
  - `dataset/reference/aaron_reference.txt`
  - `validate_renascence_asr.py`
- Narrate the article text, not its YAML front matter. Leave out code listings,
  raw URLs, image paths, video embed markup, and other text that is not useful when
  spoken.
- Split long text into a JSON list of short chunks for `qwen_narrate_longform.py`.
  Each chunk must contain `id`, `text`, `stanza`, and `pause_after_ms`.
- Use the accepted Qwen3-TTS 0.6B Aaron voice, language `English`, and native
  pacing. The renderer requires an RTX 3060 CUDA device. Use `--resume` so an
  interrupted render can continue safely.
- Encode the finished WAV as a mono, 24 kHz, 96 kbps MP3. Normalize it with
  FFmpeg's `loudnorm=I=-16:TP=-1.5:LRA=11` filter.
- Save the final file as `audio/posts/<post-slug>.mp3` and add
  `audio: /audio/posts/<post-slug>.mp3` to the post's YAML front matter.
- The post layout places the compact player directly below the title. Do not add
  a second player inside the post body.
- Confirm that the MP3 is playable, validate the narration against its source
  text, build the Jekyll site, and verify the page and audio path before publishing.
