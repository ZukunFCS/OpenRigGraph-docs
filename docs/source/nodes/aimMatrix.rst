.. _node-aimMatrix:

aimMatrix
=========

Orient an input matrix toward a primary target while retaining its translation.

**Layer:** portable graph node. **Contract:** Scoped aim matrix.

**Aliases:** none.

When to use
-----------

Use for a supported matrix-based aim relation, with primary/secondary modes captured explicitly.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - inputMatrix; primaryTargetMatrix; secondaryTargetMatrix
     - matrix endpoints
     - identity
     - Source and target matrices.
   * - secondaryInputAxisX/Y/Z; secondaryTargetVectorX/Y/Z
     - number endpoints
     - captured defaults
     - Secondary orientation inputs.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - primaryMode
     - static integer
     - 1
     - Only mode 1 is supported.
   * - secondaryMode
     - static integer enum
     - 0
     - 0 primary-only; 2 explicit secondary alignment.
   * - primaryInputAxis
     - number[3]
     - [1,0,0]
     - Static nonzero primary input axis.

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

Download :download:`the complete synthetic graph <../../../examples/graph/aimMatrix.json>`.

.. literalinclude:: ../../../examples/graph/aimMatrix.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/aimMatrix.json --output json

Expected ``result``: **0**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Dynamic primary modes/axis are rejected. Zero or coincident targets require a deliberately validated source-domain policy.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
