.. _node-setRange:

setRange
========

Map an old range into a new range with normalized position clamped to [0,1].

**Layer:** portable graph node. **Contract:** Exact numeric primitive.

**Aliases:** none.

When to use
-----------

Use for a bounded linear remap; use an animation curve for an authored nonlinear response.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - valueX / valueY / valueZ
     - number endpoints
     - 0
     - Values in the old range.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - oldMin / oldMax
     - number[3] or channel endpoints
     - 0 / 1
     - Old range boundaries.
   * - min / max
     - number[3] or channel endpoints
     - 0 / 1
     - New range boundaries.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - outValueX/Y/Z (aliases outputX/Y/Z)
     - number
     - computed
     - Remapped component.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/setRange.json>`.

.. literalinclude:: ../../../examples/graph/setRange.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/setRange.json --output json

Expected ``result``: **0.5**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

If oldMin == oldMax, that component passes its input through. Preserve this branch rather than dividing by zero.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
