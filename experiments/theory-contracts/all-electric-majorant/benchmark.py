"""Independent original-Hamiltonian interaction-depth jets, all sector columns."""
from collections import defaultdict

def require(ok,message):
    if not ok:raise ValueError(message)

def sector(parents,particles,background_flux):
    r38,parent=parents[-2:]
    old=r38.tree_model(parent,1,particles=particles,center=False)
    basis=[(mask,(flux[0]+background_flux,)) for mask,flux in old['basis']]
    index={key:j for j,key in enumerate(basis)}
    rows=[{} for _ in basis];free=[]
    for j,(mask,flux) in enumerate(basis):
        free.append(72*flux[0]**2+150*(mask&3).bit_count()+57600*((mask>>2)&3).bit_count())
        for out,w in parent.apply_parent(old['data'],{(mask,flux):1}).items():
            require(out in index,'whole physical Gauss sector, no flux cutoff')
            i=index[out];rows[i][j]=rows[i].get(j,0)+w
    require(all(rows[j].get(j,0)==free[j] for j in range(len(basis))),'original diagonal/free split')
    return {'basis':basis,'index':index,'rows':rows,'free':free,'data':old['data']}

def hamilton_jets(left,right,annihilator,depth,degree):
    """Coefficient of lambda^n t^p i^p/(14400^p p!) in the unsplit H(lambda)."""
    nr,nc=len(left['basis']),len(right['basis']);size=nr*nc
    values=[[0]*size for _ in range(depth+1)];values[0]=annihilator[:]
    history=[[row[:] for row in values]]
    perturb=[[ (i,w) for i,row in enumerate(left['rows']) if i!=a and (w:=row.get(a,0))] for a in range(nr)]
    right_rows=[[(b,w) for b,w in row.items() if b!=a] for a,row in enumerate(right['rows'])]
    for power in range(1,degree+1):
        nxt=[[0]*size for _ in range(depth+1)]
        for n in range(depth+1):
            for i in range(nr):
                for j in range(nc):
                    idx=i*nc+j
                    nxt[n][idx]+=(left['free'][i]-right['free'][j])*values[n][idx]
                    if n<depth and values[n][idx]:
                        v=values[n][idx]
                        for target,w in perturb[i]:nxt[n+1][target*nc+j]+=w*v
                        for target,w in right_rows[j]:nxt[n+1][i*nc+target]-=w*v
        values=nxt;history.append([row[:] for row in values])
    return history

def homogeneous(frequencies,through):
    values=[1]+[0]*through
    for f in frequencies:
        for degree in range(1,through+1):values[degree]+=f*values[degree-1]
    return values

def run(parents,normal,depth=5,degree=12):
    r49,r48,r47,r46,r45,r44,r43,r42,r41,r40,r39,r38,parent=parents
    require(depth==5 and degree==12,'declared independent physical check')
    backgrounds=(0,3,-4)
    models=[]
    for background in backgrounds:
        full=sector(parents,2,background);charged=sector(parents,1,background)
        annihilator=[0]*24
        for j,(mask,flux) in enumerate(full['basis']):
            step=r41.fermion_action(mask,2)
            if step:annihilator[charged['index'][step[0],flux]*6+j]=step[1]
        models.append((full,charged,hamilton_jets(charged,full,annihilator,depth,degree)))
    row=r40.parent_rows(models[0][0]['data']);groups=[defaultdict(int) for _ in backgrounds]
    counts=[];level=[normal.initial(0)]
    for n in range(depth+1):
        counts.append({'events':n,'nonzero_operator_paths':len(level),'electric_counts':sorted(set(len(p['dots']) for p in level))})
        require(len(level)<=2000000,'finite physical-control path guard')
        for p in level:
            for b,(full,charged,_) in enumerate(models):
                for j,(mask,flux) in enumerate(full['basis']):
                    current=mask;sign=1
                    for (site,species),create in zip(p['word'][::-1],normal.creates(p['word'])[::-1]):
                        step=r41.fermion_action(current,site+2*species,create)
                        if step is None:break
                        current,parity=step;sign*=parity
                    else:
                        target_flux=(flux[0]+dict(p['flux']).get(0,0),)
                        i=charged['index'][current,target_flux]
                        shift=(0,)+tuple(24*dict(prefix).get(0,0)*flux[0] for prefix in p['prefixes'])
                        for f,branch_sign in normal.branches(p):
                            key=(n,i*6+j,tuple(sorted(x+y for x,y in zip(f,shift))))
                            groups[b][key]+=p['weight']*sign*branch_sign
        if n<depth:
            next_level=[]
            for p in level:
                for branch in ('M','E'):
                    for q in normal.advance(parents,p,branch,row,range(2)):
                        if not r48.whole_fock_zero(q['word'],normal.creates(q['word'])):next_level.append(q)
            level=next_level
    results=[]
    for background,group,(_,_,expected) in zip(backgrounds,groups,models):
        actual=[[[0]*24 for _ in range(depth+1)] for _ in range(degree+1)]
        kernels={}
        for (n,index,f),w in group.items():
            if not w:continue
            if (n,f) not in kernels:kernels[n,f]=homogeneous(f,degree-n)
            for power,h in enumerate(kernels[n,f],n):actual[power][n][index]+=w*h*25**n*6**(power-n)
        require(actual==expected,'exact unsplit original-H interaction-depth matrix equality at flux '+str(background))
        results.append({'background_flux':background,'full_matrix_shape':[4,6],'all_input_columns':6,
                        'interaction_depth':depth,'time_jet_degree':degree,'all_coefficients_match':True,
                        'nonzero_frequency_groups':sum(bool(w) for w in group.values()),
                        'exact_scaled_matrix_jets':actual})
    return {'verdict':'UNSPLIT_PHYSICAL_INTERACTION_DEPTH_MATCHES_GENERAL_NORMAL_FORM',
            'path_counts_after_whole_operator_zero_rule':counts,'checks':results,
            'initial_state_null_pruning_used':False,'four_E_source_executed_in_finite_control':True,
            'bulk_probability_evaluated':False}
