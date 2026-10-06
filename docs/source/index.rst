OpenRigGraph documentation
==========================

OpenRigGraph (ORG) is a renderer-neutral graph interchange and compiled runtime
for portable character evaluation. Exporters translate supported source behavior
into explicit numeric, transform, curve, surface, and scoped geometry contracts.

Start with :doc:`getting_started`, or give an agent
:doc:`porting/agent_workflow` and a source scene plus the required SDK.
ORG is not an automatic evaluator for every Maya dependency graph node.

This reference covers **59 graph types, 7 aliases, and 14 Maya integration
types**, plus the C, Python, and command-line APIs. Runtime support, exporter
coverage, and verified source parity are distinct claims.

.. toctree::
   :maxdepth: 2
   :caption: Start here

   getting_started
   porting/index
   agents/index

.. toctree::
   :maxdepth: 2
   :caption: API reference

   nodes/index
   maya/index
   reference/index

.. toctree::
   :maxdepth: 1
   :caption: Design and release

   porting/design_decisions
   design_notes
   release

Machine-readable documentation
------------------------------

Download the :download:`node and API catalog <_generated/node_catalog.json>`.
The documentation repository supplies ``llms.txt`` and ``llms-full.txt`` for
agents and independent examples under ``examples/``.
