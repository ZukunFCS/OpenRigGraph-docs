openriggraph.maya_blendshape
============================

.. py:module:: openriggraph.maya_blendshape

**Environment:** Maya Python for scene operations; pure numeric helpers may run in ordinary Python.

Use keyword arguments when supplied; preserve the source function's declared coordinate spaces, logical indices, and path ownership. Read the :doc:`porting workflow <../../porting/agent_workflow>` for orchestration.

.. py:class:: SparseTarget

   Sparse target.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``full_weight``
     - ``float``
     - required
     - Public record field.
   * - ``indices``
     - ``tuple[int, ...]``
     - required
     - Public record field.
   * - ``deltas``
     - ``tuple[Point, ...]``
     - required
     - Public record field.

.. py:class:: TargetGroup

   Target group.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``weight_index``
     - ``int``
     - required
     - Public record field.
   * - ``targets``
     - ``tuple[SparseTarget, ...]``
     - required
     - Public record field.
   * - ``target_weights``
     - ``Mapping[int, float]``
     - required
     - Public record field.

.. py:class:: BlendBase

   Blend base.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``base_index``
     - ``int``
     - required
     - Public record field.
   * - ``points``
     - ``tuple[Point, ...]``
     - required
     - Public record field.
   * - ``groups``
     - ``tuple[TargetGroup, ...]``
     - required
     - Public record field.
   * - ``base_weights``
     - ``Mapping[int, float]``
     - required
     - Public record field.

.. py:class:: BlendShapeProgram

   Blend shape program.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``envelope``
     - ``float``
     - required
     - Public record field.
   * - ``support_negative_weights``
     - ``bool``
     - required
     - Public record field.
   * - ``bases``
     - ``tuple[BlendBase, ...]``
     - required
     - Public record field.

.. py:function:: expand_vertex_components(components)

   Expand vertex components.

   **Return type:** ``tuple[int, ...]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``components``
     - ``Iterable[str]``
     - ``required``
     - Explicit components for this operation; preserve the matching graph/program/scene data contract.

.. py:function:: compile_program(capture)

   Compile program.

   **Return type:** ``BlendShapeProgram``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``capture``
     - ``Mapping[str, Any]``
     - ``required``
     - Source capture mapping; validate its layout and declared schema before compilation.

.. py:function:: evaluate_base(program, base, weights)

   Evaluate base.

   **Return type:** ``list[list[float]]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``program``
     - ``BlendShapeProgram``
     - ``required``
     - Prepared numeric program produced by the matching compile function.
   * - ``base``
     - ``BlendBase``
     - ``required``
     - Explicit base for this operation; preserve the matching graph/program/scene data contract.
   * - ``weights``
     - ``Sequence[float]``
     - ``required``
     - Numeric weights in the program's declared target/influence order.

.. py:function:: evaluate(program, weights)

   Evaluate.

   **Return type:** ``list[list[list[float]]]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``program``
     - ``BlendShapeProgram``
     - ``required``
     - Prepared numeric program produced by the matching compile function.
   * - ``weights``
     - ``Sequence[float]``
     - ``required``
     - Numeric weights in the program's declared target/influence order.
