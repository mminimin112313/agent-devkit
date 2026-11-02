# Backend Handoff

```text
SUPPORT := {
  declared_assets,
  declared_references,
  files_read_before_coding,
  why_each_file_was_loaded,
  files_actually_used
}

SEAM := {
  name,
  sender_role,
  receiver_role,
  owner,
  parent_plan
}

CONTRACT := {
  entrypoint,
  input_shape,
  output_shape,
  dependency_edges,
  failure_mode,
  actionable_error_behavior,
  upstream_producers,
  downstream_consumers,
  consumer_impact,
  idempotency_expectation
}

DELIVERY := {
  changed_files,
  assumptions,
  side_effect_boundaries,
  baseline_evidence,
  bounded_runtime_behavior,
  query_or_caching_notes,
  static_validation_proof,
  required_follow_up,
  rollout_notes,
  performance_notes
}

VERIFICATION := {
  command,
  exact_output,
  result,
  runtime_proof,
  verification_owner
}

PASS IF
  SUPPORT.declared_assets IS named_or_none
  AND SUPPORT.declared_references IS named_or_none
  AND SUPPORT.files_read_before_coding
  AND SUPPORT.why_each_file_was_loaded
  AND SEAM.name
  AND CONTRACT.entrypoint
  AND VERIFICATION.command
  AND VERIFICATION.verification_owner

FAIL IF
  SUPPORT.files_actually_used IS missing
  OR CONTRACT.failure_mode IS implicit
```
