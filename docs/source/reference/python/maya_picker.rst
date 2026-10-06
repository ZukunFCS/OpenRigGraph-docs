openriggraph.maya_picker
========================

.. py:module:: openriggraph.maya_picker

**Environment:** Maya Python for scene operations; pure numeric helpers may run in ordinary Python.

Use keyword arguments when supplied; preserve the source function's declared coordinate spaces, logical indices, and path ownership. Read the :doc:`porting workflow <../../porting/agent_workflow>` for orchestration.

.. py:class:: PickerTarget

   One picker-visible Maya object and the buttons that reference it.

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
   * - ``domains``
     - ``set[str]``
     - field(default_factory=set)
     - Public record field.
   * - ``button_ids``
     - ``set[str]``
     - field(default_factory=set)
     - Public record field.

.. py:method:: PickerTarget.to_dict(self)

   To dict.

   **Return type:** ``dict[str, object]``.

.. py:function:: parse_picker_targets(path, domain)

   Read comma-separated ``select`` targets from an XML picker file.

   **Return type:** ``tuple[list[PickerTarget], int]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``path``
     - ``str | Path``
     - ``required``
     - Filesystem path for path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``domain``
     - ``str``
     - ``required``
     - Explicit authored/sampling domain; do not infer it solely from observed animation correlations.

.. py:function:: merge_picker_targets(groups)

   Merge targets from multiple picker domains without losing provenance.

   **Return type:** ``list[PickerTarget]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``groups``
     - ``Iterable[Sequence[PickerTarget]]``
     - ``required``
     - Explicit groups for this operation; preserve the matching graph/program/scene data contract.
