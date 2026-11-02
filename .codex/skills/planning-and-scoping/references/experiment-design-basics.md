# Experiment Design Basics

```text
PASS IF
  hypothesis_is_named
  AND target_segment_is_named
  AND primary_metric_is_named
  AND guardrail_metric_is_named
  AND sample_or_evidence_threshold_is_named
  AND stop_condition_is_named
  AND rollback_trigger_is_named

FAIL IF
  decision_to_unlock_is_missing
  OR multiple_changes_are_bundled_into_one_test
  OR rollout_or_rollback_owner_is_missing
  OR instrumentation_check_is_missing
```
