.. _node-reverse:

reverse
=======

Compute 1 - input independently for each component.

**Layer:** portable graph node. **Contract:** Exact numeric primitive.

**Aliases:** none.

When to use
-----------

Use to complement a blend weight or channel without adding a condition.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - inputX / inputY / inputZ (or input)
     - number endpoints
     - 0
     - Component channels; a static input vector supplies defaults.

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
   * - outputX / outputY / outputZ
     - number
     - computed
     - Independent component results.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/reverse.json>`.

.. literalinclude:: ../../../examples/graph/reverse.json
   :language: json

.. code-block:: console

   orgctl eval examples/graph/reverse.json --output json

Expected ``result``: **0.75**, absolute tolerance ``1e-05``.

Limits and porting notes
------------------------

Preserve the declared input/output types, source units, and domain. Semantic validation is performed by the runtime compiler, not only the structural JSON schema.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
