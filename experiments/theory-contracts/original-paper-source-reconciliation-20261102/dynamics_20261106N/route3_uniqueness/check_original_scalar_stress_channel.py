"""Exact first matching test for the original Ru scalar stress channel.
This is a tensor/contact identity, not a new source or a physical fixture.
"""
import sympy as s
import json
from pathlib import Path
p=s.Matrix(s.symbols('p0:4',real=True));p2=(p.T*p)[0]
I=s.eye(4);P=p*p.T-p2*I;theta=I-p*p.T/p2
out=[]
def zero(A):return all(s.simplify(x)==0 for x in A)
def need(name,v):
 out.append({'name':name,'passed':bool(v)})
 if not v:raise AssertionError(name)
need('full_four_momentum_transversality',zero(p.T*P))
need('actual_scalar_trace_minus_three_p_squared',s.expand(s.trace(P)+3*p2)==0)
need('transverse_projector_idempotent',zero(theta*theta-theta))
need('transverse_projector_rank_three',s.simplify(s.trace(theta)-3)==0)
spin2P=theta*P*theta-theta*s.trace(theta*P)/3
need('entire_transverse_traceless_metric_channel_annihilates_scalar_response',zero(spin2P))
A,B=s.symbols('A B');C=A*I+B*p*p.T
need('only_one_covariant_scalar_stress_amplitude_after_Ward',zero((p.T*C).subs(A,-p2*B)))
need('temporal_component_vanishes_at_zero_spatial_momentum',s.simplify(P[0,0].subs({p[1]:0,p[2]:0,p[3]:0}))==0)
need('full_mixed_time_space_component',s.expand(P[0,1]-p[0]*p[1])==0)
# Exact linearized curvature variation for inverse-metric h at the original flat branch.
h=s.zeros(4)
for i in range(4):
 for j in range(i,4):h[i,j]=h[j,i]=s.Symbol(f'h{i}{j}',real=True)
xi=s.Rational(1,6);u=s.Symbol('u')
Rlin=(p.T*h*p)[0]-p2*s.trace(h)
Slin=xi*u*Rlin;T=2*xi*u*P
need('original_Ru_vertex_with_bound_xi_one_sixth',s.expand(Slin-s.trace(T*h)/2)==0)
need('diagonal_metric_source_factor',s.expand(s.diff(Slin,h[0,0])-T[0,0]/2)==0)
need('symmetric_offdiagonal_metric_source_factor',s.expand(s.diff(Slin,h[0,1])-T[0,1])==0)
need('original_nonminimal_vertex_is_transverse',zero(p.T*T))
r={'passed':sum(c['passed']for c in out),'total':len(out),'checks':out,'scope':'Original flat covariant four-dimensional branch, full contact-subtracted scalar stress response and actual R048 xiRu vertex. No state, measure, rank, cutoff or physical matrix selected.','physical_source_evaluated':False,'whole_source_nonuniqueness_claimed':False}
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
