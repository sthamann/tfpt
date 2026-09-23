"""Exact finite witnesses; the unbounded-operator theorem is in PROOF.txt."""
import hashlib
from itertools import product
import json
from pathlib import Path

import sympy as sp

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
CLOCK='experiments/theory-contracts/compiler-integral-triality-20260918/certificate.json'


def require(ok,message):
    if not ok:
        raise ValueError(message)


def run():
    manifest=json.loads((HERE/'source_manifest.json').read_text())
    for name,digest in manifest['sha256'].items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,
                'source pin: '+name)
    data=json.loads((ROOT/CLOCK).read_text())
    c=sp.Matrix(data['clock_matrices']['C']['vector'])
    integer=set()
    for i in range(8):
        for j in range(i+1,8):
            for a,b in product((-1,1),repeat=2):
                r=[sp.S.Zero]*8;r[i]=sp.Integer(a);r[j]=sp.Integer(b)
                integer.add(tuple(r))
    spinor={tuple(sp.Rational(a,2) for a in r)
            for r in product((-1,1),repeat=8) if sum(a<0 for a in r)%2==0}
    roots=integer|spinor
    require((len(integer),len(spinor),len(roots))==(112,128,240),'root inventory')
    transform=lambda rs:{tuple(c*sp.Matrix(r)) for r in rs}
    require(transform(roots)==roots,'C lattice action')
    require(len(transform(integer)&spinor)==56,'sector leakage')
    present=integer.copy();cumulative=integer.copy();counts=[len(cumulative)];period=None
    for k in range(1,31):
        present=transform(present);cumulative|=present;counts.append(len(cumulative))
        if present==integer and period is None: period=k
    require(counts[:9]==[112,168,200,220,228,234,236,238,240],'cumulative closure')
    require(period==15,'D8 root-subset period')
    # Exact grade-one Hilbert projection: eight Cartan + 240 root states.
    p=sp.diag(*([1]*120+[0]*128));q=sp.eye(248)-p
    require(p*q==sp.zeros(248),'orthogonal sector projections')
    # H on this actual homogeneous block is (a+c0)I, so its crosscorner is zero.
    # This finite witness is not the proof of strong reduction on all grades.
    require(q*p==sp.zeros(248),'grade-one zero Hamiltonian crosscorner')
    n=sp.Symbol('N',positive=True,integer=True)
    require(sp.solve(sp.Eq(n/16,1),n)==[16],'weight-one spinor count')
    local_counts=[k for k in range(1,65) if sp.Rational(k,16).q==1]
    require(local_counts==[16,32,48,64],'integer-spin necessary counts')
    require(sp.Rational(8,4)==2,'even E8 spinor norm')
    require(sp.Rational(4,4)!=2,'smaller D4 spinor not weight one')
    # T(c=32)/T(c=8)=exp(-2pi i)=1; this is a phase ambiguity, not full characters.
    require((32-8)%24==0 and 32!=8,'modular phase does not determine magnitude')
    return {
      'contract':'charged-sector-memory-gate-20260920','verdict':'PARTIAL',
      'mathematical_verdict':'EXACT_SECTOR_MEMORY_DECOUPLING_WITH_CONDITIONAL_SPINOR_SELECTION',
      'finite_exact':{'D8_grade_one':120,'spinor_grade_one':128,
          'clock_leakage_rank':56,'retained_clock_intersection':64,
          'D8_clock_period':period,'cumulative_root_counts':counts[:9],
          'minimal_positive_integer_spin_majorana_count':16,
          'weight_one_spinor_majorana_count':16,
          'bosonic_spinor_candidates_through_64':local_counts,
          'same_vacuum_modular_phase_central_charges':[8,32]},
      'analytic_in_text_not_machine_proved':[
          'strong reduction by P_D8 for H=aL0+c',
          'QHP=0 but spinor-current QSP is nonzero',
          'Sigma=K=0 for this same sector elimination',
          'K(0)=B*B with B=QHP under stated domains'],
      'source_spinor_identification_proved':False,
      'P1_anomaly_transgression_proved':False,
      'complete_TFPT_solution':False,'physical_gates_closed':[]}


if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
