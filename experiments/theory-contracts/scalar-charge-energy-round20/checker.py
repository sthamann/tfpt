#!/usr/bin/env python3
"""Exact Ward/energy-current checks on finite-support infinite-carrier vectors."""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import sympy as s


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ward-source", type=Path, default=Path(__file__).resolve().parents[1]/"free-scalar-3d/free_scalar_ward.py")
    args = parser.parse_args(); checks = []
    def check(label, ok):
        if not bool(ok): raise AssertionError(label)
        checks.append(label)
    spec = importlib.util.spec_from_file_location("r20_energy_actual_ward", args.ward_source)
    w = importlib.util.module_from_spec(spec); sys.modules[spec.name] = w
    spec.loader.exec_module(w)
    fields = w.Fields()
    class Profile(w.WardComplex):
        def u(self, x): return s.Symbol("u_"+self.f.label(self.f.wrap(x)), real=True)
        def force(self, x): return super().force(x)-self.u(x)*self.f.phi(x)
        def rho(self, x): return super().rho(x)+self.u(x)*self.f.phi(x)**2/2
        def tau(self, i, j, x): return super().tau(i,j,x)-(self.u(x)*self.f.phi(x)**2/2 if i == j else 0)
    ward = Profile(fields); x0 = w.ZERO
    check("literal scalar profile energy Ward without hopping", s.expand(ward.energy_residual(x0)) == 0)
    for a in range(3):
        y = w.add(x0,w.E[a])
        force = -(ward.u(y)-ward.u(x0))*fields.phi(x0)*fields.phi(y)/(2*ward.a)
        check(f"axis{a}: retained actual inhomogeneous momentum force", s.expand(ward.momentum_residual(a,x0)-force) == 0 and force != 0)
    bare = w.WardComplex(fields)
    check("actual density zero-point mutation is rejected", bare.rho(x0).subs({v:0 for v in fields.reverse}) == 0)

    eye = s.eye(8)
    basis = s.Matrix.hstack(2*eye[:,0], *[eye[:,0]+eye[:,k] for k in range(1,7)], s.ones(8,1)/2)
    G = basis.T*basis
    units = [tuple(int(a == b) for a in range(8)) for b in range(8)]
    zerocharge = (0,)*8
    def energy(n): return (s.Matrix(n).T*G*s.Matrix(n))[0]/2
    def beta(n,m):
        return int(sum(n[a]*m[a]*G[a,a]/2 for a in range(8))
                   +sum(n[a]*m[b]*G[a,b] for a in range(8) for b in range(a)))%2
    def move(n, x, y, p):
        minus = tuple(-a for a in p)
        phase = (-1)**(beta(p,minus)+beta(minus,n[x])+beta(p,n[y]))
        out = list(n)
        out[x] = tuple(a-b for a,b in zip(n[x],p)); out[y] = tuple(a+b for a,b in zip(n[y],p))
        return tuple(out), phase
    # Gaussian times polynomial, stored without the common Gaussian factor.
    # All these are genuine Schwartz vectors; charge support is NOT wrapped.
    phi = s.symbols("phi0:3", real=True)
    c = s.Rational(2,5); alpha = s.Rational(1,3); nu = s.Rational(1,7)
    state = (units[1],zerocharge,zerocharge)
    psi = {state:1+phi[0]}
    def clean(v):
        return {n:s.expand(f) for n,f in v.items() if s.expand(f) != 0}
    def add(*items):
        out = {}
        for v in items:
            for n,f in v.items(): out[n] = out.get(n,0)+f
        return clean(out)
    def scale(a,v): return clean({n:a*f for n,f in v.items()})
    def diagonal(fn): return lambda v: clean({n:fn(n)*f for n,f in v.items()})
    def U(edge):
        x,y,p = edge
        def action(v):
            out = {}
            for n,f in v.items():
                target, phase = move(n,x,y,p)
                out[target] = out.get(target,0)+phase*f
            return clean(out)
        return action
    def hopping(edge):
        x,y,p = edge; u,ud = U(edge),U((y,x,p))
        return lambda v: add(scale(2,v),scale(-1,u(v)),scale(-1,ud(v)))
    def sumops(ops): return lambda v: add(*(o(v) for o in ops))
    def comm(a,b,v): return add(a(b(v)),scale(-1,b(a(v))))
    edges = [(0,1,units[1]),(1,2,units[2])]
    hopnodes = [hopping(e) for e in edges]; L = sumops(hopnodes)
    enodes = [diagonal(lambda n,i=i:energy(n[i])) for i in range(3)]
    V = diagonal(lambda n:c*sum(energy(n[i])*phi[i]**2 for i in range(3)))
    D = diagonal(lambda n:alpha*sum(energy(q) for q in n)+nu*sum(energy(tuple(a-b for a,b in zip(n[x],n[y]))) for x,y in ((0,1),(1,2))))
    def kinetic(i):
        def op(v):
            return clean({n:-(s.diff(f,phi[i],2)-2*phi[i]*s.diff(f,phi[i])+(phi[i]**2-1)*f)/2 for n,f in v.items()})
        return op
    hm_nodes = [sumops([kinetic(i),diagonal(lambda n,i=i:phi[i]**2)]) for i in range(3)]
    grad_nodes = [diagonal(lambda n,x=x,y=y:(phi[x]-phi[y])**2/2) for x,y in ((0,1),(1,2))]
    Hm = sumops(hm_nodes+grad_nodes)
    H = sumops([Hm,D,V,L])
    check("full Gram includes odd overlapping-bond pairing", G[1,2] == 1 and G.det() == 1)
    n = s.Matrix(s.symbols("n0:8", integer=True)); p = s.Matrix(s.symbols("p0:8", integer=True))
    en = (n.T*G*n)[0]/2; ep = (p.T*G*p)[0]/2
    check("all-charge departure energy finite difference", s.expand(((n-p).T*G*(n-p))[0]/2-en+(n.T*G*p)[0]-ep) == 0)
    check("all-charge doubled gradient increment", s.expand(((n-2*p).T*G*(n-2*p))[0]/2-en+2*(n.T*G*p)[0]-4*ep) == 0)
    # Verify the actual right-coefficient shift identity, not merely a trace.
    for k, edge in enumerate(edges):
        x,y,p = edge; up,um = U(edge),U((y,x,p))
        F = lambda n:alpha*sum(energy(q) for q in n)+c*sum(energy(n[i])*phi[i]**2 for i in range(3))
        dop = diagonal(F)
        delta_p = diagonal(lambda n:F(move(n,x,y,p)[0])-F(n))
        delta_m = diagonal(lambda n:F(move(n,y,x,p)[0])-F(n))
        expected = scale(s.I,add(up(delta_p(psi)),um(delta_m(psi))))
        actual = scale(s.I,comm(hopnodes[k],dop,psi))
        check(f"edge{k}: exact shift ordering in quantum energy exchange", actual == expected)
        wrong = scale(s.I,add(delta_p(up(psi)),delta_m(um(psi))))
        check(f"edge{k}: moving coefficient past shift without correction fails", wrong != actual)
    for i in range(3):
        rho_extra = diagonal(lambda n,i=i:c*energy(n[i])*phi[i]**2)
        source = diagonal(lambda n,i=i:c*phi[i]**2)(scale(s.I,comm(L,enodes[i],psi)))
        check(f"site{i}: exact dynamic scalar-density hopping source", scale(s.I,comm(L,rho_extra,psi)) == source)
    check("nonzero hopping energy source cannot be declared static", bool(comm(L,V,psi)))
    check("continuous scalar Hamiltonian commutes with bare charge hopping", not comm(Hm,L,psi))
    exchange = add(scale(s.I,comm(L,V,psi)),scale(s.I,comm(L,D,psi)),scale(s.I,comm(H,L,psi)))
    check("scalar plus diagonal charge plus hopping energy exchange cancels exactly", not exchange)
    check("omitting scalar hopping transfer breaks total energy accounting", bool(add(scale(s.I,comm(L,D,psi)),scale(s.I,comm(H,L,psi)))))
    check("actual projective neighboring hopping energies do not commute", bool(comm(hopnodes[0],hopnodes[1],psi)))
    u0,u1 = U(edges[0]),U(edges[1])
    check("odd Gram neighboring transfer operators anticommute", not add(u0(u1(psi)),u1(u0(psi))))
    same0,same1 = U((0,1,units[1])),U((0,1,units[2]))
    check("same-edge transfer operators commute after two endpoint signs", not comm(same0,same1,psi))
    # Local positive energy decomposition independent of the previous grouped H.
    nodes = [sumops([hm_nodes[i],diagonal(lambda n,i=i:(alpha+c*phi[i]**2)*energy(n[i]))]) for i in range(3)]
    nodes += [diagonal(lambda n,x=x,y=y:(phi[x]-phi[y])**2/2+nu*energy(tuple(a-b for a,b in zip(n[x],n[y])))) for x,y in ((0,1),(1,2))]
    nodes += hopnodes
    check("local energy-node sum is exactly the coupled Hamiltonian", sumops(nodes)(psi) == H(psi))
    for k,node in enumerate(nodes):
        derivative = scale(s.I,comm(H,node,psi))
        flux = add(*(scale(s.I,comm(node,other,psi)) for other in nodes))
        check(f"energy node{k}: exact local current divergence identity", not add(derivative,flux))
    check("disjoint onsite energy nodes commute", not comm(nodes[0],nodes[2],psi))
    check("all energy-node currents are antisymmetric on the true common core", not add(comm(nodes[0],hopnodes[0],psi),comm(hopnodes[0],nodes[0],psi)))
    print(json.dumps({"status":"PASS","exact_check_groups":len(checks),"checks":checks,
          "ward_sha256":hashlib.sha256(args.ward_source.read_bytes()).hexdigest(),
          "scope":"Actual Ward frontend plus exact differential/projective-shift actions on Schwartz finite-support vectors; not a truncated Hilbert space or a full relativistic stress theorem."},indent=2))


if __name__ == "__main__": main()
