# Frontend Implementation Guardrails

Trace impact beyond direct callers: shared mutable state and aliases, inherited or dynamically dispatched behavior, and observable I/O or events can carry a change into other consumers. Use these paths to choose regression checks; a small diff or a static call graph alone does not establish safety.

When coupling prevents a useful check, separate a minimal reviewed behavior-preserving boundary edit from the requested functional change. Check the available build, type, source, and runtime observations, then capture baseline behavior before changing the function. Report unavailable observations honestly. A successful build supports the edit but does not establish behavioral equivalence.

Keep preparation, structural edits, and functional edits attributable by running fast relevant checks between them. Run the project's required acceptance checks for the final result. Preserve existing work rather than restarting solely to enforce a test-writing sequence.

Review a preparatory boundary edit through its diff and available observations; this does not require a separate user approval round. Preserve the default production wiring, initialization order, failure timing, and error propagation. If any of those contracts changes, separate it as an intended behavior change rather than claiming preservation. Name an actual unavailable environment or dependency and its unverified scope when blocked; inconvenient test setup alone does not make verification unavailable.

When a regression test for a fix or new behavior was added after implementation, confirm its expected failure against a disposable pre-change copy or with only the fix disabled in an isolated copy. Keep the live checkout and existing work intact. Do not require a preservation baseline to fail. If the comparison cannot run, report that evidence gap instead of treating the new passing test as proof that it detects the regression.

Choose checks by what can change, including generated behavior, schemas, executable documentation, and rendered layout. Use the relevant build, render, or runtime check for those effects; a pure wording edit does not need an unrelated new unit test.

When browser storage, server communication, or event delivery is the changed contract, check that interaction at a real integration boundary. A mock replacing the interaction can establish local behavior but cannot establish that the integration works.

Keep component and state modules deep: expose a small, clear contract for the common case while hiding internal state representations, layout calculations, and event plumbing. Separate general-purpose UI primitives from feature-specific policy, avoid threading pass-through props across intermediate layers that add no abstraction, and model normal-case state so empty, boundary, and selection cases work without scattered special-case conditionals. Extract complex state transitions and derived calculations into pure functions or state models verified with output-based or state-based tests, and keep browser APIs, network requests, and timers inside humble boundary adapters or controllers rather than mixing deep branching logic with many mutable collaborators.

```text
PASS IF
  composition_and_seam_local_state_are_preferred_over_multi_responsibility_components
  AND loading_error_empty_disabled_and_recovery_states_are_explicit_before_polish
  AND async_and_data_wiring_stay_at_the_nearest_useful_boundary
  AND pure_state_and_selector_decisions_are_separated_from_browser_and_network_side_effects
  AND component_contracts_hide_internal_representation_and_avoid_pass_through_prop_drilling

FAIL IF
  new_dependency_materially_changes_the_seam
  OR caching_layer_materially_changes_the_seam
  OR rendering_strategy_materially_changes_the_seam
  OR a_component_combines_deep_branching_logic_with_many_out_of_process_or_browser_collaborators
  OR tests_mock_internal_component_collaborators_instead_of_verifying_observable_rendered_or_state_outcomes

IF FAIL THEN ROUTE -> planning-and-scoping
```
