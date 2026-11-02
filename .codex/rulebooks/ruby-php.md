# Ruby and PHP Rulebook

```text
SOURCE_STATUS := checked_primary_sources_http_200
ABSORPTION_DEPTH := starter_distillation
CATALOG_SEED := awesome-guidelines@e9eba9152e4c1d47522eddf5ae1a6bd482ee3e33
PRIMARY_SOURCES := {
  https://rubystyle.guide,
  https://raw.githubusercontent.com/airbnb/ruby/master/README.md,
  https://www.php-fig.org/psr/,
  https://www.phptherightway.com
}
OWNER_SKILLS := { implementation-backend, quality-and-review, security-review }

ABSORBED_RULES := {
  dynamic_language_public_methods_need_contract_tests,
  metaprogramming_and_magic_dispatch_need_explicit_reader_justification,
  framework_convention_must_not_hide_security_or_persistence_edges,
  dependency_autoload_and_namespace_behavior_need_runtime_probe_evidence
}

GENERALIZED_RULES := {
  rubocop_or_psr_formatting -> local_tooling_when_project_exists,
  community_style_detail -> readability_and_contract_evidence
}

DEFERRED_RULES := {
  rails_laravel_framework_rules_without_active_surface,
  formatter_linter_policy_without_repo_command
}

VERIFY := PASS IF
  dynamic_dispatch_namespace_security_and_persistence_edges_are_tested_or_reviewed
```

