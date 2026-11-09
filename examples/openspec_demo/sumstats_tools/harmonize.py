import pandas as pd

_KEY = ["CHR", "POS"]
_ALLELES = ["CHR", "POS", "A1", "A2"]
_AMBIGUOUS = {frozenset("AT"), frozenset("CG")}


def _require(df: pd.DataFrame, cols, name: str) -> None:
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise ValueError(f"{name} is missing required column(s): {', '.join(missing)}")


def harmonize(sumstats: pd.DataFrame, reference: pd.DataFrame):
    """Align sumstats effect alleles to a reference allele table.

    Returns (harmonized, removed). Swapped variants get A1/A2 swapped and BETA
    (and Z, if present) negated. Strand-ambiguous, unmatched and mismatched
    variants go to `removed` with a `reason` column.
    """
    _require(sumstats, _ALLELES + ["BETA"], "sumstats")
    _require(reference, _ALLELES, "reference")
    if reference.duplicated(_KEY).any():
        raise ValueError("reference has duplicated CHR:POS rows")

    ss = sumstats.copy()
    ss["A1"] = ss["A1"].str.upper()
    ss["A2"] = ss["A2"].str.upper()
    ref = reference[_ALLELES].rename(columns={"A1": "REF_A1", "A2": "REF_A2"}).copy()
    ref["REF_A1"] = ref["REF_A1"].str.upper()
    ref["REF_A2"] = ref["REF_A2"].str.upper()

    merged = ss.merge(ref, on=_KEY, how="left", indicator=True)
    ambiguous = [frozenset((a, b)) in _AMBIGUOUS for a, b in zip(merged["A1"], merged["A2"])]
    match = (merged["A1"] == merged["REF_A1"]) & (merged["A2"] == merged["REF_A2"])
    # A1 == A2 (e.g. A/A) satisfies both match and swap; never flip it
    swap = (merged["A1"] == merged["REF_A2"]) & (merged["A2"] == merged["REF_A1"]) & ~match

    reason = pd.Series("", index=merged.index)
    reason[(merged["_merge"] == "both") & ~match & ~swap] = "allele_mismatch"
    reason[merged["_merge"] == "left_only"] = "not_in_reference"
    reason[ambiguous] = "strand_ambiguous"
    keep = reason == ""

    out = merged[keep].copy()
    flip = swap[keep]
    out.loc[flip, ["A1", "A2"]] = out.loc[flip, ["A2", "A1"]].to_numpy()
    out.loc[flip, "BETA"] = -out.loc[flip, "BETA"]
    if "Z" in out.columns:
        out.loc[flip, "Z"] = -out.loc[flip, "Z"]

    harmonized = out[sumstats.columns].reset_index(drop=True)
    removed = merged.loc[~keep, _ALLELES].assign(reason=reason[~keep]).reset_index(drop=True)
    return harmonized, removed
