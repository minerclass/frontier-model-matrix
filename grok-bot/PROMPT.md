# Standard research prompt

Run this unchanged in every harness. Do not look at other harness folders.

> Today is the run date. Build a benchmark comparison of these frontier models, named as the requester gave them: "Gemini 4 Argon", "Cursor with Grok 4.7 various models", "ChatGPT 6.1 various relevant models as well as Astra", "Claude 5.5 set of models and 5.1 Fable", and "the new Muse models". Names may be approximate. Use web search to find each model's real name, maker, release date, and variants. If a named model does not seem to exist, say so.
>
> Collect (a) vendor-claimed scores from official launch posts, model cards, and system cards, and (b) independent results from leaderboards such as LMArena, Artificial Analysis, SWE-bench, ARC Prize, Epoch AI, Scale SEAL, Humanity's Last Exam, GPQA Diamond, AIME, MMMU, and Terminal-Bench. Every number needs a source URL and date. Never invent or estimate numbers. Mark anything unverified as a gap. Record settings (tools, compute, effort, pass@k) and note where claims and independent results differ.
>
> Save data.json following SCHEMA.md. Build one self-contained, offline-capable index.html with: a maker/family/variant diagram, a grouped bar chart with model toggles, a radar per model, a claims vs independent chart, a sortable table with source links, a release timeline, a "data as of" note, and methodology caveats. Save PNG screenshots in shots/. Write plainly, with no em dashes.
