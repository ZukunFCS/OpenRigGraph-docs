.. _node-choice:

choice
======

Select an indexed input using a numeric selector.

**Layer:** portable graph node. **Contract:** Exact numeric primitive.

**Aliases:** none.

When to use
-----------

Use for discrete routing; preserve logical input indices and validate nonintegral/out-of-range selections.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - selector
     - number endpoint
     - 0
     - Selected logical index.
   * - input[i]
     - indexed number endpoint
     - 0
     - Candidate inputs; vector children can be lowered component-wise.

Parameters
----------

No additional fields.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - output
     - number
     - computed
     - Scalar result.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/choice.json>`.

.. literalinclude:: ../../../examples/graph/choice.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/choice.json --output json

Expected ``result``: **7**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
