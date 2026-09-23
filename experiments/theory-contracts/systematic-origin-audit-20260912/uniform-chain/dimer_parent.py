"""NON-RH: exact dimer parent, with source-to-candidate obstruction controls."""
import itertools
import json
from collections import defaultdict
import sympy as s
import bond_algebra as src

CHECKS = 0


def require(ok, label):
    global CHECKS
    if not ok:
        raise ValueError(label)
    CHECKS += 1


def add(*terms):
    out = defaultdict(lambda: s.S.Zero)
    for scale, state in terms:
        for key, value in state.items():
            out[key] += scale*value
    return {key:s.simplify(v) for key,v in out.items() if v != 0}


def inner(a, b):
    return s.simplify(sum((s.conjugate(v)*b.get(k,0) for k,v in a.items()),s.S.Zero))


def apply_edges(operator, state, edges):
    columns = [[(divmod(i,4),operator[i,j]) for i in range(16) if operator[i,j] != 0]
               for j in range(16)]
    out = defaultdict(lambda: s.S.Zero)
    for left,right in edges:
        for key,v in state.items():
            for (i,j),coef in columns[4*key[left]+key[right]]:
                target = list(key)
                target[left],target[right] = i,j
                out[tuple(target)] += coef*v
    return {k:s.simplify(v) for k,v in out.items() if v != 0}


def main():
    gs = src.source_generators()
    aa = [s.I*g for g in gs]
    eye = s.eye(4)
    c = gs[0]*gs[1]
    singlet = s.kronecker_product(eye,c)*eye.reshape(16,1)/2
    omega = sum((s.kronecker_product(a,a) for a in aa),s.zeros(16))
    require((singlet.H*singlet)[0] == 1, 'normalized actual-source singlet')
    require(omega*singlet == -4*singlet, 'antiferromagnetic pair ground')
    for a in aa:
        require((s.kronecker_product(a,eye)+s.kronecker_product(eye,a))*singlet == s.zeros(16,1), 'each primitive vector cancels on singlet')
    triangle = s.kronecker_product(omega,eye)+s.kronecker_product(eye,omega)
    triangle += sum((s.kronecker_product(a,eye,a) for a in aa),s.zeros(64))
    eigen = triangle.eigenvals()
    require(eigen == {-4:12,-2:24,0:8,4:12,6:8}, 'complete triangle spectrum')
    positive = triangle+4*s.eye(64)
    require(all(e+4 >= 0 for e in eigen), 'positive local parent')
    require(positive*s.kronecker_product(singlet,eye) == s.zeros(64,4), 'left dimer saturates local bound')
    require(positive*s.kronecker_product(eye,singlet) == s.zeros(64,4), 'right dimer saturates local bound')
    # Six-site periodic exact state probe; no full 4096x4096 matrix allocated.
    local = [(divmod(i,4),singlet[i]) for i in range(16) if singlet[i] != 0]
    state = {}
    for terms in itertools.product(local,repeat=3):
        key = tuple(i for pair,_ in terms for i in pair)
        state[key] = s.prod(v for _,v in terms)
    shifted = {key[-1:]+key[:-1]:v for key,v in state.items()}
    require(inner(state,state) == inner(shifted,shifted) == 1, 'two normalized coverings')
    require(abs(inner(state,shifted)) < 1, 'two independent dimer coverings')
    edges = [(j,(j+1)%6) for j in range(6)]
    next_edges = [(j,(j+2)%6) for j in range(6)]
    pair = 2*s.eye(16)+omega/2
    ten = 5*pair-pair**2
    nearest = apply_edges(omega,state,edges)
    next_ = apply_edges(omega,state,next_edges)
    ten_response = apply_edges(ten,state,edges)
    parent_response = add((s.Rational(1,2),nearest),(s.Rational(1,4),next_),(6,state))
    require(not parent_response, 'six-site J=1/2,Jprime=1/4 ground energy -6 before constant')
    require(not add((s.Rational(1,2),apply_edges(omega,shifted,edges)),
                    (s.Rational(1,4),apply_edges(omega,shifted,next_edges)),(6,shifted)), 'translated covering also exact ground')
    responses = [nearest,next_,ten_response]
    means = [inner(state,x) for x in responses]
    residuals = [add((1,x),(-mean,state)) for x,mean in zip(responses,means)]
    gram = s.Matrix([[inner(a,b) for b in residuals] for a in residuals])
    require(gram[0,0] > 0, 'uniform nearest-neighbor dimer product is not an eigenstate')
    require(gram*s.Matrix([s.Rational(1,2),s.Rational(1,4),0]) == s.zeros(3,1), 'known exact dimer ratio annihilates leakage')
    require(gram.rank() == 2, 'two independent leakage directions for three-term family')
    kernel = gram.nullspace()
    require(len(kernel)==1 and kernel[0][2]==0, 'nonzero ten-word coupling cannot be repaired by changing only vector ratio')
    print(json.dumps({'scope':'NON-RH exact dimer comparison parent; not original-source energy selection',
        'checks':CHECKS+src.CHECKS,'source_pin':src.PIN,
        'triangle_spectrum':{str(k):v for k,v in eigen.items()},
        'six_site_response_means':[str(v) for v in means],
        'six_site_leakage_Gram':str(gram),'leakage_kernel':[str(v) for v in kernel],
        'all_even_periodic_lengths_ground_construction':'H=J sum Omega_nn+(J/2)sum Omega_nnn; E0=-2JL; L>=6',
        'exact_ground_space_completeness_proved_here':False,
        'uniform_nearest_neighbor_ground_solved':False,
        'generated_H10_family_is_exact_dimer_parent':False,'T1_T8_closed':[]},sort_keys=True))


if __name__ == '__main__':
    main()
