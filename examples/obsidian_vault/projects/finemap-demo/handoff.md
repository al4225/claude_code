# Handoff: finemap-demo, chr6 block 412  (updated 2026-11-05 18:10)

## Goal
Sensible credible sets for every LD block, including block 412 (MHC), before running colocalization with eQTL.

## Current state
- Done: allele harmonization; block 412 re-run with UKB EUR LD → 2 credible sets.
- In progress: checking whether the 2 remaining flagged variants are real flips (`scripts/check_flips.R`).
- Not started: coloc.susie at APOE ([[wallace2021_coloc-susie]]).

## Key decisions (and why)
- UKB EUR LD instead of 1000G EUR: see [[projects/finemap-demo/decisions|decisions]].

## What we tried that did NOT work
- L = 20 with 1000G LD: still no credible sets. The problem is [[LD-mismatch]], not L.

## Next steps (in order)
1. Resolve the 2 flagged variants; drop them if they are flips that harmonization can't fix.
2. Re-run all blocks with the harmonized pipeline.
3. Run coloc.susie at APOE and compare with ColocBoost.

## Key files / commands
- `scripts/run_susie_rss.sh 412` (entry point), `results/block412/`, `logs/`
