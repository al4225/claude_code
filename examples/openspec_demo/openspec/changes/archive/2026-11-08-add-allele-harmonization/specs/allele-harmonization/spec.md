# Spec Delta

## Purpose

Align GWAS summary statistics to a reference allele table so that effect directions are consistent with the LD reference used downstream.

## ADDED Requirements

### Requirement: Matching variants are kept unchanged
The system SHALL keep variants whose CHR, POS, A1 and A2 match a reference row, without changing BETA or Z.

#### Scenario: Exact allele match
- **WHEN** a variant has A1=A, A2=G and the reference at the same CHR:POS has A1=A, A2=G
- **THEN** the variant is kept with its original BETA and Z

### Requirement: Swapped alleles are flipped
The system SHALL keep variants whose A1 and A2 are swapped relative to the reference, swap A1 and A2 to match the reference, and negate BETA and Z.

#### Scenario: Swapped alleles
- **WHEN** a variant has A1=G, A2=A, BETA=0.3 and the reference has A1=A, A2=G
- **THEN** the output variant has A1=A, A2=G and BETA=-0.3

### Requirement: Strand-ambiguous variants are removed
The system SHALL remove variants whose allele pair is A/T or C/G (in either order).

#### Scenario: A/T variant
- **WHEN** a variant has A1=A, A2=T
- **THEN** it is absent from the harmonized output and reported with reason `strand_ambiguous`

### Requirement: Unmatched variants are removed
The system SHALL remove variants with no reference row at the same CHR:POS, and variants whose alleles match neither orientation of the reference.

#### Scenario: Position not in reference
- **WHEN** a variant's CHR:POS is not in the reference
- **THEN** it is reported with reason `not_in_reference`

#### Scenario: Allele mismatch
- **WHEN** a variant has A1=A, A2=C and the reference has A1=A, A2=G at the same position
- **THEN** it is reported with reason `allele_mismatch`

### Requirement: Removed variants are reported
The system SHALL return, alongside the harmonized table, a table of every removed variant with its CHR, POS, A1, A2 and a reason.

#### Scenario: Audit table
- **WHEN** harmonization removes 3 variants
- **THEN** the removed-variants table has exactly 3 rows, each with a non-empty reason

### Requirement: Missing required columns fail loudly
The system SHALL raise an error if the summary statistics or the reference lack any of CHR, POS, A1, A2, or if the summary statistics lack BETA.

#### Scenario: Missing BETA
- **WHEN** summary statistics without a BETA column are harmonized
- **THEN** an error naming the missing column is raised
