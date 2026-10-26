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
