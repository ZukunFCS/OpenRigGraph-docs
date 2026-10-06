.. _node-surfaceFrame:

surfaceFrame
============

Construct an attachment frame from an explicit triangle or supported quad and UV data.

**Layer:** portable graph node. **Contract:** Scoped surface attachment.

**Aliases:** none.

When to use
-----------

Use for a small, explicitly captured surface attachment with live vertex positions.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - position0X/Y/Z .. position3X/Y/Z
     - number endpoints
     - static position vectors
     - Triangle vertices, or four vertices when uv3 is present.
   * - normalN / tangentN components
     - number endpoints
     - 0
     - Optional smooth vertex normal and tangent data.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - uv0 / uv1 / uv2; optional uv3
     - number[2]
     - triangle UV basis
     - UV coordinates; uv3 selects the quad path.
   * - barycentric (alias weights)
     - number[3]
     - [1,0,0]
     - Triangle position weights.
   * - coordinate
     - number[2]
     - [0,0]
     - Quad UV attachment coordinate.
   * - normalAxis / tangentAxis
     - integer enums
     - 0 / 2
     - Output frame axis assignment.
   * - smoothNormalWeights / smoothTangentWeights; smoothTangentSign
     - number[] / number
     - first vertex / 1
     - Optional smooth-frame interpolation.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - outputMatrix[i]
     - number; i=0..15
     - computed
     - Row-major matrix element; a whole outputMatrix endpoint is accepted by matrix consumers.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/surfaceFrame.json>`.

.. literalinclude:: ../../../examples/graph/surfaceFrame.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/surfaceFrame.json --output json

Expected ``result``: **0**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Topology and interpolation choices are explicit capture data. Validate seams, shared edges, normals, and degenerate UV/geometry cases.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.


See :doc:`surface record contracts <surface_contracts>`.
