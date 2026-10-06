openriggraph.face_capture
=========================

.. py:module:: openriggraph.face_capture

**Environment:** Ordinary Python; vertex/array workflows may require NumPy.

Use keyword arguments when supplied; preserve the source function's declared coordinate spaces, logical indices, and path ownership. Read the :doc:`porting workflow <../../porting/agent_workflow>` for orchestration.

.. py:class:: FaceParityStats

   Face parity stats.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``component_count``
     - ``int``
     - required
     - Public record field.
   * - ``rms_cm``
     - ``float``
     - required
     - Public record field.
   * - ``max_cm``
     - ``float``
     - required
     - Public record field.
   * - ``passed``
     - ``bool``
     - required
     - Public record field.

.. py:function:: compare_face_points(actual, expected, rms_limit_cm=FACE_RMS_LIMIT_CM, max_limit_cm=FACE_MAX_LIMIT_CM)

   Compare final XYZ components using the user-approved visible-face gate.

   **Return type:** ``FaceParityStats``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``actual``
     - ``Sequence[float]``
     - ``required``
     - Candidate values to compare against expected reference observations.
   * - ``expected``
     - ``Sequence[float]``
     - ``required``
     - Reference/oracle values in the same order, space, and units as actual.
   * - ``rms_limit_cm``
     - ``float``
     - ``FACE_RMS_LIMIT_CM``
     - RMS point-error threshold in centimeters.
   * - ``max_limit_cm``
     - ``float``
     - ``FACE_MAX_LIMIT_CM``
     - Maximum point-error threshold in centimeters.

.. py:class:: FaceCaptureLayout

   Face capture layout.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``source_vertices``
     - ``tuple[int, ...]``
     - required
     - Public record field.
   * - ``visible_vertices``
     - ``tuple[int, ...]``
     - required
     - Public record field.
   * - ``visibility_count``
     - ``int``
     - required
     - Public record field.
   * - ``input_count``
     - ``int``
     - required
     - Public record field.
   * - ``control_count``
     - ``int``
     - required
     - Public record field.
   * - ``influence_count``
     - ``int``
     - required
     - Public record field.

.. py:property:: FaceCaptureLayout.values_per_frame

   Values per frame.

   **Return type:** ``int``.

.. py:property:: FaceCaptureLayout.source_value_count

   Source value count.

   **Return type:** ``int``.

.. py:property:: FaceCaptureLayout.visible_value_count

   Visible value count.

   **Return type:** ``int``.

.. py:class:: FaceFrame

   Face frame.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``frame``
     - ``int``
     - required
     - Public record field.
   * - ``values``
     - ``array.array``
     - required
     - Public record field.
   * - ``layout``
     - ``FaceCaptureLayout``
     - required
     - Public record field.

.. py:property:: FaceFrame.source_points

   Source points.

   **Return type:** ``memoryview``.

.. py:property:: FaceFrame.visible_points

   Visible points.

   **Return type:** ``memoryview``.

.. py:property:: FaceFrame.visibility

   Visibility.

   **Return type:** ``memoryview``.

.. py:property:: FaceFrame.control_values

   Control values.

   **Return type:** ``memoryview``.

.. py:property:: FaceFrame.control_matrices

   Control matrices.

   **Return type:** ``memoryview``.

.. py:property:: FaceFrame.influence_matrices

   Influence matrices.

   **Return type:** ``memoryview``.

.. py:function:: load_static_capture(root)

   Load static capture.

   **Return type:** ``dict``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``root``
     - ``Path``
     - ``required``
     - Filesystem path for root; use the caller's scene/package/SDK root and preserve relocation requirements.

.. py:function:: capture_layout(document)

   Capture layout.

   **Return type:** ``FaceCaptureLayout``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``document``
     - ``dict``
     - ``required``
     - Explicit document for this operation; preserve the matching graph/program/scene data contract.

.. py:function:: iter_capture_frames(root)

   Iter capture frames.

   **Return type:** ``Iterator[FaceFrame]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``root``
     - ``Path``
     - ``required``
     - Filesystem path for root; use the caller's scene/package/SDK root and preserve relocation requirements.

.. py:function:: validate_capture(root, require_complete=True)

   Validate capture.

   **Return type:** ``dict``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``root``
     - ``Path``
     - ``required``
     - Filesystem path for root; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``require_complete``
     - ``bool``
     - ``True``
     - Reject incomplete capture/output coverage rather than silently accepting a partial package.

.. py:function:: compile_face_package(capture_root, output)

   Compile immutable facial topology/deformer data into a runtime package.

   **Return type:** ``dict``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``capture_root``
     - ``Path``
     - ``required``
     - Root directory of a prepared capture, including required static and frame data.
   * - ``output``
     - ``Path``
     - ``required``
     - Explicit output for this operation; preserve the matching graph/program/scene data contract.

.. py:function:: route_face_points_into_skin_packages(capture_root, skin_export_root, output, packed_base_index=None)

   Route packed ORG facial points directly into first-layer skin passes.

   **Return type:** ``dict``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``capture_root``
     - ``Path``
     - ``required``
     - Root directory of a prepared capture, including required static and frame data.
   * - ``skin_export_root``
     - ``Path``
     - ``required``
     - Explicit skin export root for this operation; preserve the matching graph/program/scene data contract.
   * - ``output``
     - ``Path``
     - ``required``
     - Explicit output for this operation; preserve the matching graph/program/scene data contract.
   * - ``packed_base_index``
     - ``int | None``
     - ``None``
     - Base scalar offset into the declared packed layout.
