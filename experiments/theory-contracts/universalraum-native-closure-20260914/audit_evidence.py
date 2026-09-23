"""Read-only cross-check of final evidence plus independent exact polynomial audit.

This is not another full 24024-dimensional construction. It verifies source
hashes, all saved modular polynomial residues and the rational root statements.
"""
from pathlib import Path
import hashlib,json,math
import sympy as s

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def need(x,msg):
    if not bool(x):raise RuntimeError(msg)
    checks.append(msg)
for stem in ['joint_source','charge_and_matching']:
    data=json.loads((HERE/(stem+'.json')).read_text())
    need(data['source_sha256']==sha(HERE/(stem+'.py')),'source hash '+stem)
    need((HERE/(stem+'.json')).read_bytes()==(HERE/(stem+'_optimized.json')).read_bytes(),'normal optimized '+stem)
control=json.loads((HERE/'controls/verification.json').read_text())
need(control['source_sha256']==sha(HERE/'controls/verify_controls.py'),'control source hash')
scaling=json.loads((HERE/'scaling/replay.json').read_text())
need(scaling['checker_sha256']==sha(HERE/'scaling/check_scaling.py'),'scaling source hash')
need(scaling['checks']==400,'final scaling count not stale intermediate')
q=json.loads((HERE/'quartet/replay.json').read_text())
for name,h in q['source_sha256'].items():need(h==sha(HERE/'quartet'/name),'quartet source hash '+name)
e=json.loads((HERE/'quartet/exact_polynomial.json').read_text())
c=e['integer_coefficients_descending'];p=s.Poly.from_list(c,s.Symbol('x'))
need(len(c)==81 and c[0]==1,'monic degree 80')
need(all(abs(a)<=math.comb(80,k)*40**k for k,a in enumerate(c)),'all elementary coefficient bounds')
mods=e['reconstruction_primes'];need(len(mods)==17 and len(set(mods))==17,'distinct 17 reconstruction primes')
need(math.prod(mods)==e['CRT_modulus'] and math.prod(mods)>2*max(math.comb(80,k)*40**k for k in range(81)),'CRT uniqueness, independently recomputed')
for prime in mods+[e['extra_check_prime']]:
    d=json.loads((HERE/'quartet'/('modular_'+str(prime)+'.json')).read_text())
    need(s.isprime(prime),'certified prime '+str(prime))
    need([a%prime for a in c]==d['characteristic']['coefficients_descending'],'integer polynomial reduces to full saved modular polynomial '+str(prime))
    need(d['checker_sha256']==sha(HERE/'quartet/checker.py'),'modular source hash '+str(prime))
need(s.gcd(p,p.diff()).degree()==0,'rational characteristic polynomial squarefree')
a,b=map(s.Rational,e['lowest_H0_interval'])
need(p.count_roots(-41,2*a-40)==0 and p.count_roots(2*a-40,2*b-40)==1,'first standard root isolated independently')
u,v=map(s.Rational,e['second_H0_interval'])
need(p.count_roots(2*b-40,2*u-40)==0 and p.count_roots(2*u-40,2*v-40)==1,'second standard root isolated independently')
need(all(x==0 for x in c[1::2]),'exact even polynomial')
little=json.loads((HERE/'quartet/little_group_reduction.json').read_text())
rows=little['blocks']
need(len(rows)==18 and sum(x['isotypic_dimension'] for x in rows)==24024,'full singlet dimensional sum')
need(max(x['multiplicity_block_dimension']//2 for x in rows)==131,'maximum squared singular block 131')
source_paths={'N14_Fortsetzung.md':'TFPT_Universalraum_Fortsetzung_2026-09-14NEU.md',
              'N15_Ergebnisse.md':'TFPT_UNIVERSALRAUM_ERGEBNISSE_2026-09-14.md'}
for copied,original in source_paths.items():
    need(sha(HERE/'sources'/copied)==sha(Path('/Users/stefanhamann/Documents')/original),'unmodified user source '+copied)
report={'count':len(checks),'checks':checks,'scope':'independent exact polynomial and provenance audit; not a full sector replay',
        'source_sha256':sha(Path(__file__)),'all_T1_T8_still_open':True}
(HERE/'evidence_audit.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps({'conditions':len(checks),'passed':True}))
