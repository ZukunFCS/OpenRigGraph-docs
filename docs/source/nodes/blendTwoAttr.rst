.. _node-blendTwoAttr:

blendTwoAttr
============

Interpolate input[0] toward input[1] using attributesBlender.

**Layer:** portable graph node. **Contract:** Exact numeric primitive.

**Aliases:** none.

When to use
-----------

Use for a scalar two-value blend whose weight 0 selects input[0].

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - input[0] / input[1]
     - number endpoints
     - 0
     - Start and end values.
   * - attributesBlender (aliases blender/weight)
     - number endpoint
     - 0
     - Interpolation weight.

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
   * - output
     - number
     - computed
     - Scalar result.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/blendTwoAttr.json>`.

.. literalinclude:: ../../../examples/graph/blendTwoAttr.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/blendTwoAttr.json --output json

Expected ``result``: **1**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
