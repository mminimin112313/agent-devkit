from pathlib import Path
import re


REPO_ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def _assert_contains_all(body: str, parts: list[str]) -> None:
    for part in parts:
        assert part in body


def _declarations(body: str) -> set[str]:
    return set(re.findall(r"^([A-Z_]+)\s*:=", body, flags=re.MULTILINE))


def test_product_and_ux_references_are_logic_shaped_without_losing_menus() -> None:
    design_system = _read(".codex/skills/product-and-ux/references/design-system-methodology.md")
    mobile = _read(".codex/skills/product-and-ux/references/mobile-first-experience-principles.md")
    research = _read(".codex/skills/product-and-ux/references/ux-research-methods.md")
    accessibility = _read(".codex/skills/product-and-ux/references/interaction-accessibility-principles.md")

    assert "```text" in design_system
    assert {"DISCOVERY_INPUTS", "BUILD_ORDER", "PALETTE_METHOD", "QUALITY_GATES", "OUTPUT"} <= _declarations(design_system)
    _assert_contains_all(design_system, ["target_users", "brand_traits", "contrast_target", "reduced_motion", "light_or_dark_mode"])

    assert {"MOBILE_FIRST", "ACROSS_WIDTH_DECISIONS", "CHECKS", "OUTPUT"} <= _declarations(mobile)
    _assert_contains_all(mobile, ["persistent", "collapsed", "segmented", "full_width", "cropped", "deferred", "44px"])

    assert {"QUESTION_FIRST", "METHOD_SELECTION", "RESEARCH_SPINE", "GUARDRAILS"} <= _declarations(research)
    _assert_contains_all(research, ["interviews", "usability_tests", "prototype_reviews", "first_click_tests", "concept_comparison", "surveys", "analytics_review"])

    assert "USE_THIS_LENS IF" in accessibility
    assert {"CORE_RULES", "REVIEW_PROMPTS", "PROOF", "OUTPUT"} <= _declarations(accessibility)
    _assert_contains_all(accessibility, ["Tab", "Arrow_keys", "Enter", "Space", "Esc"])


def test_security_references_keep_bounded_evidence_rules() -> None:
    playbooks = _read(".codex/skills/security-lab/references/web-check-playbooks.md")
    review = _read(".codex/skills/security-review/references/web-app-review-playbook.md")
    rca = _read(".codex/skills/quality-and-review/references/root-cause-and-prevention.md")

    assert {"AUTHN_AUTHZ", "XSS", "SQLI", "SSRF", "FILE_UPLOAD_AND_PATH_TRAVERSAL", "COMMAND_EXECUTION_AND_DEBUG_EXPOSURE"} <= _declarations(playbooks)
    _assert_contains_all(playbooks, ["EVIDENCE_TO_KEEP", "object_id_used", "raw_payload", "candidate_parameter", "destination_url_used", "filename_and_content_type_used", "command_sink_or_debug_path", "STOP_IF", "parameterization_failure", "broader_extraction"])

    assert "USE_THIS_PLAYBOOK IF" in review
    assert {"AUTHN_AUTHZ", "XSS_AND_CONTENT_RENDERING", "SQLI_AND_DATA_ACCESS", "SSRF_OUTBOUND_FETCH", "FILESYSTEM_UPLOAD_COMMAND", "SECRETS_LOGGING_DEBUG"} <= _declarations(review)
    _assert_contains_all(review, ["http_request_or_response_bound", "parameterization", "allowlists", "redacted"])

    assert {"CONFIDENCE", "REVIEW_PASS", "ANTI_PATTERN"} <= _declarations(rca)
    _assert_contains_all(rca, ["confirmed", "estimated", "hypothesis_only", "data", "code", "infrastructure", "dependency", "workaround_and_next_owner"])


def test_assets_remain_form_shaped_while_references_get_compressed() -> None:
    research_asset = _read(".codex/skills/product-and-ux/assets/ux-research-plan.md")
    review_asset = _read(".codex/skills/security-review/assets/review-record.md")

    _assert_contains_all(
        research_asset,
        [
            "# UX Research Plan",
            "## Decision",
            "- product decision:",
            "- research questions:",
            "## Method",
            "## Execution",
            "## Output",
        ],
    )

    _assert_contains_all(
        review_asset,
        [
            "# Security Review Record",
            "PASS IF",
            "FAIL IF",
            "RECORD := {",
            "seam_reviewed",
            "trust_boundary",
            "evidence_checked",
            "next_skill_or_next_owner",
        ],
    )
