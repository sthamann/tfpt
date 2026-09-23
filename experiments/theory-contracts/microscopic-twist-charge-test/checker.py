"""Measure the original Gaussian microscopic twist with source-derived charges.

Finite full-sea diagnostics, not a renormalized smeared field proof.
The exact Slater Ward formula separates mean charge from fluctuations.
"""
from functools import lru_cache
import hashlib
import importlib.util
from pathlib import Path

import numpy as np

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PINS={
    "experiments/theory-contracts/source-edge-charge-transport/checker.py":
        "13705df410412ec843171e2c7dd0434da84ce8d17500aff9248274fbeee0f5c6",
    "experiments/theory-contracts/gaussian-vacuum-filter/checker.py":
        "4a319e059d25be9f0aace0fbc994c0a1201ac8846a6910962c9379d48248e9fa",
}


def require(ok,message):
    if not ok: raise ValueError(message)


def validate_pins(root=ROOT):
    for relative,digest in PINS.items():
        require(hashlib.sha256((Path(root)/relative).read_bytes()).hexdigest()==digest,
                "source pin: "+relative)


@lru_cache(maxsize=1)
def source():
    validate_pins()
    modules=[]
    for index,relative in enumerate(PINS):
        spec=importlib.util.spec_from_file_location("measured_twist_source_"+str(index),ROOT/relative)
        module=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        modules.append(module)
    modules[0].source()
    modules[1].inherited()
    return tuple(modules)


def ward_from_one_body(source_eigenvectors,occupied,unitary,a_source,a_destination,charge):
    """Exact norm on the full filled sea of (Cdest V - V Csource - charge V)."""
    basis=source_eigenvectors
    transported=unitary@basis
    b=transported.conj().T@a_destination@transported-basis.conj().T@a_source@basis
    mean=float(np.trace(b[np.ix_(occupied,occupied)]).real)
    variance=float(np.linalg.norm(b[np.ix_(~occupied,occupied)],"fro")**2)
    return dict(charge_mean=mean,ward_variance=variance,
                desired_charge=float(charge),ward_residual_squared=(mean-charge)**2+variance)


def charge_of_slater(columns,a,reference):
    ac=a@columns
    compressed=columns.conj().T@ac
    # Compute the perpendicular component, not a subtraction of nearly equal traces.
    leakage=ac-columns@compressed
    return dict(mean=float(np.trace(compressed).real-reference),
                variance=float(np.linalg.norm(leakage,"fro")**2))


@lru_cache(maxsize=16)
def case(n):
    require(type(n) is int and n>=16,"source circumference N >= 16")
    charge,gaussian=source()
    d=gaussian.source_case(n)
    t=np.kron(np.eye(n),charge.region())
    a1=charge.eigendata(d["h"],t,d["delta"])["filtered"]
    destination=charge.eigendata(d["hn"],t,d["delta"])
    a3=destination["filtered"]
    p1=d["e"]<0
    p3=destination["values"]<0
    reference=float(np.trace(d["v"][:,p1].conj().T@t@d["v"][:,p1]).real)
    # Exactly the original compensated microscopic candidate, not a new transporter.
    u=d["gauge"][:,None]*(d["v"]@d["ui"]@d["v"].conj().T)
    return dict(n=n,data=d,t=t,a1=a1,a3=a3,p1=p1,p3=p3,reference=reference,u=u,destination=destination)


def diagnostic(n):
    q=case(n)
    d=q["data"]
    columns=q["u"]@d["v"][:,q["p1"]]
    out=charge_of_slater(columns,q["a3"],q["reference"])
    row=dict(N=n,dimension=16*n,occupied_rank=int(q["p1"].sum()),filter_width=d["delta"],
             target_charge=out,
             forward=ward_from_one_body(d["v"],q["p1"],q["u"],q["a1"],q["a3"],.5),
             adjoint=ward_from_one_body(q["destination"]["vectors"],q["p3"],q["u"].conj().T,
                                        q["a3"],q["a1"],-.5),
             rescaled_output_energy=gaussian_energy(q,columns),
             unitary_defect=float(np.linalg.norm(q["u"].conj().T@q["u"]-np.eye(16*n),"fro")),
             microscopic_field_norm_on_vacuum=1.,
             point_operator_not_spacetime_smeared=True,
             full_sea_retained=True,analytic_scaling_limit_proved=False)
    return row


def controls(n):
    q=case(n)
    d=q["data"]
    result={}
    for name,u in (("identity",np.eye(16*n)),("raw_top_string",np.diag(d["raw"])),
                   ("gauge_ramp_only",np.diag(d["gauge"]))):
        columns=u@d["v"][:,q["p1"]]
        result[name]=dict(ward=ward_from_one_body(d["v"],q["p1"],u,q["a1"],q["a3"],.5),
                          target_charge=charge_of_slater(columns,q["a3"],q["reference"]),
                          rescaled_energy=gaussian_energy(q,columns))
    return dict(N=n,controls=result)


def two_forward(n):
    q=case(n)
    _,gaussian=source()
    second=gaussian.source_case(n,sector=3)
    u3=second["gauge"][:,None]*(second["v"]@second["ui"]@second["v"].conj().T)
    twice=u3@q["u"]
    ramp_twice=np.diag(q["data"]["gauge"]**2)
    result={}
    for name,u in (("original_twist_twice",twice),("pure_ramp_twice",ramp_twice)):
        result[name]=ward_from_one_body(q["data"]["v"],q["p1"],u,q["a1"],q["a1"],1.)
    return dict(N=n,forward_twice=result,second_forward_is_not_adjoint=True)


def gaussian_energy(q,columns):
    occupied=q["destination"]["values"]<0
    energy=np.trace(columns.conj().T@q["data"]["hn"]@columns).real
    return float(q["n"]/(2*np.pi)*(energy-sum(q["destination"]["values"][occupied])))
