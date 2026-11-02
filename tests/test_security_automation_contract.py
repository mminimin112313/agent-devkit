from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_security_workflow_runs_trufflehog_trivy_and_kingfisher() -> None:
    workflow = _read(".github/workflows/security-scans.yml")

    assert "pull_request:" in workflow
    assert "push:" in workflow
    assert "trufflesecurity/trufflehog@v3.91.1" in workflow
    assert "aquasec/trivy:0.65.0" in workflow
    assert "mongodb/kingfisher/v1.68.0/scripts/install-kingfisher.sh" in workflow
    assert "--git-history none" in workflow
    assert "--exclude '.git/**'" in workflow
    assert "trufflehog-evidence" in workflow
    assert "security-events: write" in workflow
    assert "github/codeql-action/upload-sarif" in workflow


def test_security_review_reads_automation_evidence_and_handoff_captures_it() -> None:
    skill = _read(".codex/skills/security-review/SKILL.md")
    reference = _read(".codex/skills/security-review/references/automation-evidence.md")
    handoff = _read(".codex/skills/security-review/assets/remediation-handoff.md")

    assert "references/automation-evidence.md" in skill
    assert "STEP_2A := read_only(automation_evidence_rules) FROM references/automation-evidence.md IF ci_scan_artifacts_exist OR scanner_output_is_cited" in skill
    assert "automation_output_does_not_replace_reading_the_affected_seam" in reference
    assert "ci_scan_artifacts" in reference
    assert "scan_jobs" in handoff
    assert "automation_artifacts" in handoff


def test_release_evidence_requires_fresh_security_scan_context() -> None:
    evidence = _read(".codex/skills/release-and-operations/references/release-evidence.md")

    assert "security_automation_is_fresh_or_explicitly_waived" in evidence
    assert "IF security_findings_exist THEN ROUTE -> security-review" in evidence
    assert "record(security_scan_jobs, security_artifacts, security_owner)" in evidence
