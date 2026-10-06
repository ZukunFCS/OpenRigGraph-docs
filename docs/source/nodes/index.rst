Graph node reference
====================

Every entry below is a runtime-accepted type with a documented authoring contract. Source-node detection and exporter support are separate capabilities.

.. toctree::
   :maxdepth: 1

   contracts
   animation_contracts
   surface_contracts

Scalar and arithmetic
---------------------

.. toctree::
   :maxdepth: 1

   unitConversion
   addDoubleLinear
   multDoubleLinear
   reverse
   clamp
   condition
   multiplyDivide
   plusMinusAverage
   ScalarMathNode

Remapping and animation
-----------------------

.. toctree::
   :maxdepth: 1

   setRange
   animCurveUU
   animCurveUL
   animCurveUA
   animCurveUT
   animCurveTA
   animCurveTL
   remapValue
   remapColor

Blending and selection
----------------------

.. toctree::
   :maxdepth: 1

   blendWeighted
   animBlendNodeAdditive
   blendColors
   blendTwoAttr
   pairBlend
   choice

Vectors and quaternions
-----------------------

.. toctree::
   :maxdepth: 1

   axisAngleToQuat
   eulerToQuat
   quatToEuler
   quatAdd
   quatProd
   quatSlerp
   angleBetween
   pointMatrixMult
   distanceBetween

Matrices and transforms
-----------------------

.. toctree::
   :maxdepth: 1

   composeMatrix
   fourByFourMatrix
   multMatrix
   inverseMatrix
   wtAddMatrix
   decomposeMatrix
   aimMatrix

Constraints and IK
------------------

.. toctree::
   :maxdepth: 1

   pointConstraint
   orientConstraint
   scaleConstraint
   parentConstraint
   aimConstraint
   ikRP
   ikRP2Bone

Curves and surfaces
-------------------

.. toctree::
   :maxdepth: 1

   curveSample
   motionPath
   tangentConstraint
   closestPointOnSurface
   surfaceFrame
   meshSurfaceFrames
   weightedVertexCage

Models and sampled behavior
---------------------------

.. toctree::
   :maxdepth: 1

   RbfNode
   ModelNode
   ApproxNode
   SampledNode

External operators
------------------

.. toctree::
   :maxdepth: 1

   RigLogic

Aliases
-------

* ``addDL`` -> :ref:`addDoubleLinear <node-addDoubleLinear>`.
* ``MathNode`` -> :ref:`ScalarMathNode <node-ScalarMathNode>`.
* ``MatrixComposeNode`` -> :ref:`composeMatrix <node-composeMatrix>`.
* ``addMatrix`` -> :ref:`wtAddMatrix <node-wtAddMatrix>`.
* ``MatrixMultiplyNode`` -> :ref:`multMatrix <node-multMatrix>`.
* ``MatrixInverseNode`` -> :ref:`inverseMatrix <node-inverseMatrix>`.
* ``MatrixWeightedAddNode`` -> :ref:`wtAddMatrix <node-wtAddMatrix>`.
