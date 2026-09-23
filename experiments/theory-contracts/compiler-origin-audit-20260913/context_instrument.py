"""NON-RH: original 15 contexts / 60 Gaussian rays, conditional instruments.

Replays only v783 P0/P1 (not its full group/negative-control audit), with
asserts transformed into always-on guards IN MEMORY. Original file untouched.
Quantum Born measurement, repeatability and execution of K are added premises.
No physical instrument, clock, seam field, or TOE closure is claimed.
"""
import ast
from collections import Counter
import contextlib
import hashlib
import io
import itertools
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'verification/v783_two_qubit_clifford.py'
PIN = '8f4851634b83f61671b04f3a6211059c40758d21caaf1f779302c799e1e9d6c4'
CHECKS = 0


def require(ok, label):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise ValueError(label)


def source_prefix():
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == PIN, 'original v783 source pin')
    tree = ast.parse(SOURCE.read_text())
    main = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'main')
    stop = next(i for i, n in enumerate(main.body)
                if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call)
                and isinstance(n.value.func, ast.Name) and n.value.func.id == 'section'
                and isinstance(n.value.args[0], ast.Constant)
                and n.value.args[0].value.startswith('P2 (H2a)'))
    main.body = main.body[:stop] + [ast.Return(value=ast.Call(func=ast.Name(id='locals', ctx=ast.Load()), args=[], keywords=[]))]

    class AlwaysOn(ast.NodeTransformer):
        def visit_Assert(self, node):
            return ast.copy_location(ast.Expr(value=ast.Call(
                func=ast.Name(id='require', ctx=ast.Load()),
                args=[node.test, ast.Constant(value='inherited source assert at line '+str(node.lineno))],
                keywords=[])), node)

    reduced = ast.fix_missing_locations(AlwaysOn().visit(ast.Module(body=[main], type_ignores=[])))
    env = {'require': require}
    exec(compile(reduced, str(SOURCE), 'exec'), env)
    with contextlib.redirect_stdout(io.StringIO()):
        data = env['main']()
    for name, ok in data['CHECKS']:
        require(ok, 'replayed ' + name)
    return data


def cmatrix(raw):
    return s.Matrix([[s.Rational(a)+s.I*s.Rational(b) for a,b in row] for row in raw])


def main():
    d = source_prefix()
    eye = s.eye(4)
    zero = (0,0,0,0)
    paulis = {v: cmatrix(p) for v,p in d['PMAT'].items()}
    contexts = d['contexts']
    # Each projector comes from an ACTUAL Gaussian E8 root, not guessed eigenvectors.
    by_label = {}
    for k in d['line_reps']:
        label = d['root_label'][d['ROOTS'][k]]
        z = s.Matrix([a+s.I*b for a,b in d['Z240'][k]])
        # Normalize Gaussian-polynomial expressions before structural equality.
        # Regression witness: z=(-1-i,-1-i,0,0) has exact norm four.
        projector = (z*z.H/4).applyfunc(s.expand)
        require(projector.H == projector and projector**2 == projector
                and s.trace(projector) == 1, 'source root gives rank-one projector')
        ray = d['canonical_ray'](d['Z240'][k])
        ci = d['stab_ray_ctx'][ray]
        by_label.setdefault(label, []).append((ci, projector))
    labels = sorted(by_label)
    require(len(labels) == 15, 'fifteen nonzero source classes')
    class_context = {}
    bases = []
    for label in labels:
        block = by_label[label]
        require(len(block) == 4 and len({ci for ci,p in block}) == 1, 'source label is one whole measurement context')
        class_context[label] = block[0][0]
        basis = [p for ci,p in block]
        require(sum(basis,s.zeros(4)) == eye, 'source context is complete sharp measurement')
        require(all(p*q == s.zeros(4) for p,q in itertools.combinations(basis,2)), 'source outcomes orthogonal')
        bases.append(basis)
    require(len(set(class_context.values())) == 15, 'source classes to contexts bijective')

    def hbar(x,y):
        value = d['hermC'](d['chart'](x),d['chart'](y))
        require(all(z % 2 == 0 for z in value), 'source Hermitian pairing integral after division by two')
        return ((value[0]//2)+(value[1]//2)) % 2

    b = s.Matrix([[int(hbar(d['REPS'][x],d['REPS'][y]) == 0) for y in labels] for x in labels])
    ctx = [contexts[class_context[label]] for label in labels]
    require(b*b == 4*s.eye(15)+3*s.ones(15), 'actual source incidence identity')
    for i in range(15):
        require(sum(b[i,j] for j in range(15)) == 7, 'source context has seven allowed successors')
        for j in range(15):
            require(bool(b[i,j]) == bool(ctx[i]&ctx[j]), 'actual context dictionary, not individual Pauli labels')

    # Rank-one projective measurement: repeatability + prescribed Born effects
    # uniquely gives I_(D,t)(rho)=Pi_(D,t) rho Pi_(D,t).
    # Gram entries are conditional Born probabilities between original rays.
    rays = [p for basis in bases for p in basis]
    gram = s.Matrix([[s.trace(p*q) for q in rays] for p in rays])
    require(set(gram) == {s.Integer(0), s.Rational(1,4), s.Rational(1,2), s.Integer(1)}, 'exact source overlaps')
    transition = s.Matrix(60,60,lambda i,j:b[i//4,j//4]*gram[i,j]/7)
    require(transition == transition.T, 'conditional sixty-state transition symmetric')
    require(all(sum(transition[:,j]) == 1 for j in range(60)), 'conditional transition stochastic')
    require(set(transition) == {s.Integer(0),s.Rational(1,14),s.Rational(1,7)}, 'exact transition probabilities')
    for j in range(60):
        require(Counter(transition[:,j]) == Counter({s.Integer(0):47,s.Rational(1,14):12,s.Rational(1,7):1}),
                'one same-ray and twelve half-overlap successors')
    reached, frontier = {0}, [0]
    while frontier:
        j = frontier.pop()
        for i in range(60):
            if transition[i,j] > 0 and i not in reached:
                reached.add(i)
                frontier.append(i)
    require(len(reached) == 60 and all(transition[i,i] > 0 for i in range(60)),
            'finite irreducible aperiodic process: uniform ray stationary law unique')
    coarse = s.Matrix(15,60,lambda i,j:int(j//4 == i))
    require(coarse*transition == (b/7)*coarse, 'all label distributions intertwine EXACTLY with original K')
    decode = s.Matrix.hstack(*(p.reshape(16,1) for p in rays))
    require(decode.rank() == 16, 'actual source projectors span full operator space')
    identity_vec = eye.reshape(16,1)
    depol = 3*s.eye(16)/7 + identity_vec*identity_vec.T/7
    require(decode*transition == depol*decode,
            'quantum shadow closes EXACTLY: rho -> (3/7)rho+(4/7)I/4')
    for ci in range(15):
        for v,p in paulis.items():
            after = sum((q*p*q for q in bases[ci]),s.zeros(4))
            require(after == (p if v == zero or v in ctx[ci] else s.zeros(4)),
                    'context measurement preserves exactly its commuting Pauli algebra')
    # Stronger source bridge: the four actual rank-one root reflections already
    # realize the nonselective context measurement as their uniform channel.
    record_rotation = s.ones(4)/2-eye
    require(record_rotation**2 == eye and record_rotation.H == record_rotation,
            'four-outcome record rotation unitary and involutive')
    uniform_ray = s.ones(4)/4
    require(any(p == uniform_ray for p in rays), 'uniform record ray is already an actual source ray')
    require(record_rotation == -(eye-2*uniform_ray), 'record rotation is minus an existing root reflection')
    for basis in bases:
        reflections = [eye-2*q for q in basis]
        require(all(r.H*r == eye for r in reflections), 'actual source reflection unitaries')
        kraus_random = [r/2 for r in reflections]
        require(sum((a.H*a for a in kraus_random),s.zeros(4)) == eye,
                'controlled-reflection isometry normalized')
        for j in range(4):
            mixed = sum((record_rotation[j,k]*kraus_random[k] for k in range(4)),s.zeros(4))
            require(mixed == basis[j], 'source record rotation turns reflection Kraus operators into projectors')
        for p in paulis.values():
            random_out = sum((r*p*r.H for r in reflections),s.zeros(4))/4
            measured_out = sum((q*p*q for q in basis),s.zeros(4))
            require(random_out == measured_out, 'original reflection mixture equals context dephasing on all operators')
    require(all(a.H*a == eye/4 for a in kraus_random),
            'unrotated record outcomes uniform independent of state: not Born outcome labels')
    # Count origin of 3/7: three of seven successor contexts keep any current Pauli.
    for ci in range(15):
        for v in ctx[ci]:
            require(sum(b[di,ci] for di in range(15) if v in ctx[di]) == 3,
                    'three of seven context choices preserve each current component')

    # Minimal trace normalization and Born effects alone do NOT choose a state update.
    # Outcome-conditioned reset to I/4 has the same effects but is not repeatable.
    p = rays[0]
    require(s.trace(p*p) == 1 and s.trace(p*eye/4) == s.Rational(1,4),
            'negative control: same Born effect, repeated-outcome probability one vs quarter')
    # K alone cannot even be a universal Born OUTCOME distribution over contexts:
    # completeness forces the probability of an independently chosen context to
    # be controlled by the setting policy, not by its subsequent outcome.
    povm = [p/15 for p in rays]
    require(sum(povm,s.zeros(4)) == eye, 'uniform context choice gives 60-outcome POVM')
    require(all(sum(povm[4*i:4*i+4],s.zeros(4)) == eye/15 for i in range(15)),
            'forgetting all four outcomes loses all state information')
    # Schedules still need original-policy execution. Another simple policy gives
    # a distinct quantum shadow while using exactly the same bases and rule.
    uniform_t = gram/15
    depol_uniform = s.eye(16)/5 + identity_vec*identity_vec.T/5
    require(decode*uniform_t == depol_uniform*decode,
            'negative control: same ideal measurements, other context policy gives factor one fifth')
    require(depol != depol_uniform, 'measurement rule does not select context scheduling')
    print(json.dumps({'scope':'NON-RH conditional exact instrument on actual source contexts and rays',
        'checks':CHECKS,'source_sha256':PIN,'replayed_source_sections':['P0','P1'],
        'source_classes':15,'source_rays':60,'rank_one_instrument_unique_given_Born_and_repeatability':True,
        'context_shadow':'K=B/7','quantum_shadow':'rho -> (3/7)rho+(4/7)I4/4',
        'quantum_operator_span':16,'nonzero_successors_per_ray':13,
        'conditional_ray_chain_unique_stationary_law':'uniform on sixty original rays',
        'same_ray_probability':'1/7','other_allowed_ray_probability':'1/14',
        'uniform_context_policy_quantum_contraction':'1/5',
        'context_dephasing_is_uniform_source_reflection_channel':True,
        'record_rotation_is_existing_source_reflection_up_to_sign':True,
        'coherent_control_and_record_basis_physically_derived':False,
        'repeatability_counterexample_probabilities':['1','1/4'],
        'setting_only_record_contains_state_information':False,
        'physical_Born_instrument_derived':False,'physical_context_policy_derived':False,
        'physical_clock_derived':False,'T1_T8_closed':[]},sort_keys=True))


if __name__ == '__main__':
    main()
