# C and C++ Rulebook

```text
SOURCE_STATUS := checked_primary_sources_http_200
ABSORPTION_DEPTH := starter_distillation
CATALOG_SEED := awesome-guidelines@e9eba9152e4c1d47522eddf5ae1a6bd482ee3e33
PRIMARY_SOURCES := {
  https://users.ece.cmu.edu/~eno/coding/CCodingStandard.html,
  https://www.gnu.org/prep/standards/html_node/Writing-C.html,
  https://google.github.io/styleguide/cppguide.html,
  https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines,
  https://llvm.org/docs/CodingStandards.html,
  https://chromium.googlesource.com/chromium/src/+/HEAD/styleguide/c++/c++.md,
  https://webkit.org/code-style-guidelines/
}
OWNER_SKILLS := { implementation-backend, architecture-and-design, quality-and-review, security-review }

ABSORBED_RULES := {
  memory_ownership_and_lifetime_are_part_of_the_contract,
  public_headers_and_apis_need_stable_dependency_boundaries,
  undefined_behavior_and_platform_assumptions_need_review_evidence,
  low_level_changes_need_tests_or_probe_artifacts_near_the_runtime_boundary,
  style_detail_yields_to_project_local_consistency
}

GENERALIZED_RULES := {
  naming_formatting_preferences -> local_style_or_existing_file_pattern,
  performance_advice -> measured_evidence_before_optimization
}

DEFERRED_RULES := {
  compiler_specific_policy_without_repo_toolchain,
  safety_critical_rules_without_safety_owner,
  large_scale_c_or_cpp_architecture_rules_without_active_codebase
}

VERIFY := PASS IF
  ownership_lifetime_and_platform_boundary_are_named
  AND compile_test_or_runtime_probe_evidence_is_present
```

