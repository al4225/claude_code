import numpy as np
import pandas as pd
import pytest

from sumstats_tools import add_zscore


def test_zscore_basic():
    df = pd.DataFrame({"BETA": [0.2, -0.1], "SE": [0.1, 0.05]})
    assert add_zscore(df)["Z"].tolist() == pytest.approx([2.0, -2.0])


def test_zero_se_gives_nan():
    df = pd.DataFrame({"BETA": [0.2], "SE": [0.0]})
    assert np.isnan(add_zscore(df)["Z"].iloc[0])


def test_missing_columns():
    with pytest.raises(ValueError):
        add_zscore(pd.DataFrame({"BETA": [0.1]}))
