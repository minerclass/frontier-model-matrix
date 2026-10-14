Written on: surface-arm · cursor · 2026-10-13

# Cursor compilation notes

Revision 2. Prompt: the Frontier Benchmark Atlas brief pasted into this session. Revision 1 is commits `e4ba379` and `058c977`, the first pass. This revision does not change any score.

## Who compiled it

- Harness: cursor
- Computer: surface-arm (`MSURFACE32ARM64`)
- Model: the Cursor session model for this chat. The product picker in this session listed Grok 4.7 as the coding model family available here. This note does not claim a specific API snapshot beyond that.
- Compile date: 2026-10-13

## How Micah's names were read

- Gemini 4 Argon is Google's model of that name, card dated 13 Oct 2026.
- Cursor with Grok 4.7 is xAI's Grok 4.7 at the effort levels CursorBench prints. Grok 4.6 is included only because it is on that same board and in xAI's launch table.
- ChatGPT 6 is a thinking slider. Instant through Extra High run GPT-6 Sol. Pro runs GPT-6 Astra. There is no model named ChatGPT 6.1 Astra.
- GPT-6.1 in the request is GPT-6.1 Sol, a Work and Codex model, not the chat slider.
- Astra is GPT-6 Astra.
- Claude 5.5 is Opus 5.5, Sonnet 5.5, and Haiku 5.5. Fable 5.1 is a separate Anthropic model, included because the request named it.
- Muse is Meta. Spark 1.3 is the model on CursorBench. Wonder and Wonder Full shipped 12 Oct 2026. Watermelon is a reported codename, not a third product name.

## What was read directly

Primary pages opened in this session on 13 Oct 2026:

- https://cursor.com/cursorbench
- https://deepmind.google/models/model-cards/gemini-4-argon/
- https://openai.com/index/gpt-6-astra/
- https://openai.com/index/introducing-gpt-6-sol-and-luna/
- https://openai.com/index/introducing-gpt-6-1-sol/
- https://help.openai.com/en/articles/20001354-gpt-6-and-other-models-in-chatgpt
- https://www.anthropic.com/claude-opus-5-5
- https://x.ai/news/grok-4-7
- https://dev.meta.ai/resources/blog/build-with-muse-wonder
- https://research.meta.ai/blog/muse-wonder
- https://research.meta.ai/static/muse-wonder-model-card
- https://artificialanalysis.ai/articles/muse-wonder

Sonnet 5.5 scores were taken from the public Sonnet 5.5 page as returned in search extracts from anthropic.com, not from a full saved copy of that page. Those cells stay in `anthropic-claude.json` with that limit.

The Muse Wonder Full ProgramBench cell of 59.0 has `readDirectly` false. The other four cells on that row were in the page text. 59.0 was the remaining cell after a primary-source reading of the same table.

## What was not used

Press roundups and aggregator estimates were not copied in as scores. `matrix_manager.py` and `data/harness_compilations.json` rank agent products without a published source. They are untracked and are not part of this compilation.

No other harness folder, and not the atlas comparison view, was opened for this revision.

## Figure file

`data/figures.json` is the file a hub can fetch. `python build.py` rewrites it from `data/harnesses/`. Do not edit `figures.json` by hand.

`stance` is one of:

- `claim`: the model's own lab printed the cell as its result, including a derived cell that lab stated.
- `rival`: the cell was taken from a lab comparison table about a model from a different lab, or the lab marked the cell as quoted or did not say who ran it.
- `independent`: the cell is on CursorBench's own board or in Artificial Analysis's own article.

A quote of CursorBench inside Anthropic's or xAI's post stays `rival` on that post's row, because that row is their table. The same number also appears under `independent` on the CursorBench row. The two are not averaged.

The GPT-6.1 Sol DeepSWE value 75.2 is derived: OpenAI printed GPT-6 Sol max at 68.8 and said GPT-6.1 Sol beats that best score by 6.4 points. OpenAI did not print 75.2.

## Name gaps

GPT-6, GPT-6.1 Sol, GPT-6 Astra, GPT-6 Luna, Muse Wonder, and Muse Wonder Full had no CursorBench row on the 13 Oct 2026 board. Those gaps are empty, not zero.
