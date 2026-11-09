# Design

## Context

`harmonize` (see `openspec/specs/allele-harmonization/spec.md`) produces aligned summary statistics. This change adds the matching check on the LD side. See proposal.md for motivation.

## Goals / Non-Goals

**Goals:**
- One call, `check_ld(R, sumstats, tol=1e-6)`, that raises on the first failed check with a specific message.

**Non-Goals:**
- Speed on very large matrices (> 20k variants); a full eigendecomposition is acceptable at fine-mapping block sizes.

## Decisions

- **Use `numpy.linalg.eigvalsh`** (symmetric eigenvalues) for the PSD check, after the symmetry check passes. Alternative: Cholesky, which is faster but only says pass/fail and can't report how negative the matrix is.
- **Check order: shape → NaN → symmetry → diagonal → PSD**, so the cheapest and most informative checks run first and `eigvalsh` only sees symmetric input.
- **Raise `ValueError`** like the rest of the package; no custom exception class.

## Risks / Trade-offs

- [Default tolerance may reject matrices from small reference panels that are slightly non-PSD] → Tolerance is a parameter; the error message reports the eigenvalue so users can decide.
