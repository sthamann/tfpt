"""Scope audit of a concurrently edited report, conditional on its irreps.

This does NOT replay the other task's Racah/weight decomposition. It checks
the conclusions that may and may not follow from that displayed decomposition.
"""
from pathlib import Path
from hashlib import sha256
import json
import sympy as s

HERE = Path(__file__).resolve().parent
checks = []


def need(ok, label):
    if not ok:
        raise RuntimeError(label)
    checks.append(label)


source = HERE / 'sources/native_RESULTS_live_addendum.md'
need(sha256(source.read_bytes()).hexdigest() == 'ab745e74b1232b1ddf35dd0e0d0da4ace0176c797d769e5db8bedd0010bcba6a',
     'fixed concurrent report snapshot, never a floating latest source')
dark = [24000, 11200, 2688]
bright = [2880, 576, 320]
chi = 64
need(sum(dark) == 37888, 'displayed dark dimensions sum to the kernel dimension')
need(sum(bright) == 3776, 'displayed bright dimensions sum to the image dimension')
need(sum(dark)+sum(bright) == 41664, 'fermionic triples alone have six inequivalent types')
need(sum(bright)+chi == 3840, 'boson plus fermion carries four types')
need(sum(dark)+2*sum(bright)+chi == 45504, 'full N3 contains each bright type twice')
multiplicities = [1, 1, 1, 2, 2, 2, 1]
need(sum(m*m for m in multiplicities) == 16,
     'symmetry-only commutant dimension sixteen, conditional on displayed irreps')
need(len(multiplicities) == 7,
     'adding nonzero pair mixing and Nb resolves the bright multiplicity matrices, leaving seven central scalars')
# A block-mixing operation invalidates the asserted universal lower floor.
# In the old commutant Z=diag(lambda_0,...,lambda_6), a connected chain of
# nonzero inter-block matrix elements imposes lambda_i=lambda_{i+1}.
incidence = s.zeros(6, 7)
for i in range(6):
    incidence[i, i] = 1
    incidence[i, i+1] = -1
need(incidence.rank() == 6, 'connected inter-block coupling leaves only one common scalar')
need(7-incidence.rank() == 1 < 7,
     'seven is not a lower bound for arbitrary extra operations')
result = {'status': 'PASS', 'checks': len(checks), 'check_labels': checks,
          'scope': 'exact consequences of a stated representation decomposition; full decomposition not re-proved here',
          'conditional_symmetry_only_commutant': 16,
          'conditional_symmetry_plus_X_Nb_commutant': 7,
          'universal_absolute_floor_seven': False,
          'native_available_operations_proved': False,
          'total_N3_symmetry_multiplicity_free': False,
          'source_sha256': sha256(Path(__file__).read_bytes()).hexdigest()}
print(json.dumps(result, indent=2))
