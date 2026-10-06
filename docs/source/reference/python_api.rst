Python API
==========

These source-neutral APIs are available with the ORG SDK Python directory on ``PYTHONPATH``. Maya-dependent calls require execution inside the matching Maya Python runtime. Private/project adapters and underscored implementation helpers are excluded.

Signatures are extracted without importing modules or Maya. Annotation types are shown as literal text; optional dependencies are listed per module.

.. toctree::
   :maxdepth: 1

   python/curve_cache
   python/face_capture
   python/maya_blendshape
   python/maya_bridge
   python/maya_curve
   python/maya_face_mode
   python/maya_picker
   python/maya_runtime
   python/maya_scene_repair
   python/maya_snapshot
   python/sampled_morph
   python/vertex_parity

Package exports
---------------

The following names are also exported from ``openriggraph``:

* ``classify_rig_logic_graph``
* ``lower_legacy_graph_to_openriggraph``
* ``lower_open_maya_blendshape_graph_to_openriggraph``
* ``FaceCaptureLayout``
* ``FaceFrame``
* ``FaceParityStats``
* ``compare_face_points``
* ``compile_face_package``
* ``iter_capture_frames``
* ``route_face_points_into_skin_packages``
* ``validate_capture``
* ``wire_openriggraph_evaluator``
* ``CurveCacheMetadata``
* ``read_curve_cache_metadata``
* ``read_curve_cache_row``
* ``write_curve_cache``
* ``write_curve_cache_stream``

Runnable cache example
----------------------

Download :download:`cache_roundtrip.py <../../../examples/python/cache_roundtrip.py>`. It verifies dense and sparse representations using independent numeric rows. Sparse compression requires NumPy in the Python environment running the example.

.. code-block:: console

   python -m pip install numpy
   python examples/python/cache_roundtrip.py --sdk-python /path/to/sdk/python
