"""Exact finite action/response quotient; no empirical consciousness claims."""
from pathlib import Path
from itertools import product
from fractions import Fraction
import hashlib
import json

ROOT = Path(__file__).resolve().parent
S = tuple(product(range(2), repeat=2))  # retained bit b; irrelevant clock bit g
A = ('wait', 'write0', 'write1', 'read', 'guess0', 'guess1')


def transition(s, a):
    b, g = s
    if a == 'write0':
        b = 0
    elif a == 'write1':
        b = 1
    return b, 1-g


def response(s, a):
    b, _ = s
    if a == 'read':
        return str(b), -1
    if a.startswith('guess'):
        return '.', int(b == int(a[-1]))
    return '.', 0


def trace(s, word):
    out = []
    for a in word:
        out.append(response(s, a))
        s = transition(s, a)
    return tuple(out)


def partitions(xs):
    if not xs:
        yield []
        return
    x, *rest = xs
    for blocks in partitions(rest):
        yield [(x,)]+blocks
        for i in range(len(blocks)):
            yield blocks[:i]+[(x,)+blocks[i]]+blocks[i+1:]


def class_map(blocks):
    return {s:i for i, block in enumerate(blocks) for s in block}


def stable_quotient(blocks, alphabet):
    q = class_map(blocks)
    return all(response(s,a) == response(t,a) and
               q[transition(s,a)] == q[transition(t,a)]
               for block in blocks for s in block for t in block for a in alphabet)


def refine(alphabet):
    blocks = [S]
    chain = [blocks]
    while True:
        q = class_map(blocks)
        groups = {}
        for s in S:
            signature = tuple((response(s,a), q[transition(s,a)]) for a in alphabet)
            groups.setdefault(signature, []).append(s)
        new = [tuple(group) for group in groups.values()]
        if all(class_map(new)[s] == class_map(new)[t] for b in blocks for s in b for t in b):
            return new, chain
        blocks = new
        chain.append(blocks)


checks = []
def check(label, truth):
    assert truth, label
    checks.append(label)


all_blocks = list(partitions(list(S)))
check('all fifteen partitions of four states', len(all_blocks) == 15)
words = [w for k in range(len(S)) for w in product(A, repeat=k)]
good = []
for i, blocks in enumerate(all_blocks):
    stable = stable_quotient(blocks, A)
    finite_future = all(trace(s,w) == trace(t,w)
                        for block in blocks for s in block for t in block for w in words)
    # Preservation of all futures does not require a redundant, nonminimal
    # compression to update deterministically. Test the exact factorization
    # condition separately: a recursively usable quotient needs kernel stability.
    if stable:
        check(f'admissible partition {i} preserves every tested future', finite_future)
        good.append(blocks)
    check(f'partition {i} respecting futures never merges different bits',
          not finite_future or all(s[0] == t[0] for block in blocks for s in block for t in block))

minimal, chain = refine(A)
restricted, _ = refine(('wait',))
check('coarsest full action quotient has two states', len(minimal) == 2)
check('coarsest wait-only quotient has one state', len(restricted) == 1)
check('full quotient stable', stable_quotient(minimal, A))
check('exactly two recursively usable partitions here', len(good) == 2)
q = class_map(minimal)
for s in S:
    for a in A:
        representative = minimal[q[s]][0]
        check(f'whole-step closure {s} {a}', response(s,a) == response(representative,a)
              and q[transition(s,a)] == q[transition(representative,a)])

hist0 = ('write0',)+('wait',)*100
hist1 = ('write1',)+('wait',)*100
initial = (0,0)
check('long observation histories identical', trace(initial,hist0) == trace(initial,hist1))
check('one future read separates them', trace(initial,hist0+('read',)) != trace(initial,hist1+('read',)))
check('one future choice separates them', trace(initial,hist0+('guess0',)) != trace(initial,hist1+('guess0',)))

# Whole finite-horizon Bellman recurrence, with known current functional state.
v = {s:0 for s in S}
bellman = []
for h in range(1,9):
    v = {s:max(response(s,a)[1]+v[transition(s,a)] for a in A) for s in S}
    check(f'Bellman values preserved at horizon {h}', all(v[s] == v[t] for b in minimal for s in b for t in b))
    bellman.append({'horizon':h, 'values':{str(s):v[s] for s in S}})

# Exact self-model and feedback of a single bit, both externally set targets.
self_model = []
for b, target in product(range(2), repeat=2):
    model = b
    action = model ^ target
    actual_next = b ^ action
    predicted_next = model ^ action
    check(f'self prediction {b} {target}', actual_next == predicted_next == target)
    self_model.append(dict(bit=b,model=model,target=target,action=action,next=actual_next))

# Observational equivalence does not determine causal response.
obs_A = {(u,u):Fraction(1,2) for u in range(2)}
obs_B = {(u,u):Fraction(1,2) for u in range(2)}
do_A = {0:Fraction(1),1:Fraction(0)}  # X=U,Y=X; intervene X:=0
do_B = {0:Fraction(1,2),1:Fraction(1,2)}  # X=U,Y=U; intervene X:=0
check('two causal models observationally identical', obs_A == obs_B)
check('two causal models interventionally distinct', do_A != do_B)

result = dict(status='ALL_EXACT_CHECKS_PASS',checks=len(checks),check_names=checks,
              states=S,actions=A,minimal_quotient=minimal,refinement_chain=chain,
              admissible_recursive_partitions=good,wait_only_quotient=restricted,
              finite_word_count=len(words),finite_word_max_length=3,
              bellman=bellman,self_model=self_model,
              theorem_scope='Explicit finite deterministic Mealy system; all allowed future actions, rewards included; no claim of consciousness or efficient general planning',
              script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(ROOT/'observer-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','checks','minimal_quotient','wait_only_quotient','finite_word_count','script_sha256']},indent=2))
