.. _node-pairBlend:

pairBlend
=========

Blend translation and rotation channels, with scoped quaternion rotation interpolation.

**Layer:** portable graph node. **Contract:** Scoped transform blend.

**Aliases:** none.

When to use
-----------

Use for captured two-source transform blending; use matrix constraints for target-space conversion.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - inTranslate1X/Y/Z; inTranslate2X/Y/Z
     - number endpoints
     - 0
     - Translation sources.
   * - inRotate1X/Y/Z; inRotate2X/Y/Z
     - number endpoints
     - 0
     - Euler rotation sources.
   * - weight
     - number endpoint
     - 0
     - Weight from source 1 toward source 2.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - translateXMode/YMode/ZMode; rotateMode
     - static integer enums
     - 0
     - 0 blend, 1 source 1, 2 source 2.
   * - rotInterpolation
     - static integer enum
     - 0
     - 0 Euler, 1 quaternion.
   * - roundWeight; exactSlerp
     - booleans
     - false
     - Optional rounding and exact spherical interpolation controls.
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
   * - outTranslateX/Y/Z; outRotateX/Y/Z
     - number
     - computed
     - Requested transform component.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/pairBlend.json>`.

.. literalinclude:: ../../../examples/graph/pairBlend.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/pairBlend.json --output json

Expected ``result``: **1**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Selection modes, interpolation mode, and rotate order must be static. Unsupported dynamic mode connections fail compilation.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
