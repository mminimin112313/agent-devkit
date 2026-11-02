# Data Workflow Review Lens

Changes that move data or schedule work need a lineage-aware review, not just a code review.

```text
USE_THIS_LENS IF change_moves_data OR schedules_work

REVIEW_QUESTIONS := {
  producers_consumers_and_dependency_edges,
  static_validation_that_proves_structural_soundness,
  runtime_proof_that_shows_execution_behavior_is_correct,
  migration_replay_or_reprocessing_proof_required_after_change,
  upstream_assumptions_checked,
  downstream_breakage_or_blast_radius_considered,
  prevention_for_drift_malformed_data_or_stale_delivery
}
```
