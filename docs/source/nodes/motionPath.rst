.. _node-motionPath:

motionPath
==========

Evaluate position and scoped orientation along an open NURBS curve.

**Layer:** portable graph node. **Contract:** Scoped curve motion path.

**Aliases:** none.

When to use
-----------

Use for captured path-follow behavior; distinguish raw parameter from fraction-mode arc-length traversal.

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
   * - minValue / maxValue
     - numbers
     - 0 / 1
     - Parameter domain.
   * - fractionMode
     - boolean
     - false
     - Resolve traversal fraction to a curve parameter.
   * - worldUpVector
     - number[3]
     - [0,1,0]
     - Up-vector basis.
   * - rotateOrder
     - integer enum
     - 0
     - Maya rotate-order code 0..5.
   * - anglesInDegrees
     - boolean
     - true
     - Rotation output units.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - allCoordinatesX/Y/Z; rotateX/Y/Z
     - number
     - computed
     - Path position and Euler rotation.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/motionPath.json>`.

.. literalinclude:: ../../../examples/graph/motionPath.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/motionPath.json --output json

Expected ``result``: **1**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
