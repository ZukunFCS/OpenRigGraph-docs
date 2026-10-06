.. _node-inverseMatrix:

inverseMatrix
=============

Invert a supported affine matrix.

**Layer:** portable graph node. **Contract:** Scoped affine inverse.

**Aliases:** ``MatrixInverseNode``.

When to use
-----------

Use for parent/world-space inversion; check singular scales before relying on the result.

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
     - identity
     - Affine matrix to invert.

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

Download :download:`the complete synthetic graph <../../../examples/graph/inverseMatrix.json>`.

.. literalinclude:: ../../../examples/graph/inverseMatrix.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/inverseMatrix.json --output json

Expected ``result``: **1**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

This is an affine transform operation; validate degenerate and non-affine matrices against the intended contract.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
