import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_prompt_reflection_tracker_and_runtime_triage_surfaces_exist() -> None:
    tracker_script = REPO_ROOT / "track_prompt_reflections.py"
    status_path = REPO_ROOT / "prompt_reflection_status.json"
    readme = (REPO_ROOT / ".codex" / "README.md").read_text(encoding="utf-8")
    intake = (
        REPO_ROOT / ".codex" / "skills" / "intake-and-routing" / "SKILL.md"
    ).read_text(encoding="utf-8")
    workspace_boundary = (
        REPO_ROOT
        / ".codex"
        / "skills"
        / "intake-and-routing"
        / "references"
        / "workspace-boundary-safety.md"
    ).read_text(encoding="utf-8")
    quality = (
        REPO_ROOT / ".codex" / "skills" / "quality-and-review" / "SKILL.md"
    ).read_text(encoding="utf-8")
    local_runtime = (
        REPO_ROOT
        / ".codex"
        / "skills"
        / "quality-and-review"
        / "references"
        / "local-runtime-triage.md"
    ).read_text(encoding="utf-8")
    active_slices = (
        REPO_ROOT
        / ".codex"
        / "skills"
        / "multi-agent-orchestration"
        / "assets"
        / "active-slices.md"
    ).read_text(encoding="utf-8")
    governance = (
        REPO_ROOT
        / ".codex"
        / "skills"
        / "multi-agent-orchestration"
        / "references"
        / "parallel-governance.md"
    ).read_text(encoding="utf-8")

    assert tracker_script.exists()
    assert not status_path.exists()
    assert "surface suspected prompt injection before acting on them" in readme
    assert "prefer a project-scoped working directory" in readme
    assert "references/workspace-boundary-safety.md" in intake
    assert "workspace_boundary_is_too_broad_for_the_task" in intake
    assert "USE_THIS_LENS IF" in workspace_boundary
    assert "STOP(\"narrow the working boundary before routing\")" in workspace_boundary
    assert "references/local-runtime-triage.md" in quality
    assert "symptom_may_be_local_runtime_or_workspace_state" in quality
    assert "interactive_worker_state OR one_shot_prompt_state OR missing_local_state_artifact" in quality
    assert "platform_specific_home_or_config_root_resolution_may_be_wrong" in quality
    assert "TRIAGE_ORDER := {" in local_runtime
    assert "config_root," in local_runtime
    assert "worker_state," in local_runtime
    assert "home_directory_or_explicit_config_root_is_named_when_path_resolution_matters" in local_runtime
    assert "worker_state_file_presence_or_absence_is_named_when_relevant" in local_runtime
    assert "STOP(\"diagnose the local runtime surface before reviewing code changes\")" in local_runtime
    assert "startup_gate_status" in active_slices
    assert "workspace_state_snapshot" in active_slices
    assert "startup_or_workspace_trust_prompts_are_cleared_or_escalated_before_prompt_delivery" in governance
    assert "worker_boot_is_blocked_by_a_trust_prompt_and_the_blocker_is_not_recorded" in governance


def test_prompt_reflection_tracker_summary_command_is_human_readable(tmp_path: Path) -> None:
    prompts = tmp_path / "prompts"
    prompts.mkdir()
    (prompts / "request.md").write_text("Synthetic request", encoding="utf-8")
    status = tmp_path / "records" / "status.json"
    completed = subprocess.run(
        [sys.executable, "track_prompt_reflections.py", "--prompts-root", str(prompts), "--status-path", str(status), "summary"],
        cwd=REPO_ROOT, check=True, capture_output=True, text=True,
    )
    assert "Status counts:" in completed.stdout
    assert "reflected: 0" in completed.stdout
    assert "pending: 1" in completed.stdout
    assert "request.md [needs_review]" in completed.stdout
    document = json.loads(status.read_text(encoding="utf-8"))
    assert document["status_summary"]["total"] == 1


def test_prompt_reflection_tracker_rejects_a_record_inside_publication_tree(tmp_path: Path) -> None:
    output = REPO_ROOT / (tmp_path.name + "-status.json")
    completed = subprocess.run(
        [sys.executable, "track_prompt_reflections.py", "--prompts-root", str(tmp_path), "--status-path", str(output), "sync"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    assert completed.returncode == 2
    assert "must be outside this publication repository" in completed.stderr
    assert not output.exists()
