# Parallel Maintenance Dispatch

```text
DISPATCH.root_skill := .codex/skills/skillsmith/SKILL.md
DISPATCH.root_reference := .codex/skills/skillsmith/references/pseudocode-style-rules.md
DISPATCH.work_area :=
DISPATCH.command :=
DISPATCH.owned_paths :=
DISPATCH.required_reads :=
DISPATCH.stop_conditions :=
DISPATCH.return_contract :=

RETURN := PASS IF
  actual_work_area = DISPATCH.work_area
  AND edited_paths SUBSET_OF DISPATCH.owned_paths
  AND required_reads_loaded = TRUE
  AND deviations_recorded = TRUE
```
