# Dependency Risk Review

```text
PASS IF
  upstream_prerequisite_state_is_known
  AND external_owner_is_named_when_present
  AND hidden_contract_or_schema_dependency_is_checked
  AND consumer_blast_radius_is_checked
  AND security_qa_or_release_gates_are_recorded
  AND rollback_sensitivity_is_noted_when_relevant

FAIL IF
  blocker_owner_is_unknown
  OR unblock_event_is_implicit
  OR single_agent_vs_orchestration_decision_is_avoided
```
