# Changes: 2026-11-09 weekly update

Window: Nov 2 to Nov 9, 2026. Every new row was read on the source page on 2026-11-09 (first-hand). No values were estimated, derived, or averaged. 301 records total, 40 new.

## Releases checked

- OpenAI: **GPT-6 Cyber** (Nov 5, cybersecurity model, select approved Daybreak Red customers via API and Codex) added, with OpenAI figures and Irregular's independent evaluation.
- Google: no new Gemini language model (Gemini Omni 1.2 Flash on Nov 5 is a video model, out of scope).
- Anthropic: no new model (newsroom read 2026-11-09; latest model items are Opus 5.5, Sonnet 5.5, Haiku 5.5).
- xAI/SpaceXAI: no new model (x.ai/news read 2026-11-09; latest is Grok 4.7).
- Meta: no new Muse model. Nov 6 post on specialized Muse models for Muse and Meta AI has no benchmark numbers in the text read, so nothing added.
- New entrants: **Inkling 2 Small** (Thinking Machines, Nov 5, proprietary at launch) added from the Artificial Analysis article. Not added: Tencent Hy4 (Nov 4), Baidu ERNIE 5.5 Flash Base (Nov 5), Kimi K3.1 Pro Highspeed (no benchmark pages opened).

## New independent results (Artificial Analysis)

- VIALS-AA launch (Nov 6): Carbon 64, Astra 63, Opus 5.5 61, Sonnet 5.5 60, GPT-6.1 Sol 59, Kimi K3.1 Pro 45 (pass^3). Terra, Luna, Argon, Grok scores are not stated in the article text, so none recorded.
- Decision Index v2 (Nov 8): Claude Haiku 5.5 77, GPT-6 Luna 76. v2 is a new composite; v1.0 values (61, 55) stay under their own name.
- Inkling 2 Small article (Nov 5): 12 records for Inkling 2 Small, plus three Sonnet 5.5 (medium) figures quoted in it.

## Other changes

- template.html: hero text, data date, timeline range, colors for the two new models. shots/ were not re-rendered.
- Not recorded: GPT-6 Astra ExploitGym 42.43 (search summary only); CyScenarioBench Astra average (only a 7 point gap is stated).


# Changes: 2026-11-02 weekly update

Window: Oct 26 to Nov 2, 2026. Every new row was read on the source page on 2026-11-02 (first-hand). No values were estimated, derived, or averaged. Settings are listed as the source gives them.

## Releases checked

- Google: **Gemini 4 Carbon** (announced Oct 28, limited access for selected cyber defenders and Fairwind Program partners) added. Genie 4 (Oct 27, world model research preview) is out of scope.
- OpenAI: **GPT-6.1 Terra** (Oct 26, ChatGPT Work, Codex, API) added. A Cleus blog post reports OpenAI cancelled a planned GPT-6.1 Astra release; not confirmed on an OpenAI page, so it is only noted under Not found.
- Anthropic: no new model (newsroom read 2026-11-02; latest items are the S-1 filing Oct 26 and a drug-development post Oct 27).
- xAI/SpaceXAI: no new model (x.ai/news read 2026-11-02).
- Meta: no new Muse model (Muse agent launched in Singapore; NVIDIA partnership news Oct 27).
- New entrants: Mistral Large 4 weights (Oct 29) checked and not added. A secondary roundup (clone-systems.com) lists the Large 4 preview at an independent score of 38, well below the tracked models; not confirmed on AA.

## Other changes

- Artificial Analysis launched Intelligence Index v5 on Oct 27 (new benchmarks FrontierCode 2.0 and Terminal-Bench-Science; HLE-Diamond, AA-Omniscience v1.1, and CritPt v2 hard subset replace older versions). v5 scores are filed under a separate benchmark name and are not comparable with v4.3.
- No new claim vs independent pairs: the Terra launch post's comparisons are mostly relative, and AA gives no matching absolute value for Terra's Terminal-Bench 4.0 claim (50.3).
- Opus 5.5 FrontierCode figure in the AA Carbon article (56%) was not recorded, because the sentence does not say whether it refers to Terminal-Bench 4.0 or FrontierCode v1.1.
- template.html: hero text, data date, timeline range, method note on index versions, and colors for the two new models. shots/ were not re-rendered.

## New records (56)

| Model | Benchmark | Value | Unit | Publisher (type) | Setting | Source | Date | First-hand |
|---|---|---|---|---|---|---|---|---|
| gemini-4-carbon | SEC-bench Pro | 88.2 | % | Google (claim) | evaluated without guardrails; Google calls it state of the art | https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/ | 2026-10-28 | yes |
| gemini-4-carbon | ExploitGym | 54.8 | % | Google (claim) | evaluated without guardrails | https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/ | 2026-10-28 | yes |
| gemini-4-carbon | CWE-bench (Collinear) | 71.0 | % | Google (claim) | evaluated without guardrails | https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/ | 2026-10-28 | yes |
| gemini-4-carbon | WebDev Arena (Elo) | 1768 | Elo | Google (claim) | Google says #4 on WebDev Arena, +89 Elo | https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/ | 2026-10-28 | yes |
| gemini-4-carbon | Gray Swan IPI attack success rate (lower better) | 0.0 | % | Google (claim) | Gray Swan Indirect Prompt Injection benchmark | https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/ | 2026-10-28 | yes |
| gpt-6-1-terra | Terminal-Bench 4.0 | 50.3 | % | OpenAI (claim) | max reasoning effort | https://openai.com/index/introducing-gpt-6-1-terra | 2026-10-26 | yes |
| gpt-6-1-terra | OpenAI internal error-inducing prompts, error rate (lower better) | 16.7 | % | OpenAI (claim) | low reasoning effort | https://openai.com/index/introducing-gpt-6-1-terra | 2026-10-26 | yes |
| gpt-6-1-terra | OpenAI internal error-inducing prompts, error rate (lower better) | 4.3 | % | OpenAI (claim) | max reasoning effort | https://openai.com/index/introducing-gpt-6-1-terra | 2026-10-26 | yes |
| gemini-4-carbon | AA Intelligence Index v5 | 59 | index | Artificial Analysis (independent) | high | https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1 | 2026-10-28 | yes |
| gemini-4-carbon | AA Coding Agent Index | 59 | index | Artificial Analysis (independent) | high, Antigravity CLI | https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1 | 2026-10-28 | yes |
| claude-opus-5-5 | AA Coding Agent Index | 62 | index | Artificial Analysis (independent) | max, Claude Code | https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1 | 2026-10-28 | yes |
| gemini-4-carbon | Terminal-Bench 4.0 | 64 | % | Artificial Analysis (independent) | high | https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1 | 2026-10-28 | yes |
| gemini-4-carbon | FrontierCode 1.1 (AA) | 51 | % | Artificial Analysis (independent) | high | https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1 | 2026-10-28 | yes |
| gemini-4-carbon | AA-Briefcase (Elo) | 1609 | Elo | Artificial Analysis (independent) | high | https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1 | 2026-10-28 | yes |
| gemini-4-argon | AA-Briefcase (Elo) | 1483 | Elo | Artificial Analysis (independent) | high | https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1 | 2026-10-28 | yes |
| grok-4-7 | AA-Briefcase (Elo) | 1638 | Elo | Artificial Analysis (independent) | xhigh | https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1 | 2026-10-28 | yes |
| muse-wonder | AA-Briefcase (Elo) | 1659 | Elo | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1 | 2026-10-28 | yes |
| kimi-k3-1-pro | AA-Briefcase (Elo) | 1678 | Elo | Artificial Analysis (independent) |  | https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1 | 2026-10-28 | yes |
| gemini-4-carbon | AA-Omniscience v1.1 Index | 54 | index | Artificial Analysis (independent) | high | https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1 | 2026-10-28 | yes |
| gemini-4-argon | AA-Omniscience v1.1 Index | 46 | index | Artificial Analysis (independent) | high | https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1 | 2026-10-28 | yes |
| gemini-4-carbon | AA-Omniscience v1.1 accuracy | 58 | % | Artificial Analysis (independent) | high | https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1 | 2026-10-28 | yes |
| gemini-4-carbon | AA-Omniscience v1.1 hallucination rate (lower better) | 11 | % | Artificial Analysis (independent) | high | https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1 | 2026-10-28 | yes |
| gemini-4-argon | AA-Omniscience v1.1 hallucination rate (lower better) | 4 | % | Artificial Analysis (independent) | high | https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1 | 2026-10-28 | yes |
| claude-opus-5-5 | AA-Omniscience v1.1 hallucination rate (lower better) | 50 | % | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1 | 2026-10-28 | yes |
| gpt-6-astra | AA-Omniscience v1.1 hallucination rate (lower better) | 50 | % | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1 | 2026-10-28 | yes |
| gpt-6-1-terra | AA Coding Agent Index v2.0 | 48 | index | Artificial Analysis (independent) | best setting reported | https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier | 2026-10-26 | yes |
| gpt-6-1-sol | AA Coding Agent Index v2.0 | 54 | index | Artificial Analysis (independent) |  | https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier | 2026-10-26 | yes |
| gpt-6-luna | AA Coding Agent Index v2.0 | 31 | index | Artificial Analysis (independent) |  | https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier | 2026-10-26 | yes |
| gpt-6-1-terra | AA-Omniscience hallucination rate (lower better) | 38 | % | Artificial Analysis (independent) |  | https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier | 2026-10-26 | yes |
| claude-opus-5-5 | AA Intelligence Index v5 | 58 | index | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| gpt-6-astra | AA Intelligence Index v5 | 57 | index | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| gpt-6-1-sol | AA Intelligence Index v5 | 55 | index | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| gemini-4-argon | AA Intelligence Index v5 | 50 | index | Artificial Analysis (independent) | high | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| kimi-k3-1-pro | AA Intelligence Index v5 | 46 | index | Artificial Analysis (independent) | weights not yet released | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| claude-haiku-5-5 | AA Intelligence Index v5 | 36 | index | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| claude-opus-5-5 | AA Intelligence Index v5 | 35 | index | Artificial Analysis (independent) | low effort | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| claude-opus-5-5 | FrontierCode 2.0 (AA) | 46 | % | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| gpt-6-astra | FrontierCode 2.0 (AA) | 42 | % | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| gpt-6-1-terra | FrontierCode 2.0 (AA) | 42 | % | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| claude-sonnet-5-5 | FrontierCode 2.0 (AA) | 42 | % | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| gpt-6-astra | Terminal-Bench-Science (AA) | 63 | % | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| claude-opus-5-5 | Terminal-Bench-Science (AA) | 59 | % | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| gpt-6-1-sol | Terminal-Bench-Science (AA) | 58 | % | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| kimi-k3-1-pro | Terminal-Bench-Science (AA) | 34 | % | Artificial Analysis (independent) |  | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| claude-haiku-5-5 | Terminal-Bench-Science (AA) | 20 | % | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| claude-opus-5-5 | HLE-Diamond (AA) | 68 | % | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| gpt-6-astra | HLE-Diamond (AA) | 64 | % | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| claude-fable-5-1 | HLE-Diamond (AA) | 60 | % | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| kimi-k3-1-pro | HLE-Diamond (AA) | 37 | % | Artificial Analysis (independent) |  | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| gpt-6-astra | CritPt v2 hard subset (AA) | 72 | % | Artificial Analysis (independent) | high | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| gpt-6-1-sol | CritPt v2 hard subset (AA) | 69 | % | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| claude-opus-5-5 | CritPt v2 hard subset (AA) | 61 | % | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| kimi-k3-1-pro | CritPt v2 hard subset (AA) | 45 | % | Artificial Analysis (independent) |  | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| claude-opus-5-5 | AA-Omniscience v1.1 Index | 48 | index | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| claude-sonnet-5-5 | AA-Briefcase (Elo) | 1812 | Elo | Artificial Analysis (independent) |  | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |
| muse-wonder-full | GDP.pdf (all-pass) | 33 | % | Artificial Analysis (independent) |  | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5 | 2026-10-27 | yes |

# Changes: 2026-10-26 weekly update

Window: Oct 13 to Oct 26, 2026. Every row was read on the source page on 2026-10-26 (first-hand) unless marked otherwise. No values were estimated or averaged. Settings are listed as the source gives them.

## Releases checked

- Google: no new frontier model. Gemini 4 Argon went GA on Oct 13 (already tracked).
- OpenAI: no new model in the news feed through Oct 23. The Decisions API (Oct 22) is a product, not a model.
- Anthropic: no new model through Oct 26. Newsroom confirms Sonnet 5.5 (Sep 28) and Haiku 5.5 (Oct 7).
- xAI/SpaceXAI: only Grok Voice 3.0 (Oct 14), which is out of scope.
- Meta: **Muse Spark Open** (Oct 15) added.
- New entrant: **Kimi K3.1 Pro** (Moonshot AI, Oct 23) added. Reflection Beam and Nemotron 3.5 were checked and not added, because they are not frontier-tier on AA.

## Other changes

- Opus 5.5 AA Intelligence Index 58: re-sourced from Tokens or Towers (second-hand) to the AA Kimi K3.1 Pro article (first-hand, 2026-10-23). The value is unchanged.
- SpaceXAI Grok 4.7 post (12 records): page opened, all values matched, and the records now count as first-hand.
- Release dates: Sonnet 5.5 2026-09-28, Haiku 5.5 2026-10-07 (anthropic.com/news), and Muse Spark 1.3 2026-09-02 (research.meta.ai).
- New pairs: Kimi K3.1 Pro Terminal-Bench 4.0 (claim 65.7, Claude-Code harness, vs AA 67), GPT-6.1 Sol HealthBench Professional (claim 64.2 vs AA length-adjusted 65.1), and GPT-6.1 Sol HealthBench (claim 58.5 vs AA 58.5). The claim and AA settings differ, so they are shown side by side, not merged.
- build.py: the ECharts embed bug is fixed. template.html: date, hero text, timeline range, and colors updated. shots/ re-rendered.

## New or re-sourced records (62: 61 new + the Opus 5.5 index re-source)

| Model | Benchmark | Value | Unit | Publisher (type) | Setting | Source | Date | First-hand |
|---|---|---|---|---|---|---|---|---|
| claude-opus-5-5 | AA Intelligence Index v4.3 | 58 | index | Artificial Analysis (independent) | max with fallback; confirmed on AA Kimi K3.1 Pro article (2026-10-23). Previously sourced second-hand from Tokens or Towers. | https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks | 2026-10-23 | yes |
| claude-sonnet-5-5 | AA Intelligence Index v4.3 | 56 | index | Artificial Analysis (independent) | max with fallback | https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks | 2026-10-23 | yes |
| kimi-k3-1-pro | AA Intelligence Index v4.3 | 55 | index | Artificial Analysis (independent) | reasoning model, AA launch test | https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks | 2026-10-23 | yes |
| muse-spark-open | AA Intelligence Index v4.3 | 39 | index | Artificial Analysis (independent) | value quoted in AA Beam article | https://artificialanalysis.ai/articles/reflection-beam | 2026-10-16 | yes |
| kimi-k3-1-pro | GDPval-AA (Elo) | 1846 | Elo | Artificial Analysis (independent) |  | https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks | 2026-10-23 | yes |
| claude-opus-5-5 | GDPval-AA (Elo) | 1866 | Elo | Artificial Analysis (independent) | max with fallback (quoted in Kimi article) | https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks | 2026-10-23 | yes |
| kimi-k3-1-pro | Terminal-Bench 4.0 | 67 | % | Artificial Analysis (independent) | AA harness; AA calls it the highest score of any model on Terminal-Bench 4.0 | https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks | 2026-10-23 | yes |
| kimi-k3-1-pro | AutomationBench-AA | 73 | % | Artificial Analysis (independent) |  | https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks | 2026-10-23 | yes |
| kimi-k3-1-pro | Humanity's Last Exam | 52 | % | Artificial Analysis (independent) |  | https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks | 2026-10-23 | yes |
| kimi-k3-1-pro | CritPt | 25 | % | Artificial Analysis (independent) |  | https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks | 2026-10-23 | yes |
| kimi-k3-1-pro | SciCode | 61 | % | Artificial Analysis (independent) |  | https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks | 2026-10-23 | yes |
| kimi-k3-1-pro | AA-Omniscience hallucination rate (lower better) | 44 | % | Artificial Analysis (independent) |  | https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks | 2026-10-23 | yes |
| kimi-k3-1-pro | AA-Omniscience Index | 30 | index | Artificial Analysis (independent) |  | https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks | 2026-10-23 | yes |
| kimi-k3-1-pro | Terminal-Bench 4.0 | 65.7 | % | Moonshot AI (claim) | Claude-Code harness | https://www.kimi.ai/blog/kimi-k3-1-pro | 2026-10-23 | yes |
| kimi-k3-1-pro | BenchCAD | 92.7 | % | Moonshot AI (claim) | with tools | https://www.kimi.ai/blog/kimi-k3-1-pro | 2026-10-23 | yes |
| kimi-k3-1-pro | OfficeQA Pro v2 | 64.4 | % | Moonshot AI (claim) | Moonshot internal benchmark; Moonshot claims state of the art | https://www.kimi.ai/blog/kimi-k3-1-pro | 2026-10-23 | yes |
| claude-opus-5-5 | BenchCAD | 96.2 | % | Moonshot AI (rival table) | as reported in Moonshot launch post | https://www.kimi.ai/blog/kimi-k3-1-pro | 2026-10-23 | yes |
| gpt-6-astra | BenchCAD | 95.9 | % | Moonshot AI (rival table) | as reported in Moonshot launch post | https://www.kimi.ai/blog/kimi-k3-1-pro | 2026-10-23 | yes |
| gpt-6-astra | HealthBench Professional (AA, length-adjusted) | 66.0 | % | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/healthbench-professional-health-conversations | 2026-10-19 | yes |
| gpt-6-1-sol | HealthBench Professional (AA, length-adjusted) | 65.1 | % | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/healthbench-professional-health-conversations | 2026-10-19 | yes |
| claude-sonnet-5-5 | HealthBench Professional (AA, length-adjusted) | 63.0 | % | Artificial Analysis (independent) | max with fallback | https://artificialanalysis.ai/articles/healthbench-professional-health-conversations | 2026-10-19 | yes |
| gpt-6-sol | HealthBench Professional (AA, length-adjusted) | 62.3 | % | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/healthbench-professional-health-conversations | 2026-10-19 | yes |
| gpt-6-luna | HealthBench Professional (AA, length-adjusted) | 61.9 | % | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/healthbench-professional-health-conversations | 2026-10-19 | yes |
| claude-opus-5-5 | HealthBench Professional (AA, length-adjusted) | 59.9 | % | Artificial Analysis (independent) | max with fallback; raw (unadjusted) score 71.4, highest raw score | https://artificialanalysis.ai/articles/healthbench-professional-health-conversations | 2026-10-19 | yes |
| claude-opus-5-5 | HealthBench Professional (AA, raw) | 71.4 | % | Artificial Analysis (independent) | max with fallback | https://artificialanalysis.ai/articles/healthbench-professional-health-conversations | 2026-10-19 | yes |
| claude-sonnet-5-5 | HealthBench (AA, length-adjusted) | 62.1 | % | Artificial Analysis (independent) | max with fallback | https://artificialanalysis.ai/articles/healthbench-professional-health-conversations | 2026-10-19 | yes |
| gpt-6-1-sol | HealthBench (AA, length-adjusted) | 58.5 | % | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/healthbench-professional-health-conversations | 2026-10-19 | yes |
| gpt-6-luna | HealthBench (AA, length-adjusted) | 54.6 | % | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/healthbench-professional-health-conversations | 2026-10-19 | yes |
| claude-opus-5-5 | FrontierCode 1.1 Main (AA) | 52 | % | Artificial Analysis (independent) | max with fallback; pass rate 58% | https://artificialanalysis.ai/articles/frontiercode | 2026-10-12 | yes |
| gpt-6-1-sol | FrontierCode 1.1 Main (AA) | 49 | % | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/frontiercode | 2026-10-12 | yes |
| claude-fable-5-1 | FrontierCode 1.1 Main (AA) | 49 | % | Artificial Analysis (independent) | max with fallback | https://artificialanalysis.ai/articles/frontiercode | 2026-10-12 | yes |
| gpt-6-luna | FrontierCode 1.1 Main (AA) | 42 | % | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/frontiercode | 2026-10-12 | yes |
| claude-opus-5-5 | FrontierCode 1.1 Main pass rate (AA) | 58 | % | Artificial Analysis (independent) | max with fallback | https://artificialanalysis.ai/articles/frontiercode | 2026-10-12 | yes |
| claude-haiku-5-5 | AA Decision Index v1.0 | 61 | index | Artificial Analysis (independent) | Low effort | https://artificialanalysis.ai/articles/artificial-analysis-decision-index | 2026-10-13 | yes |
| gpt-6-luna | AA Decision Index v1.0 | 55 | index | Artificial Analysis (independent) | Low effort | https://artificialanalysis.ai/articles/artificial-analysis-decision-index | 2026-10-13 | yes |
| gpt-6-astra | AA-Robotics v0.1 | 69 | score | Artificial Analysis (independent) | Codex, high effort | https://artificialanalysis.ai/articles/aa-robotics | 2026-10-14 | yes |
| gpt-6-1-sol | AA-Robotics v0.1 | 65 | score | Artificial Analysis (independent) | Codex, high effort | https://artificialanalysis.ai/articles/aa-robotics | 2026-10-14 | yes |
| claude-sonnet-5-5 | AA-3D (Elo) | 1194 | Elo | Artificial Analysis (independent) | max with fallback | https://artificialanalysis.ai/articles/aa-3d | 2026-10-12 | yes |
| muse-spark-1-3 | AA-3D (Elo) | 1035 | Elo | Artificial Analysis (independent) | max | https://artificialanalysis.ai/articles/aa-3d | 2026-10-12 | yes |
| gemini-4-argon | Arena Text (overall) | 1517 | Elo | Arena (LMArena) (independent) | Gemini 4 Argon (High) | https://arena.ai/leaderboard/text | 2026-10-22 | yes |
| claude-opus-5-5 | Arena Text (overall) | 1509 | Elo | Arena (LMArena) (independent) | Claude Opus 5.5 (High) | https://arena.ai/leaderboard/text | 2026-10-22 | yes |
| muse-wonder | Arena Text (overall) | 1509 | Elo | Arena (LMArena) (independent) | Muse Wonder (Max) | https://arena.ai/leaderboard/text | 2026-10-22 | yes |
| claude-fable-5-1 | Arena Text (overall) | 1503 | Elo | Arena (LMArena) (independent) | Claude Fable 5.1 (Max) | https://arena.ai/leaderboard/text | 2026-10-22 | yes |
| muse-spark-1-3 | Arena Text (overall) | 1496 | Elo | Arena (LMArena) (independent) | Muse Spark 1.3 (Max) | https://arena.ai/leaderboard/text | 2026-10-22 | yes |
| gpt-6-1-sol | Arena Text (overall) | 1480 | Elo | Arena (LMArena) (independent) | GPT-6.1 Sol (Max) | https://arena.ai/leaderboard/text | 2026-10-22 | yes |
| claude-sonnet-5-5 | Arena Text (overall) | 1478 | Elo | Arena (LMArena) (independent) | Claude Sonnet 5.5 (xHigh) | https://arena.ai/leaderboard/text | 2026-10-22 | yes |
| gpt-6-astra | Arena Text (overall) | 1476 | Elo | Arena (LMArena) (independent) | GPT-6 Astra (Max) | https://arena.ai/leaderboard/text | 2026-10-22 | yes |
| gpt-6-sol | Arena Text (overall) | 1459 | Elo | Arena (LMArena) (independent) | GPT-6 Sol (Max) | https://arena.ai/leaderboard/text | 2026-10-22 | yes |
| gpt-6-luna | Arena Text (overall) | 1442 | Elo | Arena (LMArena) (independent) | GPT-6 Luna (Max) | https://arena.ai/leaderboard/text | 2026-10-22 | yes |
| grok-4-7 | Arena Text (overall) | 1441 | Elo | Arena (LMArena) (independent) | Grok 4.7 (xHigh) | https://arena.ai/leaderboard/text | 2026-10-22 | yes |
| claude-haiku-5-5 | Arena Text (overall) | 1425 | Elo | Arena (LMArena) (independent) | Claude Haiku 5.5 (High) | https://arena.ai/leaderboard/text | 2026-10-22 | yes |
| muse-spark-open | JobBench | 61.8 | % | Meta (claim) | xhigh | https://dev.meta.ai/models/muse-spark-open/ | 2026-10-15 | yes |
| muse-spark-open | MCP-Atlas | 89.2 | % | Meta (claim) | xhigh | https://dev.meta.ai/models/muse-spark-open/ | 2026-10-15 | yes |
| muse-spark-open | GDPval-AA v2 (Elo) | 1401 | Elo | Meta (claim) | xhigh | https://dev.meta.ai/models/muse-spark-open/ | 2026-10-15 | yes |
| muse-spark-open | HLE-Diamond (no tools) | 26.1 | % | Meta (claim) | xhigh | https://dev.meta.ai/models/muse-spark-open/ | 2026-10-15 | yes |
| muse-spark-open | SciCode | 58.5 | % | Meta (claim) | xhigh | https://dev.meta.ai/models/muse-spark-open/ | 2026-10-15 | yes |
| muse-spark-open | AA-Omniscience Index | 25 | index | Meta (claim) | xhigh | https://dev.meta.ai/models/muse-spark-open/ | 2026-10-15 | yes |
| muse-spark-open | Terminal-Bench 2.1 (Terminus 2 agent) | 76.4 | % | Meta (claim) | xhigh | https://dev.meta.ai/models/muse-spark-open/ | 2026-10-15 | yes |
| muse-spark-open | DeepSWE 1.1 (best available/self-reported harness) | 60 | % | Meta (claim) | xhigh | https://dev.meta.ai/models/muse-spark-open/ | 2026-10-15 | yes |
| muse-spark-open | ZeroBench | 50.0 | % | Meta (claim) | xhigh | https://dev.meta.ai/models/muse-spark-open/ | 2026-10-15 | yes |
| muse-spark-open | BabyVision | 80.2 | % | Meta (claim) | xhigh | https://dev.meta.ai/models/muse-spark-open/ | 2026-10-15 | yes |
| muse-spark-open | SimpleVQA | 73.6 | % | Meta (claim) | xhigh | https://dev.meta.ai/models/muse-spark-open/ | 2026-10-15 | yes |
