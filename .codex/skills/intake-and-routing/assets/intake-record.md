# Intake Record

```text
SUPPORT := {
  assets_declared_before_execution,
  references_declared_before_execution,
  files_read_before_routing,
  why_each_file_was_loaded,
  support_files_actually_used
}

REQUEST := {
  request,
  target_outcome,
  success_condition,
  constraints,
  explicit_non_goals
}

CLASSIFICATION := {
  context_checked_before_routing,
  dominant_track,
  considered_next_skills,
  likely_next_skill,
  route_type,
  route_rationale,
  alternate_route_considered,
  rejected_because,
  design_required_before_implementation,
  missing_inputs,
  material_ambiguity,
  one_focused_clarification_question,
  blocked_actions_before_routing,
  escalation_needed
}

OWNERSHIP := {
  decision_owner,
  verification_owner,
  receiving_owner
}

CLOSE := {
  route_chosen,
  blocker,
  next_action,
  follow_up_question
}

PASS IF
  SUPPORT.assets_declared_before_execution IS named_or_none
  AND SUPPORT.references_declared_before_execution IS named_or_none
  AND SUPPORT.files_read_before_routing
  AND SUPPORT.why_each_file_was_loaded
  AND REQUEST.target_outcome
  AND REQUEST.success_condition
  AND CLASSIFICATION.considered_next_skills
  AND CLASSIFICATION.likely_next_skill
  AND CLASSIFICATION.route_rationale
  AND OWNERSHIP.receiving_owner
  AND CLOSE.route_chosen

FAIL IF
  REQUEST.explicit_non_goals IS missing
  OR CLASSIFICATION.material_ambiguity IS hidden
  OR CLASSIFICATION.blocked_actions_before_routing IS missing
  OR CLASSIFICATION.rejected_because IS missing
  OR SUPPORT.files_read_before_routing IS missing
  OR SUPPORT.support_files_actually_used IS missing
```
