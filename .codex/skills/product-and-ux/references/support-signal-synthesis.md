# Support Signal Synthesis

Support data becomes product evidence only after it is translated into a user problem.

```text
TRANSLATION_PASS :=
  1 -> collect_repeated_support_themes
  2 -> separate(bug, confusion, onboarding_gap, missing_capability)
  3 -> locate_the_journey_step_where_the_issue_appears
  4 -> name_segment_scope_and_breadth(broad OR narrow)
  5 -> check(freshness, duplication, whether_the_issue_is_still_current)
  6 -> compare_support_language_against(current_product_behavior, docs, known_incidents)
  7 -> ROUTE -> `security-review` IF signal_touches(trust OR privacy OR auth OR abuse OR exploitability OR policy)
  8 -> rank_by(severity, frequency, business_importance)
  9 -> state_evidence_strength_and_limitations
  10 -> write_the_product_implication

OUTPUT_RULE := PASS IF
  synthesis_does_not_stop_at_users_complain_about_x
  AND result_ends_with(change OR study_further OR intentionally_defer OR escalate_to_security_review)
  AND stale_anecdotal_support_only_or_missing_product_evidence_is_called_out
```
