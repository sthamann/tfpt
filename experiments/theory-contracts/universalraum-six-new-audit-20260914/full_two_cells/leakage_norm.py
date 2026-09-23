"""Uniform operator leakage of the full 31x31 compression, exactly."""
from pathlib import Path
import json
import sympy as s
from checker import EDGES,partitions,young,graph_operator,star_projector,su4dim
HERE=Path(__file__).resolve().parent
x=s.Symbol('x');bound=s.Rational(1023,4096);rows=[];checks=[];ranks=0;attained=[]
for shape in partitions(8):
    gens=young(shape,True);I=s.eye(gens[0].rows)
    XA=graph_operator(gens,EDGES[:3]);XB=graph_operator(gens,EDGES[3:6])
    PA=star_projector(XA,-3)+star_projector(XA,-2)
    PB=star_projector(XB,-3)+star_projector(XB,-2);P=PA*PB
    rank=int(s.trace(P));ranks+=rank*su4dim(shape)
    if P*P!=P:raise RuntimeError('projector '+str(shape))
    H=(7*I+graph_operator(gens))/2
    A=P*H*(I-P)*H*P
    factors=s.factor_list(A.charpoly(x).as_poly())[1]
    above=0
    for f,m in factors:
        at=int(f.eval(bound)==0)
        above+=m*(int(f.count_roots(bound,s.oo))-at)
        if at:attained.append(shape)
    if above!=0:raise RuntimeError('global leakage bound '+str(shape))
    checks.append('exact leakage squared spectrum <=1023/4096 '+str(shape))
    rows.append({'shape':shape,'retained_Specht_rank':rank,
       'leakage_squared_charpoly':str(s.factor(A.charpoly(x).as_expr()))})
if ranks!=961 or attained!=[(3,3,1,1)]:raise RuntimeError('rank/attainment')
checks+=['exact retained dimension961','exact unique saturation shape(3,3,1,1)']
out={'status':'EXACT_OPERATOR_LEAKAGE','squared_norm_over_J_squared':'1023/4096',
     'norm_over_J':'sqrt(1023)/64','norm_over_local_gap':'sqrt(1023)/32',
     'norm_over_J_decimal':float(s.sqrt(1023)/64),'checks':checks,'count':len(checks),'sectors':rows}
(HERE/'leakage_norm.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='sectors'},indent=2))
