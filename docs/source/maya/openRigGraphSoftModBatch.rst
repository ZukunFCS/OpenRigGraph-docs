openRigGraphSoftModBatch
========================

Apply packaged scoped soft-modification operations to packed points.

**Layer:** Maya integration node. **Type identifier:** ``openRigGraphSoftModBatch``.

When to use
-----------

Use when falloff weights, transform inputs, and affected point sets have been captured and validated.

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
   * - packedValues
     - double[]
     - empty
     - input / configuration; Packed scalar data with indices defined by the graph/package contract. Short name: ``pv``.
   * - inputPoints
     - double[]
     - empty
     - input / configuration; Packed input XYZ points in the package's declared layout. Short name: ``ip``.
   * - outputPoints
     - double[]
     - computed
     - output; Packed XYZ points in package order; every point occupies three doubles. Short name: ``op``.

Wiring and resource contract
----------------------------

Preserve deformation order and spaces. Dynamic topology and uncaptured falloff behavior are outside the package contract.

See :doc:`shared integration contracts <contracts>` for packed indices, typed units, reloads, package schemas, and safe reconnection.

Usage
-----

.. code-block:: python

   import maya.cmds as cmds
   node = cmds.createNode("openRigGraphSoftModBatch", name="exampleSoftModBatch")

This creates the DG interface; it does not prepare a graph, cache, or geometry package. Configure the listed inputs before requesting its outputs.

Download the :download:`synthetic Maya interface checks <../../../examples/maya/check_interfaces.py>` and the :doc:`complete porting tutorial <../porting/tutorial>`.

Validation
----------

Check actual attribute types and logical indices, then compare the connected output across changing inputs and fractional times. Node creation alone is not deformation parity. Reject stale/missing resources and layouts that do not match the package.
