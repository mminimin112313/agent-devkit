# Signal-Driven Routing

```text
IF dominant_signal IN { research, persona, journey }:
  ROUTE -> `product-and-ux`
ELSE IF dominant_signal IN { feedback, complaints, churn_reasons }:
  ROUTE -> `product-and-ux`
ELSE IF dominant_signal IN { redesign, visual_direction, flow_shaping }:
  ROUTE -> `product-and-ux`
ELSE IF dominant_signal = competitive_direction_change:
  ROUTE -> `product-and-ux`
ELSE IF dominant_signal = cross_team_specification_packaging_after_direction_is_accepted:
  ROUTE -> `planning-and-scoping`
ELSE:
  ROUTE -> narrower_non_product_skill

STOP("do not force product routing") IF runtime_severity OR security_exposure OR implementation_ownership dominates
```
