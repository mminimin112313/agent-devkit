# Review Sequencing

```text
ORDER :=
  1 -> spec-reviewer
  2 -> reviewer
  3 -> qa

PASS IF
  requirement_fit_is_checked_first
  AND spec_review_must_pass_before_code_quality_review_starts
  AND code_quality_review_starts_after_requirement_fit_is_clear
  AND code_quality_review_does_not_start_until_spec_gaps_are_closed
  AND qa_checks_fresh_runtime_verification_evidence

FAIL IF
  qa_evidence_is_used_as_substitute_for_spec_review
  OR code_quality_review_starts_before_requirement_fit

IF seam_failed THEN REQUIRE(named_failing_unit AND failure_type AND root_cause AND prevention_note)
IF ship_decision_is_unresolved THEN ROUTE -> release-and-operations

BOUNDARY_RULES :=
  spec-reviewer -> approved_seam_fit
  reviewer -> implementation_soundness
  qa -> proof_freshness_and_sufficiency
  specialist_lenses -> attach_to_relevant_step AND NOT replace_main_order

IF seam_itself_is_wrong THEN ROUTE -> right_owner AND STOP

PARALLEL_REVIEW := PASS IF
  each_lane_has_independent_scope
  AND each_lane_has_independent_evidence
  AND no_lane_depends_on_unfinished_lane
  AND no_two_lanes_rewrite_same_handoff
  AND one_acceptance_owner_converges

PARALLEL_REVIEW := FAIL IF
  ordered_judgment_is_required
  OR one_lane_validates_another_lanes_changing_output
  OR seam_is_too_fuzzy_for_independent_evaluation

HANDOFF_MINIMUM := PASS IF
  summary_present
  AND findings_or_acceptance_result_present
  AND risks_or_remaining_uncertainty_present
  AND artifacts_checked_present
  AND proof_freshness_or_explicit_evidence_gaps_present
  AND next_owner_or_next_action_present
```
