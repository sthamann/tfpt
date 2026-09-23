#!/usr/bin/env python3
"""Exact static-register trace check for the frozen v1033 source.

This is a bounded algebra check of the existing block-diagonal register
Hamiltonian.  It does not add a Hamiltonian term or choose a new interaction.
The matter space is the original one-particle QWZ space at nx=3, ny=1.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path

import sympy as sp
import numpy as np


HERE = Path(__file__).resolve().parent
DEFAULT_REPO = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
SOURCE_REL = "verification/v1033_charged_disorder.py"
SOURCE_SHA256 = "01c64748c70784b17cf1c61b7bd2b4c51a69c19c4a2274f09028892eab5cb83f"
CONTRACT_REL = "experiments/theory-contracts/clock-interaction-provenance/README.md"
CONTRACT_SHA256 = "e40e116d86ee092e26317b2972cff8795fa7a1d22eb6a250e03f1f8c5252fa4c"
CHECK_COUNT = 0


def require(condition: bool, message: str) -> None:
    global CHECK_COUNT
    CHECK_COUNT += 1
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def add_block(out: sp.Matrix, row: int, col: int, block: sp.Matrix) -> None:
    for i in range(block.rows):
        for j in range(block.cols):
            out[row + i, col + j] += block[i, j]


def source_audit(repo: Path) -> dict[str, str]:
    source = repo / SOURCE_REL
    contract = repo / CONTRACT_REL
    require(source.is_file(), f"missing source pin: {source}")
    require(contract.is_file(), f"missing contract text: {contract}")
    require(sha256(source) == SOURCE_SHA256, "v1033 source SHA-256 changed")
    require(sha256(contract) == CONTRACT_SHA256, "clock contract SHA-256 changed")
    text = source.read_text(encoding="utf-8")
    contract_text = contract.read_text(encoding="utf-8")
    for needle in (
        "def register_hamiltonian(nx: int, ny: int)",
        "base = hs[0] - forward - forward.conj().T",
        "np.kron(np.eye(4), base)",
        "np.kron(z, forward)",
        "np.kron(z.conj().T, forward.conj().T)",
        "def seam_forward(nx: int, ny: int)",
    ):
        require(needle in text, f"missing v1033 source witness: {needle}")
    require("Register/Fock-Hebung und Präparation eine nichtgaußsche" in contract_text,
            "contract trace question no longer present")
    require("nicht als zusätzliches Register-Hamiltonian" in contract_text,
            "contract register-Hamiltonian boundary changed")
    return {
        "source": str(source),
        "source_sha256": SOURCE_SHA256,
        "contract": str(contract),
        "contract_sha256": CONTRACT_SHA256,
    }


SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.diag(1, -1)
TX = SX / (2 * sp.I) - SZ / 2
TY = SY / (2 * sp.I) - SZ / 2


def qwz_cylinder_exact(nx: int, ny: int, mass: sp.Expr, sector: int) -> sp.Matrix:
    dim = 2 * nx * ny
    h = sp.zeros(dim)

    def sl(x: int, y: int) -> int:
        return 2 * ((x % nx) * ny + y)

    phase = sp.I ** sector
    for x in range(nx):
        for y in range(ny):
            i = sl(x, y)
            add_block(h, i, i, mass * SZ)
            j = sl(x + 1, y)
            amp = phase if x == nx - 1 else sp.Integer(1)
            add_block(h, j, i, amp * TX)
            add_block(h, i, j, sp.conjugate(amp) * TX.conjugate().T)
            if y + 1 < ny:
                j = sl(x, y + 1)
                add_block(h, j, i, TY)
                add_block(h, i, j, TY.conjugate().T)
    return h


def seam_forward_exact(nx: int, ny: int) -> sp.Matrix:
    out = sp.zeros(2 * nx * ny)
    for y in range(ny):
        i = 2 * ((nx - 1) * ny + y)
        j = 2 * y
        add_block(out, j, i, TX)
    return out


def source_blocks(nx: int = 3, ny: int = 1) -> tuple[list[sp.Matrix], sp.Matrix, sp.Matrix]:
    hs = [qwz_cylinder_exact(nx, ny, sp.Integer(1), r) for r in range(4)]
    forward = seam_forward_exact(nx, ny)
    base = hs[0] - forward - forward.conjugate().T
    return hs, base, forward


def compare_original_functions(repo: Path, hs: list[sp.Matrix],
                               base: sp.Matrix, forward: sp.Matrix) -> None:
    """Run only the pinned original definitions; compare binary-exact dyadics."""
    tree = ast.parse((repo / SOURCE_REL).read_text(encoding="utf-8"))
    names = {"SX", "SY", "SZ", "TX", "TY"}
    functions = {"qwz_cylinder", "seam_forward", "register_hamiltonian"}
    nodes = [node for node in tree.body
             if (isinstance(node, ast.FunctionDef) and node.name in functions)
             or (isinstance(node, ast.Assign)
                 and any(isinstance(t, ast.Name) and t.id in names for t in node.targets))]
    require(len(nodes) == 8, "original definition extraction incomplete")
    scope = {"np": np}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(repo / SOURCE_REL), "exec"), scope)

    def exact(array):
        return sp.Matrix(array.shape[0], array.shape[1],
                         lambda i, j: sp.Rational(float(array[i, j].real))
                         + sp.I * sp.Rational(float(array[i, j].imag)))

    require(exact(scope["TX"]) == TX, "original seam coefficient mismatch")
    require(exact(scope["TY"]) == TY, "original transverse coefficient mismatch")
    for r in range(4):
        require(exact(scope["qwz_cylinder"](3, 1, 1.0, r)) == hs[r],
                f"original source block {r} differs from exact reconstruction")
    require(exact(scope["seam_forward"](3, 1)) == forward,
            "original seam operator mismatch")
    direct, linked = scope["register_hamiltonian"](3, 1)
    require(exact(direct) == block_diag(hs) == exact(linked),
            "original register matrix mismatch")
    require(sum(hs, sp.zeros(6)) / 4 == base, "phase average is not the source base")


def block_diag(blocks: list[sp.Matrix]) -> sp.Matrix:
    d = sum(block.rows for block in blocks)
    out = sp.zeros(d)
    offset = 0
    for block in blocks:
        add_block(out, offset, offset, block)
        offset += block.rows
    return out


def partial_trace_register(mat: sp.Matrix, dreg: int, dmatter: int) -> sp.Matrix:
    out = sp.zeros(dmatter)
    for r in range(dreg):
        for i in range(dmatter):
            for j in range(dmatter):
                out[i, j] += mat[r * dmatter + i, r * dmatter + j]
    return out


def pure_density(dim: int, index: int) -> sp.Matrix:
    out = sp.zeros(dim)
    out[index, index] = 1
    return out


def series_unitary(h: sp.Matrix, t: sp.Symbol) -> sp.Matrix:
    return sp.eye(h.rows) - sp.I * t * h - t**2 * h**2 / 2


def truncate_t2(expr: sp.Expr, t: sp.Symbol) -> sp.Expr:
    return sp.expand(expr).series(t, 0, 3).removeO().expand()


def trace(mat: sp.Matrix) -> sp.Expr:
    return sp.trace(mat).expand()


def check_source_and_register(hs: list[sp.Matrix], base: sp.Matrix,
                              forward: sp.Matrix) -> dict[str, object]:
    dm = hs[0].rows
    z = sp.diag(1, sp.I, -1, -sp.I)
    h_register = block_diag(hs)
    linked = sp.kronecker_product(sp.eye(4), base)
    linked += sp.kronecker_product(z, forward)
    linked += sp.kronecker_product(z.conjugate().T, forward.conjugate().T)
    p = [sp.diag(*[1 if s == r else 0 for s in range(4)]) for r in range(4)]
    projectors = [sp.kronecker_product(p_r, sp.eye(dm)) for p_r in p]
    require(h_register == linked, "source h_r do not reconstruct v1033 register Hamiltonian")
    require(all(h_register * q == q * h_register for q in projectors),
            "register phase projectors do not commute with H_R")
    require(hs[0] - base == forward + forward.conjugate().T,
            "r=0 source block is not the seam base plus seam adjoint")
    require(all(hs[r] - base == (sp.I**r) * forward
                + sp.conjugate(sp.I**r) * forward.conjugate().T
                for r in range(4)),
            "source h_r phase differences are not the original TX seam")
    require(hs[0][4, 4] == hs[1][4, 4] == hs[2][4, 4] == hs[3][4, 4],
            "Ny=1 onsite convention changed across register sectors")
    return {"matter_dimension": dm, "register_dimension": 4}


def check_trace_channel(hs: list[sp.Matrix]) -> dict[str, str]:
    dm = hs[0].rows
    t = sp.Symbol("t", real=True)
    rho = pure_density(dm, 4)  # x=nx-1, y=0, first orbital: departing seam orbital
    hbar = sum(hs, sp.zeros(dm)) / 4
    deltas = [h - hbar for h in hs]
    variances = []
    for delta in deltas:
        mean = (rho * delta).trace()
        second = (rho * delta * delta).trace()
        variances.append(sp.simplify(second - mean**2))
    coeff_loss = sp.simplify(2 * sum(variances) / 4)
    require(coeff_loss == 1, "purity-loss coefficient is not the expected exact one")

    rho_terms = []
    for h in hs:
        a = -sp.I * (h * rho - rho * h)
        b = -(h * (h * rho - rho * h) - (h * rho - rho * h) * h) / 2
        rho_terms.append((a, b))
    a_bar = sum((a for a, _ in rho_terms), sp.zeros(dm)) / 4
    b_bar = sum((b for _, b in rho_terms), sp.zeros(dm)) / 4
    rho_t = rho + t * a_bar + t**2 * b_bar
    purity = truncate_t2(trace(rho_t * rho_t), t)
    require(purity == 1 - t**2, "exact short-time purity series is not 1-t^2")
    require(trace(a_bar) == 0 and trace(b_bar) == 0,
            "short-time channel does not preserve trace through order t^2")

    # Register coherences vanish under the register partial trace.  The test
    # uses every matrix unit E_ab and the same exact order-two unitary series.
    u_blocks = [series_unitary(h, t) for h in hs]
    u = block_diag(u_blocks)
    offdiag_zero = True
    diag_matches = True
    for a in range(4):
        for b in range(4):
            eab = sp.zeros(4)
            eab[a, b] = 1
            lifted = sp.kronecker_product(eab, rho)
            reduced = partial_trace_register(u * lifted * u.conjugate().T, 4, dm)
            reduced = reduced.applyfunc(lambda x: truncate_t2(x, t))
            if a != b:
                offdiag_zero = offdiag_zero and reduced == sp.zeros(dm)
            else:
                expected = (u_blocks[a] * rho * u_blocks[a].conjugate().T)
                expected = expected.applyfunc(lambda x: truncate_t2(x, t))
                diag_matches = diag_matches and reduced == expected
    require(offdiag_zero, "register coherences survived the exact partial trace")
    require(diag_matches, "diagonal register trace weights do not give U_r rho U_r^dagger")

    # The same output is confined to N=1.  Its Wick four-point defect is a
    # direct consequence of the purity loss, evaluated through order t^2.
    c = rho_t.T
    wick_pair = sum((c[i, i] * c[j, j] - c[i, j] * c[j, i]
                     for i in range(dm) for j in range(i + 1, dm)), sp.Integer(0))
    defect = truncate_t2(-wick_pair, t)  # actual <n_i n_j> is zero in N=1
    require(defect == -t**2 / 2,
            "one-particle Wick defect does not equal -(1-purity)/2 through t^2")
    return {
        "initial_state": "one-particle orbital (x=2,y=0,spin=0), departing seam",
        "hbar_variance_sum": str(sp.simplify(sum(variances) / 4)),
        "purity_series": str(purity),
        "purity_loss_coefficient": str(coeff_loss),
        "wick_defect_series": str(defect),
    }


def run(repo: Path, output: Path) -> dict[str, object]:
    global CHECK_COUNT
    CHECK_COUNT = 0
    pins = source_audit(repo)
    source_checks = CHECK_COUNT
    hs, base, forward = source_blocks(3, 1)
    compare_original_functions(repo, hs, base, forward)
    register = check_source_and_register(hs, base, forward)
    channel = check_trace_channel(hs)
    manifest = HERE / "source_manifest.json"
    require(manifest.is_file(), "missing source/artifact manifest")
    manifest_checks = 1
    for item in json.loads(manifest.read_text())["files"]:
        require(sha256(repo / item["path"]) == item["sha256"],
                f"manifest changed: {item['path']}")
        manifest_checks += 1
    result = {
        "scope": "static v1033 C4 register traced from an independent matter register",
        "verdict": "PASS",
        "checks": CHECK_COUNT - source_checks - manifest_checks,
        "source_pin_checks": source_checks,
        "manifest_checks": manifest_checks,
        "total_requirements": CHECK_COUNT,
        "source_pins": pins,
        "register": register,
        "channel": channel,
        "boundaries": [
            "conditional C4 tensor Fock(V) register lift only",
            "no new interaction or Hamiltonian term",
            "does not establish a native source-derived non-Gaussian Hamiltonian",
            "Ny=1 uses the original v1033 periodic-x/open-y convention",
        ],
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=DEFAULT_REPO)
    parser.add_argument("--output", type=Path, default=HERE / "certificate.json")
    args = parser.parse_args()
    result = run(args.repo_root.resolve(), args.output.resolve())
    print(json.dumps({"verdict": result["verdict"], "checks": result["checks"],
                      "output": str(args.output.resolve())}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
