openriggraph.maya_snapshot
==========================

.. py:module:: openriggraph.maya_snapshot

**Environment:** Maya Python for scene operations; pure numeric helpers may run in ordinary Python.

Use keyword arguments when supplied; preserve the source function's declared coordinate spaces, logical indices, and path ownership. Read the :doc:`porting workflow <../../porting/agent_workflow>` for orchestration.

.. py:class:: MissingSnapshotData

   A lowerer requested information that the persisted snapshot lacks.

No additional fields.

.. py:class:: MayaSnapshotCommands

   Read-only, ``maya.cmds``-shaped view of an ORG Maya snapshot.

No additional fields.

.. py:method:: MayaSnapshotCommands.openRigGraphIkChains(self)

   Return the optional native IK semantic supplement.

   **Return type:** ``list[dict[str, Any]]``.

.. py:method:: MayaSnapshotCommands.openRigGraphIkOracleFirst(self)

   Open rig graph ik oracle first.

   **Return type:** ``dict[str, dict[str, Any]]``.

.. py:method:: MayaSnapshotCommands.nodeType(self, node, **kwargs)

   Node type.

   **Return type:** ``Any``.

.. py:method:: MayaSnapshotCommands.objExists(self, value)

   Obj exists.

   **Return type:** ``bool``.

.. py:method:: MayaSnapshotCommands.getAttr(self, plug, **kwargs)

   Get attr.

   **Return type:** ``Any``.

.. py:method:: MayaSnapshotCommands.listAttr(self, node, **_kwargs)

   List attr.

   **Return type:** ``list[str]``.

.. py:method:: MayaSnapshotCommands.listConnections(self, value, **kwargs)

   List connections.

   **Return type:** ``list[str]``.

.. py:method:: MayaSnapshotCommands.listRelatives(self, node, **kwargs)

   List relatives.

   **Return type:** ``list[str]``.

.. py:method:: MayaSnapshotCommands.ls(self, value=None, **kwargs)

   Ls.

   **Return type:** ``list[str]``.

.. py:method:: MayaSnapshotCommands.aliasAttr(self, node, **kwargs)

   Alias attr.

   **Return type:** ``list[str]``.

.. py:method:: MayaSnapshotCommands.attributeQuery(self, attribute, **kwargs)

   Attribute query.

   **Return type:** ``Any``.

.. py:method:: MayaSnapshotCommands.unknownNode(self, node, **kwargs)

   Unknown node.

   **Return type:** ``str``.

.. py:method:: MayaSnapshotCommands.keyframe(self, node, **kwargs)

   Keyframe.

   **Return type:** ``list[float]``.

.. py:method:: MayaSnapshotCommands.keyTangent(self, node, **kwargs)

   Key tangent.

   **Return type:** ``list[str]``.

.. py:method:: MayaSnapshotCommands.referenceQuery(self, node, **kwargs)

   Reference query.

   **Return type:** ``Any``.

.. py:method:: MayaSnapshotCommands.file(self, **kwargs)

   File.

   **Return type:** ``str``.

.. py:method:: MayaSnapshotCommands.pointConstraint(self, node, **kwargs)

   Point constraint.

   **Return type:** ``list[str]``.

.. py:method:: MayaSnapshotCommands.skinCluster(self, node, **kwargs)

   Skin cluster.

   **Return type:** ``list[str]``.

.. py:method:: MayaSnapshotCommands.pointPosition(self, component, **_kwargs)

   Point position.

   **Return type:** ``list[float]``.

.. py:method:: MayaSnapshotCommands.pointOnCurve(self, curve, **kwargs)

   Point on curve.

   **Return type:** ``list[float]``.

.. py:method:: MayaSnapshotCommands.openRigGraphPayload(self, node)

   Return a copy of native geometry or special-node payload data.

   **Return type:** ``dict[str, Any]``.

.. py:method:: MayaSnapshotCommands.dgdirty(self, **_kwargs)

   Dgdirty.

   **Return type:** ``None``.

.. py:method:: MayaSnapshotCommands.refresh(self, **_kwargs)

   Refresh.

   **Return type:** ``None``.

.. py:function:: load_maya_snapshot(directory)

   Load maya snapshot.

   **Return type:** ``MayaSnapshotCommands``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``directory``
     - ``str | Path``
     - ``required``
     - Directory containing the complete snapshot/package expected by this entry point.

.. py:function:: lower_maya_snapshot_to_openriggraph(directory, scene_path, controller_plugs, output_plugs, **kwargs)

   Lower a persisted snapshot with the regular bridge and no Maya import.

   **Return type:** ``dict[str, Any]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``directory``
     - ``str | Path``
     - ``required``
     - Directory containing the complete snapshot/package expected by this entry point.
   * - ``scene_path``
     - ``str | Path``
     - ``required``
     - Filesystem path for scene path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``controller_plugs``
     - ``Iterable[str]``
     - ``required``
     - Requested source input plugs; preserve order and choose animator-facing independent inputs.
   * - ``output_plugs``
     - ``Iterable[str]``
     - ``required``
     - Requested source output plugs; declare units/spaces and required cohort coverage.
