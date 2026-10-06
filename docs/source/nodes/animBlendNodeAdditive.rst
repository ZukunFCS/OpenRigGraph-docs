.. _node-animBlendNodeAdditive:

animBlendNodeAdditive
=====================

Evaluate the scalar two-input animation blend boundary.

**Layer:** portable graph node. **Contract:** Scoped animation blend.

**Aliases:** none.

When to use
-----------

Use for this additive numeric animation-layer operation, not for arbitrary Maya animation layer reconstruction.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - inputA / inputB (aliases input[0]/input[1])
     - number endpoints
     - 0
     - Layer contributions.
   * - weightA / weightB (aliases weight[0]/weight[1])
     - number endpoints
     - 1
     - Contribution weights.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - weights
     - number[2]
     - [1,1]
     - Static weight defaults.
   * - interpolateMode
     - integer
     - 0
     - Captured blend interpolation mode; verify non-default modes against the source.

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

Download :download:`the complete synthetic graph <../../../examples/graph/animBlendNodeAdditive.json>`.

.. literalinclude:: ../../../examples/graph/animBlendNodeAdditive.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/animBlendNodeAdditive.json --output json

Expected ``result``: **2**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
