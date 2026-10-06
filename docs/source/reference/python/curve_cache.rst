openriggraph.curve_cache
========================

.. py:module:: openriggraph.curve_cache

**Environment:** Ordinary Python; vertex/array workflows may require NumPy.

Use keyword arguments when supplied; preserve the source function's declared coordinate spaces, logical indices, and path ownership. Read the :doc:`porting workflow <../../porting/agent_workflow>` for orchestration.

.. py:class:: CurveCacheMetadata

   Curve cache metadata.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``sample_count``
     - ``int``
     - required
     - Public record field.
   * - ``value_count``
     - ``int``
     - required
     - Public record field.
   * - ``first_frame``
     - ``float``
     - required
     - Public record field.
   * - ``last_frame``
     - ``float``
     - required
     - Public record field.

.. py:function:: write_curve_cache(path, frames, values)

   Write a dense, frame-major double-precision ORG controller cache.

   **Return type:** ``CurveCacheMetadata``.

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
   * - ``frames``
     - ``Sequence[float]``
     - ``required``
     - Strictly increasing sample coordinates; align one value row per coordinate.
   * - ``values``
     - ``Sequence[Sequence[float]]``
     - ``required``
     - Numeric values in the declared row/channel order; retain the required cardinality.

.. py:function:: write_curve_cache_stream(path, frames, values)

   Write rows incrementally so whole-animation caches stay bounded in RAM.

   **Return type:** ``CurveCacheMetadata``.

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
   * - ``frames``
     - ``Sequence[float]``
     - ``required``
     - Strictly increasing sample coordinates; align one value row per coordinate.
   * - ``values``
     - ``Iterable[Sequence[float]]``
     - ``required``
     - Numeric values in the declared row/channel order; retain the required cardinality.

.. py:function:: read_curve_cache_metadata(path)

   Read and validate the fixed-size cache header and frame range.

   **Return type:** ``CurveCacheMetadata``.

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

.. py:function:: read_curve_cache_row(path, sample_index)

   Read one frame-major row for diagnostics without loading the cache.

   **Return type:** ``tuple[float, ...]``.

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
   * - ``sample_index``
     - ``int``
     - ``required``
     - Zero-based sample row index bounded by metadata.sample_count.

.. py:function:: compress_curve_cache(source_path, destination_path, *, chunk_frames=128)

   Convert a dense v1 cache to an exact constant/dynamic-channel v2 cache.

   **Return type:** ``dict[str, int | float]``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``source_path``
     - ``str | Path``
     - ``required``
     - Filesystem path for source path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``destination_path``
     - ``str | Path``
     - ``required``
     - Filesystem path for destination path; use the caller's scene/package/SDK root and preserve relocation requirements.
   * - ``chunk_frames``
     - ``int``
     - ``128``
     - Positive streaming chunk size; changes memory/work grouping, not output semantics.
