# Frontend and Remotion Rulebook

```text
SOURCE_STATUS := checked_primary_sources
CATALOG_SEED := awesome-guidelines@e9eba9152e4c1d47522eddf5ae1a6bd482ee3e33
PRIMARY_SOURCES := {
  https://react.dev/reference/react/useEffect,
  https://react.dev/reference/rules/rules-of-hooks,
  https://react.dev/learn/keeping-components-pure,
  https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch,
  https://developer.mozilla.org/en-US/docs/Web/API/EventSource,
  https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage,
  https://www.remotion.dev/llms.txt,
  https://www.remotion.dev/docs/register-root,
  https://www.remotion.dev/docs/composition,
  https://www.remotion.dev/docs/staticfile,
  https://www.remotion.dev/docs/delay-render,
  https://www.remotion.dev/docs/cancel-render
}
OWNER_SKILLS := { implementation-frontend, product-and-ux, quality-and-review }

ABSORBED_RULES := {
  react_render_stays_pure,
  hooks_remain_top_level,
  effects_name_external_system_and_dependencies,
  browser_fetch_sse_storage_boundaries_need_lifecycle_failure_evidence,
  remotion_entry_registers_root,
  remotion_root_registers_compositions,
  scene_components_do_not_smuggle_root_routing,
  remotion_async_assets_pair_delay_continue_or_cancel
}

GENERALIZED_RULES := {
  browser_api_detail -> lifecycle_and_failure_contract,
  remotion_renderer_detail -> deterministic_render_contract
}

DEFERRED_RULES := {
  framework_specific_frontend_style_without_surface,
  visual_regression_tooling_without_repo_command
}

VERIFY := PASS IF
  rendered_behavior_or_component_contract_is_inspected
  AND accessibility_or_timing_risk_has_fresh_evidence
```

