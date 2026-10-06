openRigGraphEvaluator
=====================

Evaluate a graph with Maya numeric inputs and indexed numeric outputs.

**Layer:** Maya integration node. **Type identifier:** ``openRigGraphEvaluator``.

When to use
-----------

Use for a straightforward graph-to-Maya DG connection.

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
   * - packedInput
     - double[]
     - empty
     - input / configuration; Node packed input; see the wiring and package contract below. Short name: ``pi``.
   * - outputValue
     - double logical array
     - computed
     - output; Computed output value; see the wiring and package contract below. Short name: ``ov``.
   * - packedOutput
     - double[]
     - computed
     - output; Graph outputs in the declared graph-output order. Short name: ``po``.

Wiring and resource contract
----------------------------

Keep controller/output ordering identical to graph metadata. graphPath and reloadToken govern resource reloads.

See :doc:`shared integration contracts <contracts>` for packed indices, typed units, reloads, package schemas, and safe reconnection.

Usage
-----

.. code-block:: python

   import maya.cmds as cmds
   node = cmds.createNode("openRigGraphEvaluator", name="exampleEvaluator")

This creates the DG interface; it does not prepare a graph, cache, or geometry package. Configure the listed inputs before requesting its outputs.

Download the :download:`synthetic Maya interface checks <../../../examples/maya/check_interfaces.py>` and the :doc:`complete porting tutorial <../porting/tutorial>`.

Validation
----------

Check actual attribute types and logical indices, then compare the connected output across changing inputs and fractional times. Node creation alone is not deformation parity. Reject stale/missing resources and layouts that do not match the package.
