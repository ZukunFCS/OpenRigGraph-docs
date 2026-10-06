openriggraph.maya_curve
=======================

.. py:module:: openriggraph.maya_curve

**Environment:** Maya Python for scene operations; pure numeric helpers may run in ordinary Python.

Use keyword arguments when supplied; preserve the source function's declared coordinate spaces, logical indices, and path ownership. Read the :doc:`porting workflow <../../porting/agent_workflow>` for orchestration.

.. py:function:: evaluate_native_curve(curve, x)

   Evaluate native curve.

   **Return type:** ``float``.

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - ``curve``
     - ``Mapping[str, Any]``
     - ``required``
     - Explicit curve for this operation; preserve the matching graph/program/scene data contract.
   * - ``x``
     - ``float``
     - ``required``
     - Explicit x for this operation; preserve the matching graph/program/scene data contract.
