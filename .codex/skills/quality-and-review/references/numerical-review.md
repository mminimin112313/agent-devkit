# Numerical comparison and disputed criteria

Use when a floating-point comparison fails or the user questions its threshold. For a repository
with its own numerical procedure, use that owner for tools and acceptance policy.

1. Inspect the actual failed report, metric formula, limit and provenance. State the equivalence
   promised by the change: exact bytes, numerical accuracy, or an authorized approximation.
   Preserve the failing result. A failed criterion is evidence of a miss, not proof of its cause.
2. Verify the comparison contract: identical inputs, producer/backend versions, shapes/layouts,
   seeds, checkpoint and implementation. Inspect actual operand/accumulator/rounding precision;
   stored dtype alone does not establish compute precision.
3. Localize the first difference and compare affected/unaffected cases. Distinguish indexing,
   masking, alias/lifetime errors; changed reduction/algorithm/casts; reference variability;
   and a wrong metric or selected policy. Use the cheapest observation that separates the
   plausible causes. Error magnitude or growth pattern alone is not a causal test.
4. If the criterion may be unsuitable, independently calibrate the reference's numerical floor
   or same-setting spread and compare both implementations to a higher-precision result where
   useful. Preserve representative/edge coverage and a defect-sensitive negative control.
   Do not derive the limit from the candidate's failure or transplant another workload's floor.
   Exact transport and structural contracts remain exact; invalid/nonfinite evidence is not noise.
5. Check the promised user-visible result using the task's criteria and actual artifacts. For
   video this may include localized RGB errors, all split joins and motion. Local and final-output
   evidence answer different questions; neither silently replaces a required gate.
6. Apply existing authority to any policy correction. A new accuracy trade or numeric limit
   follows the task's governance; investigation does not require a new approval. Keep old/new
   reports distinct and explain the calibration. Never relax a limit merely to obtain a pass.

Report the observation, criterion validity, cause confidence and output impact separately. If
unresolved, name the missing evidence and smallest next check. A candidate can remain disabled
while its cause is unknown; do not describe an untested cause as a confirmed defect or harmless
rounding, or promote unaccepted diagnostic timings into a performance claim.
