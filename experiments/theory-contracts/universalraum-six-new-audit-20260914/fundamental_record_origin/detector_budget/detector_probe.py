"""Complete raw protocol with independent imperfect occupancy detectors.

The instrument is modeled on the actual matter Kraus operators of A,N,A.
Endpoint mixtures are evaluated exactly, then interpolated as multilinear
Bernstein polynomials; no conditional branch is ever renormalized.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import sympy as s

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1]
EP_PATH = BASE/"exact_one_record_protocol.py"
spec = importlib.util.spec_from_file_location("source_protocol", EP_PATH)
ep = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ep)
CHECKS = []
COLORS = list(combinations(range(4), 2))


def need(ok, message):
    if not bool(ok):
        raise RuntimeError(message)
    CHECKS.append(message)


def project(vector, edge, sign):
    out = {}
    for (word, mask), value in vector.items():
        other = list(word)
        i, j = edge
        other[i], other[j] = other[j], other[i]
        ep.add(out, (word, mask), value/2)
        ep.add(out, (tuple(other), mask), sign*value/2)
    return out


def flavor(vector, edge, pair):
    minus = project(vector, edge, -1)
    return {key:value for key,value in minus.items()
            if tuple(sorted((key[0][edge[0]], key[0][edge[1]]))) == pair}


def occupied(vector, edge, ideal):
    return [project(vector, edge, -1)] if ideal else [flavor(vector, edge, pair) for pair in COLORS]


def echo(vector, ideal):
    return [project(vector, (0,1), 1), *occupied(vector, (0,1), ideal)]


def good_weight(vector):
    # Omega numerator has norm sqrt24; use squared integer-sign amplitude.
    amplitude = sum((F(ep.parity(w))*vector.get((w,0), F(0)) for w in permutations(range(4))), F(0))
    return amplitude*amplitude/24


def end(vector, ideal):
    out = F(0)
    occupied_weight = F(0)
    for branch in occupied(vector, (0,3), ideal):
        occupied_weight += ep.norm2(branch)
        decoded = ep.clifford(branch, inverse=True)
        out += decoded.get(((0,0,0,0),0), F(0))**2
        need(ep.norm2(decoded) == ep.norm2(branch), "inverse xi preserves every raw end branch norm")
    n0 = ep.norm2(project(vector, (0,3), 1))
    need(n0+occupied_weight == ep.norm2(vector), "complete end occupancy instrument preserves raw mass")
    return out, occupied_weight


def evaluate(a, b, c, recorded):
    xi = ep.clifford({((0,0,0,0),0):F(1)})
    prep = occupied(xi, (0,3), a)
    pprep = sum(map(ep.norm2, prep), F(0))
    need(pprep == F(3,8), "prep herald is exactly three eighths for either detector endpoint")
    need(ep.norm2(project(xi,(0,3),1))+pprep == 1, "prep outcomes sum to one")
    prep_good = sum(map(good_weight, prep), F(0))
    need(prep_good/pprep == (F(1) if a else F(1,6)), "actual preparation fidelity endpoint")
    branches = []
    echo_minus = F(0)
    for v in prep:
        ticked = ep.tick(v)
        if recorded:
            local = [(0,project(ticked,(0,1),1)), *[(1,q) for q in occupied(ticked,(0,1),b)]]
            need(sum((ep.norm2(q) for flag,q in local), F(0)) == ep.norm2(ticked), "complete echo instrument preserves branch mass")
            echo_minus += sum((ep.norm2(q) for q in occupied(ticked,(0,1),b)), F(0))
        else:
            local = [(-1,ticked)]
        branches.extend((flag,ep.tick(q,inverse=True)) for flag,q in local)
    need(sum((ep.norm2(q) for flag,q in branches), F(0)) == pprep, "complete echo retains full raw prep mass")
    raw, end_occ = F(0), F(0)
    split = {"raw_success_echo0":F(0),"raw_success_echo1":F(0),
             "raw_end_occupied_echo0":F(0),"raw_end_occupied_echo1":F(0)}
    for flag,branch in branches:
        local_raw, local_occ = end(branch, c)
        raw += local_raw
        end_occ += local_occ
        if flag in [0,1]:
            split["raw_success_echo"+str(flag)] += local_raw
            split["raw_end_occupied_echo"+str(flag)] += local_occ
    need(F(5,8)+(pprep-raw)+raw == 1, "prep reject and both complete end flags sum to one")
    return {"raw_success": raw, "raw_end_occupied": end_occ,
            "raw_echo_occupied": echo_minus, "raw_prep_good": prep_good,
            "raw_after_echo_good": sum((good_weight(q) for flag,q in branches),F(0)), **split}


def multilinear(corners, variables, key):
    result = 0
    for bits, values in corners.items():
        coeff = s.Rational(values[key].numerator, values[key].denominator)
        for bit, variable in zip(bits,variables):
            coeff *= variable if bit else 1-variable
        result += coeff
    return s.factor(result)


def density_control(a, b, c, recorded):
    """Separate rational density-matrix implementation of the whole protocol."""
    xi = ep.clifford({((0,0,0,0),0):F(1)})
    xi = {w:v for (w,mask),v in xi.items()}
    rho = {(w,z):v*u for w,v in xi.items() for z,u in xi.items()}

    def swapped(word, edge):
        word = list(word)
        i,j = edge
        word[i],word[j] = word[j],word[i]
        return tuple(word)

    def projection(density, edge, sign):
        out = {}
        for (w,z),v in density.items():
            for ww,ss in [(w,1),(swapped(w,edge),sign)]:
                for zz,tt in [(z,1),(swapped(z,edge),sign)]:
                    ep.add(out,(ww,zz),v*ss*tt/4)
        return out

    def occupied_density(density, edge, eta):
        out = projection(density,edge,-1)
        return {(w,z):v*(1 if sorted((w[edge[0]],w[edge[1]]))==sorted((z[edge[0]],z[edge[1]])) else eta)
                for (w,z),v in out.items()}

    def trace(density):
        return sum((v for (w,z),v in density.items() if w==z),F(0))

    def clock(density, inverse=False):
        colors = [2,0,1,3] if inverse else [1,2,0,3]
        return {((colors[w[0]],*w[1:]),(colors[z[0]],*z[1:])):v for (w,z),v in density.items()}

    rho = occupied_density(rho,(0,3),a)
    need(trace(rho)==F(3,8), "independent density control preserves raw prep weight")
    rho = clock(rho)
    if recorded:
        minus = occupied_density(rho,(0,1),b)
        rho = projection(rho,(0,1),1)
        for key,value in minus.items():
            ep.add(rho,key,value)
    rho = clock(rho,inverse=True)
    need(trace(rho)==F(3,8), "independent density echo is trace preserving")
    rho = occupied_density(rho,(0,3),c)
    return sum((v*xi.get(w,F(0))*xi.get(z,F(0)) for (w,z),v in rho.items()),F(0))


def complete_classical_histogram(a, b, c, recorded):
    """Include all final eight-bit strings, not only the all-zero event."""
    xi = ep.clifford({((0,0,0,0),0):F(1)})
    histogram = {"prep_reject": F(5,8)}
    for v in occupied(xi,(0,3),a):
        ticked = ep.tick(v)
        branches = [(0,project(ticked,(0,1),1)), *[(1,q) for q in occupied(ticked,(0,1),b)]] if recorded else [(-1,ticked)]
        for flag,q in branches:
            q = ep.tick(q,inverse=True)
            ep.add(histogram, str((flag,"end_N0")), ep.norm2(project(q,(0,3),1)))
            for r in occupied(q,(0,3),c):
                for (w,mask),amplitude in ep.clifford(r,inverse=True).items():
                    ep.add(histogram,str((flag,"end_N1",w)),amplitude*amplitude)
    need(sum(histogram.values(),F(0))==1, "complete classical histogram includes rejection and every final bit string")
    return histogram


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=HERE/"verification.json")
    ap.add_argument("--mutant", choices=["ideal_end", "correlated_detectors", "normalize_histories"])
    args = ap.parse_args()
    a,b,c,eta = s.symbols("a b c eta", real=True)
    retained = {(x,z):evaluate(x,0,z,False) for x,z in product([0,1],repeat=2)}
    recorded = {(x,y,z):evaluate(x,y,z,True) for x,y,z in product([0,1],repeat=3)}
    keep = {key:multilinear(retained,[a,c],key) for key in next(iter(retained.values()))}
    fresh = {key:multilinear(recorded,[a,b,c],key) for key in next(iter(recorded.values()))}
    need(s.expand(keep["raw_success"]-3*(5*a*c+1)/128) == 0, "retained raw polynomial independently matches density/effect overlap")
    need(keep["raw_success"].subs({a:1,c:1}) == s.Rational(9,64), "ideal retained source value")
    need(fresh["raw_success"].subs({a:1,b:1,c:1}) == s.Rational(153,2048), "ideal recorded source value")
    need(s.expand(fresh["raw_success"]-3*(19*a*b*c+66*a*c+3*b+14)/4096)==0,
         "independent detector recorded multilinear polynomial")
    need(s.factor(fresh["raw_success"].subs(b,1)/keep["raw_success"]) == s.Rational(17,32),
         "ideal middle detector preserves ideal ratio despite arbitrarily bad prep and end detectors")
    need(s.expand(fresh["raw_end_occupied"]-3*(b+10)/128)==0,
         "middle detector can be calibrated from complete raw end occupation")
    common_keep = s.factor(keep["raw_success"].subs({a:eta,c:eta}))
    common_fresh = s.factor(fresh["raw_success"].subs({a:eta,b:eta,c:eta}))
    common_gap = s.factor(common_keep-common_fresh)
    if args.mutant == "ideal_end":
        need(s.expand(common_keep-keep["raw_success"].subs({a:eta,c:1})) == 0,
             "MUTANT: a detector-corrupted end must not be replaced by an ideal end")
    if args.mutant == "correlated_detectors":
        correlated = eta*s.Rational(retained[(1,1)]["raw_success"])+(1-eta)*s.Rational(retained[(0,0)]["raw_success"])
        need(s.expand(correlated-common_keep) == 0,
             "MUTANT: perfectly correlated detector imperfections are not independent uses")
    if args.mutant == "normalize_histories":
        xi = ep.clifford({((0,0,0,0),0):F(1)})
        normalized_mass = sum(F(1) for q in occupied(xi,(0,3),False) if ep.norm2(q))
        need(normalized_mass == F(3,8), "MUTANT: independently normalizing hidden color histories changes the raw mass")
    eta0_keep, eta0_fresh = common_keep.subs(eta,0),common_fresh.subs(eta,0)
    need(eta0_keep==s.Rational(3,128) and eta0_fresh==s.Rational(21,2048),
         "complete color loss still gives a positive raw echo contrast")
    ratio_difference = s.factor(common_fresh/common_keep-s.Rational(17,32))
    need(s.cancel(ratio_difference/((eta-1)*(19*eta**2+3))-1/(32*(5*eta**2+1))) == 0,
         "common eta ratio equals ideal only at eta one on the physical interval")
    # Independent exact effect construction from the six projected xi rows.
    xi = ep.clifford({((0,0,0,0),0):F(1)})
    colored_rows = occupied(xi,(0,3),False)
    need(all(ep.norm2(v)==F(1,16) for v in colored_rows), "six noisy end rows each have squared norm one sixteenth")
    need(all(sum((x*colored_rows[j].get(k,F(0)) for k,x in colored_rows[i].items()),F(0))==0
             for i,j in combinations(range(6),2)), "six noisy end rows are mutually orthogonal")
    need(sum((good_weight(v) for v in colored_rows),F(0))==F(1,16),
         "fully dephased end accepts ideal Omega with probability one sixteenth")
    for values in [(F(1,2),F(1,3),F(2,5)),(F(0),F(1),F(0)),(F(1),F(0),F(1)),(F(1),F(1),F(1)),(F(0),F(0),F(0))]:
        for recorded_mode, polynomial in [(False,keep["raw_success"]),(True,fresh["raw_success"])]:
            direct = density_control(*values,recorded_mode)
            need(direct == polynomial.subs(dict(zip([a,b,c],values))),
                 "independent full density calculation matches raw polynomial at "+str(values)+" recorded="+str(recorded_mode))
    for middle in [0,1]:
        for recorded_mode in [False,True]:
            h00 = complete_classical_histogram(0,middle,0,recorded_mode)
            h10 = complete_classical_histogram(1,middle,0,recorded_mode)
            h01 = complete_classical_histogram(0,middle,1,recorded_mode)
            need(h00==h10==h01, "all accessible final bit strings and occupation flags depend on a,c only through ac")
    # The endpoint complete maps are CP trace preserving. Their affine
    # combinations therefore remain instruments for every eta in [0,1].
    # Independent applications give products of endpoint weights, not a
    # shared hidden Bernoulli choice across the entire experiment.
    result = {"status":"EXACT_INDEPENDENT_OCCUPANCY_DEPHASING_INSTRUMENT",
              "variables":{"a":"prep ideal weight", "b":"recorded echo ideal weight", "c":"end ideal weight"},
              "instrument":"N0 ideal; occupied Kraus sqrt(eta)Pminus and sqrt(1-eta)B_color, separately summed histories",
              "retained_polynomials":{k:str(v) for k,v in keep.items()},
              "recorded_polynomials":{k:str(v) for k,v in fresh.items()},
              "common_eta":{"retained":str(common_keep),"recorded":str(common_fresh),"gap":str(common_gap),
                            "ratio":str(s.factor(common_fresh/common_keep)),"prep_fidelity":str((1+5*eta)/6)},
              "end_effect":"(3*c/8) P_Omega + ((1-c)/16) Q6; Q6 is the sum of six orthonormal Schmidt-component projectors",
              "end_effect_spectrum":{"Omega":"(1+5c)/16","five_orthogonal_Q6_states":"(1-c)/16","remaining_250_states":"0"},
              "environment_Gram":{"Fidelity":"sum_cd G_cd / 36", "uniform_visibility":"G=eta*ones+(1-eta)*I6", "infidelity":"sum_(c<d) ||e_c-e_d||^2 /36"},
              "calibration":{"ac_from_retained":"(128*p_keep/3-1)/5",
                             "b_from_end_occupied_recorded":"128*p_end_occupied/3-10",
                             "prep_F_lower_bound_from_retained":"(1+5*a*c)/6 = 64*p_keep/9",
                             "individual_a_and_c_identified":False,
                             "nonidentifiability_includes_all_final_bit_strings":True,
                             "common_eta_from_retained":"sqrt((128*p_keep/3-1)/5)",
                             "one_part_per_million_prep_infidelity_max_color_dephasing_weight":"3/2500000"},
              "retained_corners":{str(k):{q:str(v) for q,v in vals.items()} for k,vals in retained.items()},
              "recorded_corners":{str(k):{q:str(v) for q,v in vals.items()} for k,vals in recorded.items()},
              "source_sha256":hashlib.sha256(EP_PATH.read_bytes()).hexdigest(),
              "check_count":len(CHECKS), "checks":CHECKS}
    args.out.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k not in ["checks","retained_corners","recorded_corners"]},indent=2))


if __name__ == "__main__":
    main()
