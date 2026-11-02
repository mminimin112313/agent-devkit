from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_repo_docs_require_compile_first_absorption_of_superpowers() -> None:
    codex_readme = _read(".codex/README.md")
    codex_agents = _read(".codex/AGENTS.md")
    skills_readme = _read(".codex/skills/README.md")

    assert "compile imported execution systems into repo-local skills and rules before creating new top-level surface area" in codex_readme
    assert "large_or_multi_phase_work_should_route_through_repo_local_planning_before_execution" in codex_readme
    assert "PROMOTE(new_top_level_skill) ONLY IF existing_repo_local_owners_cannot_preserve(trigger_clarity AND output_contract_force)" in codex_agents
    assert "ROUTE(large_or_multi_phase_change) -> planning-and-scoping BEFORE implementation_or_release_completion" in codex_agents
    assert "compile useful `superpowers` behavior into existing repo-local skills first" in skills_readme
    assert "current absorbed `superpowers` convergence status: no remaining source currently requires a new top-level repo-local skill" in skills_readme


def test_skillsmith_records_top_level_admission_gate_and_parallel_namespace_ban() -> None:
    skillsmith = _read(".codex/skills/skillsmith/SKILL.md")
    record = _read(".codex/skills/skillsmith/assets/skill-authoring-record.md")
    skills_readme = _read(".codex/skills/README.md")

    assert "Do not ship a parallel top-level namespace when an existing repo-local skill can absorb the behavior without losing trigger clarity." in skillsmith
    assert "IF new_top_level_skill_is_proposed THEN REQUIRE(admission_gate_justification)" in skillsmith
    assert "IF external_behavior_is_being_imported AND imported_behavior_map_is_incomplete THEN STOP(\"finish the convergence audit before changing catalog surface area\")" in skillsmith
    assert "TARGET.admission_gate_justification :=" in record
    assert "TARGET.source_behavior_map :=" in record
    assert "PACKAGE.compile_first_absorption_kept := TRUE OR FALSE" in record
    assert "PACKAGE.parallel_namespace_added := TRUE OR FALSE" in record
    assert "PACKAGE.admission_gate_result := absorbed OR promoted" in record
    assert "PACKAGE.remaining_source_behaviors_needing_top_level_promotion :=" in record
    assert "do not present imported `superpowers` as a second public catalog" in skills_readme
