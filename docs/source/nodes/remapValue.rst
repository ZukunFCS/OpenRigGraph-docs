.. _node-remapValue:

remapValue
==========

Normalize and clamp an input, evaluate a ramp, then map into an output range.

**Layer:** portable graph node. **Contract:** Exact numeric primitive.

**Aliases:** none.

When to use
-----------

Use for an authored scalar ramp with explicit input and output ranges.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - inputValue
     - number endpoint
     - 0
     - Input to normalize.
   * - inputMin / inputMax; outputMin / outputMax
     - number endpoints
     - 0 / 1; 0 / 1
     - Connected range boundaries are supported.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - positions / values
     - matching number[]
     - required, at least 2 entries
     - Ramp knots and scalar values; ramp/value record arrays are also accepted.
   * - interpolation
     - string enum
     - linear
     - linear, step/constant, smooth/smoothstep.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - outValue
     - number
     - computed
     - Remapped ramp result.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/remapValue.json>`.

.. literalinclude:: ../../../examples/graph/remapValue.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/remapValue.json --output json

Expected ``result``: **0.5**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
