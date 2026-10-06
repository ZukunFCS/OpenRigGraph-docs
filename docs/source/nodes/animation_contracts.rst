Animation curve contracts
=========================

Simple keys
-----------

Supply ordered keys with input/value (aliases time/x and output/y), or matching
x/values arrays. Interpolation is linear, step/constant, or smooth/smoothstep.
This simplified response curve does not reconstruct all Maya tangent modes.

Native tangents
---------------

nativeCurve.keys is a nonempty ordered array with finite input/value and native
incoming/outgoing tangent vectors ``in_xy`` and ``out_xy`` (two numbers each).
``out_type`` defaults to 2; preserve the source-exported tangent type code.
``nativeCurve.weighted`` defaults false and selects weighted tangent evaluation.
Inputs are strictly increasing; a single numeric value key is a constant.
Preserve exporter version and numeric units;
the native representation is evaluated separately from simple interpolation.
Use the SDK curve exporter and maya_curve.evaluate_native_curve for a matching
reference representation. See :doc:`../reference/python/maya_curve`.

Infinity and verification
-------------------------

preInfinity/postInfinity accept 0 (constant) or 3 (cycle); other modes fail
compilation. Test both ends, endpoints, fractional coordinates, tangent
transitions, and repeated cycles. Frame-only playback does not establish
fractional-time equivalence.
