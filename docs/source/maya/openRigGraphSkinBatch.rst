openRigGraphSkinBatch
=====================

Evaluate packaged skinning into packed point arrays.

**Layer:** Maya integration node. **Type identifier:** ``openRigGraphSkinBatch``.

When to use
-----------

Use for a declared influence/weight/bind layout, including optional pre-skin point input.

Attributes
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - packagePath
     - string
     - empty
     - input / configuration; Path to the node's explicitly prepared geometry package. Short name: ``pp``.
   * - reloadToken
     - integer
     - 0
     - input / configuration; Increment after replacing a resource at the same path to force reload. Short name: ``rt``.
   * - expectedPackedValueCount
     - integer
     - 0
     - input / configuration; Declared expected packed value count; must match the corresponding packed layout. Short name: ``epvc``.
   * - packedMatrices
     - double[]
     - empty
     - input / configuration; Node packed matrices; see the wiring and package contract below. Short name: ``pm``.
   * - packedPoints
     - double[]
     - empty
     - input / configuration; Node packed points; see the wiring and package contract below. Short name: ``ppoints``.
   * - inputGeometry
     - mesh logical array
     - MObject::kNullObj
     - input / configuration; Node input geometry; see the wiring and package contract below. Short name: ``ig``.
   * - geometryMatrix
     - matrix4x4 (double) logical array
     - identity
     - input / configuration; Node geometry matrix; see the wiring and package contract below. Short name: ``gm``.
   * - outputGeometry
     - mesh logical array
     - computed
     - output; Computed output geometry; see the wiring and package contract below. Short name: ``og``.

Wiring and resource contract
----------------------------

Verify influence order, bind matrix convention, point ranges, and pre-skin ownership before wiring.

See :doc:`shared integration contracts <contracts>` for packed indices, typed units, reloads, package schemas, and safe reconnection.

Usage
-----

.. code-block:: python

   import maya.cmds as cmds
   node = cmds.createNode("openRigGraphSkinBatch", name="exampleSkinBatch")

This creates the DG interface; it does not prepare a graph, cache, or geometry package. Configure the listed inputs before requesting its outputs.

Download the :download:`synthetic Maya interface checks <../../../examples/maya/check_interfaces.py>` and the :doc:`complete porting tutorial <../porting/tutorial>`.

Validation
----------

Check actual attribute types and logical indices, then compare the connected output across changing inputs and fractional times. Node creation alone is not deformation parity. Reject stale/missing resources and layouts that do not match the package.
