from pathlib import Path
import re
import shutil
import subprocess


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / ".codex" / "skills"


def _read(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


def test_architecture_skill_absorbs_deep_modules_and_humble_object_contracts() -> None:
    arch_skill = _read(".codex/skills/architecture-and-design/SKILL.md")
    decomp = _read(".codex/skills/architecture-and-design/references/service-decomposition.md")
    platform = _read(".codex/skills/architecture-and-design/references/platform-contracts.md")
    separation = _read(".codex/skills/architecture-and-design/references/provider-service-tool-separation.md")
    design_note = _read(".codex/skills/architecture-and-design/assets/design-note.md")
    checklist = _read(".codex/skills/architecture-and-design/assets/architecture-review-checklist.md")

    assert "<MODULE-DEPTH-AND-TESTABILITY-GATE>" in arch_skill
    assert "interface_cost_vs_hidden_capability" in arch_skill
    assert "information_hiding_vs_backdoor_leakage" in arch_skill
    assert "pull_complexity_downwards" in arch_skill
    assert "code_quadrant_separation" in arch_skill

    assert "temporal decomposition" in decomp
    assert "back-door leakage" in decomp
    assert "each_module_hides_a_distinct_changeable_design_decision" in decomp
    assert "deep_domain_or_algorithm_logic_is_separated_from_wide_collaborator_orchestration" in decomp
    assert "resulting_methods_or_classes_are_conjoined_and_cannot_be_understood_independently" in decomp

    assert "somewhat general-purpose" in platform
    assert "uncalibrated configuration parameters" in platform
    assert "single-implementation interfaces" in platform
    assert "pass_through_methods_or_pass_through_variables_cross_layers_without_new_abstraction" in platform

    assert "CanExecute" in separation
    assert "immutable past-tense domain events" in separation
    assert "domain_service_calls_out_of_process_dependencies_directly" in separation

    assert "module_depth_vs_interface_cost" in design_note
    assert "domain_vs_controller_quadrant_split" in design_note
    assert "managed_vs_unmanaged_dependency_boundaries" in design_note
    assert "module_depth_and_hidden_design_decisions_justify_the_interface_cost" in checklist


def test_implementation_and_planning_skills_absorb_pinch_points_quadrants_and_dependency_rules() -> None:
    backend_skill = _read(".codex/skills/implementation-backend/SKILL.md")
    backend_guardrails = _read(".codex/skills/implementation-backend/references/implementation-guardrails.md")
    backend_arch = _read(".codex/skills/implementation-backend/references/backend-architecture-review.md")
    contract_checklist = _read(".codex/skills/implementation-backend/assets/contract-checklist.md")
    frontend_skill = _read(".codex/skills/implementation-frontend/SKILL.md")
    frontend_guardrails = _read(".codex/skills/implementation-frontend/references/implementation-guardrails.md")
    planning_skill = _read(".codex/skills/planning-and-scoping/SKILL.md")

    assert "<DESIGN-AND-TESTING-DISCIPLINE-GATE>" in backend_skill
    assert "SEPARATE(deep_domain_or_algorithm_decisions, humble_out_of_process_orchestration)" in backend_skill
    assert "CLASSIFY(dependencies := in_process OR managed_out_of_process OR unmanaged_external)" in backend_skill

    assert "pinch points" in backend_guardrails
    assert "sprout" in backend_guardrails
    assert "output-based or state-based tests" in backend_guardrails
    assert "managed out-of-process dependencies" in backend_guardrails
    assert "unmanaged external dependencies" in backend_guardrails
    assert "separate transaction or unit-of-work scopes for arrange, act, and assert" in backend_guardrails
    assert "managed_dependencies_are_verified_via_final_state_with_isolated_arrange_act_assert_scopes" in backend_guardrails
    assert "unmanaged_dependencies_are_mocked_or_spied_only_at_consumer_owned_outermost_adapters" in backend_guardrails

    assert "deep_interface_hides_representation_and_avoids_pass_through_layers" in backend_arch
    assert "atomic_transaction_or_unit_of_work_boundary_is_explicit_when_state_mutates" in backend_arch
    assert "domain_decisions_are_testable_without_out_of_process_collaborators" in contract_checklist

    assert "<DESIGN-AND-TESTING-DISCIPLINE-GATE>" in frontend_skill
    assert "pure_state_and_selector_decisions_are_separated_from_browser_and_network_side_effects" in frontend_guardrails
    assert "SEPARATE(deep_domain_or_algorithm_slices, humble_controller_and_adapter_orchestration_slices)" in planning_skill
    assert "IDENTIFY(pinch_points_and_sprout_or_wrap_seams)" in planning_skill


def test_quality_and_review_absorbs_four_pillars_and_design_red_flags() -> None:
    quality_skill = _read(".codex/skills/quality-and-review/SKILL.md")
    lenses = _read(".codex/skills/quality-and-review/references/evidence-ladder-and-root-cause-lenses.md")
    review_checklist = _read(".codex/skills/quality-and-review/assets/review-checklist.md")
    code_review = _read(".codex/skills/quality-and-review/assets/code-review.md")

    assert "<DESIGN-AND-TEST-QUALITY-GATE>" in quality_skill
    assert "STEP_6A := audit_design_red_flags" in quality_skill
    assert "STEP_6B := audit_test_quality" in quality_skill

    assert "TEST_VALUE_FOUR_PILLARS_GATE" in lenses
    assert "DESIGN_RED_FLAG_AUDIT_GATE" in lenses
    assert "resistance to refactoring is non-negotiable" in lenses
    assert "Never assert interactions on stubs" in lenses
    assert "support logging" in lenses and "diagnostic logging" in lenses

    assert "design depth and red-flag audit:" in review_checklist
    assert "test value four-pillars and anti-pattern audit:" in review_checklist
    assert "design red flags:" in code_review
    assert "test anti-patterns:" in code_review


def test_public_surface_has_no_source_book_titles_authors_or_canonical_examples() -> None:
    forbidden_terms = (
        "Ousterhout",
        "Khorikov",
        "Feathers",
        "Philosophy of Software Design",
        "Unit Testing Principles, Practices",
        "Working Effectively with Legacy Code",
        "9781732102217",
        "9781617296277",
        "9780131177055",
        "MessageRenderer",
        "CrmContext",
        "CompanyFactory",
        "RAMCloud",
        "IndexLookup",
    )
    public_files = [
        REPO_ROOT / "AGENTS.md",
        REPO_ROOT / "README.md",
        REPO_ROOT / "docs" / "inventory.md",
        *sorted((REPO_ROOT / ".codex").rglob("*.md")),
        *sorted((REPO_ROOT / "scripts").glob("install-global.*")),
    ]
    for path in public_files:
        text = path.read_text(encoding="utf-8")
        for term in forbidden_terms:
            assert term not in text, f"{path}: found forbidden source identifier {term!r}"
        assert not re.search(r"[A-Za-z]:[\\/]Users[\\/][^\s]+", text), f"{path}: contains personal path"


def test_global_installer_supports_codex_claude_antigravity_and_opencode(tmp_path: Path) -> None:
    ps1_script = REPO_ROOT / "scripts" / "install-global.ps1"
    sh_script = REPO_ROOT / "scripts" / "install-global.sh"

    assert b"\r\n" not in sh_script.read_bytes()
    sh_text = sh_script.read_text(encoding="utf-8")
    for token in ("CLAUDE_HOME", "ANTIGRAVITY_HOME", "GEMINI_CONFIG_HOME", "OPENCODE_HOME", "INSTALL_TARGETS"):
        assert token in sh_text

    powershell_bin = shutil.which("pwsh") or shutil.which("powershell")
    assert powershell_bin is not None

    codex_home = tmp_path / "codex"
    claude_home = tmp_path / "claude"
    agy_home = tmp_path / "gemini" / "antigravity"
    gemini_config_home = tmp_path / "gemini" / "config"
    gemini_home = tmp_path / "gemini"
    opencode_home = tmp_path / "opencode"
    workspace_guide = tmp_path / "workspace" / "AGENTS.md"

    # Seed pre-existing user config and guides to verify preservation.
    codex_home.mkdir(parents=True)
    (codex_home / "config.toml").write_text('model = "custom-user-model"\n', encoding="utf-8")
    (codex_home / "AGENTS.md").write_text("# Custom User Codex Guide\n", encoding="utf-8")
    claude_home.mkdir(parents=True)
    (claude_home / "CLAUDE.md").write_text("# Custom User Claude Guide\n", encoding="utf-8")

    completed = subprocess.run(
        [
            powershell_bin,
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(ps1_script),
            "-CodexHome",
            str(codex_home),
            "-ClaudeHome",
            str(claude_home),
            "-AntigravityHome",
            str(agy_home),
            "-GeminiConfigHome",
            str(gemini_config_home),
            "-GeminiHome",
            str(gemini_home),
            "-OpenCodeHome",
            str(opencode_home),
            "-WorkspaceGuidePath",
            str(workspace_guide),
        ],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    assert "Global skillpack install complete" in completed.stdout

    expected_skills = [p.name for p in sorted(SKILLS_ROOT.iterdir()) if p.is_dir()]
    assert len(expected_skills) == 13

    for target_skills_root in (
        codex_home / "skills",
        claude_home / "skills",
        agy_home / "skills",
        gemini_config_home / "skills",
        gemini_home / "skills",
        opencode_home / "skills",
    ):
        for skill_name in expected_skills:
            assert (target_skills_root / skill_name / "SKILL.md").exists(), f"{target_skills_root}/{skill_name}"

    # Existing user config and guides are preserved while .agent-devkit.* reference copies are written.
    assert (codex_home / "config.toml").read_text(encoding="utf-8") == 'model = "custom-user-model"\n'
    assert (codex_home / "AGENTS.md").read_text(encoding="utf-8") == "# Custom User Codex Guide\n"
    assert (codex_home / "config.agent-devkit.toml").exists()
    assert (codex_home / "AGENTS.agent-devkit.md").exists()
    assert (claude_home / "CLAUDE.md").read_text(encoding="utf-8") == "# Custom User Claude Guide\n"
    assert (claude_home / "AGENTS.agent-devkit.md").exists()
    assert (opencode_home / "AGENTS.md").exists()
    assert workspace_guide.exists()
