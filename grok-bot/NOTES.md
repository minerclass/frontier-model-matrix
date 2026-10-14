Written on: cloud · grok-bot · 2026-10-13

# Grok Bot compilation notes

- Harness: grok-bot (display name: Grok Bot (Research Bot))
- Model: Grok Bot
- Computer: cloud (Grok Bot box)
- Format: atlas.json uses grok-bot-atlas-v1. index.html is built by build.py from the same records; data.json was removed on 2026-10-13 with Micah's approval.

This is a first pass, compiled independently before seeing any other harness's results.

## Sources: first-hand vs second-hand

144 records from 15 source pages.

First-hand (opened with WebFetch during compilation): 3 pages, 23 records.
- Artificial Analysis, Gemini 4 Argon article (2026-09-30): 13 records
- Artificial Analysis, Claude Fable 5.1 article (2026-09-01): 4 records
- Artificial Analysis, Benchmarking Grok 4.7 (2026-09-21): 6 records

Second-hand: 12 pages, 121 records (read_myself = false).
- Taken from web search result excerpts of the primary page, page not opened: Google DeepMind Argon model card (73), SpaceXAI Grok 4.7 post (12), Artificial Analysis Muse Wonder article (11), OpenAI GPT-6.1 Sol system card addendum (3), Google Argon blog (1), Anthropic Opus page (1).
- Relayed by aggregators citing a primary source: BenchLM (6), Tokens or Towers (6), BenchmarkList (5), Benchmark Heaven (1), Apidog (1).
- One record filed under the opened AA Argon article (Claude Fable 5.1, AA Intelligence Index v4.3 = 53) is not stated on that page; the value came from a search summary. atlas.json marks it second-hand and unconfirmed. The legacy chart on index.html still shows this value without the flag.

By publisher_type: claim 45, rival table 60, independent 39. Unclassified: 0.

## How Micah's model names were interpreted

- "Gemini 4 Argon": Google's Gemini 4 Argon (GA Oct 13, 2026; AA tested a limited rollout Sep 30).
- "ChatGPT 6.1 ... as well as Astra": GPT-6.1 Sol (the only GPT-6.1 model found) plus GPT-6 Astra. No GPT-6.1 Astra exists in what I found. GPT-6 Sol included as context; GPT-6 Luna is name only.
- "Cursor with Grok 4.7": Grok 4.7 from SpaceXAI (xAI). There is no Cursor variant; the only Cursor link is xAI's self-reported CursorBench 4.0 score (46.3%).
- "Claude 5.5 set of models": Claude Opus 5.5. Sonnet 5.5 is partial (two AA figures). Haiku 5.5 is name only.
- "5.1 Fable": Claude Fable 5.1.
- "The new Muse models": Meta's Muse Wonder and Muse Wonder Full (Oct 12, 2026). Muse Spark 1.3 is partial (one AA index figure).

## Not verified

- No scores found on LMArena, SWE-bench Verified, ARC Prize, Epoch AI, Scale SEAL, GPQA Diamond, AIME, or MMMU for these models.
- No independent figures for GPT-6 Sol, GPT-6 Luna, or Claude Haiku 5.5.
- Release dates not verified for Sonnet 5.5, Haiku 5.5, GPT-6 Luna, Muse Spark 1.3. GPT-6 Astra's Sep 3 date comes from a search summary.
- Claude Opus 5.5 AA Intelligence Index (58) is from Tokens or Towers, not AA directly.
- Benchmark names outside Google's table may be normalized from the publisher's wording; each such record says so in its note.
- AutomationBench (Zapier) and AutomationBench-AA are different variants and should not be compared directly.
