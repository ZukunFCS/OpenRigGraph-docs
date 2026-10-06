Choose the representation
=========================

Use source behavior and the required domain to choose a contract. Similar node
names do not establish compatible plugs, spaces, or interpolation modes.

.. list-table::
   :header-rows: 1

   * - Representation
     - Use when
     - Evidence
   * - Exact primitive
     - A documented operation expresses the behavior.
     - Correct plugs, units, defaults, and boundary cases.
   * - Scoped transform/constraint/IK/geometry
     - Topology/configuration fit the documented subset.
     - Captured spaces/basis/offsets and independent source parity.
   * - RbfNode
     - Kernel, centers, and evaluation coefficients are explicit.
     - Independent domain validation, beyond training centers.
   * - SampledNode
     - Sample replay/interpolation is the intended contract.
     - Coverage, discontinuities, and held-out residuals.
   * - ModelNode / ApproxNode
     - A sparse-linear response meets the error budget.
     - Separate fit/verification rows and per-output errors.
   * - External boundary
     - A DCC/provider-owned operation intentionally remains external.
     - Explicit interfaces, dependencies, resource/state lifetimes.
   * - New general-purpose node
     - Existing contracts cannot express a useful reusable behavior.
     - Source-neutral semantics, independent fixtures, regression tests.

Current scope
-------------

ORG supports documented numeric utilities, curves, vectors/quaternions, affine
matrix paths, scoped constraints/rotate-plane IK, explicit surface contracts,
and opt-in Maya geometry integration. Check individual pages. Arbitrary DCC
graphs, materials, simulation, mutable topology, and undeclared solver state
are not automatically portable; retain boundaries or explain exclusions.

Prefer exporter decomposition before adding nodes. New nodes need explicit
typed interfaces, units/spaces, domains, errors, determinism/state, resources,
and independent tests. Do not add source-specific runtime wrappers to make an
export appear complete. See :doc:`design_decisions` for invented examples.
