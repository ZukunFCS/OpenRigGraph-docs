openriggraph.maya_bridge
========================

.. py:module:: openriggraph.maya_bridge

**Environment:** Maya Python for scene operations; pure numeric helpers may run in ordinary Python.

Use keyword arguments when supplied; preserve the source function's declared coordinate spaces, logical indices, and path ownership. Read the :doc:`porting workflow <../../porting/agent_workflow>` for orchestration.

.. py:function:: csv_env_set(name)

   Csv env set.

   **Return type:** ``set[str]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``name``
     - ``str``
     - ``required``
     - Explicit name for this operation; preserve the matching graph/program/scene data contract.

.. py:function:: maya_node_leaf_name(node)

   Maya node leaf name.

   **Return type:** ``str``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``node``
     - ``str``
     - ``required``
     - Maya node identifier for the named integration boundary; requires the matching plug-in/scene context.

.. py:function:: maya_node_name_looks_like_static_helper(node)

   Maya node name looks like static helper.

   **Return type:** ``bool``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``node``
     - ``str``
     - ``required``
     - Maya node identifier for the named integration boundary; requires the matching plug-in/scene context.

.. py:function:: maya_node_name_looks_like_animator_control(node)

   Maya node name looks like animator control.

   **Return type:** ``bool``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``node``
     - ``str``
     - ``required``
     - Maya node identifier for the named integration boundary; requires the matching plug-in/scene context.

.. py:function:: resolve_project_references(cmds, scene_path)

   Load missing/deferred references from matching files beside the project scene.

   **Return type:** ``list[dict[str, Any]]``.

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
   * - ``scene_path``
     - ``Path``
     - ``required``
     - Filesystem path for scene path; use the caller's scene/package/SDK root and preserve relocation requirements.

.. py:function:: reset_maya_controller_defaults(cmds, controller_attrs)

   Reset settable scalar controllers to their Maya-declared defaults.

   **Return type:** ``list[dict[str, Any]]``.

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
   * - ``controller_attrs``
     - ``Sequence[str]``
     - ``required``
     - Explicit controller attrs for this operation; preserve the matching graph/program/scene data contract.

.. py:function:: recover_ascii_node_types(scene_path)

   Recover node types from a Maya ASCII scene without loading plug-ins.

   **Return type:** ``dict[str, str]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``scene_path``
     - ``Path``
     - ``required``
     - Filesystem path for scene path; use the caller's scene/package/SDK root and preserve relocation requirements.

.. py:function:: classify_rig_logic_graph(graph)

   Classify whether a graph payload is directly supported by ORG v1.

   **Return type:** ``dict[str, Any]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``graph``
     - ``Optional[Mapping[str, Any]]``
     - ``required``
     - Parsed ORG/legacy graph mapping; use the format expected by this entry point.

.. py:function:: lower_legacy_graph_to_openriggraph(graph)

   Lower the legacy renderer-local graph shape to OpenRigGraph v1 JSON.

   **Return type:** ``Optional[dict[str, Any]]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``graph``
     - ``Mapping[str, Any]``
     - ``required``
     - Parsed ORG/legacy graph mapping; use the format expected by this entry point.

.. py:function:: lower_open_maya_blendshape_graph_to_openriggraph(cmds, scene_path, blendshape_nodes, target_names, extra_outputs=None, allow_partial_outputs=False, enable_experimental_matrix_constraints=False, enable_translate_only_matrix_constraints=False, enable_known_controller_matrix_constraints=True, known_matrix_controller_allowlist=None, controller_allowlist=None, enable_dag_matrix_lowering=False, effective_joint_paths=None, emit_effective_joint_matrices=False, emit_effective_joint_channels=True, external_source_endpoints=None, external_transform_nodes=None)

   Trace an already-open Maya scene and return an ORG graph when possible.

   **Return type:** ``Optional[dict[str, Any]]``.

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
   * - ``scene_path``
     - ``str | Path``
     - ``required``
     - Filesystem path for scene path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``blendshape_nodes``
     - ``Sequence[str]``
     - ``required``
     - Maya node identifier for the named integration boundary; requires the matching plug-in/scene context.
   * - ``target_names``
     - ``Sequence[str]``
     - ``required``
     - Explicit target names for this operation; preserve the matching graph/program/scene data contract.
   * - ``extra_outputs``
     - ``Sequence[str | Mapping[str, Any]] | None``
     - ``None``
     - Explicit extra outputs for this operation; preserve the matching graph/program/scene data contract.
   * - ``allow_partial_outputs``
     - ``bool``
     - ``False``
     - Permit an explicitly reported partial lowering; not a complete-port acceptance flag.
   * - ``enable_experimental_matrix_constraints``
     - ``bool``
     - ``False``
     - Opt in to the named scoped lowering path; independently verify its topology/settings and outputs.
   * - ``enable_translate_only_matrix_constraints``
     - ``bool``
     - ``False``
     - Opt in to the named scoped lowering path; independently verify its topology/settings and outputs.
   * - ``enable_known_controller_matrix_constraints``
     - ``bool``
     - ``True``
     - Opt in to the named scoped lowering path; independently verify its topology/settings and outputs.
   * - ``known_matrix_controller_allowlist``
     - ``Collection[str] | None``
     - ``None``
     - Explicit known matrix controller allowlist for this operation; preserve the matching graph/program/scene data contract.
   * - ``controller_allowlist``
     - ``Collection[str] | None``
     - ``None``
     - Optional explicit input cohort; do not discard live intermediate dependencies.
   * - ``enable_dag_matrix_lowering``
     - ``bool``
     - ``False``
     - Opt in to the named scoped lowering path; independently verify its topology/settings and outputs.
   * - ``effective_joint_paths``
     - ``Sequence[str] | None``
     - ``None``
     - Explicit effective joint paths for this operation; preserve the matching graph/program/scene data contract.
   * - ``emit_effective_joint_matrices``
     - ``bool``
     - ``False``
     - Choose whether the named effective channels/matrices are emitted; declare output layout explicitly.
   * - ``emit_effective_joint_channels``
     - ``bool``
     - ``True``
     - Choose whether the named effective channels/matrices are emitted; declare output layout explicitly.
   * - ``external_source_endpoints``
     - ``Mapping[str, str] | None``
     - ``None``
     - Explicit externally owned source endpoints retained at the graph boundary.
   * - ``external_transform_nodes``
     - ``Collection[str] | None``
     - ``None``
     - Maya node identifier for the named integration boundary; requires the matching plug-in/scene context.
