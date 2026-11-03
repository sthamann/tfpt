"""Independent closure from actual source D8 and the supplied native sigma.

Loads only the actual source isometry M and the literal SIGMA_IDX assignment.
No E8 roots, E8 basis, discriminant gluing target or v634 module is imported.
This tests conditional lattice closure, not the P1 origin of sigma or M.
"""
import ast
import itertools
import json
from pathlib import Path

import sympy as s
from sympy.matrices.normalforms import hermite_normal_form


def need(condition, message):
    if not condition:
        raise RuntimeError(message)


ROOT = Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
OUT = Path(__file__).resolve().parent
m_path = ROOT / 'experiments/theory-contracts/v16-operator-pullback-20261014/fold-results.json'
sigma_path = ROOT / 'verification/v634_st31_structure.py'
M = s.Matrix([[s.Rational(x) for x in row] for row in
              json.loads(m_path.read_text())['explicit_Weyl_matrix']])
tree = ast.parse(sigma_path.read_text())
idx = next(ast.literal_eval(node.value) for node in tree.body
           if isinstance(node, ast.Assign) and any(
               isinstance(t, ast.Name) and t.id == 'SIGMA_IDX' for t in node.targets))
E = s.eye(8)
sigma = E[idx, :]
R = M.T * sigma * M
need(M.T * M == E, 'actual M is an isometry')
need(sigma.T * sigma == E and sigma**3 == E, 'actual native sigma is order3 isometry')
need(R.T * R == E and R**3 == E, 'transported source R is order3 isometry')

# Source charge lattice only: D8={z in Z8:sum(z) even}.
B = s.Matrix.hstack(*[E[:, j] - E[:, j+1] for j in range(7)], E[:, 6] + E[:, 7])
need(abs(B.det()) == 2, 'source D8 covolume2')
need((B.T * B).det() == 4, 'source D8 Gram determinant4')
need(all(sum(B[:, j]) % 2 == 0 for j in range(8)), 'D8 basis has even coordinate sum')

def doubled_hnf(generators):
    doubled = 2 * generators
    need(all(x.q == 1 for x in doubled), 'doubled generators are integral')
    integer_matrix = s.Matrix([[int(x) for x in row] for row in doubled.tolist()])
    return hermite_normal_form(integer_matrix)


# Full generated lattice from its 16 basis columns, not from target roots.
H = doubled_hnf(B.row_join(R * B))
need(H.shape == (8, 8), 'independent full rank 8x8 HNF')
L = H / 2
gram = L.T * L
need(all(x.q == 1 for x in gram), 'joint lattice is integral')
need(all(gram[j, j] % 2 == 0 for j in range(8)), 'joint lattice is even')
need(gram.det() == 1, 'joint lattice is unimodular')
need(abs(B.det() / L.det()) == 2, 'source lattice index2 in closure')
R_on_L = L.inv() * R * L
need(all(x.q == 1 for x in R_on_L), 'closure is stable under actual R')

# One native-clock image outside old D8. This is the actual admission witness.
old_current = E[:, 0] + E[:, 2]
p = R * old_current
need(p.dot(p) == 2 and all(x.q == 2 for x in p), 'actual clock image is a norm2 half vector')
need(sum(p) % 2 == 0, 'actual half vector belongs to even halfspin class')
need(all(x.q == 1 for x in B.inv() * (2*p)), 'twice the new charge is old D8')
need(not all(x.q == 1 for x in B.inv() * p), 'new charge is outside old D8')
need(doubled_hnf(B.row_join(p)) == H, 'one actual clock image generates entire closure')

# Intrinsic characterization of the observed class. The all-plus half vector
# is introduced only after the HNF output as a representative of p modD8.
half = s.ones(8, 1)/2
need(all(x.q == 1 for x in B.inv() * (p-half)), 'p has the uniform halfspin discriminant class')
need(doubled_hnf(B.row_join(half)) == H, 'closure equals D8 plus its observed halfspin coset')

# Complete source-root alphabet independently enumerated from D8 definition.
counts = {'old_D8': 0, 'observed_halfspin_coset': 0}
witnesses = []
for i, j in itertools.combinations(range(8), 2):
    for a, b in itertools.product((-1, 1), repeat=2):
        root = a*E[:, i] + b*E[:, j]
        image = R * root
        need(image.dot(image) == 2, 'all actual clock images retain norm2')
        if all(x.q == 1 for x in B.inv() * image):
            counts['old_D8'] += 1
        else:
            need(all(x.q == 1 for x in B.inv() * (image-p)),
                 'every new clock image is in the same observed halfspin coset')
            counts['observed_halfspin_coset'] += 1
            witnesses.append(image)
need(sum(counts.values()) == 112, 'complete old D8 root alphabet used')

# The 128 norm2 half vectors follow from the resulting coset description.
half_weights = [s.Matrix([s.Rational(a, 2) for a in signs])
                for signs in itertools.product((-1, 1), repeat=8)
                if sum(a < 0 for a in signs) % 2 == 0]
need(len(half_weights) == 128, '128 weights in the observed halfspin coset')
need(all(all(x.q == 1 for x in L.inv()*v) for v in half_weights),
     'all128 halfspin weights belong to HNF closure')

data = {
    'status': 'PASS_CONDITIONAL_SOURCE_CLOCK_LATTICE_CLOSURE',
    'inputs_only': [str(m_path), str(sigma_path) + ':SIGMA_IDX'],
    'sigma_idx': idx,
    'R': [[str(x) for x in row] for row in R.tolist()],
    'twice_closure_basis_HNF': [[int(x) for x in row] for row in H.tolist()],
    'closure_gram': [[int(x) for x in row] for row in gram.tolist()],
    'closure_gram_determinant': int(gram.det()),
    'closure_even': True,
    'closure_integral': True,
    'source_index_in_closure': 2,
    'actual_R_preserves_closure': True,
    'one_old_current': list(map(str, old_current)),
    'its_actual_clock_image': list(map(str, p)),
    'all112_source_root_image_counts': counts,
    'resulting_halfspin_weights': len(half_weights),
    'no_E8_target_loaded': True,
    'scope': 'Conditional minimal integral charge-lattice closure under supplied actual R. No derivation of R, M, source field action or P1 locality/state/time from original P1.',
}
output = json.dumps(data, indent=2, sort_keys=True)
(OUT / 'clock_closure_hnf_result.json').write_text(output + '\n')
print(output)
