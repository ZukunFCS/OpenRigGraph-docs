openRigGraphUvPinBatch
======================

Evaluate packaged mesh-surface attachment output batches.

**Layer:** Maya integration node. **Type identifier:** ``openRigGraphUvPinBatch``.

When to use
-----------

Use when a declared mesh/UV attachment set can share one packed geometry input.

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
     - input / configuration; Path to the node's explicitly prepared geometry package. Short name: ``pkg``.
   * - packedPoints
     - double[]
     - empty
     - input / configuration; Node packed points; see the wiring and package contract below. Short name: ``ppoints``.
   * - reloadToken
     - integer
     - 0
     - input / configuration; Increment after replacing a resource at the same path to force reload. Short name: ``reload``.
   * - expectedPackedPointCount
     - integer
     - computed
     - output; Declared expected packed point count; must match the corresponding packed layout. Short name: ``expectedPoints``.
   * - outputMatrix
     - matrix4x4 (double) logical array
     - computed
     - output; Computed output matrix; see the wiring and package contract below. Short name: ``outMatrix``.

Wiring and resource contract
----------------------------

Capture topology, UV indices, and frame policies explicitly; verify seams and changing deformation.

See :doc:`shared integration contracts <contracts>` for packed indices, typed units, reloads, package schemas, and safe reconnection.

Usage
-----

.. code-block:: python

   import maya.cmds as cmds
   node = cmds.createNode("openRigGraphUvPinBatch", name="exampleUvPinBatch")

This creates the DG interface; it does not prepare a graph, cache, or geometry package. Configure the listed inputs before requesting its outputs.

Download the :download:`synthetic Maya interface checks <../../../examples/maya/check_interfaces.py>` and the :doc:`complete porting tutorial <../porting/tutorial>`.

Validation
----------

Check actual attribute types and logical indices, then compare the connected output across changing inputs and fractional times. Node creation alone is not deformation parity. Reject stale/missing resources and layouts that do not match the package.
