from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _skill_body(name: str) -> str:
    return (REPO_ROOT / ".codex" / "skills" / name / "SKILL.md").read_text(encoding="utf-8")


def _skill_path(name: str) -> Path:
    return REPO_ROOT / ".codex" / "skills" / name


def test_architecture_skill_uses_pseudocode_style_contract() -> None:
    body = _skill_body("architecture-and-design")
    reference = _skill_path("architecture-and-design") / "references" / "service-decomposition.md"
    asset = _skill_path("architecture-and-design") / "assets" / "architecture-review-checklist.md"

    assert reference.exists()
    assert asset.exists()
    assert "## Procedure" in body
    assert "```text" in body
    assert "IF seam_is_not_stable OR contract_is_implicit THEN STOP" in body
    assert "ROUTE ->" in body

    reference_body = reference.read_text(encoding="utf-8")
    asset_body = asset.read_text(encoding="utf-8")
    assert "PASS IF split_reduces_hidden_coupling" in reference_body
    assert "FAIL IF split_only_renames_layers" in reference_body
    assert "PASS IF" in asset_body
    assert "FAIL IF" in asset_body


def test_backend_skill_uses_top_level_required_reads() -> None:
    body = _skill_body("implementation-backend")
    guardrail_path = _skill_path("implementation-backend") / "references" / "implementation-guardrails.md"
    asset_path = _skill_path("implementation-backend") / "assets" / "contract-checklist.md"

    assert guardrail_path.exists()
    assert asset_path.exists()
    guardrail_body = guardrail_path.read_text(encoding="utf-8")
    asset_body = asset_path.read_text(encoding="utf-8")
    assert "## Required Reads" in body
    assert "You MUST read `references/implementation-guardrails.md`" in body
    assert "You MUST start from `assets/contract-checklist.md`" in body
    assert "```text" in body
    assert "IF seam_is_not_explicit OR verification_path_is_missing THEN STOP" in body
    assert "ROUTE -> planning-and-scoping" in body
    assert "contract_and_boundary_behavior_are_defined_before_implementation_detail" in guardrail_body
    assert "side_effects_are_isolated_at_explicit_runtime_edges_or_adapters" in guardrail_body
    assert "null_empty_timeout_duplicate_and_partial_failure_cases_are_treated_as_first_class_work" in guardrail_body
    assert "PASS IF" in asset_body
    assert "FAIL IF" in asset_body


def test_frontend_skill_uses_top_level_required_reads() -> None:
    body = _skill_body("implementation-frontend")
    guardrail_path = _skill_path("implementation-frontend") / "references" / "implementation-guardrails.md"
    asset_path = _skill_path("implementation-frontend") / "assets" / "component-state-checklist.md"

    assert guardrail_path.exists()
    assert asset_path.exists()
    guardrail_body = guardrail_path.read_text(encoding="utf-8")
    asset_body = asset_path.read_text(encoding="utf-8")
    assert "## Required Reads" in body
    assert "You MUST read `references/implementation-guardrails.md`" in body
    assert "You MUST start from `assets/frontend-implementation-brief.md`" in body
    assert "```text" in body
    assert "IF user_facing_behavior_is_implicit OR state_coverage_is_missing THEN STOP" in body
    assert "ROUTE -> planning-and-scoping" in body
    assert "composition_and_seam_local_state_are_preferred_over_multi_responsibility_components" in guardrail_body
    assert "loading_error_empty_disabled_and_recovery_states_are_explicit_before_polish" in guardrail_body
    assert "IF FAIL THEN ROUTE -> planning-and-scoping" in guardrail_body
    assert "PASS IF" in asset_body
    assert "FAIL IF" in asset_body


def test_skillsmith_uses_top_level_required_reads() -> None:
    body = _skill_body("skillsmith")
    guardrail_path = _skill_path("skillsmith") / "references" / "overlap-and-audit-guardrails.md"

    assert guardrail_path.exists()
    guardrail_body = guardrail_path.read_text(encoding="utf-8")
    assert "## Required Reads" in body
    assert "Read `references/overlap-and-audit-guardrails.md` when widening a package" in body
    assert "Use `assets/skill-authoring-record.md` for a substantial package change" in body
    assert "## Overlap And Audit Guardrails" not in body
    assert "RULE_1 := IMPROVE(existing_broad_skill) BEFORE CREATE_OR_WIDEN(neighboring_skill_package)" in guardrail_body
    assert "AUDIT := PASS IF" in guardrail_body
    assert "trigger_is_narrower_and_clearer_than_adjacent_skills" in guardrail_body
    assert "required_support_files_are_obvious_without_hidden_context" in guardrail_body
    assert "output_contract_is_obvious_without_hidden_context" in guardrail_body
