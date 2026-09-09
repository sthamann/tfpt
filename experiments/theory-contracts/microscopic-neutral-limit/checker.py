"""Full neutral-source proof checks. Not charged fields, four-dimensional QFT or TOE."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PINS = {
    "experiments/theory-contracts/source-current-symbol-match/checker.py":
    "b5aba00e28885a43965a75a45733ad9eb4ce8b12d624a83da942bc3848652d37",
    "experiments/theory-contracts/current-truncation-bridge/checker.py":
    "0bcd39189a0b504f181670d4113437f706608b6d43af8267965e70c2ff1d3eda",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def inherited():
    modules = []
    for index, (name, digest) in enumerate(PINS.items()):
        path = ROOT / name
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest, "source pin: " + name)
        spec = importlib.util.spec_from_file_location("neutral_limit_parent_" + str(index), path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        modules.append(module)
    symbol, truncation = modules
    linear, history, gaussian, source = symbol.inherited()
    return symbol, truncation, linear, history, gaussian, source


def low_constants(n):
    symbol, _, linear, _, _, _ = inherited()
    m = linear.cutoff(n)
    lam = m / (8*n)
    r = 8*lam**2
    s = 2*r**7.5
    jj = symbol.analytic_caps(n)["filtered_JJ_operator_bound"]
    local = jj + 4*np.pi*s + np.pi*(r**6+s)**2
    return dict(N=n, M=m, delta=4*n**(-.75), lambda_cut=lam,
                rho_low_cap=r, vector_low_cap=s, JJ_operator_cap=jj,
                low_operator_cap=local)


def history_envelope(dimension, delta, lam, local_cap, legs=2, raw_norm=2*np.pi):
    require(dimension >= 1 and delta > 0 and lam > 0 and local_cap >= 0,
            "positive comparison domain")
    require(isinstance(legs, int) and legs >= 1 and raw_norm > 0, "bounded unit-leg word")
    diff = 2*raw_norm
    gaussian = np.exp(-.5*(lam/delta)**2)
    epsilon = local_cap + diff*np.sqrt(dimension)*gaussian
    cross = np.sqrt(dimension)*(local_cap + 2*diff*gaussian)
    log_weighted_tail = legs*raw_norm*np.exp(.5)+.5-lam/delta
    weighted_tail = np.exp(log_weighted_tail)
    cap = legs*cross + legs**2*raw_norm*np.sqrt(dimension)*(epsilon+diff*weighted_tail)
    return dict(local_input_cap=epsilon, cross_HS_cap=cross,
                gaussian_tail=gaussian, log_weighted_tail=float(log_weighted_tail),
                history_integral_cap=float(cap))


def full_caps(n):
    row = low_constants(n)
    row.update(history_envelope(16*n,row["delta"],row["lambda_cut"],row["low_operator_cap"]))
    return row


def low_inventory(n):
    """All exact source momenta, only 16x16 spectral problems, no dense large H."""
    _, _, linear, _, _, source = inherited()
    m = linear.cutoff(n)
    lam = m/(8*n)
    top_count = bottom_count = 0
    errors, tails, bottom_equation_errors = [], [], []
    for label in range(-(n//2), n-n//2):
        p = (2*np.pi*label-np.pi/2)/n
        h = source.strip_at_momentum(p,8)
        j = None
        if -m <= label <= m:
            data = linear.source_strip(n,label,source)
            sharp, j = data["sharp"], data["j"]
        else:
            sharp = h
        values, vectors = np.linalg.eigh(sharp)
        for index in np.flatnonzero(abs(values)<=2*lam):
            require(j is not None, "no missing-window low mode")
            vector = vectors[:,index]
            if abs(np.vdot(j,vector))**2 > .5:
                top_count += 1
                continue
            bottom_count += 1
            rho = 2*np.sin(p/2)**2
            q = np.kron(rho**np.arange(8),[1,-1]).astype(complex)
            q /= np.linalg.norm(q)
            overlap = np.vdot(q,vector)
            vector = vector*overlap.conjugate()/abs(overlap)
            errors.append(float(np.linalg.norm(vector-q)))
            tails.append(float(np.linalg.norm(vector[-4:])))
            bottom_equation_errors.append(float(np.linalg.norm(h@vector-values[index]*vector)))
            require(values[index]*p > 0, "R-low is bottom sign, not hidden top")
    return dict(N=n, top_count=top_count, bottom_count=bottom_count,
                largest_bottom_vector_difference=max(errors,default=0.),
                largest_bottom_top2_tail=max(tails,default=0.),
                largest_original_bottom_equation_residual=max(bottom_equation_errors,default=0.),
                tiny_vector_caps_not_float_interval_certified=True)


def raw_endpoint(n,length):
    require(isinstance(length,int) and 0<=length<n, "lattice endpoint")
    ramp = np.repeat(np.pi*np.arange(n)/n,16)
    arc = np.zeros((n,8,2))
    arc[:length,-2:,:]=1
    return ramp+np.pi*arc.reshape(-1)


def full_source_diagnostic(n,a=0,b=None,order=5):
    """Original full determinant and full histories; finite floating corroboration."""
    symbol, truncation, linear, history, gaussian, _ = inherited()
    if b is None:
        b=n//2
    require(n<=64, "small full-source diagnostic only")
    data=gaussian.source_case(n)
    j,labels,rp,_=history.embedding(data,linear.cutoff(n))
    p=data["e"]<0
    remainder=np.eye(16*n)-j@j.conj().T
    momenta=(2*np.pi*labels-np.pi/2)/n
    h=np.diag(data["e"])
    sharp=(j*(-momenta))@j.conj().T+remainder@h@remainder
    to_energy=lambda diagonal: data["v"].conj().T@(diagonal[:,None]*data["v"])
    raw=[to_energy(raw_endpoint(n,length)) for length in (a,b)]
    original=[linear.filter_matrix(h,k,data["delta"]) for k in raw]
    filtered=[linear.filter_matrix(sharp,k,data["delta"]) for k in raw]
    small=dict(N=n,labels=labels,t=n*data["delta"])
    currents=[symbol.halfcell_current(small,length) for length in (a,b)]
    empty=linear.filter_matrix(sharp,to_energy(data["ramp"]),data["delta"])
    common=remainder@empty@remainder
    refs=[j@k@j.conj().T+common for k in currents]
    signed=lambda pair: [-pair[0],pair[1]]
    source_rows=history.history_blocks(signed(original),p)
    sharp_rows=history.history_blocks(signed(filtered),p)
    ref_rows=history.history_blocks(signed(refs),p)
    source_amp=history.normal_overlap(signed(original),p)
    ref_amp=history.normal_overlap(signed(refs),p)
    small_amp=history.normal_overlap(signed(currents),rp)
    _,current=truncation.inherited()
    target=current.comparator(n*data["delta"],((b-a)%n)/n)
    ideal=np.exp(-target["loss"]+1j*target["phase"])
    z2=np.exp(target["harmonic"]/4)
    return dict(N=n,a=a/n,b=b/n,
                measured_I_linearization=history.history_comparison(source_rows,sharp_rows,order)["history_HS_integral_estimate"],
                measured_I_sharp_reference=history.history_comparison(sharp_rows,ref_rows,order)["history_HS_integral_estimate"],
                measured_I_source_reference=history.history_comparison(source_rows,ref_rows,order)["history_HS_integral_estimate"],
                reference_completion_amplitude_residual=float(abs(ref_amp-small_amp)),
                normalized_source_current_error=float(z2*abs(source_amp-ideal)),
                source_real=float(source_amp.real),source_imag=float(source_amp.imag),
                quadrature_order=order,finite_floats_not_limit_proof=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    report=dict(status="MICROSCOPIC_NEUTRAL_PAIR_PROOF_WITH_INTERNAL_REVIEW",
                pins=PINS, bounds=[full_caps(n) for n in (64,256,1024,65536,1048576)],
                low_inventory=[low_inventory(n) for n in (64,256,1024)],
                full_source=[full_source_diagnostic(n) for n in (8,16,32)],
                charged_fields_constructed=False, eight_channel_identification=False,
                four_dimensional_QFT_complete=False, TOE_complete=False)
    content=json.dumps(report,indent=2)+"\n"
    if args.output:
        args.output.write_text(content)
    else:
        print(content,end="")


if __name__=="__main__":
    main()
