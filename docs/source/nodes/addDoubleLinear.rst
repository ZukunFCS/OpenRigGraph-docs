.. _node-addDoubleLinear:

addDoubleLinear
===============

Add two scalar values: input1 + input2.

**Layer:** portable graph node. **Contract:** Exact numeric primitive.

**Aliases:** ``addDL``.

When to use
-----------

Use for a two-value numeric sum, including a constant offset.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - input1 / input2
     - number endpoints
     - 0 / 0
     - Operands; static input1/input2 parameters are also accepted.

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

Download :download:`the complete synthetic graph <../../../examples/graph/addDoubleLinear.json>`.

.. literalinclude:: ../../../examples/graph/addDoubleLinear.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/addDoubleLinear.json --output json

Expected ``result``: **3**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.

Related: :ref:`plusMinusAverage <node-plusMinusAverage>`, :ref:`ScalarMathNode <node-ScalarMathNode>`.
