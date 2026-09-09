"""Fixture builder; this file is never imported by the runtime."""
import json,random,hashlib
from pathlib import Path
from sympy import nextprime,isprime
R=Path(__file__).resolve().parent
old={row[0] for row in json.loads((R.parent/'factor_fixtures.json').read_text())}
old.update(row['n'] for row in json.loads((R.parent/'relation-gate/inputs.json').read_text()))
old.update(row['n'] for row in json.loads((R.parent/'arithmetic-gate/inputs.json').read_text()))
seen=set(old);public=[];answers=[]
for split,seed in [('discovery',202609083301),('validation',202609083302)]:
 rng=random.Random(seed)
 for bits in [32,40,48,56]:
  count=0;half=bits//2
  while count<16:
   p=int(nextprime(rng.randrange(2**(half-1),2**half)))
   q=int(nextprime(rng.randrange(2**(half-1),2**half)))
   n=p*q
   if p==q or p>=2**half or q>=2**half or n.bit_length()!=bits or n in seen:continue
   seen.add(n);ident=f'{split}-{bits}-{count:02d}'
   public.append({'id':ident,'split':split,'n':n});answers.append({'id':ident,'n':n,'p':p,'q':q});count+=1
(R/'inputs.json').write_text(json.dumps(public,indent=2)+'\n')
(R/'answers.json').write_text(json.dumps(answers,indent=2)+'\n')
(R/'input_manifest.json').write_text(json.dumps({'count':len(public),'distinct':len({r['n'] for r in public}),'old_overlap':len(old&{r['n'] for r in public}),'inputs_sha256':hashlib.sha256((R/'inputs.json').read_bytes()).hexdigest(),'protocol_sha256':hashlib.sha256((R/'PROTOCOL.md').read_bytes()).hexdigest(),'seeds':[202609083301,202609083302]},indent=2)+'\n')
print('generated',len(public),'fresh public inputs; answers in separate file')
