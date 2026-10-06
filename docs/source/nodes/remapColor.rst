.. _node-remapColor:

remapColor
==========

Remap each color component through its own scalar ramp.

**Layer:** portable graph node. **Contract:** Exact numeric primitive.

**Aliases:** none.

When to use
-----------

Use when shared ramp positions have different R, G, and B responses; these are numeric lanes, not color management.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - colorR/G/B (aliases inputR/G/B)
     - number endpoints
     - 0
     - Per-channel input.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - color
     - ramp record array
     - required, at least 2 entries
     - Each entry has position and color=[R,G,B] (aliases value/rgb).
   * - inputMin / inputMax; outputMin / outputMax
     - numbers; output ranges may be number[3]
     - 0 / 1; 0 / 1
     - Remapping ranges.
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
   * - outColorR/G/B
     - number
     - computed
     - Remapped components.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/remapColor.json>`.

.. literalinclude:: ../../../examples/graph/remapColor.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/remapColor.json --output json

Expected ``result``: **0.25**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
