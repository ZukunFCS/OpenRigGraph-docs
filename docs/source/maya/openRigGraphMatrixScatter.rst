openRigGraphMatrixScatter
=========================

Expose selected matrices from packed evaluation output.

**Layer:** Maya integration node. **Type identifier:** ``openRigGraphMatrixScatter``.

When to use
-----------

Use to connect matrix blocks into Maya transform/deformer inputs.

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
   * - jointCount
     - integer
     - 0
     - input / configuration; Declared joint count; must match the corresponding packed layout. Short name: ``jc``.
   * - expectedInputValueCount
     - integer
     - 0
     - input / configuration; Declared expected input value count; must match the corresponding packed layout. Short name: ``eivc``.
   * - inputMode
     - integer
     - 0
     - input / configuration; Node input mode; see the wiring and package contract below. Short name: ``im``.
   * - rotateOrder
     - integer logical array
     - 0
     - input / configuration; Node rotate order; see the wiring and package contract below. Short name: ``ro``.
   * - jointOrientValues
     - double[]
     - empty
     - input / configuration; Node joint orient values; see the wiring and package contract below. Short name: ``jov``.
   * - outputMatrix
     - matrix4x4 (double) logical array
     - computed
     - output; Computed output matrix; see the wiring and package contract below. Short name: ``om``.

Wiring and resource contract
----------------------------

Each matrix block contains 16 row-major values. Check base indices and graph output units.

See :doc:`shared integration contracts <contracts>` for packed indices, typed units, reloads, package schemas, and safe reconnection.

Usage
-----

.. code-block:: python

   import maya.cmds as cmds
   node = cmds.createNode("openRigGraphMatrixScatter", name="exampleMatrixScatter")

This creates the DG interface; it does not prepare a graph, cache, or geometry package. Configure the listed inputs before requesting its outputs.

Download the :download:`synthetic Maya interface checks <../../../examples/maya/check_interfaces.py>` and the :doc:`complete porting tutorial <../porting/tutorial>`.

Validation
----------

Check actual attribute types and logical indices, then compare the connected output across changing inputs and fractional times. Node creation alone is not deformation parity. Reject stale/missing resources and layouts that do not match the package.
