Synthetic character tutorial
============================

This independent example creates a procedural four-vertex mesh, one blendshape,
one joint, two controls, and editable curves. Maya retains deformation and
animation ownership; ORG replaces the numeric control boundary. More extensive
geometry lowering is a separate step.

Graph and output mapping
------------------------

``smile`` and ``twist`` are controller names; ``smileWeight`` and ``twistValue``
are outputs. The clamp preserves the source's bounded smile behavior. Twist
passes through; do not add clamping merely because a value drives rotation.

.. literalinclude:: ../../../examples/tutorial/character.json
   :language: json

Download :download:`character.json <../../../examples/tutorial/character.json>`
and :download:`samples.json <../../../examples/tutorial/samples.json>`.

Evaluate without Maya
---------------------

.. code-block:: console

   orgctl validate examples/tutorial/character.json
   orgctl eval examples/tutorial/character.json --set smile=0.25 --set twist=-15 --output json
   orgctl eval-batch examples/tutorial/character.json --samples-json examples/tutorial/samples.json --output json
   orgctl compile examples/tutorial/character.json character.orgb --backend native

The single evaluation returns ``smileWeight=0.25`` and ``twistValue=-15``.
Batch smile inputs -0.1 and 1.1 produce zero and one. Controller ``clamp:false``
ensures the graph clamp, rather than controller input clamping, is exercised.

Port and verify in Maya
-----------------------

Run :download:`the procedural port <../../../examples/maya/port_character.py>`
with a ``mayapy`` executable and plug-in built for the same Maya version:

.. code-block:: powershell

   & "C:\Program Files\Autodesk\Maya2024\bin\mayapy.exe" examples\maya\port_character.py --plugin C:\sdk\maya2024\openriggraph_maya.mll --output-dir synthetic_org_port

The script builds the native scene, captures world-space points at integer and
fractional times, connects original controls to an ``openRigGraphEvaluator``,
and reconnects graph outputs to the same blendshape/joint boundaries. It compares
all vertices, saves a relative graph path, copies the package, reopens it, and
compares again. Original animator controls and keyed curves remain editable.

Outputs are ``character.ma``, ``character.json``, ``verification.json``, and a
``relocated/`` package. The report records Maya version, sample/vertex counts,
maximum error, and pass/fail against ``1e-4 cm``. Failure exits nonzero.

Transfer to a real scene
------------------------

Discover the actual driven mesh cohort and requested controls. Trace dependencies
from outputs; bake constants only with proof. Choose nodes by plugs, units,
operations, and scope. Preserve typed-unit boundaries and editable animation.
Follow :doc:`agent_workflow` and :doc:`export_verify`; this example's small
sample set and tolerance are not universal character acceptance criteria.
