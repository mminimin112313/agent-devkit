# Scientific Languages Rulebook

```text
SOURCE_STATUS := checked_primary_sources_http_200_with_catalog_url_drift_noted
ABSORPTION_DEPTH := starter_distillation
CATALOG_SEED := awesome-guidelines@e9eba9152e4c1d47522eddf5ae1a6bd482ee3e33
PRIMARY_SOURCES := {
  https://google.github.io/styleguide/Rguide.html,
  https://style.tidyverse.org,
  https://github.com/JuliaDiff/BlueStyle,
  https://fortran-lang.org/learn/best_practices/
}
CATALOG_DRIFT := fortran-lang_catalog_url_redirected_from_/en/learn/best_practices/_to_/learn/best_practices/
OWNER_SKILLS := { implementation-backend, quality-and-review, architecture-and-design }

ABSORBED_RULES := {
  numerical_code_needs_units_precision_and_data_shape_evidence,
  vectorized_or_array_semantics_need edge_case_tests,
  notebooks_or_scripts_must_separate_exploration_from_reusable_pipeline_logic,
  scientific_results_need_reproducible_inputs_outputs_and_seed_or_environment_notes
}

GENERALIZED_RULES := {
  language_style_detail -> reproducibility_and_data_contract,
  plotting_or_notebook_convention -> artifact_provenance_contract
}

DEFERRED_RULES := {
  package_specific_scientific_style_without_project_surface,
  benchmark_policy_without measured_target
}

VERIFY := PASS IF
  data_shape_precision_units_seed_and_reproducibility_evidence_are_named
```

