.. _node-weightedVertexCage:

weightedVertexCage
==================

Evaluate a small cage from weighted local frames built on declared support vertices.

**Layer:** portable graph node. **Contract:** Scoped local-frame cage.

**Aliases:** none.

When to use
-----------

Use for a captured generic local-frame cage relationship whose weights and topology are fixed and validated.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - positionNX/Y/Z
     - number endpoints
     - static positionN vectors
     - Live support vertex positions.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - faceVertexIndices
     - unique nonnegative integer[]
     - required; 1..4096
     - Support vertex identifiers.
   * - cageVertexCount
     - integer
     - required; 1..256
     - Output cage point count.
   * - centers
     - center-record[]
     - required; 1..1024
     - Frame supports, nonnegative weights, and local rest offsets; see surface contracts.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - outputNX/Y/Z
     - number
     - computed
     - Component of cage vertex N.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/weightedVertexCage.json>`.

.. literalinclude:: ../../../examples/graph/weightedVertexCage.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/weightedVertexCage.json --output json

Expected ``result``: **0**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Weights must sum to one for every output vertex. All referenced vertices must belong to the support set; offsets and weights must be finite.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.


See :doc:`surface record contracts <surface_contracts>`.
