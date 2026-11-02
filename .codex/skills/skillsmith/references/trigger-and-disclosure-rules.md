# Trigger And Disclosure Rules

Use this lens when trigger wording, `SKILL.md` size, or bundled-resource boundaries are changing.

```text
DESCRIPTION := PASS IF
  description_states(what_the_skill_does)
  AND description_states(when_the_skill_should_trigger)
  AND description_distinguishes_nearby_capabilities_without_threats
  AND description_does_not_claim_authority_over_user_or_runtime_controls
  AND description_names(realistic_contexts_or_near_misses) WHEN undertrigger_risk_is_high

DISCLOSURE := PASS IF
  frontmatter_owns(trigger_metadata)
  AND SKILL_md_owns(workflow_gates_and_output_contract)
  AND references_or_assets_own(durable_detail)
  AND scripts_own(repeated_runnable_helpers)

BODY_SHAPE := PASS IF
  SKILL_md_stays_scannable
  AND procedure_is_easy_to_find
  AND large_detail_is_moved_to_named_support_files_before_SKILL_md_turns_into_prompt_dump
  AND support_file_selection_tells_the_operator_exactly_when_to_read_more

SCRIPT_PROMOTION := PASS IF
  repeated_helper_logic_shows_up_across(multiple_runs OR transcripts OR source_examples)
  AND helper_is_stable_enough_to_live_under_scripts
  AND skill_instructions_treat_the_helper_as_black_box_first

FAIL IF
  description_only_names_the_domain_without_trigger_context
  OR description_uses_threats_or_faint_relevance_as_activation_logic
  OR procedure_is_obscured_by_boilerplate
  OR SKILL_md_repeats_reference_material_instead_of_pointing_to_it
  OR one_off_example_code_is_promoted_to_script_without_repeat_evidence
  OR support_file_loading_boundaries_are_implicit
```
