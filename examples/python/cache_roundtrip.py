"""Independent SDK Python example: dense/sparse numeric cache round trip."""
from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sdk-python", type=Path, help="SDK Python directory containing openriggraph; otherwise use PYTHONPATH")
    args = parser.parse_args()
    if args.sdk_python:
        sys.path.insert(0, str(args.sdk_python.resolve()))
    from openriggraph.curve_cache import write_curve_cache, read_curve_cache_row, read_curve_cache_metadata, compress_curve_cache
    with tempfile.TemporaryDirectory(prefix="org-cache-example-") as temp:
        dense = Path(temp) / "example.orgcache"
        sparse = Path(temp) / "example_sparse.orgcache"
        frames = [1.0, 1.5, 2.0]
        values = [[0.0, 2.0], [0.5, 2.0], [1.0, 2.0]]
        meta = write_curve_cache(dense, frames, values)
        assert (meta.sample_count, meta.value_count) == (3, 2)
        assert read_curve_cache_row(dense, 1) == (0.5, 2.0)
        compress_curve_cache(dense, sparse)
        assert read_curve_cache_metadata(sparse) == meta
        for i, expected in enumerate(values):
            assert read_curve_cache_row(sparse, i) == tuple(expected)
        print(json.dumps(dict(samples=3, channels=2, dense_and_sparse_equal=True)))


if __name__ == "__main__":
    main()
