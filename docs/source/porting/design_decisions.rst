Hypothetical porting design decisions
=====================================

These are invented teaching situations. They describe representation choices,
not a source plug-in's implementation or provenance.

A fictional response node
-------------------------

Suppose two numeric controls produce a scalar response. Reuse arithmetic and
clamping for a documented bounded sum, or a curve for an authored response.
If only observations are available, decide whether a sampled/fitted contract is
acceptable for the intended domain. Test unseen interiors and combinations;
agreement on a small fitted sample set is not general equivalence. A special
source-specific wrapper is not a reusable public primitive.

A fictional transform driver
-----------------------------

Suppose a driver produces orientation/translation relative to a parent. Identify
spaces, units, rotate order, offsets, and live inputs. Reuse matrix/quaternion
or constraint primitives when they express the relation. An untraceable parent
input is a blocker, not a constant equal to the current observed matrix.

If a reusable behavior remains unrepresentable, specify typed inputs/outputs,
domain, degeneracy policy, and independent fixtures before adding a node.
Do not derive a public explanation from a source-specific algorithm.

A fictional attachment
-----------------------

Use a surface attachment contract only when topology, space, frame interpolation,
and input ownership match the intended behavior. Test seams and temporal
changes. Do not add a special node to conceal mismatched frames or missing
upstream geometry.

A fictional playback workflow
------------------------------

Keep editable curves and define live/cached boundaries. Relevant edits invalidate
the cache; rebuilding restores validity. A switch selects a stream but cannot
prove cache freshness. Deliver mode, reload, interpolation, and invalidation
rules with the package.

When to create a node
---------------------

Require a useful behavior independent of one asset, explicit typed interfaces,
units/spaces, valid domain, resource/state ownership, predictable errors, and
independent tests. Separate exporter responsibility from runtime responsibility.
Explain why existing representations fail the required contract rather than
justifying support through one animation or fitted sample centers.
