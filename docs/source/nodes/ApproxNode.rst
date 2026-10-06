.. _node-ApproxNode:

ApproxNode
==========

Evaluate a deterministic sparse-linear output model.

**Layer:** portable graph node. **Contract:** Validated model contract.

**Aliases:** none.

When to use
-----------

Use for a compact affine response only after separate verification over the declared input domain.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - declared input names
     - number endpoints
     - required by terms
     - Named model features.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - backend
     - string
     - sparse_linear
     - Only sparse_linear is supported.
   * - outputs
     - named output-record object
     - required
     - Each output contains bias and weights or terms; terms contain input/weight.
   * - provenance
     - object
     - exporter requirement
     - Record domain, fit/validation split, sample counts, and error metrics in private port artifacts.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - declared output names
     - number
     - computed
     - bias + sum(weight * input).

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/ApproxNode.json>`.

.. literalinclude:: ../../../examples/graph/ApproxNode.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/ApproxNode.json --output json

Expected ``result``: **7**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

ApproxNode shares the sparse-linear compiler path. Neither name proves approximation quality; report residuals on held-out observations.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
