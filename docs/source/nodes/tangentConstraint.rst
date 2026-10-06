.. _node-tangentConstraint:

tangentConstraint
=================

Orient toward the tangent of a captured open curve.

**Layer:** portable graph node. **Contract:** Scoped curve tangent orientation.

**Aliases:** none.

When to use
-----------

Use for tangent-driven orientation with known aim/up basis and parent-space conversion.

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
   * - aimVector / upVector / worldUpVector
     - number[3]
     - X / Y / Y
     - Orientation basis vectors.
   * - constraintParentInverseMatrix
     - number[16]
     - identity
     - Captured parent inverse basis.
   * - anglesInDegrees
     - boolean
     - true
     - Set false for radian-valued Euler/angle channels.
   * - rotateOrder
     - string
     - xyz
     - xyz, yzx, zxy, xzy, yxz, or zyx; check node-specific integer order fields.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - constraintRotateX/Y/Z
     - number
     - computed
     - Constrained Euler rotation.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/tangentConstraint.json>`.

.. literalinclude:: ../../../examples/graph/tangentConstraint.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/tangentConstraint.json --output json

Expected ``result``: **0**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
