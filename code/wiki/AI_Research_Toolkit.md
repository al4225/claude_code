# AI Research Toolkit: Skills, Tools & Prompting Tips for StatGen

*Lab meeting, Nov 9, 2026*

This page continues [Claude_Code_User_Tips.md](Claude_Code_User_Tips.md). That page covers terminal setup, the Codex plugin, Humanize, and Remote Control. This page covers **how to work with AI across a research project**, from feeding it papers to shipping a figure-ready manuscript and slide deck.

The sections follow the order of a real project. Read top to bottom the first time; after that, use the [cheat sheet](#cheat-sheet).

```mermaid
flowchart LR
    A["0. Prompt well<br/>Altitude · Depth · Range"] --> C["1. Plan<br/>OpenSpec"]
    C --> D["2. Verify<br/>Codex independent score"]
    D --> E["3. Hand off<br/>handoff.md"]
    E --> G["4. Write<br/>statgen style · defensive · Humanizer"]
    G --> H["5. Present<br/>scientific-slides"]
    H --> I["6. StatGen tips"]
    I --> F["7. Reuse<br/>Skills · find-skills"]
```

---

## Overview

| # | Part | Tool / Tip | One-line pitch |
|---|------|-----------|----------------|
| 0 | [How to talk to AI](#0-how-to-talk-to-ai-altitude-depth-range) | Altitude / Depth / Range | Stop saying "you are an expert in X". Give it a goal, a workflow, and an outcome |
| 1 | [Plan](#1-openspec-spec-driven-development) | OpenSpec | Agree on a written spec before AI writes code |
| 2 | [Verify](#2-codex-review-independent-scoring) | Codex independent scoring | A second model scores the work against a rubric |
| 3 | [Continuity](#3-handoffmd-never-lose-context) | `handoff.md` | One file that lets a new session pick up where the last one stopped |
| 4 | [Writing](#4-writing) | statgen-writing-style · defensive writing · Humanizer · ref verification | Write in lab style, stop GPT from watering down claims, sound human, cite real papers |
| 5 | [Present](#5-scientific-slides-talks-in-the-lab-style-beamerpdf-or-pptx) | scientific-slides | Papers → lab-style talk as Beamer/PDF or **editable** PPTX |
| 6 | [StatGen tips](#6-practical-tips-for-statgen-research) | HPC, big files, simulation checks, DUAs, MarkItDown | Lessons from using AI on real genetics projects |
| 7a | [Reuse](#7a-make-it-a-skill) | Make it a skill | Turn a good session into a `/command` |
| 7b | [Reuse](#7b-find-skills--top-skills) | find-skills, top skills | Use skills other people already wrote |

---

## 0. How to Talk to AI: Altitude, Depth, Range

### Who is Felix, and what is the idea

[Felix Rieseberg](https://felixrieseberg.com) works on Claude at Anthropic, where he has led engineering for Claude.ai, Claude Cowork, and the Claude Code desktop app. He previously worked at Notion, Stripe, Slack, and Microsoft, and co-maintains Electron. His essay [*How to be more ambitious: A tutorial for humans with models*](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/) (Oct 13, 2026) argues that **the bottleneck is usually how little we ask for, not what the model can do.**

He focuses on three kinds of ambition:

| Kind | Meaning | Short version |
|------|---------|---------------|
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

**Rule 2: replace the nouns with verbs** (a trick he credits to *The Art of Innovation*). A noun fixes the format before you've thought about the goal. If you think "quarterly review", all you picture is a slide deck. Felix's verb version describes what the review has to *do*: *"getting busy people to believe a story about cause and effect, and to decide under uncertainty, in 30 minutes."* That sentence opens up options a deck template never would: lead with the decision, show the causal evidence, put the uncertainty up front.

The same move in our work:

| Noun (format fixed) | Verb (what it must achieve) |
|---|---|
| "a lab-meeting deck" | "in 15 minutes, get people who don't know my method to understand why the old model fails here, believe the new result, and tell me what's missing" |
| "a QQ-plot script" | "convince reviewers the test is calibrated under the null" |
| "a Methods section" | "let someone reproduce every number in the paper without emailing us" |

Give Claude the verb version and it can propose formats you didn't think of.

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

*"Do not ask the model to judge itself."* The best check is *"a tool the model can run to get feedback immediately"*: tests, a simulation with known truth, a held-out dataset, or a different model reviewing the work (see [Part 2](#2-codex-review-independent-scoring) and [6.3](#63-validate-statistical-code-with-simulation)). Write the check into the prompt itself, as in item (4) of the depth prompt.

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
- Chinese summary (WeChat official account article): <https://www.woshipm.com/ai/6479197.html>

---

## 1. OpenSpec: Spec-Driven Development

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
- Pair with [Part 2](#2-codex-review-independent-scoring): have Codex score the proposal before `/opsx:apply`.
- Command names differ between versions. Run `openspec --help` or see <https://openspec.dev/docs/getting-started>.

---

## 2. Codex Review: Independent Scoring

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
- **For prose, don't loop "rewrite until the AI reviewer score goes up".** AI reviewers reward hedging, and repeated review → revise rounds make GPT retract more and more of your claims (see [6b](#4b-defensive-writing-dont-let-gpt-water-down-your-claims)). Use the score to *find* issues; fix them yourself.

---

## 3. `handoff.md`: Never Lose Context

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

## 4. Writing

Writing is where AI helps most and also where it hurts most if used naively. Use these in order: **draft in lab style → keep claims calibrated (no AI over-hedging) → make it sound human → verify every reference**.

### 4a. statgen-writing-style: Write Like the Lab

Gao shared a skill that encodes the **Wang group writing style**, derived from the SuSiE, mvSuSiE, ColocBoost, SuSiE-Ann, jeTWAS, and fSuSiE papers. It applies to manuscripts, figure legends, supplementary notes, Specific Aims, and response letters.

**What it enforces (highlights):**

- **Mechanism first.** Open paragraphs with the problem, finding, or claim. Describe what the method *does*, not how exciting it is.
- **Abstract/Intro structure:** existing approach → specific methodological gap → *"Here, we propose [method] that…"*
- **Tense:** past for results (*ColocBoost identified*), present for methods (*The model accommodates*), present perfect for background.
- **Banned phrases:** "a pervasive challenge", "striking", "intriguing", "paradigm shift", "cutting-edge"; **no em dashes** when drafting with an LLM; no colons in headings.
- **Use sparingly:** "notably", "importantly", "novel".
- **Quantitative, no hedging adverbs:** *"reduced this 3.1-fold"*, not *"reduced this quite substantially"*.

**Install:** nothing to do. It is in our Claude Teams org skills, so it is available automatically in claude.ai and in Claude Code (where it appears as `anthropic-skills:statgen-writing-style`; start a new session if you don't see it yet).

**Use:**

```
Using statgen-writing-style, rewrite this Results paragraph. Keep every number. Flag any claim
that isn't supported by a figure or table we have.
```

```
Review my Introduction against statgen-writing-style. List violations with line references; don't rewrite yet.
```

### 4b. Defensive Writing: Don't Let GPT Water Down Your Claims

**Problem → why it happens → how to prevent it → how to check.**

#### 1. The problem

When GPT revises a paper, it often **adds hedges or retracts claims that your data actually support**. It is writing for an imagined reviewer, not for the evidence. [Liao et al. (arXiv:2610.11355)](https://arxiv.org/abs/2610.11355) call this *defensive writing*.

```diff
- ColocBoost identified 2,043 colocalized loci, 38% more than the next best method.
+ Within the settings we evaluated, ColocBoost identified 2,043 putatively colocalized loci;
+ however, these results do not by themselves establish shared causal variants...
```

The numbers didn't change; the claim just got weaker. Real caution is different: it names a specific limitation of *your* data, says it once, and puts it in Limitations.

**What the study measured** (77 paragraphs from 20 papers, 8 GPT versions vs. Claude / DeepSeek / Grok):

- Newest GPT **retracted 7.9%** of author claims in a single rewrite (other models ≤ 1%). After one AI-review → revise round: **11–25%** (Claude Opus ~1–5%).
- Readers found the hedged text **harder to read** and the authors **less certain**. Comprehension did not improve.
- AI reviewers **scored the hedged versions higher**. So "revise until the AI reviewer is happy" makes it worse every round.
- Not all softening was bad: more than half of the changed claims (28 of 48) were judged warranted. **The fix is for you to decide, not to ban every change.**

#### 2. What triggers it: the word "reviewer"

| Prompt | Defensive writing |
|---|---|
| "Polish this paragraph" | ≈ none |
| "Revise so it holds up under peer review" | More |
| "Address the concerns a reviewer is likely to raise" | **Most** |
| Review → revise, repeated | Accumulates every round |

#### 3. How to prevent it: separate critique from rewriting

**Rule:** a rewrite prompt never mentions reviewers, and a critique prompt never rewrites. You decide what to change in between.

**① Rewrite: language only, claims locked**

```
Polish this paragraph for clarity, flow, and concision. This is a language edit only.
- Keep every claim, number, and comparison at its current strength.
- Do not add hedges, scope limits, or "we do not claim / do not establish" sentences.
- If you think a claim is unsupported, do NOT change it. List it after the paragraph as:
  [CLAIM] → [why unsupported] → [what evidence would support it].
```

**② Critique: list problems, change nothing**

```
Read the Results section. Do not rewrite anything. One row per claim:
claim (quoted) | supporting figure/number | overclaim / calibrated / UNDERclaim | reason.
Underclaims count as errors too. Only mark "overclaim" if you can name the missing analysis.
```

Then fix the real problems yourself, with a new analysis or one targeted sentence. Typical real statgen objections: LD reference mismatch · population stratification · winner's curse · GWAS–QTL sample overlap · simulations that favor your method · multiple testing across tissues.

**③ Make it permanent**: put this in `CLAUDE.md` or ChatGPT custom instructions:

```markdown
# Claim calibration
- State findings at the strength the evidence supports. No reflexive hedging.
- A caveat must name a specific limitation of OUR data (e.g. "EUR-only LD reference"), stated once.
- Never silently weaken or delete a claim. Flag it and let me decide.
```

**We tested ①** (GPT via `codex exec`, 3 runs each, same ColocBoost Results paragraph):

| Prompt | Conclusion kept | Defensive sentences added |
|---|---|---|
| "Revise … so that it holds up under peer review" | 0/3 | 3/3 ("However, … requires …", "do not isolate …") |
| ① | **3/3** word for word | **0/3**. The same concern appeared as a flag **below** the paragraph, for the author to decide |

#### 4. Check after any AI edit

- [ ] Did any number, effect size, or "outperforms" get weaker?
- [ ] Any new "we do not claim", "do not establish", "may", "in the evaluated settings"?
- [ ] Does every remaining caveat name a real limitation, stated only once?

Already have a revised draft? Ask: *"Compare original.md and revised.md. Label each claim kept / softened / retracted. For every new qualification, cite the data that requires it, or mark it UNGROUNDED."* Then revert the ungrounded ones.

### 4c. Humanizer: Remove AI-Writing Tells

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

### 4d. Verify Every Reference

LLMs make up citations: real-looking authors, plausible titles, wrong years, fake DOIs. **Never paste an AI-generated reference list without checking it.**

- The `nature-ref-verifier` skill (nature-skills) cross-checks each reference against multiple sources (authors, title, year, volume, pages, DOI) and produces a report.
- Minimum manual check: every DOI resolves, and the paper says what you cite it for.

```
Verify every reference in manuscript.md with nature-ref-verifier. Then, for each in-text citation,
confirm the cited paper actually supports the sentence; list any mismatches.
```

---

## 5. scientific-slides: Talks in the Lab Style (Beamer/PDF or PPTX)

### What it is

`scientific-slides` turns papers, manuscripts, notes, and old decks into a **scientific talk**: lab meetings, journal clubs, seminars, lectures, or several of your papers joined into one story. It started from Gao's lecture-preparation SOPs, and we extended it to output PowerPoint as well. It applies the same rules as Gao's writing style ([6a](#4a-statgen-writing-style-write-like-the-lab)), adapted for slides:

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

- Give it the **real sources** (PDFs or MarkItDown output from [6.8](#68-give-ai-documents-as-markdown-markitdown)). It will not invent figures or numbers it can't find. It marks them "check before talk" instead.
- Say **audience and minutes**. That decides what gets cut, not a slides-per-minute rule.
- To **audit any deck**, including hand-made ones, run `python3 pptxkit.py audit talk.pptx`. It flags shrink-to-fit, text under 17 pt, shapes off the slide, and overcrowded slides.
- Always open the final file yourself. Renders come from LibreOffice, and PowerPoint can wrap lines slightly differently.

**Alternative:** [PPT Master](https://github.com/hugohe3/ppt-master) (`npx skills add hugohe3/ppt-master`) quickly turns any document into an editable `.pptx` with a generic design and can copy the look of a template deck. Use it for non-research slides. For lab talks, use `scientific-slides`.

---

## 6. Practical Tips for StatGen Research

What we have learned using AI on real genetics projects on the HPC.

### 6.1 Put HPC rules in `CLAUDE.md`

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

### 6.2 Big files: inspect, don't read

A 5 GB VCF or a 10M-row sumstats file will flood the context (or crash the session). Ask for **summaries computed by code**:

```
Don't open the file. Write and run a script that reports: number of variants, columns, genome build
guess, % missing per column, and the first 5 rows.
```

### 6.3 Validate statistical code with simulation

AI-written statistical code can *run* and still be *wrong* (sign errors, wrong variance, off-by-one in LD indexing). Always ask for a simulation check:

```
Before running on real data: simulate genotypes (n=1000, p=500, realistic LD from this panel),
plant 2 causal variants with known effects, run the method, and check (1) the causal variants are in
the credible sets, (2) coverage across 100 replicates is ≈ 95%, (3) under the null, p-values are uniform.
```

Simulation under known truth is the most reliable external check you have, in the same spirit as "verify externally" in [Part 0](#0-how-to-talk-to-ai-altitude-depth-range).

### 6.4 Protect controlled-access data

- **Individual-level data under a DUA (dbGaP, UK Biobank, AMP-AD, ...) must not be sent to cloud AI services.** That includes pasting rows, letting the agent `cat` the files, or uploading them.
- Safer: let the AI write code that runs **locally** and only prints aggregate summaries; share only public summary statistics or simulated data.
- Block sensitive paths with permission rules in `.claude/settings.json`:
  ```json
  { "permissions": { "deny": ["Read(//path/to/controlled_data/**)"] } }
  ```
  Absolute paths need **two** leading slashes (`//path/...`); a single `/` is read as relative to the project. The rule also stops Claude from reading those files via `cat`/`head` in Bash.

### 6.5 Reproducibility by default

Ask for scripts, not interactive one-offs. Every AI-run analysis should leave a script, fixed seeds, recorded package versions (`sessionInfo()` / `pip freeze`), and a short note in the project log. Commit before and after each AI change so you can roll back (see [practices_RL.md](practices_RL.md) for the git rollback strategy).

### 6.6 Use the skills you already have

| Task | Tool |
|------|------|
| Literature search / reading / paper cards | nature-skills (`nature-academic-search`, `nature-reader`, `nature-paper-card`) |
| Statistical reporting check | `nature-statistics` |
| Figures | `nature-figure`, or the `dataviz` skill |
| Response to reviewers | `nature-response` + [calibrated-claim prompts](#4b-defensive-writing-dont-let-gpt-water-down-your-claims) + [Codex scoring](#2-codex-review-independent-scoring) |
| Lab meeting / journal club slides | `scientific-slides` ([Part 5](#5-scientific-slides-talks-in-the-lab-style-beamerpdf-or-pptx)) |
| Long multi-day analysis | [OpenSpec](#1-openspec-spec-driven-development) for the plan + [`handoff.md`](#3-handoffmd-never-lose-context) between sessions |

### 6.7 Derivations: ask for LaTeX *and* a numeric check

When AI derives a gradient, posterior, or ELBO update, ask it to (1) write the derivation step by step in LaTeX and (2) check it numerically: finite-difference gradients, or compare the closed form against Monte Carlo. A derivation that reads well is not necessarily correct.


### 6.8 Give AI documents as Markdown (MarkItDown)

[MarkItDown](https://github.com/microsoft/markitdown) converts PDF / Word / PPT / Excel to Markdown. That costs fewer tokens than having the model read the raw file, and headings and lists survive.

```bash
pip install 'markitdown[all]'
markitdown paper.pdf -o paper.md
# optional: let Claude convert files itself
pip install markitdown-mcp && claude mcp add markitdown -- markitdown-mcp
```

PDF equations and tables come out as plain text, so check them against the original (or use the arXiv LaTeX source / supplementary `.xlsx`).

---

## 7a. Make It a Skill

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

## 7b. find-skills & Top Skills

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
| **humanizer** (blader) | Remove AI-writing tells from prose | see [Part 4c](#4c-humanizer-remove-ai-writing-tells) |
| **obsidian-skills** (kepano) | If you keep notes in [Obsidian](https://obsidian.md): teaches the agent Obsidian Markdown (wikilinks, callouts), Bases, and Canvas | `npx skills add kepano/obsidian-skills` |
| **claude-scientific-skills** (K-Dense-AI) | Scientific packages and databases (scanpy, Biopython, PubMed, ...) | Large (100+ skills): install only what you need, e.g. `npx skills add K-Dense-AI/claude-scientific-skills --skill scanpy` |
| **nature-skills** | Academic workflow: literature search, paper reading, reference verification, polishing, reviewer responses, figures | `git clone https://github.com/Yuan1z0825/nature-skills` |
| **statgen-writing-style** (Gao) | Wang-group manuscript style | see [Part 4a](#4a-statgen-writing-style-write-like-the-lab) |
| **scientific-slides** (lab) | Lab-style talks as Beamer/PDF or editable PPTX | Claude Teams org skill; see [Part 5](#5-scientific-slides-talks-in-the-lab-style-beamerpdf-or-pptx) |

### Tips

- **Read a skill before installing it.** A skill is a set of instructions your agent will follow, possibly with scripts. Prefer well-known authors and check the repo.
- More skills is not better. Each skill's description takes up context. Install what you use, and remove the rest.

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
