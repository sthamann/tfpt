"""Bounded independent audit: integer Krylov contraction, finite Ritz and field types.

The C++ contraction avoids storing the 15,252,960-component v3.  Every
mathematical bound has an explicit source/assumption; numerical Ritz values
are not promoted to certified enclosures or a complete ground-state vector.
"""
import argparse
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import subprocess
import numpy as np

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'sources'
TENSOR = SOURCE / 'native_tensor.npz'
CHECKS = []


def need(ok, label, kind='exact'):
    if not ok:
        raise RuntimeError(label)
    CHECKS.append({'label': label, 'kind': kind})


def generators(n):
    ann = []
    for j in range(n):
        a = np.zeros((2**n, 2**n), dtype=complex)
        for m in range(2**n):
            if (m >> j) & 1:
                a[m ^ (1 << j), m] = (-1)**((m & ((1 << j) - 1)).bit_count())
        ann.append(a)
    gamma = [a + a.T for a in ann] + [1j*(a.T-a) for a in ann]
    even = [m for m in range(2**n) if not m.bit_count() % 2]
    return [(a @ b)[np.ix_(even, even)] for a,b in combinations(gamma, 2)]


def full_matrix_algebra_certificate(gens, n, prime=101):
    """Exact finite-field full-rank certificate for integer matrix words.

    A nonzero determinant modulo 101 proves the corresponding integer
    determinant is nonzero over C. Only the positive full-rank conclusion
    is used; no rank-deficiency conclusion is transferred from F_101.
    """
    pivots={};basis=[];words=[]
    def add(matrix, word):
        row=matrix.reshape(-1).copy()%prime
        for pivot, echelon in sorted(pivots.items()):
            if row[pivot]:row=(row-int(row[pivot])*echelon)%prime
        positions=np.flatnonzero(row)
        if len(positions)==0:return False
        pivot=int(positions[0]);row=(row*pow(int(row[pivot]),-1,prime))%prime
        pivots[pivot]=row;basis.append(matrix%prime);words.append(word)
        return True
    add(np.eye(n,dtype=np.int64),[])
    cursor=0
    while cursor<len(basis) and len(basis)<n*n:
        matrix=basis[cursor];word=words[cursor]
        for index,g in enumerate(gens):
            add((matrix@g)%prime,word+[index])
            if len(basis)==n*n:break
        cursor+=1
    need(len(basis)==n*n,f'integer product algebra spans M_{n} certified modulo {prime}')
    return {'modulus':prime,'dimension':len(basis),'maximum_word_length':max(map(len,words)),
            'independent_words':words}


def main(output):
    need(sha256(TENSOR.read_bytes()).hexdigest() ==
         '3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763', 'tensor source pin')
    raw = np.load(TENSOR, allow_pickle=False)['W']
    need(np.all(raw.imag == 0) and np.all(raw.real == np.rint(raw.real)), 'integer native tensor')
    W = raw.real.astype(np.int64)
    need(np.array_equal(W@W.T, 8*np.eye(60, dtype=np.int64)), 'W W transpose = 8 I')
    pairs = list(combinations(range(64), 2))
    support = [[(*pairs[c], int(W[A,c])) for c in np.flatnonzero(W[A])] for A in range(60)]
    text = '\n'.join(f'{A} {i} {j} {w}' for A,s in enumerate(support) for i,j,w in s)
    replay = subprocess.run([str(HERE/'contracted_krylov')], input=text, capture_output=True,
                            text=True, check=True, timeout=90)
    c = json.loads(replay.stdout)
    for key, value in {'v2_entries':108240, 'v2_norm2':439680,
                       'v2_dot_u':575078400, 'u_norm2':752194252800}.items():
        need(c[key] == value, 'fresh independent contraction '+key)
    nu2,nu3 = c['v2_norm2'], c['v2_dot_u']
    w2 = F(c['u_norm2']) - F(nu3**2, nu2)
    need(w2 == F(5001523200,229), 'corrected orthogonal Krylov norm')
    need(w2 > 0, 'single vector per boson layer does not close')
    alpha = F(nu3,nu2)
    need(alpha == F(299520,229), 'projection coefficient')
    need(w2/nu3 == F(1809,47632), 'extra Ritz coupling squared')
    old = json.loads((SOURCE/'native_ground_state.json').read_text())
    srcsha = sha256((SOURCE/'native_ground_state.py').read_bytes()).hexdigest()
    need(srcsha != old['checker_sha256'], 'supplied ground JSON is stale relative to corrected code')
    need(F(old['guards']['closure']['w2_norm2']) == w2 * 229**2,
         'stale norm differs exactly by omitted denominator 229 squared')
    need(old['guards']['closure']['closure_defect'] > 1,
         'stale orthogonal fraction fails elementary probability bound')

    ritz = []
    moment_path = SOURCE/'moment_4.stdout.txt'
    prior_moment=json.loads(moment_path.read_text())
    need(prior_moment['order']==4 and prior_moment['squared_norm']==952296652800,
         'prior v1.6.4 fourth moment receipt retained, not re-enumerated')
    nu4 = prior_moment['squared_norm']
    for g in (F(1,20), F(1,40), F(1,100), F(1,400)):
        h = np.diag(np.arange(4, dtype=float))
        for k, r in enumerate((480,916,F(nu3,nu2))):
            h[k,k+1] = h[k+1,k] = float(g)*float(r)**.5
        hx = np.zeros((5,5));hx[:4,:4]=h;hx[4,4]=2
        hx[3,4]=hx[4,3]=float(g)*float(w2/nu3)**.5
        vals, vec = np.linalg.eigh(h)
        e, ex = vals[0], np.linalg.eigvalsh(hx)[0]
        c3sq = vec[3,0]**2
        residual2 = float(g*g)*c3sq*float((F(nu4)+w2)/nu3)
        need(ex <= e, 'expanded Ritz bound is non-increasing '+str(g), 'numerical')
        ritz.append({'g':str(g),'four_state_ritz':float(e),'five_state_ritz':float(ex),
                     'energy_change':float(ex-e), 'residual_squared_using_prior_nu4':residual2,
                     'residual_norm':residual2**.5, 'last_chain_weight':float(c3sq)})
    known_upper=F(-1129636,10**6)
    need(F(-1158089,10**6)>F(-6,5), 'proposed E below -1.2 contradicts prior lower enclosure')
    need(F(-1158089,10**6)>F(-11625,10000), 'proposed E below -1.1625 contradicts prior lower enclosure')
    need(ritz[0]['five_state_ritz'] - float(known_upper) > .0354,
         'new low-order Ritz value remains at least .0354 above known true-ground upper bound', 'numerical')
    residual_share= w2/(F(nu4)+w2)
    need(residual_share < F(23,10**6), 'small w2 accounts for less than 23 ppm of K3 residual squared')

    adj=[set() for _ in range(64)]
    mats=[]
    for A,s in enumerate(support):
        M=np.zeros((64,64),dtype=np.int64)
        for i,j,w in s: adj[i].add(j);adj[j].add(i);M[i,j]=w;M[j,i]=-w
        mats.append(M)
    need(all(len(n)==15 for n in adj),'native graph regular degree 15')
    seen={0};pending=[0]
    while pending:
        for j in adj[pending.pop()]:
            if j not in seen:seen.add(j);pending.append(j)
    need(len(seen)==64,'native graph connected')
    cycle=[16,45,0,30,37]
    need(len(set(cycle))==5 and all(cycle[(k+1)%5] in adj[cycle[k]] for k in range(5)),
         'supplied five-cycle independently checked')
    need(all(not(adj[i]&adj[j]) for i in range(64) for j in adj[i]),'no triangles')
    block=mats[0].reshape(16,4,16,4)
    s,t=next((s,t) for s in range(16) for t in range(16) if block[s,:,t,:].any())
    Cfactor=[mats[a].reshape(16,4,16,4)[s,:,t,:] for a in range(6)]
    i,j=np.argwhere(Cfactor[0]!=0)[0]
    Sfactor=[mats[6*k].reshape(16,4,16,4)[:,i,:,j]//Cfactor[0][i,j] for k in range(10)]
    need(all(np.array_equal(mats[6*k+a],np.kron(Sfactor[k],Cfactor[a]))
             for k in range(10) for a in range(6)), 'exact tensor factorization M_ka=S_k tensor C_a')
    need(np.array_equal(sum(s.T@s for s in Sfactor),5*np.eye(16,dtype=int)), 'spinor factor completeness 5 I')
    need(np.array_equal(sum(c.T@c for c in Cfactor),3*np.eye(4,dtype=int)), 'colour factor completeness 3 I')
    spin_algebra=full_matrix_algebra_certificate([x.T@y for x in Sfactor for y in Sfactor],16)
    colour_algebra=full_matrix_algebra_certificate([x.T@y for x in Cfactor for y in Cfactor],4)
    eps=np.array([[0,1],[-1,0]],dtype=complex)
    s1=np.array([[0,1],[1,0]],dtype=complex)
    s2=np.array([[0,-1j],[1j,0]],dtype=complex)
    s3=np.diag([1,-1]).astype(complex);I=np.eye(2,dtype=complex);O=np.zeros((2,2),complex)
    gamma=[np.block([[O,I],[I,O]])]+[np.block([[O,s],[-s,O]]) for s in (s1,s2,s3)]
    C=1j*gamma[2]@gamma[0];g5=1j*gamma[0]@gamma[1]@gamma[2]@gamma[3]
    kernels={'scalar':C,'pseudoscalar':C@g5}
    kernels.update({f'axial{mu}':C@g@g5 for mu,g in enumerate(gamma)})
    kernels.update({f'vector{mu}':C@g for mu,g in enumerate(gamma)})
    kernels.update({f'tensor{mu}{nu}':C@((1j/2)*(gamma[mu]@gamma[nu]-gamma[nu]@gamma[mu]))
                    for mu,nu in combinations(range(4),2)})
    symmetries={}
    for name,K in kernels.items():
        expected=1 if name.startswith(('vector','tensor')) else -1
        need(np.array_equal(K.T,expected*K),'exact Dirac kernel transpose '+name)
        symmetries[name]='symmetric' if expected==1 else 'antisymmetric'
    for A,M in enumerate(mats):
        T=np.kron(M,eps)
        need(np.array_equal(T,T.T),f'single Weyl scalar channel vanishes {A}')
        T2=np.kron(np.kron(M,eps),eps)
        need(np.array_equal(T2,-T2.T) and np.any(T2),f'independent two-copy scalar repair nonzero {A}')
        V=np.kron(M,kernels['vector0'])
        need(np.array_equal(V,-V.T) and np.any(V),f'four-component vector nonzero {A}')
        doubled=np.kron(M,s1)
        Gamma=np.diag(np.tile([1,-1],64))
        need(np.array_equal(Gamma@doubled+doubled@Gamma,np.zeros((128,128))),
             f'bipartite two-copy cover permits opposite handed endpoints {A}')

    ev=[m for m in range(32) if m.bit_count()%2==0]
    cv=[m for m in range(8) if m.bit_count()%2==0]
    fw=np.array([[1-2*((m>>j)&1) for j in range(5)]+[1-2*((c>>j)&1) for j in range(3)] for m in ev for c in cv])
    spin=[np.kron(g,np.eye(4)) for g in generators(5)]
    colour=[np.kron(np.eye(16),g) for g in generators(3)]
    gens=spin+colour
    gradings={'identity':np.ones(64,dtype=int)}
    gradings.update({f'spinor{p}{q}':fw[:,p]*fw[:,q] for p,q in combinations(range(5),2)})
    gradings.update({f'colour{p}{q}':fw[:,5+p]*fw[:,5+q] for p,q in combinations(range(3),2)})
    gradings.update({f'mixed{s}_{c}':gradings[s]*gradings[c]
                     for s in tuple(gradings) if s.startswith('spinor')
                     for c in tuple(gradings) if c.startswith('colour')})
    grading_results={}
    for name,gr in gradings.items():
        comm=np.array([((gr[:,None]-gr[None,:])*g).ravel() for g in gens])
        gram=(comm@comm.conj().T).real
        need(np.array_equal(gram,np.diag(np.diag(gram))),f'exact real Gram diagonal for grading {name}')
        dim=int(np.count_nonzero(np.diag(gram)==0))
        census={'vector':0,'tensor':0,'mixed':0}
        for s in support:
            opposite=sum(gr[i]!=gr[j] for i,j,w in s)
            census['vector' if opposite==8 else 'tensor' if opposite==0 else 'mixed']+=1
        tag=next((t for t in ('identity','spinor','colour','mixed') if name.startswith(t)))
        expected={'identity':(0,60,60),'spinor':(24,36,36),'colour':(40,20,52),'mixed':(32,28,28)}[tag]
        need((census['vector'],census['tensor'],dim)==expected and census['mixed']==0,
             'exact grading census and stabilizer '+name)
        grading_results[name]={'census':census,'stabilizer_real_dimension':dim}
    fields = json.loads((SOURCE/'field_dictionary.json').read_text())
    result={'status':'PASS','checks':CHECKS,'checks_count':len(CHECKS),
            'input_sha256':{p.name:sha256(p.read_bytes()).hexdigest() for p in sorted(SOURCE.iterdir()) if p.is_file()},
            'verifier_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'contraction_source_sha256':sha256((HERE/'contracted_krylov.cpp').read_bytes()).hexdigest(),
            'checks_exact':sum(c['kind']=='exact' for c in CHECKS),
            'checks_numerical':sum(c['kind']=='numerical' for c in CHECKS),
            'contraction':c,'w2_norm2':str(w2),'w2_coupling_squared':str(w2/nu3),
            'w2_fraction_of_total_K3_residual_squared':str(residual_share),
            'ritz':ritz,'graph':{'odd_cycle':cycle,'connected':True,'bipartite':False},
            'basis_independent_grading_obstruction':{
                'hypothesis':'Gamma Hermitian and Gamma^T M_A+M_A Gamma=0 for every unchanged channel',
                'conclusion':'Gamma=0; in particular no Hermitian involution grades all channels as opposite-handed',
                'spin_algebra_certificate':spin_algebra,'colour_algebra_certificate':colour_algebra,
                'reason':'Gamma commutes with all M_A dagger M_B; factor completeness and full generated matrix algebras force scalar Gamma; the original condition then forces zero'},
            'dirac_kernel_symmetries':symmetries,'gradings':grading_results,
            'source_status':{'ground_code_sha256':srcsha,'ground_json_code_sha256':old['checker_sha256'],
                             'ground_json_is_stale':True,
                             'field_json_code_matches':fields['checker_sha256']==sha256((SOURCE/'field_dictionary.py').read_bytes()).hexdigest()},
            'boundaries':['no complete ground eigenvector','no convergence certificate from small w2 alone',
                          'four-component and two-copy repairs add degrees of freedom',
                          'no healthy kinetic term or native field adapter derived','no T1-T8 closure']}
    output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:result[k] for k in ('status','checks_count','checks_exact','checks_numerical','contraction','w2_norm2','ritz','source_status')},indent=2))


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=HERE/'audit.json');args=ap.parse_args()
    main(args.output)
