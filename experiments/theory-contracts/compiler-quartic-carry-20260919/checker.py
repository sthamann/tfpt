from pathlib import Path
# Reconstruct projective compiler multiplication from symplectic transport,
# the defect of a quadratic refinement, and permutation parity.
exec((Path(__file__).with_name('core.py')).read_text())
from collections import deque
basis=(1,2,4,8)
def q(v):return (((v&3)&(v>>2)).bit_count())%2
def b(v,w):return (((v&3)&(w>>2)).bit_count()+((w&3)&(v>>2)).bit_count())%2
W=[]
for v in range(16):
    W.append(np.kron(np.linalg.matrix_power(X,v&1)@np.linalg.matrix_power(Z,(v>>2)&1),np.linalg.matrix_power(X,(v>>1)&1)@np.linalg.matrix_power(Z,(v>>3)&1)))
wkeys={canon(w):v for v,w in enumerate(W)}
for v,w in it.product(range(16),repeat=2):
    require(np.array_equal(W[v]@W[w],((-1)**(((v>>2)&(w&3)).bit_count()%2))*W[v^w]),'native Heisenberg multiplication')
Rs=[refl[i] for i in chain]
Sp=[]
for r in Rs:
    perm=tuple(wkeys[canon(r@w@r.conj().T)] for w in W)
    require(all(perm[v^w]==perm[v]^perm[w] and b(perm[v],perm[w])==b(v,w) for v,w in it.product(range(16),repeat=2)),'actual symplectic Pauli action')
    Sp.append(perm)
idperm=tuple(range(16)); sperms=[idperm]; sindex={idperm:0}; parities=[0]; queue=deque([0]); transitions=[]
while queue:
    k=queue.popleft();row=[]
    for sj in Sp:
        prod=tuple(sperms[k][sj[v]] for v in range(16))
        if prod not in sindex:
            sindex[prod]=len(sperms);sperms.append(prod);parities.append(parities[k]^1);queue.append(sindex[prod])
        m=sindex[prod];require(parities[m]==parities[k]^1,'parity descends to quotient');row.append(m)
    transitions.append(row)
require(len(sperms)==720,'five quotient generators generate full S6')
d=[]
for perm in sperms:
    possible=[a for a in range(16) if all(b(perm[v],a)==q(v)^q(perm[v]) for v in range(16))]
    require(len(possible)==1,'unique quadratic-defect vector');d.append(possible[0])
# All 720^2 pairs: derivation law d(st)=d(s)+s d(t).
for i,ps in enumerate(sperms):
    for j,pt in enumerate(sperms):
        st=sindex[tuple(ps[pt[v]] for v in range(16))]
        require(d[st]==d[i]^ps[d[j]],'quadratic defect derivation law')
print('DERIVATION verified all 518400 pairs',flush=True)
# Symbolic candidate isomorphism, 20 binary unknowns = the 4 correction bits
# of each of five actual generators. BFS over all physical projective operations.
pivots={}; constraints=0
def equation(mask,rhs):
    global constraints
    constraints+=1
    while mask:
        pivot=mask.bit_length()-1
        if pivot not in pivots:pivots[pivot]=(mask,rhs);return
        old,bit=pivots[pivot];mask^=old;rhs^=bit
    require(rhs==0,'consistent explicit extension isomorphism')
gm=[np.eye(4,dtype=complex)];gindex={canon(2*gm[0]):0}; gsi=[0]; lin=[(0,0,0,0)]; const=[0]; queue=deque([0]); edges=[]
while queue:
    k=queue.popleft();row=[];ps=sperms[gsi[k]]
    for j,r in enumerate(Rs):
        mat=gm[k]@r;key=canon(2*mat);sn=transitions[gsi[k]][j]
        newlin=list(lin[k])
        for bit in range(4):
            for var in range(4):
                if ps[basis[var]]&basis[bit]:newlin[bit]^=1<<(4*j+var)
        newconst=const[k]^d[gsi[k]]
        if key not in gindex:
            m=len(gm);gindex[key]=m;gm.append(mat);gsi.append(sn);lin.append(tuple(newlin));const.append(newconst);queue.append(m)
        else:
            m=gindex[key];require(gsi[m]==sn,'projective group quotient is consistent')
            for bit in range(4):equation(lin[m][bit]^newlin[bit],((const[m]^newconst)>>bit)&1)
        row.append(m)
    edges.append(row)
    require(len(gm)<=11520,'finite source group size bound')
require(len(gm)==11520,'actual generators reconstruct all projective source operations')
for v in range(16):
    k=gindex[canon(2*W[v])];require(gsi[k]==0,'Pauli belongs to quotient kernel')
    for bit in range(4):equation(lin[k][bit],((v^const[k])>>bit)&1)
solution=0
for pivot,(mask,rhs) in sorted(pivots.items()):
    value=rhs^((mask&solution).bit_count()%2)
    if value:solution|=1<<pivot
aval=[const[k]^sum((((mask&solution).bit_count()%2)<<bit) for bit,mask in enumerate(lin[k])) for k in range(len(gm))]
require(len(set(zip(gsi,aval)))==11520,'bijective carry encoding of every source operation')
for k,row in enumerate(edges):
    for j,m in enumerate(row):
        target=aval[k]^sperms[gsi[k]][(solution>>(4*j))&15]^d[gsi[k]]
        require(aval[m]==target,'carry multiplication reproduces each Cayley edge')
# Simple native closed visible loop with nontrivial carry.
loops=[]
for i,j in it.combinations(range(5),2):
    m=3 if j==i+1 else 2
    mat=np.linalg.matrix_power(Rs[i]@Rs[j],m)
    wk=canon(mat)
    require(wk in wkeys,'Coxeter relation closes into actual Pauli kernel')
    if wkeys[wk]!=0:
        v=wkeys[wk];psi=next(z/2 for z in zlist if abs(np.vdot(z/2,mat@(z/2)))==0)
        loops.append({'generator_pair':[i,j],'repetition':m,'Pauli_bits':v,'word_length':2*m,'matrix':[[str(v) for v in row] for row in mat],'input_state':[str(v) for v in psi],'return_probability':0})
print('CARRY',{'group':len(gm),'GF2_rank':len(pivots),'solution_count':2**(20-len(pivots)),'loops':len(loops)},flush=True)
# Restore central mu4 phases on every generator edge, then enumerate the full lift.
phase_values=(1,1j,-1,-1j); phase_edges=[]
for k,row in enumerate(edges):
    pr=[]
    for j,m in enumerate(row):
        pmat=gm[k]@Rs[j]@gm[m].conj().T
        require(scalar(pmat),'central phase recovered exactly')
        pr.append(phase_values.index(pmat[0,0]))
    phase_edges.append(pr)
full_seen={(0,0)};fq=deque([(0,0)])
while fq:
    phase,k=fq.popleft()
    for j,m in enumerate(edges[k]):
        target=((phase+phase_edges[k][j])%4,m)
        if target not in full_seen:full_seen.add(target);fq.append(target)
require(len(full_seen)==46080,'full mu4 phase lift reconstructed')
# Invisible continuous kernel events: all diagonal Pauli jumps fix populations,
# act as identity on the quartic quotient; their average commutes with coordinate permutations.
diagonal=[W[v] for v in (0,4,8,12)]
for p in diagonal:require(np.array_equal(kron(p,4)@V,V),'diagonal Pauli jump invisible in quartic quotient')
for i,j in it.product(range(4),repeat=2):
    e=np.zeros((4,4));e[i,j]=1
    pinched=sum(p@e@p.conj().T for p in diagonal)/4
    require(np.array_equal(pinched,e if i==j else np.zeros((4,4))),'kernel average equals diagonal pinching')
anchor=[r for r in refl if np.count_nonzero(r[:,3])==1 and r[3,3]!=0]
require(len(anchor)==16,'exactly 16 native reflections preserve the anchor')
require(all(all(np.count_nonzero(row)==1 for row in r) for r in anchor),'every anchor-preserving reflection is monomial')
monomial=anchor
Dsuper=sum(np.kron(p,p.conj()) for p in diagonal)/4
require(np.array_equal(Dsuper@Dsuper,Dsuper) and np.array_equal(Dsuper.conj().T,Dsuper),'pinching is a self-adjoint projection')
probe=np.array([1,0,1,0]);rho=np.outer(probe,probe)/2;drho=np.diag(np.diag(rho))
require(np.trace(rho@drho)==0.5 and np.trace(rho@(rho-drho))==0.5,'exact coefficients of return probability (1+exp(-gamma*t))/2')
for r in monomial:
    ad=np.kron(r,r.conj());require(np.array_equal(Dsuper@ad,ad@Dsuper),'pinching commutes with all native anchor-preserving reflection events')
# Here L_gamma=gamma*(D-id), gamma>=0. Matrix units give exact semigroup
# D+exp(-gamma*t)*(id-D). This is a test family, not a selected physical law.
zero=np.zeros((4,4));sigma=np.zeros((4,4))
for i in range(4):sigma[(i+1)%3 if i<3 else 3,i]=1
for p in it.permutations(range(4)):
    perm=np.eye(4)[:,p]
    for v in diagonal:
        require(canon(perm@v@perm.T) in {canon(z) for z in diagonal},'dephasing kernel covariant under all coordinate permutations')
# The marked compiler clock J*sigma has scalar J, hence the same conjugation.
# Self-adjoint nonnegative -L and its transfer e^(t L) have a positive
# Hilbert-Schmidt reflected-time kernel, by factorization of e^{(ti+tj)L}.
res={'research_id':'UR.COMPILER.QUARTIC_LIFT.09','source_pins':_pins,'nonsplitting':{k:result[k] for k in ('projective_sections_count','candidate_counts','admissible_prefix_counts')},'verdict':'EXACT_NONSPLIT_PROJECTIVE_COMPILER_WITH_EXPLICIT_QUADRATIC_CARRY','group_order':len(gm),'quotient_order':len(sperms),'kernel_order':16,'carry_formula':'(a,s)(b,t)=(a+s(b)+epsilon(t)d(s),st), arithmetic in F2^4','defect_definition':'B(sv,d(s))=q(v)+q(sv); q(a,p)=a dot p','defect_law_pairs':720**2,'Cayley_edges_verified':len(gm)*5,'GF2_constraint_rank':len(pivots),'generator_carry_choices':[(solution>>(4*j))&15 for j in range(5)],'coordinate_isomorphism_count_fixing_kernel_and_quotient':2**(20-len(pivots)),'loops':loops,'phase_retention':'The projective codec must be accompanied by the original mu4 scalar for coherent word sums; it does not recover scalar phases from projective data.','full_phase_lift_order':len(full_seen),'central_edge_phase_counts':dict(Counter(p for row in phase_edges for p in row)),'invisible_dynamics_family':{'generator':'L_gamma=gamma*(D-id), gamma>=0; D is diagonal pinching','preserves':'coordinate populations for every time and any base semigroup made of the 16 anchor-preserving reflections; every event in the added kernel acts identically in the quartic quotient; added kernel is covariant under all coordinate permutations, including displayed sigma; scalar J is trivial under conjugation','coherent_probe':'for psi=(e0+e2)/sqrt2, return probability at t is (1+exp(-gamma*t))/2','scope':'finite operational algebra; not claimed to satisfy an unconstructed full P1 net or all SM interfaces'},'physical_dynamics_selected':False,'T1_T8_closed':[]}
(OUT/'carry_certificate.json').write_text(json.dumps(res,indent=2)+'\n')
np.savez_compressed(OUT/'carry_codec.npz',symplectic_permutations=np.array(sperms,dtype=np.uint8),parity=np.array(parities,dtype=np.uint8),quadratic_defect=np.array(d,dtype=np.uint8),group_symplectic_index=np.array(gsi,dtype=np.uint16),group_carry=np.array(aval,dtype=np.uint8),group_matrices=np.array(gm),generator_edges=np.array(edges,dtype=np.uint16),central_phase_edges=np.array(phase_edges,dtype=np.uint8))
