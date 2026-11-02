# Book Absorption Rules

Use long-form material only within the user's requested improvement. Read meaningful source sections before extracting a decision and keep the reading record outside the publication repository. Available extracted text is not evidence that the source has been fully read.

Write original operational guidance that states when a technique applies, its assumptions, failure modes, and a result that can be inspected. Do not transfer source passages, diagrams, proprietary templates, or example code into the package. Inspect rights and preserve required license notices when importing redistributable code or assets. A public URL or a supplied file does not by itself grant redistribution rights.

Record selected scope, material actually inspected, decisions applied, and unread or unresolved material privately. A partial-source improvement needs coverage for its selected scope; require a source-wide disposition audit only when claiming whole-source absorption. Do not put book titles, account-specific links, personal file paths, or filled reading ledgers in reusable public instructions. Keep those details in the authorized private working area and state the actual coverage when reporting to the user.

For bounded work, the source inventory below covers the selected sections, not every chapter in the source. Apply slicing and dispatch checks only when the selected scope needs multiple slices or delegated work; a direct edit still names its target owner and the material actually used. Keep unrelated sections explicitly outside the claim rather than inventing a completed review of them.

```text
SOURCE_INVENTORY := PASS IF
  selected_scope_has(topic_map OR section_inventory)
  AND selected_source_inventory_is_recorded_before_distillation
  AND no_selected_source_band_is_left_without_a_disposition

TEXT_EXTRACTION := PASS IF
  selected_material_has_readable_working_text_before_distillation
  AND private_working_text_location_is_recorded
  AND extraction_quality_is_checked_on(table_of_contents OR representative_pages)

PAGE_IMAGE_REVIEW := USE IF
  layout_or_figure_meaning_is_lost_in_text
  OR OCR_or_text_extraction_is_ambiguous
  OR visual_examples_carry_the_actual_rule

CHAPTER_SLICING := PASS IF
  selected_material_is_split_by_meaningful_topic WHEN parallel_or_large_scope_work_needs_slices
  AND each_slice_has_a_named_target_skill_or_reference_seam
  AND workers_return(page_ranges_or_topic_ranges_used, target_paths, ambiguities) WHEN delegation_is_used

OWNERSHIP_SPLIT := PASS IF
  each_slice_names(target_skill_or_reference_owner)
  AND direction_layer_and_implementation_layer_work_are_not_mixed_without_justification
  AND convergence_owner_is_named_before_target_files_change

DISTILLATION := PASS IF
  prose_is_compiled_into_rules_heuristics_and_decision_criteria
  AND original_operational_explanations_replace_source_examples
  AND no_source_code_diagrams_or_distinctive_cases_enter_public_instructions

COVERAGE_LEDGER := PASS IF
  each_selected_source_band_is_marked_as(absorbed_now OR deferred OR excluded_as_non_durable OR needs_visual_review)
  AND absorbed_rules_name(target_paths)
  AND deferred_rules_name(next_owner_or_next_batch)
  AND visual_review_backlog_names(page_ranges_and_reason)

CONVERGENCE_CHECK := PASS IF
  declared_target_paths_do_not_cover_the_source_inventory = FALSE
  AND every_deferred_or_visual_review_item_is_visible
  AND source_wide_gap_check_runs_before_completion_claim WHEN claiming_whole_source_absorption

FAIL IF
  verbatim_book_prose_is_copied_instead_of_distilled_rules
  OR page_images_are_rendered_for_the_whole_book_without_need
  OR slicing_is_done_by_arbitrary_page_count_when_chapter_boundaries_are_available
  OR target_skill_mapping_is_left_implicit
  OR declared_target_paths_do_not_cover_the_source_inventory
  OR deferred_or_visual_review_backlog_is_hidden
```
