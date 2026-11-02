# Experiment Brief

```text
EXPERIMENT := {
  hypothesis,
  user_segment,
  target_seam,
  primary_metric,
  guardrail_metric,
  expected_effect,
  stop_condition,
  rollback_trigger,
  owner,
  implementation_path,
  review_path,
  release_path
}

PASS IF
  EXPERIMENT.hypothesis
  AND EXPERIMENT.primary_metric
  AND EXPERIMENT.guardrail_metric
  AND EXPERIMENT.stop_condition
  AND EXPERIMENT.rollback_trigger

FAIL IF
  EXPERIMENT.owner IS missing
  OR EXPERIMENT.review_path IS implicit
```
