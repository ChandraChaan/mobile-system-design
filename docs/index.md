# Mobile System Design

**Worked case studies for mobile system design interviews and real projects: payments, wearables, chat, feeds, live tracking, uploads and safe releases.**

Most system design material is about servers. Mobile rounds ask different questions: what happens when the app is killed mid-payment, how a wearable's data reaches the cloud exactly once, how a chat stays in order on a train with no signal. This guide answers them with diagrams, data models, APIs and failure modes, the way you'd explain them in an interview.

## Start here

1. **[The framework](framework.md):** the seven steps to follow in any mobile design round, and the mistakes to avoid.
2. **[Building blocks](building-blocks.md):** offline-first reads, the outbox, conflicts, real-time updates, pagination, caching, tokens and background work. Every case study reuses these.
3. **[Cheat sheet](cheatsheet.md):** one page for the night before.

## Case studies

| Case study | Difficulty | You'll practise |
|---|---|---|
| [UPI payments app](case-studies/upi-payments-app.md) | 🔴 Senior | Payment state machines, idempotency, reconciliation, device binding |
| [Wearable health-data sync](case-studies/wearable-health-sync.md) | 🔴 Senior | Bluetooth LE, background limits, deduplication, time zones, HealthKit and Health Connect |
| [Offline-first chat](case-studies/offline-first-chat.md) | 🟡 Mid – 🔴 Senior | Outbox, ordering with sequence numbers, receipts, sockets and push |
| [Infinite news feed](case-studies/news-feed.md) | 🟢 Junior – 🟡 Mid | Cursor pagination, images, video, smooth lists, optimistic likes |
| [Live ride tracking](case-studies/live-ride-tracking.md) | 🔴 Senior | Location streams, trip state, smooth maps, battery |
| [Resumable video upload](case-studies/resumable-video-upload.md) | 🟡 Mid – 🔴 Senior | S3 multipart upload, presigned URLs, background transfers |
| [Feature flags and staged rollouts](case-studies/feature-flags-and-rollouts.md) | 🟡 Mid – 🔴 Senior | Remote config, kill switches, experiments, forced updates |

Every case study has the same sections: **requirements, estimates, architecture, data model, API, deep dives, failure modes, trade-offs and interview follow-ups.** Read the requirements, close the page, sketch your own design, then compare.

## Who it's for

- Mobile engineers (Flutter, Android, iOS, React Native) preparing for senior and staff interviews
- Interviewers who want consistent questions and a reference answer
- Teams designing features like these for real

The designs are platform-neutral, with notes for Android, iOS and Flutter where the platforms differ.

## Related

- [Flutter Architect Handbook](https://github.com/ChandraChaan/flutter-architect-handbook): 67 interview questions from Dart basics to architecture and leadership
- [flutter-production-starter](https://github.com/ChandraChaan/flutter-production-starter): a template app that applies many of these patterns
