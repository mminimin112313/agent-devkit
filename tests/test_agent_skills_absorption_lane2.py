from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _skill_body(skill_name: str) -> str:
    return (REPO_ROOT / ".codex" / "skills" / skill_name / "SKILL.md").read_text(encoding="utf-8")


def _reference_body(skill_name: str, reference_name: str) -> str:
    return (
        REPO_ROOT / ".codex" / "skills" / skill_name / "references" / reference_name
    ).read_text(encoding="utf-8")


def test_quality_and_review_uses_top_level_required_reads() -> None:
    body = _skill_body("quality-and-review")
    reference = _reference_body("quality-and-review", "criterion-discipline.md")

    assert "## Required Reads" in body
    assert "START -> assets/review-checklist.md" in body
    assert "MUST READ -> references/review-sequencing.md" in body
    assert "IF seam_has(explicit_acceptance_criteria OR approved_plan_steps OR spec_language)" in body
    assert "PASS IF" in reference
    assert "claimed_acceptance_criteria_are_extracted_before_approval" in reference
    assert "file:line OR artifact:section" in reference
    assert "failed_criteria_route_to_named_remediation_owner" in reference


def test_security_review_uses_top_level_required_reads() -> None:
    body = _skill_body("security-review")
    reference = _reference_body("security-review", "static-vs-dynamic-boundary.md")

    assert "## Required Reads" in body
    assert "MUST START -> assets/review-record.md" in body
    assert "MUST READ -> references/review-lenses.md" in body
    assert "IF exploitability_is_uncertain OR runtime_proof_may_be_needed" in body
    assert "PASS IF" in reference
    assert "security-review_classifies(boundary AND likely_weakness)" in reference
    assert "security-lab_proves_exploitability" in reference
    assert "separate_review_records" in reference


def test_security_lab_uses_pseudocode_required_reads_and_validation_rules() -> None:
    body = _skill_body("security-lab")
    reference = _reference_body("security-lab", "finding-validation-rules.md")

    assert "## Required Reads" in body
    assert "MUST START -> assets/lab-run-record.md" in body
    assert "MUST READ -> references/docker-lab-safety.md" in body
    assert "IF escalating_a_lead_to_a_confirmed_finding THEN MUST READ -> references/finding-validation-rules.md" in body
    assert "CONFIRMED_FINDING := PASS IF" in reference
    assert "LEAD_ONLY := PASS IF" in reference
    assert "FALSE_POSITIVE_CONTROLS := PASS IF" in reference
