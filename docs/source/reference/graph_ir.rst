Graph IR and binary compatibility
=================================

The structural JSON schema is downloadable as
:download:`openriggraph.schema.json <../../../schemas/openriggraph.schema.json>`.
``orgctl validate`` remains the semantic compiler/validator. The schema allows
node-specific parameters; passing it alone is not proof of runtime support.

Top-level contract
------------------

.. list-table::
   :header-rows: 1

   * - Field
     - Type
     - Meaning
   * - version / format
     - integer / string
     - Supported Graph IR versions are 1 and 2; format is OpenRigGraph.
   * - controllers
     - controller-record[]
     - Stable names, defaults, min/max, optional clamp, optional UI metadata.
   * - nodes
     - node-record[] or name-keyed object
     - Type, inputs, static parameters, and optional private working provenance.
   * - connections
     - connection-record[]
     - Explicit src/source and dst/destination endpoint connections.
   * - outputs / output_map
     - records / keyed mapping
     - Output name/source plus semantic kind, indices, component/space/mode.
   * - resources
     - resource-record[]
     - Named typed resources for supported external operator interfaces.
   * - mappings / interaction_groups
     - record[]
     - Supported legacy sampled migration inputs; prefer explicit current nodes.

An endpoint may be a number, controller name, node.pin string, or object with
const/value, control, node/output, or source. A node has name/type, live inputs,
params, and optional provenance. The node reference records accepted aliases;
unreserved top-level fields are merged into params by the loader.

Output kinds include scalar, blendshape/morph, pose/joint, joint_center, and
animated_map. Preserve declared target/joint/component indexing and supported
space/mode semantics. Output naming/order is a consumer contract, not a string
to recover later by guessing. Controllers with clamp enabled are limited before
evaluation; preserve signed/unbounded domains when the source requires them.

Resources and compiled modules
-------------------------------

Graph IR v2 carries typed named resources and external operator declarations.
The embedding context binds resource bytes and registers providers. A graph
declaring an external operator can compile without an executable provider, but
instance creation/evaluation requires the dependency. See :doc:`embedding`.

``orgctl compile`` writes a versioned ORGB module. The current source declares
compiled-module format maximum version **16** and provider ABI version **1**;
the serializer may choose a lower required format for a simpler graph. Graph IR
version, binary format, provider ABI, runtime package version, and documentation
release version are different values. Use loader errors rather than assuming
all .orgb files are interchangeable. The SDK runtime package version is 0.1.0
for this API snapshot.
