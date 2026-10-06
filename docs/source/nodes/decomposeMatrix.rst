.. _node-decomposeMatrix:

decomposeMatrix
===============

Extract translation, scale, shear, Euler rotation, and quaternion components from an affine matrix.

**Layer:** portable graph node. **Contract:** Scoped affine decomposition.

**Aliases:** none.

When to use
-----------

Use at a matrix-to-channel boundary; choose the source rotate order and compare orientation across wrap boundaries.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - inputMatrix (alias matrix)
     - matrix endpoint
     - required for computed decomposition
     - Affine matrix to decompose.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - anglesInDegrees
     - boolean
     - true
     - Set false for radian-valued Euler/angle channels.
   * - rotateOrder
     - string
     - xyz
     - xyz, yzx, zxy, xzy, yxz, or zyx; check node-specific integer order fields.
   * - translate/translation/outputTranslate; scale/outputScale; shear/outputShear
     - number[3]
     - absent
     - Explicit exported component overrides take precedence.
   * - rotate/rotation/outputRotate; quaternion/quat/outputQuat
     - number[3] / number[4]
     - absent
     - Explicit orientation overrides.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - outputTranslateX/Y/Z; outputScaleX/Y/Z; outputShearX/Y/Z
     - number
     - computed
     - Affine components.
   * - outputRotateX/Y/Z; outputQuatX/Y/Z/W
     - number
     - computed
     - Euler and XYZW quaternion outputs.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/decomposeMatrix.json>`.

.. literalinclude:: ../../../examples/graph/decomposeMatrix.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/decomposeMatrix.json --output json

Expected ``result``: **0**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Rotation is evaluated from connected matrices in the current runtime; it is not restricted to baked rotation outputs.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
