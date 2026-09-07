#!/usr/bin/env python3
"""Exact full-lattice charged carry lift; no microscopic scaling/TOE claim."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import os
from pathlib import Path
import subprocess
import sys

import sympy as sp


FROZEN = {
    "experiments/theory-contracts/matter-geometry-round15/PROOF.md":
        "707c585ca07f4a675390222ed53fef1d093e938ac6a3d2e3cf33c0825d255f51",
    "experiments/theory-contracts/matter-geometry-round15/eight_channel_bridge_check.py":
        "18a5938053a1d3532db3fdaa13381cafc4566de0fb1ec2e559fb46a32b4a9bfd",
    "verification/v983_simple_current_generator.py":
        "769a9c5cb5e6518d8d2a445d347150f5ce0d1410c95db263ca2db72466e176c8",
    "verification/v988_psi_lambda_reduction.py":
        "eae02e79be5703ccec67f1f11470e3ffd99895b17575c9ce1d553720bd1752cd",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contracts-root", type=Path,
                        default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    contracts = args.contracts_root.resolve()
    repo = contracts.parents[1]
    groups = []

    def check(name, condition):
        if not bool(condition):
            raise AssertionError(name)
        groups.append(name)

    actual_hashes = {}
    for relative, digest in FROZEN.items():
        path = repo / relative
        if not path.is_file():
            raise FileNotFoundError(path)
        actual_hashes[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
        check(f"frozen source {relative}", actual_hashes[relative] == digest)
    src = repo / "verification"
    sys.path.insert(0, str(src))
    spec = importlib.util.spec_from_file_location("round16_v983", src / "v983_simple_current_generator.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load the literal frozen charge source")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    U = sp.Matrix([[1, 1, -1, -1], [1, -1, 1, -1], [1, -1, -1, 1]]) / 2
    s = sp.Matrix(module.OMEGA_S).col_join(U * sp.Matrix(module.OMEGA_F))
    check("literal lambda maps to the retained eight-channel spinor", s == sp.ones(8, 1) / 2)

    predecessor = contracts / "matter-geometry-round15/eight_channel_bridge_check.py"
    command = [sys.executable, "-B", str(predecessor), "--repo", str(repo)]
    env = dict(os.environ, PYTHONOPTIMIZE="0", PYTHONDONTWRITEBYTECODE="1")
    run = subprocess.run(command, text=True, capture_output=True, timeout=60, env=env)
    if run.returncode:
        raise RuntimeError(f"Frozen predecessor failed: {run.stdout}\n{run.stderr}")
    prior = json.loads(run.stdout)
    check("unchanged complete source predecessor passes separately", prior.get("status") == "PASS"
          and prior.get("exact_check_groups") == 29
          and prior.get("floating_source_matrix_groups") == 5
          and len(prior.get("checks", [])) == 34
          and all(row.get("status") == "PASS" for row in prior["checks"]))

    eye = sp.eye(8)
    old = sp.Matrix.hstack(2 * eye[:, 0],
                          *[eye[:, 0] + eye[:, k] for k in range(1, 7)], s)
    jrow = sp.Matrix([[-2] * 5 + [4] * 3])
    a = tuple(int((jrow * old[:, k])[0]) for k in range(7))
    check("integer splitting functional and actual seven charges", a == (-4, -4, -4, -4, -4, 2, 2)
          and (jrow * s)[0] == 1)
    K = sp.Matrix.hstack(*[old[:, k] - a[k] * s for k in range(7)])
    new = K.row_join(s)
    change = old.inv() * new
    check("unimodular whole-lattice change of basis", old.det() == new.det() == change.det() == 1
          and all(v.is_integer is True for v in change))
    check("kernel basis and primitive neutral winding", jrow * K == sp.zeros(1, 7)
          and K.row_join(4 * s).det() == 4)
    check("new neutral basis lies in the actual D5 plus D3 lattice", all(
        all(x.is_integer is True for x in K[:, k])
        and sum(K[:5, k]) % 2 == 0 and sum(K[5:, k]) % 2 == 0 for k in range(7)))
    check("winding is primitive neutral but half-winding is not neutral",
          all(v.is_integer for v in 4 * s) and sum((4 * s)[:5]) % 2 == 0
          and sum((2 * s)[:5]) % 2 == 1)

    zero = (0,) * 7
    units = [tuple(int(i == k) for i in range(7)) for k in range(7)]
    us = [zero] + units + [tuple(-z for z in u) for u in units]
    us += [(2, -3, 1, 0, -1, 4, -2), (-1, 2, 0, 3, -4, 1, 2)]

    def old_coords(u, j):
        return tuple(u) + (j - sum(ai * ui for ai, ui in zip(a, u)),)

    def charge(u, j):
        return new * sp.Matrix(tuple(u) + (j,))

    inverse = new.inv()
    check("all-sign exact inverse and Euclidean remainder fixtures", all(
        inverse * charge(u, j) == sp.Matrix(tuple(u) + (j,))
        and 4 * divmod(j, 4)[0] + divmod(j, 4)[1] == j
        and 0 <= divmod(j, 4)[1] < 4 for u in us for j in range(-9, 10)))
    check("cover grade equals frozen internal grade on all fixtures", all(
        int(2 * sum(charge(u, j)[:5])) % 4 == j % 4 for u in us for j in range(-9, 10)))
    G = [[int(v) for v in (old.T * old).row(i)] for i in range(8)]

    def eps_exponent(n, m):
        return (sum(n[i] * m[i] * (G[i][i] // 2) for i in range(8))
                + sum(n[i] * m[h] * G[i][h] for i in range(8) for h in range(i))) % 2

    def d_exp(u, j):
        return (j * (j - 1) // 2 + j * sum(u)) % 2

    def bk(v, u):
        return (sum(v[i] * u[i] for i in range(1, 7))
                + sum(v[i] * u[h] for i in range(1, 7) for h in range(1, i))) % 2

    s_coeff = (0,) * 7 + (1,)
    check("frozen charged cocycle equals the derived parity", all(
        eps_exponent(s_coeff, old_coords(u, j)) == (j + sum(u)) % 2
        for u in us for j in range(-9, 10)))
    check("phase recursion works across zero and negative winding", all(
        (d_exp(u, j + 1) - d_exp(u, j)) % 2 == (j + sum(u)) % 2
        for u in us for j in range(-12, 13)))
    check("phase is four-periodic but the charge shift is not", all(
        d_exp(u, j + 4) == d_exp(u, j) and old_coords(u, j + 4) != old_coords(u, j)
        for u in us for j in range(-12, 13)))
    check("missing cocycle phase negative control fires", any(
        eps_exponent(s_coeff, old_coords(u, j)) != 0 for u in us for j in range(4)))
    check("full neutral cocycle and integer mixed term are retained", all(
        eps_exponent(old_coords(v, 0), old_coords(u, j)) == bk(v, u)
        for v in us for u in us for j in (-3, 0, 4)))
    check("neutral-to-spinor direct product phase is exactly trivial", all(
        eps_exponent(old_coords(v, 0), old_coords(zero, h)) == 0 for v in us for h in range(-6, 7)))
    full_intertwining = True
    for v, u, h, j in itertools.product(us, us, (-5, -2, -1, 0, 1, 2, 4), (-5, 0, 3)):
        uv = tuple(x + y for x, y in zip(u, v))
        direct = (d_exp(u, j) + eps_exponent(old_coords(v, h), old_coords(u, j))
                  + d_exp(uv, j + h)) % 2
        derived = (h * (h - 1) // 2 + bk(v, u) + (j + h) * sum(v)) % 2
        full_intertwining &= direct == derived
    check("every general charged-neutral operator has the derived conjugated phase", full_intertwining)
    check("neutral shifts cannot all be made commuting with the charged shift", all(
        int((K[:, i].T * s)[0]) % 2 == 1 for i in range(7)))

    def carry(m, r):
        return m + (r == 3), (r + 1) % 4

    def carry_inverse(m, r):
        return m - (r == 0), (r - 1) % 4

    check("bilateral carry has the exact inverse", all(
        carry_inverse(*carry(m, r)) == (m, r) and carry(*carry_inverse(m, r)) == (m, r)
        for m in range(-8, 9) for r in range(4)))
    fourth = True
    for m, r in itertools.product(range(-8, 9), range(4)):
        state = (m, r)
        for _ in range(4):
            state = carry(*state)
        fourth &= state == (m + 1, r)
    check("fourth power is exactly one winding shift", fourth)
    check("finite-periodic winding negative control has wrong charge monodromy", all(
        charge(zero, 4 * n) != charge(zero, 0) for n in (1, 2, 3, 8)))

    # Gaussian-unit phases are stored as integers mod four, never approximate floats.
    def gamma(bits, orbital):
        return bits ^ (1 << orbital), 2 * ((bits & ((1 << orbital) - 1)).bit_count() % 2)

    def F(bits):
        middle, e1 = gamma(bits, 5)
        target, e2 = gamma(middle, 0)
        return target, (1 + e1 + e2) % 4

    def wa(bits):
        return 2 * (((bits >> 1) & 1) + ((bits >> 6) & 1)) % 4

    def physical(r, bits):
        return bits.bit_count() % 2 == 0 and (bits & 31).bit_count() % 2 == (r // 2) % 2

    def lift(m, r, bits):
        e = wa(bits)
        target = bits
        if r % 2:
            target, ef = F(bits)
            e = (e + ef) % 4
        mm, rr = carry(m, r)
        return mm, rr, target, e

    def vr(r, bits):
        e = wa(bits) if r % 2 else 0
        target = bits
        if r // 2:
            target, ef = F(bits)
            e = (e + ef) % 4
        return target, e

    code0 = [b for b in range(256) if physical(0, b)]
    check("all finite code fibers are explicit equal nonzero spaces", len(code0) == 64
          and all(sum(physical(r, b) for b in range(256)) == 64 for r in range(4)))
    check("explicit fiber maps and their inverse preserve code", all(
        physical(r, vr(r, b)[0]) and vr(r, vr(r, b)[0])[0] == b
        and (vr(r, b)[1] + vr(r, vr(r, b)[0])[1]) % 4 == 0
        for r in range(4) for b in code0))
    code_intertwining = True
    for m, r, b in itertools.product(range(-3, 4), range(4), code0):
        br, er = vr(r, b)
        mm, rr, target, e = lift(m, r, br)
        next_b, next_e = vr(rr, b)
        code_intertwining &= (target, (er + e) % 4) == (next_b, next_e)
        code_intertwining &= (mm, rr) == carry(m, r)
    check("fiber trivialization intertwines every winding and closing sector step", code_intertwining)
    micro_fourth = True
    for m, r, b in itertools.product((-2, 0, 2), range(4), range(256)):
        mm, rr, bb, phase = m, r, b, 0
        for _ in range(4):
            mm, rr, bb, e = lift(mm, rr, bb)
            phase = (phase + e) % 4
        micro_fourth &= (mm, rr, bb, phase) == (m + 1, r, b, 0)
    check("full CAR lift fourth power retains the neutral winding exactly", micro_fourth)
    check("code preservation and dual grade are retained after lift", all(
        physical(r, b) == physical(lift(m, r, b)[1], lift(m, r, b)[2])
        and (lift(m, r, b)[1] - r) % 4 == 1
        for m, r, b in itertools.product((-1, 0, 1), range(4), range(256))))

    # Omega = (Phi tensor I) (I tensor J*) on actual code basis states.
    def omega(u, m, r, b):
        base_b, e = vr(r, b)
        return old_coords(u, 4 * m + r), base_b, (e + 2 * d_exp(u, 4 * m + r)) % 4

    combined = True
    for u, m, r, b in itertools.product(us[:4], (-2, 0, 1), range(4), range(256)):
        if not physical(r, b):
            continue
        n, base_b, phase = omega(u, m, r, b)
        mm, rr, bb, e = lift(m, r, b)
        n2, base_b2, phase2 = omega(u, mm, rr, bb)
        expected_n = tuple(n[i] + s_coeff[i] for i in range(8))
        combined &= (n2, base_b2, (e + phase2) % 4) == (
            expected_n, base_b, (phase + 2 * eps_exponent(s_coeff, n)) % 4)
    check("displayed full unitary identifies finite-code lift with the actual cocycle shift", combined)

    u_symbols = sp.symbols("u1:8", real=True)
    j_symbol = sp.symbols("j", real=True)
    x = K * sp.Matrix(u_symbols) + j_symbol * s
    E = sp.expand((x.T * x)[0] / 2)
    expression = j_symbol**2 + j_symbol * (sp.Matrix(u_symbols).T * K.T * s)[0]
    expression += (sp.Matrix(u_symbols).T * K.T * K * sp.Matrix(u_symbols))[0] / 2
    check("full charge energy retains the source cross terms", sp.expand(E - expression) == 0)
    new_gram = new.T * new
    check("energy is positive definite in all eight cover coordinates", all(
        new_gram[:k, :k].det() > 0 for k in range(1, 9)) and new_gram.det() == 1)
    energy_difference = sp.expand(E.subs(j_symbol, j_symbol + 1) - E)
    check("charged energy increment is the exact unbounded affine charge", sp.expand(
        energy_difference - (x.T * s)[0] - 1) == 0
        and sp.diff(energy_difference, j_symbol) == 2)
    check("charge-translation graph-domain bound has an exact positive square", sp.expand(
        2 * E + 2 - E.subs(j_symbol, j_symbol + 1) - ((x - s).T * (x - s))[0] / 2) == 0)
    check("neutral four-step energy is not a finite-register zero cost",
          E.subs(dict(zip(u_symbols, zero))).subs(j_symbol, 4) == 16
          and E.subs(dict(zip(u_symbols, zero))).subs(j_symbol, 0) == 0)
    check("separate winding-square penalty negative control misses source energy", sp.expand(
        E - j_symbol**2 - (sp.Matrix(u_symbols).T * K.T * K * sp.Matrix(u_symbols))[0] / 2) != 0)

    print(json.dumps({
        "status": "PASS", "exact_check_groups": len(groups), "checks": groups,
        "source_sha256": actual_hashes,
        "predecessor": {"status": prior["status"], "command": command,
                        "exact_check_groups": prior["exact_check_groups"],
                        "floating_source_matrix_groups": prior["floating_source_matrix_groups"]},
        "neutral_lattice_split": "L0 = K rank7 direct_sum Z(4s)",
        "charged_operator_equivalence": "Omega T_lift Omega* = T_s tensor I_code0",
        "finite_code_multiplicity_fixture": len(code0),
        "added_unbounded_integer_coordinates": 8,
        "scope": "Full neutral/cocycle representation and declared energetic code lift; not microscopic TFPT selection, scaling, 4D chirality, TOE or RH.",
    }, indent=2))


if __name__ == "__main__":
    main()
