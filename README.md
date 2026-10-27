# HIVE

<!-- ENUMINOUS-UNIFIED-NAV:START -->
## Repository navigation

**eNuminous network:** [All public repositories](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md) · [EFMW](https://github.com/enuminous/EFMW) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Zoo](https://github.com/enuminous/Tortoise) · [Papers](https://github.com/enuminous/papers) · [Quantum geometry](https://github.com/enuminous/Base888-Quantum-Geometry)

**This project:** [Repository home](https://github.com/enuminous/Hive) · [Subject index](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md#zoo-index-and-agents)

<details open>
<summary><strong>On this page</strong></summary>

- [Intended uses](#intended-uses)
- [Core signal path](#core-signal-path)
- [Flat-stack repository](#flat-stack-repository)
- [Scientific hypothesis](#scientific-hypothesis)
- [Example signals](#example-signals)
- [Baselines](#baselines)
- [Primary endpoint](#primary-endpoint)
- [Installation](#installation)
- [Run example](#run-example)
- [Tests](#tests)
- [Minimal usage](#minimal-usage)
- [Freeze discipline](#freeze-discipline)
- [Negative results](#negative-results)
- [Status](#status)


</details>

**Related repositories:** [Tortoise](https://github.com/enuminous/Tortoise) · [Monolithic-Zoo-Lean4](https://github.com/enuminous/Monolithic-Zoo-Lean4) · [Monolithic-102-Zoo-Lean4](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Eagle](https://github.com/enuminous/Eagle) · [Gecko](https://github.com/enuminous/Gecko) · [Crab](https://github.com/enuminous/Crab) · [Octopus](https://github.com/enuminous/Octopus)

> **Evidence boundary:** A link between projects is navigation, not an assertion of proven equivalence, experimental validation, or shared authorship. See each repository’s own status and review notes.
<!-- ENUMINOUS-UNIFIED-NAV:END -->


**Hierarchical Interaction and Variance Engine**

HIVE is an EFMW-derived framework for organizational and project-system reliability.

Its narrow question is:

> Can distributed changes in task flow, ownership, dependencies, meeting load, rework, and delivery variance reveal organizational failure before conventional project status indicators do?

## Intended uses

- software projects
- operations teams
- product launches
- research programs
- multi-team programs
- service organizations
- incident-response organizations
- complex delivery programs

## Core signal path

```text
work events
→ team / owner state
→ dependency structure
→ variance and rework
→ interaction stress
→ ownership concentration
→ multiscale coordination state
→ delivery-risk score
```

## Flat-stack repository

```text
README.md
LICENSE
CITATION.cff
pyproject.toml
requirements.txt
hive.py
features.py
baselines.py
metrics.py
freeze.py
risk_schema.json
example_config.yaml
example_data.csv
example_run.py
test_hive.py
MANIFEST.sha256
```

## Scientific hypothesis

> In distributed organizations, impending delivery failure may appear first as changing relationships among workstreams rather than as a single late task.

HIVE does not assume this hypothesis is correct.

## Example signals

- task completion rate
- reopened-work rate
- overdue fraction
- blocked-task fraction
- dependency density
- owner concentration
- meeting load
- handoff frequency
- variance in cycle time
- coordination contradiction
- cross-team divergence

## Baselines

Included:

- raw KPI logistic model
- overdue-rate baseline
- rework baseline
- deadline-slippage baseline
- base-rate predictor

## Primary endpoint

For a frozen delivery-failure definition:

> At matched information cutoff, does HIVE improve probabilistic prediction of later project failure over simpler KPI models?

## Installation

```bash
python -m pip install -r requirements.txt
```

## Run example

```bash
python example_run.py
```

## Tests

```bash
pytest -q
```

## Minimal usage

```python
import pandas as pd
from hive import HIVEExperiment

df = pd.read_csv("example_data.csv")

exp = HIVEExperiment(
    time_column="week",
    target_column="delivery_failure",
    feature_columns=[
        "completion_rate",
        "reopen_rate",
        "blocked_fraction",
        "overdue_fraction",
        "dependency_density",
        "meeting_hours",
        "handoff_rate",
        "owner_concentration",
    ],
    horizons=(1, 3, 7, 12),
)

print(exp.run(df))
```

## Freeze discipline

Freeze before testing:

- KPI definitions
- team/project unit
- failure definition
- information cutoff
- horizons
- feature construction
- score weights
- baselines
- model capacity
- metrics
- exclusions
- seeds

Then run:

```bash
python freeze.py
```

## Negative results

If simple project KPIs or conventional models match HIVE, then the HIVE-specific relational architecture has not demonstrated incremental value.

## Status

Research software. Experimental. Not validated for employment decisions, personnel scoring, or automated disciplinary action.
