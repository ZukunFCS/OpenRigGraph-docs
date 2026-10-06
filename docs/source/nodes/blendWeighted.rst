.. _node-blendWeighted:

blendWeighted
=============

Sum input[i] * weight[i] without normalizing weights.

**Layer:** portable graph node. **Contract:** Exact numeric primitive.

**Aliases:** none.

When to use
-----------

Use for weighted scalar accumulation; it does not automatically produce a convex blend.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - input[i] / weight[i]
     - indexed number endpoints
     - 0 / 1
     - Inputs and corresponding weights.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - weights
     - number[]
     - 1 for omitted entries
     - Optional static weight defaults indexed by logical slot.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - output
     - number
     - computed
     - Scalar result.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/blendWeighted.json>`.

.. literalinclude:: ../../../examples/graph/blendWeighted.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/blendWeighted.json --output json

Expected ``result``: **0.5**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
