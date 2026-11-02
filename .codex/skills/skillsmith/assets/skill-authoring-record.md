# Skill Authoring Record

Copy this optional template into a working area outside the publication repository when a substantial change benefits from a durable record. Omit fields that do not apply; do not fill it for every direct wording edit.

## Inputs

```text
SUPPORT.declared_assets :=
SUPPORT.declared_references :=
SUPPORT.files_read_before_revision :=
SUPPORT.why_each_file_was_loaded :=
SUPPORT.files_actually_used :=
TARGET.skill_path :=
TARGET.operating_concern :=
TARGET.trigger_conditions :=
TARGET.output_contract :=
TARGET.delegated_execution_or_reporting_contract :=
TARGET.admission_gate_justification :=
TARGET.source_behavior_map :=
TARGET.instruction_surface_decision :=
TARGET.catalog_non_fit_decision :=
TARGET.active_repo_local_owner_or_exclusion_record :=
TARGET.import_disposition_summary :=
```

## Package Decisions

```text
PACKAGE.roles_added :=
PACKAGE.assets_added :=
PACKAGE.references_added :=
PACKAGE.discovery_metadata_updated := TRUE OR FALSE
PACKAGE.compile_first_absorption_kept := TRUE OR FALSE
PACKAGE.parallel_namespace_added := TRUE OR FALSE
PACKAGE.admission_gate_result := absorbed OR promoted
PACKAGE.remaining_source_behaviors_needing_top_level_promotion :=
PACKAGE.xml_or_dot_added := TRUE OR FALSE
PACKAGE.example_or_best_code_decision := KEEP OR DROP OR MOVE
PACKAGE.dispatch_traceability_fields_added := TRUE OR FALSE
PACKAGE.actual_usage_reporting_fields_added := TRUE OR FALSE
PACKAGE.parallel_maintenance_dispatch_added := TRUE OR FALSE
PACKAGE.instruction_surface_contract_updated := TRUE OR FALSE
```

## Style Contract

```text
STYLE.routing := PASS IF branches_and_owner_boundaries_are_clear
STYLE.process := PASS IF prose_lists_or_pseudocode_preserve_the_actual_decisions
STYLE.checklists := PASS IF acceptance_conditions_and_evidence_are_explicit
STYLE.references := PASS IF reference_selection_matches(style_rules)
```

## Risks

```text
RISK.ambiguity_removed :=
RISK.hidden_dependency_removed :=
RISK.delegated_skill_ambiguity_removed :=
RISK.remaining_gap :=
RISK.distillation_notes :=
```

PASS IF
  SUPPORT.declared_assets IS named_or_none
  AND SUPPORT.declared_references IS named_or_none
  AND SUPPORT.files_read_before_revision
  AND SUPPORT.why_each_file_was_loaded
  AND TARGET.skill_path
  AND TARGET.output_contract
  AND TARGET.instruction_surface_decision IS named_or_not_applicable
  AND TARGET.catalog_non_fit_decision IS named_or_not_applicable

FAIL IF
  SUPPORT.files_actually_used IS missing
