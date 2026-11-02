# Code Review Dispatch

Use this when another reviewer needs a compact, repo-local code review brief.

```text
Review lane:
  Use asset at `quality-and-review/assets/code-review.md`

  full_task_text_or_requirement_excerpt: [copy the bounded task text or exact requirement excerpt]
  implementer_claims: [from implementer's report]
  do_not_trust_the_report_without_code_and_evidence_check: TRUE
  review_feedback_must_be_verified_against_codebase_reality: TRUE
  unclear_items_must_be_clarified_before_changes: TRUE
  PLAN_OR_REQUIREMENTS: [task id or approved requirement]
  BASE_SHA: [commit before task]
  HEAD_SHA: [current commit]
  DESCRIPTION: [task summary]
  SEAM: [bounded surface under review]
```

Add specialist review assets when the seam needs them:

- security -> `assets/security-review-checklist.md`
- docs -> `assets/review-handoff.md` plus `references/docs-as-code-review.md`
- inclusive visuals -> `references/inclusive-visual-qa.md`
