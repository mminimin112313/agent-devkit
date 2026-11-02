# UI Restraint And Proof

Use while building or polishing a surface, and before claiming it is done. The approved direction decides what exists. This file keeps implementation from adding UI the direction did not ask for, and keeps completion claims honest. It is the implementation summary of `product-and-ux/references/restraint-and-rule-intent.md`; read that file when a judgment call is not covered here.

## Build Only What The Direction Justifies

Implementation is where over-kindness and over-display usually enter. An agent adds a toast, a confirm dialog, a helper line, or a badge "to be safe." Each addition costs attention and needs a named failure it prevents.

```text
ADDITION := any(toast, confirm_dialog, helper_text, badge, count, tooltip, tour, banner, empty_state_media, extra_heading, decorative_divider, animation)
IF ADDITION not_in(approved_direction) THEN
  REQUIRE(named_user_failure_it_prevents)
  PREFER(cheaper form per CHEAPER_FORM_ORDER := nothing < convention < inline_text < undo < inline_warning < blocking_dialog)
  RECORD(reason) IF kept
FAIL IF ADDITION_exists_only_because_a_checklist_mentions_it
FAIL IF reversible_action_gets_a_confirm_dialog_instead_of_undo
FAIL IF success_feedback_duplicates_a_result_already_visible_in_place
FLOOR := {
  accessible_name_role_state_and_focus,
  contrast_and_target_size,
  error_message_when_an_error_actually_occurs,
  legally_or_regulatorily_required_disclosure_or_consent,
  safety_warning_for_irreversible_harm,
  status_for_work_the_user_cannot_otherwise_see
}
FAIL IF restraint_removes_a_FLOOR_item
```

## Anti-Generic Checks

These checks prevent template output. Keep the reason with each check so it is not applied mechanically.

```text
FAIL IF card_grids_or_stat_tiles_fill_space_without_serving_the_task      ; why: filler hides the real content hierarchy
FAIL IF metrics_sections_or_copy_are_invented                             ; why: fake data misleads review and users
FAIL IF dark_theme_is_chosen_by_default_instead_of_by_context             ; why: a default is not a decision
FAIL IF the_change_erases_existing_product_identity_without_an_approved_reason ; why: users rely on learned recognition
ACCESSORY_REVIEW := before handoff, ask of each accessory element who would fail without it; remove it when the answer is nobody; no removal quota
ONE_EMPHASIS := spend boldness in one place per region; a second decorative emphasis must win against the first or go; error, danger, and safety treatment is exempt
SCOPE := marketing surfaces may carry more personality; dense tools and dashboards carry less; neither license overrides FLOOR
```

## Motion

```text
MOTION_DEFAULT := none
ADD(motion) ONLY IF motion_explains(cause_effect OR spatial_origin OR state_change OR loading_progress)
REQUIRE(prefers_reduced_motion_alternative) IF motion_exists
PREFER(transform AND opacity) OVER(layout_affecting_properties)
FAIL IF motion_is_added_only_for_polish
```

## Numbers, Not Adjectives

```text
REPORT(contrast_ratio) FROM actual_color_values, not "looks fine"
REPORT(target_size, font_size, line_length) FROM rendered or token values
MARK(estimate) WHEN a value was not measured
TOKEN_PRECEDENCE := project_design_tokens > shared_rules_in_this_skill > ad_hoc_values_in_the_task
FAIL IF ad_hoc_values_override_existing_tokens_without_a_recorded_reason
```

## Completion Claims

```text
CLAIM(visual_check) ONLY IF the_surface_was_rendered_and_inspected
IF only_code_was_read THEN SAY("code inspected; not rendered") AND do_not_claim_visual_verification
RENDER_CHECK := desktop + narrow_width + relevant_states(hover, focus, disabled, empty, error, long_text_overflow)
BEFORE_AFTER := PASS IF report_states(clearer?, more_useful?, what_got_worse, what_to_revert)
PASS IF the_handoff_lists_removed_elements_and_why_kept_elements_remain
```
