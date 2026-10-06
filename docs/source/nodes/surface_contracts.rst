Surface attachment and cage records
===================================

meshSurfaceFrames attachments
-----------------------------

Every attachment declares faceIndex and coordinate=[u,v]. Preserve vertex,
face-vertex UV, and attachment ordering. Optional capture records select an
explicit policy; they do not discover source semantics at runtime.

.. list-table::
   :header-rows: 1

   * - Fields
     - Type / constraint
     - Meaning
   * - normalAxis / tangentAxis
     - integer; defaults 0 / 2
     - Frame axis assignment.
   * - positionVertexIndices / positionWeights
     - integer[] / matching number[]
     - Explicit position support.
   * - triangleVertexIndices / barycentricWeights
     - integer[3] / number[3]
     - Triangle interpolation.
   * - frameVertexIndices / normalWeights
     - integer[] / matching number[]
     - Normal interpolation support.
   * - tangentWeights / tangentPositionWeights
     - number[] matching support
     - Tangent interpolation; position weights select the position-based path.
   * - normalVertexIndices / normalMatrixWeights
     - 1..32 integer indices / 9 numbers per vertex
     - Explicit affine normal support.
   * - tangentVertexIndices / tangentMatrixWeights / tangentAnchorVertex
     - 1..32 indices / 9 numbers per vertex / integer
     - Explicit affine tangent support and anchor.
   * - tangentMode
     - string
     - Empty default, firstTriangle, firstTriangleFixed13, firstTriangleFixed02,
       firstTriangleFixed023, or firstTriangleFixed123.
   * - vertexNormalMode
     - string
     - Empty default, simple, or simpleLocal.
   * - tangentSign / positionFloat32
     - number / boolean; defaults 1 / false
     - Orientation sign and reduced-precision position policy.

Verify nondefault frame policies independently. Do not adjust them solely to
reduce final error without proving the upstream intended contract.

weightedVertexCage centers
--------------------------

Each record has centerFaceVertex (integer), normalOppositePairs (two integer
vertex pairs), tangentEdgeNeighbor (integer), weightsByCageVertex (one finite
nonnegative weight per cage output), and restLocalCageOffsets (one finite XYZ
offset per output). References belong to faceVertexIndices. Weights across
centers sum to one for each output point. Verify frame orientation and geometry
on independent synthetic input; rest offsets cannot hide missing dependencies.
