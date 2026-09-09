"""Independent arithmetic and no-answer-input regression tests."""
import ast,inspect,math,unittest
import numpy as np
import engine

class EngineTests(unittest.TestCase):
 def test_exact_positive_factor_control(self):
  n=77;base=[2,3,5];xs,qs,e,ids,ops=engine.screen(n,np.array([0]),base)
  self.assertEqual(int(xs[0]),9);self.assertEqual(int(qs[0]),4)
  out=engine.combine(n,xs,qs,e,ids,base)
  self.assertTrue(out['factor_found']);self.assertIn(out['certificate']['factor'],[7,11])
 def test_vector_screen_against_scalar(self):
  for n in [77,1009*1013,65537*65539,1000003*1000033]:
   base,_=engine.factor_base(n,200);offsets=np.random.default_rng(n).choice(1000,200,replace=False)
   xs,qs,e,ids,_=engine.screen(n,offsets,base);expected=[]
   for idx,j in enumerate(offsets):
    x=math.isqrt(n)+1+int(j);q=x*x-n;rem=q;exps=[]
    for p in base:
     count=0
     while rem%p==0:rem//=p;count+=1
     exps.append(count)
    if rem==1:expected.append((idx,x,q,exps))
   self.assertEqual(ids.tolist(),[v[0] for v in expected])
   self.assertEqual(xs.tolist(),[v[1] for v in expected])
   self.assertEqual(qs.tolist(),[v[2] for v in expected])
   self.assertEqual(e.tolist(),[v[3] for v in expected])
 def test_digit_selection_literal_and_wrap(self):
  s='1415926535897932384626433832795028841971';d=np.array(list(map(int,s)),dtype=np.uint8)
  for n in [1,77,123456789012345]:
   got=engine.select(n,'pi',d,pool=100,budget=20)
   keys=[int(''.join(s[(n%len(s)+8*j+k)%len(s)] for k in range(8))) for j in range(100)]
   expected=sorted(range(100),key=lambda j:keys[j])[:20]
   self.assertEqual(got.tolist(),expected)
 def test_stable_ties_and_distinct_offsets(self):
  d=np.zeros(17,dtype=np.uint8)
  self.assertEqual(engine.select(77,'pi',d,pool=100,budget=20).tolist(),list(range(20)))
 def test_runtime_no_answer_key_access(self):
  tree=ast.parse(inspect.getsource(engine));imports=[]
  for n in ast.walk(tree):
   if isinstance(n,ast.Import):imports.extend(x.name for x in n.names)
   if isinstance(n,ast.ImportFrom):imports.append(n.module)
  self.assertFalse(any(x in ['sympy','make_inputs','test_engine'] for x in imports))
  strings=[n.value for n in ast.walk(tree) if isinstance(n,ast.Constant) and isinstance(n.value,str)]
  self.assertFalse(any(x.endswith('answers.json') for x in strings))
  self.assertEqual(list(inspect.signature(engine.run_one).parameters),['n','method','digits'])
 def test_repeated_offsets_not_accepted_by_actual_selector(self):
  for method in engine.METHODS:
   ids=engine.select(65537*65539,method,np.arange(1000,dtype=np.uint8)%10,pool=200,budget=100)
   self.assertEqual(len(set(ids.tolist())),100)
 def test_binary_dependency_certificates(self):
  n=1009*1013;base,_=engine.factor_base(n,100)
  xs,qs,e,ids,_=engine.screen(n,np.arange(2000),base)
  out=engine.combine(n,xs,qs,e,ids,base);self.assertTrue(out['factor_found'])
  c=out['certificate'];product=math.prod(c['qs']);y=math.isqrt(product)
  self.assertEqual(y*y,product)
  x=math.prod(c['xs'])
  self.assertEqual((x*x-y*y)%n,0);self.assertEqual(x%n,c['X_mod_N']);self.assertEqual(y%n,c['Y_mod_N'])
  self.assertEqual(c['factor']*c['cofactor'],n)

if __name__=='__main__':unittest.main()
