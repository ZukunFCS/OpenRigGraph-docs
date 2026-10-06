openriggraph.maya_runtime
=========================

.. py:module:: openriggraph.maya_runtime

**Environment:** Maya Python for scene operations; pure numeric helpers may run in ordinary Python.

Use keyword arguments when supplied; preserve the source function's declared coordinate spaces, logical indices, and path ownership. Read the :doc:`porting workflow <../../porting/agent_workflow>` for orchestration.

.. py:function:: wire_openriggraph_evaluator(cmds, graph_metadata_path, module_path=None, *, plugin_path=None, node_name='openRigGraphEvaluator', namespace='', plug_map=None, replace_existing=False, connect_outputs=True)

   Create and connect an ``openRigGraphEvaluator`` Maya node.

   **Return type:** ``dict[str, Any]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``cmds``
     - ``Any``
     - ``required``
     - Maya commands-compatible interface, or the SDK snapshot adapter where supported.
   * - ``graph_metadata_path``
     - ``str | Path``
     - ``required``
     - Filesystem path for graph metadata path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``module_path``
     - ``str | Path | None``
     - ``None``
     - Filesystem path for module path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``plugin_path``
     - ``str | Path | None``
     - ``None``
     - Filesystem path for plugin path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``node_name``
     - ``str``
     - ``'openRigGraphEvaluator'``
     - Maya node identifier for the named integration boundary; requires the matching plug-in/scene context.
   * - ``namespace``
     - ``str``
     - ``''``
     - Maya namespace used to resolve scene plugs; do not infer one from an unrelated asset.
   * - ``plug_map``
     - ``Mapping[str, str] | None``
     - ``None``
     - Explicit plug map for this operation; preserve the matching graph/program/scene data contract.
   * - ``replace_existing``
     - ``bool``
     - ``False``
     - Allow the helper's documented reconnection/replacement; preserve a restorable source wiring packet.
   * - ``connect_outputs``
     - ``bool``
     - ``True``
     - Choose whether the named scene outputs are connected during wiring; preserve their ownership.

.. py:function:: connect_openriggraph_outputs(cmds, evaluator, graph_metadata_path, *, namespace='', plug_map=None, replace_existing=False)

   Connect an existing evaluator's indexed outputs to graph destinations.

   **Return type:** ``dict[str, Any]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``cmds``
     - ``Any``
     - ``required``
     - Maya commands-compatible interface, or the SDK snapshot adapter where supported.
   * - ``evaluator``
     - ``str``
     - ``required``
     - Maya node identifier for the named integration boundary; requires the matching plug-in/scene context.
   * - ``graph_metadata_path``
     - ``str | Path``
     - ``required``
     - Filesystem path for graph metadata path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``namespace``
     - ``str``
     - ``''``
     - Maya namespace used to resolve scene plugs; do not infer one from an unrelated asset.
   * - ``plug_map``
     - ``Mapping[str, str] | None``
     - ``None``
     - Explicit plug map for this operation; preserve the matching graph/program/scene data contract.
   * - ``replace_existing``
     - ``bool``
     - ``False``
     - Allow the helper's documented reconnection/replacement; preserve a restorable source wiring packet.

.. py:function:: wire_openriggraph_packed_evaluator(cmds, graph_metadata_path, module_path, *, plugin_path=None, node_prefix='openRigGraphPacked', namespace='', plug_map=None, connect_joint_outputs=False, replace_existing=False, output_mode='joint_channels')

   Wire the packed Maya bridge while preserving the ORGB controller/output order.

   **Return type:** ``dict[str, Any]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``cmds``
     - ``Any``
     - ``required``
     - Maya commands-compatible interface, or the SDK snapshot adapter where supported.
   * - ``graph_metadata_path``
     - ``str | Path``
     - ``required``
     - Filesystem path for graph metadata path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``module_path``
     - ``str | Path``
     - ``required``
     - Filesystem path for module path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``plugin_path``
     - ``str | Path | None``
     - ``None``
     - Filesystem path for plugin path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``node_prefix``
     - ``str``
     - ``'openRigGraphPacked'``
     - Maya node identifier for the named integration boundary; requires the matching plug-in/scene context.
   * - ``namespace``
     - ``str``
     - ``''``
     - Maya namespace used to resolve scene plugs; do not infer one from an unrelated asset.
   * - ``plug_map``
     - ``Mapping[str, str] | None``
     - ``None``
     - Explicit plug map for this operation; preserve the matching graph/program/scene data contract.
   * - ``connect_joint_outputs``
     - ``bool``
     - ``False``
     - Choose whether the named scene outputs are connected during wiring; preserve their ownership.
   * - ``replace_existing``
     - ``bool``
     - ``False``
     - Allow the helper's documented reconnection/replacement; preserve a restorable source wiring packet.
   * - ``output_mode``
     - ``str``
     - ``'joint_channels'``
     - Explicit output mode for this operation; preserve the matching graph/program/scene data contract.

.. py:function:: wire_openriggraph_packed_values(cmds, graph_metadata_path, module_path, *, plugin_path=None, node_prefix='openRigGraphPackedValues', namespace='', plug_map=None, matrix_sources=None)

   Wire arbitrary packed ORG outputs without imposing a joint layout.

   **Return type:** ``dict[str, Any]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``cmds``
     - ``Any``
     - ``required``
     - Maya commands-compatible interface, or the SDK snapshot adapter where supported.
   * - ``graph_metadata_path``
     - ``str | Path``
     - ``required``
     - Filesystem path for graph metadata path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``module_path``
     - ``str | Path``
     - ``required``
     - Filesystem path for module path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``plugin_path``
     - ``str | Path | None``
     - ``None``
     - Filesystem path for plugin path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``node_prefix``
     - ``str``
     - ``'openRigGraphPackedValues'``
     - Maya node identifier for the named integration boundary; requires the matching plug-in/scene context.
   * - ``namespace``
     - ``str``
     - ``''``
     - Maya namespace used to resolve scene plugs; do not infer one from an unrelated asset.
   * - ``plug_map``
     - ``Mapping[str, str] | None``
     - ``None``
     - Explicit plug map for this operation; preserve the matching graph/program/scene data contract.
   * - ``matrix_sources``
     - ``Mapping[str, str] | None``
     - ``None``
     - Declared source matrices and their graph input-layout mapping.

.. py:function:: connect_openriggraph_shot_inputs(cmds, graph_metadata_path, bundle, *, plug_map=None)

   Connect explicitly marked shot-level curves after the rig is referenced.

   **Return type:** ``dict[str, Any]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``cmds``
     - ``Any``
     - ``required``
     - Maya commands-compatible interface, or the SDK snapshot adapter where supported.
   * - ``graph_metadata_path``
     - ``str | Path``
     - ``required``
     - Filesystem path for graph metadata path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``bundle``
     - ``str``
     - ``required``
     - Maya node identifier for the named integration boundary; requires the matching plug-in/scene context.
   * - ``plug_map``
     - ``Mapping[str, str] | None``
     - ``None``
     - Explicit plug map for this operation; preserve the matching graph/program/scene data contract.

.. py:function:: wire_openriggraph_packed_skin_evaluator(cmds, graph_metadata_path, module_path, **kwargs)

   Wire a packed evaluator whose outputs are contiguous world matrices.

   **Return type:** ``dict[str, Any]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``cmds``
     - ``Any``
     - ``required``
     - Maya commands-compatible interface, or the SDK snapshot adapter where supported.
   * - ``graph_metadata_path``
     - ``str | Path``
     - ``required``
     - Filesystem path for graph metadata path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``module_path``
     - ``str | Path``
     - ``required``
     - Filesystem path for module path; use the caller's scene/package/SDK root and preserve relocation requirements.

.. py:function:: wire_openriggraph_compact_runtime(cmds, graph_metadata_path, module_path, *, plugin_path=None, node_name='openRigGraphRuntime', namespace='', plug_map=None, controller_indices=None)

   Wire the fused sparse-input ORG runtime node.

   **Return type:** ``dict[str, Any]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``cmds``
     - ``Any``
     - ``required``
     - Maya commands-compatible interface, or the SDK snapshot adapter where supported.
   * - ``graph_metadata_path``
     - ``str | Path``
     - ``required``
     - Filesystem path for graph metadata path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``module_path``
     - ``str | Path``
     - ``required``
     - Filesystem path for module path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``plugin_path``
     - ``str | Path | None``
     - ``None``
     - Filesystem path for plugin path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``node_name``
     - ``str``
     - ``'openRigGraphRuntime'``
     - Maya node identifier for the named integration boundary; requires the matching plug-in/scene context.
   * - ``namespace``
     - ``str``
     - ``''``
     - Maya namespace used to resolve scene plugs; do not infer one from an unrelated asset.
   * - ``plug_map``
     - ``Mapping[str, str] | None``
     - ``None``
     - Explicit plug map for this operation; preserve the matching graph/program/scene data contract.
   * - ``controller_indices``
     - ``set[int] | None``
     - ``None``
     - Graph controller-array indices for supplied values; do not compact sparse logical slots.

.. py:function:: connect_openriggraph_skin_matrices(cmds, wiring, skin_influences_by_cluster, *, namespace='', plug_map=None, replace_existing=False)

   Connect packed ORG world matrices directly to skinCluster matrix slots.

   **Return type:** ``dict[str, Any]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``cmds``
     - ``Any``
     - ``required``
     - Maya commands-compatible interface, or the SDK snapshot adapter where supported.
   * - ``wiring``
     - ``Mapping[str, Any]``
     - ``required``
     - Runtime wiring metadata returned by the corresponding connection helper.
   * - ``skin_influences_by_cluster``
     - ``Mapping[str, Any]``
     - ``required``
     - Explicit skin influences by cluster for this operation; preserve the matching graph/program/scene data contract.
   * - ``namespace``
     - ``str``
     - ``''``
     - Maya namespace used to resolve scene plugs; do not infer one from an unrelated asset.
   * - ``plug_map``
     - ``Mapping[str, str] | None``
     - ``None``
     - Explicit plug map for this operation; preserve the matching graph/program/scene data contract.
   * - ``replace_existing``
     - ``bool``
     - ``False``
     - Allow the helper's documented reconnection/replacement; preserve a restorable source wiring packet.

.. py:function:: restore_openriggraph_joint_drivers(cmds, disconnected)

   Restore the exact Maya connections returned by a body-joint driver cut.

   **Return type:** ``int``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``cmds``
     - ``Any``
     - ``required``
     - Maya commands-compatible interface, or the SDK snapshot adapter where supported.
   * - ``disconnected``
     - ``list[Mapping[str, str]]``
     - ``required``
     - Saved original connections used for restoration.

.. py:function:: wire_openriggraph_curve_cache(cmds, runtime_node, cache_path, controller_count, *, node_name='openRigGraphCurveCache', time_plug='time1.outTime', interpolation='nearest', live_controller_indices=None)

   Replace eager scalar runtime inputs with a dense time-sampled cache.

   **Return type:** ``dict[str, Any]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``cmds``
     - ``Any``
     - ``required``
     - Maya commands-compatible interface, or the SDK snapshot adapter where supported.
   * - ``runtime_node``
     - ``str``
     - ``required``
     - Maya node identifier for the named integration boundary; requires the matching plug-in/scene context.
   * - ``cache_path``
     - ``str | Path``
     - ``required``
     - Filesystem path for cache path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``controller_count``
     - ``int``
     - ``required``
     - Declared graph controller cardinality.
   * - ``node_name``
     - ``str``
     - ``'openRigGraphCurveCache'``
     - Maya node identifier for the named integration boundary; requires the matching plug-in/scene context.
   * - ``time_plug``
     - ``str``
     - ``'time1.outTime'``
     - Maya plug supplying evaluation time in the declared cache/curve convention.
   * - ``interpolation``
     - ``str``
     - ``'nearest'``
     - Declared interpolation policy for the corresponding curve/cache representation.
   * - ``live_controller_indices``
     - ``set[int] | None``
     - ``None``
     - Explicit live controller indices for this operation; preserve the matching graph/program/scene data contract.

.. py:function:: disconnect_openriggraph_joint_drivers(cmds, influence_order)

   Cut native TRS/OPM drivers after ORG takes over skin matrices.

   **Return type:** ``list[dict[str, str]]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``cmds``
     - ``Any``
     - ``required``
     - Maya commands-compatible interface, or the SDK snapshot adapter where supported.
   * - ``influence_order``
     - ``list[str]``
     - ``required``
     - Explicit influence ordering shared by matrices, weights, and package metadata.

.. py:function:: replace_joint_outputs_with_packed_opm(cmds, graph_path, wiring, *, namespace='', plug_map=None)

   Replace native joint channel drivers with the packed scatter OPM output.

   **Return type:** ``dict[str, Any]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``cmds``
     - ``Any``
     - ``required``
     - Maya commands-compatible interface, or the SDK snapshot adapter where supported.
   * - ``graph_path``
     - ``str | Path``
     - ``required``
     - Filesystem path for graph path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``wiring``
     - ``Mapping[str, Any]``
     - ``required``
     - Runtime wiring metadata returned by the corresponding connection helper.
   * - ``namespace``
     - ``str``
     - ``''``
     - Maya namespace used to resolve scene plugs; do not infer one from an unrelated asset.
   * - ``plug_map``
     - ``Mapping[str, str] | None``
     - ``None``
     - Explicit plug map for this operation; preserve the matching graph/program/scene data contract.
