# Functional and Dynamic Languages Rulebook

```text
SOURCE_STATUS := checked_primary_sources_http_200
ABSORPTION_DEPTH := starter_distillation
CATALOG_SEED := awesome-guidelines@e9eba9152e4c1d47522eddf5ae1a6bd482ee3e33
PRIMARY_SOURCES := {
  https://github.com/bbatsov/clojure-style-guide,
  https://www.erlang.org/doc/system/secure_coding.html,
  https://dlang.org/dstyle.html,
  https://dart.dev/effective-dart
}
OWNER_SKILLS := { implementation-backend, architecture-and-design, security-review, quality-and-review }

ABSORBED_RULES := {
  immutable_data_and_side_effect_boundaries_should_be_explicit,
  message_passing_actor_or_async_edges_need_failure_and_shutdown_evidence,
  macro_reflection_or_code_generation_requires_reader_and_security_justification,
  package_public_surface_needs_compatibility_evidence_even_when_language_is_dynamic
}

GENERALIZED_RULES := {
  paradigm_specific_idioms -> architecture_decision_record_when_crossing_repo_norms,
  secure_coding_detail -> trust_boundary_review_lens
}

DEFERRED_RULES := {
  language_tooling_policy_without_active_project,
  ecosystem_specific_scaffold_without_owner
}

VERIFY := PASS IF
  side_effect_message_passing_async_and_generated_code_boundaries_are_reviewed
```

