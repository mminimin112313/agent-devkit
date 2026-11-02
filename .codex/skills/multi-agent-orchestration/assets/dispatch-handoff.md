# Dispatch Handoff

```text
DISPATCH := {
  slice,
  objective_summary,
  scene_setting_context,
  independence_proof,
  shared_state_risk,
  sender_role,
  receiver_role,
  receiver_identity,
  receiver_opening_line,
  receiver_execution_position,
  receiver_owned_lane,
  receiver_forbidden_authority,
  identity_drift_instruction,
  clarification_rule,
  required_skills,
  decision_owner,
  verification_owner
}

SKILL_INPUTS := {
  required_local_agents,
  required_local_assets,
  required_local_references,
  required_local_scripts,
  usage_notes
}

SCOPE := {
  owned_files_or_concerns,
  shared_read_seams,
  forbidden_files_or_concerns,
  dependencies,
  public_seam,
  completion_criteria,
  self_review_required,
  report_format_contract
}

RETURN_SHAPE := {
  declared_identity,
  summary,
  findings,
  risks,
  open_questions,
  artifacts,
  actual_support_paths_used,
  actual_skills_used,
  actual_local_agents_used,
  actual_local_assets_used,
  actual_local_references_used,
  actual_local_scripts_used,
  deviations_from_dispatch,
  next_action
}

PASS IF
  DISPATCH.slice
  AND DISPATCH.receiver_identity
  AND DISPATCH.receiver_opening_line
  AND DISPATCH.receiver_execution_position
  AND DISPATCH.identity_drift_instruction
  AND DISPATCH.scene_setting_context
  AND DISPATCH.independence_proof
  AND DISPATCH.shared_state_risk
  AND DISPATCH.clarification_rule
  AND DISPATCH.required_skills
  AND SKILL_INPUTS.required_local_assets
  AND SCOPE.owned_files_or_concerns
  AND SCOPE.self_review_required
  AND SCOPE.report_format_contract
  AND RETURN_SHAPE.declared_identity
  AND RETURN_SHAPE.actual_support_paths_used
  AND RETURN_SHAPE.actual_local_assets_used

FAIL IF
  SCOPE.forbidden_files_or_concerns IS empty_when_overlap_risk_exists
  OR DISPATCH.receiver_opening_line IS missing
  OR DISPATCH.receiver_execution_position IS missing
  OR DISPATCH.identity_drift_instruction IS missing
  OR DISPATCH.scene_setting_context IS missing
  OR DISPATCH.independence_proof IS missing
  OR DISPATCH.shared_state_risk IS missing
  OR DISPATCH.clarification_rule IS missing
  OR SCOPE.self_review_required IS missing
  OR SCOPE.report_format_contract IS missing
  OR RETURN_SHAPE.declared_identity IS missing
  OR RETURN_SHAPE.actual_support_paths_used IS missing
  OR RETURN_SHAPE.declared_identity = DISPATCH.sender_role_without_explicit_justification
  OR RETURN_SHAPE.deviations_from_dispatch IS hidden
  OR RETURN_SHAPE.next_action IS missing
```
