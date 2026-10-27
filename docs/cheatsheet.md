# One-page cheat sheet

Read this the night before the interview.

## The order

1. **Clarify:** 3–4 features, then offline, freshness, scale, devices, security, battery.
2. **Estimate:** 2–3 numbers that change a decision.
3. **Architecture:** client layers (UI → state → repository → local DB + API + sync), backend as boxes.
4. **Data and API:** key entities with IDs, versions and status; the calls the app makes.
5. **Deep dives:** the hardest part, with failure modes.
6. **Cross-cutting:** security, observability, releases, accessibility, testing.
7. **Wrap up:** summary, biggest risk, what's next.

## Phrases that show seniority

- "The local database is the source of truth for the UI; the network only writes into it."
- "Every write carries an idempotency key created when the user acts, so retries are safe."
- "Push is a hint. When it arrives, we sync from our cursor."
- "Here's what happens if the app is killed right here…"
- "This ships behind a flag, because we can't roll back a mobile release."
- "I'd measure this on our cheapest supported phone, in release mode."

## Defaults to reach for

| Problem | Default |
|---|---|
| IDs for things created on the device | UUID v7 |
| Lists from the server | Cursor pagination, prefetch 5 items early |
| Offline writes | Outbox in the same DB transaction |
| Conflicts | Version per record, server rejects stale writes with 409 |
| Live data in the foreground | WebSocket + catch-up from cursor on reconnect |
| Background updates | Push → sync |
| Big uploads | Direct to object storage with presigned URLs, multipart, resumable |
| Images | CDN resizing, display-size decode, memory cache limited by bytes |
| Money | Integer minor units (paise), server-confirmed status, `unknown` state |
| Time | UTC + offset at recording time; server sequence for ordering |
| Tokens | Access token in memory, refresh token in Keychain/Keystore, single-flight refresh |
| Risky features | Flag, default off, staged rollout, kill switch |

## Numbers worth knowing

| | Rough value |
|---|---|
| One frame | 16 ms at 60 Hz, 8 ms at 120 Hz |
| Decoded image | width × height × 4 bytes |
| Feed post JSON | ~1–2 KB |
| Feed image at phone width | ~80–150 KB (WebP) |
| Chat message with metadata | ~200–500 bytes |
| BLE practical throughput | ~5–100 KB/s |
| S3 multipart | parts ≥ 5 MB (except the last), ≤ 10,000 parts |
| Requests per second | daily requests ÷ 86,400, × 3–5 for peak |

## Questions to ask the interviewer

- "Which matters more here: freshness or battery?"
- "Should writes work offline, or is read-only offline enough?"
- "What's the cheapest phone we need to support?"
- "Is there anything regulated in this data: money, health, children?"
