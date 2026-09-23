"""Independent exact audit of the full-60 stopped marked-jump instrument."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent
SOURCE = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py")
spec = importlib.util.spec_from_file_location("contract_source_channel", SOURCE)
src = importlib.util.module_from_spec(spec)
spec.loader.exec_module(src)
checks = []


def require(ok, name):
    if not bool(ok):
        raise RuntimeError(name)
    checks.append(name)


def main():
    rays = src.source_rays()
    bell, raw, _ = src.reflection_actions(rays)
    six, _ = src.outer_mark_action(raw)
    mapping = src.find_bell_partition_intertwiner(bell, six)
    s60 = src.superoperator_integer(bell)
    require(not np.any(s60.imag), "full60 superoperator real in Bell matrix units")
    s60 = np.rint(s60.real).astype(np.int64)

    spectra = []
    count_stats = []
    for mark in range(6):
        out = src.marked_data(mark, bell, six, mapping)
        j20 = out[4]
        require(not np.any(j20.imag), f"mark {mark}: J20 real")
        j20 = np.rint(j20.real).astype(np.int64)
        require(not np.any(s60@j20-j20@s60), f"mark {mark}: [S60,J20]=0")

        # J20 is the accepted-jump submap.  S60-J20 contains selected stays
        # and every event from the complementary 40-ray source.
        reject = s60-j20
        require(not np.any(reject.imag if np.iscomplexobj(reject) else 0), f"mark {mark}: rejection real")
        effect = np.zeros((10, 10), dtype=np.int64)
        for a in range(10):
            col = a+10*a
            for b in range(10):
                effect[b, b] += j20[b+10*b, col] if a == b else 0
        # Direct Kraus audit from source_channel gives J20^dagger(I)=12I.
        direct_effect = np.zeros((10, 10), dtype=np.complex128)
        idx = out[0]
        for k in idx:
            U = bell[k]
            perm = src.bell_permutation(U)
            dj = np.diag([int(perm[a] != a) for a in range(10)])
            K = U@dj
            direct_effect += K.conj().T@K
        require(np.array_equal(direct_effect, 12*np.eye(10)), f"mark {mark}: accept probability 1/5")

        den = sp.Matrix(60*np.eye(100, dtype=np.int64)-s60+j20)
        require(den.det() != 0, f"mark {mark}: stopped resolvent invertible")
        phi = sp.Matrix(j20)*den.inv()
        roots = [sp.Integer(1), sp.Rational(1, 11), -sp.Rational(1, 4),
                 sp.Integer(0), sp.Rational(1, 13), -sp.Rational(1, 13)]
        poly = sp.eye(100)
        for root in roots:
            poly = poly*(phi-root*sp.eye(100))
        require(poly == sp.zeros(100), f"mark {mark}: full60 stopped spectral polynomial")
        moments = [sp.trace(phi**k) for k in range(6)]
        vand = sp.Matrix([[r**k for r in roots] for k in range(6)])
        mult = list(vand.inv()*sp.Matrix(moments))
        require(mult == [1, 5, 4, 60, 15, 15], f"mark {mark}: full60 stopped multiplicities")

        diag = [a+10*a for a in range(10)]
        pop_s60 = sp.Matrix(s60[np.ix_(diag, diag)])
        pop_j20 = sp.Matrix(j20[np.ix_(diag, diag)])
        A = sp.Matrix(out[2])
        one = sp.ones(10)
        require(pop_s60 == 4*(5*sp.eye(10)+one), f"mark {mark}: C60 populations (5I+J)/15")
        require(pop_j20 == 4*A, f"mark {mark}: accepted populations A/15")
        phi_pop = pop_j20*(60*sp.eye(10)-pop_s60+pop_j20).inv()
        require(phi_pop == A*(10*sp.eye(10)-one+A).inv(), f"mark {mark}: full60 stopped population formula")
        require(phi.extract(diag, diag) == phi_pop, f"mark {mark}: population restriction agrees")

        z = sp.Symbol("z")
        pgf = (z/(5-4*z))**6
        mean = sp.diff(pgf, z).subs(z, 1)
        variance = sp.diff(pgf, z, 2).subs(z, 1)+mean-mean**2
        require(mean == 30 and variance == 120 and pgf.subs(z, 1) == 1,
                f"mark {mark}: six accepted jumps count mean30 variance120")
        spectra.append({"mark": mark, "multiplicities": [str(v) for v in mult]})
        count_stats.append({"mark": mark, "pgf": str(pgf), "mean": str(mean), "variance": str(variance)})

    result = {
        "verdict": "PASS_FULL60_CONDITIONAL_INSTRUMENT",
        "scope": "fixed outer mark, iid uniform 60-ray events, accept only marked20 jump branches; no claim for all TFPT clocks",
        "commutator": "[S60,J20]=0 for all six marks",
        "stopped_channel": "Phi60=J20(60I-S60+J20)^-1",
        "spectrum": {"1": 1, "1/11": 5, "-1/4": 4, "0": 60, "1/13": 15, "-1/13": 15},
        "population_channel": "C60_pop=(5I+ones)/15; Jaccept_pop=A/15; Phi_pop=A(10I-ones+A)^-1",
        "six_accept_count": {"pgf": "(z/(5-4z))^6", "mean": 30, "variance": 120},
        "implication": "The 20-source clock spectrum requires a preselected marked20 source. Post-selecting marked jumps from a uniform full60 source gives the different spectrum above.",
        "checks_passed": len(checks),
        "per_mark": spectra,
    }
    (HERE/"review_full60.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps({k: result[k] for k in ("verdict", "spectrum", "six_accept_count", "checks_passed")}, indent=2))


if __name__ == "__main__":
    main()
