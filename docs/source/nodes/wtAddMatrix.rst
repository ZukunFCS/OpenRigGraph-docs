.. _node-wtAddMatrix:

wtAddMatrix
===========

Sum matrix elements multiplied by their weights.

**Layer:** portable graph node. **Contract:** Exact numeric primitive.

**Aliases:** ``MatrixWeightedAddNode``, ``addMatrix``.

When to use
-----------

Use for weighted matrix arithmetic; element-wise addition is not quaternion orientation blending.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - wtMatrix[i].matrixIn / wtMatrix[i].weightIn
     - matrix / number endpoints
     - identity / 1
     - Indexed matrices and weights; matrixIn[i]/weight[i] aliases are accepted.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - matrices / weights
     - matrix[] / number[]
     - identity / 1
     - Static defaults.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - matrixSum[i] (alias outputMatrix[i])
     - number; i=0..15
     - computed
     - Weighted element sum.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/wtAddMatrix.json>`.

.. literalinclude:: ../../../examples/graph/wtAddMatrix.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/wtAddMatrix.json --output json

Expected ``result``: **0.5**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
