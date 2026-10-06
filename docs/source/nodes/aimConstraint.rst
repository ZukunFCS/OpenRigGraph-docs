.. _node-aimConstraint:

aimConstraint
=============

Aim a constrained orientation toward an ordered, weighted target set.

**Layer:** portable graph node. **Contract:** Scoped aim constraint.

**Aliases:** none.

When to use
-----------

Use for supported aim/up/world-up behavior with known parent basis and offsets.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - constraintTranslateX/Y/Z; constraintParentInverseMatrix
     - number / matrix endpoints
     - 0 / identity
     - Constrained origin and parent-space basis.
   * - target[i].targetTranslateX/Y/Z; target[i].targetParentMatrix; target[i].targetWeight
     - number / matrix endpoints
     - target defaults
     - World target reconstruction and weights.
   * - worldUpVectorX/Y/Z; worldUpMatrix
     - number / matrix endpoints
     - [0,1,0] / identity
     - Up-direction data.

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
     - Target translation, matrix, and weight data.
   * - aimVector / upVector; offset / jointOrient
     - number[3]
     - [0,0,1] / [0,1,0]; zero offsets
     - Captured aim basis and rotation adjustments.
   * - worldUpType
     - static integer enum
     - 4
     - Captured Maya world-up mode; validate the selected mode and basis.
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
     - Euler constrained orientation.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/aimConstraint.json>`.

.. literalinclude:: ../../../examples/graph/aimConstraint.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/aimConstraint.json --output json

Expected ``result``: **0**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
