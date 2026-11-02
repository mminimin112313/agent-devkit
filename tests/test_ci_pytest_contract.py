from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_github_actions_runs_pytest_on_push_and_pull_request() -> None:
    workflow = REPO_ROOT / ".github" / "workflows" / "pytest.yml"

    assert workflow.exists()

    body = workflow.read_text(encoding="utf-8")

    assert "push:" in body
    assert "pull_request:" in body
    assert "pytest -q" in body
