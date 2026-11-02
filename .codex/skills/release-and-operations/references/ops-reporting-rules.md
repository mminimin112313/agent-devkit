# Ops Reporting Rules

Operational reporting should reduce uncertainty quickly.

```text
REPORT_SHAPE := {
  current_status,
  user_impact,
  evidence_source,
  confidence_or_uncertainty,
  next_action,
  next_update_time IF unresolved
}

FAILURE_MODES := {
  vague_monitoring_claims,
  no_owner_for_next_action,
  speculation_mixed_with_confirmed_facts
}

PASS IF
  every_field_in(REPORT_SHAPE) IS present_when_relevant
  AND uncertainty_is_labeled_instead_of_hidden
  AND next_action_has_a_named_owner

FAIL IF
  report_matches_any(FAILURE_MODES)
```
