from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / ".codex" / "skills"
LOGIC_MARKERS = ("PASS IF", "FAIL IF", ":=", "ROUTE ->", "STOP(")


def _read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_knowledge_router_is_removed_from_catalog() -> None:
    assert not (SKILLS_ROOT / "knowledge").exists()
    for doc in ("AGENTS.md", "README.md", ".codex/skills/README.md"):
        assert "`knowledge` |" not in _read(doc)
        assert "- `knowledge`\n" not in _read(doc)


def test_design_references_live_with_their_owning_skill() -> None:
    for name in ("ux-interaction.md", "interface-patterns.md", "design-principles.md",
                 "restraint-and-rule-intent.md", "discovery-interview.md"):
        assert (SKILLS_ROOT / "product-and-ux" / "references" / name).exists(), name
    for name in ("color-systems.md", "ui-composition.md", "design-systems-and-figma.md",
                 "ui-restraint-and-proof.md"):
        assert (SKILLS_ROOT / "implementation-frontend" / "references" / name).exists(), name


def test_moved_and_new_references_are_logic_shaped() -> None:
    paths = [
        SKILLS_ROOT / "product-and-ux" / "references" / n
        for n in ("ux-interaction.md", "interface-patterns.md", "design-principles.md",
                  "restraint-and-rule-intent.md", "discovery-interview.md")
    ] + [
        SKILLS_ROOT / "implementation-frontend" / "references" / n
        for n in ("color-systems.md", "ui-composition.md", "design-systems-and-figma.md",
                  "ui-restraint-and-proof.md")
    ]
    for path in paths:
        body = path.read_text(encoding="utf-8")
        assert "```text" in body and any(m in body for m in LOGIC_MARKERS), path


def test_product_and_ux_routes_restraint_and_discovery() -> None:
    skill = _read(".codex/skills/product-and-ux/SKILL.md")
    assert "You MUST read `references/restraint-and-rule-intent.md`" in skill
    assert "READ -> references/discovery-interview.md" in skill
    assert "READ -> references/ux-interaction.md" in skill
    assert "READ -> references/interface-patterns.md" in skill
    assert "READ -> references/design-principles.md" in skill
    assert "bounded_change_inside_approved_direction" in skill
    assert "This applies to EVERY project regardless of perceived simplicity." not in skill
    assert "ask(one_question_at_a_time)" not in skill


def test_restraint_reference_keeps_reasons_and_floors() -> None:
    body = _read(".codex/skills/product-and-ux/references/restraint-and-rule-intent.md")
    assert "| Rule | Why it exists | Apply when | Stop when | Overreach signal |" in body
    assert "FAIL IF element_exists_because_a_checklist_or_reference_mentions_it" in body
    assert "FAIL IF restraint_is_used_to_justify_removing_a_FLOOR_item" in body
    assert "legally_or_regulatorily_required_disclosure_or_consent" in body
    assert "When Restraint Itself Over-Applies" in body


def test_ux_interaction_rules_are_scoped_not_absolute() -> None:
    body = _read(".codex/skills/product-and-ux/references/ux-interaction.md")
    assert "restraint-and-rule-intent.md" in body
    assert "SUCCESS := confirm completion and next consequence\n" not in body
    assert "a visible in-place result is its own confirmation" in body
    assert "BEHAVIORAL_LEVER_GATE :=" in body
    assert "deliberately absent with a reason" in body


def test_implementation_frontend_routes_absorbed_references_and_honest_proof() -> None:
    skill = _read(".codex/skills/implementation-frontend/SKILL.md")
    for ref in ("ui-restraint-and-proof.md", "ui-composition.md", "color-systems.md",
                "design-systems-and-figma.md"):
        assert f"references/{ref}" in skill, ref
    assert "no_unapproved_interface_additions" in skill
    assert 'REPORT("code inspected; not rendered")' in skill
    proof = _read(".codex/skills/implementation-frontend/references/ui-restraint-and-proof.md")
    assert "FAIL IF reversible_action_gets_a_confirm_dialog_instead_of_undo" in proof
    assert "MOTION_DEFAULT := none" in proof
    coverage = _read(".codex/skills/implementation-frontend/references/ui-state-coverage.md")
    assert "NOT_APPLICABLE :=" in coverage


def test_host_drift_is_synced_back_and_routed() -> None:
    orchestration = _read(".codex/skills/multi-agent-orchestration/SKILL.md")
    for ref in ("runtime-routing.md", "lane-graph.md", "self-evolution.md"):
        assert f"READ -> references/{ref}" in orchestration, ref
    assert "references/rulebook-routing-map.md" in _read(".codex/skills/intake-and-routing/SKILL.md")
    assert "references/numerical-review.md" in _read(".codex/skills/quality-and-review/SKILL.md")
    assert "references/external-guideline-source-absorption.md" in _read(".codex/skills/skillsmith/SKILL.md")
    rulebook_map = _read(".codex/skills/intake-and-routing/references/rulebook-routing-map.md")
    for target in sorted(set(__import__("re").findall(r"\.codex/rulebooks/([\w-]+\.md)", rulebook_map))):
        assert (REPO_ROOT / ".codex" / "rulebooks" / target).exists(), target


def test_self_evolution_respects_user_authorization_and_portability() -> None:
    body = _read(".codex/skills/multi-agent-orchestration/references/self-evolution.md")
    assert "when the user's standing or current instructions authorize harness fixes" in body
    assert "~/.codex" not in body and "OKF" not in body


def test_rulebooks_name_only_active_skills() -> None:
    import re
    active = {p.name for p in SKILLS_ROOT.iterdir() if p.is_dir()}
    for path in sorted((REPO_ROOT / ".codex" / "rulebooks").glob("*.md")):
        for block in re.findall(r"OWNER_SKILLS := \{([^}]*)\}", path.read_text(encoding="utf-8-sig")):
            for name in (n.strip() for n in block.split(",")):
                assert name in active, (path.name, name)
