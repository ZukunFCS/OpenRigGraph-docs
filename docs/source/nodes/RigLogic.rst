.. _node-RigLogic:

RigLogic
========

Declare a resource-backed external operator with an explicit scalar interface.

**Layer:** portable graph node. **Contract:** External provider required.

**Aliases:** none.

When to use
-----------

Use only when the embedding application supplies the matching provider and resource. ORG itself does not implement the resource's solver.

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - interface.inputs names
     - number endpoints
     - all required
     - Ordered provider inputs.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - interface
     - object with string[] inputs/outputs
     - required
     - Outputs must be nonempty and match requested output pins.
   * - resource
     - string
     - required
     - Name of a declared graph resource, bound by the embedding context.

Outputs
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Name
     - Type
     - Default
     - Meaning
   * - interface.outputs names
     - number
     - provider-defined
     - Provider output lanes.

Usage and verification
----------------------

Download :download:`the complete synthetic graph <../../../examples/graph/RigLogic.json>`.

.. literalinclude:: ../../../examples/graph/RigLogic.json
   :language: json

``orgctl validate`` can check this contract. Evaluation needs a registered provider; use the :doc:`identity-provider example <../reference/c_api>` rather than expecting the unextended CLI to execute it.

Limits and porting notes
------------------------

See the independent identity-provider C example. The CLI cannot evaluate this graph without a provider; missing-provider failure is expected, not a builtin implementation.

See :doc:`common contracts <contracts>` for endpoint syntax, numeric domains, units, and error handling.
