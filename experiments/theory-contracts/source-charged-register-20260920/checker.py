#!/usr/bin/env python3
"""Exact finite charged-register completion for the frozen v1033 source.

The calculation is deliberately bounded to nx=3, ny=1.  It checks the
conditional C4 tensor Fock(V) encoding and the actual v1033 disorder string;
it does not add a Hamiltonian or claim a source-derived interacting theory.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import ast
from collections import defaultdict
from pathlib import Path

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent
DEFAULT_REPO = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
SOURCE_REL = "verification/v1033_charged_disorder.py"
SOURCE_SHA256 = "01c64748c70784b17cf1c61b7bd2b4c51a69c19c4a2274f09028892eab5cb83f"
STATIC_CHECKER = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/source-static-register-20260920/checker.py")
STATIC_SHA256 = "d4366eb7e45453b81e722621cb9a3829af5834a9aad75890b05d2eb6bbf3a093"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Op:
    """Small exact sparse matrix with SymPy Gaussian/rational entries."""

    def __init__(self, rows: int, cols: int | None = None,
                 data: dict[tuple[int, int], sp.Expr] | None = None):
        self.rows = rows
        self.cols = rows if cols is None else cols
        clean: dict[tuple[int, int], sp.Expr] = {}
        for key, value in (data or {}).items():
            require(0 <= key[0] < self.rows and 0 <= key[1] < self.cols,
                    "sparse entry outside matrix shape")
            value = sp.simplify(value)
            if value != 0:
                clean[key] = value
        self.data = clean

    @property
    def dim(self) -> int:
        require(self.rows == self.cols, "rectangular operator has no square dimension")
        return self.rows

    @classmethod
    def zero(cls, dim: int) -> "Op":
        return cls(dim)

    @classmethod
    def identity(cls, dim: int) -> "Op":
        return cls(dim, data={(i, i): sp.Integer(1) for i in range(dim)})

    def copy(self) -> "Op":
        return Op(self.rows, self.cols, dict(self.data))

    def __add__(self, other: "Op") -> "Op":
        require((self.rows, self.cols) == (other.rows, other.cols),
                "dimension mismatch in addition")
        out = defaultdict(lambda: sp.Integer(0))
        for key, value in self.data.items():
            out[key] += value
        for key, value in other.data.items():
            out[key] += value
        return Op(self.rows, self.cols, dict(out))

    def __sub__(self, other: "Op") -> "Op":
        return self + other.scale(-1)

    def scale(self, factor: sp.Expr) -> "Op":
        return Op(self.rows, self.cols,
                  {key: factor * value for key, value in self.data.items()})

    def __matmul__(self, other: "Op") -> "Op":
        require(self.cols == other.rows, "dimension mismatch in product")
        rows: dict[int, list[tuple[int, sp.Expr]]] = defaultdict(list)
        for (row, col), value in other.data.items():
            rows[row].append((col, value))
        out = defaultdict(lambda: sp.Integer(0))
        for (row, mid), left in self.data.items():
            for col, right in rows.get(mid, []):
                out[(row, col)] += left * right
        return Op(self.rows, other.cols, dict(out))

    def dagger(self) -> "Op":
        return Op(self.cols, self.rows, {(col, row): sp.conjugate(value)
                                         for (row, col), value in self.data.items()})

    def __eq__(self, other: object) -> bool:
        return (isinstance(other, Op)
                and (self.rows, self.cols) == (other.rows, other.cols)
                and self.data == other.data)

    def witness(self) -> tuple[int, int, str] | None:
        if not self.data:
            return None
        row, col = sorted(self.data)[0]
        return row, col, str(self.data[(row, col)])


class CheckBook:
    """Fail-closed checks whose counts come from executed checks."""

    def __init__(self) -> None:
        self._counts: defaultdict[str, int] = defaultdict(int)

    def check(self, category: str, condition: bool, message: str) -> None:
        self._counts[category] += 1
        if not condition:
            raise RuntimeError(message)

    def counts(self) -> dict[str, int]:
        return dict(sorted(self._counts.items()))

    def total(self) -> int:
        return sum(self._counts.values())


def diag(values: list[sp.Expr]) -> Op:
    return Op(len(values), data={(i, i): value for i, value in enumerate(values)})


def dense(rows: list[list[sp.Expr]]) -> Op:
    return Op(len(rows), data={(i, j): value for i, row in enumerate(rows)
                               for j, value in enumerate(row) if value != 0})


def kron(left: Op, right: Op) -> Op:
    data = {}
    for (i, j), a in left.data.items():
        for (k, l), b in right.data.items():
            data[(i * right.rows + k, j * right.cols + l)] = a * b
    return Op(left.rows * right.rows, left.cols * right.cols, data)


def comm(left: Op, right: Op) -> Op:
    return left @ right - right @ left


def add_block(out: Op, row0: int, col0: int, block: Op) -> Op:
    require(block.dim == 2, "source block must be two by two")
    data = dict(out.data)
    for (row, col), value in block.data.items():
        key = (row0 + row, col0 + col)
        data[key] = data.get(key, sp.Integer(0)) + value
    return Op(out.dim, data=data)


def fock_ops(n_modes: int) -> tuple[list[Op], list[Op], Op, list[int]]:
    dim = 1 << n_modes
    annihilators: list[Op] = []
    numbers: list[Op] = []
    occupations = [mask.bit_count() for mask in range(dim)]
    for mode in range(n_modes):
        entries = {}
        for mask in range(dim):
            if mask & (1 << mode):
                sign = -1 if (mask & ((1 << mode) - 1)).bit_count() % 2 else 1
                entries[(mask ^ (1 << mode), mask)] = sign
        c = Op(dim, data=entries)
        annihilators.append(c)
        numbers.append(c.dagger() @ c)
    return annihilators, numbers, diag([sp.Integer(n) for n in occupations]), occupations


def dgamma(h: Op, creators: list[Op], annihilators: list[Op]) -> Op:
    out = Op.zero(creators[0].dim)
    for (i, j), value in h.data.items():
        out = out + (creators[i] @ annihilators[j]).scale(value)
    return out


def verify_adjacent_manifest(repo: Path) -> dict[str, object]:
    """Verify an installed contract manifest; absence is allowed in work mode."""
    manifest = HERE / "source_manifest.json"
    if not manifest.is_file():
        if (HERE / "contract_index.json").is_file():
            require(False, "installed contract has contract_index.json but no source_manifest.json")
        return {"status": "absent-allowed-work-mode", "path": str(manifest), "pins": 0}
    raw = json.loads(manifest.read_text(encoding="utf-8"))
    entries = raw.get("files", raw.get("original_files", []))
    if isinstance(entries, dict):
        entries = [{"path": path, "sha256": digest}
                   for path, digest in entries.items()]
    require(isinstance(entries, list) and bool(entries),
            "source_manifest files must be a nonempty list or mapping")
    checked = 0
    for entry in entries:
        require(isinstance(entry, dict) and "path" in entry and "sha256" in entry,
                "malformed source_manifest entry")
        path = Path(str(entry["path"]))
        candidate = path if path.is_absolute() else repo / path
        require(candidate.is_file(), f"manifest-pinned file missing: {candidate}")
        require(sha256(candidate) == str(entry["sha256"]),
                f"manifest pin changed: {candidate}")
        checked += 1
    return {"status": "verified", "path": str(manifest), "pins": checked}


def source_audit(repo: Path) -> dict[str, object]:
    source = repo / SOURCE_REL
    require(source.is_file(), f"missing source: {source}")
    require(STATIC_CHECKER.is_file(), f"missing prior checker: {STATIC_CHECKER}")
    require(sha256(source) == SOURCE_SHA256, "v1033 source SHA-256 changed")
    require(sha256(STATIC_CHECKER) == STATIC_SHA256, "static-register checker SHA-256 changed")
    text = source.read_text(encoding="utf-8")
    for needle in (
        "def register_hamiltonian(nx: int, ny: int)",
        "def sharp_arc_phase(nx: int, ny: int, endpoint: int)",
        "full_disorder = np.kron(shift, u)",
        "shift = np.roll(np.eye(4), 1, axis=0)",
        "base = hs[0] - forward - forward.conj().T",
        "np.kron(z, forward)",
    ):
        require(needle in text, f"missing v1033 source witness: {needle}")
    compare_original_source(repo, text)
    manifest = verify_adjacent_manifest(repo)
    return {
        "source": str(source),
        "source_sha256": SOURCE_SHA256,
        "previous_checker": str(STATIC_CHECKER),
        "previous_checker_sha256": STATIC_SHA256,
        "adjacent_manifest": manifest,
        "original_adapter": "AST-extracted source definitions executed and compared",
    }


SX = dense([[0, 1], [1, 0]])
SY = dense([[0, -sp.I], [sp.I, 0]])
SZ = diag([1, -1])
TX = SX.scale(1 / (2 * sp.I)) - SZ.scale(sp.Rational(1, 2))
TY = SY.scale(1 / (2 * sp.I)) - SZ.scale(sp.Rational(1, 2))


def source_hamiltonians(nx: int = 3, ny: int = 1) -> tuple[list[Op], Op, Op]:
    require((nx, ny) == (3, 1), "checker is intentionally bounded to nx=3, ny=1")
    hs: list[Op] = []
    for sector in range(4):
        h = Op.zero(2 * nx * ny)
        for x in range(nx):
            for y in range(ny):
                i = 2 * (x * ny + y)
                h = add_block(h, i, i, SZ)
                j = 2 * (((x + 1) % nx) * ny + y)
                amp = sp.I**sector if x == nx - 1 else sp.Integer(1)
                h = add_block(h, j, i, TX.scale(amp))
                h = add_block(h, i, j, TX.dagger().scale(sp.conjugate(amp)))
                if y + 1 < ny:
                    j = 2 * (x * ny + y + 1)
                    h = add_block(h, j, i, TY)
                    h = add_block(h, i, j, TY.dagger())
        hs.append(h)
    forward = Op.zero(6)
    forward = add_block(forward, 0, 4, TX)
    base = hs[0] - forward - forward.dagger()
    return hs, base, forward


def _array_to_op(array: np.ndarray) -> Op:
    """Convert the pinned source adapter's exact-valued NumPy output."""
    data: dict[tuple[int, int], sp.Expr] = {}
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            value = complex(array[i, j])
            real = sp.Rational(str(float(value.real)))
            imag = sp.Rational(str(float(value.imag)))
            exact = real + sp.I * imag
            if exact != 0:
                data[(i, j)] = exact
    return Op(array.shape[0], array.shape[1], data)


def _block_diag_ops(blocks: list[Op]) -> Op:
    size = sum(block.rows for block in blocks)
    out: dict[tuple[int, int], sp.Expr] = {}
    offset = 0
    for block in blocks:
        for (row, col), value in block.data.items():
            out[(offset + row, offset + col)] = value
        offset += block.rows
    return Op(size, size, out)


def compare_original_source(repo: Path, source_text: str) -> None:
    """Execute the original AST definitions and compare their nx=3 output."""
    tree = ast.parse(source_text)
    names = {"SX", "SY", "SZ", "TX", "TY"}
    functions = {"qwz_cylinder", "seam_forward", "register_hamiltonian"}
    nodes = [node for node in tree.body
             if (isinstance(node, ast.FunctionDef) and node.name in functions)
             or (isinstance(node, ast.Assign)
                 and any(isinstance(target, ast.Name) and target.id in names
                         for target in node.targets))]
    require(len(nodes) == 8, "original v1033 definition extraction incomplete")
    scope = {"np": np}
    exec(compile(ast.Module(body=nodes, type_ignores=[]),
                 str(repo / SOURCE_REL), "exec"), scope)
    hs, base, forward = source_hamiltonians()
    original_hs = [_array_to_op(scope["qwz_cylinder"](3, 1, 1.0, r))
                   for r in range(4)]
    original_forward = _array_to_op(scope["seam_forward"](3, 1))
    require(original_hs == hs, "AST-extracted source one-body blocks differ")
    require(original_forward == forward, "AST-extracted source seam differs")
    direct, linked = scope["register_hamiltonian"](3, 1)
    require(_array_to_op(direct) == _block_diag_ops(hs),
            "original register_hamiltonian direct output differs")
    require(_array_to_op(linked) == _block_diag_ops(hs),
            "original register_hamiltonian linked output differs")
    require(sum(hs, Op.zero(6)).scale(sp.Rational(1, 4)) - base == Op.zero(6),
            "phase average is not the source base")


def powers_i(exponent: int) -> sp.Expr:
    return sp.I**exponent


def build_system() -> dict[str, object]:
    hs, base, forward = source_hamiltonians()
    annihilators, numbers, number_op, occupations = fock_ops(6)
    creators = [c.dagger() for c in annihilators]
    matter_dim = 64
    q = [1, 1, 0, 0, 0, 0]
    u_one = diag([powers_i(value) for value in q])
    gamma_u = diag([powers_i(sum(q[j] for j in range(6) if mask & (1 << j)))
                    for mask in range(matter_dim)])
    i_number = diag([powers_i(value) for value in occupations])
    z = diag([1, sp.I, -1, -sp.I])
    shift = Op(4, data={((r + 1) % 4, r): 1 for r in range(4)})
    projectors = [diag([1 if r == s else 0 for r in range(4)]) for s in range(4)]
    h_prime = [diag([powers_i(-r * value) for value in q]) @ hs[r]
                @ diag([powers_i(r * value) for value in q]) for r in range(4)]
    dgs = [dgamma(h, creators, annihilators) for h in hs]
    dgs_prime = [dgamma(h, creators, annihilators) for h in h_prime]
    H = Op.zero(256)
    for r in range(4):
        H = H + kron(projectors[r], dgs[r])
    T = diag([powers_i(r * sum(q[j] for j in range(6) if mask & (1 << j)))
              for r in range(4) for mask in range(matter_dim)])
    D = kron(shift, gamma_u)
    C = kron(z, i_number)
    F_plain = [kron(shift, annihilators[j]) for j in range(6)]
    F_u = [T @ f @ T.dagger() for f in F_plain]
    F_formula = []
    for j in range(6):
        zpow = diag([powers_i(-q[j] * r) for r in range(4)])
        F_formula.append(kron(shift @ zpow, gamma_u @ annihilators[j]))
    Js: list[Op] = []
    Jsu: list[Op] = []
    Hs: list[Op] = []
    Dquads: list[Op] = []
    for s in range(4):
        data = {}
        for mask in range(matter_dim):
            register = (s - occupations[mask]) % 4
            data[(register * matter_dim + mask, mask)] = 1
        j = Op(256, 64, data)
        ju = T @ j
        Js.append(j)
        Jsu.append(ju)
        Hs.append(ju.dagger() @ H @ ju)
        Dquads.append(dgs_prime[(s - 1) % 4])
    return {
        "hs": hs, "base": base, "forward": forward,
        "annihilators": annihilators, "creators": creators,
        "numbers": numbers, "number_op": number_op, "occupations": occupations,
        "q": q, "u_one": u_one, "gamma_u": gamma_u, "i_number": i_number,
        "z": z, "shift": shift, "projectors": projectors,
        "h_prime": h_prime, "dgs": dgs, "dgs_prime": dgs_prime,
        "H": H, "T": T, "D": D, "C": C, "F_u": F_u,
        "F_formula": F_formula, "Js": Js, "Jsu": Jsu,
        "Hs": Hs, "Dquads": Dquads,
    }


def sector_entries(op: Op, occupations: list[int], n: int) -> dict[tuple[int, int], sp.Expr]:
    return {(row, col): value for (row, col), value in op.data.items()
            if occupations[row] == n and occupations[col] == n}


def first_nonzero(op: Op) -> tuple[int, int, str]:
    witness = op.witness()
    require(witness is not None, "expected a nonzero exact operator")
    return witness


def run_checks(repo: Path) -> dict[str, object]:
    pins = source_audit(repo)
    book = CheckBook()

    def require(condition: bool, message: str) -> None:
        lowered = message.lower()
        if any(word in lowered for word in ("naive", "disorder car")):
            category = "naive_disorder_control"
        elif any(word in lowered for word in ("locality", "offcut", "delta h", "h_cut",
                                               "matrix element", "commutator")):
            category = "locality_control"
        elif any(word in lowered for word in ("car", "canonical", "c4", "unitary",
                                               "commute", "charge", "formula", "controlled")):
            category = "canonical_car_and_charge"
        elif any(word in lowered for word in ("sector", "isometry", "overlap", "resolution",
                                               "hj=", "n=", "h0")):
            category = "encoded_sectors_and_dynamics"
        else:
            category = "source_and_gauge"
        book.check(category, condition, message)

    data = build_system()
    hs: list[Op] = data["hs"]
    h_prime: list[Op] = data["h_prime"]
    H: Op = data["H"]
    T: Op = data["T"]
    D: Op = data["D"]
    C: Op = data["C"]
    F_u: list[Op] = data["F_u"]
    F_formula: list[Op] = data["F_formula"]
    Jsu: list[Op] = data["Jsu"]
    Hs: list[Op] = data["Hs"]
    Dquads: list[Op] = data["Dquads"]
    projectors: list[Op] = data["projectors"]
    annihilators: list[Op] = data["annihilators"]
    creators: list[Op] = data["creators"]
    numbers: list[Op] = data["numbers"]
    occupations: list[int] = data["occupations"]
    identity64 = Op.identity(64)
    identity256 = Op.identity(256)
    total_number = kron(Op.identity(4), data["number_op"])
    parity = kron(Op.identity(4), diag([(-1) ** n for n in occupations]))

    require(H == sum((kron(projectors[r], data["dgs"][r]) for r in range(4)), Op.zero(256)),
            "four-sector H_R reconstruction failed")
    require(all(h_prime[r] == diag([powers_i(-r * x) for x in data["q"]]) @ hs[r]
                @ diag([powers_i(r * x) for x in data["q"]]) for r in range(4)),
            "gauge-moved h'_r is not u^-r h_r u^r")
    require(all(h_prime[r].data.get((0, 4), 0) == TX.data.get((0, 0), 0)
                for r in range(4)), "seam phase was not removed from x2 to x0")
    require(h_prime[1].data.get((2, 0), 0) == TX.scale(sp.I).data.get((0, 0), 0),
            "r=1 phase did not move to link x0 to x1")
    require(h_prime[2].data.get((2, 0), 0) == TX.scale(-1).data.get((0, 0), 0),
            "r=2 moved-link phase mismatch")

    require(T.dagger() @ T == identity256 and T @ T.dagger() == identity256,
            "controlled gauge T is not unitary")
    require(D.dagger() @ D == identity256, "actual disorder D=S Gamma(u) is not unitary")
    require(C @ D @ C.dagger() == D.scale(sp.I), "D has wrong C4 charge")
    require(C @ D == D @ C.scale(sp.I), "CD=i DC intertwiner failed")
    require(C @ H == H @ C, "C does not commute with H_R")
    require(all(C @ f == f @ C for f in F_u), "C does not commute with canonical charged F_i")
    require(all(total_number @ f - f @ total_number == f.scale(-1) for f in F_u),
            "canonical charged F_i have wrong number charge")
    require(all(parity @ f @ parity == f.scale(-1) for f in F_u),
            "canonical charged F_i are not odd under matter parity")

    for j in range(6):
        require(F_u[j] == F_formula[j], f"canonical F_{j} formula mismatch")
    for i in range(6):
        for j in range(6):
            require(F_u[i] @ F_u[j] + F_u[j] @ F_u[i] == Op.zero(256),
                    f"CAR annihilator bracket failed ({i},{j})")
            expected = identity256 if i == j else Op.zero(256)
            require(F_u[i] @ F_u[j].dagger() + F_u[j].dagger() @ F_u[i] == expected,
                    f"CAR mixed bracket failed ({i},{j})")

    resolution = sum((J @ J.dagger() for J in Jsu), Op.zero(256))
    require(resolution == identity256, "four encoded sector isometries do not resolve full space")
    for s in range(4):
        require(Jsu[s].dagger() @ Jsu[s] == identity64, f"J_{s} is not an isometry")
        for t in range(s):
            require(Jsu[s].dagger() @ Jsu[t] == Op.zero(64), "encoded sectors overlap")
        require(H @ Jsu[s] == Jsu[s] @ Hs[s], f"full HJ=JH_s failed for s={s}")
        require(D @ Jsu[s] == Jsu[(s + 1) % 4],
                f"original disorder D J_{s}=J_{s+1} intertwiner failed")
        for j in range(6):
            require(F_u[j] @ Jsu[s] == Jsu[s] @ annihilators[j],
                    f"F_{j} J_{s}=J_{s} c_{j} failed")
            require(F_u[j].dagger() @ Jsu[s] == Jsu[s] @ creators[j],
                    f"F_{j}^dagger J_{s}=J_{s} c_{j}^dagger failed")

        expected_data: dict[tuple[int, int], sp.Expr] = {}
        for row in range(64):
            n_row = occupations[row]
            r = (s - n_row) % 4
            for (rr, col), value in data["dgs_prime"][r].data.items():
                if rr == row and occupations[col] == n_row:
                    expected_data[(rr, col)] = value
        expected_hs = Op(64, data=expected_data)
        require(Hs[s] == expected_hs,
                f"independent all-N reconstruction of H_{s} failed")

    for s in range(4):
        delta = Hs[s] - Dquads[s]
        require(not sector_entries(delta, occupations, 0), f"N=0 mismatch for s={s}")
        require(not sector_entries(delta, occupations, 1), f"N=1 mismatch for s={s}")
        require(sector_entries(delta, occupations, 2), f"N=2 mismatch absent for s={s}")

    # The naive product D c_i is not a CAR field when one orbital lies inside
    # the sharp string and the other lies outside it.
    bare_c = [kron(Op.identity(4), annihilators[j]) for j in range(6)]
    naive = [D @ c for c in bare_c]
    naive_defect = naive[0] @ naive[2].dagger() + naive[2].dagger() @ naive[0]
    require(naive_defect != Op.zero(256), "naive D c_i unexpectedly obeys mixed CAR")
    naive_witness = first_nonzero(naive_defect)
    naive_plain_defect = naive[0] @ naive[2] + naive[2] @ naive[0]
    require(naive_plain_defect != Op.zero(256),
            "naive {D c_0,D c_2} unexpectedly vanished")
    naive_plain_witness = first_nonzero(naive_plain_defect)

    # Delta H and the actual phase-dependent cut differ by a fixed local
    # cut operator. Their commutators with offcut modes agree; check this
    # equality explicitly instead of identifying the two Hamiltonians.
    # The three-site ring is not a test of arbitrarily remote separation.
    delta_h = Hs[0] - Dquads[0]
    cut_forward = add_block(Op.zero(6), 2, 0, TX)
    cut_a = dgamma(cut_forward, creators, annihilators)
    cut_phase = diag([powers_i(-n) for n in occupations])
    H_cut = cut_phase @ cut_a + cut_phase.dagger() @ cut_a.dagger()
    require(Hs[0].data.get((4, 1), 0) == sp.I / 2,
            "exact H_0 matrix element <2|H_0|0> != i/2")
    require(Hs[0].data.get((20, 17), 0) == sp.Rational(1, 2),
            "exact H_0 matrix element <2,4|H_0|0,4> != 1/2")
    c4 = annihilators[4]
    c5 = annihilators[5]
    n0 = numbers[0]
    local_first = comm(H_cut, c4)
    local_double = comm(local_first, n0)
    local_bilinear = comm(H_cut, creators[4] @ annihilators[5])
    require(local_first == comm(delta_h, c4),
            "offcut H_cut and Delta H commutators differ")
    require(local_bilinear == comm(delta_h, creators[4] @ annihilators[5]),
            "offcut neutral H_cut and Delta H commutators differ")
    require(local_first != Op.zero(64), "locality witness [H_cut,c4] vanished")
    require(local_double != Op.zero(64), "locality witness [[H_cut,c4],n0] vanished")
    require(local_bilinear == Op.zero(64), "neutral offcut bilinear failed to commute")

    result = {
        "verdict": "PASS",
        "scope": "exact nx=3, ny=1 v1033 charged-register completion",
        "dimensions": {"matter_fock": 64, "register_matter": 256,
                       "one_body": 6, "register": 4},
        "source_pins": pins,
        "checks": book.counts(),
        "check_total": book.total(),
        "canonical_field": "F_j^u = S Z^(-q_j) tensor Gamma(u) c_j, q=(1,1,0,0,0,0)",
        "gauge_move": "u^(-r) h_r u^r moves the r seam phase x2->x0 to x0->x1",
        "naive_disorder_car_defect": {
            "pair": [0, 2],
            "witness": list(naive_witness),
            "plain_product_witness": list(naive_plain_witness),
            "meaning": "D c_i is not a CAR field across one in-string and one out-of-string orbital",
        },
        "fixed_N_comparison": {
            "N0": "zero",
            "N1": "zero; equals dGamma(h'_(s-1))",
            "N2": "nonzero; number-dependent twist remains",
            "N2_witness_s0": list(first_nonzero(sector_difference(delta_h, occupations, 2))),
            "H0_matrix_elements": {
                "<2|H0|0>": str(Hs[0].data[(4, 1)]),
                "<2,4|H0|0,4>": str(Hs[0].data[(20, 17)]),
            },
        },
        "locality": {
            "operator": "H_cut = i^(-N) dGamma(a_cut) + i^N dGamma(a_cut)^dagger",
            "comparison": "offcut commutators equal those of Delta H = H_0 - dGamma(h'_3)",
            "first_commutator_witness": list(first_nonzero(local_first)),
            "double_commutator_witness": list(first_nonzero(local_double)),
            "neutral_bilinear": "[H_cut,c4^dagger c5]=0",
            "ring_boundary": "nx=3 periodic ring; no arbitrary remote separation claimed",
        },
        "boundaries": [
            "conditional C4 tensor Fock(V) encoding",
            "actual v1033 disorder is D=S tensor Gamma(u), not bare S",
            "fixed-N H_s blocks are free; no native interacting Hamiltonian derived",
            "general remote locality obstruction remains the parent's analytic result",
        ],
    }
    return result


def sector_difference(op: Op, occupations: list[int], n: int) -> Op:
    return Op(op.rows, op.cols, sector_entries(op, occupations, n))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=DEFAULT_REPO)
    parser.add_argument("--output", type=Path, default=HERE / "certificate.json")
    args = parser.parse_args()
    result = run_checks(args.repo_root.resolve())
    args.output.resolve().parent.mkdir(parents=True, exist_ok=True)
    args.output.resolve().write_text(json.dumps(result, indent=2, sort_keys=True) + "\n",
                                      encoding="utf-8")
    print(json.dumps({"verdict": result["verdict"], "checks": result["checks"],
                      "output": str(args.output.resolve())}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
