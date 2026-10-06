.. _node-blendColors:

blendColors
===========

Compute color1 * blender + color2 * (1 - blender), component-wise.

**Layer:** portable graph node. **Contract:** Exact numeric primitive.

**Aliases:** none.

When to use
-----------

Use for component blending with Maya blendColors weight direction; it differs from a-to-b lerp.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - color1R/G/B; color2R/G/B
     - number endpoints
     - 0
     - Component values.
   * - blender
     - number endpoint
     - 0
     - Weight of color1; weight 0 selects color2.

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
   * - outputR/G/B
     - number
     - computed
     - Blended components.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/blendColors.json>`.

.. literalinclude:: ../../../examples/graph/blendColors.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/blendColors.json --output json

Expected ``result``: **1**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
