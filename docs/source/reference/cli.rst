orgctl command-line API
=======================

Use ``orgctl.exe`` on Windows or ``orgctl`` on other supported SDK platforms. Put the executable on PATH or use its full path.

validate
--------

Check graph syntax and semantic compilation diagnostics.

.. code-block:: console

   orgctl validate <graph.json>

   orgctl validate examples/graph/addDoubleLinear.json

compile
-------

Write a versioned compiled module; select native or scalar backend.

.. code-block:: console

   orgctl compile <graph.json> <module.orgb> [--backend native|scalar]

   orgctl compile examples/graph/addDoubleLinear.json example.orgb --backend native

inspect
-------

Inspect controllers, outputs, and optionally lowered instructions.

.. code-block:: console

   orgctl inspect <graph.json> [--instructions]

   orgctl inspect examples/graph/addDoubleLinear.json --instructions

eval
----

Evaluate one control assignment and emit text or JSON outputs.

.. code-block:: console

   orgctl eval <graph.json> [--backend native|scalar] [--set name=value ...] [--inputs-json inputs.json] [--output json|text]

   orgctl eval examples/graph/addDoubleLinear.json --output json

eval-batch
----------

Evaluate explicit sample rows with machine-readable results.

.. code-block:: console

   orgctl eval-batch <graph.json> --samples-json samples.json [--output json]

   orgctl eval-batch examples/tutorial/character.json --samples-json examples/tutorial/samples.json --output json

bench
-----

Measure a specified control-update/evaluation workload with warmup and iterations.

.. code-block:: console

   orgctl bench <graph.json|module.orgb> [--backend native|scalar] [--mode all|name|index|bulk|eval-only] [--warmup N] [--iterations N] [--output json|text]

   orgctl bench examples/graph/addDoubleLinear.json --backend native --mode eval-only --warmup 100 --iterations 1000 --output json

compare
-------

Compare graph outputs for the same control assignment at an explicit tolerance.

.. code-block:: console

   orgctl compare <expected.json> <actual.json> [--set name=value ...] [--tolerance value]

   orgctl compare examples/graph/addDoubleLinear.json examples/graph/addDoubleLinear.json --tolerance 0.00001

Exit status zero means the requested operation succeeded. Retain stderr and the JSON result on failures. Do not infer Maya/geometry parity from successful validation or compilation alone.
