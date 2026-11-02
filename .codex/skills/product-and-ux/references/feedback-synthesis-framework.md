# Feedback Synthesis Framework

Convert noisy feedback into decisions, not dashboards.

```text
PROCESSING_ORDER :=
  1 -> collect(surveys, support_tickets, reviews, interviews, analytics_notes)
  2 -> clean(remove_duplicates, split_compound_complaints, normalize_wording)
  3 -> code(problem, user_segment, segment_scope, journey_moment, severity)
  4 -> cluster_themes_by_shared_root_problem
  5 -> rank(frequency, impact, strategic_fit)_separately
  6 -> write_implication(now, later, needs_more_evidence)
  7 -> state_evidence_strength_and_limitations_before_promotion

RANKING_RULES := PASS IF
  frequency_alone_does_not_set_priority
  AND sharp_pain_in_a_critical_journey_can_outrank_a_common_annoyance
  AND feature_requests_are_translated_back_into_the_user_problem_first
  AND support_heavy_themes_produce_operational_and_ux_implications
  AND channel_mix_and_segment_scope_adjust_confidence

FAILURE_MODES := FAIL IF
  loud_customers_are_counted_as_representative
  OR bugs_usability_issues_and_product_gaps_are_blended_together
  OR themes_have_no_owner_or_next_move
  OR limitations_or_contradictory_signals_are_skipped
```
