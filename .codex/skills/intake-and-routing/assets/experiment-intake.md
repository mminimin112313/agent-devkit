# Experiment Intake

```text
HYPOTHESIS := {
  idea,
  target_behavior,
  user_segment
}

BOUNDARIES := {
  primary_metric,
  guardrail_metric,
  stop_condition,
  rollback_trigger
}

ROUTING := {
  next_skill,
  approval_owner,
  missing_evidence
}

PASS IF
  HYPOTHESIS.idea
  AND BOUNDARIES.primary_metric
  AND BOUNDARIES.guardrail_metric
  AND ROUTING.next_skill

FAIL IF
  ROUTING.approval_owner IS missing
  OR ROUTING.missing_evidence IS hidden
```
