.. _node-quatProd:

quatProd
========

Multiply quaternions to compose rotations.

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
     - Ordered quaternion operands.

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
   * - outputQuatX/Y/Z/W
     - number
     - computed
     - Euler or quaternion components.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/quatProd.json>`.

.. literalinclude:: ../../../examples/graph/quatProd.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/quatProd.json --output json

Expected ``result``: **1**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Quaternion sign and Euler wrap can differ while describing the same orientation. Compare transformed bases or angular distance, not only raw component subtraction.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
