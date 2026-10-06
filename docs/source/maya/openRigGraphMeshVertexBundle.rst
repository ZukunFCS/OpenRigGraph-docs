openRigGraphMeshVertexBundle
============================

Extract indexed mesh point data as a packed numeric array.

**Layer:** Maya integration node. **Type identifier:** ``openRigGraphMeshVertexBundle``.

When to use
-----------

Use to feed reusable geometry evaluation with a declared support vertex set.

Attributes
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - inputValues
     - double[]
     - empty
     - input / configuration; Node input values; see the wiring and package contract below. Short name: ``iv``.
   * - inputMesh
     - mesh
     - MObject::kNullObj
     - input / configuration; Node input mesh; see the wiring and package contract below. Short name: ``im``.
   * - worldMatrix
     - matrix4x4 (double)
     - identity
     - input / configuration; Node world matrix; see the wiring and package contract below. Short name: ``wm``.
   * - baseIndex
     - integer
     - 0
     - input / configuration; Declared base index; indices address the packed input/package layout. Short name: ``bi``.
   * - vertexIndices
     - integer[]
     - empty
     - input / configuration; Declared vertex indices; indices address the packed input/package layout. Short name: ``vi``.
   * - outputValues
     - double[]
     - computed
     - output; Computed output values; see the wiring and package contract below. Short name: ``ov``.

Wiring and resource contract
----------------------------

Keep topology and vertex identifiers stable. Coordinate space follows the declared mesh/matrix input boundary.

See :doc:`shared integration contracts <contracts>` for packed indices, typed units, reloads, package schemas, and safe reconnection.

Usage
-----

.. code-block:: python

   import maya.cmds as cmds
   node = cmds.createNode("openRigGraphMeshVertexBundle", name="exampleMeshVertexBundle")

This creates the DG interface; it does not prepare a graph, cache, or geometry package. Configure the listed inputs before requesting its outputs.

Download the :download:`synthetic Maya interface checks <../../../examples/maya/check_interfaces.py>` and the :doc:`complete porting tutorial <../porting/tutorial>`.

Validation
----------

Check actual attribute types and logical indices, then compare the connected output across changing inputs and fractional times. Node creation alone is not deformation parity. Reject stale/missing resources and layouts that do not match the package.
