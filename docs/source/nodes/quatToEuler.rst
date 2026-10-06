.. _node-quatToEuler:

quatToEuler
===========

Convert an XYZW quaternion into ordered Euler rotation.

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
   * - inputQuatX/Y/Z/W
     - number endpoints
     - [0,0,0,1]
     - Quaternion components.

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

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - outputRotateX/Y/Z
     - number
     - computed
     - Euler or quaternion components.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/quatToEuler.json>`.

.. literalinclude:: ../../../examples/graph/quatToEuler.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/quatToEuler.json --output json

Expected ``result``: **0**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Quaternion sign and Euler wrap can differ while describing the same orientation. Compare transformed bases or angular distance, not only raw component subtraction.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
