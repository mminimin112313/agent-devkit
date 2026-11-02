from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_release_skill_absorbs_worktree_and_branch_finish_rules() -> None:
    release = _read(".codex/skills/release-and-operations/SKILL.md")
    gate = _read(".codex/skills/release-and-operations/assets/release-gate.md")
    review = _read(".codex/skills/release-and-operations/assets/release-review-checklist.md")
    launch = _read(".codex/skills/release-and-operations/assets/launch-readiness-checklist.md")
    rollback = _read(".codex/skills/release-and-operations/assets/rollback-record.md")
    evidence = _read(".codex/skills/release-and-operations/references/release-evidence.md")

    assert "isolated_workspace_readiness_must_be_checked_before_execution_or_release_completion" in release
    assert "branch_finish_requires_explicit_option_selection_after_fresh_verification" in release
    assert "worktree_or_workspace_path" in gate
    assert "branch_disposition_option" in gate
    assert "base_branch_or_merge_target" in gate
    assert "workspace_isolation_verified" in review
    assert "merge_or_pr_option_selected_explicitly" in review
    assert "worktree_baseline_or_workspace_baseline_checked" in launch
    assert "worktree_cleanup_owner" in rollback
    assert "keep_branch_as_is_is_allowed_without_forced_cleanup" in evidence
    assert "discard_requires_explicit_confirmation" in evidence


def test_shared_repo_docs_keep_release_absorption_repo_local() -> None:
    readme = _read(".codex/README.md")
    codex_agents = _read(".codex/AGENTS.md")
    skills_readme = _read(".codex/skills/README.md")

    assert "large_or_multi_phase_work_should_route_through_repo_local_planning_before_execution" in readme
    assert "ROUTE(large_or_multi_phase_change) -> planning-and-scoping BEFORE implementation_or_release_completion" in codex_agents
    assert "branch exit, isolated workspace setup, and release completion stay inside repo-local planning or release owners" in skills_readme
