#!/usr/bin/env python3
"""Read-only extraction of selected exact Fable definitions; independent LL2 fix in memory."""
import ast
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

source = Path('/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-fable-kernfragen-20260910/fable/checks.py')
snapshot = Path(__file__).with_name('fable-ll2-reviewed-source.py')
raw = snapshot.read_bytes()
sha = hashlib.sha256(raw).hexdigest()
assert sha == 'a92ba954452f1397c364da1da6e7243d5ec5dff5fead0e5548f14f96becc8e6a', 'review snapshot changed'
tree = ast.parse(raw)
keep = {'fermion','hop','add','gauss_ok','apply_H','inner','plaquette_S','leak_theorem',
        'scale','axpy','diagonal_energy','leak_matrix','dressed_code'}
body = []
for node in tree.body:
    if isinstance(node, ast.FunctionDef) and node.name in keep:
        body.append(node)
    elif isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'SITES' for t in node.targets):
        body.append(node)
    elif isinstance(node, ast.Assign) and any(isinstance(t, ast.Tuple) and any(isinstance(x, ast.Name) and x.id == 'C_LL2' for x in t.elts) for t in node.targets):
        body.append(node)


def require(ok, message):
    if not ok:
        raise AssertionError(message)


ns = {'F':F,'require':require}
exec(compile(ast.Module(body=body,type_ignores=[]),str(source), 'exec'), ns)
old_H = ns['apply_H']


def direct_two_link(state, amp, x, y, z):
    mask, flux = state
    mask1, s1 = ns['fermion'](mask, x, False)
    if mask1 is None:
        return None
    mask2, s2 = ns['fermion'](mask1, z, True)
    if mask2 is None:
        return None
    flux = list(flux)
    for p,q in [(x,y),(y,z)]:
        if q == (p+1)%ns['SITES']:
            flux[p] += 1
        elif q == (p-1)%ns['SITES']:
            flux[q] -= 1
        else:
            raise AssertionError('not an adjacent ring edge')
    return (mask2, tuple(flux)), amp*s1*s2


def corrected_H(vec):
    out = {}
    for state, amp in vec.items():
        mask,E = state
        diag = ns['diagonal_energy'](state)
        ns['add'](out,state,amp*diag)
        for x in range(ns['SITES']):
            for y in ((x+1)%ns['SITES'], (x-1)%ns['SITES']):
                for sf,st,coef in [(0,0,ns['A_LL']),(0,1,ns['B_LH']),(1,0,ns['B_LH'])]:
                    res = ns['hop'](state,amp*coef,x,y,sf,st)
                    if res:
                        ns['add'](out,*res)
                z = (2*y-x)%ns['SITES']
                res = direct_two_link(state,amp*ns['C_LL2'],x,y,z)
                if res:
                    ns['add'](out,*res)
    return out


checks=[]


def check(name,value):
    require(value,name)
    checks.append(name)


witness=(0b1011+(1<<6),(0,0,0,0))
check('witness satisfies exact Gauss law',ns['gauss_ok'](witness))
blocked = ns['hop'](witness,F(1,576),0,1,0,0)
check('first sequential hop is Pauli blocked',blocked is None)
direct = direct_two_link(witness,F(1,576),0,1,2)
target,amp = direct
check('direct endpoint bilinear exists',target == (0b1110+(1<<6),(1,1,0,0)))
check('direct JW amplitude is -1/576',amp == -F(1,576))
check('direct target satisfies exact Gauss law',ns['gauss_ok'](target))
check('current full source H omits this target',old_H({witness:F(1)}).get(target,F(0)) == 0)
check('independent corrected H includes this target',corrected_H({witness:F(1)}).get(target,F(0)) == -F(1,576))

omega=(0b1111,(0,0,0,0))
for a in range(4):
    s=ns['plaquette_S'](omega,a)
    check(f'bare all-low H unchanged on code state{a}',old_H({s:F(1)}) == corrected_H({s:F(1)}))

old_result=ns['leak_theorem']()
ns['apply_H']=corrected_H
new_result=ns['leak_theorem']()
check('bare leak theorem unchanged',old_result['gamma_dagger_gamma_diagonal'] == new_result['gamma_dagger_gamma_diagonal'])
check('dressed residual leak changes',old_result['dressed_code']['dressed_leak_diagonal'] != new_result['dressed_code']['dressed_leak_diagonal'])
check('first-order high admixture unchanged',old_result['dressed_code']['high_admixture_weight'] == new_result['dressed_code']['high_admixture_weight'])
out={'status':'EXACT_IMPLEMENTATION_MISMATCH_CONFIRMED','source':str(source),'source_sha256':sha,
     'source_read_from_snapshot':str(snapshot),
     'source_unchanged_during_readonly_review':hashlib.sha256(source.read_bytes()).hexdigest()==sha,
     'checks':checks,'count':len(checks),'witness':{'mask':witness[0],'flux':witness[1],
     'target_mask':target[0],'target_flux':target[1],'current_amplitude':'0','correct_bilinear_amplitude':str(amp)},
     'before':old_result,'after_in_memory_only':new_result,
     'original_source_mutated':False,
     'scope':'Nonbacktracking LL2 endpoint correction only. No change to onsite energies, other terms, code definition, or first-order dressing formula.'}
Path(__file__).with_name('fable-ll2-review-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'checks':len(checks),'sha256':sha,
 'old_dressed_leak':old_result['dressed_code']['dressed_leak_float'],
 'corrected_dressed_leak':new_result['dressed_code']['dressed_leak_float'],
 'source_unchanged':out['source_unchanged_during_readonly_review']}))
