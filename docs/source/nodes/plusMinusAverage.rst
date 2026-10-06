.. _node-plusMinusAverage:

plusMinusAverage
================

Reduce an indexed array by pass-through, sum, subtraction, or average.

**Layer:** portable graph node. **Contract:** Exact numeric primitive.

**Aliases:** none.

When to use
-----------

Use for multi-input arithmetic; retain source logical indices, especially for subtraction.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - input1D[i]; input2D[i].input2Dx/y; input3D[i].input3Dx/y/z
     - indexed number endpoints
     - 0
     - Sparse logical array entries, grouped by dimensionality.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - operation
     - integer enum
     - 1
     - 0 first input; 1 sum; 2 first minus remaining; 3 average.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - output1D; output2Dx/y; output3Dx/y/z
     - number
     - computed
     - Requested dimensional component.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/plusMinusAverage.json>`.

.. literalinclude:: ../../../examples/graph/plusMinusAverage.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/plusMinusAverage.json --output json

Expected ``result``: **6**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
