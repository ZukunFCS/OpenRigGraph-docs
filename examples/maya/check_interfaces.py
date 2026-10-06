"""Verify the public Maya node/attribute inventory with a compatible plug-in.

mayapy examples/maya/check_interfaces.py --plugin /path/to/openriggraph_maya.mll
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plugin", required=True, help="Compatible ORG Maya plug-in path")
    parser.add_argument("--catalog", type=Path, default=Path(__file__).resolve().parents[2] / "docs/source/_generated/node_catalog.json")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    import maya.standalone
    maya.standalone.initialize(name="python")
    import maya.cmds as cmds
    cmds.loadPlugin(str(Path(args.plugin).resolve()))
    report = dict(maya_version=cmds.about(version=True), nodes=[], failures=[])
    for spec in json.loads(args.catalog.read_text())["nodes"]:
        if spec["layer"] != "maya":
            continue
        node = cmds.createNode(spec["type"])
        actual = set(cmds.listAttr(node) or [])
        missing = [a["name"] for a in spec["attributes"] if a["name"] not in actual]
        attrs = []
        for attr in spec["attributes"]:
            if attr["name"] in actual:
                attrs.append(dict(name=attr["name"], maya_type=cmds.getAttr(node + "." + attr["name"], type=True),
                                  array=cmds.attributeQuery(attr["name"], node=node, multi=True)))
        if missing:
            report["failures"].append(dict(type=spec["type"], missing_attributes=missing))
        report["nodes"].append(dict(type=spec["type"], declared_attributes=len(spec["attributes"]), attributes=attrs))
        cmds.delete(node)
    text = json.dumps(report, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    print("ORG_DOCS_INTERFACES " + json.dumps(dict(maya_version=report["maya_version"], nodes=len(report["nodes"]), failures=report["failures"])))
    maya.standalone.uninitialize()
    if report["failures"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
