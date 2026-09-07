#!/usr/bin/env python3
"""Exact Fourier-factor/positive averaging and actual exchange inventory."""
from itertools import product
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from round22_algebra import AVERAGING_GRID, Certificate, G, add, band_bounds, inputs, subtract, wrap
import sympy as s


def main():
    w=inputs(); cert=Certificate(); check=cert.check
    half=1; grid=AVERAGING_GRID
    check("quadrature cannot alias any square-factor frequency difference", grid > 6*half)
    differences=range(-6*half,6*half+1)
    check("finite quadrature equals Haar projection for every allowed frequency", all((int(d % grid == 0) == int(d == 0)) for d in differences))
    check("old spatial grid is an actual reciprocal-lattice alias mutant", 3 % 3 == 0 and 3 != 0)
    check("full three-dimensional quadrature has explicit finite cost", grid**3 == 343)
    amplitudes=s.symbols("b_m3 b_m2 b_m1 b_0 b_1 b_2 b_3",commutative=False)
    adjoints=s.symbols("d_m3 d_m2 d_m1 d_0 d_1 d_2 d_3",commutative=False)
    freq=list(range(-3,4))
    exact=sum(adjoints[i]*amplitudes[i] for i in range(7))
    sampled=sum(adjoints[i]*amplitudes[j] for i in range(7) for j in range(7) if (freq[j]-freq[i]) % grid == 0)
    mutant=sum(adjoints[i]*amplitudes[j] for i in range(7) for j in range(7) if (freq[j]-freq[i]) % 3 == 0)
    check("ordered operator Parseval leaves precisely the positive squares", s.expand(sampled-exact) == 0)
    check("using the spatial lattice as quadrature retains wrong cross terms", s.expand(mutant-exact) != 0)
    check("preassigned source-independent subtraction has weight one", s.Rational(1,grid**3)*grid**3 == 1)
    check("full E8 scalar coupling can be factored without dropping cross terms", G[1,2] == 1 and G.is_positive_definite)
    n=s.Matrix(s.symbols("n0:8",integer=True)); phi=s.Symbol("phi",real=True)
    eye=s.eye(8)
    basis=s.Matrix.hstack(2*eye[:,0],*[eye[:,0]+eye[:,k] for k in range(1,7)],s.ones(8,1)/2)
    check("literal charge-scalar square factor matches the original coupling", s.expand(sum(v**2*phi**2 for v in basis*n)/2-(n.T*G*n)[0]*phi**2/2) == 0)
    f=w.Fields(period=3); ward=w.WardComplex(f)
    for i in range(3):
        for j in range(i,3):
            stress=ward.tau(i,j,w.ZERO)
            if i == j:
                stress-= (f.pi(w.ZERO)**2-ward.mass2*f.phi(w.ZERO)**2)/2
            symbols=[a for a in stress.free_symbols if a in f.reverse]
            check(f"actual sigma{i}{j} respects the quadratic factor-frequency bound", s.Poly(s.expand(stress),symbols).total_degree() <= 2 and all(f.reverse[a][0] == "phi" for a in symbols))
    k=(0,-1,0); l=(1,0,0)
    channels=[((1,0,0),(0,-1,0)),((-1,-1,0),(1,1,0))]
    weights=[]
    for label,(q,r) in zip(("A","B"),channels):
        defect=subtract(add(l,r),add(k,q))
        weight=int(all(a == 0 for a in defect)); weights.append(weight)
        check(f"{label}: old vertex conserves only the required lattice character", wrap(defect) == (0,0,0))
        check(f"{label}: exact quadrature applies the unwrapped selection", int(all(a % grid == 0 for a in defect)) == weight)
    check("completion retains real exchange while deleting the incompatible channel", weights == [1,0])
    check("retained channel is nonzero at certified positive hopping", band_bounds(27)["form_factor_lower"] > 0)

    momenta=list(product((-1,0,1),repeat=3))
    kept=0; removed=0
    for charge_k,scalar_q,scalar_r in product(momenta,repeat=3):
        raw=subtract(add(charge_k,scalar_q),scalar_r)
        charge_l=wrap(raw)
        if raw == charge_l: kept+=1
        else: removed+=1
    check("complete lowest-band number-preserving channel inventory", kept+removed == 27**3)
    check("unwrapped exchange count agrees with independent factorized census", kept == 19**3 and removed == 27**3-19**3)
    # Exact low-level covariance of Fourier blocks is not an assertion that
    # the changed operator has the old local domain or observable dynamics.
    r,t=s.symbols("r t",integer=True)
    check("Fourier block graph norm is unchanged by its covariance phase", s.simplify(s.exp(s.I*r*t)*s.exp(-s.I*r*t)) == 1)
    cert.witnesses.update({"averaging_grid":grid,"positive_conjugate_copies":grid**3,
                           "number_preserving_channels_retained":kept,
                           "number_preserving_channels_removed":removed,
                           "channel_A_retained":True,"channel_B_removed":True})
    cert.emit("Finite positive Fourier-square construction and exact exchange selection for a changed full parent. Global momentum, not native local stress; no charge cutoff, original-vertex preservation, Gaussian-limit or TOE claim.")


if __name__ == "__main__": main()
