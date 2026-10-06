"""Build and verify an independent synthetic character port.

Creates only procedural geometry, one joint, one blendshape, and two controls.
Run in mayapy; outputs default relative to the supplied output directory.
"""
from __future__ import annotations

import argparse
import json
import math
import shutil
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plugin", required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("synthetic_org_port"))
    parser.add_argument("--graph", type=Path, default=Path(__file__).resolve().parents[1] / "tutorial/character.json")
    args = parser.parse_args()
    import maya.standalone
    maya.standalone.initialize(name="python")
    import maya.cmds as cmds
    import maya.api.OpenMaya as om
    cmds.loadPlugin(str(Path(args.plugin).resolve()))
    cmds.file(new=True, force=True)
    cmds.currentUnit(linear="cm", angle="deg", time="film")
    out = args.output_dir.resolve()
    out.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(args.graph, out / "character.json")
    # A plain relative path resolves beside the current scene. Name that scene
    # before the first graph demand, including while it is not saved yet.
    cmds.file(rename=str(out / "character.ma"))
    ctrl = cmds.createNode("transform", name="exampleControls")
    for name, lo, hi in (("smile", 0, 1), ("twist", -30, 30)):
        cmds.addAttr(ctrl, longName=name, attributeType="double", minValue=lo, maxValue=hi, keyable=True)
    mesh = cmds.polyPlane(name="exampleCharacter", width=2, height=2, subdivisionsX=1, subdivisionsY=1)[0]
    target = cmds.duplicate(mesh, name="exampleSmileTarget")[0]
    cmds.move(0, 0.5, 0, target + ".vtx[0]", relative=True)
    blend = cmds.blendShape(target, mesh, name="exampleBlend")[0]
    cmds.delete(target)
    cmds.select(clear=True)
    joint = cmds.joint(name="exampleRootJoint", position=(0, 0, 0))
    cmds.skinCluster(joint, mesh, toSelectedBones=True, name="exampleSkin")
    clamp = cmds.createNode("clamp", name="exampleNativeClamp")
    cmds.setAttr(clamp + ".maxR", 1)
    cmds.connectAttr(ctrl + ".smile", clamp + ".inputR")
    cmds.connectAttr(clamp + ".outputR", blend + ".weight[0]")
    cmds.connectAttr(ctrl + ".twist", joint + ".rotateZ")
    for time, smile, twist in ((1, 0, -20), (2, 0.5, 0), (3, 1, 20)):
        cmds.setKeyframe(ctrl, attribute="smile", time=time, value=smile)
        cmds.setKeyframe(ctrl, attribute="twist", time=time, value=twist)
    cmds.keyTangent(ctrl, inTangentType="linear", outTangentType="linear")
    times = [1, 1.25, 1.5, 2, 2.5, 2.75, 3]

    def observation(time):
        cmds.currentTime(time, update=True)
        shape = cmds.listRelatives(mesh, shapes=True, noIntermediate=True, fullPath=True)[0]
        selection = om.MSelectionList()
        selection.add(shape)
        points = om.MFnMesh(selection.getDagPath(0)).getPoints(om.MSpace.kWorld)
        return dict(time=time, smile=cmds.getAttr(ctrl + ".smile"), twist=cmds.getAttr(ctrl + ".twist"),
                    points=[[p.x, p.y, p.z] for p in points])

    oracle = [observation(time) for time in times]
    evaluator = cmds.createNode("openRigGraphEvaluator", name="exampleORG")
    # Store a relative path and verify reopening with a changed working directory.
    cmds.setAttr(evaluator + ".graphPath", "character.json", type="string")
    import os
    os.environ["OPENRIGGRAPH_PACKAGE_ROOT"] = str(out)
    cmds.connectAttr(ctrl + ".smile", evaluator + ".inputValue[0]")
    cmds.connectAttr(ctrl + ".twist", evaluator + ".inputValue[1]")
    cmds.connectAttr(evaluator + ".outputValue[0]", blend + ".weight[0]", force=True)
    cmds.connectAttr(evaluator + ".outputValue[1]", joint + ".rotateZ", force=True)
    actual = [observation(time) for time in times]

    def max_error(a, b):
        return max(abs(x-y) for row_a, row_b in zip(a, b) for point_a, point_b in zip(row_a["points"], row_b["points"]) for x, y in zip(point_a, point_b))

    delta = max_error(oracle, actual)
    scene = out / "character.ma"
    cmds.file(rename=str(scene))
    cmds.file(save=True, type="mayaAscii", force=True)
    moved = out / "relocated"
    moved.mkdir(exist_ok=True)
    shutil.copyfile(scene, moved / scene.name)
    shutil.copyfile(out / "character.json", moved / "character.json")
    os.environ["OPENRIGGRAPH_PACKAGE_ROOT"] = str(moved)
    cmds.file(new=True, force=True)
    cmds.file(str(moved / scene.name), open=True, force=True)
    relocated = [observation(time) for time in times]
    relocated_delta = max_error(oracle, relocated)
    report = dict(maya_version=cmds.about(version=True), scene="character.ma", samples=len(times), vertex_count=len(oracle[0]["points"]),
                  max_vertex_error_cm=delta, relocated_max_vertex_error_cm=relocated_delta, tolerance_cm=1e-4,
                  passed=delta <= 1e-4 and relocated_delta <= 1e-4,
                  source="independent procedural example", oracle=oracle, org=actual)
    (out / "verification.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("ORG_DOCS_PORT " + json.dumps({k:v for k,v in report.items() if k not in ("oracle", "org")}))
    maya.standalone.uninitialize()
    if not report["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
