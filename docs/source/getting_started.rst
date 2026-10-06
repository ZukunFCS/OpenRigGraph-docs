Getting started
===============

Runtime access
--------------

This is a documentation-only distribution. Running examples requires an existing
OpenRigGraph SDK or authorized source checkout. This repository does not contain
the runtime library, executable, or Maya plug-in. Do not build ORG from the
documentation repository.

Locate ``orgctl`` (``orgctl.exe`` on Windows), the public header/library for
embedding, and a plug-in built for your Maya version. Put ``orgctl`` on PATH or
substitute its full path. Maya and source plug-ins are separate dependencies.

.. code-block:: console

   git clone https://github.com/ZukunFCS/OpenRigGraph-docs.git
   cd OpenRigGraph-docs
   orgctl validate examples/graph/addDoubleLinear.json
   orgctl eval examples/graph/addDoubleLinear.json --output json

The result is ``{"result": 3}``. Continue with the
:doc:`synthetic character tutorial <porting/tutorial>`.

Build from authorized source
----------------------------

Run from the ORG source root, not the documentation root. Requirements are
CMake 3.25+, a C++20 toolchain, and the configured JSON dependency.
On Windows use an installed Visual Studio C++ toolchain:

.. code-block:: powershell

   cmake -S . -B build_verify -G "Visual Studio 18 2026"
   cmake --build build_verify --config Release --parallel 4
   ctest --test-dir build_verify -C Release --output-on-failure
   .\build_verify\Release\orgctl.exe eval examples\graph\addDoubleLinear.json --output json

Select the corresponding CMake generator if using another installed Visual
Studio version. The source rejects the mutable Scoop LLVM ``current`` toolchain
path; use MSVC or an explicitly versioned toolchain.

For the opt-in Maya integration, supply the actual Maya installation:

.. code-block:: powershell

   cmake -S . -B build_maya -G "Visual Studio 18 2026" -DORG_BUILD_MAYA_PLUGIN=ON -DORG_MAYA_ROOT="C:/Program Files/Autodesk/Maya2024"
   cmake --build build_maya --config Release --parallel 4

Use a separate build tree per Maya ABI. Successful compilation does not prove
compatibility with another version. See :doc:`release` and :doc:`maya/contracts`.

Build the documentation
-----------------------

The documentation build needs neither Maya nor the SDK:

.. code-block:: console

   python -m venv .venv
   python -m pip install -r docs/requirements.txt
   python -m sphinx -n -W -b html docs/source docs/build/html

Activate the virtual environment before installing requirements: Windows uses
``.venv\Scripts\Activate.ps1`` and POSIX uses ``source .venv/bin/activate``.
Open ``docs/build/html/index.html``. API details are in :doc:`reference/cli`
and :doc:`reference/embedding`.
