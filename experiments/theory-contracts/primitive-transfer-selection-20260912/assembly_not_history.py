"""Source-pinned matrix assembly versus an explicitly additional pulse history."""
import ast
import collections
import itertools
import json
import sympy as S
import boundary_access as source


def main():
    _,b,o16,_=source.source_matrices()
    tree=ast.parse(source.SOURCE.read_bytes())
    names={'perm_order','edge_orbits'}
    nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names]
    env={'itertools':itertools}
    exec(compile(ast.Module(body=nodes,type_ignores=[]),str(source.SOURCE),'exec'),env)
    perm=(0,3,1,2,5,4)
    channels={0:list(range(10,16))}
    channels.update({j:[2*(j-1),2*(j-1)+1] for j in range(1,6)})
    j2=S.Matrix([[0,1],[-1,0]])
    groups=[]
    sizes=[]
    counts=collections.Counter()
    for edges,reverse,(x,y) in env['edge_orbits'](perm):
        block=j2 if reverse else (S.Matrix.vstack(*([S.eye(2)]*3)) if x==0 else S.eye(2))
        group=[]
        sizes.append(len(edges))
        for _ in range(env['perm_order'](perm)):
            updates={}
            for i,row in enumerate(channels[x]):
                for j,col in enumerate(channels[y]):
                    updates[row,col]=block[i,j]
                    updates[col,row]=-block[i,j]
            group.append(updates)
            counts[tuple(sorted((x,y)))]+=1
            x,y=perm[x],perm[y]
        groups.append(group)
    all_records=[r for group in groups for r in group]
    seen={}
    for record in all_records:
        for coordinate,value in record.items():
            if coordinate in seen:
                source.require(seen[coordinate]==value,'overlapping writes agree exactly')
            seen[coordinate]=value
    def assemble(records):
        result=S.zeros(16)
        for record in records:
            for coordinate,value in record.items():
                result[coordinate]=value
        return result
    source.require(assemble(all_records)==b,'literal assignment replay equals pinned source matrix')
    source.require(sorted(sizes)==[1,2,3,3,6], 'five edge-orbit sizes')
    source.require(len(all_records)==30 and len(counts)==15, 'thirty writes but fifteen unique edges')
    source.require(dict(collections.Counter(counts.values()))=={1:6,2:6,3:2,6:1}, 'nonuniform redundant write counts')
    for order in itertools.permutations(range(5)):
        records=[r for j in order for r in groups[j]]
        source.require(assemble(records)==b,'all orbit enumeration orders preserve assembled matrix')
    source.require(assemble(list(reversed(all_records)))==b,'reversing every write preserves assembled matrix')
    added=S.zeros(16)
    for record in all_records:
        for coordinate,value in record.items():
            added[coordinate]+=value
    ratios={S.simplify(added[i,j]/b[i,j]) for i in range(16) for j in range(16) if b[i,j]!=0}
    source.require(ratios=={S.Integer(1),S.Integer(2),S.Integer(3),S.Integer(6)}, 'interpreting writes as added events changes relative couplings')
    # Additional carrier-edge pulses: do not infer these from the write loop.
    edge=S.zeros(16)
    for i in (0,1):
        for j in (6,7): edge[i,j],edge[j,i]=b[i,j],b[j,i]
    k=edge[::2,1::2]+S.I*edge[::2,::2]
    o=o16[::2,::2]; eye=S.eye(8)
    orbit=[o**j*k*(o.T)**j for j in range(6)]
    j=next(j for j in range(1,6) if k*orbit[j]!=orbit[j]*k)
    l=orbit[j]
    source.require(k**3==k and l**3==l,'exact finite-pulse polynomials')
    u=eye-k*k-S.I*k; v=eye-l*l-S.I*l
    source.require(u*u.adjoint()==v*v.adjoint()==eye,'unitary pulses')
    forward,backward=v*u,u*v
    source.require(forward!=backward,'opposite histories are different maps')
    source.require(backward==u*forward*u.adjoint(),'opposite histories unitarily similar')
    source.require(forward.charpoly().as_expr()==backward.charpoly().as_expr(),'identical full spectra')
    witness=next((a,c) for a in range(8) for c in range(8)
                 if S.simplify(abs(forward[a,c])**2-abs(backward[a,c])**2)!=0)
    a,c=witness
    probabilities=[S.simplify(abs(m[a,c])**2) for m in (forward,backward)]
    source.require(probabilities[0]!=probabilities[1],'same prepared coordinate and measurement distinguish histories')
    print(json.dumps({'checks':source.count,'source_sha256':source.PIN,
        'orbit_sizes':sizes,'write_records':30,'unique_edges':15,
        'all_120_orbit_orders_preserve_assembly':True,
        'write_multiplicities':dict(sorted(collections.Counter(counts.values()).items())),
        'pulse_clock_offset':j,'pulse_history_same_spectrum':True,
        'witness_input_mode':c,'witness_output_mode':a,
        'witness_probabilities':list(map(str,probabilities)),
        'pulse_history_source_derived':False,'physical_witness_access_derived':False,
        'T1_T8_closed':[]},sort_keys=True))


if __name__=='__main__':
    main()
