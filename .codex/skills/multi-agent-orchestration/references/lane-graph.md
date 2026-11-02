# Lane Graph

Do not run the work as a queue. Draw it as a graph and run every ready node at once, across several lanes.

## Build the graph (minutes, not an essay)

- **Node:** one unit of output with named inputs and named outputs (files, contracts, findings). Example: `contract:api`, `build:parser`, `build:ui`, `check:e2e`.
- **Edge:** node B reads an output of node A.
- **Lanes:** parallel tracks that always keep moving. Pick the ones the task needs:

| Lane | Nodes it holds |
| --- | --- |
| read | exploration, source reading, probing a load-bearing assumption |
| contract | interfaces, schemas, file formats, shared config written before fan-out |
| build | the actual changes, one writer per file |
| verify | the single final pass and its repair rounds |
| harness | skill, script, lint and instruction fixes found along the way |
| human | decisions only the user can make, posted and then left to wait |

Write the graph down as a short list or table in the run record, not as prose.

## Shared resources

Mark exclusive resources on nodes: a GPU, shared test database, device, deployment slot, or account. Treat each as a lock: run only one node that holds the same lock at a time, while unrelated nodes continue. Keep resource use inside current user and project authorization; contention does not authorize a platform or resource change.

## Run it

```text
LOOP
  ready = nodes whose inputs all exist and that are not done
  launch every ready node now, each lane in parallel, up to runtime concurrency
  when a node returns: open its output, mark it done, add nodes it revealed
  a changed input marks every downstream node stale; rerun only those
UNTIL only verify nodes remain, then run the final pass
```

- **Never idle a lane waiting on another.** A human-lane question is posted, then the other lanes keep running. A blocked build node leaves its siblings running.
- **Shortest path wins.** Reorder, merge or drop nodes whenever that shortens the critical path. The graph serves the outcome; it is not a contract.
- **Stale, not redone.** When a contract changes, rerun only its downstream nodes.
- **The coordinator is a lane too.** It takes a build or contract node itself instead of watching.

## Spawning

Spawn one agent per ready node, or per cluster of nodes sharing files. Do not wait for a full plan before the first spawn: read-lane agents can go out while the graph is still forming.

Honor the latest explicit user choices and applicable project instructions for models and reasoning effort, and check what the active runtime supports. For unspecified settings, inherit runtime defaults; do not encode a fixed model or effort in a generic skill. When the runtime permits seat selection and the task benefits from it, fit the choice to the node within the user's budget and project limits. Give agents the outcome, not a recipe.
