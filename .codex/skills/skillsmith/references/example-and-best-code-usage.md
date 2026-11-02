# Example And Best-Code Usage

Examples and best-code belong in a skill only when timing and placement are explicit.

```text
ADD_EXAMPLE := PASS IF
  workflow_is_easy_to_misunderstand_without_one_concrete_instance
  OR operator_must_see_expected_output_shape
  OR recurring_handoff_or_dispatch_stub_benefits_from_copyable_skeleton

SKIP_EXAMPLE := PASS IF
  example_only_repeats_an_already_clear_rule
  OR example_is_project_specific_and_will_age_badly
  OR operator_really_needs_checklist_not_sample

ADD_BEST_CODE := PASS IF
  code_captures_stable_repeated_implementation_pattern
  AND pattern_is_central_to_the_skill
  AND skill_scope_is_tight_enough_that_code_stays_relevant

SKIP_BEST_CODE := PASS IF
  code_is_tied_to_one_stack_or_repo_detail_the_skill_does_not_own
  OR underlying_lesson_is_process_or_review_not_syntax
  OR code_should_instead_live_under_scripts/

PLACEMENT_MATRIX := {
  output_or_handoff_stub -> assets/*.md,
  repeated_worksheet_or_record -> assets/*.md,
  explanatory_example -> references/*.md,
  copyable_stable_pattern -> references/*.md,
  runnable_helper -> scripts/
}

TIMING_RULE := PASS IF
  examples_and_best_code_are_decided_after(trigger AND procedure AND failure_guards)_are_stable
  AND support_material_does_not_replace_the_skill_foundation
```
