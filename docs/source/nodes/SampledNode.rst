.. _node-SampledNode:

SampledNode
===========

Represent behavior with explicit sampled tables and a declared interpolation policy.

**Layer:** portable graph node. **Contract:** Validated sampled contract.

**Aliases:** none.

When to use
-----------

Use when the sample-domain contract is intentional and quantified; it is not equivalent to reconstructing an arbitrary solver.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - x / y; or names in input_order
     - number endpoints
     - 0 / declared endpoints
     - Table coordinates or nearest-center dimensions.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - interpolation
     - string enum
     - linear1d
     - linear1d (aliases linear/piecewise_linear), bilinear2d (alias bilinear), nearest (aliases nearestnd/nearest_nd/exact_centers).
   * - x / values
     - matching number[]
     - required for linear1d
     - Ordered input axis and scalar samples.
   * - x_axis / y_axis; grid (or flattened values)
     - number[]; number[][] or number[]
     - required for bilinear2d
     - Axes each contain at least 2 values; grid shape matches axis lengths.
   * - input_order / centers / outputs
     - string[] / number[][] / output records
     - required for nearest path
     - Nearest-center inputs and one output value per center.
   * - bias
     - number
     - 0
     - Optional output bias in the nearest-center path.
   * - provenance
     - object
     - exporter requirement
     - Sampling coverage, input domain, and independent verification evidence.

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

Download :download:`the complete synthetic graph <../../../examples/graph/SampledNode.json>`.

.. literalinclude:: ../../../examples/graph/SampledNode.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/SampledNode.json --output json

Expected ``result``: **0.5**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Grid paths clamp at the sampled domain edge; nearest-center evaluation can be discontinuous. Test interiors, boundaries, and unseen combinations.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
