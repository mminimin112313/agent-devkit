# Task Breakdown Stub

```text
FRAMING := {
  feature_name,
  goal_line,
  architecture_summary,
  tech_stack,
  intended_audience,
  decision_to_unlock,
  source_inputs
}

GOAL := {
  target,
  seam,
  source_requirement_or_artifact,
  owned_proof_path,
  created_files,
  modified_files,
  test_files,
  file_responsibilities
}

CURRENT_STEP := {
  active_step,
  bite_sized_steps,
  size,
  owner,
  clean_stop_point
}

UPCOMING_PATH := {
  next_1,
  next_2,
  cut_point_or_review_gate
}

TRACEABILITY := {
  requirement_ids,
  acceptance_ids,
  proof_artifact_or_command,
  receiving_owner
}

BOUNDARIES := {
  non_goals,
  parked_follow_ups,
  blockers,
  dependency_order,
  assumptions_to_confirm,
  acceptance_note,
  next_skill
}

PASS IF
  FRAMING.feature_name
  AND FRAMING.goal_line
  CURRENT_STEP.active_step
  AND CURRENT_STEP.bite_sized_steps
  AND CURRENT_STEP.clean_stop_point
  AND TRACEABILITY.proof_artifact_or_command

FAIL IF
  GOAL.file_responsibilities IS missing
  UPCOMING_PATH.next_1 IS missing
  OR BOUNDARIES.next_skill IS implicit
```
