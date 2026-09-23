"""Exact clock identities and source diagnostics; infinite proofs in PROOF.txt."""
import argparse
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import sys

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CLOCK = "experiments/theory-contracts/compiler-integral-triality-20260918/certificate.json"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def verify_pins():
    manifest = json.loads((HERE / "source_manifest.json").read_text())
    for name, expected in manifest["sha256"].items():
        require(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected,
                "source pin mismatch: " + name)


def clock_certificate():
    data = json.loads((ROOT / CLOCK).read_text())["clock_matrices"]
    c, j = (sp.Matrix(data[name]["vector"]) for name in ("C", "J"))
    eye = sp.eye(8)
    require(c.T*c == eye and j.T*j == eye, "orthogonal clocks")
    require(c**30 == eye and j**2 == -eye, "clock orders")
    x = sp.Symbol("x")
    require(c.charpoly(x).as_expr() == sp.cyclotomic_poly(30, x), "Phi30")
    roots = set()
    for a in range(8):
        for b in range(a+1,8):
            for sa,sb in product((-1,1),repeat=2):
                root = [sp.S.Zero]*8
                root[a],root[b] = sp.Integer(sa),sp.Integer(sb)
                roots.add(tuple(root))
    for signs in product((-1,1),repeat=8):
        if sum(q<0 for q in signs)%2 == 0:
            roots.add(tuple(sp.Rational(q,2) for q in signs))
    require(len(roots)==240, "E8 root inventory")
    require({tuple(c*sp.Matrix(r)) for r in roots}==roots, "C root lattice action")
    v = eye + (c+c.T)/4
    require(v == v.T and c.T*v*c == v, "C covariance")
    require(j.T*v*j != v, "counterfamily must violate additional J symmetry")
    require(v != sp.trace(v)*eye/8, "unequal velocities")
    minors = [v[:k,:k].det() for k in range(1,9)]
    require(all(q > 0 for q in minors), "strict positivity by Sylvester")
    basis = []
    for a in range(8):
        for b in range(a,8):
            m = sp.zeros(8)
            m[a,b] = m[b,a] = 1
            basis.append(m)
    def constraints(matrices):
        return sp.Matrix.hstack(*[
            sp.Matrix.vstack(*[(g.T*b*g-b).reshape(64,1) for g in matrices])
            for b in basis])
    cdim = 36-constraints([c]).to_DM().rank()
    both = 36-constraints([c,j]).to_DM().rank()
    require(cdim == 4 and both == 1, "symmetric invariant dimensions")
    return {
        "status": "EXACT_RATIONAL_ALGEBRA",
        "C_symmetric_invariants": cdim, "CJ_symmetric_invariants": both,
        "V": [[str(q) for q in row] for row in v.tolist()],
        "V_positive_leading_minors": [str(q) for q in minors],
        "V_characteristic_polynomial": str(sp.factor(v.charpoly(x).as_expr())),
        "distinct_velocities_approx": [float(1+sp.cos(2*sp.pi*m/30)/2)
                                        for m in (1,7,11,13)],
        "C_covariant": True, "J_covariant": False,
        "C_preserves_all_240_E8_roots": True,
        "quartic_coupling_dimension_point_defect": -1,
        "quartic_coupling_dimension_extended_edge": 0,
        "same_stress_c1_to_E8_c8": "IMPOSSIBLE",
        "coset_Lminus2_vacuum_norm_squared_if_compatible": "-7/2",
    }


def exact_strip_identities():
    rho, s = sp.symbols("rho s", real=True)
    for w in (2,3,8):
        shift = sp.zeros(w)
        for a in range(w-1):
            shift[a+1,a] = 1
        b = rho*sp.eye(w)-shift
        t = (1+rho**2)*sp.eye(w)-rho*(shift+shift.T)
        end = sp.zeros(w)
        end[w-1,w-1] = 1
        require(b.T*b == t-end, "rank-one identity")
        h = (-s*sp.eye(w)).row_join(b.T).col_join(b.row_join(s*sp.eye(w)))
        require(sp.simplify(h*h-sp.diag(s*s*sp.eye(w)+b.T*b,
                                      s*s*sp.eye(w)+b*b.T)) == sp.zeros(2*w),
                "squared block identity")
    return {"status": "EXACT_IDENTITIES_AT_W_2_3_8; ALL_W_PROOF_IN_TEXT",
            "bulk_unscaled_gap": 1, "scaled_bulk_gap": "N/(2*pi)",
            "finite_energy_label_bound": "abs(j-1/4) <= pi*E/2",
            "limiting_channels": {"top_complex_chiral": 1, "bottom_complex_chiral": 1}}


def source_module():
    sys.path.insert(0, str(ROOT / "verification"))
    spec = importlib.util.spec_from_file_location("rg_bridge_original_v1033",
                        ROOT / "verification/v1033_charged_disorder.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def cutoff_energies(modes, cutoff):
    energies = [0.0]
    for value in modes:
        energies += [x+value for x in energies if x+value <= cutoff]
    return np.sort(energies)


def source_diagnostics():
    source = source_module()
    w = 8
    plus, minus = np.array([1,1])/np.sqrt(2), np.array([1,-1])/np.sqrt(2)
    u = np.column_stack([np.kron(np.eye(w)[:,i],v)
                         for v in (plus,minus) for i in range(w)])
    shift = np.diag(np.ones(w-1),-1)
    residual = 0.0
    smallest_bulk = float("inf")
    rows = []
    for n in (32,64,128):
        modes = []
        for label in range(-n//2+1,n//2+1):
            p = 2*np.pi*(label-.25)/n
            h = source.strip_at_momentum(p,w)
            b = (1-np.cos(p))*np.eye(w)-shift
            block = np.block([[-np.sin(p)*np.eye(w),b.T],[b,np.sin(p)*np.eye(w)]])
            residual = max(residual,float(np.linalg.norm(u.T@h@u-block)))
            e = np.sort(np.abs(np.linalg.eigvalsh(h)))
            smallest_bulk = min(smallest_bulk,float(e[2]))
            require(e[2] >= 1-1e-12,"bulk gap diagnostic")
            if abs(p) >= np.pi/2:
                require(e[0] >= 1-1e-12,"outside window diagnostic")
            scaled = n*e/(2*np.pi)
            modes.extend(scaled[scaled <= 4.1])
        for cap in (1.1,2.1,3.1,4.1):
            limit_modes = [abs(j-.25) for j in range(-6,7) for _ in range(2)
                           if abs(j-.25) <= cap]
            micro = cutoff_energies(modes,cap)
            limit = cutoff_energies(limit_modes,cap)
            if n == 128:
                require(len(micro) == len(limit),"large-N full cutoff rank diagnostic")
            rows.append({"N":n,"E":cap,"full_cutoff_rank":len(micro),
                         "limit_cutoff_rank":len(limit),
                         "ranks_agree":len(micro) == len(limit),
                         "max_sorted_energy_error":float(np.max(np.abs(micro-limit)))
                             if len(micro) == len(limit) else None})
    require(residual < 1e-12,"original source block mismatch")
    return {"status":"NUMERICAL_REGRESSION_ONLY_NOT_INFINITE_PROOF",
            "max_original_strip_block_residual":residual,
            "smallest_bulk_abs_eigenvalue":smallest_bulk,
            "full_many_body_cutoffs":rows}


def run():
    verify_pins()
    return {"contract":"source-rg-clock-bridge-20260920", "verdict":"PARTIAL",
            "mathematical_verdict":"EXACT_FIXED_SOURCE_EXHAUSTION_AND_KINETIC_COUNTERFAMILY",
            "clock":clock_certificate(), "source":exact_strip_identities(),
            "diagnostics":source_diagnostics(),
            "complete_TFPT_solution":False,"physical_gates_closed":[],
            "local_scaling_algebra_exhaustion_proved":False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    result = run()
    content = json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(content)
    else:
        print(content,end="")
