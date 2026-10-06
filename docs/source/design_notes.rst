Runtime design
==============

Graph IR is the portable interchange/debugging representation. Compilation
resolves endpoints, orders required dependencies, lowers operations, and produces
an evaluation module. Instances own mutable controls and output state. Compile
once for repeated evaluation and inspect lowered instructions when tracing errors.

The runtime owns explicit contracts; exporters own DCC discovery, extraction,
unit/space adaptation, and validation against the source. Maya integration nodes
bridge numeric/packed/geometry boundaries without implying full-DG compatibility.
External operators supply their behavior through registered providers/resources.

Exact primitives, scoped behaviors, and sampled/fitted representations coexist.
Their error evidence and dependency boundaries remain explicit. See
:doc:`porting/design_decisions` for invented representation decisions and
:doc:`reference/embedding` for library ownership.
