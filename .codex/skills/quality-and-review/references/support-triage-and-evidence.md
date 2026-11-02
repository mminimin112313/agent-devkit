# Support Triage And Evidence

Support cases should be reviewable, not just readable.

```text
MINIMUM_EVIDENCE := {
  symptom_in_user_terms,
  affected_surface,
  environment_or_version,
  timing_or_recency,
  severity_and_workaround_status,
  repro_steps_or_explicit_repro_gap,
  recent_related_change_if_known,
  impact_scope,
  attachments_logs_or_screenshots_when_they_materially_support_the_claim
}

REVIEW_DISCIPLINE := PASS IF
  support_language_is_normalized_into_one_failure_claim_at_a_time
  AND reproduction_happens_before_concluding_when_feasible
  AND reproduction_gaps_are_classified_as(missing_steps OR missing_environment_parity OR non_determinism)
  AND confidence_is_labeled_as(confirmed OR estimated OR hypothesis_only)
  AND next_owner_and_next_action_are_required_when_evidence_is_incomplete

ROUTING_RULES :=
  outage_or_degraded_runtime -> release-and-operations
  reproducible_product_issue -> implementation_after_review
  non_reproducible_issue -> evidence_completion
  recurring_confusion -> product-and-ux_synthesis
```
