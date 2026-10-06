.. _node-multMatrix:

multMatrix
==========

Multiply an ordered array of matrices.

**Layer:** portable graph node. **Contract:** Exact numeric primitive.

**Aliases:** ``MatrixMultiplyNode``.

When to use
-----------

Use for local-to-parent/world matrix chains; preserve source multiplication order and sparse indices.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - matrixIn[i] (or matrixIn[i][element])
     - matrix endpoint or scalar elements
     - identity
     - Matrix inputs indexed in source order.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - matrices
     - array of number[16]
     - required unless indexed matrices are connected
     - Static matrices used when an input is not connected.

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
     - Product matrix elements.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/multMatrix.json>`.

.. literalinclude:: ../../../examples/graph/multMatrix.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/multMatrix.json --output json

Expected ``result``: **1**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
