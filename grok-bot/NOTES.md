Written on: cloud · grok-bot · 2026-10-26

# Grok Bot compilation notes

- Harness: grok-bot (display name: Grok Bot (Research Bot))
- Model: Grok Bot
- Computer: cloud (Grok Bot box)
- Format: atlas.json uses grok-bot-atlas-v1. index.html is built by build.py from the same records; data.json was removed on 2026-10-13 with Micah's approval.

First pass compiled 2026-10-13, independently of other harnesses. Weekly update 2026-10-26 covers releases and results from Oct 13 to Oct 26, 2026; see CHANGES.md for every added record and its source.

## Sources: first-hand vs second-hand

205 records from 26 source pages (144 on 2026-10-13, plus 61 new on 2026-10-26).

First-hand (page opened with WebFetch or curl): 14 pages, 97 records.
- Artificial Analysis, Gemini 4 Argon article (2026-09-30): 13 records
- SpaceXAI Grok 4.7 post (2026-09-21): 12 records. Opened on 2026-10-26; all 12 values match what was filed on 2026-10-13, so these moved from second-hand to first-hand.
- Artificial Analysis, Kimi K3.1 Pro launch article (2026-10-23): 12 records (new)
- Arena text leaderboard, snapshot read 2026-10-22: 12 records (new)
- Meta, Muse Spark Open model page (2026-10-15): 11 records (new)
- Artificial Analysis, HealthBench Professional article (2026-10-19): 10 records (new)
- Artificial Analysis, Benchmarking Grok 4.7 (2026-09-21): 6 records
- Moonshot AI, Kimi K3.1 Pro blog (2026-10-23): 5 records (new)
- Artificial Analysis, FrontierCode article (2026-10-12): 5 records (new)
- Artificial Analysis, Claude Fable 5.1 article (2026-09-01): 4 records
- Artificial Analysis, Decision Index (2026-10-13), AA-Robotics (2026-10-14), AA-3D (2026-10-12): 2 records each (new)
- Artificial Analysis, Reflection Beam article (2026-10-16): 1 record (new; Muse Spark Open's AA Intelligence Index)

Second-hand: 12 pages, 108 records (read_myself = false).
- Taken from web search result excerpts of the primary page, page not opened: Google DeepMind Argon model card (73), Artificial Analysis Muse Wonder article (11), OpenAI GPT-6.1 Sol system card addendum (3), Google Argon blog (1), Anthropic Opus page (1).
- Relayed by aggregators citing a primary source: BenchLM (6), Tokens or Towers (5), BenchmarkList (5), Benchmark Heaven (1), Apidog (1).
- One record filed under the opened AA Argon article (Claude Fable 5.1, AA Intelligence Index v4.3 = 53) is not stated on that page; the value came from a search summary. atlas.json marks it second-hand and unconfirmed. Still unconfirmed on 2026-10-26. The chart on index.html shows this value without the flag.

By publisher_type: claim 59, rival table 62, independent 84. Unclassified: 0.

## How Micah's model names were interpreted

- "Gemini 4 Argon": Google's Gemini 4 Argon (GA Oct 13, 2026; AA tested a limited rollout Sep 30).
- "ChatGPT 6.1 ... as well as Astra": GPT-6.1 Sol (the only GPT-6.1 model found) plus GPT-6 Astra. No GPT-6.1 Astra exists in what I found. GPT-6 Sol included as context; GPT-6 Luna is name only.
- "Cursor with Grok 4.7": Grok 4.7 from SpaceXAI (xAI). There is no Cursor variant; the only Cursor link is xAI's self-reported CursorBench 4.0 score (46.3%).
- "Claude 5.5 set of models": Claude Opus 5.5 (Sep 22). Sonnet 5.5 (Sep 28) and Haiku 5.5 (Oct 7) are partial; dates are from the Anthropic newsroom, read 2026-10-26.
- "5.1 Fable": Claude Fable 5.1.
- "The new Muse models": Meta's Muse Wonder and Muse Wonder Full (Oct 12, 2026), plus Muse Spark Open (Oct 15, 2026, added 2026-10-26). Muse Spark 1.3 (Sep 2, 2026, per Meta's research blog) is partial.
- Added on 2026-10-26 as a major new entrant: Kimi K3.1 Pro from Moonshot AI (Oct 23, 2026). It is not one of Micah's named models; it is included because AA ranks it next to them.

## Not verified

- No scores found on SWE-bench Verified, ARC Prize (page is rendered by JavaScript and could not be read), Epoch AI, Scale SEAL, GPQA Diamond, AIME, or MMMU for these models.
- GPT-6 Luna release date is still not verified. GPT-6 Astra's Sep 3 date comes from a search summary.
- Gemini 4 Argon model card numbers (73 records) are still second-hand.
- Arena scores are a live leaderboard snapshot read 2026-10-22, with each model's listed reasoning setting. They will change.
- Muse Spark Open units: Meta's table prints bare numbers. Rows are filed as % except the GDPval-AA Elo and AA-Omniscience Index rows.
- AA FrontierCode: GPT-6 Astra is described only as "2 points below" GPT-6.1 Sol. That value is not recorded, because it would be derived.
- Benchmark names outside Google's table may be normalized from the publisher's wording; each such record says so in its note.
- AutomationBench (Zapier) and AutomationBench-AA are different variants and should not be compared directly. Terminal-Bench 2.1 (Meta table) and Terminal-Bench 4.0 are separate benchmarks.

## Changes on 2026-10-26

- New models: Muse Spark Open (Meta, Oct 15) and Kimi K3.1 Pro (Moonshot AI, Oct 23).
- 61 new records: AA index and evaluation results, the Arena text leaderboard, Meta's Muse Spark Open table, and Moonshot's Kimi K3.1 Pro claims.
- Release dates filled in from the labs' own pages: Sonnet 5.5, Haiku 5.5, Muse Spark 1.3.
- Opus 5.5 AA Intelligence Index 58 is now sourced to AA directly (Kimi K3.1 Pro article), replacing Tokens or Towers.
- The 12 SpaceXAI Grok 4.7 post records were confirmed on the page and are now first-hand.
- 3 new claim-vs-independent pairs: Kimi K3.1 Pro Terminal-Bench 4.0, GPT-6.1 Sol HealthBench Professional, and GPT-6.1 Sol HealthBench.
- build.py fix: the ECharts embed now reads the local file as text, or falls back to the 5.6.0 CDN copy decoded. The old line failed in both branches.
- template.html: hero text and data date updated, timeline axis extended to Oct 31, and colors added for new models.
- shots/ re-rendered from the new index.html.
- No new frontier models from Google, OpenAI, Anthropic, or xAI between Oct 13 and Oct 26.
