import json
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_root_readme_documents_global_install_and_validation() -> None:
    readme = _read("README.md")

    assert "## Install Globally" in readme
    assert '.\\scripts\\install-global.ps1' in readme
    assert "sh ./scripts/install-global.sh" in readme
    assert "Set `CODEX_HOME` to install somewhere other than `$HOME/.codex`." in readme
    assert "WORKSPACE_GUIDE_PATH=\"$HOME/projects/AGENTS.md\" sh ./scripts/install-global.sh" in readme
    assert not re.search(r"[A-Za-z]:[\\/]Users[\\/][^\s]+", readme)
    assert "python -m pip install -r requirements-dev.txt" in readme
    assert "python -m pytest -q" in readme
    assert "Do not scan public or third-party targets with `security-lab`." in readme


def test_global_install_scripts_are_repo_relative_and_portable() -> None:
    ps1 = _read("scripts/install-global.ps1")
    sh = _read("scripts/install-global.sh")
    inventory = _read("docs/inventory.md")

    assert "$PSCommandPath" in ps1
    assert '$env:CODEX_HOME' in ps1
    assert "WorkspaceGuidePath" in ps1
    assert "Copy-Item -Recurse -Force" in ps1
    assert "skills\\skillsmith\\SKILL.md" in ps1
    assert not re.search(r"[A-Za-z]:[\\/]Users[\\/][^\s]+", ps1)

    assert 'repo_root=$(CDPATH= cd -- "$script_dir/.." && pwd -P)' in sh
    assert 'CODEX_HOME:-"$HOME/.codex"' in sh
    assert "WORKSPACE_GUIDE_PATH" in sh
    assert 'cp -R "$source_codex"/. "$codex_home"/' in sh
    assert "skills/skillsmith/SKILL.md" in sh
    assert not re.search(r"[A-Za-z]:[\\/]Users[\\/][^\s]+", sh)

    assert "scripts/install-global.ps1" in inventory
    assert "scripts/install-global.sh" in inventory
    assert "portable_global_install" in inventory


def test_docs_inventory_is_required_living_map() -> None:
    root_agents = _read("AGENTS.md")
    codex_agents = _read(".codex/AGENTS.md")
    inventory = _read("docs/inventory.md")

    assert "For meaningful changes, update `docs/` in the same change" in root_agents
    assert "REQUIRE(docs_updated_under_docs)" in codex_agents
    assert "This document is the living map for the repository." in inventory
    assert "file_layout OR operating_logic OR workflow_contract OR verification_contract OR security_boundary" in inventory
    assert "verification_evidence" in inventory


def test_pytest_workflow_uses_dev_requirements_permissions_matrix_and_shellcheck() -> None:
    workflow = _read(".github/workflows/pytest.yml")
    requirements = _read("requirements-dev.txt")

    assert "permissions:" in workflow
    assert "contents: read" in workflow
    assert 'python-version: ["3.11", "3.12"]' in workflow
    assert "python -m pip install -r requirements-dev.txt" in workflow
    assert "python -m pytest -q" in workflow
    assert "shellcheck .codex/skills/security-lab/scripts/*.sh" in workflow
    assert "pytest>=8.3,<9" in requirements


def test_gitignore_excludes_generated_security_and_secret_artifacts() -> None:
    gitignore = _read(".gitignore")

    assert "artifacts/" in gitignore
    assert "*.tar.gz" in gitignore
    assert "*.log" in gitignore
    assert ".env" in gitignore
    assert ".env.*" in gitignore
    assert "!.env.example" in gitignore


def test_mail_handoff_surface_is_removed_from_active_skills() -> None:
    assert not (REPO_ROOT / ".codex/skills/multi-agent-orchestration/assets/mail-handoff.md").exists()
    assert not (REPO_ROOT / ".codex/skills/release-and-operations/assets/mail-handoff.md").exists()

    active_files = [
        ".codex/skills/multi-agent-orchestration/SKILL.md",
        ".codex/skills/release-and-operations/SKILL.md",
        ".codex/skills/README.md",
    ]
    for path in active_files:
        assert "mail-handoff" not in _read(path)


def test_every_top_level_skill_requires_root_cause_solution_and_approved_workarounds() -> None:
    skills_root = REPO_ROOT / ".codex" / "skills"
    skill_files = sorted(skills_root.glob("*/SKILL.md"))
    assert skill_files

    for path in skill_files:
        body = path.read_text(encoding="utf-8")
        assert "<ROOT-CAUSE-SOLUTION-HOOK>" in body, path
        assert "IF problem_solving_requires(fallback OR workaround OR bypass OR temporary_patch) THEN" in body, path
        assert "ASK_USER_APPROVAL(reason, scope, risk, rollback_plan) BEFORE applying_non_root_solution" in body, path
        assert "PREFER(root_cause_fix) OVER(symptom_workaround)" in body, path
        assert "STOP(\"fallback or workaround requires explicit user approval and a root-cause plan\") IF approval_is_missing" in body, path

    root_agents = _read("AGENTS.md")
    codex_agents = _read(".codex/AGENTS.md")
    skills_readme = _read(".codex/skills/README.md")
    inventory = _read("docs/inventory.md")

    assert "Problem solving must target the root cause and apply a fundamental fix." in root_agents
    assert "REQUIRE(root_cause_solution := diagnose_root_cause + apply_fundamental_fix + verify_behavior) WHEN solving_problem" in codex_agents
    assert "REQUIRE(user_approval_for_non_root_solution := reason + scope + risk + rollback_plan) BEFORE fallback_or_workaround_or_bypass_or_temporary_patch" in codex_agents
    assert "keep a `ROOT-CAUSE-SOLUTION-HOOK` in every top-level skill" in skills_readme
    assert "every top-level SKILL.md carries a ROOT-CAUSE-SOLUTION-HOOK near the portability mandate" in inventory


def test_security_lab_requires_explicit_sample_target_and_signature_diff() -> None:
    bootstrap = _read(".codex/skills/security-lab/scripts/bootstrap-lab.sh")
    run_checks = _read(".codex/skills/security-lab/scripts/run-web-checks.sh")
    verify = _read(".codex/skills/security-lab/scripts/verify-fix.sh")

    assert "ALLOW_SAMPLE_TARGET" in bootstrap
    assert "set TARGET_CONTAINER or TARGET_IMAGE" in bootstrap
    assert "findings-summary.json" in run_checks
    assert "tool-status.tsv" in run_checks
    assert "signature" in run_checks
    assert "verification-diff.json" in verify
    assert "remaining_high_or_critical_count" in verify


def test_parallel_limit_matches_config_choice() -> None:
    codex_agents = _read(".codex/AGENTS.md")
    config = _read(".codex/config.toml")

    assert "PARALLEL_LIMIT := up_to_twelve_workers" in codex_agents
    assert "max_threads = 12" in config


def test_non_trivial_work_requires_distinct_planner_implementer_and_evaluator() -> None:
    root_agents = _read("AGENTS.md")
    codex_agents = _read(".codex/AGENTS.md")
    planning = _read(".codex/skills/planning-and-scoping/SKILL.md")
    orchestration = _read(".codex/skills/multi-agent-orchestration/SKILL.md")
    quality = _read(".codex/skills/quality-and-review/SKILL.md")
    inventory = _read("docs/inventory.md")

    assert "define evaluation criteria before implementation" in root_agents
    assert "planner, implementer, and evaluator" in root_agents
    assert "REQUIRE(evaluation_criteria) BEFORE implementation_begins" in codex_agents
    assert "planner != implementer AND implementer != evaluator AND planner != evaluator" in codex_agents
    assert "SUBAGENT_EVALUATION := USE_distinct_subagents_when_available" in codex_agents
    assert "<EVALUATION-GATE>" in planning
    assert "exact_planner, exact_executor, exact_evaluator" in planning
    assert "<EVALUATION-SEPARATION-GATE>" in orchestration
    assert "fresh_evaluator_subagent_after_implementation" in orchestration
    assert "<EVALUATOR-INDEPENDENCE-GATE>" in quality
    assert "inspect_artifacts(changed_files, generated_outputs, docs, logs, screenshots_or_renders_when_relevant)" in quality
    assert "non-trivial work separates planner, implementer, and evaluator roles" in inventory


def test_programming_work_requires_search_config_scaffold_line_counts_and_stepwise_review() -> None:
    root_agents = _read("AGENTS.md")
    codex_agents = _read(".codex/AGENTS.md")
    planning = _read(".codex/skills/planning-and-scoping/SKILL.md")
    backend = _read(".codex/skills/implementation-backend/SKILL.md")
    frontend = _read(".codex/skills/implementation-frontend/SKILL.md")
    quality = _read(".codex/skills/quality-and-review/SKILL.md")
    inventory = _read("docs/inventory.md")

    assert "Programming work must search existing code, tests, docs, config, and patterns before editing" in root_agents
    assert "if the preferred search tool fails or is permission-denied" in root_agents
    assert "without narrowing the intended search scope or bypassing existing ignore intent" in root_agents
    assert "avoid hardcoded addresses or environment-specific values" in root_agents
    assert "god classes" in root_agents
    assert "line counts" in root_agents
    assert "REQUIRE(search_evidence := broad_search + targeted_search + existing_pattern_check)" in codex_agents
    assert "REQUIRE(search_fallback := record_command_failure_signal + use_shell_native_fallback + preserve_search_scope + preserve_existing_ignore_intent)" in codex_agents
    assert "REQUIRE(no_hardcoded_addresses_or_environment_values) IN application_logic" in codex_agents
    assert "REQUIRE(extension_scaffold_without_god_class)" in codex_agents
    assert "REQUIRE(line_count_audit_changed_files) BEFORE final_handoff" in codex_agents
    assert "IMPLEMENTATION_MODEL := search_first + search_tool_fallback + root_cause_solution + verify_uncertainty + scaffold_extension_seams + avoid_god_class + line_count_audit + stepwise_execution" in codex_agents
    assert "<SCAFFOLD-GATE>" in planning
    assert "SEARCH(existing_code, tests, docs, config, patterns)" in planning
    assert "FAIL IF planned_structure_contains_god_class OR hardcoded_address_path_is_planned" in planning
    assert "line_count_audit_step" in planning
    assert "<IMPLEMENTATION-HYGIENE-GATE>" in backend
    assert "SEARCH(existing_implementations, tests, docs, config, adapters, environment_patterns)" in backend
    assert "SPLIT_OR_JUSTIFY IF source_file_lines > local_limit OR source_file_lines > 300" in backend
    assert "<IMPLEMENTATION-HYGIENE-GATE>" in frontend
    assert "SEARCH(existing_components, tests, docs, config, routes, design_tokens, data_adapters)" in frontend
    assert "component_file_lines > local_limit OR component_file_lines > 200 OR source_file_lines > 300" in frontend
    assert "<CODE-HYGIENE-REVIEW-GATE>" in quality
    assert "hardcoded_address_scan" in quality
    assert "oversized_file_without_split_or_justification" in quality
    assert "search_code_tests_docs_config_before_editing" in inventory
    assert "record_search_command_failure_and_preserve_scope_and_ignore_intent_with_fallback" in inventory
    assert "proceed_step_by_step_with_clean_stop_points" in inventory


def test_skill_support_file_mentions_resolve_to_existing_files() -> None:
    skills_root = REPO_ROOT / ".codex" / "skills"
    support_path_pattern = re.compile(r"(?<![\w./-])((?:assets|references)/[A-Za-z0-9_.-]+\.md)")
    missing = []

    for skill_file in sorted(skills_root.glob("*/SKILL.md")):
        body = skill_file.read_text(encoding="utf-8")
        for relative_support_path in support_path_pattern.findall(body):
            if not (skill_file.parent / relative_support_path).exists():
                missing.append(f"{skill_file.parent.name}: {relative_support_path}")

    assert not missing
    assert "SKILL.md support file mentions resolve to existing skill-local assets or references" in _read("docs/inventory.md")


def test_agent_instructions_front_load_identity_lane_and_forbidden_behavior() -> None:
    agents_guidance = _read(".codex/agents/AGENTS.md")
    assert "front-load the structurally important contract" in agents_guidance

    repo_agent_files = sorted((REPO_ROOT / ".codex" / "agents").glob("*.toml"))
    assert repo_agent_files
    for path in repo_agent_files:
        first_text = "\n".join(path.read_text(encoding="utf-8").splitlines()[:18])
        assert "Role identity is mandatory." in first_text, path
        assert "Stay inside this role's lane." in first_text, path
        assert "Start the first substantive handoff line" in first_text, path
        assert "Do not present yourself as the orchestrator" in first_text, path

    skill_agent_files = sorted((REPO_ROOT / ".codex" / "skills").glob("*/agents/*.md"))
    assert skill_agent_files
    for path in skill_agent_files:
        first_lines = path.read_text(encoding="utf-8").splitlines()[:45]
        first_text = "\n".join(first_lines)
        first_nonblank = next(line for line in first_lines if line.strip())
        assert first_nonblank.startswith("You are") or first_nonblank == "Compatibility bridge only.", path
        assert "Own:" in first_text or "<identity>" in first_text or "Canonical execution roles:" in first_text, path
        assert "Do not:" in first_text or "<must_not_do>" in first_text or "Never answer as" in first_text, path


def test_shell_scripts_are_lf_normalized_by_git_attributes() -> None:
    attributes = _read(".gitattributes")

    assert "*.sh text eol=lf" in attributes
    for script in (REPO_ROOT / ".codex" / "skills" / "security-lab" / "scripts").glob("*.sh"):
        assert b"\r\n" not in script.read_bytes(), script




def test_skill_descriptions_are_specific_and_do_not_claim_overriding_authority() -> None:
    skill_files = sorted((REPO_ROOT / ".codex/skills").glob("*/SKILL.md"))
    assert len(skill_files) == 13
    for path in skill_files:
        body = path.read_text(encoding="utf-8")
        description = next(line for line in body.splitlines() if line.startswith("description:"))
        assert len(description) > 35, path
        for phrase in ("ABSOLUTE MANDATE", "fanatical", "fatal contract violation", "god-given"):
            assert phrase not in body, path
        assert "## Procedure" in body, path


def test_removed_memory_surface_has_no_active_routes() -> None:
    removed = "failure" + "-memory"
    assert not (REPO_ROOT / ".codex/skills" / removed).exists()
    assert not (REPO_ROOT / ".codex/lessons").exists()
    active = [REPO_ROOT / "AGENTS.md", REPO_ROOT / "README.md", REPO_ROOT / "pytest.ini"]
    active += list((REPO_ROOT / ".codex").glob("*.md"))
    active += list((REPO_ROOT / ".codex/skills").glob("*/SKILL.md"))
    active += list((REPO_ROOT / "scripts").glob("install-global.*"))
    for path in active:
        body = path.read_text(encoding="utf-8")
        assert removed not in body, path
        assert "FAILURE-MEMORY-HOOK" not in body, path
