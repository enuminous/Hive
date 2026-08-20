import numpy as np
import pandas as pd

EPS = 1e-8

def robust_z(s, window=12):
    s = s.astype(float)
    med = s.rolling(window, min_periods=3).median()
    mad = (s-med).abs().rolling(window, min_periods=3).median()
    return ((s-med)/(1.4826*mad+EPS)).replace([np.inf,-np.inf], np.nan).fillna(0.0)

def build_hive_features(df, feature_columns, horizons=(1,3,7,12)):
    x = df[feature_columns].astype(float).copy()
    out = pd.DataFrame(index=df.index)

    # Local KPI state
    for c in feature_columns:
        out[f"{c}__z"] = robust_z(x[c], max(horizons))
        out[f"{c}__dx"] = x[c].diff().fillna(0.0)
        out[f"{c}__var"] = x[c].rolling(max(horizons), min_periods=2).var().fillna(0.0)

    # Cross-KPI tensions: pairs that often move in opposite operational directions.
    pairs = []
    for i, a in enumerate(feature_columns):
        for b in feature_columns[i+1:]:
            dname = f"pair__{a}__{b}__divergence"
            diff = robust_z(x[a], max(horizons)) - robust_z(x[b], max(horizons))
            out[dname] = diff.abs()
            pairs.append(dname)

    if pairs:
        out["interaction_stress"] = out[pairs].mean(axis=1)
        out["interaction_variance"] = out[pairs].var(axis=1).fillna(0.0)
    else:
        out["interaction_stress"] = 0.0
        out["interaction_variance"] = 0.0

    # Explicit organizational composites if fields exist.
    def col(name):
        return x[name] if name in x.columns else pd.Series(0.0, index=x.index)

    out["delivery_pressure"] = (
        col("overdue_fraction")
        + col("blocked_fraction")
        + col("reopen_rate")
        + col("handoff_rate")
    ) / 4.0

    out["coordination_load"] = (
        col("dependency_density")
        + col("meeting_hours").rank(pct=True)
        + col("owner_concentration")
    ) / 3.0

    out["throughput_conflict"] = (
        col("completion_rate").rank(pct=True)
        - out["delivery_pressure"].rank(pct=True)
    ).abs()

    for h in horizons:
        out[f"stress_mean_{h}"] = out["interaction_stress"].rolling(h, min_periods=1).mean()
        out[f"pressure_mean_{h}"] = out["delivery_pressure"].rolling(h, min_periods=1).mean()
        out[f"coordination_mean_{h}"] = out["coordination_load"].rolling(h, min_periods=1).mean()
        out[f"conflict_mean_{h}"] = out["throughput_conflict"].rolling(h, min_periods=1).mean()

    components = [
        out["interaction_stress"],
        out["interaction_variance"],
        out["delivery_pressure"],
        out["coordination_load"],
        out["throughput_conflict"],
    ]
    for h in horizons:
        components.extend([
            out[f"stress_mean_{h}"],
            out[f"pressure_mean_{h}"],
            out[f"coordination_mean_{h}"],
            out[f"conflict_mean_{h}"],
        ])

    ranked = pd.concat(components, axis=1).rank(pct=True)
    out["hive_risk_score"] = ranked.mean(axis=1).fillna(0.0)

    return out.replace([np.inf,-np.inf], np.nan).fillna(0.0)
