.. _node-angleBetween:

angleBetween
============

Compute the angle, axis, and Euler rotation between two vectors.

**Layer:** portable graph node. **Contract:** Exact numeric primitive.

**Aliases:** none.

When to use
-----------

Use for directional relationships; handle zero-length vectors before depending on an orientation.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - vector1X/Y/Z; vector2X/Y/Z
     - number endpoints
     - 0
     - Direction vectors.

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
   * - angle; axisX/Y/Z; eulerX/Y/Z
     - number
     - computed
     - Angle and axis, or Euler components.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/angleBetween.json>`.

.. literalinclude:: ../../../examples/graph/angleBetween.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/angleBetween.json --output json

Expected ``result``: **1.5707963267948966**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

This node returns angle/Euler components in radians. Unlike transform/quaternion conversion nodes, it does not read anglesInDegrees.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
