.. _node-RbfNode:

RbfNode
=======

Evaluate explicit radial basis centers and output coefficient vectors.

**Layer:** portable graph node. **Contract:** Explicit RBF contract.

**Aliases:** none.

When to use
-----------

Use for an RBF with a known kernel and coefficients, or a separately validated fitted response; do not equate training-center agreement with domain accuracy.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - names in input_order
     - named number endpoints
     - required
     - One input endpoint for every declared dimension.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - input_order
     - nonempty string[]
     - required
     - Ordered input dimensions.
   * - centers
     - number[][]
     - required, nonempty
     - Each center dimension matches input_order.
   * - kernel
     - string enum
     - required
     - gaussian, polyharmonic_1, cubic, thin_plate, multiquadric, inverse_quadratic, inverse_multiquadric.
   * - outputs
     - object of coefficient records
     - required
     - Each output has exactly one coefficients array with one value per center.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - declared output names
     - number
     - computed
     - Kernel-weighted response.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/RbfNode.json>`.

.. literalinclude:: ../../../examples/graph/RbfNode.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/RbfNode.json --output json

Expected ``result``: **1**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Coefficients are evaluation coefficients, not automatically solved from target samples. Input scaling and domain selection belong to the exporter.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
