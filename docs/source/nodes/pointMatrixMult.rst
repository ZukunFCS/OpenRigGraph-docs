.. _node-pointMatrixMult:

pointMatrixMult
===============

Transform a point or vector by an affine matrix.

**Layer:** portable graph node. **Contract:** Exact numeric primitive.

**Aliases:** none.

When to use
-----------

Use at a declared space boundary; vectorMultiply excludes translation.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - inPointX/Y/Z
     - number endpoints
     - 0
     - Point/vector components.
   * - inMatrix
     - matrix endpoint
     - identity
     - Row-vector transform.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - vectorMultiply
     - boolean
     - false
     - False transforms a point; true transforms a direction.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - outputX/Y/Z
     - number
     - computed
     - Transformed components.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/pointMatrixMult.json>`.

.. literalinclude:: ../../../examples/graph/pointMatrixMult.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/pointMatrixMult.json --output json

Expected ``result``: **2**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
