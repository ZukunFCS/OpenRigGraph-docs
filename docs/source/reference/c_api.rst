C embedding API
===============

The API snapshot documents all exported ``ORG_API`` functions. Include ``openriggraph/openriggraph.h`` and link your existing ORG SDK.

See :doc:`embedding lifecycle and errors <embedding>` before using these declarations.

Public types
------------

.. c:type:: org_graph

.. code-block:: c

   typedef struct org_graph org_graph;

.. c:type:: org_module

.. code-block:: c

   typedef struct org_module org_module;

.. c:type:: org_instance

.. code-block:: c

   typedef struct org_instance org_instance;

.. c:type:: org_context

.. code-block:: c

   typedef struct org_context org_context;

.. c:type:: org_status

.. code-block:: c

   typedef enum org_status {
       ORG_STATUS_OK = 0,
       ORG_STATUS_ERROR = 1,
       ORG_STATUS_INVALID_ARGUMENT = 2,
       ORG_STATUS_VALIDATION_ERROR = 3,
       ORG_STATUS_NOT_FOUND = 4,
       ORG_STATUS_OUT_OF_RANGE = 5,
       ORG_STATUS_OPERATOR_ERROR = 6,
       ORG_STATUS_INCOMPATIBLE_BINARY = 7
   } org_status;

.. c:type:: org_output_type

.. code-block:: c

   typedef enum org_output_type {
       ORG_OUTPUT_BLENDSHAPE = 0,
       ORG_OUTPUT_POSE = 1,
       ORG_OUTPUT_SCALAR = 2,
       ORG_OUTPUT_JOINT_CENTER = 3,
       ORG_OUTPUT_ANIMATED_MAP = 4
   } org_output_type;

.. c:type:: org_compile_backend

.. code-block:: c

   typedef enum org_compile_backend {
       ORG_COMPILE_BACKEND_NATIVE = 0,
       ORG_COMPILE_BACKEND_SCALAR = 1
   } org_compile_backend;

.. c:type:: org_compile_options

.. code-block:: c

   typedef struct org_compile_options {
       size_t struct_size;
       int backend;
   } org_compile_options;

.. c:type:: org_resource_view

.. code-block:: c

   typedef struct org_resource_view {
       const char* name;
       const char* type;
       const void* data;
       size_t size;
       const char* sha256;
   } org_resource_view;

.. c:type:: org_operator_create_fn

.. code-block:: c

   typedef void* (*org_operator_create_fn)(
       void* user_data,
       const char* node_name,
       const char* config_json,
       const org_resource_view* resource,
       size_t input_count,
       size_t output_count,
       char* error_buffer,
       size_t error_buffer_size
   );

.. c:type:: org_operator_destroy_fn

.. code-block:: c

   typedef void (*org_operator_destroy_fn)(void* user_data, void* operator_instance);

.. c:type:: org_operator_evaluate_fn

.. code-block:: c

   typedef int (*org_operator_evaluate_fn)(
       void* user_data,
       void* operator_instance,
       const float* inputs,
       size_t input_count,
       float* outputs,
       size_t output_count,
       char* error_buffer,
       size_t error_buffer_size
   );

.. c:type:: org_operator_provider

.. code-block:: c

   typedef struct org_operator_provider {
       uint32_t abi_version;
       void* user_data;
       org_operator_create_fn create;
       org_operator_destroy_fn destroy;
       org_operator_evaluate_fn evaluate;
   } org_operator_provider;

Status and format constants
---------------------------

* ``ORG_STATUS_OK = 0``.
* ``ORG_STATUS_ERROR = 1``.
* ``ORG_STATUS_INVALID_ARGUMENT = 2``.
* ``ORG_STATUS_VALIDATION_ERROR = 3``.
* ``ORG_STATUS_NOT_FOUND = 4``.
* ``ORG_STATUS_OUT_OF_RANGE = 5``.
* ``ORG_STATUS_OPERATOR_ERROR = 6``.
* ``ORG_STATUS_INCOMPATIBLE_BINARY = 7``.
* ``ORG_OUTPUT_BLENDSHAPE = 0``.
* ``ORG_OUTPUT_POSE = 1``.
* ``ORG_OUTPUT_SCALAR = 2``.
* ``ORG_OUTPUT_JOINT_CENTER = 3``.
* ``ORG_OUTPUT_ANIMATED_MAP = 4``.
* ``ORG_COMPILE_BACKEND_NATIVE = 0``.
* ``ORG_COMPILE_BACKEND_SCALAR = 1``.
* ``ORG_OPERATOR_PROVIDER_ABI_VERSION = 1``.
* ``ORG_COMPILED_MODULE_FORMAT_VERSION = 16``.

Functions
---------

.. c:function:: const char* org_status_string(int status)

   Return the static human-readable name of a status code.

.. c:function:: org_context* org_context_create(void)

   Create a provider/resource context. Returns null on allocation failure; destroy it after dependent instances are finished.

.. c:function:: void org_context_destroy(org_context* context)

   Destroy the context. Do not use it to create further modules or instances after destruction.

.. c:function:: int org_context_register_operator_provider( org_context* context, const char* operator_type, const org_operator_provider* provider, char* error_buffer, size_t error_buffer_size )

   Register an operator provider by type. Supply the supported ABI version and all required callbacks; returns a status and writes diagnostics on failure.

.. c:function:: int org_context_bind_resource( org_context* context, const char* name, const char* type, const void* data, size_t size, const char* sha256, char* error_buffer, size_t error_buffer_size )

   Copy named resource bytes into the context. A supplied SHA-256 must match those bytes; omitted hash is computed. Name/type/hash must match the graph declaration and provider expectations.

.. c:function:: org_graph* org_graph_load_json(const char* json_text, char* error_buffer, size_t error_buffer_size)

   Parse graph JSON. Returns an owned graph handle, or null with an error-buffer diagnostic.

.. c:function:: void org_graph_destroy(org_graph* graph)

   Release the owned handle. Never reuse a released handle; release instances before their modules.

.. c:function:: int org_graph_validate(org_graph* graph, char* error_buffer, size_t error_buffer_size)

   Validate supported graph semantics by compilation. Query graph diagnostics when validation fails.

.. c:function:: size_t org_graph_diagnostic_count(const org_graph* graph)

   Query graph-owned validation diagnostics; message pointers remain owned by the graph. Bounds are defined by the corresponding count query.

.. c:function:: const char* org_graph_diagnostic_message(const org_graph* graph, size_t index)

   Query graph-owned validation diagnostics; message pointers remain owned by the graph. Bounds are defined by the corresponding count query.

.. c:function:: org_module* org_module_compile(const org_graph* graph, char* error_buffer, size_t error_buffer_size)

   Compile with the default native backend and no external context. Returns an owned module or null with a diagnostic.

.. c:function:: org_module* org_module_compile_with_context( const org_graph* graph, const org_context* context, char* error_buffer, size_t error_buffer_size )

   Compile with external provider/resource bindings in the supplied context.

.. c:function:: org_module* org_module_compile_with_options( const org_graph* graph, const org_context* context, const org_compile_options* options, char* error_buffer, size_t error_buffer_size )

   Compile with explicit backend options; set struct_size to sizeof(org_compile_options).

.. c:function:: org_module* org_module_load_binary( const void* data, size_t size, char* error_buffer, size_t error_buffer_size )

   Load a serialized module from the supplied bytes. Incompatible versions or malformed payloads fail with a diagnostic.

.. c:function:: size_t org_module_serialized_size(const org_module* module)

   Query compiled-module serialized size. Use the corresponding count before indexed access. Returned strings remain owned by the module; copy them before destroying it.

.. c:function:: int org_module_serialize( const org_module* module, void* data, size_t size, char* error_buffer, size_t error_buffer_size )

   Write the module into a caller-owned buffer sized using org_module_serialized_size. Check the returned status.

.. c:function:: void org_module_destroy(org_module* module)

   Release the owned handle. Never reuse a released handle; release instances before their modules.

.. c:function:: const char* org_module_source_sha256(const org_module* module)

   Query compiled-module source sha256. Use the corresponding count before indexed access. Returned strings remain owned by the module; copy them before destroying it.

.. c:function:: size_t org_module_operator_count(const org_module* module)

   Query compiled-module operator count. Use the corresponding count before indexed access. Returned strings remain owned by the module; copy them before destroying it.

.. c:function:: size_t org_module_controller_count(const org_module* module)

   Query compiled-module controller count. Use the corresponding count before indexed access. Returned strings remain owned by the module; copy them before destroying it.

.. c:function:: const char* org_module_controller_name(const org_module* module, size_t index)

   Query compiled-module controller name. Use the corresponding count before indexed access. Returned strings remain owned by the module; copy them before destroying it.

.. c:function:: float org_module_controller_default(const org_module* module, size_t index)

   Query compiled-module controller default. Use the corresponding count before indexed access. Returned strings remain owned by the module; copy them before destroying it.

.. c:function:: double org_module_controller_default_f64(const org_module* module, size_t index)

   Query compiled-module controller default f64. Use the corresponding count before indexed access. Returned strings remain owned by the module; copy them before destroying it.

.. c:function:: float org_module_controller_min(const org_module* module, size_t index)

   Query compiled-module controller min. Use the corresponding count before indexed access. Returned strings remain owned by the module; copy them before destroying it.

.. c:function:: float org_module_controller_max(const org_module* module, size_t index)

   Query compiled-module controller max. Use the corresponding count before indexed access. Returned strings remain owned by the module; copy them before destroying it.

.. c:function:: int org_module_controller_clamp_enabled(const org_module* module, size_t index)

   Query compiled-module controller clamp enabled. Use the corresponding count before indexed access. Returned strings remain owned by the module; copy them before destroying it.

.. c:function:: size_t org_module_output_count(const org_module* module)

   Query compiled-module output count. Use the corresponding count before indexed access. Returned strings remain owned by the module; copy them before destroying it.

.. c:function:: const char* org_module_output_name(const org_module* module, size_t index)

   Query compiled-module output name. Use the corresponding count before indexed access. Returned strings remain owned by the module; copy them before destroying it.

.. c:function:: int org_module_output_type(const org_module* module, size_t index)

   Query compiled-module output type. Use the corresponding count before indexed access. Returned strings remain owned by the module; copy them before destroying it.

.. c:function:: size_t org_module_output_target_index(const org_module* module, size_t index)

   Query compiled-module output target index. Use the corresponding count before indexed access. Returned strings remain owned by the module; copy them before destroying it.

.. c:function:: size_t org_module_output_joint_index(const org_module* module, size_t index)

   Query compiled-module output joint index. Use the corresponding count before indexed access. Returned strings remain owned by the module; copy them before destroying it.

.. c:function:: size_t org_module_output_component(const org_module* module, size_t index)

   Query compiled-module output component. Use the corresponding count before indexed access. Returned strings remain owned by the module; copy them before destroying it.

.. c:function:: const char* org_module_output_space(const org_module* module, size_t index)

   Query compiled-module output space. Use the corresponding count before indexed access. Returned strings remain owned by the module; copy them before destroying it.

.. c:function:: const char* org_module_output_mode(const org_module* module, size_t index)

   Query compiled-module output mode. Use the corresponding count before indexed access. Returned strings remain owned by the module; copy them before destroying it.

.. c:function:: int org_module_output_clamp_enabled(const org_module* module, size_t index)

   Query compiled-module output clamp enabled. Use the corresponding count before indexed access. Returned strings remain owned by the module; copy them before destroying it.

.. c:function:: size_t org_module_instruction_count(const org_module* module)

   Inspect lowered instruction metadata. Instruction and source/parameter indices are bounded by their count queries; this is diagnostic introspection, not an editing API.

.. c:function:: size_t org_module_instruction_dst_count(const org_module* module, size_t index)

   Inspect lowered instruction metadata. Instruction and source/parameter indices are bounded by their count queries; this is diagnostic introspection, not an editing API.

.. c:function:: size_t org_module_register_count(const org_module* module)

   Query compiled-module register count. Use the corresponding count before indexed access. Returned strings remain owned by the module; copy them before destroying it.

.. c:function:: const char* org_module_instruction_opcode(const org_module* module, size_t index)

   Inspect lowered instruction metadata. Instruction and source/parameter indices are bounded by their count queries; this is diagnostic introspection, not an editing API.

.. c:function:: int org_module_instruction_dst(const org_module* module, size_t index)

   Inspect lowered instruction metadata. Instruction and source/parameter indices are bounded by their count queries; this is diagnostic introspection, not an editing API.

.. c:function:: size_t org_module_instruction_src_count(const org_module* module, size_t index)

   Inspect lowered instruction metadata. Instruction and source/parameter indices are bounded by their count queries; this is diagnostic introspection, not an editing API.

.. c:function:: int org_module_instruction_src(const org_module* module, size_t instruction_index, size_t source_index)

   Inspect lowered instruction metadata. Instruction and source/parameter indices are bounded by their count queries; this is diagnostic introspection, not an editing API.

.. c:function:: size_t org_module_instruction_param_count(const org_module* module, size_t index)

   Inspect lowered instruction metadata. Instruction and source/parameter indices are bounded by their count queries; this is diagnostic introspection, not an editing API.

.. c:function:: float org_module_instruction_param(const org_module* module, size_t instruction_index, size_t param_index)

   Inspect lowered instruction metadata. Instruction and source/parameter indices are bounded by their count queries; this is diagnostic introspection, not an editing API.

.. c:function:: size_t org_module_instruction_int_count(const org_module* module, size_t index)

   Inspect lowered instruction metadata. Instruction and source/parameter indices are bounded by their count queries; this is diagnostic introspection, not an editing API.

.. c:function:: int org_module_instruction_int(const org_module* module, size_t instruction_index, size_t int_index)

   Inspect lowered instruction metadata. Instruction and source/parameter indices are bounded by their count queries; this is diagnostic introspection, not an editing API.

.. c:function:: org_instance* org_instance_create(const org_module* module)

   Create mutable evaluation state for a compiled module; returns an owned instance or null.

.. c:function:: org_instance* org_instance_create_with_context( const org_module* module, const org_context* context, char* error_buffer, size_t error_buffer_size )

   Create mutable evaluation state and provider instances using a context; missing resources/providers produce diagnostics.

.. c:function:: void org_instance_destroy(org_instance* instance)

   Release the owned handle. Never reuse a released handle; release instances before their modules.

.. c:function:: const char* org_instance_last_error(const org_instance* instance)

   Read instance-owned diagnostics from the most recent evaluation failure; copy the text before the next state-changing call.

.. c:function:: int org_instance_reset_controls(org_instance* instance)

   Restore declared controller defaults; evaluate afterward to update outputs.

.. c:function:: int org_instance_set_control(org_instance* instance, size_t index, float value)

   Set control values by the stated name/index or bulk array. Names and indices follow module metadata; bulk count must match. Check status, including unknown names and out-of-range indices. This entry point accepts float values. Evaluate to refresh outputs.

.. c:function:: int org_instance_set_controls(org_instance* instance, const float* values, size_t count)

   Set control values by the stated name/index or bulk array. Names and indices follow module metadata; bulk count must match. Check status, including unknown names and out-of-range indices. This entry point accepts float values. Evaluate to refresh outputs.

.. c:function:: int org_instance_set_control_by_name(org_instance* instance, const char* name, float value)

   Set control values by the stated name/index or bulk array. Names and indices follow module metadata; bulk count must match. Check status, including unknown names and out-of-range indices. This entry point accepts float values. Evaluate to refresh outputs.

.. c:function:: int org_instance_set_control_f64(org_instance* instance, size_t index, double value)

   Set control values by the stated name/index or bulk array. Names and indices follow module metadata; bulk count must match. Check status, including unknown names and out-of-range indices. The f64 entry point accepts double values. Evaluate to refresh outputs.

.. c:function:: int org_instance_set_controls_f64(org_instance* instance, const double* values, size_t count)

   Set control values by the stated name/index or bulk array. Names and indices follow module metadata; bulk count must match. Check status, including unknown names and out-of-range indices. The f64 entry point accepts double values. Evaluate to refresh outputs.

.. c:function:: int org_instance_set_control_by_name_f64(org_instance* instance, const char* name, double value)

   Set control values by the stated name/index or bulk array. Names and indices follow module metadata; bulk count must match. Check status, including unknown names and out-of-range indices. The f64 entry point accepts double values. Evaluate to refresh outputs.

.. c:function:: int org_instance_evaluate(org_instance* instance)

   Evaluate current controls and update outputs. Check status and org_instance_last_error on failure.

.. c:function:: float org_instance_get_output(const org_instance* instance, size_t index)

   Read the last evaluated output by name/index. Name-based access writes to the supplied value pointer and returns a status. Returns float precision.

.. c:function:: int org_instance_get_output_by_name(const org_instance* instance, const char* name, float* value)

   Read the last evaluated output by name/index. Name-based access writes to the supplied value pointer and returns a status. Returns float precision.

.. c:function:: double org_instance_get_output_f64(const org_instance* instance, size_t index)

   Read the last evaluated output by name/index. Name-based access writes to the supplied value pointer and returns a status. Returns double precision.

.. c:function:: int org_instance_get_output_by_name_f64(const org_instance* instance, const char* name, double* value)

   Read the last evaluated output by name/index. Name-based access writes to the supplied value pointer and returns a status. Returns double precision.

.. c:function:: int org_instance_copy_outputs_f64(const org_instance* instance, double* values, size_t count)

   Copy evaluated outputs into the caller's double buffer; count must match the declared output count.

Independent provider example
----------------------------

The :download:`identity provider <../../../examples/c/identity_provider.c>` implements a fictional, source-neutral one-input identity operator. It exercises registration and lifetime without including any external solver implementation.

.. literalinclude:: ../../../examples/c/identity_provider.c
   :language: c
