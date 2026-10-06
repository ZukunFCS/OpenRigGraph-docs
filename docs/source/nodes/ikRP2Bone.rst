.. _node-ikRP2Bone:

ikRP2Bone
=========

Solve a scoped rotate-plane two-bone chain.

**Layer:** portable graph node. **Contract:** Scoped rotate-plane IK.

**Aliases:** none.

When to use
-----------

Use only when the source chain matches this solver contract; preserve lengths, pole direction, joint basis, and source solver settings.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - parentWorldMatrix / handleWorldMatrix
     - matrix endpoints
     - identity
     - Parent and goal world-space matrices.
   * - poleWorldPosition; startTranslate; midTranslate; effectorTranslate
     - number[3] or channel endpoints
     - pole=[0,1,0]; chain along X
     - Chain geometry in the declared spaces.
   * - startScale / midScale; startBaseRotate / midBaseRotate
     - number[3] or channel endpoints
     - unit scale / zero rotation
     - Scale and FK baseline for two-bone solving.
   * - ikBlend / twist
     - number endpoints
     - 1 / 0
     - IK blend and twist.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - startAimVector / startUpVector; midAimVector / midUpVector
     - number[3]
     - X aim / Y up
     - Static segment basis for two-bone solving.
   * - startJointOrient / midJointOrient; startRotateAxis / midRotateAxis
     - number[3]
     - zero
     - Static joint-basis terms.
   * - startRotateOrder / midRotateOrder
     - integer enum
     - 0
     - Maya rotate-order code 0..5.
   * - anglesInDegrees
     - boolean
     - true
     - Euler and twist channel unit.
   * - nativeRadiusMode
     - integer enum
     - 0
     - 0 standard radius; 1 native effective-radius path.
   * - nativeSolverTolerance
     - number endpoint
     - 1e-5
     - Tolerance for the native-radius path.
   * - midPreferredRotate
     - number[3] or channel endpoints
     - zero
     - Preferred middle rotation for the native-radius path.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - startRotateX/Y/Z; midRotateX/Y/Z
     - number
     - computed
     - Local Euler rotation channels.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/ikRP2Bone.json>`.

.. literalinclude:: ../../../examples/graph/ikRP2Bone.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/ikRP2Bone.json --output json

Expected ``result``: **0**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

This is not support for every Maya IK solver or arbitrary chain topology. Test reach limits, pole singularities, IK/FK blends, scales, and rotation wrap.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
