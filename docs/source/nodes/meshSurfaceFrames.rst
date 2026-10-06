.. _node-meshSurfaceFrames:

meshSurfaceFrames
=================

Evaluate multiple surface attachment matrices from a declared mesh topology and UV layout.

**Layer:** portable graph node. **Contract:** Scoped batched surface attachment.

**Aliases:** none.

When to use
-----------

Use for batched attachment evaluation when many outputs share a mesh input and topology.

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
     - Live positions indexed by mesh vertex.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - faces
     - integer[][]
     - required
     - Faces have at least three nonnegative vertex indices.
   * - uvs
     - number[2][]
     - required
     - UV coordinate table.
   * - faceVertexUvIndices; optional positionFaceVertexUvIndices
     - integer[]
     - required / same topology
     - Flattened per-face-vertex UV indices.
   * - attachments
     - attachment-record[]
     - required, nonempty
     - Each record declares faceIndex and coordinate; optional interpolation and frame policies are documented in surface contracts.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - outputMatrixN[i]
     - number; i=0..15
     - computed
     - Matrix element for attachment N.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/meshSurfaceFrames.json>`.

.. literalinclude:: ../../../examples/graph/meshSurfaceFrames.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/meshSurfaceFrames.json --output json

Expected ``result``: **0**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.

Related: :ref:`surfaceFrame <node-surfaceFrame>`.

See :doc:`surface record contracts <surface_contracts>`.
