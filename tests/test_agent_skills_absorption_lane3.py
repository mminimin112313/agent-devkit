from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _skill_body(skill_name: str) -> str:
    return (REPO_ROOT / ".codex" / "skills" / skill_name / "SKILL.md").read_text(encoding="utf-8")


def test_intake_and_routing_uses_top_level_required_reads() -> None:
    body = _skill_body("intake-and-routing")
    reference = REPO_ROOT / ".codex" / "skills" / "intake-and-routing" / "references" / "signal-driven-routing.md"
    clarification_reference = REPO_ROOT / ".codex" / "skills" / "intake-and-routing" / "references" / "intake-clarification-patterns.md"
    asset = REPO_ROOT / ".codex" / "skills" / "intake-and-routing" / "assets" / "intake-record.md"
    decision_asset = REPO_ROOT / ".codex" / "skills" / "intake-and-routing" / "assets" / "routing-decision.md"

    assert reference.exists()
    assert clarification_reference.exists()
    assert asset.exists()
    assert decision_asset.exists()
    assert "## Required Reads" in body
    assert "You MUST start from `assets/intake-record.md`" in body
    assert "You MUST read `references/signal-driven-routing.md`" in body
    assert "## Procedure\n\n```text" in body
    assert "IF" in body
    assert "ROUTE" in body
    ref_body = reference.read_text(encoding="utf-8")
    assert "IF" in ref_body
    assert "ROUTE -> `product-and-ux`" in ref_body
    assert "ROUTE -> `planning-and-scoping`" in ref_body
    assert "ELSE" in ref_body

    clarification_body = clarification_reference.read_text(encoding="utf-8")
    assert "PASS IF" in clarification_body
    assert "FAIL IF" in clarification_body

    asset_body = asset.read_text(encoding="utf-8")
    assert "PASS IF" in asset_body
    assert "FAIL IF" in asset_body

    decision_body = decision_asset.read_text(encoding="utf-8")
    assert "PASS IF" in decision_body
    assert "FAIL IF" in decision_body


def test_product_and_ux_uses_top_level_required_reads() -> None:
    body = _skill_body("product-and-ux")
    reference = REPO_ROOT / ".codex" / "skills" / "product-and-ux" / "references" / "signal-translation-rules.md"

    assert reference.exists()
    assert "## Required Reads" in body
    assert "You MUST start from `assets/product-brief.md`" in body
    assert "You MUST read `references/signal-translation-rules.md`" in body
    ref_body = reference.read_text(encoding="utf-8")
    assert "```text" in ref_body
    assert "IF signal_is_research THEN" in ref_body
    assert "ROUTE -> planning-and-scoping" in ref_body
    assert "FAIL IF" in ref_body
