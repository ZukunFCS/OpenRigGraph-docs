.. _node-scaleConstraint:

scaleConstraint
===============

Compute a weighted geometric scale, rather than an arithmetic mean.

**Layer:** portable graph node. **Contract:** Scoped constraint.

**Aliases:** none.

When to use
-----------

Use when the source constraint's targets, spaces, weights, offset, and interpolation mode are all known.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - target[i].targetTranslateX/Y/Z; target[i].targetRotateX/Y/Z; target[i].targetScaleX/Y/Z
     - number endpoints
     - 0 / 0 / 1
     - Ordered target channels.
   * - target[i].targetWeight
     - number endpoint
     - target record weight, else 1
     - Dynamic target weight.
   * - constraintParentInverseMatrix; target[i].targetParentMatrix
     - matrix endpoints
     - identity
     - Source-space conversion for matrix-aware paths.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - targets
     - nonempty target-record[]
     - required
     - Records preserve translate, rotate, scale, weight, targetParentMatrix, and captured input offsets.
   * - normalize
     - boolean
     - true
     - Normalize scalar weighted paths by total weight.
   * - translateOffset / rotateOffset / scaleOffset
     - number[3]
     - 0 / 0 / 1
     - Captured maintain-offset behavior.
   * - matrixConstraint / matrixTranslateConstraint / matrixOrientConstraint
     - booleans
     - false
     - Select the scoped matrix-aware lowering path.
   * - interpType
     - static integer
     - captured source mode
     - Orientation interpolation support is path-specific; verify the exported mode.
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
   * - constraintScaleX/Y/Z
     - number
     - computed
     - Requested constraint channels; parentConstraint also exposes constraintRotateX/Y/Z.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/scaleConstraint.json>`.

.. literalinclude:: ../../../examples/graph/scaleConstraint.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/scaleConstraint.json --output json

Expected ``result``: **1**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

The runtime does not discover a Maya DAG. Export all space/basis data. Multi-target rotation, zero total weights, nonpositive scales, and nondefault interpolation need explicit parity tests.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
