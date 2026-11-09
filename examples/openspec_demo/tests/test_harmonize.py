import numpy as np
import pandas as pd
import pytest

from sumstats_tools import add_zscore, harmonize

REF = pd.DataFrame(
    {"CHR": [1, 1, 1, 1, 1], "POS": [100, 200, 300, 400, 500],
     "A1": ["A", "A", "A", "C", "A"], "A2": ["G", "G", "T", "G", "G"]}
)


def ss(rows):
    return pd.DataFrame(rows, columns=["CHR", "POS", "A1", "A2", "BETA"])


def test_exact_match_unchanged():
    h, r = harmonize(ss([[1, 100, "A", "G", 0.3]]), REF)
    assert h["BETA"].tolist() == [0.3] and r.empty


def test_swapped_alleles_flipped():
    h, _ = harmonize(ss([[1, 200, "G", "A", 0.3]]), REF)
    row = h.iloc[0]
    assert (row["A1"], row["A2"]) == ("A", "G")
    assert row["BETA"] == pytest.approx(-0.3)


def test_swapped_alleles_flip_z():
    df = add_zscore(ss([[1, 200, "G", "A", 0.3]]).assign(SE=0.1))
    h, _ = harmonize(df, REF)
    assert h["Z"].iloc[0] == pytest.approx(-3.0)


def test_lowercase_alleles():
    h, _ = harmonize(ss([[1, 100, "a", "g", 0.3]]), REF)
    assert h["A1"].iloc[0] == "A"


def test_strand_ambiguous_removed():
    h, r = harmonize(ss([[1, 300, "A", "T", 0.1], [1, 400, "C", "G", 0.2]]), REF)
    assert h.empty
    assert r["reason"].tolist() == ["strand_ambiguous", "strand_ambiguous"]


def test_not_in_reference_and_mismatch():
    h, r = harmonize(ss([[2, 100, "A", "G", 0.1], [1, 500, "A", "C", 0.2]]), REF)
    assert h.empty
    assert r["reason"].tolist() == ["not_in_reference", "allele_mismatch"]


def test_missing_beta_raises():
    with pytest.raises(ValueError, match="BETA"):
        harmonize(pd.DataFrame({"CHR": [1], "POS": [1], "A1": ["A"], "A2": ["G"]}), REF)


def test_duplicated_reference_raises():
    with pytest.raises(ValueError, match="duplicated"):
        harmonize(ss([[1, 100, "A", "G", 0.3]]), pd.concat([REF, REF.iloc[:1]]))


def test_identical_alleles_not_flipped():
    # Found by Codex review: A/A matched both "match" and "swap" and got its sign flipped
    ref = pd.DataFrame({"CHR": [1], "POS": [100], "A1": ["A"], "A2": ["A"]})
    h, _ = harmonize(ss([[1, 100, "A", "A", 0.5]]), ref)
    assert h["BETA"].iloc[0] == 0.5


def test_simulated_recovery():
    rng = np.random.default_rng(1)
    n = 1000
    pairs = np.array([("A", "G"), ("A", "C"), ("C", "T"), ("G", "T")])
    alleles = pairs[rng.integers(0, len(pairs), n)]
    ref = pd.DataFrame({"CHR": 1, "POS": np.arange(n), "A1": alleles[:, 0], "A2": alleles[:, 1]})
    true_beta = rng.normal(0, 0.1, n)
    swap = rng.random(n) < 0.3
    obs = ref.copy()
    obs.loc[swap, ["A1", "A2"]] = obs.loc[swap, ["A2", "A1"]].to_numpy()
    obs["BETA"] = np.where(swap, -true_beta, true_beta)

    h, r = harmonize(obs, ref)
    assert len(h) + len(r) == n
    assert np.allclose(h.sort_values("POS")["BETA"].to_numpy(), true_beta)
