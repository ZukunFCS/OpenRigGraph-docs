.. _node-multDoubleLinear:

multDoubleLinear
================

Multiply two scalar values: input1 * input2.

**Layer:** portable graph node. **Contract:** Exact numeric primitive.

**Aliases:** none.

When to use
-----------

Use for scalar gains and masks; use multiplyDivide for component-wise operations.

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
     - Operands; an omitted second input is zero, not one.

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

Download :download:`the complete synthetic graph <../../../examples/graph/multDoubleLinear.json>`.

.. literalinclude:: ../../../examples/graph/multDoubleLinear.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/multDoubleLinear.json --output json

Expected ``result``: **6**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.

Related: :ref:`multiplyDivide <node-multiplyDivide>`.
