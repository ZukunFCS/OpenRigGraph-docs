.. _node-condition:

condition
=========

Compare two scalars and select true or false component values.

**Layer:** portable graph node. **Contract:** Exact numeric primitive.

**Aliases:** none.

When to use
-----------

Use for numeric branch selection; preserve the comparison operation and threshold.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - firstTerm / secondTerm
     - number endpoints
     - 0
     - Comparison operands.
   * - colorIfTrueR/G/B; colorIfFalseR/G/B
     - number endpoints
     - true: 1; false: 0
     - Branch values.

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
     - 0
     - 0 equal; 1 not equal; 2 greater; 3 greater-or-equal; 4 less; 5 less-or-equal.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - outColorR / outColorG / outColorB
     - number
     - computed
     - Selected components.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/condition.json>`.

.. literalinclude:: ../../../examples/graph/condition.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/condition.json --output json

Expected ``result``: **7**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
