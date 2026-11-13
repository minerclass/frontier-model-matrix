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
5. Use a new `benchmark.id` when the setup is different. `automationbench` and `automationbench-aa` stay separate. `terminal-bench-4.0`, `terminal-bench-4.0-aa`, `terminal-bench-4-0-vals`, and `terminal-bench-4-1` stay separate. `aa-intelligence-index-v4-3` and `aa-intelligence-index-v5-0` stay separate.
6. Add a line to `data/releases.json`.
7. Run `python build.py`.

Do not copy a score from one harness file into another. The model page collects every harness that already named that model.

## Pages

- `index.html` lines up benchmarks that more than one harness published.
- `harnesses/` is one page per publisher, including how that publisher compiled the score.
- `models/` is one page per model, repeating each harness's cells for that model.

## Current sources

Updated through 12 Nov 2026 (Revision 3). Primary sources read directly: CursorBench 4.0 (90 rows on 12 Nov 2026, plus three preserved rows from 13 Oct 2026), Google DeepMind's Gemini 4 Argon (13 Oct), Gemini 4 Carbon (10 Nov), and Gemini 4 Hydrogen (12 Nov) model cards and methodology pages, OpenAI's GPT-6 Astra, GPT-6 Sol/Luna, GPT-6.1 Sol, and GPT-6.1 Terra (26 Oct) pages, Anthropic's Opus 5.5, Sonnet 5.5, Haiku 5.5, and Claude Fable 5.2 / Mythos 5.2 (9 Nov) posts, xAI's Grok 4.7 post, Meta's Muse Wonder, Muse Spark Open (15 Oct), and Muse Ember (9 Nov) posts and evaluation reports, Moonshot AI's Kimi K3.1 Pro card (23 Oct), DeepSeek's V4.1 Flash 1017 card (17 Oct), Artificial Analysis's Index v5.0 leaderboard and October–November articles, and Vals AI's Index v2.2 and component leaderboards.

Watermelon is the reported codename for Muse Wonder and Muse Wonder Full. The repository uses Meta's shipping names.

## Git

This copy lives outside OneDrive. Revision 3 updates `data/figures.json` and `NOTES.md` for the Frontier Benchmark Atlas brief. The hub link on each page is https://minerclass.github.io/frontier-benchmark-atlas/. Ask before pushing.
