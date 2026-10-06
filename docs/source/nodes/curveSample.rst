.. _node-curveSample:

curveSample
===========

Evaluate an open NURBS curve position or tangent component.

**Layer:** portable graph node. **Contract:** Scoped open NURBS curve.

**Aliases:** none.

When to use
-----------

Use for curve-driven numeric outputs; export CVs and knot/domain data rather than querying a Maya object at runtime.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - parameter (aliases u/uValue)
     - number endpoint
     - 0
     - Parameter or normalized coordinate, depending on mode.
   * - controlPoints[i].x/y/z
     - number endpoints
     - static controlPoints
     - Live control-point components.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - degree
     - integer
     - node-specific
     - Open curve degree; require at least degree+1 CVs.
   * - controlPoints
     - number[3][]
     - required
     - Ordered CVs in one declared space.
   * - knots (alias knotVector)
     - number[]
     - generated if absent
     - Full or supported compact knot sequence.
   * - minValue / maxValue
     - numbers
     - 0 / 1
     - Parameter domain.
   * - percentage (alias turnOnPercentage)
     - boolean
     - false
     - Interpret input as a normalized domain coordinate.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - positionX/Y/Z; tangentX/Y/Z; normalizedTangentX/Y/Z
     - number
     - computed
     - Curve sample components.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/curveSample.json>`.

.. literalinclude:: ../../../examples/graph/curveSample.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/curveSample.json --output json

Expected ``result``: **1**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
