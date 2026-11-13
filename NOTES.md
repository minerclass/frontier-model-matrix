Written on: surface-arm · cursor · 2026-11-12

# Cursor compilation notes

Revision 3. Prompt: Micah's 12 Nov 2026 instruction to update the model Atlas for Gemini 4 Hydrogen, Gemini 4 Carbon, and other recent frontier releases, continuing from the Frontier Benchmark Atlas brief (`HARNESS.md`). Revision 1 is commits `e4ba379` and `058c977`. Revision 2 is commit `b362d95` (13 Oct 2026).

## Who compiled it

- Harness: cursor
- Computer: surface-arm (`MSURFACE32ARM64`)
- Model: Gemini 4 Carbon (Cursor session model for Revision 3; Revision 2 ran on the earlier Cursor session model where the picker listed the Grok 4.7 family)
- Compile date: 2026-11-12 (first compiled 2026-10-13)

## What changed in Revision 3

1. **Google Gemini 4 Carbon and Gemini 4 Hydrogen**: Added `data/harnesses/google-carbon-card.json` from the 10 Nov 2026 Carbon model card and methodology page, and `data/harnesses/google-hydrogen-card.json` from the 12 Nov 2026 Hydrogen model card, methodology page, and Google blog post. Extended `google-argon-card.json` with three rows from the Argon card (`chartography-no-tools`, `riemannbench`, and `graphwalks-256k-1m`) that connect directly to Carbon and Hydrogen.
2. **Anthropic Claude Fable 5.2, Mythos 5.2, Sonnet 5.5, and Haiku 5.5**: Updated `data/harnesses/anthropic-claude.json` from direct readings of Anthropic's 9 Nov 2026 Fable 5.2 / Mythos 5.2 post, 28 Sep 2026 Sonnet 5.5 post, and 7 Oct 2026 Haiku 5.5 post (resolving Revision 2's search-extract note on Sonnet 5.5).
3. **OpenAI GPT-6.1 Terra and GPT-6.1 Sol**: Updated `data/harnesses/openai-gpt-6.json` from the Vega-Lite chart specs embedded in OpenAI's 26 Oct 2026 GPT-6.1 Terra launch page (`Agents' Last Exam v1`, `MMMU-Pro (Vision)`, `OSWorld 2.1, offline set`, `Terminal-Bench 4.0`, and `Terminal-Bench-Science 0.1`), read in the Cursor IDE browser. Also recorded OpenAI's GPT-6 Cyber cell where Anthropic cited it on CyScenarioBench.
4. **Meta Muse Ember, Muse Spark Open, and Muse Wonder model card**: Added `data/harnesses/meta-muse-ember.json` from Meta's 9 Nov 2026 Muse Ember blog post and evaluation report plus Meta's 15 Oct 2026 Muse Spark Open Hugging Face model card and evaluation methodology. Read the Muse Wonder model card directly on 12 Nov 2026, confirming Wonder Full's 59.0 ProgramBench cell (`readDirectly` is now `true`) and adding Fable 5.1's 79.0 MemoryBench cell along with PSI and OSWorld 2.1 (partial).
5. **Open-weight frontier cards (Kimi K3.1 Pro and DeepSeek V4.1 Flash 1017)**: Added `data/harnesses/moonshot-kimi-k3-1.json` (23 Oct 2026) and `data/harnesses/deepseek-v4-1-flash.json` (17 Oct 2026) from their official Hugging Face model cards.
6. **CursorBench 4.0 refresh**: Updated `data/harnesses/cursorbench.json` to all 90 rows on the 12 Nov 2026 CursorBench board, adding Gemini 4 Carbon (High 60.4%, Medium 60.1%, Low 58.6%), Claude Fable 5.2 (Max 60.0% down to Low 53.2%), Gemini 4 Hydrogen (High 54.3%, Medium 46.7%, Low 27.9%), Muse Wonder (Max 50.4% down to Minimal 34.2%), and DeepSeek V4.1 Flash 1017 (Max 47.7% down to Low 44.9%). The three rows from the 13 Oct 2026 board that no longer appear on the 12 Nov 2026 board (Gemini 4 Argon Minimal 48.8% and Gemini 3.8 Flash High/Medium) are preserved with `sourceDate: "2026-10-13"` and notes.
7. **Independent evaluators (Artificial Analysis v5.0 / MKA and Vals AI v2.2)**: Updated `data/harnesses/artificial-analysis.json` with AA Intelligence Index v5.0 (launched 27 Oct 2026, read from the 12 Nov 2026 LLM Leaderboard and AA's October–November articles) and Multimodal Knowledge Agent (MKA Climb WSR, 10 Nov 2026), while keeping v4.3 separate. Added `data/harnesses/vals-ai.json` for Vals Index v2.2 and its standalone component leaderboards (`Finance Agent v2.1`, `EMB v1.1`, `Terminal-Bench 4.0` in `mini-swe-agent`, `Legal Research Bench`, `Tax Agent Bench`, `HLAB-Vals-1.1`, and `Vibe Code Bench v1.1`).
8. **Builder fix for lower-is-better benchmarks**: Updated `build.py` so `best_row` picks the lowest cost on `higherIsBetter: false` benchmarks (such as cost per task) instead of the highest cost, and formatted four- and five-digit dollar balances cleanly for Vending-Bench 2.

## How model names and non-releases were read

- **Gemini 4 Carbon** (`gemini-4-carbon`): Google DeepMind frontier model based on Argon; previewed late October 2026 via Fairwind and Artificial Analysis, general availability and model card published 10 Nov 2026 ($4 / $20 standard, $2 / $10 introductory through 30 Nov 2026).
- **Gemini 4 Hydrogen** (`gemini-4-hydrogen`): Google DeepMind fast, efficient Gemini 4 model adapted from Carbon, published 12 Nov 2026 ($1.50 / $7.50 flat across 1M context, thinking levels low through xhigh).
- **Claude Fable 5.2 and Claude Mythos 5.2** (`claude-fable-5-2`, `claude-mythos-5-2`): Anthropic's 9 Nov 2026 technical upgrade ($8 / $40 standard, $16 / $80 fast mode). Same underlying model; Fable 5.2 is generally available with cyber/biology safeguards, Mythos 5.2 is gated to Verification Programs.
- **GPT-6.1 Terra** (`gpt-6-1-terra`): OpenAI's 26 Oct 2026 fast computer-use and coding model in ChatGPT Work, Codex, and the API ($1 / $5 per 1M tokens). **GPT-6 Cyber** (`gpt-6-cyber`, 5 Nov 2026) is OpenAI's restricted cybersecurity model for vetted researchers; only the CyScenarioBench score cited by Anthropic is recorded here.
- **Muse Ember** (`muse-ember`, 9 Nov 2026) and **Muse Spark Open** (`muse-spark-open`, 15 Oct 2026): Meta's smallest efficient API/Muse Code model ($0.10 / $0.50 up to 200K) trained using Muse Wonder Full, and Meta's 816B/42B-active open-weight MoE under the Muse Model License.
- **Kimi K3.1 Pro** (`kimi-k3-1-pro`, 23 Oct 2026) and **DeepSeek V4.1 Flash 1017** (`deepseek-v4-1-flash-1017`, 17 Oct 2026): Leading open-weight releases scored across AA v5.0, Vals v2.2, and (for DeepSeek 1017) CursorBench 4.0.
- **xAI Grok 4.8**: Not yet scored. Elon Musk stated on 10 Nov 2026 that Grok 4.8 completed pretraining, entered reinforcement learning on a rewritten C/C++ stack, and plans a limited Bot rollout later this week, with no benchmark figures published as of 12 Nov 2026. Grok 4.7 remains xAI's newest scored model.

## What was read directly

Primary pages opened in Revision 2 (13 Oct 2026) and Revision 3 (12 Nov 2026):

- https://cursor.com/cursorbench (read 13 Oct 2026 and 12 Nov 2026)
- https://deepmind.google/models/model-cards/gemini-4-argon/
- https://deepmind.google/models/model-cards/gemini-4-carbon/
- https://deepmind.google/models/evals-methodology/gemini-4-carbon
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/
- https://deepmind.google/models/model-cards/gemini-4-hydrogen/
- https://deepmind.google/models/evals-methodology/gemini-4-hydrogen
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/
- https://openai.com/index/gpt-6-astra/
- https://openai.com/index/introducing-gpt-6-sol-and-luna/
- https://openai.com/index/introducing-gpt-6-1-sol/
- https://openai.com/index/introducing-gpt-6-1-terra (prose and embedded Vega-Lite chart specs read directly in the Cursor IDE browser)
- https://help.openai.com/en/articles/20001354-gpt-6-and-other-models-in-chatgpt
- https://www.anthropic.com/claude-opus-5-5
- https://www.anthropic.com/claude-sonnet-5-5
- https://www.anthropic.com/claude-haiku-5-5
- https://www.anthropic.com/claude-fable-and-mythos-5-2
- https://x.ai/news/grok-4-7
- https://dev.meta.ai/resources/blog/build-with-muse-wonder
- https://research.meta.ai/static/muse-wonder-model-card
- https://research.meta.ai/blog/muse-spark-open
- https://dev.meta.ai/resources/blog/build-with-muse-spark-open
- https://research.meta.ai/static/muse-spark-open-evaluation-methodology
- https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B
- https://research.meta.ai/blog/muse-ember
- https://research.meta.ai/static/muse-ember-evaluation-report
- https://huggingface.co/moonshotai/Kimi-K3.1-Pro
- https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017
- https://artificialanalysis.ai/leaderboards/models
- https://artificialanalysis.ai/articles/muse-wonder
- https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier
- https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5
- https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1
- https://artificialanalysis.ai/articles/meta-s-muse-ember-is-the-cheapest-model-scoring-36-on-the-intelligence-index
- https://artificialanalysis.ai/articles/google-deepmind-multimodal-knowledge-agent
- https://www.vals.ai/benchmarks/vals_index
- https://www.vals.ai/benchmarks/fabv2-1
- https://www.vals.ai/benchmarks/emb-v1-1
- https://www.vals.ai/benchmarks/terminal-bench-4
- https://www.vals.ai/benchmarks/legal_research
- https://www.vals.ai/benchmarks/tax_agent_bench
- https://www.vals.ai/models/anthropic_claude-fable-5-2
- https://www.vals.ai/models/google_gemini-4-carbon
- https://www.vals.ai/models/google_gemini-4-hydrogen
- https://www.vals.ai/models/openai_gpt-6.1-terra
- https://www.vals.ai/models/meta_muse-ember

## Benchmark separation and sourcing rules

- Different benchmark versions and harnesses keep distinct `benchmarkId` slugs: `aa-intelligence-index-v4-3` vs `aa-intelligence-index-v5-0`; `vals-index` (Oct 13 Argon card) vs `vals-index-v2-2`; `vals-finance-v2` vs `vals-finance-v2-1`; `terminal-bench-2-1` vs `terminal-bench-4.0` vs `terminal-bench-4.0-aa` vs `terminal-bench-4-0-vals` vs `terminal-bench-4-1`; `automationbench` (Zapier) vs `automationbench-aa` vs `automation-bench-v1-0-6`; `osworld-2.0-offline` vs `osworld-2-1-offline` vs `osworld-2-1-partial`; `programbench` vs `programbench-binary`.
- `data/figures.json` is rewritten by `python build.py` from `data/harnesses/`. Every figure in Revision 3 has `readDirectly: true`.
- The GPT-6.1 Sol DeepSWE value 75.2 remains `derived` (68.8 + 6.4 points stated by OpenAI on 29 Sep 2026).

## Name gaps on CursorBench

GPT-6 Astra, GPT-6 Sol, GPT-6.1 Sol, GPT-6.1 Terra, GPT-6 Luna, Muse Wonder Full, Muse Ember, Muse Spark Open, and Kimi K3.1 Pro had no row on the 12 Nov 2026 CursorBench 4.0 board. Those gaps remain empty, not zero.
