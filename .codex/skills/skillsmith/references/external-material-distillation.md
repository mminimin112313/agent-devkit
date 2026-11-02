# External Material Distillation

When importing from another repo, absorb procedure and judgment, not theater.

```text
KEEP := {
  workflows,
  decision_criteria,
  evidence_requirements,
  failure_guards,
  reusable_record_shapes,
  small_examples_only_when_they_materially_prevent_misuse
}

STRIP := {
  persona_fluff,
  fake_memory_or_identity_claims,
  vanity_success_metrics_with_no_enforcement_mechanism,
  stack_or_vendor_specific_defaults_outside_target_skill_ownership,
  vendor_specific_skill_surfaces_without_active_repo_local_owner,
  document_output_specific_skill_surfaces_without_active_repo_local_owner,
  media_production_specific_skill_surfaces_without_active_repo_local_owner,
  giant_example_code_blocks_unless_repeatedly_reusable,
  aspirational_best_practice_code_with_no_stable_operator_value
}

CATALOG_NON_FIT := PASS IF
  vendor_specific_skill_has_no_active_repo_local_owner
  OR document_output_skill_would_require_a_new_top_level_surface_without_admission_justification
  OR media_production_skill_is_artifact_or_asset_focused_without_reusable_repo_local_decision_logic

CATALOG_NON_FIT_ACTION := {
  record_non_fit_reason,
  keep_the_active_catalog_unchanged,
  absorb_only_general_packaging_or_guardrail_lessons_when_they_transfer_cleanly,
  reject_parallel_authority
}

DISPOSITION := {
  absorbed,
  generalized_only,
  rejected
}

GENERALIZE_ONLY IF
  active_repo_local_owner_exists
  AND reusable_rule_survives_after_vendor_or_product_specific_surface_is_removed

EXCLUDE_AS_NON_FIT IF
  imported_surface_is(vendor_specific OR document_output_specific OR media_production_specific)
  AND active_repo_local_owner_exists = FALSE

PLACEMENT_RULES := {
  trigger_or_gate_behavior -> SKILL.md,
  narrow_role_execution_stance -> agents/*.md,
  durable_domain_knowledge -> references/*.md,
  reusable_operational_artifact -> assets/*.md,
  stable_executable_helper -> scripts/
}

EXAMPLES_AND_BEST_CODE := {
  operational_fill_in_form_example -> assets/*.md,
  illustrative_pattern_teaching_example -> references/*.md,
  stable_copyable_implementation_pattern -> references/*.md_or_scripts/_depending_on_read_or_run,
  one_off_showcase_examples -> DO_NOT_IMPORT
}

WORKING_STYLE :=
  1 -> import_by_domain
  2 -> ship_one_batch
  3 -> verify_the_pattern
  4 -> adjust
  5 -> continue
```
