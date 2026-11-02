from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / ".codex" / "skills"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_product_and_ux_package_uses_pseudocode_style() -> None:
    skill = _read(SKILLS_ROOT / "product-and-ux" / "SKILL.md")
    asset = _read(SKILLS_ROOT / "product-and-ux" / "assets" / "product-brief.md")
    reference = _read(SKILLS_ROOT / "product-and-ux" / "references" / "signal-translation-rules.md")

    assert "## Required Reads" in skill
    assert "```text" in skill
    assert "IF signal_is_research" in skill or "IF evidence_mode" in skill
    assert "ROUTE ->" in skill
    assert "PASS IF" in asset
    assert "FAIL IF" in asset
    assert "IF signal_is_research THEN" in reference


def test_release_and_operations_package_uses_pseudocode_style() -> None:
    skill = _read(SKILLS_ROOT / "release-and-operations" / "SKILL.md")
    asset = _read(SKILLS_ROOT / "release-and-operations" / "assets" / "release-gate.md")
    reference = _read(SKILLS_ROOT / "release-and-operations" / "references" / "release-evidence.md")

    assert "```text" in skill
    assert "IF current_mode = incident_response" in skill or "IF evidence_is_weak THEN STOP" in skill
    assert "ROUTE ->" in skill
    assert "PASS IF" in asset
    assert "FAIL IF" in asset
    assert "IF shipping_scope IS vague THEN FAIL" in reference
