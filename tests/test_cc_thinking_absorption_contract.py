from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / ".codex" / "skills"


def _read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


SOURCE_SKILLS = [
    "thinking_archetypes",
    "thinking_bayesian",
    "thinking_bounded_rationality",
    "thinking_circle_of_competence",
    "thinking_cynefin",
    "thinking_debiasing",
    "thinking_dual_process",
    "thinking_effectuation",
    "thinking_feedback_loops",
    "thinking_fermi_estimation",
    "thinking_first_principles",
    "thinking_five_whys_plus",
    "thinking_inversion",
    "thinking_jobs_to_be_done",
    "thinking_kepner_tregoe",
    "thinking_leverage_points",
    "thinking_lindy_effect",
    "thinking_map_territory",
    "thinking_margin_of_safety",
    "thinking_model_combination",
    "thinking_model_router",
    "thinking_model_selection",
    "thinking_occams_razor",
    "thinking_ooda",
    "thinking_opportunity_cost",
    "thinking_pre_mortem",
    "thinking_probabilistic",
    "thinking_red_team",
    "thinking_regret_minimization",
    "thinking_reversibility",
    "thinking_scientific_method",
    "thinking_second_order",
    "thinking_socratic",
    "thinking_steel_manning",
    "thinking_systems",
    "thinking_theory_of_constraints",
    "thinking_thought_experiment",
    "thinking_triz",
    "thinking_via_negativa",
]


def test_cc_thinking_absorption_maps_all_source_skills_without_parallel_namespace() -> None:
    reference = _read(".codex/skills/skillsmith/references/thinking-skill-absorption.md")

    for skill in SOURCE_SKILLS:
        assert skill in reference

    assert "SOURCE := cc-thinking-skills@0313ee0d476bf9db2c38ad8bd11d9933a61350d4" in reference
    assert "CATALOG_RULE := do_not_create(thinking_*) AS top_level_repo_local_skills" in reference
    assert "source_reports_zero_robust_replicated_elevate_skills" in reference
    assert "thinking_regret_minimization -> EXCLUDE_AS_NON_FIT" in reference
    for line in reference.splitlines():
        if any(line.strip().startswith(skill + " ->") for skill in SOURCE_SKILLS):
            assert " -> " in line and line.split(" -> ", 1)[1].strip()

    assert not list(SKILLS_ROOT.glob("thinking-*"))


def test_destination_skills_reference_absorbed_reasoning_lenses() -> None:
    skillsmith = _read(".codex/skills/skillsmith/SKILL.md")
    quality = _read(".codex/skills/quality-and-review/SKILL.md")
    architecture = _read(".codex/skills/architecture-and-design/SKILL.md")
    planning = _read(".codex/skills/planning-and-scoping/SKILL.md")
    product = _read(".codex/skills/product-and-ux/SKILL.md")
    intake = _read(".codex/skills/intake-and-routing/SKILL.md")
    readme = _read(".codex/skills/README.md")

    assert "references/thinking-skill-absorption.md" in skillsmith
    assert "references/evidence-ladder-and-root-cause-lenses.md" in quality
    assert "references/decision-lens-guardrails.md" in architecture
    assert "references/risk-and-commitment-lenses.md" in planning
    assert "references/job-and-exploration-lenses.md" in product
    assert "mental_model_router_or_thinking_namespace" in intake
    assert "cc-thinking-skills" in readme


def test_new_thinking_absorption_references_are_logic_shaped() -> None:
    paths = [
        ".codex/skills/skillsmith/references/thinking-skill-absorption.md",
        ".codex/skills/quality-and-review/references/evidence-ladder-and-root-cause-lenses.md",
        ".codex/skills/architecture-and-design/references/decision-lens-guardrails.md",
        ".codex/skills/planning-and-scoping/references/risk-and-commitment-lenses.md",
        ".codex/skills/product-and-ux/references/job-and-exploration-lenses.md",
    ]

    for path in paths:
        body = _read(path)
        assert "```text" in body
        assert "PASS IF" in body
        assert "FAIL IF" in body
