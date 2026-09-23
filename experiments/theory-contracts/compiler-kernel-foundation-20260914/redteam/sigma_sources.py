"""Read-only replay: source lattice sigma acts on contexts, not Pauli labels."""
from pathlib import Path
from itertools import combinations
import ast
import contextlib
import hashlib
import importlib.util
import io
import json
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
CHECKS=[]


def need(ok,message):
    if not bool(ok):raise RuntimeError(message)
    CHECKS.append(message)


def source_prefix():
    path=ROOT/'verification/v783_two_qubit_clifford.py'
    tree=ast.parse(path.read_text())
    main=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='main')
    stop=next(i for i,n in enumerate(main.body) if isinstance(n,ast.Expr) and isinstance(n.value,ast.Call)
              and isinstance(n.value.func,ast.Name) and n.value.func.id=='section'
              and isinstance(n.value.args[0],ast.Constant) and n.value.args[0].value.startswith('P2 (H2a)'))
    main.body=main.body[:stop]+[ast.Return(ast.Call(ast.Name('locals',ast.Load()),[],[]))]
    class Guards(ast.NodeTransformer):
        def visit_Assert(self,node):
            return ast.copy_location(ast.Expr(ast.Call(ast.Name('need',ast.Load()),[node.test,ast.Constant('source assertion '+str(node.lineno))],[])),node)
    module=ast.fix_missing_locations(Guards().visit(ast.Module([main],[])))
    env={'need':need};exec(compile(module,str(path),'exec'),env)
    with contextlib.redirect_stdout(io.StringIO()):d=env['main']()
    for name,ok in d['CHECKS']:need(ok,'v783 source '+name)
    return d


def run():
    d=source_prefix()
    path=ROOT/'verification/v774_arf_spinor_compiler.py'
    spec=importlib.util.spec_from_file_location('arf_source',path)
    src=importlib.util.module_from_spec(spec);spec.loader.exec_module(src)
    with contextlib.redirect_stdout(io.StringIO()):src.s1_lattice()
    for name,ok in src.CHECKS:need(ok,'v774 source '+name)
    need(src.PI_SIG==d['PI_SIG']==(4,5,0,1,2,3,6,7),'the two original sources use exactly the same ambient sigma')
    sigma=s.Matrix([[0,0,1,0],[1,0,0,0],[0,1,0,0],[0,0,0,1]])
    pm={bits:s.Matrix([[s.Integer(x)+s.I*y for x,y in row] for row in matrix]) for bits,matrix in d['PMAT'].items()}
    perm={}
    for bits,matrix in pm.items():
        transformed=sigma*matrix*sigma.H
        candidates=[other for other,value in pm.items() if transformed==value or transformed==-value]
        need(len(candidates)==1,'source coordinate sigma has unique projective Pauli image '+str(bits))
        perm[bits]=candidates[0]
    fixed_paulis=[b for b in d['NZ_BITS'] if perm[b]==b]
    ctxperm={j:d['contexts'].index(frozenset(perm[b] for b in ctx)) for j,ctx in enumerate(d['contexts'])}
    fixed_contexts=[j for j in ctxperm if ctxperm[j]==j]
    need(len(fixed_paulis)==0 and len(fixed_contexts)==3,'same Gaussian sigma fixes zero Pauli points and three Pauli contexts')
    class_ctx={}
    for r,z in zip(d['ROOTS'],d['Z240']):
        label=d['root_label'][r];ctx=d['stab_ray_ctx'][d['canonical_ray'](z)]
        if label in class_ctx:need(class_ctx[label]==ctx,'all four rays in a Gaussian class give the same context')
        class_ctx[label]=ctx
    need(len(class_ctx)==len(set(class_ctx.values()))==15,'actual source class-to-context dictionary is bijective')
    for r in d['ROOTS']:
        sr=tuple(r[j] for j in d['PI_SIG'])
        need(class_ctx[d['root_label'][sr]]==ctxperm[class_ctx[d['root_label'][r]]],
             'source sigma intertwines every root-class image with its context image')
    fixed_bits=[v for v in src.W16 if any(v) and src.sig_bits(v)==v]
    need(len(fixed_bits)==3,'v774 family labels have three nonzero fixed words, as source contexts do')
    result={'status':'SOURCE_SIGMA_DISTINCTION_RESOLVED_BY_CONTEXT_DICTIONARY',
            'check_count':len(CHECKS),'checks':CHECKS,
            'same_ambient_sigma_in_v774_and_v783':True,
            'v774_nonzero_fixed_quotient_labels':list(map(list,fixed_bits)),
            'gaussian_sigma_fixed_nonzero_pauli_operator_labels':len(fixed_paulis),
            'gaussian_sigma_fixed_pauli_contexts':len(fixed_contexts),
            'source_class_context_bijection':15,'rootwise_equivariance_checks':240,
            'interpretation':'same underlying source lattice element, different representations: quotient labels correspond to Pauli contexts, not Pauli operator labels',
            'source_outer_twist_reference':'v783 lines928-935 explicitly name GQ(2,2) point-line duality and S6 outer twist; its Hom census is not recomputed here',
            'no_source_contradiction_claimed':True,
            'source_hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                             for p in [ROOT/'verification/v783_two_qubit_clifford.py',path,ROOT/'verification/v689_gaussian_code_bridge.py']}}
    return result


if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('--out',default='sigma_verification.json');args=ap.parse_args()
    result=run();(HERE/args.out).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
