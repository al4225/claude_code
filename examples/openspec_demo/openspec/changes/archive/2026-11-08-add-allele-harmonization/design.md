# Design

## Context

`sumstats_tools` currently only computes Z from BETA/SE. Inputs are pandas DataFrames (see project context). See proposal.md for motivation.

## Goals / Non-Goals

**Goals:**
- Vectorized implementation (pandas merge), usable on millions of variants.
- Deterministic, auditable output: every input variant is either in the harmonized table or in the removed table.

**Non-Goals:**
- Handling multi-allelic sites as more than one row per CHR:POS in the reference (reference is assumed to have unique CHR:POS).

## Decisions

- **API: `harmonize(sumstats, reference) -> (harmonized, removed)`** returning two DataFrames.
  Alternative considered: a single table with a `status` column. Rejected because downstream code would have to remember to filter, which reintroduces the risk of using unaligned variants.
- **Join on CHR:POS, then compare alleles**, rather than joining on CHR:POS:A1:A2. Joining on position first lets us distinguish `not_in_reference` from `allele_mismatch`, which the spec requires.
- **Ambiguity check before matching.** A/T and C/G variants are removed even if they appear to match, because a strand flip would look identical.
- **Allele comparison is case-insensitive**; alleles are upper-cased in the output.
- **Z is flipped only if present**, so harmonization can run before or after `add_zscore`.

## Risks / Trade-offs

- [Dropping all A/T and C/G SNPs loses ~15% of variants] → Accept for now; frequency-based resolution is listed as out of scope and can be added later.
- [Duplicate CHR:POS in the reference would duplicate variants] → Raise an error if the reference has duplicated CHR:POS.
