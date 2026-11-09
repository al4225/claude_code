# Vault rules (read by Claude Code when started in this folder)

This is a research knowledge base for statistical genetics. Notes are plain Markdown with Obsidian `[[wikilinks]]`.

## Layout
- `raw/`: original files and their MarkItDown conversions. **Never edit files in raw/.**
- `papers/`: one note per paper, named `<firstauthor><year>_<keyword>.md`, using the paper template below.
- `concepts/`: one note per method or idea (e.g. [[fine-mapping]], [[LD-mismatch]]). Short; link out to papers.
- `projects/<name>/`: `log.md` (dated entries, newest first), `decisions.md`, `handoff.md`.
- `meetings/`: one note per meeting, `YYYY-MM-DD-<type>.md`, using the meeting template below.
- `outputs/`: answers to questions asked of the vault, saved so they can be reused.
- `Home.md`: index. Add every new note to it.

## Rules
- Link every new note to at least one existing note with `[[wikilinks]]`. Create a concept note if a link target doesn't exist.
- When answering "what do we know about X": search `papers/`, `concepts/`, `projects/`, `meetings/` first, cite note names as `[[note]]`, and say clearly when something is NOT in the vault.
- Paper facts (authors, year, journal, claims) must come from the paper itself. If unsure, write `TODO: verify`.
- People in meeting notes are referred to by role.
- When a meeting creates a decision, also append it to the relevant `projects/<name>/decisions.md`.

## Paper note template
```
---
type: paper
year:
tags: []
---
# <Title>
**Citation**:
**Question**:
**Method**: model, assumptions, inference
**Data**:
**Key result**:
**Relevance to our work**:
**Limitations / open questions**:
**Related**: [[...]]
```

## Meeting note template
```
---
type: meeting
date:
source: raw/<file>
---
# <Meeting> YYYY-MM-DD
## Summary (3 bullets)
## Discussion (by topic, with [[links]])
## Decisions
## Action items
- [ ] <owner>: <task> (due)
```
