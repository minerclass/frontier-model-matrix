# Frontier model matrix

Local record of published agent-model scores. Each harness has its own data file and its own page. A number enters the comparison only through the harness that published it.

This is not an in-house test. Nothing here was produced by running the models.

## Open it

From this folder:

```powershell
python build.py
python -m http.server 8765
```

Then open `http://127.0.0.1:8765/`. The pages also open as files, because the builder writes plain HTML.

## How a release is added

1. Add the model to `data/models.json` if it is new.
2. Add a JSON file in `data/harnesses/`, or add rows to the harness that published the score.
3. Set `origin` to `measured`, `quoted`, `derived`, or `unspecified`.
4. Quoted and derived rows need a `note` that says where the number came from.
5. Use a new `benchmark.id` when the setup is different. `automationbench` and `automationbench-aa` stay separate. `terminal-bench-4.0` and `terminal-bench-4.0-aa` stay separate.
6. Add a line to `data/releases.json`.
7. Run `python build.py`.

Do not copy a score from one harness file into another. The model page collects every harness that already named that model.

## Pages

- `index.html` lines up benchmarks that more than one harness published.
- `harnesses/` is one page per publisher, including how that publisher compiled the score.
- `models/` is one page per model, repeating each harness's cells for that model.

## Current sources

Read on 13 Oct 2026. CursorBench, the Gemini 4 Argon model card, OpenAI's GPT-6 and GPT-6.1 posts, Anthropic's Opus 5.5 and Sonnet 5.5 posts, xAI's Grok 4.7 post, Meta's Muse Wonder developer table, and Artificial Analysis's 12 Oct 2026 Wonder article.

Watermelon is the reported codename for Muse Wonder and Muse Wonder Full. The repository uses Meta's shipping names.

## Git

This copy lives outside OneDrive. Revision 2 adds `data/figures.json` and `NOTES.md` for the Frontier Benchmark Atlas brief. The hub link on each page is https://minerclass.github.io/frontier-benchmark-atlas/. Ask before pushing.
