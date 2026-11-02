# Routing Decision

```text
SUPPORT := {
  assets_declared_before_execution,
  references_declared_before_execution,
  files_read_before_routing,
  why_each_file_was_loaded,
  support_files_actually_used
}

DECISION := {
  request,
  intake_mode,
  considered_skills,
  recommended_skill,
  route_type,
  rationale,
  alternate_skills_considered,
  rejected_because,
  route_confidence,
  material_ambiguity,
  one_focused_clarification_question,
  blocked_actions_before_routing
}

BOUNDARY := {
  in_scope_now,
  not_in_scope_now,
  approval_needed,
  verification_expectation,
  severity
}

OWNERS := {
  decision_owner,
  next_owner,
  escalation_owner,
  informed_stakeholders
}

PASS IF
  SUPPORT.assets_declared_before_execution IS named_or_none
  AND SUPPORT.references_declared_before_execution IS named_or_none
  AND SUPPORT.files_read_before_routing
  AND SUPPORT.why_each_file_was_loaded
  AND DECISION.considered_skills
  AND DECISION.recommended_skill
  AND DECISION.rationale
  AND BOUNDARY.in_scope_now
  AND BOUNDARY.not_in_scope_now
  AND OWNERS.next_owner

FAIL IF
  DECISION.rejected_because IS missing
  OR DECISION.blocked_actions_before_routing IS missing
  OR SUPPORT.files_read_before_routing IS missing
  OR SUPPORT.support_files_actually_used IS missing
```
