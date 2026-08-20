import pandas as pd
from features import build_hive_features
from hive import HIVEExperiment

FEATURES = [
    "completion_rate",
    "reopen_rate",
    "blocked_fraction",
    "overdue_fraction",
    "dependency_density",
    "meeting_hours",
    "handoff_rate",
    "owner_concentration",
]

def test_features():
    df = pd.read_csv("example_data.csv")
    hf = build_hive_features(df, FEATURES)
    assert len(hf) == len(df)
    assert "hive_risk_score" in hf.columns
    assert hf["hive_risk_score"].between(0,1).all()

def test_experiment_runs():
    df = pd.read_csv("example_data.csv")
    exp = HIVEExperiment(
        time_column="week",
        target_column="delivery_failure",
        feature_columns=FEATURES,
    )
    out = exp.run(df)
    assert "results" in out
    assert "hive" in out["results"]
    assert "raw_kpi" in out["results"]
