.. _node-quatSlerp:

quatSlerp
=========

Interpolate between two quaternion orientations.

**Layer:** portable graph node. **Contract:** Exact numeric primitive.

**Aliases:** none.

When to use
-----------

Use at an orientation representation boundary; keep XYZW component order and multiplication direction explicit.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - input1QuatX/Y/Z/W; input2QuatX/Y/Z/W
     - number endpoints
     - identity / identity
     - Start and end orientations.
   * - inputT
     - number endpoint
     - 0
     - Interpolation coordinate.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - anglesInDegrees
     - boolean
     - true
     - Set false for radian-valued Euler/angle channels.
   * - rotateOrder
     - string
     - xyz
     - xyz, yzx, zxy, xzy, yxz, or zyx; check node-specific integer order fields.
   * - exactSlerp
     - boolean
     - false
     - Request exact spherical interpolation instead of the default evaluated path.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - outputQuatX/Y/Z/W
     - number
     - computed
     - Euler or quaternion components.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/quatSlerp.json>`.

.. literalinclude:: ../../../examples/graph/quatSlerp.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/quatSlerp.json --output json

Expected ``result``: **1**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Quaternion sign and Euler wrap can differ while describing the same orientation. Compare transformed bases or angular distance, not only raw component subtraction.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
