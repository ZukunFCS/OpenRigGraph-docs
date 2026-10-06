.. _node-multiplyDivide:

multiplyDivide
==============

Component-wise pass-through, multiply, divide, or power.

**Layer:** portable graph node. **Contract:** Exact numeric primitive.

**Aliases:** none.

When to use
-----------

Use for independent XYZ arithmetic; this is not a vector dot or cross product.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - input1X/Y/Z; input2X/Y/Z
     - number endpoints
     - input1: 0; input2: 1
     - Component operands.

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
     - 0 pass input1; 1 multiply; 2 divide; 3 power.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - outputX / outputY / outputZ
     - number
     - computed
     - Independent component results.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/multiplyDivide.json>`.

.. literalinclude:: ../../../examples/graph/multiplyDivide.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/multiplyDivide.json --output json

Expected ``result``: **3**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
