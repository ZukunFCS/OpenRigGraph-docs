openRigGraphCurveCache
======================

Read sparse cached numeric rows using a time input.

**Layer:** Maya integration node. **Type identifier:** ``openRigGraphCurveCache``.

When to use
-----------

Use for verified cached playback with a known output layout.

Attributes
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - cachePath
     - string
     - empty
     - input / configuration; Path to the prepared numeric cache. Short name: ``cp``.
   * - reloadToken
     - integer
     - 0
     - input / configuration; Increment after replacing a resource at the same path to force reload. Short name: ``rt``.
   * - time
     - time
     - 0.0
     - input / configuration; Evaluation time in the cache's declared time convention. Short name: ``tm``.
   * - interpolation
     - integer enum
     - 1
     - input / configuration; 0 exact sample, 1 nearest (default), 2 linear; see integration contracts. Short name: ``ip``.
   * - outputValues
     - double[]
     - computed
     - output; Computed output values; see the wiring and package contract below. Short name: ``ov``.
   * - sampleIndex
     - integer
     - computed
     - output; Declared sample index; indices address the packed input/package layout. Short name: ``si``.

Wiring and resource contract
----------------------------

Cache time range, fractional-time policy, path reload, and stale-cache detection must be explicit. Preserve editable source curves for authoring.

See :doc:`shared integration contracts <contracts>` for packed indices, typed units, reloads, package schemas, and safe reconnection.

Usage
-----

.. code-block:: python

   import maya.cmds as cmds
   node = cmds.createNode("openRigGraphCurveCache", name="exampleCurveCache")

This creates the DG interface; it does not prepare a graph, cache, or geometry package. Configure the listed inputs before requesting its outputs.

Download the :download:`synthetic Maya interface checks <../../../examples/maya/check_interfaces.py>` and the :doc:`complete porting tutorial <../porting/tutorial>`.

Validation
----------

Check actual attribute types and logical indices, then compare the connected output across changing inputs and fractional times. Node creation alone is not deformation parity. Reject stale/missing resources and layouts that do not match the package.
