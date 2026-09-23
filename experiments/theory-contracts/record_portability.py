"""Narrow replay normalization; never rewrites historical scientific records."""
from copy import deepcopy
import hashlib
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ORIGINAL_ROOT = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
SOURCE = "experiments/tfpt-discovery/seam_state_derivation_probe.py"
SOURCE_SHA = "5e54c416be72a125a8ce6e235b4300f9f9c2344b3ada796d2dc4c7e2ea01482b"


def portable_source_record(record, root=ROOT):
    """Canonicalize only one verified provenance path, not other record data."""
    if isinstance(record, list):
        return [portable_source_record(value, root) for value in record]
    if not isinstance(record, dict):
        return record
    result = {key: portable_source_record(value, root) for key, value in record.items()}
    path = record.get("source")
    if isinstance(path, str) and path.startswith("/"):
        allowed = {str(ORIGINAL_ROOT/SOURCE), str(Path(root).resolve()/SOURCE)}
        if path not in allowed or record.get("source_sha256") != SOURCE_SHA:
            raise ValueError("unrecognized source provenance path or hash")
        if hashlib.sha256((Path(root)/SOURCE).read_bytes()).hexdigest() != SOURCE_SHA:
            raise ValueError("source bytes differ from the frozen provenance hash")
        result["source"] = SOURCE
    return result


def carrier_source_record(record):
    """Check two numeric diagnostics against their existing exact source values.

    The pinned source already enforces these same strict 1e-12 bounds.
    All other fields, including every integer/boolean, compare unchanged.
    """
    result = deepcopy(record)
    for row in result["rows"]:
        sector = row["r"]
        if type(sector) is not int or sector not in range(4):
            raise ValueError("source sector in 0..3")
        expected = {"PH_identity_residual": 0.,
                    "opposite_holonomy_operator_difference": 2. if sector % 2 else 0.}
        for name, target in expected.items():
            value = row[name]
            if (type(value) not in (float, int) or not math.isfinite(value)
                    or value < 0 or abs(value-target) >= 1e-12):
                raise ValueError("source diagnostic violates its existing bound: " + name)
            row[name] = target
    return result
