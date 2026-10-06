# OpenRigGraph documentation

Public Sphinx/ReadTheDocs documentation for the OpenRigGraph API and character
porting workflows. This docs-only repository contains no runtime source or
binaries. Executable examples require an existing authorized ORG SDK and a
compatible Maya environment where applicable.

The reference covers every current graph node, alias, and ORG Maya integration
node, the C/Python/CLI APIs, formats, and independent synthetic examples.
Start with `docs/source/getting_started.rst` or the agent porting workflow.
`llms.txt`, `llms-full.txt`, and the downloadable JSON catalog support agents.

## Build

```console
python -m pip install -r docs/requirements.txt
python tools/docs/check_public.py
python -m sphinx -n -W -b html docs/source docs/build/html
```

For runtime examples, use `python tools/docs/verify_examples.py --orgctl
/path/to/orgctl` on one line. SDK-dependent C and Maya examples are under
`examples/`. The reference and tutorial document prerequisites and expected
results. Python 3.12 is used by ReadTheDocs; the docs build has no Maya imports.

ReadTheDocs configuration is in `.readthedocs.yaml`. The main branch supplies
latest and dated release tags supply stable. Runtime, graph, binary, provider,
and documentation versions are separate compatibility dimensions.

Only independently authored examples and reviewed public contracts belong here.
New API types require a catalog/reference update before publication.
