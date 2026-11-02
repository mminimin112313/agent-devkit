# Plan Record

```text
SUPPORT := {
  assets_declared_before_execution,
  references_declared_before_execution,
  files_read_before_scoping,
  why_each_file_was_loaded,
  support_files_actually_used,
  isolated_workspace_path,
  isolated_workspace_verified
}

FRAMING := {
  feature_name,
  intended_audience,
  decision_to_unlock,
  influence_goal,
  source_inputs,
  goal_line,
  architecture_summary,
  tech_stack,
  plan_scaffold_created,
  section_order,
  sections_left_as_placeholders
}

GOAL := {
  delivery_target,
  source_requirement_or_artifact,
  source_quote_or_finding,
  source_last_confirmed,
  requirement_freshness,
  approval_owner,
  design_presented_and_user_approved,
  owned_seam,
  owned_files_or_surface,
  non_goals,
  assumptions_that_may_go_stale,
  dependency_risks_or_blockers,
  producer_or_consumer_impact,
  created_files,
  modified_files,
  test_files,
  file_responsibilities
}

TRACEABILITY := {
  requirement_or_decision_id,
  planned_change,
  acceptance_id,
  exact_proof_path
}

ACCEPTANCE := {
  acceptance_wording,
  negative_or_blocked_path,
  approval_owner
}

CURRENT_STEP := {
  active_step,
  active_step_full_text,
  bite_sized_steps,
  executor_context,
  exact_executor,
  exact_verifier,
  exact_receiver,
  proof_path,
  verification_command_or_evidence,
  expected_failure_or_red_signal,
  clean_stop_point,
  blockers
}

CURRENT_STEP.active_step_full_text := exact_step_text_ready_for_execution_without_replanning
CURRENT_STEP.executor_context := bounded_scene_setting_without_replanning
CURRENT_STEP.expected_failure_or_red_signal := what_should_fail_or_block_before_green

PARKED := {
  parked_follow_up_1,
  parked_follow_up_2,
  parked_follow_up_3_or_cut_point,
  execution_mode_recommendation
}

PARKED.execution_mode_recommendation := subagent_driven OR parallel_session
UPCOMING.execution_mode_recommendation := subagent_driven OR parallel_session

OWNERSHIP := {
  decision_owner,
  implementation_owner,
  verification_owner,
  receiving_owner
}

PROOF := {
  proof_expected,
  exact_proof_path,
  verification_command_or_evidence,
  fresh_reader_questions,
  fresh_reader_findings
}

CLOSE := {
  stop_condition,
  unresolved_risks,
  recheck_trigger,
  next_skill
}

PASS IF
  SUPPORT.assets_declared_before_execution IS named_or_none
  AND SUPPORT.references_declared_before_execution IS named_or_none
  AND SUPPORT.files_read_before_scoping
  AND SUPPORT.why_each_file_was_loaded
  AND SUPPORT.isolated_workspace_verified
  AND FRAMING.feature_name
  AND FRAMING.goal_line
  AND FRAMING.architecture_summary
  AND FRAMING.tech_stack
  AND FRAMING.plan_scaffold_created
  AND FRAMING.section_order
  AND GOAL.delivery_target
  AND GOAL.source_quote_or_finding
  AND GOAL.approval_owner
  AND GOAL.design_presented_and_user_approved
  AND GOAL.owned_seam
  AND GOAL.owned_files_or_surface
  AND GOAL.file_responsibilities
  AND GOAL.non_goals
  AND ACCEPTANCE.acceptance_wording
  AND CURRENT_STEP.active_step
  AND CURRENT_STEP.bite_sized_steps
  AND CURRENT_STEP.exact_executor
  AND CURRENT_STEP.exact_verifier
  AND CURRENT_STEP.exact_receiver
  AND CURRENT_STEP.clean_stop_point
  AND PROOF.exact_proof_path
  AND PROOF.verification_command_or_evidence
  AND CLOSE.stop_condition
  AND CLOSE.next_skill
  AND PROOF.fresh_reader_questions
  AND PROOF.fresh_reader_findings

FAIL IF
  TRACEABILITY.exact_proof_path IS missing
  OR CURRENT_STEP.active_step_full_text IS vague
  OR CURRENT_STEP.bite_sized_steps IS vague
  OR FRAMING.sections_left_as_placeholders IS missing_when_a_section_is_not_ready
  OR OWNERSHIP.implementation_owner IS missing
  OR OWNERSHIP.verification_owner IS missing
  OR OWNERSHIP.receiving_owner IS missing
  OR PROOF.fresh_reader_findings IS missing
  OR SUPPORT.files_read_before_scoping IS missing
  OR SUPPORT.isolated_workspace_verified IS missing_when_execution_requires_isolation
  OR SUPPORT.support_files_actually_used IS missing
```
