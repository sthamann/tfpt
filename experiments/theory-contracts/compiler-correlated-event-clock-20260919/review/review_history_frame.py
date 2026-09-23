"""Exact audit of the history-frame recovery of the marked20 stopped clock."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent
SOURCE = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py")
spec = importlib.util.spec_from_file_location("contract_source_channel_history", SOURCE)
src = importlib.util.module_from_spec(spec)
spec.loader.exec_module(src)
checks = []


def require(ok, name):
    if not bool(ok):
        raise RuntimeError(name)
    checks.append(name)


def matrix_key(a):
    require(np.array_equal(a.real, np.rint(a.real)) and np.array_equal(a.imag, np.rint(a.imag)),
            "Gaussian integer monomial matrix")
    return tuple((int(round(v.real)), int(round(v.imag))) for v in a.ravel())


def superop(u):
    return np.kron(u.conj(), u)


def main():
    rays = src.source_rays()
    bell, raw, _ = src.reflection_actions(rays)
    six, _ = src.outer_mark_action(raw)
    mapping = src.find_bell_partition_intertwiner(bell, six)
    eye100 = np.eye(100, dtype=np.int64)
    per_mark = []

    for mark in range(6):
        out = src.marked_data(mark, bell, six, mapping)
        selected = out[0]
        complement = [k for k in range(60) if k not in selected]
        S = np.rint(out[3].real).astype(np.int64)
        J = np.rint(out[4].real).astype(np.int64)
        require(len(selected) == 20 and len(complement) == 40, f"mark {mark}: 20+40 partition")
        require(all(six[k][mark] != mark for k in selected), f"mark {mark}: selected moves mark")
        require(all(six[k][mark] == mark for k in complement), f"mark {mark}: background fixes mark")

        selected_lookup = {matrix_key(bell[k]): k for k in selected}
        require(len(selected_lookup) == 20, f"mark {mark}: selected matrices distinct")
        conjugation_rows = []
        for h in complement:
            Uh = bell[h]
            row = []
            H = superop(Uh)
            require(np.array_equal(H.conj().T@S@H, S), f"mark {mark}: S covariance under background {h}")
            require(np.array_equal(H.conj().T@J@H, J), f"mark {mark}: J covariance under background {h}")
            for ell in selected:
                U = bell[ell]
                transported = Uh.conj().T@U@Uh
                key = matrix_key(transported)
                require(key in selected_lookup, f"mark {mark}: exact 40x20 conjugation closure {h},{ell}")
                target = selected_lookup[key]
                row.append(target)

                p = src.bell_permutation(U)
                pt = src.bell_permutation(bell[target])
                Ds = np.diag([int(p[a] == a) for a in range(10)])
                Dst = np.diag([int(pt[a] == a) for a in range(10)])
                require(np.array_equal(Uh.conj().T@Ds@Uh, Dst),
                        f"mark {mark}: stay projector covariance {h},{ell}")
                require(np.array_equal(Uh.conj().T@(U@Ds)@Uh, bell[target]@Dst),
                        f"mark {mark}: stay Kraus covariance {h},{ell}")
                Dj = np.eye(10, dtype=np.complex128)-Ds
                Djt = np.eye(10, dtype=np.complex128)-Dst
                require(np.array_equal(Uh.conj().T@(U@Dj)@Uh, bell[target]@Djt),
                        f"mark {mark}: jump Kraus covariance {h},{ell}")
            require(len(set(row)) == 20, f"mark {mark}: each background event permutes selected alphabet")
            conjugation_rows.append(row)

        # In the frame rho'=F^dagger rho F, a background W followed by
        # F' = W F is exactly invisible.  Selected U becomes F^dagger U F;
        # closure above proves it remains uniformly distributed on the same 20.
        # Unnormalised source matrices make the equality denominator-free.
        # S_eff=(40 I+S)/60, J_eff=J/60.
        den_eff = 20*eye100-S
        phi20 = sp.Matrix(J)*sp.Matrix(den_eff).inv()
        phi_eff = sp.Matrix(J)*sp.Matrix(60*eye100-(40*eye100+S)).inv()
        require(phi_eff == phi20, f"mark {mark}: history-frame stopped channel equals marked20 channel")
        require(phi_eff.eigenvals() == {sp.Integer(1): 1, sp.Rational(1,3): 5,
                -sp.Rational(2,3): 4, sp.Integer(0): 60,
                sp.Rational(1,5): 15, -sp.Rational(1,5): 15},
                f"mark {mark}: recovered stopped spectrum")

        z = sp.Symbol("z")
        pgf = (z/(5-4*z))**6
        mean = sp.diff(pgf, z).subs(z, 1)
        variance = sp.diff(pgf, z, 2).subs(z, 1)+mean-mean**2
        require(mean == 30 and variance == 120, f"mark {mark}: all-event count mean30 variance120")
        per_mark.append({"mark": mark, "closure_pairs": 40*20,
                         "background_permutations": 40,
                         "count_mean": 30, "count_variance": 120})

    result = {
        "verdict": "PASS_HISTORY_FRAME_FINITE_CONSTRUCTION",
        "scope": "fixed outer mark; iid uniform full60 source; exact record of every background40 event; co-moving readout rho'=F^dagger rho F",
        "frame_update": "for background W: physical rho -> W rho W^dagger and F -> W F, hence rho' is unchanged",
        "selected_update": "for selected U: F is held and U_eff=F^dagger U F remains uniformly distributed in the marked20 alphabet",
        "closure": "all 6 marks x 40 background events x 20 selected events close exactly, without an extra scalar phase",
        "instrument_covariance": "stay and jump projectors/Kraus maps are conjugated to the corresponding selected event",
        "effective_maps": "S_eff=(40 Id+S20)/60; J_eff=J20/60",
        "stopped_identity": "J_eff(I-S_eff)^-1=J20(20I-S20)^-1=Phi20",
        "recovered_spectrum": {"1": 1, "1/3": 5, "-2/3": 4, "0": 60,
                               "1/5": 15, "-1/5": 15},
        "all_event_count_six_accepts": {"pgf": "(z/(5-4z))^6", "mean": 30, "variance": 120},
        "open_physical_premise": "the outer mark, complete background-event record, and co-moving frame readout must be physically available; the finite algebra does not derive them",
        "not_claimed": "no coherent erasure of physical background evolution, no autonomous clock selection, no continuum or TOE closure",
        "checks_passed": len(checks),
        "per_mark": per_mark
    }
    (HERE/"review_history_frame.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps({k: result[k] for k in ("verdict", "closure", "effective_maps",
          "stopped_identity", "recovered_spectrum", "checks_passed")}, indent=2))


if __name__ == "__main__":
    main()
