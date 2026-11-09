# Spec Delta

## Purpose

Catch invalid or mismatched LD matrices before they are used for summary-statistics fine-mapping, so errors surface as clear messages instead of wrong results.

## ADDED Requirements

### Requirement: Dimensions match the summary statistics
The system SHALL raise an error if the LD matrix is not square or its dimension differs from the number of summary-statistic variants.

#### Scenario: Dimension mismatch
- **WHEN** an LD matrix of size 99 x 99 is checked against 100 variants
- **THEN** an error stating both sizes is raised

### Requirement: Matrix is a valid correlation matrix
The system SHALL raise an error if the LD matrix contains missing values, is not symmetric within 1e-8, or has diagonal entries that differ from 1 by more than 1e-6.

#### Scenario: Asymmetric matrix
- **WHEN** R[0,1] = 0.5 and R[1,0] = 0.4
- **THEN** an error mentioning symmetry is raised

#### Scenario: Missing value
- **WHEN** the LD matrix contains NaN
- **THEN** an error mentioning missing values is raised

### Requirement: Matrix is positive semi-definite within tolerance
The system SHALL raise an error if the smallest eigenvalue of the LD matrix is below minus the tolerance (default 1e-6), and the error SHALL report the smallest eigenvalue.

#### Scenario: Clearly non-PSD matrix
- **WHEN** a 3 x 3 matrix with smallest eigenvalue -0.2 is checked with default tolerance
- **THEN** an error reporting -0.2 is raised

#### Scenario: Small numerical noise is accepted
- **WHEN** the smallest eigenvalue is -1e-9 and the tolerance is 1e-6
- **THEN** validation passes

### Requirement: Valid matrices pass silently
The system SHALL return without error and without modifying the input when all checks pass.

#### Scenario: Valid LD matrix
- **WHEN** a correlation matrix computed from simulated genotypes is checked against matching summary statistics
- **THEN** no error is raised and the matrix is unchanged
