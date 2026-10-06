.. _node-distanceBetween:

distanceBetween
===============

Measure the Euclidean distance between two transformed points.

**Layer:** portable graph node. **Contract:** Exact numeric primitive.

**Aliases:** none.

When to use
-----------

Use for distance-driven controls; both points must be interpreted in the intended common space.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - point1X/Y/Z; point2X/Y/Z
     - number endpoints
     - 0
     - Point coordinates.
   * - inMatrix1 / inMatrix2
     - matrix endpoints
     - identity
     - Optional transforms into the comparison space.

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
   * - distance
     - number
     - computed
     - Distance in the declared length units.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/distanceBetween.json>`.

.. literalinclude:: ../../../examples/graph/distanceBetween.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/distanceBetween.json --output json

Expected ``result``: **5**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
