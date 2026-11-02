# Backend Docs Gates

```text
UPDATE_DOCS_OR_HANDOFF IF
  api_shape_changed
  OR job_contract_changed
  OR new_runtime_dependency_was_introduced
  OR operator_needs_rollout_or_rollback_context
  OR consumer_must_adapt_to_new_data_semantics

HANDOFF_READY := PASS IF
  changed_seam
  AND affected_consumers
  AND remaining_risk_are_recorded

FAIL IF seam_changed AND handoff_stayed_vague
```
