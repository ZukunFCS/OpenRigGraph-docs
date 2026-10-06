/* Independent documentation example: an identity operator, not a solver. */
#include <openriggraph/openriggraph.h>
#include <stdio.h>

static void *create_identity(void *user, const char *name, const char *config,
    const org_resource_view *resource, size_t inputs, size_t outputs,
    char *error, size_t error_size) {
    static int marker;
    (void)user; (void)name; (void)config; (void)resource;
    if (inputs != 1 || outputs != 1) {
        snprintf(error, error_size, "identity needs one input and one output");
        return NULL;
    }
    return &marker;
}

static void destroy_identity(void *user, void *instance) {
    (void)user; (void)instance;
}

static int evaluate_identity(void *user, void *instance,
    const float *inputs, size_t input_count, float *outputs,
    size_t output_count, char *error, size_t error_size) {
    (void)user; (void)instance; (void)input_count; (void)output_count;
    (void)error; (void)error_size;
    outputs[0] = inputs[0];
    return ORG_STATUS_OK;
}

int main(void) {
    const char *json = "{\"version\":2,\"format\":\"OpenRigGraph\","
        "\"controllers\":[],\"resources\":[{\"name\":\"example_resource\","
        "\"type\":\"example.identity\"}],\"nodes\":[{\"name\":\"identity\","
        "\"type\":\"RigLogic\",\"interface\":{\"inputs\":[\"x\"],"
        "\"outputs\":[\"response\"]},\"resource\":\"example_resource\","
        "\"inputs\":{\"x\":2}}],\"outputs\":[{\"name\":\"result\","
        "\"type\":\"scalar\",\"source\":\"identity.response\"}]}";
    char error[4096] = {0};
    const unsigned char resource_data[] = {0};
    org_operator_provider provider = {ORG_OPERATOR_PROVIDER_ABI_VERSION,
        NULL, create_identity, destroy_identity, evaluate_identity};
    org_context *context = org_context_create();
    org_graph *graph = NULL;
    org_module *module = NULL;
    org_instance *instance = NULL;
    int success = 0;
    if (!context) goto done;
    if (org_context_register_operator_provider(context, "RigLogic", &provider,
            error, sizeof(error)) != ORG_STATUS_OK) goto done;
    if (org_context_bind_resource(context, "example_resource", "example.identity",
            resource_data, sizeof(resource_data), NULL, error, sizeof(error))
            != ORG_STATUS_OK) goto done;
    graph = org_graph_load_json(json, error, sizeof(error));
    if (!graph) goto done;
    module = org_module_compile_with_context(graph, context, error, sizeof(error));
    if (!module) goto done;
    instance = org_instance_create_with_context(module, context, error, sizeof(error));
    if (!instance) goto done;
    if (org_instance_evaluate(instance) != ORG_STATUS_OK) {
        snprintf(error, sizeof(error), "%s", org_instance_last_error(instance));
        goto done;
    }
    success = org_instance_get_output(instance, 0) == 2.0f;
    printf("identity result: %.1f\n", org_instance_get_output(instance, 0));
done:
    if (!success) fprintf(stderr, "identity example failed: %s\n", error);
    if (instance) org_instance_destroy(instance);
    if (module) org_module_destroy(module);
    if (graph) org_graph_destroy(graph);
    if (context) org_context_destroy(context);
    return success ? 0 : 1;
}
