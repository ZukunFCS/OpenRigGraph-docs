openriggraph.vertex_parity
==========================

.. py:module:: openriggraph.vertex_parity

**Environment:** Ordinary Python; vertex/array workflows may require NumPy.

Use keyword arguments when supplied; preserve the source function's declared coordinate spaces, logical indices, and path ownership. Read the :doc:`porting workflow <../../porting/agent_workflow>` for orchestration.

.. py:class:: ControllerSpec

   Controller spec.

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
   * - ``default``
     - ``float``
     - required
     - Public record field.
   * - ``minimum``
     - ``float``
     - required
     - Public record field.
   * - ``maximum``
     - ``float``
     - required
     - Public record field.

.. py:property:: ControllerSpec.validation_value

   Validation value.

   **Return type:** ``float``.

.. py:class:: PrimitiveVertices

   Primitive vertices.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``mesh_name``
     - ``str``
     - required
     - Public record field.
   * - ``primitive_index``
     - ``int``
     - required
     - Public record field.
   * - ``positions``
     - ``tuple[tuple[float, float, float], ...]``
     - required
     - Public record field.
   * - ``uvs``
     - ``tuple[tuple[float, float], ...]``
     - required
     - Public record field.
   * - ``maya_source_shape``
     - ``str``
     - ''
     - Public record field.
   * - ``maya_source_vertex_indices``
     - ``tuple[int, ...]``
     - ()
     - Public record field.

.. py:class:: GlbGeometry

   Glb geometry.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``primitives``
     - ``tuple[PrimitiveVertices, ...]``
     - required
     - Public record field.
   * - ``centroid``
     - ``tuple[float, float, float]``
     - required
     - Public record field.
   * - ``normalization_scale``
     - ``float``
     - required
     - Public record field.

.. py:property:: GlbGeometry.vertex_count

   Vertex count.

   **Return type:** ``int``.

.. py:property:: GlbGeometry.positions

   Positions.

   **Return type:** ``tuple[tuple[float, float, float], ...]``.

.. py:function:: renderer_normalization(positions)

   Match Vaper's sequential glm::vec3 float normalization exactly.

   **Return type:** ``tuple[tuple[float, float, float], float]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``positions``
     - ``Sequence[Sequence[float]]``
     - ``required``
     - Ordered XYZ point data; retain vertex identity, topology, coordinate space, and units.

.. py:function:: controller_specs(graph)

   Controller specs.

   **Return type:** ``list[ControllerSpec]``.

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

.. py:function:: read_glb(path)

   Read glb.

   **Return type:** ``tuple[dict[str, Any], bytes]``.

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

.. py:function:: embedded_graph(root)

   Embedded graph.

   **Return type:** ``dict[str, Any]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``root``
     - ``Mapping[str, Any]``
     - ``required``
     - Filesystem path for root; use the caller's scene/package/SDK root and preserve relocation requirements.

.. py:function:: load_glb_geometry(path)

   Load glb geometry.

   **Return type:** ``GlbGeometry``.

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

.. py:function:: read_text_points(path)

   Read text points.

   **Return type:** ``list[tuple[float, float, float]]``.

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

.. py:function:: read_binary_points(path)

   Read binary points.

   **Return type:** ``list[tuple[float, float, float]]``.

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

.. py:function:: normalize_points(points, centroid, scale)

   Normalize points.

   **Return type:** ``list[tuple[float, float, float]]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``points``
     - ``Iterable[Sequence[float]]``
     - ``required``
     - Ordered XYZ point data; retain vertex identity, topology, coordinate space, and units.
   * - ``centroid``
     - ``Sequence[float]``
     - ``required``
     - Explicit centroid for this operation; preserve the matching graph/program/scene data contract.
   * - ``scale``
     - ``float``
     - ``required``
     - Explicit scale for this operation; preserve the matching graph/program/scene data contract.

.. py:function:: compare_point_arrays(expected, actual, tolerance, *, worst_limit=20)

   Compare point arrays.

   **Return type:** ``dict[str, Any]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``expected``
     - ``Sequence[Sequence[float]]``
     - ``required``
     - Reference/oracle values in the same order, space, and units as actual.
   * - ``actual``
     - ``Sequence[Sequence[float]]``
     - ``required``
     - Candidate values to compare against expected reference observations.
   * - ``tolerance``
     - ``float``
     - ``required``
     - Explicit acceptance threshold in the compared output's declared units.
   * - ``worst_limit``
     - ``int``
     - ``20``
     - Worst-case residual limit in the comparison's declared units.

.. py:function:: compare_deformation_deltas(maya_neutral, maya_posed, runtime_neutral, runtime_posed, normalization_scale, tolerance, *, worst_limit=20)

   Compare deformation deltas.

   **Return type:** ``dict[str, Any]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``maya_neutral``
     - ``Sequence[Sequence[float]]``
     - ``required``
     - Ordered point observations for the named source/evaluation state; compare in a common space.
   * - ``maya_posed``
     - ``Sequence[Sequence[float]]``
     - ``required``
     - Ordered point observations for the named source/evaluation state; compare in a common space.
   * - ``runtime_neutral``
     - ``Sequence[Sequence[float]]``
     - ``required``
     - Ordered point observations for the named source/evaluation state; compare in a common space.
   * - ``runtime_posed``
     - ``Sequence[Sequence[float]]``
     - ``required``
     - Ordered point observations for the named source/evaluation state; compare in a common space.
   * - ``normalization_scale``
     - ``float``
     - ``required``
     - Explicit normalization scale for this operation; preserve the matching graph/program/scene data contract.
   * - ``tolerance``
     - ``float``
     - ``required``
     - Explicit acceptance threshold in the compared output's declared units.
   * - ``worst_limit``
     - ``int``
     - ``20``
     - Worst-case residual limit in the comparison's declared units.
