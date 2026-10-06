openRigGraphFaceGeometryBatch
=============================

Execute an explicitly packaged sequence of supported geometry operations.

**Layer:** Maya integration node. **Type identifier:** ``openRigGraphFaceGeometryBatch``.

When to use
-----------

Use when multiple point/deformation operations can share a declared schedule and buffer layout.

Attributes
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - programPath
     - string
     - empty
     - input / configuration; Node program path; see the wiring and package contract below. Short name: ``pp``.
   * - reloadToken
     - integer
     - 0
     - input / configuration; Increment after replacing a resource at the same path to force reload. Short name: ``rt``.
   * - packedValues
     - double[]
     - empty
     - input / configuration; Packed scalar data with indices defined by the graph/package contract. Short name: ``pv``.
   * - inputGeometry
     - mesh logical array
     - MObject::kNullObj
     - input / configuration; Node input geometry; see the wiring and package contract below. Short name: ``ig``.
   * - outputGeometry
     - mesh logical array
     - computed
     - output; Computed output geometry; see the wiring and package contract below. Short name: ``og``.
   * - auxiliaryGeometry
     - mesh logical array
     - computed
     - output; Computed auxiliary geometry; see the wiring and package contract below. Short name: ``ag``.
   * - outputPoints
     - double[]
     - computed
     - output; Packed XYZ points in package order; every point occupies three doubles. Short name: ``op``.

Wiring and resource contract
----------------------------

Validate operation ordering, buffer ranges, and external inputs. The node name does not imply an automatic character exporter.

See :doc:`shared integration contracts <contracts>` for packed indices, typed units, reloads, package schemas, and safe reconnection.

Usage
-----

.. code-block:: python

   import maya.cmds as cmds
   node = cmds.createNode("openRigGraphFaceGeometryBatch", name="exampleFaceGeometryBatch")

This creates the DG interface; it does not prepare a graph, cache, or geometry package. Configure the listed inputs before requesting its outputs.

Download the :download:`synthetic Maya interface checks <../../../examples/maya/check_interfaces.py>` and the :doc:`complete porting tutorial <../porting/tutorial>`.

Validation
----------

Check actual attribute types and logical indices, then compare the connected output across changing inputs and fractional times. Node creation alone is not deformation parity. Reject stale/missing resources and layouts that do not match the package.
