.. _node-animCurveTL:

animCurveTL
===========

Evaluate an authored scalar key curve (time to length).

**Layer:** portable graph node. **Contract:** Scoped authored curve.

**Aliases:** none.

When to use
-----------

Use for set-driven responses or keyed time evaluation. Preserve source units explicitly; the type name alone does not convert numeric values.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - input (alias time)
     - number endpoint
     - 0
     - Curve coordinate, in the exported curve's numeric units.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - keys or x/values
     - key records or matching number[]
     - required unless nativeCurve is supplied
     - Keys contain input/value; coordinates must be ordered.
   * - interpolation (alias tangent)
     - string enum
     - linear
     - linear, step/constant, smooth/smoothstep.
   * - preInfinity / postInfinity
     - integer enum
     - 0
     - 0 constant; 3 cycle. Other infinity modes are rejected.
   * - nativeCurve
     - object
     - absent
     - Native tangent representation; see animation contracts for key fields and units.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - output
     - number
     - computed
     - Scalar result.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/animCurveTL.json>`.

.. literalinclude:: ../../../examples/graph/animCurveTL.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/animCurveTL.json --output json

Expected ``result``: **0.5**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Default infinity is constant; cycle must be requested. Test fractional coordinates and both ends. Native tangent evaluation is distinct from the simplified linear/step/smooth representation.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.

Related: :ref:`remapValue <node-remapValue>`, :ref:`SampledNode <node-SampledNode>`.

See :doc:`animation contracts <animation_contracts>`.
