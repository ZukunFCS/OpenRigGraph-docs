.. _node-clamp:

clamp
=====

Restrict each channel to a minimum and maximum.

**Layer:** portable graph node. **Contract:** Exact numeric primitive.

**Aliases:** none.

When to use
-----------

Use when the source graph actually clamps a value; preserve signed values otherwise.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - inputR/G/B (aliases inputX/Y/Z)
     - number endpoints
     - 0
     - Channels to clamp.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - minR/G/B; maxR/G/B (or min/max vectors)
     - numbers
     - 0 / 1
     - Per-component bounds; connected bounds are supported.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - outputR / outputG / outputB
     - number
     - computed
     - Clamped channels.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/clamp.json>`.

.. literalinclude:: ../../../examples/graph/clamp.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/clamp.json --output json

Expected ``result``: **1**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
