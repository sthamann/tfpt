#!/usr/bin/env python3
"""Finite exact controls and numerical receipt; does not formalize PROOF.md."""
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
checks = {}


def require(name, condition):
    checks[name] = bool(condition)
    if not condition:
        raise RuntimeError(name)


def load_drive():
    spec = importlib.util.spec_from_file_location("flux_drive_checked", HERE / "flux_drive.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def exact_blocks(mod):
    def exact(a):
        return sp.Matrix(a).applyfunc(lambda z: sp.nsimplify(z, rational=True))
    sz, tx, ty = map(exact, (mod.SZ, mod.TX, mod.TY))
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    require("primitive_source_values", tx == sx/(2*sp.I)-sz/2 and ty == sy/(2*sp.I)-sz/2)
    rho, s = sp.symbols("rho s", real=True)
    hh = sp.zeros(16)
    hop = (1-rho-sp.I*s)*tx + (1-rho+sp.I*s)*tx.conjugate().T
    B = sp.zeros(16)
    for y in range(8):
        for a in range(2):
            for b in range(2):
                hh[2*y+a,2*y+b] = sz[a,b]+hop[a,b]
                if y<7:
                    hh[2*(y+1)+a,2*y+b] = ty[a,b]
                    hh[2*y+b,2*(y+1)+a] = sp.conjugate(ty[a,b])
        B[2*y,y] = B[2*y+1,y] = 1/sp.sqrt(2)
        B[2*y,8+y] = 1/sp.sqrt(2)
        B[2*y+1,8+y] = -1/sp.sqrt(2)
    D = rho*sp.eye(8)
    for y in range(7):
        D[y,y+1] = -1
    target = (-s*sp.eye(8)).row_join(D).col_join(D.T.row_join(s*sp.eye(8)))
    require("exact_primitive_to_edge_block", (B.T*hh*B-target).applyfunc(sp.simplify)==sp.zeros(16))
    require("exact_signed_small_singular_order", D.det()==rho**8)
    require("exact_zero_spectrum", target.subs({s:0,rho:0}).eigenvals()=={-1:7,0:2,1:7})
    qtop = sp.Matrix([rho**(7-y) for y in range(8)])
    qbot = sp.Matrix([rho**y for y in range(8)])
    require("exact_top_residual", D.T*qtop == sp.Matrix([rho**8]+[0]*7))
    require("exact_bottom_residual", D*qbot == sp.Matrix([0]*7+[rho**8]))
    require("exact_kernel_slopes", target.diff(s)[7,7]==-1 and target.diff(s)[8,8]==1)
    for p in (-0.2, 0.0, 0.12, 1.4, 3.0):
        numerical = np.array((B*target*B.T).subs({rho:1-np.cos(p),s:np.sin(p)}),dtype=complex)
        require(f"source_numeric_block_{p}", np.linalg.norm(numerical-mod.hamiltonian(p))<1e-13)


def fock_energy_guard():
    # Four orbitals: a non-ground tracked determinant and a rotated Slater.
    Cdag=[]
    for a in range(4):
        op=np.zeros((16,16),complex)
        for mask in range(16):
            if not (mask>>a)&1:
                op[mask|(1<<a),mask]=(-1)**((mask&((1<<a)-1)).bit_count())
        Cdag.append(op)
    def dg(a):
        return sum(a[i,j]*Cdag[i]@Cdag[j].conj().T for i in range(4) for j in range(4))
    U=np.eye(4)
    for a,b,t in ((0,1,.23),(2,3,.31),(0,3,.17)):
        g=np.eye(4); g[a,a]=g[b,b]=np.cos(t);g[a,b]=-np.sin(t);g[b,a]=np.sin(t)
        U=g@U
    W=U[:,[0,2]]; P=np.diag([1,0,1,0]); G=W@W.T
    psi=np.zeros(16,complex);psi[0]=1
    for col in (1,0):
        psi=sum(W[a,col]*Cdag[a] for a in range(4))@psi
    K=np.diag([-3.,-1.,1.,2.]); H=dg(K)
    mean=np.vdot(psi,H@psi).real
    var=np.vdot(H@psi,H@psi).real-mean**2
    hs=np.linalg.norm(G-P,"fro")
    require("slater_variance_full_fock", abs(var-.5*np.linalg.norm(K@G-G@K,"fro")**2)<1e-13)
    require("energy_mean_quadratic_leakage", abs(mean-np.trace(K@P))<=np.linalg.norm(K,2)*hs**2+1e-13)
    require("energy_variance_hs_bound", var<=2*np.linalg.norm(K,2)**2*hs**2+1e-13)
    A=U@np.diag([.1,.3,.7,.9])@U.T
    variance=lambda c: np.trace(c@A@A-c@A@c@A).real
    require("charge_variance_trace_lipschitz", abs(variance(G)-variance(P))<=3*np.linalg.norm(G-P,ord="nuc")+1e-13)


def main():
    manifest=json.loads((HERE/"source_manifest.json").read_text())
    for item in manifest["files"]:
        actual=hashlib.sha256((REPO/item["path"]).read_bytes()).hexdigest()
        require("pin:"+item["path"],actual==item["sha256"])
    mod=load_drive()
    exact_blocks(mod)
    fock_energy_guard()
    data=json.loads((HERE/"flux_drive_results.json").read_text())
    require("seven_source_evolutions",len(data["results"])==7)
    sha=hashlib.sha256(mod.SOURCE.read_bytes()).hexdigest()
    for r in data["results"]:
        tag=f'{r["N"]}:{r["T"]}:{r["dt"]}:{r["profile"]}'
        require("run_source:"+tag,r["primitive_source_sha256"]==sha)
        require("unitarity:"+tag,r["max_unitarity_error"]<1e-10)
        require("particle_number:"+tag,r["max_number_error"]<1e-10)
        require("half_filtered_charge:"+tag,abs(r["half_filtered_regional_charge"]-.5)<2e-5)
        require("whole_filtered_charge:"+tag,abs(r["filtered_regional_charge"]-1)<1e-5)
        require("inverse_control:"+tag,r["inverse_first_half_initial_projector_defect"]<1e-10)
        require("no_sea_reset:"+tag,abs(r["covariance_distance_to_final_sea"]-np.sqrt(2))<1e-3)
        require("actual_half_target:"+tag,0<=r["half_actual_vs_instantaneous_sea_trace_norm"]<1)
    smooth=[r for r in data["results"] if r["profile"]=="sinusoidal"]
    require("smooth_refinement_pair",len(smooth)==2)
    require("smooth_dt_charge_control",abs(smooth[0]["filtered_regional_charge"]-smooth[1]["filtered_regional_charge"])<1e-9)
    require("smooth_full_covariance_control",max(r["global_target_trace_norm_defect"] for r in smooth)<.0005)
    require("smooth_filtered_variance",max(r["sum_covariance_variance"] for r in smooth)<2e-10)
    result={"status":"PASS_FINITE_CONTROLS","research_verdict":"PARTIAL","checks":checks,
            "count":len(checks),"general_proof":"PROOF.md (written argument, not formalized)",
            "time_integration":"midpoint matrix exponentials, numerical not interval certified",
            "complete_TFPT_solution":False,"physical_gates_closed":[]}
    out=HERE/("certificate.optimized.json" if sys.flags.optimize else "certificate.json")
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"status":result["status"],"count":len(checks),"output":str(out)}))


if __name__=="__main__":
    main()
