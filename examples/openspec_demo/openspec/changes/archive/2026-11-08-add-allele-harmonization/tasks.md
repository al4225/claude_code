# Tasks

## 1. Core harmonization

- [x] 1.1 Add `sumstats_tools/harmonize.py` with `harmonize(sumstats, reference)` validating required columns; verify a test that missing BETA raises `ValueError` naming the column
- [x] 1.2 Implement position join and match / swap / mismatch / not-in-reference classification; verify tests for an exact match (BETA unchanged) and a swapped variant (alleles swapped, BETA and Z negated)
- [x] 1.3 Remove strand-ambiguous A/T and C/G variants before matching; verify a test that A/T and C/G variants appear only in the removed table with reason `strand_ambiguous`
- [x] 1.4 Reject references with duplicated CHR:POS; verify a test that a duplicated reference raises `ValueError`
- [x] 1.5 Export `harmonize` from `sumstats_tools/__init__.py`; verify `from sumstats_tools import harmonize` works in tests

## 2. Integration check

- [x] 2.1 Simulated-data check: simulate 1,000 variants, swap alleles and negate BETA for a random 30%, harmonize against the true reference; verify every recovered BETA equals the true BETA and every input variant is in exactly one of the two output tables
- [x] 2.2 Run the full test suite with `pytest -q` and verify all tests pass

## Workflow follow-up

- Archive the change with `openspec archive add-allele-harmonization` after review.
