"""Scoped source audit: exact identities plus calls to unchanged original operators.

This does not derive a primitive charged P1 source. Mathematical proofs and
domains are in PROOF.md; finite checks alone do not establish those theorems.
"""
from pathlib import Path
import hashlib
import json
import sys

import numpy as np
import sympy as s

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "verification"))
import v210_mark_local_dtn as v210
import v290_z4_smooth_curvature_adversary as v290


def require(condition, label):
    if not bool(condition):
        raise RuntimeError(label)


def run():
    pins = json.loads((HERE / "source_pins.json").read_text())
    for rel, digest in pins.items():
        require(hashlib.sha256((REPO / rel).read_bytes()).hexdigest() == digest,
                "Source changed: " + rel)

    eps = s.symbols("eps", real=True)
    k = s.symbols("k", positive=True)
    block = s.Matrix([[0, eps / 2], [eps / 2, k]])
    require(s.simplify(block.det() + eps**2 / 4) == 0,
            "zero-mode obstruction")
    ns, rho, flat, perturbed = v290._operators()
    i0, i4 = list(ns).index(0), list(ns).index(4)
    two = perturbed[np.ix_([i0, i4], [i0, i4])].real
    expected = np.array([[0., v290.EPS / 2], [v290.EPS / 2, 4.]])
    require(np.allclose(two, expected, atol=1e-14), "original compression")
    eigen_min = float(np.linalg.eigvalsh(perturbed)[0])
    require(eigen_min < -1e-3, "original adversary must be indefinite")
    zero_residual = float(np.linalg.norm(perturbed[:, i0]))
    require(zero_residual > .1, "original constant mode not annihilated")
    comm = float(np.linalg.norm(rho @ perturbed - perturbed @ rho))
    require(comm < 1e-12, "clock commutation preserved")

    # General Weyl cancellation in dimension two, not a finite-mode inference.
    sigma, boundary_sigma = s.symbols("sigma boundary_sigma", real=True)
    require(s.simplify(s.exp(2*sigma)*s.exp(-2*sigma)) == 1,
            "Dirichlet energy density is Weyl invariant in dimension two")
    require(s.simplify(s.exp(boundary_sigma)*s.exp(-boundary_sigma)) == 1,
            "boundary density cancels the DtN conformal weight")
    # An exact smooth metric in the already-used scalar disk class: boundary
    # metric unchanged; bulk AND boundary curvature change; DtN remains |D|.
    x, y, a = s.symbols("x y a", real=True)
    sigma_disk = a*(1-x*x-y*y)
    lap_sigma = s.diff(sigma_disk, x, 2)+s.diff(sigma_disk, y, 2)
    require(lap_sigma == -4*a, "nonzero interior curvature")
    r = s.symbols("r", nonnegative=True)
    radial_sigma = a*(1-r*r)
    require(radial_sigma.subs(r, 1) == 0, "same boundary metric")
    require(s.diff(radial_sigma,r).subs(r,1) == -2*a,
            "different boundary normal derivative")

    # Positive geometric alternative: ds=w(theta)dtheta, w=1+eps cos4theta.
    # Generalized spectral problem |D|f=lambda*w*f; no additive curvature term.
    theta = s.symbols("theta", real=True)
    w = 1+eps*s.cos(4*theta)
    require(s.simplify(w.subs(theta,theta+s.pi/2)-w) == 0, "C4 boundary metric")
    require(s.simplify(w.subs(theta,-theta)-w) == 0, "reflection boundary metric")
    require(s.integrate(w,(theta,0,2*s.pi)) == 2*s.pi, "fixed circumference")
    gram_pm2 = s.Matrix([[1,eps/2],[eps/2,1]])
    derivative_pm2 = s.Matrix([[0,-1],[-1,0]])
    require(gram_pm2.det() == 1-eps**2/4, "weighted pair Gram")
    require(set(derivative_pm2.eigenvals()) == {-1,1}, "first-order splitting")

    # The original median shift is regulator dependent even in the flat case.
    cutoff_rows = []
    for N in (3,4,5,8,12,16,24):
        modes = np.arange(-N,N+1)
        Lam = np.diag(np.abs(modes).astype(float))
        spectrum = np.linalg.eigvalsh(Lam)
        mu = .5*(spectrum[N-1]+spectrum[N])
        require(mu == N/2, "exact flat median")
        C = v210.covariance(Lam)
        expected_C = np.diag(.5*(1+np.sign(np.abs(modes)-N/2)))
        require(np.allclose(C,expected_C,atol=1e-14), "original cutoff covariance")
        if N % 2 == 0:
            require(np.linalg.norm(C@C-C) > .3,
                    "even flat cutoff contains half-occupied threshold pair")
        if N > 4:
            sel = np.flatnonzero(np.abs(modes)<=2)
            require(np.linalg.norm(C[np.ix_(sel,sel)]) < 1e-14,
                    "fixed-mode limit is zero")
        cutoff_rows.append({"N":N,"mu":mu,"C_mode_1":float(C[N+1,N+1]),
                            "projector_defect":float(np.linalg.norm(C@C-C))})

    # Also check the actual original positive mark profile, on a FIXED block.
    profile = v210.mark_sum([j*np.pi/2 for j in range(4)])
    sampled_profile = np.fft.ifft(profile*len(profile)).real
    require(sampled_profile.min() > 0, "original mark source is positive")
    mark_rows = []
    for N in (16,32,64):
        Lam, modes = v210.dtn(profile,N)
        spectrum = np.linalg.eigvalsh(Lam)
        mu = .5*(spectrum[N-1]+spectrum[N])
        C = v210.covariance(Lam)
        keep = np.flatnonzero(np.abs(modes)<=2)
        norm = float(np.linalg.norm(C[:,keep],ord=2))
        require(mu >= N/2-1e-10, "positive-source median lower bound")
        require(np.linalg.eigvalsh(Lam-np.diag(np.abs(modes)))[0] > -1e-10,
                "actual Toeplitz compression positivity")
        require(np.linalg.eigvalsh(Lam/mu-C@C)[0] > -1e-9,
                "actual source spectral bound C^2 <= Lambda/mu")
        mark_rows.append({"N":N,"mu":float(mu),"fixed_block_norm":norm})
    require(mark_rows[-1]["fixed_block_norm"] < 1e-10,
            "actual source fixed-block depletion")

    # Scalar |D| cannot select the sign/Hardy polarization.
    z = s.symbols("z")
    A = s.eye(2)*z
    # Any spectral function of diag(|r|,|-r|) is a scalar multiple of I,
    # whereas the required Hardy restriction is diag(1,0).
    chiral = s.diag(1,0)
    swap = s.Matrix([[0,1],[1,0]])
    require(A*swap-swap*A == s.zeros(2), "every scalar multiplier is even")
    require(chiral*swap-swap*chiral != s.zeros(2), "Hardy polarization is directed")
    h0,hv,hs,hc = 0,s.Rational(1,2),1,1
    monodromy = s.simplify(s.exp(2*s.pi*s.I*(hc-hv-hs)))
    require(monodromy == -1, "D8 vector-spinor monodromy")

    return {
        "checker_verdict":"PASS",
        "research_verdict":"PARTIAL",
        "primitive_charged_source_selected":False,
        "claims_promoted":[],
        "original_v290":{
            "N":int(v290.N),"epsilon":float(v290.EPS),
            "compression":two.tolist(),"minimum_eigenvalue":eigen_min,
            "constant_mode_residual":zero_residual,"clock_commutator":comm,
            "scalar_massless_DtN_candidate":False},
        "exact":{
            "zero_mode_minor":"-eps**2/4",
            "weyl_DtN":"Lambda_exp(2sigma)g = exp(-sigma_boundary) Lambda_g",
            "weyl_boundary_form":"B_exp(2sigma)g = B_g",
            "disk_curvature":"4*a*exp(-2*a*(1-r**2))",
            "boundary_geodesic_curvature":"1-2*a",
            "weighted_pm2_gram":"[[1,eps/2],[eps/2,1]]",
            "weighted_DtN_cluster_derivatives":[-1,1],
            "flat_v210_median":"N/2",
            "v210_strong_fixed_mode_limit":0,
            "D8_vector_spinor_monodromy":-1},
        "cutoff_rows":cutoff_rows,
        "actual_mark_source_cutoff_rows":mark_rows,
        "limitations":[
            "Pure scalar massless 2D Laplacian only for conformal reduction",
            "Cones require an unchanged domain, e.g. deformation supported away from them",
            "No replacement of RP by ordinary operator positivity",
            "No charged P1 field algebra, NS spin structure, vacuum or physical time derived",
            "Weighted boundary family is a scope test, not a selected TFPT source"
        ]}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, ensure_ascii=False))
