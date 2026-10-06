.. _node-unitConversion:

unitConversion
==============

Multiply a scalar by an explicit unit conversion factor.

**Layer:** portable graph node. **Contract:** Exact numeric primitive.

**Aliases:** none.

When to use
-----------

Use at a documented unit boundary; avoid converting a value twice.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - input (alias inputX)
     - number endpoint
     - 0
     - Value to convert.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - conversionFactor (alias factor)
     - number
     - 1
     - Multiplicative conversion, baked by the exporter.

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

Download :download:`the complete synthetic graph <../../../examples/graph/unitConversion.json>`.

.. literalinclude:: ../../../examples/graph/unitConversion.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/unitConversion.json --output json

Expected ``result``: **0.5**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.

Related: :ref:`multDoubleLinear <node-multDoubleLinear>`.
