# Tasks

## 1. LD matrix check

- [ ] 1.1 Add `sumstats_tools/ld_check.py` with `check_ld(R, sumstats, tol=1e-6)` implementing the shape check; verify a test that a 99 x 99 matrix against 100 variants raises `ValueError` with both sizes
- [ ] 1.2 Add NaN, symmetry and unit-diagonal checks; verify one test per check that the error message names the failed check
- [ ] 1.3 Add the PSD check with `eigvalsh`; verify a test that a matrix with smallest eigenvalue -0.2 raises with "-0.2" in the message, and a test that -1e-9 passes at default tolerance
- [ ] 1.4 Export `check_ld` from `sumstats_tools/__init__.py`; verify `from sumstats_tools import check_ld` works in tests

## 2. Integration check

- [ ] 2.1 Simulated-data check: simulate genotypes (n=500, p=50) with LD, compute R with `numpy.corrcoef`, verify `check_ld` passes and R is unchanged
- [ ] 2.2 Run `pytest -q` and verify all tests pass

## Workflow follow-up

- Archive with `openspec archive add-ld-matrix-check` after review.
