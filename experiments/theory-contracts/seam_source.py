"""Read-only extraction of the existing exact finite seam constructor.

Execute only main()'s source prefix before Aint_f, which builds the bit model,
the selected C6 action, and integer wiring. No KMS or spectral target is read.
The precise prefix/full-source SHA256 is returned for provenance.
"""
import ast
import contextlib
import hashlib
import importlib.util
import io
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "experiments/tfpt-discovery/seam_state_derivation_probe.py"


def construct():
    source = SOURCE.read_text()
    spec = importlib.util.spec_from_file_location("audit_source_seam", SOURCE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    tree = ast.parse(source)
    original = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "main")
    body = []
    for node in original.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "Aint_f" for t in node.targets):
            break
        body.append(node)
    else:
        raise RuntimeError("Source-prefix endpoint changed")
    last_line = body[-1].end_lineno
    body.append(ast.Return(value=ast.Call(func=ast.Name(id="locals", ctx=ast.Load()), args=[], keywords=[])))
    original.name = "audit_construct"
    original.body = body
    extract = ast.fix_missing_locations(ast.Module(body=[original], type_ignores=[]))
    exec(compile(extract, str(SOURCE), "exec"), module.__dict__)
    log = io.StringIO()
    with contextlib.redirect_stdout(log):
        data = module.audit_construct()
    if not all(bool(row[1]) for row in module.CHECKS):
        raise RuntimeError(log.getvalue())
    data["provenance"] = {
        "source": str(SOURCE),
        "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "prefix_last_line": last_line,
        "prefix_sha256": hashlib.sha256("\n".join(source.splitlines()[:last_line]).encode()).hexdigest(),
        "source_checks": len(module.CHECKS),
        "log": log.getvalue(),
    }
    return data
