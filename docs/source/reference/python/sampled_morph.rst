openriggraph.sampled_morph
==========================

.. py:module:: openriggraph.sampled_morph

**Environment:** Maya Python for scene operations; pure numeric helpers may run in ordinary Python.

Use keyword arguments when supplied; preserve the source function's declared coordinate spaces, logical indices, and path ownership. Read the :doc:`porting workflow <../../porting/agent_workflow>` for orchestration.

.. py:class:: SampledMorphTarget

   Sampled morph target.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``name``
     - ``str``
     - required
     - Public record field.
   * - ``controller``
     - ``str``
     - required
     - Public record field.
   * - ``default``
     - ``float``
     - required
     - Public record field.
   * - ``sample_value``
     - ``float``
     - required
     - Public record field.
   * - ``shape_deltas``
     - ``dict[str, dict[int, Point]]``
     - required
     - Public record field.

.. py:function:: maya_property_aliases(name)

   Return unambiguous textual aliases commonly used for a Maya plug.

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

.. py:function:: deforming_property_rows(report)

   Deforming property rows.

   **Return type:** ``list[dict[str, Any]]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``report``
     - ``Mapping[str, Any]``
     - ``required``
     - Explicit report for this operation; preserve the matching graph/program/scene data contract.

.. py:function:: inferred_character_root(report)

   Inferred character root.

   **Return type:** ``str | None``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``report``
     - ``Mapping[str, Any]``
     - ``required``
     - Explicit report for this operation; preserve the matching graph/program/scene data contract.

.. py:function:: missing_property_rows(report, graph)

   Missing property rows.

   **Return type:** ``list[dict[str, Any]]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``report``
     - ``Mapping[str, Any]``
     - ``required``
     - Explicit report for this operation; preserve the matching graph/program/scene data contract.
   * - ``graph``
     - ``Mapping[str, Any] | None``
     - ``required``
     - Parsed ORG/legacy graph mapping; use the format expected by this entry point.

.. py:function:: evaluate_maya(cmds)

   Evaluate maya.

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

.. py:function:: reset_property_defaults(cmds, report)

   Reset property defaults.

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
   * - ``report``
     - ``Mapping[str, Any]``
     - ``required``
     - Explicit report for this operation; preserve the matching graph/program/scene data contract.

.. py:function:: rebase_property_defaults(cmds, report)

   Shift measured controller intervals onto the scene's initialized state.

   **Return type:** ``tuple[dict[str, Any], list[dict[str, str]]]``.

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
   * - ``report``
     - ``Mapping[str, Any]``
     - ``required``
     - Explicit report for this operation; preserve the matching graph/program/scene data contract.

.. py:function:: capture_sampled_morph_targets(cmds, shapes, shape_points, neutral_points, report, graph, *, tolerance=1e-08)

   Capture missing measured controllers and augment a graph with v1 primitives.

   **Return type:** ``tuple[list[SampledMorphTarget], dict[str, Any], dict[str, Any]]``.

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
   * - ``shapes``
     - ``Sequence[str]``
     - ``required``
     - Explicit shapes for this operation; preserve the matching graph/program/scene data contract.
   * - ``shape_points``
     - ``Callable[[str], Sequence[Point]]``
     - ``required``
     - Ordered XYZ point data; retain vertex identity, topology, coordinate space, and units.
   * - ``neutral_points``
     - ``ShapePoints``
     - ``required``
     - Ordered XYZ point data; retain vertex identity, topology, coordinate space, and units.
   * - ``report``
     - ``Mapping[str, Any]``
     - ``required``
     - Explicit report for this operation; preserve the matching graph/program/scene data contract.
   * - ``graph``
     - ``Mapping[str, Any] | None``
     - ``required``
     - Parsed ORG/legacy graph mapping; use the format expected by this entry point.
   * - ``tolerance``
     - ``float``
     - ``1e-08``
     - Explicit acceptance threshold in the compared output's declared units.
