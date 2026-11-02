# Convergence Rules

```text
PASS IF
  slice_ownership_is_disjoint
  AND shared_reads_do_not_require_shared_writes
  AND proof_is_checkable_per_slice
  AND integration_order_is_known_before_dispatch
  AND merge_strategy_is_named
  AND acceptance_owner_is_named

FAIL IF
  slice_depends_on_slice_output
  OR two_slices_share_the_same_file_or_decision
  OR single_owner_path_is_lower_risk
  OR fan_out_exists_only_for_status_theater

ROUTE -> assets/slice-record.md IF per_slice_proof_contract_is_fuzzy
ROUTE -> assets/convergence-record.md IF integration_order_or_acceptance_owner_is_the_main_risk
ROUTE -> assets/dispatch-handoff.md IF another_operator_cannot_execute_without_guessing
ROUTE -> assets/active-slices.md IF fan_out_is_live

STOP("collapse fan-out") IF overlap_grows OR shared_state_edits_dominate
```
