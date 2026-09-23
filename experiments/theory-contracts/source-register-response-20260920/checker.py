#!/usr/bin/env python3
"""Bounded exact source ground/charged response and numerical determinant replay.

The analytic arbitrary-size statement is in PROOF.md. This program validates
the original six-mode diagnostic and independent exterior/Fock identities.
No assertions: checks stay active under python -OO.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
DEFAULT_REPO = Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
COUNTS = {'exact': 0, 'numeric': 0, 'provenance': 0}
MAX_ERROR = 0.0


def require(ok, message, kind='exact'):
    COUNTS[kind] += 1
    if not bool(ok):
        raise RuntimeError(message)


def near(a, b, message, tol=3e-12):
    global MAX_ERROR
    err = float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
    MAX_ERROR = max(MAX_ERROR, err)
    require(err < tol, message + ': error=' + str(err), 'numeric')


def canon(a):
    # These matrices contain Gaussian rationals only; expansion keeps exact
    # arithmetic compact without repeatedly invoking general simplification.
    return a.applyfunc(sp.expand)


def eq(a, b, message):
    require(canon(a-b) == sp.zeros(a.rows, a.cols), message)


def npmat(a):
    return np.array(a.evalf(17)).astype(complex)


def basis(d, n):
    return list(itertools.combinations(range(d), n))


def annihilator(d, n, j):
    src = basis(d, n)
    dst = {v: i for i, v in enumerate(basis(d, n-1))}
    out = sp.zeros(len(dst), len(src))
    for col, occupied in enumerate(src):
        if j in occupied:
            pos = occupied.index(j)
            out[dst[occupied[:pos]+occupied[pos+1:]], col] = (-1)**pos
    return out


def dgamma(h, n):
    d = h.rows
    size = len(basis(d, n))
    if n == 0:
        return sp.zeros(1)
    cs = [annihilator(d, n, j) for j in range(d)]
    out = sp.zeros(size)
    for i in range(d):
        for j in range(d):
            if h[i, j] != 0:
                out += h[i, j] * cs[i].H * cs[j]
    return out


def wedge_columns(v):
    return sp.Matrix([v.extract(list(occ), range(v.cols)).det()
                      for occ in basis(v.rows, v.cols)])


def exterior_numeric(u, n):
    bs = basis(u.shape[0], n)
    return np.array([[np.linalg.det(u[np.ix_(i, j)]) for j in bs]
                     for i in bs], dtype=complex)


def adjugate_numeric(a):
    """Cofactors, no inverse: valid also at det(a)=0."""
    n = a.shape[0]
    if n == 1:
        return np.ones((1, 1), dtype=complex)
    return np.array([[(-1)**(i+j) * np.linalg.det(
        np.delete(np.delete(a, j, axis=0), i, axis=1))
        for j in range(n)] for i in range(n)], dtype=complex)


def kernels(u, v):
    gram = np.linalg.det(v.conj().T @ v)
    overlap = v.conj().T @ u @ v
    adj = adjugate_numeric(overlap)
    minus = v @ adj @ v.conj().T / gram
    plus = (np.linalg.det(overlap)*u - u @ v @ adj @ v.conj().T @ u)/gram
    return plus, minus


def unitary(h, t):
    vals, vecs = np.linalg.eigh(h)
    return (vecs * np.exp(-1j*t*vals)) @ vecs.conj().T


def pin_sources(repo):
    manifest = json.loads((HERE/'source_manifest.json').read_text())
    for row in manifest['sources']:
        path = (repo if row['root'] == 'repo' else HERE)/row['path']
        require(path.is_file(), 'missing source '+str(path), 'provenance')
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        require(digest == row['sha256'], 'changed source '+str(path), 'provenance')
    return manifest['sources']


def run(repo):
    pins = pin_sources(repo)
    helper = repo/'experiments/theory-contracts/source-static-register-20260920/checker.py'
    spec = importlib.util.spec_from_file_location('pinned_static_register', helper)
    upstream = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(upstream)
    upstream.source_audit(repo)
    hs, base, seam = upstream.source_blocks()
    upstream.compare_original_functions(repo, hs, base, seam)
    require(upstream.CHECK_COUNT > 0, 'original function comparison did not run', 'provenance')
    d = 6
    u = sp.diag(sp.I, sp.I, 1, 1, 1, 1)
    hp = [u**(-r)*h*u**r for r, h in enumerate(hs)]
    for r, h in enumerate(hp):
        eq(h, h.H, 'original Hermitian final block '+str(r))
    x = sp.Symbol('x')
    polys = [sp.factor(h.charpoly(x).as_expr()) for h in hs]
    require(polys[0] == x**2*(x*x-3)**2, 'r0 spectrum')
    require(polys[1] == (x*x-2)*(x**4-4*x*x+1), 'r1 spectrum')
    require(polys[2] == (x-2)*(x-1)**2*(x+1)**2*(x+2), 'r2 spectrum')
    require(polys[3] == polys[1], 'r3 spectrum')
    # Complete Fock ground is found by filling each negative one-particle mode.
    energies = [-2*sp.sqrt(3), -sp.sqrt(6)-sp.sqrt(2), -sp.Integer(4),
                -sp.sqrt(6)-sp.sqrt(2)]
    gap = 4-sp.sqrt(6)-sp.sqrt(2)
    require(gap.is_positive, 'global finite ground gap positive')
    require((4-2*sp.sqrt(3)-gap).is_positive, 'r0 lies above first excited level')
    require((1-gap).is_positive, 'r2 internal Fock gap is larger')
    require((2-sp.sqrt(3)) > 0, 'r1/r3 lack zero modes')
    h0 = hp[2]
    p = canon((sp.eye(d)-(7*h0-h0**3)/6)/2)
    eq(p*p, p, 'ground one-body projector idempotence')
    eq(p.H, p, 'ground one-body projector Hermitian')
    require(sp.trace(p) == 3 and sp.trace(h0*p) == -4, 'ground rank and energy')
    v = sp.Matrix.hstack(*p.columnspace())
    gramdet = sp.factor((v.H*v).det())
    require(gramdet == sp.Rational(1, 144), 'ground Slater Gram determinant')
    psi = canon(12*wedge_columns(v))
    require((psi.H*psi)[0] == 1, 'ground normalized')
    h_n3 = dgamma(h0, 3)
    eq(h_n3*psi, -4*psi, 'exact encoded ground equation')
    rho = psi*psi.H
    exterior_p = sp.Matrix([[p.extract(i, j).det() for j in basis(d, 3)]
                            for i in basis(d, 3)])
    eq(rho, exterior_p, 'ground density is third exterior projector')
    vm = sp.Matrix.hstack(*[annihilator(d, 3, j)*psi for j in range(d)])
    vp = sp.Matrix.hstack(*[annihilator(d, 4, j).H*psi for j in range(d)])
    eq((vm.H*vm).T, p, 'removal zeroth moment')
    eq(vp.H*vp, sp.eye(d)-p, 'addition zeroth moment')
    # s=1, initial r=2,N=3. Creation decreases r, annihilation increases r.
    plus_h = dgamma(hp[1], 4)
    minus_h = dgamma(hp[3], 2)
    plus_q = plus_h+4*sp.eye(plus_h.rows)
    minus_q = minus_h+4*sp.eye(minus_h.rows)
    # Comparison is the same initial sea with the register spuriously frozen.
    plus_frozen = dgamma(h0, 4)+4*sp.eye(15)
    minus_frozen = dgamma(h0, 2)+4*sp.eye(15)
    moments = []
    pow_plus = sp.eye(15); pow_minus = sp.eye(15)
    pow_plus_f = sp.eye(15); pow_minus_f = sp.eye(15)
    for k in range(5):
        mp = canon(vp.H*pow_plus*vp)
        mm = canon((vm.H*pow_minus*vm).T)
        fp = canon(vp.H*pow_plus_f*vp)
        fm = canon((vm.H*pow_minus_f*vm).T)
        require(mp == mp.H and mm == mm.H, 'moment Hermiticity '+str(k))
        row = {'order':k, 'addition_trace':str(sp.trace(mp)),
               'removal_trace':str(sp.trace(mm)),
               'frozen_addition_trace':str(sp.trace(fp)),
               'frozen_removal_trace':str(sp.trace(fm)),
               'addition_diagonal':[str(mp[i,i]) for i in range(d)],
               'removal_diagonal':[str(mm[i,i]) for i in range(d)]}
        moments.append(row)
        pow_plus = canon(pow_plus*plus_q); pow_minus = canon(pow_minus*minus_q)
        pow_plus_f = canon(pow_plus_f*plus_frozen); pow_minus_f = canon(pow_minus_f*minus_frozen)
    require(moments[1]['addition_trace'] != moments[1]['frozen_addition_trace'],
            'first moment detects the changed source evolution')
    expected_actual = ['3','16/3','115/9','115/3','1220/9']
    expected_frozen = ['3','4','6','10','18']
    for k, row in enumerate(moments):
        require(row['addition_trace'] == row['removal_trace'] == expected_actual[k],
                'exact actual total moment '+str(k))
        require(row['frozen_addition_trace'] == row['frozen_removal_trace'] == expected_frozen[k],
                'exact frozen total moment '+str(k))
    # Exact rational trace resolvent. Thirteen genuine poles, no numerical cutoff.
    # Here x is final unshifted Fock energy; charged energy is x+4.
    denominator = x*(x*x-2)*(x*x-6)*(x**4-4*x*x+1)*(x**4-12*x*x+9)
    denominator = sp.Poly(denominator, x)
    require(sp.factor(plus_h.charpoly(x).as_expr()-x*x*denominator.as_expr()) == 0,
            'full addition characteristic polynomial')
    require(sp.factor(minus_h.charpoly(x).as_expr()-x*x*denominator.as_expr()) == 0,
            'full removal characteristic polynomial')
    require(sp.gcd(denominator,denominator.diff()).degree() == 0,
            'thirteen distinct roots')
    coeffs = denominator.all_coeffs()
    polys_response=[]
    for label, h, vectors in [('addition',plus_h,vp),('removal',minus_h,vm)]:
        vvectors = vectors
        seq=[]
        for k in range(14):
            seq.append(sp.expand(sp.trace(vectors.H*vvectors)))
            vvectors = canon(h*vvectors)
        require(sp.expand(sum(coeffs[i]*seq[13-i] for i in range(14))) == 0,
                label+' trace recurrence')
        numerator = sp.Poly(sum(sum(coeffs[i]*seq[j-i] for i in range(j+1))*x**(12-j)
                                for j in range(13)), x)
        require(sp.gcd(numerator,denominator).degree() == 0,
                label+' no pole cancellation: all thirteen weights nonzero')
        polys_response.append(numerator)
    require(polys_response[0] == polys_response[1], 'addition and removal total measures agree exactly')
    # D is the supplied even register-shift observable. In encoded coordinates
    # it keeps the matter vector but changes s, hence r, by one.
    disorder = {}
    disorder_ops = {}
    for label, rfinal in [('D',3),('D_adjoint',1)]:
        qd = dgamma(hp[rfinal],3)+4*sp.eye(20)
        disorder_ops[label] = qd
        vec = psi
        dm=[]
        for k in range(5):
            dm.append(str(sp.expand((psi.H*vec)[0])))
            vec=canon(qd*vec)
        vals,vecs=np.linalg.eigh(npmat(qd))
        weights=np.abs(vecs.conj().T@npmat(psi)).ravel()**2
        near(vals[0], float(gap), label+' accesses full-system gap energy')
        require(weights[0]>1e-6, label+' global first gap has nonzero weight', 'numeric')
        # Exact negative projector for the r=1,3 spectra. Its third exterior
        # power is the unique final sea; overlap gives the exact threshold weight.
        c0=-sp.sqrt(2)/6+sp.sqrt(6)
        c1=-5*sp.sqrt(6)/6+2*sp.sqrt(2)/3
        c2=-sp.sqrt(2)/6+sp.sqrt(6)/6
        hd=hp[rfinal]
        pd=canon((sp.eye(6)-c0*hd-c1*hd**3-c2*hd**5)/2)
        eq(pd*pd,pd,label+' final negative projector')
        require(sp.expand(sp.trace(pd))==3,label+' final occupied rank')
        require(sp.expand(sp.trace(hd*pd))==-sp.sqrt(6)-sp.sqrt(2),label+' final sea energy')
        exact_weight=sp.expand(canon(v.H*pd*v).det()/gramdet)
        expected_weight=35*sp.sqrt(3)/324+343*sp.sqrt(2)/2592+25*sp.sqrt(6)/324+sp.Rational(245,1296)
        require(sp.expand(exact_weight-expected_weight)==0,label+' exact nonzero lowest residue')
        require(exact_weight.is_positive,label+' exact positive lowest residue')
        near(weights[0],float(exact_weight),label+' lowest weight exact versus numerical')
        disorder[label]={'moments':dm,'lowest_energy_exact':str(gap),
                         'lowest_weight_numeric':float(weights[0]),
                         'lowest_weight_exact':str(exact_weight)}
    # Independent 1-particle exterior evolution versus many-body Hamiltonian.
    times = [0.0, 0.125, 0.5, 1.0, 2.5, 7.0]
    vn = npmat(v); vpn = npmat(vp); vmn = npmat(vm)
    for t in times:
        up = unitary(npmat(hp[1]), t)
        um = unitary(npmat(hp[3]), t)
        kp, _ = kernels(up, vn)
        _, km = kernels(um, vn)
        phase = np.exp(-4j*t)
        ep = unitary(npmat(plus_q), t)
        em = unitary(npmat(minus_q), t)
        near(phase*kp, vpn.conj().T@ep@vpn, 'addition determinant at '+str(t))
        near(phase*km, (vmn.conj().T@em@vmn).T, 'removal determinant at '+str(t))
        near(phase*exterior_numeric(up, 4), ep, 'addition exterior at '+str(t))
        near(phase*exterior_numeric(um, 2), em, 'removal exterior at '+str(t))
        for label, rfinal in [('D',3),('D_adjoint',1)]:
            ud = unitary(npmat(hp[rfinal]),t)
            det_answer = phase*np.linalg.det(vn.conj().T@ud@vn)/float(gramdet)
            fock_answer = (npmat(psi).conj().T@unitary(npmat(disorder_ops[label]),t)@npmat(psi))[0,0]
            near(det_answer,fock_answer,label+' determinant at '+str(t))
    # Exact singular-overlap test: exchange occupied e0 with empty e2.
    uv = sp.eye(4); uv[0,0]=uv[2,2]=0; uv[0,2]=uv[2,0]=1
    vv = sp.eye(4)[:, :2]
    ov = vv.H*uv*vv
    require(ov.det() == 0, 'singular overlap control is genuinely singular')
    adj = ov.adjugate()
    kmx = vv*adj*vv.H
    kpx = ov.det()*uv-uv*vv*adj*vv.H*uv
    psix = wedge_columns(vv)
    cxm = sp.Matrix.hstack(*[annihilator(4,2,j)*psix for j in range(4)])
    cxp = sp.Matrix.hstack(*[annihilator(4,3,j).H*psix for j in range(4)])
    gx3 = sp.Matrix([[uv.extract(i,j).det() for j in basis(4,3)] for i in basis(4,3)])
    eq(kmx, (cxm.H*uv*cxm).T, 'singular exact removal cofactor identity')
    eq(kpx, cxp.H*gx3*cxp, 'singular exact addition bordered determinant')
    require(kmx != sp.zeros(4) and kpx != sp.zeros(4), 'singular response is nonzero')
    # Non-Hermitian U and complex nonorthogonal V: independent general identity.
    vu = sp.Matrix([[1,sp.I],[2,1],[sp.I,2],[1,-1]])
    xu = sp.Matrix([[1,sp.I,2,0],[0,2,1,sp.I],[1,0,3,1],[sp.I,1,0,2]])
    wg = sp.factor((vu.H*vu).det())
    ws = wedge_columns(vu)
    wm = sp.Matrix.hstack(*[annihilator(4,2,j)*ws for j in range(4)])
    wp = sp.Matrix.hstack(*[annihilator(4,3,j).H*ws for j in range(4)])
    xa = vu.H*xu*vu; xadj=xa.adjugate()
    xm=canon(vu*xadj*vu.H/wg)
    xp=canon((xa.det()*xu-xu*vu*xadj*vu.H*xu)/wg)
    xg3=sp.Matrix([[xu.extract(i,j).det() for j in basis(4,3)] for i in basis(4,3)])
    eq(xm, (wm.H*xu*wm).T/wg, 'general exact removal formula')
    eq(xp, wp.H*xg3*wp/wg, 'general exact addition formula')
    near(*[npmat(m) for m in [xm,sp.Matrix(kernels(npmat(xu),npmat(vu))[1])]],
         'numeric helper removal matches exact general cofactor')
    near(*[npmat(m) for m in [xp,sp.Matrix(kernels(npmat(xu),npmat(vu))[0])]],
         'numeric helper addition matches exact general bordered determinant')
    # Accessible spectral bottom; existence/weight also measured directly below.
    threshold = 4-sp.sqrt(2+sp.sqrt(3))-sp.sqrt(2)
    require(threshold.is_positive, 'charged transition spectrum nonnegative')
    spectral = {}
    for label, q, vectors in [('addition',plus_q,vp),('removal',minus_q,vm)]:
        vals, vecs = np.linalg.eigh(npmat(q))
        weights = np.sum(np.abs(vecs.conj().T@npmat(vectors))**2,axis=1)
        near(vals[0], float(threshold), label+' bottom exact versus numerical')
        require(weights[0] > 1e-6, label+' bottom has nonzero total weight', 'numeric')
        near(sum(weights), 3.0, label+' total spectral weight')
        grouped=[]
        for val, weight in zip(vals,weights):
            if grouped and abs(grouped[-1]['energy']-val)<1e-10:
                grouped[-1]['weight'] += float(weight)
                grouped[-1]['multiplicity'] += 1
            else:
                grouped.append({'energy':float(val),'weight':float(weight),'multiplicity':1})
        spectral[label]=grouped
    return {'contract':'UR.SOURCE.REGISTER_RESPONSE.01','verdict':'PARTIAL',
            'mathematical_verdict':'EXACT_CONDITIONAL_DETERMINANT_RESPONSE',
            'complete_TFPT_solution':False,
            'fixture':{'nx':3,'ny':1,'mass':1,'arc_endpoint':0,'modes':6,
                       'register_ground':2,'particle_number_ground':3,'encoded_class_s':1},
            'ground':{'energy':'-4','unique':True,'one_particle_characteristic_polynomials':[str(p) for p in polys],
                      'sector_ground_energies':[str(e) for e in energies],
                      'full_source_gap':str(gap),'slater_gram_determinant':str(gramdet)},
            'moments':moments,
            'trace_response_resolvent':{
                'variable':'x = charged_energy - 4',
                'numerator':str(polys_response[0].as_expr()),
                'denominator':str(sp.factor(denominator.as_expr())),
                'number_distinct_poles':13,'no_pole_cancellations_exact':True,
                'applies_to':'orbital trace of either positive-energy addition or removal measure'},
            'disorder_response':disorder,
            'charged_spectral_bottom':str(threshold),
            'spectral_weights_numeric':spectral,
            'time_samples':times,'numerical_max_abs_error':MAX_ERROR,
            'numerical_tolerance':3e-12,'counts':COUNTS,
            'upstream_original_definition_checks':upstream.CHECK_COUNT,
            'source_pins':pins,
            'scope':['Common register/Fock lift and completed charged field map assumed',
                     'Exact determinant formula proven separately for arbitrary finite dimension',
                     'Finite six-mode ground and moments, numerical all-matrix time samples',
                     'No physical selection of lift/field algebra or infinite-volume ground claimed',
                     'No local gauge completion, E8 channel derivation, 3+1D or T1-T8 closure'],
            'independent_agent_review':False}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--repo',type=Path,default=DEFAULT_REPO)
    parser.add_argument('--output',type=Path,default=HERE/'certificate.json')
    args=parser.parse_args()
    result=run(args.repo)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'output':str(args.output),'verdict':result['verdict'],
                      'counts':COUNTS,'max_error':MAX_ERROR},ensure_ascii=False))


if __name__=='__main__':
    main()
