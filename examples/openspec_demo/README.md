# OpenSpec Demo: `sumstats_tools`

A tiny, real Python package for GWAS summary statistics, developed with [OpenSpec](https://github.com/Fission-AI/OpenSpec) (v1.16.1). It shows both states of the OpenSpec workflow so you can **read a finished change** and **run one yourself**.

Back to the guide: [AI_Research_Toolkit.md §2](../../code/wiki/AI_Research_Toolkit.md#2-openspec-spec-driven-development)

## What's in here

```
openspec_demo/
├── openspec/
│   ├── config.yaml                      # project context + rules the AI must follow (statgen constraints)
│   ├── specs/
│   │   └── allele-harmonization/spec.md # LIVING SPEC: what the package does today (6 requirements)
│   └── changes/
│       ├── add-ld-matrix-check/         # ① PENDING change: proposal written, NOT implemented (0/6 tasks)
│       └── archive/
│           └── 2026-11-08-add-allele-harmonization/   # ② FINISHED change: proposed → applied → archived
├── sumstats_tools/
│   ├── zscore.py                        # original code (before OpenSpec)
│   └── harmonize.py                     # implemented by change ②
├── tests/                               # 13 tests, all passing
├── .claude/commands/opsx/               # /opsx:* slash commands for Claude Code (created by `openspec init`)
└── .agents/skills/                      # same workflows as skills for Codex
```

## Tour 1: read a finished change (5 min)

Read the files of change ② in this order. This is exactly what you would review in a real project:

1. `openspec/changes/archive/2026-11-08-add-allele-harmonization/proposal.md`: **why** (sign flips corrupt fine-mapping) and what's **out of scope**
2. `.../specs/allele-harmonization/spec.md`: **what** the behavior must be, as testable WHEN/THEN scenarios
3. `.../design.md`: **how**, with alternatives considered (e.g. why two output tables instead of a status column)
4. `.../tasks.md`: the checklist the AI worked through, each task with its verification
5. `sumstats_tools/harmonize.py` + `tests/test_harmonize.py`: the result
6. `openspec/specs/allele-harmonization/spec.md`: after archiving, the requirements were merged into the living spec

## Tour 2: do it yourself (15 min)

Requirements: Node ≥ 20, Python with `pandas`, `numpy`, `pytest`, and Claude Code (or Codex).

```bash
cd examples/openspec_demo
npm install -g @fission-ai/openspec@latest   # or prefix commands with: npx -y @fission-ai/openspec@latest
python -m pytest -q                          # 13 passed
openspec list                                # add-ld-matrix-check   0/6 tasks
openspec show add-ld-matrix-check            # read the pending proposal
```

**Step 1: review the pending proposal.** Open `openspec/changes/add-ld-matrix-check/`. Try editing it the way you would in real life, for example change the default tolerance in `specs/ld-matrix-validation/spec.md`, or add a requirement. Then run:

```bash
openspec validate add-ld-matrix-check --strict
```

**Step 2: implement it.** Start Claude Code in this folder and run:

```
/opsx:apply add-ld-matrix-check
```

The AI implements `sumstats_tools/ld_check.py` and its tests, ticking off `tasks.md` as it goes. Check with `python -m pytest -q` and `openspec list` (should show 6/6).

**Step 3: archive it.**

```
/opsx:archive add-ld-matrix-check
```

The AI will ask whether to sync the spec first. Answer **1 (sync now)**. `openspec/specs/` then has a second capability, `ld-matrix-validation` (check with `openspec list --specs`), and the change moves to `changes/archive/`.

**Step 4: propose your own.** For example:

```
/opsx:propose Add a function that computes Z from P-value and sign of BETA when SE is missing,
with a warning for P = 0 or P = 1.
```

> To reset the demo afterwards, run `git checkout -- . && git clean -fd .` inside this folder. This restores the committed version, so use it only in a clone of the repo, never on uncommitted work of your own.

**Tested end to end (2026-11-08):** in a fresh copy, headless Claude Code ran `/opsx:apply add-ld-matrix-check` (6/6 tasks, all tests passing), `/opsx:archive` (2 specs, both pass `openspec validate --specs --strict`), and the `/opsx:propose` example above (valid change, 11 tasks, no code edited). The AI's code and wording will differ from run to run.

## How change ② was produced

```bash
openspec init --tools claude,codex          # created openspec/, .claude/, .agents/
# edited openspec/config.yaml: project context (effect direction matters, fail loudly) + rules
openspec new change add-allele-harmonization
# wrote proposal → specs → design → tasks, following `openspec instructions <artifact> --change ...`
openspec validate add-allele-harmonization --strict   # valid
# implemented tasks.md; python -m pytest -q → 12 passed; ticked all tasks
openspec archive add-allele-harmonization --yes       # merged 6 requirements into openspec/specs/
```

**Codex caught a real bug here (2026-11-09).** An independent `codex exec` review (page Part 3, Option B) found that an A/A variant matched both "match" and "swap", so its BETA/Z got flipped. 12 tests passed and missed it. Fixed in `harmonize.py` with a regression test (`test_identical_alleles_not_flipped`).
