# Obsidian Demo Vault: Statistical Genetics Knowledge Base

A small, working Obsidian vault that Claude Code can read, search, and maintain. Open it in Obsidian to browse the linked notes and graph, and start `claude` inside it to ask questions or add notes.

Back to the guide: [AI_Research_Toolkit.md §1b](../../code/wiki/AI_Research_Toolkit.md#1b-obsidian-a-knowledge-base-your-ai-can-read)

> Paper notes summarize real papers (SuSiE, SuSiE-RSS, coloc, coloc+SuSiE). The lab meeting, project log, and results are **fictional demo data**.

## What's in here

```
obsidian_vault/
├── CLAUDE.md                 # rules for the AI: layout, templates, citation rules  ← start here
├── Home.md                   # index of every note
├── raw/
│   ├── lab_meeting_2026-10-27.docx   # original Word file (37 KB)
│   └── lab_meeting_2026-10-27.md     # MarkItDown output (1.2 KB), real conversion
├── papers/                   # 4 paper notes, same template
├── concepts/                 # fine-mapping, credible-set, colocalization, LD-mismatch, allele-harmonization
├── meetings/2026-10-27-lab-meeting.md   # AI-written from raw/ using the meeting template
├── projects/finemap-demo/    # log.md · decisions.md · handoff.md
└── outputs/                  # saved answers to questions asked of the vault ← example RESULTS
```

## The pipeline this vault shows

```
Word / PDF / PPT ──markitdown──▶ raw/*.md ──Claude + CLAUDE.md──▶ meetings/ papers/ concepts/ (linked)
                                                                      │
                                         "what do we know about X?" ◀─┘──▶ outputs/ (saved, cited answers)
```

1. **Convert**: `markitdown raw/lab_meeting_2026-10-27.docx -o raw/lab_meeting_2026-10-27.md`
2. **Structure**: Claude turned `raw/…md` into `meetings/2026-10-27-lab-meeting.md`, linked it to papers/concepts, and copied the decisions into `projects/finemap-demo/decisions.md` (all rules from `CLAUDE.md`).
3. **Query**: questions asked of the vault are saved in `outputs/` with the prompt in the front matter and every claim citing a `[[note]]`.

## Try it

**Browse (no AI):** Obsidian → *Open folder as vault* → select `examples/obsidian_vault`. Open `Home.md`, click links, open *Graph view*.

**Ask questions:**

```bash
cd examples/obsidian_vault
claude
```

```
How do we handle multiple causal variants in colocalization? Table with pros/cons, cite note names.
```
Compare with `outputs/2026-11-08_multiple-causal-variants.md`.

```
List every open action item across meetings/ and projects/, grouped by owner.
```
Compare with `outputs/2026-11-08_open-action-items.md`.

```
Why did block 412 have no credible sets, and what did we try? Answer only from the vault.
```

**Add something new (the "maintain" part):**

```bash
# convert any paper or notes you have (needs: pip install 'markitdown[all]')
markitdown ~/Downloads/some_paper.pdf -o raw/some_paper.md
```
```
Turn raw/some_paper.md into a paper note using the template in CLAUDE.md, link it to existing
concepts (create concept notes if needed), and add it to Home.md.
```

**Teach Claude Obsidian syntax (optional):** `npx skills add kepano/obsidian-skills`

## Things to notice

- **CLAUDE.md does the heavy lifting.** Templates and rules there are why the AI-written notes look consistent. Edit it to fit your own workflow.
- **Answers say what is NOT in the vault** (e.g. "No paper note for ColocBoost"). That rule in `CLAUDE.md` stops the AI from filling gaps with guesses.
- **MarkItDown isn't perfect:** in `raw/lab_meeting_2026-10-27.md` the Word table's header row came out as a data row under an empty header. Check converted tables before relying on them.
- Don't put controlled-access data (individual-level genotypes, PHI) in a vault you point a cloud AI at.
