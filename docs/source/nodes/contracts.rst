Shared graph-node contracts
===========================

Endpoints and values
--------------------

Inputs resolve numbers, controller names, node.outputPin strings, or explicit
endpoint objects. Matrix/vector values use declared channels; supported matrix
consumers can accept a whole-matrix endpoint. Do not assume all Maya compound
plugs are universally supported. Logical array indices remain significant.

Use inputs for live endpoints and params for static configuration. The parser
also merges unreserved top-level node fields into params. Canonical aliases are
listed in :doc:`index`. Compilation is demand-driven from declared outputs;
exercise every required output rather than relying on unused nodes' presence.

Units and precision
-------------------

Matrices are row-major, use row vectors, and store translation in elements
12..14. A matrix is sixteen values. Vector/quaternion component order is XYZ/XYZW.
Transform/quaternion nodes use degrees when their anglesInDegrees contract
defaults true. angleBetween and scalar trigonometry return/use radians.
Maya typed angles use internal radians and distances use centimeters.
Curve numeric units must be exported explicitly.

Float and double C entry points coexist. A double interface does not guarantee
all kernels/parameter paths preserve arbitrary precision. Verify sensitive
transforms and delivered deformation. Test finite values, zero weights/scales,
division by zero, zero vectors, coincident aims, singular matrices, repeated
curve coordinates, and degenerate geometry if they belong to the required domain.

Support claims
--------------

Exact primitives evaluate defined formulas. Scoped nodes require documented
basis/topology/settings and source parity. RBF/model/sampled nodes evaluate
declared representations; their approximation quality is separate evidence.
External operators require provider/resource bindings. orgctl validate checks
semantic compilation, not DCC behavior or final character geometry.
