# Proposal

## Why

Summary-statistics fine-mapping (e.g. SuSiE-RSS) takes z-scores plus an LD matrix R. If R is not a valid correlation matrix, or if its variant order does not match the z-scores, results are wrong without any error. Users need a check that runs before fine-mapping and fails loudly.

## What Changes

- Add an LD-matrix validation step that takes an LD matrix and the harmonized summary statistics.
- It checks that R is square, symmetric, has a unit diagonal, has no missing values, and has dimension equal to the number of variants.
- It checks that R is positive semi-definite up to a user-set tolerance on the smallest eigenvalue.
- On failure it raises an error stating which check failed and by how much (e.g. the smallest eigenvalue).

**Out of scope:** repairing invalid matrices (e.g. shrinkage or nearest-PSD projection), computing LD from genotypes, and detecting LD mismatch between the reference panel and the GWAS sample.

## Capabilities

### New Capabilities
- `ld-matrix-validation`: checking that an LD matrix is a valid correlation matrix consistent with the summary statistics it will be paired with.

### Modified Capabilities
<!-- none -->

## Impact

- New public function in `sumstats_tools`.
- Uses numpy only; no new dependencies.
