# AI Research Toolkit: Skills, Tools & Prompting Tips for StatGen

*Lab meeting, Nov 9, 2026*

This page continues [Claude_Code_User_Tips.md](Claude_Code_User_Tips.md). That page covers terminal setup, the Codex plugin, Humanize, and Remote Control. This page covers **how to work with AI across a research project**, from feeding it papers to shipping a figure-ready manuscript and slide deck.

The sections follow the order of a real project. Read top to bottom the first time; after that, use the [cheat sheet](#cheat-sheet).

```mermaid
flowchart LR
    A["0. Prompt well<br/>Altitude · Depth · Range"] --> B["1. Feed context<br/>MarkItDown"]
    B --> C["2. Plan<br/>OpenSpec"]
    C --> D["3. Verify<br/>Codex independent score"]
    D --> E["4. Hand off<br/>handoff.md"]
    E --> F["5. Reuse<br/>Skills · find-skills"]
    F --> G["6. Write<br/>statgen style · defensive · Humanizer"]
    G --> H["7. Present<br/>scientific-slides"]
```

---

## Overview

| # | Part | Tool / Tip | One-line pitch |
|---|------|-----------|----------------|
| 0 | [How to talk to AI](#0-how-to-talk-to-ai-altitude-depth-range) | Altitude / Depth / Range | Stop saying "you are an expert in X". Give it a goal, a workflow, and an outcome |
| 1 | [Feed context](#1-markitdown-any-file-to-markdown) | MarkItDown | PDF / Word / PPT / Excel → Markdown. Fewer tokens, better answers |
| 2 | [Plan](#2-openspec-spec-driven-development) | OpenSpec | Agree on a written spec before AI writes code |
| 3 | [Verify](#3-codex-review-independent-scoring) | Codex independent scoring | A second model scores the work against a rubric |
| 4 | [Continuity](#4-handoffmd-never-lose-context) | `handoff.md` | One file that lets a new session pick up where the last one stopped |
| 5a | [Reuse](#5a-make-it-a-skill) | Make it a skill | Turn a good session into a `/command` |
| 5b | [Reuse](#5b-find-skills--top-skills) | find-skills, top skills | Use skills other people already wrote |
| 6 | [Writing](#6-writing) | statgen-writing-style · defensive writing · Humanizer · ref verification | Write in lab style, stop GPT from watering down claims, sound human, cite real papers |
| 7 | [Present](#7-scientific-slides-talks-in-the-lab-style-beamerpdf-or-pptx) | scientific-slides | Papers → lab-style talk as Beamer/PDF or **editable** PPTX |
| 8 | [StatGen tips](#8-practical-tips-for-statgen-research) | HPC, big files, simulation checks, DUAs | Lessons from using AI on real genetics projects |

---

## 0. How to Talk to AI: Altitude, Depth, Range

### Who is Felix, and what is the idea

[Felix Rieseberg](https://felixrieseberg.com) works on Claude at Anthropic, where he has led engineering for Claude.ai, Claude Cowork, and the Claude Code desktop app. He previously worked at Notion, Stripe, Slack, and Microsoft, and co-maintains Electron. His essay [*How to be more ambitious: A tutorial for humans with models*](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/) (Oct 13, 2026) argues that **the bottleneck is usually how little we ask for, not what the model can do.**

He names four kinds of ambition:

| Kind | Meaning | Short version |
|------|---------|---------------|
| **Speed** | The same work in less time | Everyone already does this. He skips it |
| **Altitude** | Go up in abstraction: ask for the outcome, not the task | *"What's the goal beyond the goal?"* |
| **Depth** | Do the task the way a field-leading expert actually does it | Expert **methods and tools**, not expert vocabulary |
| **Range** | Draw on several fields, not just the obvious one | Bring in other disciplines; describe verbs, not nouns |

Two things make all three work:

- **Role prompts don't.** *"When prompted to act like a professional, models often switch vocabulary without actually switching methods."* "You are a world-class statistical geneticist…" gets you the jargon, not the workflow. *"Don't ask the model to write like a short seller, ask it to do what a short seller does."*
- **The model needs a computer.** These approaches require a model that can run code, install software, and touch real data. For us that means Claude Code on the HPC, not a chat window with pasted text.

---

### 1) Altitude: ask for the goal beyond the goal

**Rule 1: describe the outcome, not the next step.** Felix went from asking Claude to fix single crashes to asking it to *"simply keep our apps crash-free."*

**Rule 2: ask for a target that sounds unreasonable, and say it is reasonable.** *"You need your website to load in 5s instead of 10s? Ask for 200ms."* Then *"reiterate that it's very much solvable, it just needs to keep going."* Models often stop at the first improvement and report success. A far target makes them change the approach instead of tuning the old one.

StatGen example:

```diff
- The fine-mapping loop over 20,000 genes takes 3 days. Can you speed it up?
+ Goal: run fine-mapping for all 20,000 genes in under 1 hour on our cluster, with
+ results identical to the current version (PIPs within 1e-6 on a 200-gene test set).
+ This is very much solvable. Profile first, find where the time actually goes
+ (I/O? LD loading? the R loop? single-threaded BLAS?), fix the biggest cost, re-measure,
+ and keep going until you hit the target or can show with numbers what blocks it.
```

Second example, one level higher:

```diff
- Fix the bug in susie_wrapper.R line 120.
+ Our pipeline sometimes returns empty credible sets on chr6 (MHC).
+ Goal: every LD block gives sensible credible sets, or fails loudly with a clear reason.
+ Here are the logs, one failing block, and its LD matrix. Reproduce the failure,
+ find the root cause, fix it, and add a regression test.
```

---

### 2) Depth: make it use the expert's real tools

**Felix's copy-paste depth prompt.** Put it in front of any task where you want the expert-level version:

```text
I want a deeper version of this task, not a bigger one. Before rewriting it:
(1) say what a top professional in this field would do here that I'm not asking for;
(2) name the rawest material they would start from instead of what has already been digested for me;
(3) name the specific methods and tools they would use;
(4) say what, other than you or me, would show the result is right.
Then rewrite my prompt to ask for exactly that.
```

**Rule: if it answers with a markdown table, send it back.** *"When Claude reaches for markdown tables, insist on the use of databases and statistical models."* A table of numbers you pasted is a summary, not an analysis. Insist on real data stores (a DuckDB/SQLite database, or the actual summary-statistics files), proper regression models with covariates, and causal-inference methods with sensitivity analyses. **You don't need to know which methods the experts use.** Item (3) of the prompt makes Claude name them, and it usually knows them well.

StatGen example:

```diff
- You are an expert in statistical genetics. Is our eQTL signal enriched in brain?
- Summarize the attached table.
+ I want a deeper version of this task, not a bigger one. [Felix's 4 questions above]
+ Task: is the genetic signal for our trait enriched in brain-specific regulation?
```

What a good answer to the 4 questions looks like (illustrative):

| Question | Typical answer |
|---|---|
| (1) What would a top professional do that I'm not asking for? | Test enrichment formally against a baseline model, not by eye. Check that it isn't driven by LD, gene size, or MAF. Compare against other tissues |
| (2) Rawest material | Full GWAS summary statistics and tissue-specific annotations, not a table of top hits |
| (3) Methods and tools | Stratified LD score regression with the baseline-LD model; MAGMA gene-property analysis; colocalization at top loci; Mendelian randomization with sensitivity analyses (MR-Egger, weighted median) if a causal claim is wanted; results stored in a DuckDB database, not in markdown |
| (4) Outside evidence it's right | Null annotations and shuffled tissues give no enrichment; simulated traits with known enrichment are recovered; results replicate in an independent GWAS |

Then Claude rewrites your prompt along those lines, and you run that.

Second example, validating results:

```diff
- You are an expert in colocalization. Check my coloc results.
+ Before doing anything, list what a top statistical geneticist would check when validating
+ colocalization results (LD mismatch between GWAS and eQTL panels, allele flips, sample
+ overlap, prior sensitivity, multiple causal variants...) and the tool for each.
+ Then run those checks on results/coloc_*.tsv and report which pass or fail, with evidence.
```

---

### 3) Range: borrow other fields' methods

**Rule 1: bring in several disciplines, including someone whose job is to break the result.** Felix: *"For production quality, I'd bring in an analyst, a journalist, and an editor"*, then *"a short seller and a forensic accountant"* as the red team. Ask each to **do** their job, not to role-play.

**Rule 2: replace the nouns with verbs** (a trick he credits to *The Art of Innovation*). "Write a QQ-plot script" names an artifact. "Convince reviewers the test is calibrated" names an effect, and that leaves room for solutions you didn't think of.

StatGen example:

```diff
- Write a plotting script for the QQ plot.
+ I want reviewers to believe our new test is calibrated under the null.
+ Attack this claim the way three different people would, then produce the evidence:
+  - a statistician: QQ plots, genomic inflation, type-I error by MAF bin and sample size;
+  - a software tester: edge cases (monomorphic SNPs, tiny n, missing genotypes) that could break it;
+  - a skeptical reviewer: permutation and adversarial nulls (population structure, relatedness)
+    designed to make it fail.
+ Report where it holds and where it doesn't.
```

---

### Always: verify outside the model

*"Do not ask the model to judge itself."* The best check is *"a tool the model can run to get feedback immediately"*: tests, a simulation with known truth, a held-out dataset, or a different model reviewing the work (see [Part 3](#3-codex-review-independent-scoring) and [8.3](#83-validate-statistical-code-with-simulation)). Write the check into the prompt itself, as in item (4) of the depth prompt.

### One template that combines all three

```text
Goal (beyond the immediate task): <the outcome I actually want>
Target: <a far target>. This is very much solvable; keep going until you reach it
or can show with numbers what blocks it.
I want a deeper version of this task, not a bigger one. Before starting:
(1) what would a top professional in this field do that I'm not asking for;
(2) the rawest material they would start from;
(3) the specific methods and tools they would use (databases and statistical models,
    not markdown tables);
(4) what, other than you or me, would show the result is right.
Also: which other fields have solved a similar problem, and what would they do?
Then do it, and verify it with (4).
```

### References

- Original essay: Felix Rieseberg, *How to be more ambitious: A tutorial for humans with models* (Oct 13, 2026). <https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/>
- About the author: <https://felixrieseberg.com>
- Chinese write-ups translate the terms as 高度 / 深度 / 广度 (Altitude / Depth / Range); this page uses the original English terms.

---

## 1. MarkItDown: Any File to Markdown

### What it is

[MarkItDown](https://github.com/microsoft/markitdown) (Microsoft) converts PDF, Word, PowerPoint, Excel, HTML, images (OCR), audio, and more into **clean Markdown**.

### Why it matters

- **Saves tokens.** Markdown is the format LLMs handle best. A PDF read through the vision path, or a `.docx` full of XML, costs many more tokens than the same text as Markdown.
- **Better answers.** Headings, tables, and lists survive conversion, so the model sees the paper's structure.
- **Convert once, reuse many times.** The `.md` file can go into a project folder, a notes folder, or any AI tool.

### Install

```bash
pip install 'markitdown[all]'          # everything
pip install 'markitdown[pdf,docx,pptx]' # or only what you need
```

### How to use

```bash
# One file
markitdown paper.pdf -o paper.md

# A folder of papers
mkdir -p papers_md
for f in papers/*.pdf; do markitdown "$f" -o "papers_md/$(basename "${f%.pdf}").md"; done

# Reviewer comments in Word, a collaborator's slides
markitdown reviews_round1.docx -o reviews_round1.md
markitdown lab_meeting.pptx    -o lab_meeting.md
```

Then in Claude Code:

```
Read papers_md/susie_2020.md and papers_md/colocboost_2025.md.
Make a table comparing their model assumptions, priors, and how each handles multiple causal variants.
```

**Optional: as an MCP server**, so Claude converts files on its own:

```bash
pip install markitdown-mcp
claude mcp add markitdown -- markitdown-mcp
```

### Tips

- Equations in PDFs often come out garbled. For math-heavy papers, check the Methods section or use the arXiv LaTeX source.
- Scanned PDFs need OCR. Check the output before relying on it.
- **PDF tables lose their structure**: they come out as plain lines of text, not Markdown tables. Word/Excel/PPT tables convert cleanly. For a key PDF table, ask for the supplementary `.xlsx`/`.csv` instead.
- Keep the converted `.md` next to the original so you don't convert the same file twice.

---

## 2. OpenSpec: Spec-Driven Development

### What it is

[OpenSpec](https://github.com/Fission-AI/OpenSpec) adds a lightweight **spec layer** between you and the AI. Before code is written, the AI writes a *proposal*, *design*, and *task list* that you review. After implementation, the change is merged into a living spec of what the system does.

> **Hands-on example:** [`examples/openspec_demo/`](../../examples/openspec_demo/README.md) is a small, real Python package (`sumstats_tools`) built with OpenSpec v1.16.1. It contains **one finished change** (allele harmonization: proposed → implemented with 12 passing tests → archived into the living spec) to read, and **one pending proposal** (LD matrix check) you can implement yourself with `/opsx:apply`.

### When to use it

- Medium-to-large changes, such as adding a new method to a package or refactoring a pipeline, where "just start coding" leads to AI going off in the wrong direction.
- Shared repos, where the spec documents *why* things are the way they are.
- Skip it for one-line fixes.

### Install

```bash
npm install -g @fission-ai/openspec@latest
cd your-project
openspec init        # pick Claude Code (and/or Codex); installs slash commands, creates openspec/
```

### Workflow

```
/opsx:explore   (optional)  think through the problem with the AI, no files yet
      │
/opsx:propose   →  openspec/changes/<change>/  proposal.md · design.md · tasks.md · spec deltas
      │            ← YOU review and edit these. Iterate until the plan is right.
/opsx:apply     →  AI implements tasks.md, checking items off
      │
/opsx:archive   →  spec deltas merged into openspec/specs/, change moved to changes/archive/
```

Useful CLI commands: `openspec list`, `openspec show <change>`, `openspec validate <change>`, `openspec view` (dashboard).

### Example: adding a feature to a statgen package

```
/opsx:propose Add support for summary-statistics input (z-scores + LD matrix) to our fine-mapping
wrapper, in addition to individual-level genotypes. Must handle allele flips between sumstats and
LD reference, and reject LD matrices that are not PSD with a clear error.
```

OpenSpec writes `proposal.md` (why and scope), `design.md` (API, data flow, how flips are detected), and `tasks.md`:

```markdown
## 1. Input handling
- [ ] 1.1 Add `z`, `R`, `n` arguments; validate dimensions
- [ ] 1.2 Allele harmonization against LD reference; flip sign of z on mismatch
- [ ] 1.3 PSD check on R with informative error
## 2. Tests
- [ ] 2.1 Simulated data: sumstats path matches individual-level path within tolerance
- [ ] 2.2 Flipped-allele and non-PSD cases raise the expected errors
```

You fix anything wrong in the plan (e.g., "PSD check should allow a small tolerance, add `r_tol`"). Then run `/opsx:apply`, and `/opsx:archive` when it is merged.

### Tips

- **The review step is the point.** Ten minutes editing `design.md` saves hours of undoing AI code.
- Pair with [Part 3](#3-codex-review-independent-scoring): have Codex score the proposal before `/opsx:apply`.
- Command names differ between versions. Run `openspec --help` or see <https://openspec.dev/docs/getting-started>.

---

## 3. Codex Review: Independent Scoring

### The idea

The model that wrote something is the worst judge of it, because it shares the same blind spots and is biased toward its own reasoning. Use a **different model, in a fresh context, with an explicit rubric** that outputs a **score**. Then loop: Claude revises → Codex re-scores → stop when the score passes the bar.

This works for code, and also for **plans, specs, paper sections, grant aims, and responses to reviewers**.

> Setup of the Codex plugin (`/codex:review`, `/codex:adversarial-review`) is in [Claude_Code_User_Tips.md §2](Claude_Code_User_Tips.md#2-codex-code-review-plugin). This section is about *how to use it as an independent scorer*.

### Option A: inside Claude Code (plugin)

```
/codex:adversarial-review Score this change 1–10 on: statistical correctness, edge cases
(missing data, monomorphic SNPs, non-PSD LD), numerical stability, test coverage.
List blocking issues first. Do not suggest style changes.
```

### Option B: from the shell (`codex exec`, read-only)

```bash
codex exec --sandbox read-only "$(cat <<'EOF'
You are an independent reviewer. You did not write this code. Read openspec/changes/add-sumstats-input/
and the diff from `git diff main`.

Score each criterion 1-10 with a one-line justification:
1. Statistical correctness (does it compute what design.md says?)
2. Robustness (allele flips, NA, monomorphic SNPs, non-PSD LD, n mismatch)
3. Tests (would they catch a sign error in z?)
4. Reproducibility (seeds, versions, no hard-coded paths)

Then output:
OVERALL: <score>/10
BLOCKING: <numbered list, or "none">
NON-BLOCKING: <numbered list>
EOF
)" > review_round1.md
```

**HPC variant** (when Codex can't read files, see Tips): inline the files into the prompt.

```bash
codex exec --sandbox read-only "Do not run any commands; everything you need is below.
<same rubric as above>

$(for f in openspec/changes/<change>/design.md src/harmonize.py tests/test_harmonize.py; do
    echo "=== $f"; cat "$f"; done)" > review_round1.md
```

We ran this on [`examples/openspec_demo`](../../examples/openspec_demo/) and it found a real bug that 12 passing tests missed: an A/A variant matched both "match" and "swap", so its BETA got flipped (score 6/10, 2 BLOCKING). Fixed with a regression test.

Then hand it back to Claude:

```
Read review_round1.md. Fix every BLOCKING item. For each NON-BLOCKING item, either fix it or explain
in one line why not. Then I'll re-score.
```

### The loop

```
Claude writes → Codex scores (rubric) → Claude fixes BLOCKING → Codex re-scores
          stop when OVERALL ≥ 8 and BLOCKING = none   (cap at ~3 rounds)
```

### Rubric templates

| Reviewing… | Suggested criteria |
|------------|--------------------|
| Code | correctness · edge cases · numerical stability · tests · reproducibility |
| Plan / spec | solves the stated goal · scope creep · missing failure modes · testability |
| Paper section | claim ↔ evidence match · overclaiming · clarity · missing comparisons/baselines |
| Response to reviewers | each point answered · tone · manuscript actually changed · new analyses justified |

### Tips

- **Fresh context matters.** Don't paste Claude's reasoning into the review prompt, only the artifact. Otherwise Codex anchors on it.
- Ask for **blocking vs. non-blocking**. Otherwise you get 30 suggestions of equal weight.
- **Don't enable auto-review on every edit.** It burns quota in an endless loop. Score at milestones (after the plan, after implementation, before PR).
- Scores are a signal, not ground truth. Read the blocking items yourself.
- **On our HPC, Codex's sandbox fails** (`bwrap: pivot_root: Invalid argument`): it can't run `git diff` or tests, and on some nodes can't even read files, so it returns `OVERALL: N/A`. Fix: put the files in the prompt yourself (see the HPC variant under Option B) and run the tests yourself.
- **For prose, don't loop "rewrite until the AI reviewer score goes up".** AI reviewers reward hedging, and repeated review → revise rounds make GPT retract more and more of your claims (see [6b](#6b-defensive-writing-dont-let-gpt-water-down-your-claims)). Use the score to *find* issues; fix them yourself.

---

## 4. `handoff.md`: Never Lose Context

### The problem

Long tasks outlive a single context window. Sessions get compacted or closed, you switch from Claude to Codex, a labmate picks up your work, or you come back after a week. Each time, the new session starts knowing nothing.

### The fix

Before ending a session, have the AI write a **`handoff.md`**: a short, structured state dump that a fresh session (or a human) can read in 30 seconds and continue.

### Template

```markdown
# Handoff: <task name>  (updated 2026-11-08 17:40)

## Goal
One or two sentences: the end result we want, and how we'll know it's done.

## Current state
- Done: ...
- In progress: ... (file:line, what's half-finished)
- Not started: ...

## Key decisions (and why)
- Used UKB EUR LD panel, not 1000G, because sample-size mismatch inflated false positives in block 412.

## What we tried that did NOT work
- Increasing L to 20: no change, the problem is LD mismatch, not L.

## Next steps (in order)
1. ...
2. ...

## Key files / commands
- `scripts/run_finemap.sh` (entry point), `results/chr6/`, `logs/slurm-1234567.out`
- To reproduce the current state: `sbatch scripts/run_finemap.sh chr6`
```

### How to use

```
# End of session
Write handoff.md for this task using the template in skills/handoff/SKILL.md.

# New session (Claude, Codex, or a labmate)
Read handoff.md and continue from "Next steps". Ask me before changing any "Key decisions".
```

Even simpler: this repo ships a ready-made skill at [`skills/handoff/SKILL.md`](../../skills/handoff/SKILL.md). Copy it to `~/.claude/skills/handoff/` and type `/handoff`.

### Tips

- The **"what did NOT work"** section is the most valuable. It stops the next session from repeating dead ends.
- Write the handoff **before** the context is nearly full. At that point the model has already lost detail.
- Write it **in the same session that did the work**. A new session only sees git, not the conversation, so it can't fill in "what did NOT work" or "key decisions".
- Commit `handoff.md` with the code, so `git log` shows the history of where the project stood.

---

## 5a. Make It a Skill

### The idea

If you have typed the same long instructions more than twice, make them a **skill**. A skill is a folder with a `SKILL.md` file: a name, a description (which tells the AI *when* to use it), and the instructions. Claude loads it automatically when relevant, or you call it as `/skill-name`.

Example in this repo: [`skills/handoff/`](../../skills/handoff/SKILL.md).

### Where skills live

| Location | Scope |
|----------|-------|
| `~/.claude/skills/<name>/SKILL.md` | You, every project |
| `<repo>/.claude/skills/<name>/SKILL.md` | Everyone who clones the repo (shared lab conventions) |
| Plugin / marketplace | Distributed to others via `/plugin install` |

### Minimal `SKILL.md`

```markdown
---
name: qc-sumstats
description: QC GWAS summary statistics before fine-mapping or colocalization. Use when the user
  provides a sumstats file or asks to harmonize / QC GWAS results.
---

# Summary statistics QC

1. Detect columns (CHR, POS, A1, A2, BETA/OR, SE, P, N, EAF). Ask if ambiguous.
2. Check genome build (compare 20 known SNP positions against hg19/hg38).
3. Remove: duplicated variants, strand-ambiguous A/T and C/G SNPs with 0.4 < EAF < 0.6, INFO < 0.8.
4. Convert OR → log(OR); compute Z = BETA/SE; flag |Z| inconsistent with P.
5. Write <input>.qc.tsv.gz and a qc_report.md with counts removed at each step.
Never load the full file into context; use zcat | head and awk/R/Python scripts.
```

### The fastest way: let AI write it

At the end of a session that went well:

```
That workflow worked. Turn what we just did into a reusable skill in ~/.claude/skills/<name>/.
Generalize the file paths into arguments, keep the checks we found necessary, and include the
pitfalls we hit.
```

Or use Anthropic's **skill-creator** skill, which interviews you, drafts the skill, and can test it:

```
/skill-creator Create a skill for running SuSiE-RSS fine-mapping on one LD block with our lab defaults.
```

### Tips

- **The description is the trigger.** Write it as "Use when…" with the words people actually type.
- Keep `SKILL.md` short. Put long references in separate files in the same folder and say *when* to read them.
- Put lab-wide skills in a shared repo so improvements reach everyone.

---

## 5b. find-skills & Top Skills

### find-skills: search before you write

[skills.sh](https://skills.sh) is an open directory and leaderboard of agent skills, with an `npx skills` CLI. The **find-skills** skill lets your agent search it for you.

```bash
# Install the finder (into the current project's .claude/skills; add -g for global)
npx skills add vercel-labs/skills --skill find-skills

# Or search yourself
npx skills find "single cell"
npx skills find "pr review"

# Install any skill: owner/repo, or owner/repo@skill
npx skills add blader/humanizer
```

Inside Claude Code you can then just ask: *"Is there a skill for making publication-quality matplotlib figures? Find and install the best one."*

### Skills worth knowing

| Skill / collection | What it does | Install |
|--------------------|--------------|---------|
| **anthropics/skills** | Official: `pdf`, `docx`, `pptx`, `xlsx`, `skill-creator`, `frontend-design` | `/plugin marketplace add anthropics/skills` then `/plugin install document-skills@anthropic-agent-skills` (and/or `example-skills@anthropic-agent-skills`) |
| **obra/superpowers** | Disciplined dev workflow: brainstorming → writing plans → TDD → systematic debugging | `/plugin marketplace add obra/superpowers-marketplace` then `/plugin install superpowers@superpowers-marketplace` |
| **find-skills** (vercel-labs) | Search and install skills from skills.sh | see above |
| **humanizer** (blader) | Remove AI-writing tells from prose | see [Part 6](#6c-humanizer-remove-ai-writing-tells) |
| **obsidian-skills** (kepano) | If you keep notes in [Obsidian](https://obsidian.md): teaches the agent Obsidian Markdown (wikilinks, callouts), Bases, and Canvas | `npx skills add kepano/obsidian-skills` |
| **claude-scientific-skills** (K-Dense-AI) | Scientific packages and databases (scanpy, Biopython, PubMed, ...) | Large (100+ skills): install only what you need, e.g. `npx skills add K-Dense-AI/claude-scientific-skills --skill scanpy` |
| **nature-skills** | Academic workflow: literature search, paper reading, reference verification, polishing, reviewer responses, figures | `git clone https://github.com/Yuan1z0825/nature-skills` |
| **statgen-writing-style** (Gao) | Wang-group manuscript style | see [Part 6a](#6a-statgen-writing-style-write-like-the-lab) |
| **scientific-slides** (lab) | Lab-style talks as Beamer/PDF or editable PPTX | Claude Teams org skill; see [Part 7](#7-scientific-slides-talks-in-the-lab-style-beamerpdf-or-pptx) |

### Tips

- **Read a skill before installing it.** A skill is a set of instructions your agent will follow, possibly with scripts. Prefer well-known authors and check the repo.
- More skills is not better. Each skill's description takes up context. Install what you use, and remove the rest.

---

## 6. Writing

Writing is where AI helps most and also where it hurts most if used naively. Use these in order: **draft in lab style → keep claims calibrated (no AI over-hedging) → make it sound human → verify every reference**.

### 6a. statgen-writing-style: Write Like the Lab

Gao shared a skill that encodes the **Wang group writing style**, derived from the SuSiE, mvSuSiE, ColocBoost, SuSiE-Ann, jeTWAS, and fSuSiE papers. It applies to manuscripts, figure legends, supplementary notes, Specific Aims, and response letters.

**What it enforces (highlights):**

- **Mechanism first.** Open paragraphs with the problem, finding, or claim. Describe what the method *does*, not how exciting it is.
- **Abstract/Intro structure:** existing approach → specific methodological gap → *"Here, we propose [method] that…"*
- **Tense:** past for results (*ColocBoost identified*), present for methods (*The model accommodates*), present perfect for background.
- **Banned phrases:** "a pervasive challenge", "striking", "intriguing", "paradigm shift", "cutting-edge"; **no em dashes** when drafting with an LLM; no colons in headings.
- **Use sparingly:** "notably", "importantly", "novel".
- **Quantitative, no hedging adverbs:** *"reduced this 3.1-fold"*, not *"reduced this quite substantially"*.

**Install:** Claude app → Customize → Skills → "+" (upload `statgen-writing-style/SKILL.md`), or drop it into `~/.claude/skills/statgen-writing-style/` for Claude Code. Ask Gao or check the lab org skills if you don't have it.

**Use:**

```
Using statgen-writing-style, rewrite this Results paragraph. Keep every number. Flag any claim
that isn't supported by a figure or table we have.
```

```
Review my Introduction against statgen-writing-style. List violations with line references; don't rewrite yet.
```

### 6b. Defensive Writing: Don't Let GPT Water Down Your Claims

**What it is.** When GPT models revise a paper, they tend to **narrow, qualify, or even retract the authors' claims without any support in the source material**. A recent study calls this *defensive writing*: writing for an imagined reviewer instead of for the evidence ([Liao et al., arXiv:2610.11355](https://arxiv.org/abs/2610.11355)). This is different from real caution, which points to a limitation that actually exists in your data.

**What the study found** (77 paragraphs from 20 pre-ChatGPT papers, 8 GPT versions vs. Claude / DeepSeek / Grok):

| Finding | Number |
|---------|--------|
| Ungrounded qualifications added (newest GPT, result-analysis paragraphs) | ~1.3 per 100 words vs. ~0.04 in the authors' originals |
| Author claims **retracted** in one rewrite (newest GPT vs. control models) | 7.9% vs. ≤ 1.0% |
| Claims retracted after **one AI review → revise round** (GPT versions) | 11–25% (Claude Opus: ~1–5%) |
| Added qualifications judged **redundant** by PhD-student checkers | 36 of 60 (3 actually wrong) |
| Changed claims judged **warranted** | 28 of 48, so some of the softening was useful |
| Human readers: ease of reading / perceived author certainty | 5.75 → 5.05 (1–7) / 4.35 → 3.38 (1–5); comprehension unchanged |
| AI reviewer scores | **Higher** for hedged versions; stripping only the qualifications lowered scores ~0.8 |

So the hedging makes the paper harder to read and makes you sound unsure, without making it clearer. AI reviewers *reward* it, so a "rewrite until the AI reviewer is happy" loop makes it worse every round.

**What triggers it.** It depends on the prompt wording:

| Prompt framing | Defensive writing |
|----------------|-------------------|
| "Polish this paragraph" | ≈ none (close to the original) |
| "Make claims scientifically accurate / as strong as the evidence warrants" | Up somewhat |
| "Revise so it holds up under peer review" | Up |
| "Address the concerns a peer reviewer is likely to raise" | **Highest** |
| Review → revise, repeated | Accumulates every round |

**Typical patterns to watch for:**

- *Retraction disguised as rigor*: "this network has better stability properties" → "we therefore **do not claim** that the proposed formulation has better stability properties"
- *Weakened magnitude*: "outperforms the baselines by a large margin" → "achieves the highest performance"
- *"Not-shown" sentences*: "these results **do not by themselves establish** …"
- *Generic scoping*: "**in the evaluated settings**", "**under our assumptions**", repeated in every paragraph

StatGen version of the same thing:

```diff
- ColocBoost identified 2,043 colocalized loci, 38% more than the next best method.
+ Within the settings we evaluated, ColocBoost identified 2,043 putatively colocalized loci;
+ however, these results do not by themselves establish shared causal variants, and differences
+ relative to other methods may depend on LD reference and prior choices.
```

The numbers are the same; the hedges just make the claim sound weaker. If LD-reference sensitivity really matters, say it **once**, with the analysis that shows it, in Limitations.

#### Prompts that keep claims calibrated (neither overclaiming nor defensive)

The goal is **as strong as the evidence supports, no stronger and no weaker, with the author making the call**. Two rules follow from the study: (1) keep *critique* and *rewriting* as separate steps, and (2) don't put "reviewer" or "peer review" in a rewrite prompt.

**① Rewrite / polish: language only, claims locked**

```
Polish this paragraph for clarity, flow, and concision. This is a language edit only.
Rules:
- Keep every claim at its current strength. Do not add hedges, qualifications, scope limits,
  or "we do not claim / these results do not establish" sentences.
- Do not remove or weaken any claim, number, or comparison.
- If you think a claim is not supported, do NOT change it. Instead list it after the paragraph
  as: [CLAIM] → [why you think it's unsupported] → [what evidence would support it].
```

> **We tested it** (2026-11-09, GPT via `codex exec`, 3 runs each, same ColocBoost Results paragraph ending in *"These results show that joint modeling of multiple traits improves power…"*):
>
> | Prompt | Last sentence kept? | Defensive sentences added |
> |--------|---------------------|---------------------------|
> | "Revise this paragraph so that it holds up under peer review." | **0/3**: "show… improves power" became "demonstrate a higher discovery yield… under the simulated conditions" | **3/3** added "However, … requires matched false-positive rates / ablation", or "these comparisons do not isolate…" |
> | Prompt ① | **3/3**, word for word | **0/3**. The same concern (joint modeling not isolated → needs an ablation) shows up as a flagged item **below** the paragraph, for you to decide |
>
> GPT's concern is a fair one. With ① it reaches you as a flag for you to decide on, instead of being written into your paper.

**② Critique: list problems, change nothing**

```
Read the Results section. Do not rewrite anything.
Make a table with one row per claim: claim (quoted) | supporting figure/table/number |
verdict: overclaim / calibrated / UNDERclaim | one-line reason.
Count underclaims (claims weaker than the evidence) as errors too.
Only mark "overclaim" if you can point to a specific missing analysis or contradicting result.
```

Asking for **underclaims** as well as overclaims is what keeps this from turning defensive.

**③ Audit a draft someone (or some AI) already revised**

```
Compare original.md and revised.md sentence by sentence.
For every claim, label it: kept / softened / retracted / strengthened.
For every qualification that appears in revised.md but not original.md, cite the specific
data, figure, or analysis in our paper that requires it. If none exists, mark it UNGROUNDED.
Output the table only.
```

Then **you** decide: keep the warranted changes (the study found more than half of the changed claims were warranted) and revert the ungrounded ones.

**④ Standing instruction**: put it in `CLAUDE.md`, ChatGPT custom instructions, or a project's instructions:

```markdown
# Claim calibration
- State findings directly at the strength the evidence supports. No reflexive hedging.
- A qualification is allowed only if it names a specific limitation of OUR data or analysis
  (e.g. "EUR-only LD reference"), and it is stated once (usually in Limitations), not repeated.
- Never add "we do not claim…", "these results do not by themselves establish…",
  or "in the evaluated settings" unless I ask.
- Never silently weaken or delete a claim. Flag it and let me decide.
```

**When you do want reviewer-style criticism** (e.g., before submission or for a response letter), use a reviewer prompt **only to produce a list of objections**, not to rewrite. Fix the real ones yourself with new analyses or targeted wording. Typical real statgen objections: LD reference mismatch · population stratification · winner's curse · sample overlap between GWAS and QTL · simulation settings too favorable to your method · unfair baseline settings · multiple testing across tissues/contexts.

**Quick self-check after any AI edit:**

- [ ] Did any number, effect size, or "X-fold / outperforms" comparison get weaker?
- [ ] Any new "we do not claim", "do not establish", "may", "potentially", "in the evaluated settings"?
- [ ] Is every remaining caveat tied to a named limitation, and stated only once?
- [ ] Did I, not the model, decide each softening?

> Model note: in the study, Claude and DeepSeek added almost no ungrounded qualifications; recent GPT versions added the most. It's still worth running the check whichever model you use.

### 6c. Humanizer: Remove AI-Writing Tells

> Not the same as the *Humanize* plugin in the old page (that one is for plans and PR loops).

[blader/humanizer](https://github.com/blader/humanizer) is a skill based on Wikipedia's *"Signs of AI writing"* guide. It detects and rewrites AI tells: inflated significance ("plays a pivotal role"), rule-of-three lists, "not only… but also", vague attributions, em-dash overuse, promotional tone, and filler conclusions.

```bash
npx skills add blader/humanizer
# or: git clone https://github.com/blader/humanizer.git ~/.claude/skills/humanizer
```

```
/humanizer Rewrite the Discussion in draft.md. Keep all technical content and numbers.
```

Tips: run it **after** content is final, not before. Check that technical terms weren't changed for "variety" (e.g., *credible set* must stay *credible set*). It complements statgen-writing-style, it doesn't replace it.

### 6d. Verify Every Reference

LLMs make up citations: real-looking authors, plausible titles, wrong years, fake DOIs. **Never paste an AI-generated reference list without checking it.**

- The `nature-ref-verifier` skill (nature-skills) cross-checks each reference against multiple sources (authors, title, year, volume, pages, DOI) and produces a report.
- Minimum manual check: every DOI resolves, and the paper says what you cite it for.

```
Verify every reference in manuscript.md with nature-ref-verifier. Then, for each in-text citation,
confirm the cited paper actually supports the sentence; list any mismatches.
```

---

## 7. scientific-slides: Talks in the Lab Style (Beamer/PDF or PPTX)

### What it is

`scientific-slides` turns papers, manuscripts, notes, and old decks into a **scientific talk**: lab meetings, journal clubs, seminars, lectures, or several of your papers joined into one story. It started from Gao's lecture-preparation SOPs, and we extended it to output PowerPoint as well. It applies the same rules as Gao's writing style ([6a](#6a-statgen-writing-style-write-like-the-lab)), adapted for slides:

- **Story first.** Open with a concrete question or tension, give each slide one job, and connect papers through a shared model. Never "Paper 1 / Paper 2 / Paper 3".
- **Models explained properly.** Show the smallest complete model, say what is observed, assumed, or estimated, and give the formula before the numbers. A new method is introduced as a change to the old model.
- **Honest figures.** Use real figures from the paper for evidence and drawn diagrams for mechanisms. Never fabricate data points, citations, or benchmarks. Credits are short (`Author et al. (year), Fig. N`), and full provenance goes in `planning/figures.csv`.
- **Lab visual style.** White slides, blue structure, sparse **dark-red bold** for decisive terms, *blue italic* for concepts, a named blue box for a math fact (e.g. "Variance of a Sum") right before it is first used, and spoken background in presenter notes.
- **No shrinking text to fit.** If a slide is too full, it cuts, moves detail to notes, or splits the slide.

**Two output formats, one style:**

| You ask for | You get |
|---|---|
| Nothing specific (default) | Editable **LaTeX Beamer + PDF** |
| "PPTX" / "PowerPoint", or you give it a `.pptx` to revise | Editable **native-shape `.pptx`**: real text boxes and shapes, LaTeX-rendered formulas, speaker notes. The same palette and rules as the Beamer version |

### Install

**It is already in our Claude Teams org skills as `scientific-slides`.** Nothing to install: it shows up for everyone in the org. In Claude Code it syncs automatically and appears as `anthropic-skills:scientific-slides` (start a new session if you don't see it yet). Type `/scientific-slides`, or just say "use scientific-slides to…".

For PPTX it uses `python-pptx`, plus LaTeX for formulas and LibreOffice to render pages for checking. On the HPC: `pip install python-pptx pyyaml` (LaTeX and LibreOffice are already there).

### How to use

```
Use scientific-slides. Make a 20-minute journal-club deck as PPTX from papers/colocboost.pdf.
Audience: statistical geneticists who know coloc but not ColocBoost.
Open with the question the paper answers, show the model before the results, use the paper's
real figures for evidence, put the key identity in a blue box before first use,
and write what I'll say in the speaker notes. Render every page and check it.
```

```
Use scientific-slides. Only revise slides 5–6 of talk.pptx: make the model slide follow from
slide 4. Keep the theme, the other slides, and the notes unchanged; save as talk_v2.pptx and
show me the rendered pages you changed.
```

```
Use scientific-slides. Audit the narrative of my lab-meeting deck (talk.pptx): where does
the story jump, which quantities are undefined? Don't edit any files.
```

What happens behind the scenes, for PPTX:

1. It writes `talk/deck.yaml`: one entry per slide (title, columns, bullets, cards, equations, notes, credit).
2. `pptxkit.py build` turns that into `deck.pptx` and reports overfull slides and lint errors.
3. `pptxkit.py render` turns each page into an image, and Claude **looks at every page** and fixes problems.
4. You get `deck.pptx` (edit it in PowerPoint), `deck.yaml` (the editable source), the rendered pages in `qa/`, and `planning/claims.csv` (which source supports each claim).

### Tips

- Give it the **real sources** (PDFs or MarkItDown output from [Part 1](#1-markitdown-any-file-to-markdown)). It will not invent figures or numbers it can't find. It marks them "check before talk" instead.
- Say **audience and minutes**. That decides what gets cut, not a slides-per-minute rule.
- To **audit any deck**, including hand-made ones, run `python3 pptxkit.py audit talk.pptx`. It flags shrink-to-fit, text under 17 pt, shapes off the slide, and overcrowded slides.
- Always open the final file yourself. Renders come from LibreOffice, and PowerPoint can wrap lines slightly differently.

**Alternative:** [PPT Master](https://github.com/hugohe3/ppt-master) (`npx skills add hugohe3/ppt-master`) quickly turns any document into an editable `.pptx` with a generic design and can copy the look of a template deck. Use it for non-research slides. For lab talks, use `scientific-slides`.

---

## 8. Practical Tips for StatGen Research

What we have learned using AI on real genetics projects on the HPC.

### 8.1 Put HPC rules in `CLAUDE.md`

The AI doesn't know your cluster. Tell it once in a project `CLAUDE.md`:

```markdown
# Environment
- HPC with SLURM. NEVER run heavy compute on the login node; write an sbatch script and submit it.
- Partitions: <name> (default), <name> (high-mem). Max walltime: ...
- Activate env: `micromamba activate <env>` / `module load R/4.4`
- Data lives in /path/to/data (read-only). Write outputs to /path/to/project/results.

# Data handling
- Never `cat` or `Read` genotype/VCF/BGEN/sumstats files. Inspect with `zcat file | head`, `bcftools view -h`,
  `wc -l`, or a script that prints a summary.
- Large outputs: write to files; print only summaries.
```

### 8.2 Big files: inspect, don't read

A 5 GB VCF or a 10M-row sumstats file will flood the context (or crash the session). Ask for **summaries computed by code**:

```
Don't open the file. Write and run a script that reports: number of variants, columns, genome build
guess, % missing per column, and the first 5 rows.
```

### 8.3 Validate statistical code with simulation

AI-written statistical code can *run* and still be *wrong* (sign errors, wrong variance, off-by-one in LD indexing). Always ask for a simulation check:

```
Before running on real data: simulate genotypes (n=1000, p=500, realistic LD from this panel),
plant 2 causal variants with known effects, run the method, and check (1) the causal variants are in
the credible sets, (2) coverage across 100 replicates is ≈ 95%, (3) under the null, p-values are uniform.
```

Simulation under known truth is the most reliable external check you have, in the same spirit as "verify externally" in [Part 0](#0-how-to-talk-to-ai-altitude-depth-range).

### 8.4 Protect controlled-access data

- **Individual-level data under a DUA (dbGaP, UK Biobank, AMP-AD, ...) must not be sent to cloud AI services.** That includes pasting rows, letting the agent `cat` the files, or uploading them.
- Safer: let the AI write code that runs **locally** and only prints aggregate summaries; share only public summary statistics or simulated data.
- Block sensitive paths with permission rules in `.claude/settings.json`:
  ```json
  { "permissions": { "deny": ["Read(//path/to/controlled_data/**)"] } }
  ```
  Absolute paths need **two** leading slashes (`//path/...`); a single `/` is read as relative to the project. The rule also stops Claude from reading those files via `cat`/`head` in Bash.

### 8.5 Reproducibility by default

Ask for scripts, not interactive one-offs. Every AI-run analysis should leave a script, fixed seeds, recorded package versions (`sessionInfo()` / `pip freeze`), and a short note in the project log. Commit before and after each AI change so you can roll back (see [practices_RL.md](practices_RL.md) for the git rollback strategy).

### 8.6 Use the skills you already have

| Task | Tool |
|------|------|
| Literature search / reading / paper cards | nature-skills (`nature-academic-search`, `nature-reader`, `nature-paper-card`) |
| Statistical reporting check | `nature-statistics` |
| Figures | `nature-figure`, or the `dataviz` skill |
| Response to reviewers | `nature-response` + [calibrated-claim prompts](#6b-defensive-writing-dont-let-gpt-water-down-your-claims) + [Codex scoring](#3-codex-review-independent-scoring) |
| Lab meeting / journal club slides | `scientific-slides` ([Part 7](#7-scientific-slides-talks-in-the-lab-style-beamerpdf-or-pptx)) |
| Long multi-day analysis | [OpenSpec](#2-openspec-spec-driven-development) for the plan + [`handoff.md`](#4-handoffmd-never-lose-context) between sessions |

### 8.7 Derivations: ask for LaTeX *and* a numeric check

When AI derives a gradient, posterior, or ELBO update, ask it to (1) write the derivation step by step in LaTeX and (2) check it numerically: finite-difference gradients, or compare the closed form against Monte Carlo. A derivation that reads well is not necessarily correct.

---

## Cheat Sheet

| I want to… | Use | Command / prompt |
|------------|-----|------------------|
| Get better results from any prompt | Altitude / Depth / Range | "Goal is X. What would the best person use? Use it. Verify." |
| Give AI a PDF/Word/PPT cheaply | MarkItDown | `markitdown paper.pdf -o paper.md` |
| Plan a non-trivial change | OpenSpec | `/opsx:propose` → review → `/opsx:apply` → `/opsx:archive` |
| Get an unbiased quality check | Codex scoring | `/codex:adversarial-review <rubric>` or `codex exec --sandbox read-only` |
| Continue tomorrow / hand to a labmate | handoff.md | `/handoff` → next session: "Read handoff.md and continue" |
| Stop repeating myself | Make a skill | "Turn what we just did into a skill" / `/skill-creator` |
| Find an existing skill | find-skills | `npx skills find "<topic>"` |
| Write in lab style | statgen-writing-style | "Using statgen-writing-style, rewrite…" |
| Polish without GPT watering down claims | Calibrated-claim prompts | "Language edit only. Keep every claim at its current strength; flag, don't change" |
| Remove AI tone | Humanizer | `/humanizer` |
| Check citations are real | nature-ref-verifier | "Verify every reference in…" |
| Paper → slides | scientific-slides | `/scientific-slides` "20-min journal club as PPTX from paper.pdf" |

## Your First Week

1. **Day 1:** Re-write one prompt you use often with Altitude / Depth / Range. Compare the outputs.
2. **Day 2:** `pip install 'markitdown[all]'`; convert the 5 papers you're reading now.
3. **Day 3:** Install `find-skills` and `humanizer`; get `statgen-writing-style` from Gao.
4. **Day 4:** Add an HPC + data-handling `CLAUDE.md` to your main project ([§8.1](#81-put-hpc-rules-in-claudemd)).
5. **Day 5:** End a real session with `/handoff`, start the next one from it. Score one piece of work with Codex.
6. **Next big change:** try OpenSpec end to end.

---

## References

- MarkItDown: <https://github.com/microsoft/markitdown>
- kepano/obsidian-skills (for Obsidian users): <https://github.com/kepano/obsidian-skills>
- OpenSpec: <https://github.com/Fission-AI/OpenSpec> · docs: <https://openspec.dev/docs/getting-started>
- Codex plugin for Claude Code: <https://github.com/openai/codex-plugin-cc> · Codex CLI: <https://github.com/openai/codex>
- Claude Code skills docs: <https://docs.anthropic.com/en/docs/claude-code/skills> · anthropics/skills: <https://github.com/anthropics/skills>
- skills.sh directory: <https://skills.sh> · find-skills: <https://github.com/vercel-labs/skills>
- obra/superpowers: <https://github.com/obra/superpowers>
- Humanizer: <https://github.com/blader/humanizer> · Wikipedia "Signs of AI writing": <https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing>
- scientific-slides: Claude Teams org skill (based on Gao Wang's lecture SOPs; PPTX output added 2026-11) · PPT Master (alternative): <https://github.com/hugohe3/ppt-master>
- nature-skills: <https://github.com/Yuan1z0825/nature-skills>
- Defensive writing in GPT models (Liao et al.): <https://arxiv.org/abs/2610.11355>
- Felix Rieseberg, "How to be more ambitious: A tutorial for humans with models" (2026): <https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/>
