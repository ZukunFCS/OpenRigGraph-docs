Embedding lifecycle and errors
==============================

Load, compile, instantiate, evaluate
------------------------------------

1. Load JSON with ``org_graph_load_json``. Check null and the error buffer.
2. Validate and inspect diagnostics. Compile a module once, using the context
   and options entry points when resources/providers or an explicit backend
   are required.
3. Create an instance for mutable controls and evaluated output state.
4. Set controls by stable name/index, or a shape-matched bulk array. Evaluate,
   check status, then read/copy the evaluated outputs.
5. Destroy instances, modules, graphs, and contexts after their dependent work
   is finished. Copy handle-owned strings before releasing the owner.

Use a distinct instance for each independent mutable evaluation stream. Do not
mutate/evaluate one instance concurrently; this documentation does not promise
thread-safe shared mutation. A module is compiled evaluation data, not current
control/output state. Reusing the module avoids repeated JSON parsing/compilation.

Status and buffers
------------------

Check every status-returning call against ``ORG_STATUS_OK``. Pointer-returning
creation/load calls can return null. Supply a writable error buffer and its
actual size where the signature asks for one. Graph diagnostics explain semantic
compilation failures; instance errors explain evaluation failures. A successful
compile does not prove source-scene parity.

Counts bound array/index access. Bulk controls/outputs must match the module's
declared cardinality; introspection queries expose controller/output names,
defaults, ranges, clamp flags, output kind, and lowered instructions. Do not
depend on out-of-bounds getter fallback values as an application contract.

Contexts and external providers
-------------------------------

A provider has ABI version, user data, and create/destroy/evaluate callbacks.
Register it for the graph operator type and bind resources by declared name and
type. Callbacks receive ordered scalar lanes and a resource view. The provider
must implement its own solver/resource behavior and return a status on failure.
The :doc:`identity example <c_api>` is independent and exercises this boundary.

Retain provider user data and callback code for all dependent instances. Resource
binding copies the bytes into the context and computes SHA-256; a supplied hash
must match. The resource view handed to create is temporary: copy any needed
resource data into provider state rather than retaining the view's pointers.
Instances borrow their compiled module, so the module must outlive every instance.
Callback user data remains application-owned and must remain valid until provider
instances are destroyed.

Compilation and persistence
---------------------------

Set ``org_compile_options.struct_size`` to ``sizeof(org_compile_options)`` and
choose ``ORG_COMPILE_BACKEND_NATIVE`` or ``ORG_COMPILE_BACKEND_SCALAR``.
Use the serialized-size query before allocating a binary output buffer, then
check serialize/load results. Binary format compatibility is separate from
Graph IR version and provider ABI version; never identify a binary by filename
alone. Resources/providers needed by an external operator are not an embedded
implementation of that operator.

With an installed SDK CMake package, build the independent example:

.. code-block:: console

   cmake -S examples/c -B example_build -DCMAKE_PREFIX_PATH=/path/to/installed/sdk
   cmake --build example_build --config Release

Run ``example_build/Release/identity_provider.exe`` on Windows, or the generated
executable for your SDK toolchain. Expected output is ``identity result: 2.0``.
