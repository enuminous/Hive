from dataclasses import dataclass
import pandas as pd
from features import build_hive_features
from baselines import LogisticModel, BaseRateModel
from metrics import binary_metrics

@dataclass
class HIVEExperiment:
    time_column: str
    target_column: str
    feature_columns: list
    horizons: tuple = (1,3,7,12)
    train_fraction: float = 0.65
    random_state: int = 23

    def run(self, df):
        df = df.sort_values(self.time_column).reset_index(drop=True).copy()
        cut = max(12, int(len(df)*self.train_fraction))
        y = df[self.target_column].astype(int).to_numpy()

        hf = build_hive_features(df, self.feature_columns, self.horizons)

        raw = df[self.feature_columns].astype(float).ffill().fillna(0.0)
        hive_X = pd.concat([raw, hf], axis=1).fillna(0.0)

        overdue_only = pd.DataFrame({
            "overdue_fraction": raw["overdue_fraction"] if "overdue_fraction" in raw else 0.0
        }, index=df.index)

        rework_only = pd.DataFrame({
            "reopen_rate": raw["reopen_rate"] if "reopen_rate" in raw else 0.0
        }, index=df.index)

        models = {
            "hive": (LogisticModel(self.random_state), hive_X),
            "raw_kpi": (LogisticModel(self.random_state), raw),
            "overdue_only": (LogisticModel(self.random_state), overdue_only),
            "rework_only": (LogisticModel(self.random_state), rework_only),
            "base_rate": (BaseRateModel(), raw),
        }

        results = {}
        for name, (model, X) in models.items():
            model.fit(X.iloc[:cut], y[:cut])
            p = model.predict_proba(X.iloc[cut:])
            results[name] = binary_metrics(y[cut:], p)

        return {
            "n_total": len(df),
            "train_n": cut,
            "test_n": len(df)-cut,
            "results": results,
            "primary_delta_brier_raw_minus_hive": (
                results["raw_kpi"]["brier"] - results["hive"]["brier"]
            ),
            "interpretation": (
                "Positive delta favors HIVE over the matched raw-KPI model. "
                "A negative delta means HIVE added complexity without improving Brier score."
            )
        }
