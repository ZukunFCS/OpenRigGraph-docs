Export and verification
=======================

Artifacts
---------

Keep graph JSON/compiled module, stable input/output mapping, relative resource
manifest with versions/hashes, source and independent verification observations,
per-output residuals/tolerances/units, tested domains, failures/exclusions, and
replay commands. SDK runners may emit reports, status, conformance, agent
packets, and handoff files; check their actual content and declared scope.

Layered acceptance
------------------

1. Check structural JSON, then semantic runtime compilation. The permissive
   structural schema cannot prove valid plugs/operations or source equivalence.
2. Compare primitive outputs, curve responses, local/parent/world matrices,
   and typed-unit boundaries before final deformation.
3. Compare the actual visible mesh cohort with stable vertex identity and
   coordinate space. Include required intermediate geometry deliberately.
4. Test neutral, extremes, blend interiors/endpoints, thresholds, curve knots,
   fractional times, rotation wraps, and relevant control combinations.
5. If state/history matters, test forward, reverse, and nonsequential evaluation.
6. Reopen a relocated package and repeat its declared acceptance observations.

Declare tolerances by output kind and unit. Also compare matrix translation and
transformed basis vectors; raw Euler differences can mislead across wraps.
For approximations, separate fitting from verification, report worst/RMS error,
and document domain coverage. An observed correlation is not proof of an
enforced input constraint and must not justify destructive specialization.

Authoring and performance
-------------------------

Preserve intended controls/curves. Test cache invalidation after edits, rebuild,
fractional-time policy, and stale-cache refusal. Measure the actual delivered
path with warmup, declared workloads, and percentile latency; compilation or
isolated operator speed is not scene-level performance evidence.
