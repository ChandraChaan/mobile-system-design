# Contributing

Thanks for helping make this guide better. Corrections, clearer explanations, better trade-offs and new case studies are all welcome.

## Small fixes

Typos, wrong numbers, broken diagrams or a platform detail that has changed: open a pull request directly. Please say where the correct information comes from (documentation, a spec, or your production experience).

## Disagreeing with a design

There's rarely one right design. If you'd make a different trade-off, open a [discussion](https://github.com/ChandraChaan/mobile-system-design/discussions) first. Good alternatives get added to the case study's **Trade-offs** section, credited to you.

## New case studies

Open an issue with the prompt (one or two sentences, as an interviewer would say it) before writing. A case study must:

- Start with `# Design …`, then a quoted prompt and a `**Difficulty:**` line
- Have exactly these sections, in order: Requirements, Estimates, Architecture, Data model, API, Deep dives, Failure modes, Trade-offs, Interview follow-ups
- Include at least two Mermaid diagrams and a failure-mode table
- Focus on the **client**: what the app does, stores and survives. Keep the backend at the level of boxes unless the design depends on it
- Be original writing, not copied from books, courses or other repositories
- Be added to `README.md`, `docs/index.md` and the `nav` in `mkdocs.yml`

## Checking your change

```bash
python scripts/check_docs.py          # template, links, navigation
pip install -r requirements.txt
mkdocs serve                          # preview at http://127.0.0.1:8000
mkdocs build --strict                 # what CI runs
```

CI also renders every Mermaid diagram, so a syntax error fails the build.

## Style

- Plain, direct English. Short sentences. Explain jargon the first time you use it.
- Numbers in estimates should change a decision; say which one.
- Prefer tables for comparisons and failure modes.
