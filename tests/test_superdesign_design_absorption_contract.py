from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_product_and_ux_absorbs_variation_wireframe_and_design_system_knowledge() -> None:
    skill = _read(".codex/skills/product-and-ux/SKILL.md")
    ideation = _read(".codex/skills/product-and-ux/references/ui-ideation-prompt-patterns.md")
    wireframe = _read(".codex/skills/product-and-ux/references/wireframe-discipline.md")
    extraction = _read(".codex/skills/product-and-ux/references/design-system-extraction.md")
    differentiation = _read(
        ".codex/skills/product-and-ux/references/visual-direction-differentiation-rules.md"
    )
    brief = _read(".codex/skills/product-and-ux/assets/product-brief.md")

    assert "references/wireframe-discipline.md" in skill
    assert "references/design-system-extraction.md" in skill
    assert "references/visual-direction-differentiation-rules.md" in skill
    assert "aesthetic direction" in skill
    assert "memorable differentiator" in skill
    assert "anti-generic frontend constraints" in skill
    assert "variation_count" in ideation
    assert "2_to_3_contrasted_concepts" in ideation
    assert "black_and_white_wireframes" in wireframe
    assert "layout_flow_and_hierarchy" in wireframe
    assert "design_system_json" in extraction
    assert "color_palette" in extraction
    assert "spacing_scale" in extraction
    assert "MEMORABLE_DIFFERENTIATOR := PASS IF" in differentiation
    assert "ANTI_GENERIC_FRONTEND := PASS IF" in differentiation
    assert "THEME_COMPARISON := PASS IF" in differentiation
    assert "the_same_visual_formula_could_fit_any_saas_landing_page" in differentiation
    assert "- aesthetic direction:" in brief
    assert "- memorable differentiator:" in brief
    assert "- theme system options compared:" in brief
    assert "- palette and typography pairing:" in brief
    assert "- anti-generic frontend constraints:" in brief


def test_implementation_frontend_absorbs_theme_handoff_and_preview_safe_rules() -> None:
    skill = _read(".codex/skills/implementation-frontend/SKILL.md")
    foundations = _read(".codex/skills/implementation-frontend/references/design-system-foundations.md")
    playbook = _read(".codex/skills/implementation-frontend/references/component-implementation-playbook.md")
    responsive = _read(".codex/skills/implementation-frontend/references/responsive-layout-patterns.md")
    rendered_ui = _read(".codex/skills/implementation-frontend/references/rendered-ui-proof.md")

    assert "theme_token_handoff" in foundations
    assert "component_only_presentation_work" in playbook
    assert "preview_safe_markup" in playbook
    assert "single_component_surface" in playbook
    assert "mobile_tablet_desktop" in responsive
    assert "presentation_proof" in responsive
    assert "references/design-system-foundations.md" in skill
    assert "references/rendered-ui-proof.md" in skill
    assert "readiness_wait_happens_before_dom_or_screenshot_inspection" in rendered_ui
    assert "selectors_come_from(rendered_dom OR accessibility_tree OR visible_ui_copy)" in rendered_ui
    assert "helper_script_source_is_read_first_when_help_output_would_suffice" in rendered_ui
