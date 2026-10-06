openRigGraphRuntime
===================

Evaluate a compiled graph through compact scalar, matrix, and curve input interfaces.

**Layer:** Maya integration node. **Type identifier:** ``openRigGraphRuntime``.

When to use
-----------

Use for packed runtime wiring with output-generation and changed-influence tracking.

Attributes
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - graphPath
     - string
     - empty
     - input / configuration; Graph JSON or supported compiled-module path; use a relocatable package path. Short name: ``gp``.
   * - reloadToken
     - integer
     - 0
     - input / configuration; Increment after replacing a resource at the same path to force reload. Short name: ``rt``.
   * - inputValue
     - double logical array
     - 0.0
     - input / configuration; Controller value at its graph logical index. Short name: ``iv``.
   * - inputMatrix
     - matrix4x4 (double) logical array
     - identity
     - input / configuration; Matrix input; preserve declared input-space convention. Short name: ``im``.
   * - matrixBaseIndex
     - integer logical array
     - -1
     - input / configuration; Controller-array base index assigned to each matrix input. Short name: ``mbi``.
   * - curveIndices
     - integer[]
     - empty
     - input / configuration; Graph controller indices for the corresponding curveValues entries. Short name: ``ci``.
   * - curveValues
     - double[]
     - empty
     - input / configuration; Curve values ordered exactly like curveIndices. Short name: ``cv``.
   * - expectedOutputValueCount
     - integer
     - 0
     - input / configuration; Expected packed scalar count; validate against the loaded module. Short name: ``eovc``.
   * - matrixOutputCount
     - integer
     - 0
     - input / configuration; Number of matrix output blocks used by change tracking. Short name: ``moc``.
   * - changeEpsilon
     - double
     - 0.0
     - input / configuration; Nonnegative change-detection threshold; does not change graph math. Short name: ``ce``.
   * - resolvedControls
     - double[]
     - computed
     - output; Resolved graph control array, including defaults and bound inputs. Short name: ``rc``.
   * - packedOutput
     - double[]
     - computed
     - output; Graph outputs in the declared graph-output order. Short name: ``po``.
   * - outputGeneration
     - integer
     - computed
     - output; Generation marker used to coordinate output consumers. Short name: ``og``.
   * - changedInfluenceIndices
     - integer[]
     - computed
     - output; Indices whose output matrix blocks changed beyond changeEpsilon. Short name: ``cii``.

Wiring and resource contract
----------------------------

Graph controller order, matrixBaseIndex, and output counts must match the loaded module. Increment reloadToken after replacing the same graph path.

See :doc:`shared integration contracts <contracts>` for packed indices, typed units, reloads, package schemas, and safe reconnection.

Usage
-----

.. code-block:: python

   import maya.cmds as cmds
   node = cmds.createNode("openRigGraphRuntime", name="exampleRuntime")

This creates the DG interface; it does not prepare a graph, cache, or geometry package. Configure the listed inputs before requesting its outputs.

Download the :download:`synthetic Maya interface checks <../../../examples/maya/check_interfaces.py>` and the :doc:`complete porting tutorial <../porting/tutorial>`.

Validation
----------

Check actual attribute types and logical indices, then compare the connected output across changing inputs and fractional times. Node creation alone is not deformation parity. Reject stale/missing resources and layouts that do not match the package.
