"""Exact full-block lower bounds from an even Schatten moment.

For self-adjoint X, every eigenvalue satisfies |lambda|^32 <= tr(X^32).
Unlike a Ritz estimate, this checks the whole reduced block. Six modular
traces reconstruct the integral moment with a priori bound n*24^32; an
unused seventh modulus checks it independently.
"""
from pathlib import Path
from fractions import Fraction as Q
import hashlib,json,math,time
import numpy as np
import checker as ck

HERE=Path(__file__).resolve().parent

def moment(block,p):
    power=np.array(block['X'],dtype=np.int64)
    for _ in range(5):power=power@power%p
    return int(np.trace(power)%p)

def main():
    start=time.time();out={'moment_order':32,'blocks':{},'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'full_singlet_order_certified':False,'non_singlet_exclusion_certified':False}
    ck.need(20**32>Q(421,25)**32,'negative hidden eigenmode violates trace exclusion despite exact other Ritz vectors')
    paths=sorted(HERE.glob('modular_*.json'),reverse=True)
    for name,(shape,n) in ck.SHAPES.items():
        bound=n*24**32;modulus=1;res=[0];used=[];certs=[]
        for path in paths:
            data=json.loads(path.read_text());p=data['prime'];block=data['blocks'][name]
            ck.need(block['exact_full_intertwining'] and block['exact_full_projector_membership'],'whole primitive block certified')
            v=moment(block,p);res,modulus=ck.combine(res,modulus,[v],p);used.append(p)
            certs.append({'prime':p,'trace_X32_mod_p':v})
            if modulus>2*bound:break
        ck.need(modulus>2*bound,'enough moduli for exact trace_X32')
        exact=res[0] if 2*res[0]<=modulus else res[0]-modulus
        ck.need(0<exact<=bound,'positive moment within a priori bound')
        extra=next((json.loads(path.read_text()) for path in paths if json.loads(path.read_text())['prime'] not in used),None)
        ck.need(extra is not None,'unused trace verification prime available')
        ep=extra['prime'];ev=moment(extra['blocks'][name],ep)
        ck.need(exact%ep==ev,'independent prime verifies exact moment')
        ck.need((exact+1)%ep!=ev,'negative moment mutation rejected')
        # Floating point only proposes an endpoint. The integer comparison
        # certifies it; all statements use the exact rational endpoint below.
        num=math.ceil(exact**(1/32)*10**6)
        while num**32<=exact*10**192:num+=1
        radius=Q(num,10**6)
        ck.need(radius**32>exact,'exact whole-block spectral-radius certificate')
        bare=20-radius/2
        corrected=max(Q(47,50)*bare+Q(39,25),Q(93,100)*bare+Q(42,25))
        ck.need(corrected>Q(249,20),'every corrected eigenvalue exceeds quartet upper')
        full_irrep=ck.yb.char(shape,(1,)*5)
        out['blocks'][name]={'shape':shape,'multiplicity':n,'full_irrep_dimension':full_irrep,
          'isotypic_dimension':n*full_irrep,'trace_X32':exact,'trace_bound':bound,
          'CRT_modulus':modulus,'CRT_unique':True,'modular_certificates':certs,'extra_prime':ep,
          'X_spectral_radius_upper':str(radius),'H0_lower':str(bare),'H0_lower_decimal':float(bare),
          'Htr_lower':str(corrected),'Htr_lower_decimal':float(corrected),
          'whole_corrected_block_above_12_45':True}
        print('EXACT WHOLE BLOCK',name,'H0 >',float(bare),'Htr >',float(corrected),flush=True)
    added=sum(b['isotypic_dimension'] for b in out['blocks'].values())
    ck.need(added==1416 and added+348==1764,'all seven zero-momentum types exhausted')
    inherited=json.loads((HERE.parent/'filtered_certificate.json').read_text())
    ck.need(inherited['combined_trivial_plus_standard_dimension']==348,'correct inherited two-block dimension')
    ck.need(Q(inherited['sectors']['standard']['Rayleigh_upper']['rational'])<Q(249,20),'inherited quartet below threshold')
    out.update({'additional_controlled_isotypic_dimension':added,'total_zero_momentum_dimension':1764,
      'all_seven_zero_momentum_symmetry_types_certified':True,
      'exactly_five_eigenvalues_below_12_45_in_zero_momentum_sector':True,
      'lowest_multiplicities_in_zero_momentum_sector':[1,4],
      'zero_momentum_gap_lower':inherited['gap_in_combined_space_lower'],
      'remaining_singlet_types':11,'remaining_singlet_dimension':24024-1764,
      'parent_certificate_sha256':hashlib.sha256((HERE.parent/'filtered_certificate.json').read_bytes()).hexdigest(),
      'seconds':time.time()-start,'power_checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
    ck.save(HERE/'power_certificate.json',out)

if __name__=='__main__':main()
