.. _node-composeMatrix:

composeMatrix
=============

Compose a row-vector affine matrix from transform channels.

**Layer:** portable graph node. **Contract:** Scoped affine/joint transform.

**Aliases:** ``MatrixComposeNode``.

When to use
-----------

Use for live transform expressions, including supported joint-orientation and scale-compensation terms.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - inputTranslateX/Y/Z; inputRotateX/Y/Z; inputScaleX/Y/Z; inputShearX/Y/Z
     - number endpoints
     - 0; scale=1
     - Transform components; matching vector parameters supply defaults.
   * - jointOrientX/Y/Z; rotateAxisX/Y/Z; inverseScaleX/Y/Z
     - number endpoints
     - 0; inverseScale=1
     - Joint and rotation-basis terms.

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
   * - segmentScaleCompensate
     - boolean
     - false
     - Enable supported inverse-scale compensation.
   * - inputRotateDoublePrecision; jointOrientDoublePrecision
     - booleans
     - false
     - Preserve double-precision parameter paths where implemented.
   * - scaleEpsilon
     - number
     - 0
     - Scale handling epsilon.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - outputMatrix[i]
     - number; i=0..15
     - computed
     - Row-major matrix element; a whole outputMatrix endpoint is accepted by matrix consumers.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/composeMatrix.json>`.

.. literalinclude:: ../../../examples/graph/composeMatrix.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/composeMatrix.json --output json

Expected ``result``: **2**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Matrices use row vectors and translation elements 12..14. Joint orientation, rotate axis, shear, and inherited scale are separate terms; do not replace them with a neutral snapshot.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.

Related: :ref:`decomposeMatrix <node-decomposeMatrix>`, :ref:`multMatrix <node-multMatrix>`.
