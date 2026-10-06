.. _node-ScalarMathNode:

ScalarMathNode
==============

Apply a source-neutral scalar math operation.

**Layer:** portable graph node. **Contract:** Exact numeric primitive.

**Aliases:** ``MathNode``.

When to use
-----------

Use when a formula has a direct numeric expression rather than a Maya-specific node contract.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - input (aliases in/x/a/value)
     - number endpoint or parameter
     - 0
     - Unary operand.
   * - a / b
     - number endpoints or parameters
     - 0; b=1 for multiply/divide/power
     - Binary operands; input1/input2 and indexed aliases are supported.
   * - min / max; t
     - number endpoints or parameters
     - 0 / 1; 0
     - Clamp bounds or lerp weight, as required by op.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - op (alias operation)
     - string enum
     - identity
     - identity, negate, abs, add, subtract, multiply, divide, min, max, power, clamp, saturate, lerp, one_minus, sqrt, tan, acos, atan2.

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

Download :download:`the complete synthetic graph <../../../examples/graph/ScalarMathNode.json>`.

.. literalinclude:: ../../../examples/graph/ScalarMathNode.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/ScalarMathNode.json --output json

Expected ``result``: **5**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Trigonometric operations use radians. Guard invalid numeric domains in the source graph; validate divide-by-zero and power edge cases explicitly.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
