openRigGraphInputBundle
=======================

Pack Maya scalar input plugs into a typed double array.

**Layer:** Maya integration node. **Type identifier:** ``openRigGraphInputBundle``.

When to use
-----------

Use when a packed evaluator or geometry operation consumes a shared control array.

Attributes
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - defaultValues
     - double[]
     - empty
     - input / configuration; Node default values; see the wiring and package contract below. Short name: ``dv``.
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
   * - outputValues
     - double[]
     - computed
     - output; Computed output values; see the wiring and package contract below. Short name: ``ov``.

Wiring and resource contract
----------------------------

Logical array indices are part of the graph layout; do not compact them.

See :doc:`shared integration contracts <contracts>` for packed indices, typed units, reloads, package schemas, and safe reconnection.

Usage
-----

.. code-block:: python

   import maya.cmds as cmds
   node = cmds.createNode("openRigGraphInputBundle", name="exampleInputBundle")

This creates the DG interface; it does not prepare a graph, cache, or geometry package. Configure the listed inputs before requesting its outputs.

Download the :download:`synthetic Maya interface checks <../../../examples/maya/check_interfaces.py>` and the :doc:`complete porting tutorial <../porting/tutorial>`.

Validation
----------

Check actual attribute types and logical indices, then compare the connected output across changing inputs and fractional times. Node creation alone is not deformation parity. Reject stale/missing resources and layouts that do not match the package.
