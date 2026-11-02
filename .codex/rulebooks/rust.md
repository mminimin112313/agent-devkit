# Rust Rulebook

```text
SOURCE_STATUS := checked_primary_sources_http_200
ABSORPTION_DEPTH := starter_distillation
CATALOG_SEED := awesome-guidelines@e9eba9152e4c1d47522eddf5ae1a6bd482ee3e33
PRIMARY_SOURCES := {
  https://github.com/rust-lang/rust/tree/HEAD/src/doc/style-guide/src,
  https://rust-lang.github.io/api-guidelines/
}
OWNER_SKILLS := { implementation-backend, architecture-and-design, security-review, quality-and-review }

ABSORBED_RULES := {
  ownership_borrowing_and_lifetime_choices_are_part_of_api_design,
  error_types_and_result_boundaries_need_caller_evidence,
  unsafe_blocks_require_named_invariant_and_review_evidence,
  public_crate_surface_needs_compatibility_and_feature_boundary_notes,
  concurrency_traits_and_send_sync_assumptions_need explicit_verification
}

GENERALIZED_RULES := {
  rustfmt_style -> local_tooling_when_crate_exists,
  api_guidelines -> public_contract_review_lens
}

DEFERRED_RULES := {
  crate_layout_policy_without_rust_project,
  unsafe_policy_without_rust_surface
}

VERIFY := PASS IF
  unsafe_lifetime_error_and_public_api_edges_have_tests_or_review_notes
```

