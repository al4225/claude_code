Lab meeting notes - 2026-10-27

DEMO DATA: fictional notes created for the AI Research Toolkit example. Attendees are listed by role.

# Attendees

* PI
* Postdoc A
* Student B
* Student C

# 1. Fine-mapping on chr6 MHC block

Student B: SuSiE-RSS returns no credible sets for block 412 (MHC). Using the 1000G EUR LD panel. kriging\_rss diagnostic flags ~40 variants as possible allele flips.

PI: likely LD mismatch rather than a modelling problem. Try in-sample LD or the UKB EUR panel; do not increase L just to force credible sets.

# 2. Colocalization with eQTL

Postdoc A: coloc (single causal variant) gives PP.H4 = 0.31 at the APOE region but the locus clearly has two signals. Plan: run coloc on SuSiE credible sets (coloc.susie) and compare with ColocBoost.

# Decisions

|  |  |  |
| --- | --- | --- |
| Decision | Owner | Due |
| Switch block 412 to UKB EUR LD panel | Student B | 2026-11-03 |
| Harmonize alleles before every SuSiE-RSS run | Student B | 2026-11-03 |
| Compare coloc.susie vs ColocBoost at APOE | Postdoc A | 2026-11-10 |

# Action items

* Student C: write QC script for sumstats (build check, ambiguous SNPs)
* Everyone: write a handoff.md at the end of each analysis session