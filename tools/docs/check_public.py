"""Check standalone docs integrity and generic publication privacy constraints.

Private publication gates additionally pass a local denylist using --denylist.
That file, its contents, and private validation reports are never exported.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


def check(root, denylist=None, rendered=None):
    catalog_path = root / "docs/source/_generated/node_catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    errors = []
    release_manifest = root / "release-manifest.json"
    if release_manifest.exists():
        for name, digest in json.loads(release_manifest.read_text(encoding="utf-8"))["files"].items():
            path = root / name
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                errors.append("Release checksum mismatch: " + name)
    for spec in catalog["nodes"]:
        page = root / "docs/source" / spec["url"].replace(".html", ".rst")
        if not page.exists():
            errors.append("Missing node page: " + spec["type"])
        if spec["layer"] == "graph":
            path = root / spec["example_path"]
            graph = json.loads(path.read_text())
            if graph["nodes"][0]["type"] != spec["type"]:
                errors.append("Example type mismatch: " + spec["type"])
            if not all(key in spec for key in ("purpose", "when_to_use", "inputs", "parameters", "outputs", "scope", "expected")):
                errors.append("Incomplete contract: " + spec["type"])
        elif not spec["attributes"]:
            errors.append("Empty Maya attribute contract: " + spec["type"])
    types = {n["type"] for n in catalog["nodes"] if n["layer"] == "graph"}
    if not set(catalog["aliases"].values()) <= types:
        errors.append("Alias targets are not canonical types")
    c_page = (root / "docs/source/reference/c_api.rst").read_text()
    found = set(re.findall(r'^\.\. c:function:: .*?\b(org_\w+)\(', c_page, re.M))
    if found != set(catalog["c_api"]["functions"]):
        errors.append("C ABI page/catalog drift")
    manifest = json.loads((root / "docs/source/_generated/generated_manifest.json").read_text())
    for relative, digest in manifest.items():
        path = root / relative
        if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            errors.append("Generated file changed: " + relative)
    denied = []
    if denylist:
        denied = [s.strip() for s in Path(denylist).read_text().splitlines() if s.strip() and not s.startswith("#")]
    patterns = [re.compile(r'(?i)[A-Z]:[\\/]Users[\\/]'),
                re.compile(r'\\\\(?:\d{1,3}\.){3}\d{1,3}[\\/]'),
                re.compile(r'(?i)\b(?:api[_-]?key|access[_-]?token|password)\s*[:=]\s*[\"\x27][A-Za-z0-9_-]{16,}')]
    trees = [root / "docs/source", root / "docs/agent_skills", root / "examples", root / "schemas"]
    if rendered:
        trees.append(Path(rendered))
    # Root publications and workflow/config files also carry content and names.
    source_checkout = (root / "src/openriggraph.cpp").exists()
    public_root_names = {"README.md", "LICENSE", ".readthedocs.yaml", "llms.txt", "llms-full.txt", "release-manifest.json"}
    extra = [p for p in root.iterdir() if p.is_file() and (not source_checkout or p.name in public_root_names)]
    extra += list((root / ".github").rglob("*")) if (root / ".github").exists() else []
    scanned = 0
    collections = [(tree, tree.rglob("*")) for tree in trees] + [(root, extra)]
    for tree, paths in collections:
        for path in paths:
            if not path.is_file() or path.suffix.lower() not in (".rst", ".md", ".txt", ".html", ".json", ".py", ".c", ".js", ".yml", ".yaml"):
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            scanned += 1
            if any(p.search(text) for p in patterns):
                errors.append("Private path/credential pattern: " + str(path.relative_to(tree)))
            for token in denied:
                if re.search(r'(?i)(?<![A-Za-z0-9])' + re.escape(token) + r'(?![A-Za-z0-9])', text + "\n" + str(path.relative_to(tree))):
                    # Never print protected tokens into a publication log.
                    errors.append("Protected identifier in: " + str(path.relative_to(tree)))
                    break
    return dict(passed=not errors, scanned_files=scanned, graph_types=len(types), maya_types=len(catalog["nodes"])-len(types),
                aliases=len(catalog["aliases"]), c_functions=len(found), errors=errors)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--denylist", type=Path)
    parser.add_argument("--rendered", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = check(args.root.resolve(), args.denylist, args.rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
