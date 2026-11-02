from pathlib import Path
import re


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / ".codex" / "skills"

LOGIC_MARKERS = ("PASS IF", "FAIL IF", ":=", "ROUTE ->", "STOP(")


def test_reference_files_are_readable_and_local_links_resolve() -> None:
    reference_files = sorted(SKILLS_ROOT.glob("*/references/*.md"))

    assert reference_files

    missing = []
    for path in reference_files:
        body = path.read_text(encoding="utf-8-sig")
        lines = body.splitlines()
        if not lines or not lines[0].startswith("# ") or not "\n".join(lines[1:]).strip():
            missing.append(path.relative_to(REPO_ROOT).as_posix())
        for target in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", body):
            if target.startswith(("https://", "http://", "#")):
                continue
            assert (path.parent / target.split("#", 1)[0]).exists(), (path, target)

    assert not missing, f"reference files missing a readable title or body: {missing}"


def test_representative_assets_remain_form_shaped() -> None:
    asset_paths = [
        REPO_ROOT / ".codex" / "skills" / "product-and-ux" / "assets" / "ux-research-plan.md",
        REPO_ROOT / ".codex" / "skills" / "security-review" / "assets" / "review-record.md",
        REPO_ROOT / ".codex" / "skills" / "quality-and-review" / "assets" / "review-checklist.md",
    ]

    for path in asset_paths:
        body = path.read_text(encoding="utf-8")
        assert "#" in body
        assert "references/" not in body
