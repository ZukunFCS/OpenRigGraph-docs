.. _node-closestPointOnSurface:

closestPointOnSurface
=====================

Find a closest position on a captured open NURBS surface.

**Layer:** portable graph node. **Contract:** Scoped open NURBS surface query.

**Aliases:** none.

When to use
-----------

Use for the supported numeric surface-position query. It does not evaluate arbitrary Maya surface nodes or deformation history.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - inPositionX/Y/Z
     - number endpoints
     - 0
     - Query point in the surface CV space.
   * - controlPoints[i].x/y/z
     - number endpoints
     - static CVs
     - Surface control-point components.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - degreeU / degreeV; uCount / vCount
     - integers
     - 3 / 3; counts required
     - Each axis requires at least degree+1 CVs.
   * - controlPoints
     - number[3][]
     - required
     - Flattened surface CV grid.
   * - knotsU / knotsV
     - number[]
     - generated if absent
     - Full count+degree+1 or compact count+degree-1 knot vectors.
   * - minU / maxU / minV / maxV
     - numbers
     - 0 / 1 / 0 / 1
     - Surface parameter domains.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - positionX/Y/Z
     - number
     - computed
     - Closest position; parameter and normal outputs are not part of this contract.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/closestPointOnSurface.json>`.

.. literalinclude:: ../../../examples/graph/closestPointOnSurface.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/closestPointOnSurface.json --output json

Expected ``result``: **0**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
