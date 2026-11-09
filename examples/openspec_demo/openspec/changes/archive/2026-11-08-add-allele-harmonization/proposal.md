# Proposal

## Why

GWAS summary statistics and LD reference panels often code the effect allele differently. If a variant's alleles are swapped relative to the reference, its z-score has the wrong sign, which silently corrupts fine-mapping and colocalization. The package currently has no way to align summary statistics to a reference panel.

## What Changes

- Add a harmonization step that aligns summary statistics to a reference allele table (CHR, POS, A1, A2).
- Variants whose alleles match the reference are kept unchanged.
- Variants whose alleles are swapped relative to the reference are kept, with A1/A2 swapped and the sign of BETA (and Z, if present) flipped.
- Strand-ambiguous variants (A/T, C/G) are dropped, because their orientation cannot be determined from alleles alone.
- Variants absent from the reference, or with alleles that match neither orientation, are dropped.
- Every dropped variant is reported with a reason, so users can audit what was removed.

**Out of scope:** strand flipping of non-ambiguous SNPs (e.g. A/G vs T/C), using allele frequencies to resolve ambiguous SNPs, indel normalization, and genome build liftover.

## Capabilities

### New Capabilities
- `allele-harmonization`: aligning summary-statistic effect alleles to a reference panel, including sign correction and reporting of removed variants.

### Modified Capabilities
<!-- none -->

## Impact

- New public function in `sumstats_tools`.
- No change to existing `add_zscore` behavior.
- No new dependencies (pandas, numpy only).
