import ast,cmath,inspect,math,unittest
import numpy as np
import engine_arithmetic as eng

class ArithmeticTests(unittest.TestCase):
 def test_exact_cofactor_scalar(self):
  n=1009*1013;fb,_=eng.base.factor_base(n,200);x=math.isqrt(n)+1+np.arange(500);q=x*x-n
  rem,_=eng.small_cofactors(q,fb)
  expected=[]
  for v in q:
   a=int(v)
   for p in fb:
    if p>43:continue
    while a%p==0:a//=p
   expected.append(a)
  self.assertEqual(rem.tolist(),expected)
 def test_conditioned_pi_literal(self):
  n=1009*1013;fb,_=eng.base.factor_base(n,200);s='1415926535897932384626433832795028841971';digits=np.array(list(map(int,s)),dtype=np.uint8)
  got,_=eng.select(n,'bucket_pi',fb,digits,pool=500,budget=100)
  scores=[]
  for j in range(500):
   x=math.isqrt(n)+1+j;r=x*x-n
   for p in fb:
    if p>43:continue
    while r%p==0:r//=p
   key=int(''.join(s[(n%len(s)+8*j+k)%len(s)] for k in range(8)))
   scores.append((r.bit_length(),key,j))
  self.assertEqual(got.tolist(),[v[2] for v in sorted(scores)[:100]])
 def test_phase_table_direct_complex(self):
  for q in [2,3,4,5,7,8,9,11,16,25,43,128,4096]:
   table=eng.phase_table(q)
   for r in set([0,1,q//2,q-1]):
    direct=abs(sum(cmath.exp(2j*math.pi*k*r/q) for k in range(9))/9)**2
    self.assertAlmostEqual(float(table[r]),direct,places=12)
    self.assertGreaterEqual(table[r],-1e-14);self.assertLessEqual(table[r],1+1e-12)
 def test_full_projector_divisibility(self):
  for q in [2,3,4,5,7,8,9,11,16,17,25,27,43]:
   for r in range(q):
    z=sum(cmath.exp(2j*math.pi*k*r/q) for k in range(q))/q
    self.assertLess(abs(z-int(r==0)),1e-12)
 def test_exact_and_phase_positive_factor(self):
  n=1009*1013;fb,_=eng.base.factor_base(n,100)
  for method in ['exact_cofactor','phase8']:
   offsets,_=eng.select(n,method,fb,pool=2000,budget=500)
   x,q,e,ids,_=eng.base.screen(n,offsets,fb)
   result=eng.base.combine(n,x,q,e,ids,fb)
   self.assertTrue(result['factor_found'])
 def test_same_info_and_unique_selection(self):
  n=1009*1013;fb,_=eng.base.factor_base(n,200);digits=np.arange(1000,dtype=np.uint8)%10
  for method in eng.METHODS:
   offsets,ops=eng.select(n,method,fb,digits,pool=500,budget=100)
   self.assertEqual(len(set(offsets.tolist())),100)
   if method.startswith('bucket_'):self.assertEqual(ops['prefilter_pool'],500)
 def test_runtime_does_not_read_answers(self):
  tree=ast.parse(inspect.getsource(eng));strings=[n.value for n in ast.walk(tree) if isinstance(n,ast.Constant) and isinstance(n.value,str)]
  self.assertFalse(any(s.endswith('answers.json') for s in strings))
  self.assertEqual(list(inspect.signature(eng.run_one).parameters),['n','method','digits'])

if __name__=='__main__':unittest.main()
