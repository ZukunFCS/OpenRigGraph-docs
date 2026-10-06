openRigGraphScalarScatter
=========================

Expose typed scalar channels from a packed double array.

**Layer:** Maya integration node. **Type identifier:** ``openRigGraphScalarScatter``.

When to use
-----------

Use at numeric, angle, distance, or time plug boundaries requiring explicit Maya types.

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
   * - expectedInputValueCount
     - integer
     - 0
     - input / configuration; Declared expected input value count; must match the corresponding packed layout. Short name: ``eivc``.
   * - numberIndices
     - integer[]
     - empty
     - input / configuration; Packed source indices, one per corresponding output logical element. Short name: ``ni``.
   * - outputNumber
     - double logical array
     - computed
     - output; Typed values selected by the corresponding indices array. Short name: ``on``.
   * - angleIndices
     - integer[]
     - empty
     - input / configuration; Packed source indices, one per corresponding output logical element. Short name: ``ai``.
   * - outputAngle
     - angle; packed degrees logical array
     - computed
     - output; Typed values selected by the corresponding indices array. Short name: ``oa``.
   * - distanceIndices
     - integer[]
     - empty
     - input / configuration; Packed source indices, one per corresponding output logical element. Short name: ``di``.
   * - outputDistance
     - distance; packed centimeters logical array
     - computed
     - output; Typed values selected by the corresponding indices array. Short name: ``od``.
   * - boolIndices
     - integer[]
     - empty
     - input / configuration; Packed source indices, one per corresponding output logical element. Short name: ``bi``.
   * - outputBool
     - boolean; packed 0 or 1 logical array
     - computed
     - output; Typed values selected by the corresponding indices array. Short name: ``ob``.
   * - intIndices
     - integer[]
     - empty
     - input / configuration; Packed source indices, one per corresponding output logical element. Short name: ``ii``.
   * - outputInt
     - integer; packed integral int32 logical array
     - computed
     - output; Typed values selected by the corresponding indices array. Short name: ``oi``.

Wiring and resource contract
----------------------------

Select indices explicitly. Typed angle outputs use Maya's internal unit conventions; compare connected downstream values.

See :doc:`shared integration contracts <contracts>` for packed indices, typed units, reloads, package schemas, and safe reconnection.

Usage
-----

.. code-block:: python

   import maya.cmds as cmds
   node = cmds.createNode("openRigGraphScalarScatter", name="exampleScalarScatter")

This creates the DG interface; it does not prepare a graph, cache, or geometry package. Configure the listed inputs before requesting its outputs.

Download the :download:`synthetic Maya interface checks <../../../examples/maya/check_interfaces.py>` and the :doc:`complete porting tutorial <../porting/tutorial>`.

Validation
----------

Check actual attribute types and logical indices, then compare the connected output across changing inputs and fractional times. Node creation alone is not deformation parity. Reject stale/missing resources and layouts that do not match the package.
