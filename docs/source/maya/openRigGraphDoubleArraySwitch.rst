openRigGraphDoubleArraySwitch
=============================

Select between live and cached typed double-array streams.

**Layer:** Maya integration node. **Type identifier:** ``openRigGraphDoubleArraySwitch``.

When to use
-----------

Use at a deliberate live-authoring/cached-playback boundary.

Attributes
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - cachedValues
     - double[]
     - empty
     - input / configuration; Node cached values; see the wiring and package contract below. Short name: ``cv``.
   * - liveValues
     - double[]
     - empty
     - input / configuration; Node live values; see the wiring and package contract below. Short name: ``lv``.
   * - liveMode
     - boolean
     - false
     - input / configuration; Node live mode; see the wiring and package contract below. Short name: ``lm``.
   * - outputValues
     - double[]
     - computed
     - output; Computed output values; see the wiring and package contract below. Short name: ``ov``.

Wiring and resource contract
----------------------------

Selection does not make a stale cache valid. Invalidate caches after relevant input or curve edits and rebuild before switching back.

See :doc:`shared integration contracts <contracts>` for packed indices, typed units, reloads, package schemas, and safe reconnection.

Usage
-----

.. code-block:: python

   import maya.cmds as cmds
   node = cmds.createNode("openRigGraphDoubleArraySwitch", name="exampleDoubleArraySwitch")

This creates the DG interface; it does not prepare a graph, cache, or geometry package. Configure the listed inputs before requesting its outputs.

Download the :download:`synthetic Maya interface checks <../../../examples/maya/check_interfaces.py>` and the :doc:`complete porting tutorial <../porting/tutorial>`.

Validation
----------

Check actual attribute types and logical indices, then compare the connected output across changing inputs and fractional times. Node creation alone is not deformation parity. Reject stale/missing resources and layouts that do not match the package.
