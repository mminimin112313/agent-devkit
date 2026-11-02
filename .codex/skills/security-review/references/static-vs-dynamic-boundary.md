# Static vs Dynamic Boundary

```text
USE IF review_could_drift_from(source_level_classification) TO(runtime_exploitability_claim)

PASS IF
  security-review_classifies(boundary AND likely_weakness) FROM(code_or_config_evidence)
  AND security-lab_proves_exploitability WHEN runtime_evidence_is_required
  AND multiple_suspected_weaknesses_split_into_separate_review_records UNLESS one_exploit_path_is_shared

FAIL IF
  one_suspicious_seam_is_widened_into_unrelated_findings
  OR runtime_claims_are_made_without_runtime_evidence
```
