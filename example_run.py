import json
import pandas as pd
from hive import HIVEExperiment

df = pd.read_csv("example_data.csv")

features = [
    "completion_rate",
    "reopen_rate",
    "blocked_fraction",
    "overdue_fraction",
    "dependency_density",
    "meeting_hours",
    "handoff_rate",
    "owner_concentration",
]

exp = HIVEExperiment(
    time_column="week",
    target_column="delivery_failure",
    feature_columns=features,
    horizons=(1,3,7,12),
    random_state=23,
)

result = exp.run(df)
print(json.dumps(result, indent=2))
