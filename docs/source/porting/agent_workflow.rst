Agent porting workflow
======================

Required input packet
---------------------

Provide the source scene, authorized SDK/source root, matching ``mayapy`` and
ORG plug-in, output directory, intended controller domain, target output cohort,
and tolerances with units. Optional root/mesh/controller hints reduce ambiguity.
Source identifiers and probes belong in private working artifacts.

Read :doc:`../getting_started`, :doc:`../nodes/index`, :doc:`../maya/index`, and
:doc:`decision_criteria`. The catalog records runtime support, not automatic
export coverage.

Execution sequence
------------------

1. Discover actual visible outputs, deformer history, transform outputs, and
   animator inputs. Resolve missing source dependencies before sampling.
2. Declare input/output order, units/spaces, topology, time requirements,
   resource ownership, and intended domains.
3. Audit closure: each dependency ends in a live input, proven constant,
   supported expression, deliberate boundary, or explicit blocker.
4. Lower using exact/scoped primitives first; use an explicit RBF, sampled, or
   fitted representation only with independent domain validation.
5. Wire numeric/packed interfaces and retain original controls and editable
   curves. Reconnect outputs through documented typed-unit boundaries.
6. Verify intermediate values/matrices, deformation, temporal behavior, and
   package relocation.
7. Deliver artifacts, tested domains/errors, remaining dependencies, exclusions,
   and replayable commands.

SDK export tooling
------------------

The SDK/source checkout includes discovery/export tooling. It is not included
in this docs-only repository. Inspect its installed command contracts first:

.. code-block:: console

   python tools/maya_coverage/run_org_v1_rig_round.py --help
   python tools/maya_coverage/run_org_v1_rig_round.py --selection-manifest selection.json --output-dir port_output --workers 1 --verify-samples 64 --mayapy /path/to/mayapy

Use the runner's installed selection/discovery manifest contracts; do not invent
their wire shape. The :doc:`procedural tutorial <tutorial>` is fully bundled.
Public importable entry points are listed in :doc:`../reference/python_api`.

Failure routing
---------------

* Discovery ambiguity: provide explicit mesh/control/output selection.
* Missing source dependency: restore the oracle environment before interpreting
  observations.
* Runtime gap: check existing representations before adding a primitive.
* Exporter gap: fix extraction/lowering/wiring when runtime support already exists.
* Unsupported state/topology: retain a deliberate boundary or report a blocker.
  Recursion guards do not prove constancy.
* Approximation failure: report the failed domain and expand independent tests;
  fitting rows are not sole acceptance evidence.
* Parity failure: identify the earliest failed intermediate output before
  altering final visible geometry.

Completion packet
-----------------

Return graph JSON, output mapping, input domains, resource manifest,
verification observations/results, and replay commands. Report all unresolved
and excluded outputs. Completion requires no unexplained missing outputs,
passing declared parity gates, preserved authoring behavior, and a relocatable
package. A load, export ratio, exit code, or still frame alone is insufficient.
