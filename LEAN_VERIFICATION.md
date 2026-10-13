# Shared Lean 4 verification for Hive

The selected formal core is maintained in the shared [Monolithic Zoo package](https://github.com/enuminous/Monolithic-Zoo-Lean4).

- Checked module: [Hive.lean](https://github.com/enuminous/Monolithic-Zoo-Lean4/blob/44d9881e8878a702fdfa47da53d80436276d92a6/Hive.lean).
- Verified package commit: `44d9881e8878a702fdfa47da53d80436276d92a6`.
- Successful workflow: [38484522045](https://github.com/enuminous/Monolithic-Zoo-Lean4/actions/runs/38484522045).
- Selected upstream source revision: [`e66e03d67c19f1f1e663a2a7feaea9f21c48384e`](https://github.com/enuminous/Hive/commit/e66e03d67c19f1f1e663a2a7feaea9f21c48384e); preserved source blobs and hashes are in the shared package's `UPSTREAM_SOURCES.json`.
- Scope: rank aggregation of precomputed component columns; feature extraction and model training not ported.
- Named theorem declarations: `Zoo.Hive.output_length`, `Zoo.Hive.valid_column_count`, `Zoo.Hive.report_requires_freeze`.

The run passed the pinned Lean build, strict axiom audit, audit rejection controls,
90 finite reference comparisons across the shared package, and the 46-module roster.
These are package-level checks; they do not mean that 90 tests belong to this animal.

This evidence covers the selected core and its stated hypotheses. It does not
certify this repository's complete Python pipeline, feature extraction, training,
all floating-point edge cases, or empirical effectiveness. The shared
[coverage ledger](https://github.com/enuminous/Monolithic-Zoo-Lean4/blob/main/COVERAGE.md)
and [remaining obligations](https://github.com/enuminous/Monolithic-Zoo-Lean4/blob/main/FORMALIZATION_NOTES.md)
preserve those limits. Future source changes require a fresh correspondence review.

Reuse the pinned shared package instead of maintaining a divergent proof copy here.
