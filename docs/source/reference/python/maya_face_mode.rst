openriggraph.maya_face_mode
===========================

.. py:module:: openriggraph.maya_face_mode

**Environment:** Maya Python for scene operations; pure numeric helpers may run in ordinary Python.

Use keyword arguments when supplied; preserve the source function's declared coordinate spaces, logical indices, and path ownership. Read the :doc:`porting workflow <../../porting/agent_workflow>` for orchestration.

.. py:function:: set_face_evaluation_mode(live, *, cmds=None, allow_invalid_cache=False)

   Select live authoring or cached scrub evaluation.

   **Return type:** ``dict[str, Any]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``live``
     - ``bool``
     - ``required``
     - Choose the live authoring path; cached playback requires validated current cache data.
   * - ``cmds``
     - ``Any | None``
     - ``None``
     - Maya commands-compatible interface, or the SDK snapshot adapter where supported.
   * - ``allow_invalid_cache``
     - ``bool``
     - ``False``
     - Explicit override for cache validity handling; normal authoring must invalidate/rebuild stale caches.

.. py:function:: rebuild_face_output_cache(*, cmds=None, start=None, end=None, path=None)

   Capture the current authored facial evaluator and return to scrub mode.

   **Return type:** ``dict[str, Any]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``cmds``
     - ``Any | None``
     - ``None``
     - Maya commands-compatible interface, or the SDK snapshot adapter where supported.
   * - ``start``
     - ``int | None``
     - ``None``
     - Declared capture/evaluation interval boundary in the source time convention.
   * - ``end``
     - ``int | None``
     - ``None``
     - Declared capture/evaluation interval boundary in the source time convention.
   * - ``path``
     - ``str | Path | None``
     - ``None``
     - Filesystem path for path; use the caller's scene/package/SDK root and preserve relocation requirements.
