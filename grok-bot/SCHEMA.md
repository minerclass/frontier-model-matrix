# Shared data.json schema

Every harness writes `harnesses/<name>/data.json`:

```json
{
  "harness": {"name": "grok-bot", "model": "", "run_date": "2026-10-13"},
  "as_of": "2026-10-13",
  "records": [
    {
      "model": "Gemini 4 Argon",
      "maker": "Google",
      "variant": "high",
      "benchmark": "Terminal-Bench 4.0",
      "score": 57.4,
      "unit": "%",
      "claim_type": "vendor",
      "setting": "high effort, vendor harness",
      "source_url": "https://...",
      "source_date": "2026-10-13",
      "retrieved_at": "2026-10-13T20:55:00-05:00",
      "notes": ""
    }
  ],
  "not_found": ["model or benchmark that could not be verified"]
}
```

- `claim_type`: `vendor` (the model's maker), `independent` (third-party evaluator), or `secondary` (aggregator or rival vendor citing someone else).
- `score`: a number, never estimated. Unverified values go in `not_found`, not as 0.
- Use model and benchmark names exactly as the source writes them, so the compare page can match them.
