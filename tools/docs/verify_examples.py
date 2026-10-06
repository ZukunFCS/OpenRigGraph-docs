"""Validate independent documentation graphs against an existing ORG SDK CLI."""
from __future__ import annotations

import argparse
import json
import math
import subprocess
from pathlib import Path


def verify(root, executable):
    catalog = json.loads((root / "docs/source/_generated/node_catalog.json").read_text())
    results = []
    for spec in catalog["nodes"]:
        if spec["layer"] != "graph":
            continue
        graph = root / spec["example_path"]
        validation = subprocess.run([str(executable), "validate", str(graph)], capture_output=True, text=True)
        evaluation = subprocess.run([str(executable), "eval", str(graph), "--output", "json"], capture_output=True, text=True)
        if spec["type"] == "RigLogic":
            # The CLI has no registered identity provider. Both compile-based
            # validation and evaluation may reject this missing dependency.
            passed = validation.returncode == 0 and evaluation.returncode != 0 and "failed to create instance" in evaluation.stderr.lower()
            result = dict(type=spec["type"], passed=passed, case="missing external provider")
        else:
            try:
                value = json.loads(evaluation.stdout)["result"]
            except (ValueError, KeyError):
                value = None
            passed = validation.returncode == 0 and evaluation.returncode == 0 and value is not None and math.isfinite(value) and abs(value - spec["expected"]) <= spec["tolerance"]
            result = dict(type=spec["type"], passed=passed, expected=spec["expected"], actual=value,
                          error=(validation.stderr + evaluation.stderr).strip() if not passed else "")
        results.append(result)
    # Alias resolution must agree numerically with the canonical node.
    for alias, canonical in catalog["aliases"].items():
        graph = json.loads((root / ("examples/graph/" + canonical + ".json")).read_text())
        graph["nodes"][0]["type"] = alias
        # Avoid mutating any source fixture: use a temporary file.
        import tempfile
        with tempfile.TemporaryDirectory(prefix="org-docs-alias-") as tmp:
            path = Path(tmp) / "alias.json"
            path.write_text(json.dumps(graph))
            p = subprocess.run([str(executable), "eval", str(path), "--output", "json"], capture_output=True, text=True)
            spec = next(n for n in catalog["nodes"] if n["type"] == canonical)
            try:
                value = json.loads(p.stdout)["result"]
                ok = p.returncode == 0 and abs(value-spec["expected"]) <= spec["tolerance"]
            except (ValueError, KeyError):
                ok = False
            results.append(dict(type=alias, canonical=canonical, passed=ok))
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--orgctl", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    results = verify(args.root.resolve(), args.orgctl.resolve())
    report = dict(cases=len(results), passed=sum(r["passed"] for r in results), results=results)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k:v for k,v in report.items() if k != "results"}, indent=2))
    failed = [r for r in results if not r["passed"]]
    if failed:
        print(json.dumps(failed, indent=2))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
