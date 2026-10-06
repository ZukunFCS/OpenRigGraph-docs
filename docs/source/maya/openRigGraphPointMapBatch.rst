openRigGraphPointMapBatch
=========================

Apply a packaged reusable point mapping to packed geometry.

**Layer:** Maya integration node. **Type identifier:** ``openRigGraphPointMapBatch``.

When to use
-----------

Use for a validated point mapping with stable source and destination layouts.

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
   * - driverGeometry
     - mesh
     - MObject::kNullObj
     - input / configuration; Node driver geometry; see the wiring and package contract below. Short name: ``dg``.
   * - inputGeometry
     - mesh logical array
     - MObject::kNullObj
     - input / configuration; Node input geometry; see the wiring and package contract below. Short name: ``ig``.
   * - inputMatrix
     - matrix4x4 (double) logical array
     - identity
     - input / configuration; Matrix input; preserve declared input-space convention. Short name: ``im``.
   * - inputRadius
     - double logical array
     - 1.0
     - input / configuration; Node input radius; see the wiring and package contract below. Short name: ``ir``.
   * - outputGeometry
     - mesh logical array
     - computed
     - output; Computed output geometry; see the wiring and package contract below. Short name: ``og``.

Wiring and resource contract
----------------------------

The package declares the mapping; this node does not discover a correspondence automatically.

See :doc:`shared integration contracts <contracts>` for packed indices, typed units, reloads, package schemas, and safe reconnection.

Usage
-----

.. code-block:: python

   import maya.cmds as cmds
   node = cmds.createNode("openRigGraphPointMapBatch", name="examplePointMapBatch")

This creates the DG interface; it does not prepare a graph, cache, or geometry package. Configure the listed inputs before requesting its outputs.

Download the :download:`synthetic Maya interface checks <../../../examples/maya/check_interfaces.py>` and the :doc:`complete porting tutorial <../porting/tutorial>`.

Validation
----------

Check actual attribute types and logical indices, then compare the connected output across changing inputs and fractional times. Node creation alone is not deformation parity. Reject stale/missing resources and layouts that do not match the package.
