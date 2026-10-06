openriggraph.maya_scene_repair
==============================

.. py:module:: openriggraph.maya_scene_repair

**Environment:** Maya Python for scene operations; pure numeric helpers may run in ordinary Python.

Use keyword arguments when supplied; preserve the source function's declared coordinate spaces, logical indices, and path ownership. Read the :doc:`porting workflow <../../porting/agent_workflow>` for orchestration.

.. py:function:: file_sha256(path)

   File sha256.

   **Return type:** ``str``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``path``
     - ``Path``
     - ``required``
     - Filesystem path for path; use the caller's scene/package/SDK root and preserve relocation requirements.

.. py:function:: infer_project_root(scene_path)

   Return the project directory that owns a Maya scene.

   **Return type:** ``Path``.

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

.. py:function:: normalized_dependency_path(raw_path, scene_path, project_root)

   Normalized dependency path.

   **Return type:** ``Path``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``raw_path``
     - ``str``
     - ``required``
     - Filesystem path for raw path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``scene_path``
     - ``Path``
     - ``required``
     - Filesystem path for scene path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``project_root``
     - ``Path``
     - ``required``
     - Filesystem path for project root; use the caller's scene/package/SDK root and preserve relocation requirements.

.. py:function:: dependency_exists(raw_path, scene_path, project_root)

   Dependency exists.

   **Return type:** ``bool``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``raw_path``
     - ``str``
     - ``required``
     - Filesystem path for raw path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``scene_path``
     - ``Path``
     - ``required``
     - Filesystem path for scene path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``project_root``
     - ``Path``
     - ``required``
     - Filesystem path for project root; use the caller's scene/package/SDK root and preserve relocation requirements.

.. py:function:: build_filename_index(roots)

   Build a case-insensitive basename index once for a repair batch.

   **Return type:** ``dict[str, list[Path]]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``roots``
     - ``Iterable[Path]``
     - ``required``
     - Explicit roots for this operation; preserve the matching graph/program/scene data contract.

.. py:function:: resolve_dependency(raw_path, *, scene_path, project_root, filename_index, kind)

   Resolve one missing dependency and only approve an unambiguous match.

   **Return type:** ``dict[str, Any]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``raw_path``
     - ``str``
     - ``required``
     - Filesystem path for raw path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``scene_path``
     - ``Path``
     - ``required keyword``
     - Filesystem path for scene path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``project_root``
     - ``Path``
     - ``required keyword``
     - Filesystem path for project root; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``filename_index``
     - ``Mapping[str, Sequence[Path]]``
     - ``required keyword``
     - Explicit filename index for this operation; preserve the matching graph/program/scene data contract.
   * - ``kind``
     - ``str``
     - ``required keyword``
     - Explicit kind for this operation; preserve the matching graph/program/scene data contract.

.. py:function:: collect_path_dependencies(cmds)

   Collect path dependencies.

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

.. py:function:: collect_reference_dependencies(cmds)

   Collect reference dependencies.

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

.. py:function:: collect_material_assignments(cmds)

   Collect material assignments.

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

.. py:function:: controller_inventory(cmds)

   Controller inventory.

   **Return type:** ``dict[str, int]``.

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

.. py:function:: audit_scene_dependencies(cmds, scene_path, *, filename_index)

   Audit scene dependencies.

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
   * - ``scene_path``
     - ``Path``
     - ``required``
     - Filesystem path for scene path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``filename_index``
     - ``Mapping[str, Sequence[Path]]``
     - ``required keyword``
     - Explicit filename index for this operation; preserve the matching graph/program/scene data contract.

.. py:function:: create_immutable_backup(scene_path, backup_root=None)

   Create immutable backup.

   **Return type:** ``dict[str, Any]``.

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
   * - ``backup_root``
     - ``Path | None``
     - ``None``
     - Filesystem path for backup root; use the caller's scene/package/SDK root and preserve relocation requirements.

.. py:function:: apply_dependency_repairs(cmds, dependencies)

   Apply dependency repairs.

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
   * - ``dependencies``
     - ``Sequence[Mapping[str, Any]]``
     - ``required``
     - Explicit dependencies for this operation; preserve the matching graph/program/scene data contract.

.. py:function:: save_current_scene(cmds, scene_path)

   Save current scene.

   **Return type:** ``None``.

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
