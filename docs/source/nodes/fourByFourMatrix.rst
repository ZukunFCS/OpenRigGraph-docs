.. _node-fourByFourMatrix:

fourByFourMatrix
================

Assemble a matrix from sixteen scalar elements.

**Layer:** portable graph node. **Contract:** Exact numeric primitive.

**Aliases:** none.

When to use
-----------

Use when the source provides matrix elements directly rather than a TRS expression.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - in00..in33
     - number endpoints
     - identity matrix
     - Row and column addressed elements.

Parameters
----------

No additional fields.

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

Download :download:`the complete synthetic graph <../../../examples/graph/fourByFourMatrix.json>`.

.. literalinclude:: ../../../examples/graph/fourByFourMatrix.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/fourByFourMatrix.json --output json

Expected ``result``: **2**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
