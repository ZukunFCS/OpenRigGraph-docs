.. _node-ikRP:

ikRP
====

Solve a scoped rotate-plane orientation boundary.

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
     - Parent and goal matrices.
   * - poleVectorX/Y/Z
     - number endpoints
     - [0,1,0]
     - Pole-vector direction.
   * - baseRotateX/Y/Z (aliases rotateX/Y/Z)
     - number endpoints
     - 0
     - Baseline Euler rotation.
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
   * - aimVector / upVector
     - number[3]
     - [1,0,0] / [0,1,0]
     - Static aim/up basis.
   * - translate / jointOrient / rotateAxis
     - number[3]
     - 0
     - Static translation and rotation-basis terms.
   * - rotateOrder
     - integer enum
     - 0
     - Maya rotate-order code 0..5.
   * - anglesInDegrees
     - boolean
     - true
     - Euler and twist units.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - rotateX/Y/Z
     - number
     - computed
     - Local Euler rotation channels.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/ikRP.json>`.

.. literalinclude:: ../../../examples/graph/ikRP.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/ikRP.json --output json

Expected ``result``: **0**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

This is not support for every Maya IK solver or arbitrary chain topology. Test reach limits, pole singularities, IK/FK blends, scales, and rotation wrap.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
