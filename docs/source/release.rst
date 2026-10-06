Documentation release and maintenance
=====================================

This docs-only release is an API snapshot dated 2026-10-06. Runtime/SDK access is
an explicit prerequisite. Public material includes independent examples and
reusable interfaces; it does not include source assets, captured scenes, custom
source-node implementations, or runtime binaries.

ReadTheDocs configuration uses version 2, Ubuntu 24.04, Python 3.12, pinned
Sphinx/theme requirements, HTML, and downloadable HTML ZIP. The documentation
repository builds without Maya or private source. See the
`ReadTheDocs configuration reference <https://docs.readthedocs.com/platform/stable/config-file/v2.html>`_.

The main documentation branch supplies latest; a dated documentation tag supplies
stable. Runtime, Graph IR, binary format, and provider ABI versions are recorded
separately. Future node/API changes must update the reviewed catalog and regenerate
the reference before publishing.

Validation matrix
-----------------

Graph examples and aliases are checked against the current native runtime.
The C example exercises independent provider registration and evaluation.
Maya 2024 interface checks and the procedural port establish that snapshot's
tested integration environment. Other Maya versions require their own ABI build
and validation; this page does not assert unmeasured compatibility.

Build with ``python -m sphinx -n -W -b html docs/source docs/build/html``.
Nitpicky references and warnings fail the release build. See the
`Sphinx build reference <https://www.sphinx-doc.org/en/master/man/sphinx-build.html>`_.
Public CI checks standalone docs, inventory/download integrity, and synthetic
JSON structure; SDK CI additionally runs source drift and executable graph checks.
C embedding and Maya integration checks are release validation steps run with
the authorized SDK and matching Maya installation.

The release export is allowlisted and scanned before publication. Keep internal
reports, paths, source histories, protected identifiers, and generated captures
outside the public bundle. Review invented examples for accidental identifying
details; changing names in a real capture is not independent authoring.
