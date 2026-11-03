"""Compare original v1027 additive CAR parent with original v1002 DET16 flat parent."""
import hashlib
import json
import math
import sys
from pathlib import Path
import numpy as np
import scipy
import scipy.sparse as sp
import check_det16_source as ref


def need(ok,label):
    if not bool(ok): raise ArithmeticError(label)


def maxabs(m):
    m=m.tocsr()
    return float(np.max(np.abs(m.data))) if m.nnz else 0.0


def cj(z): return [float(z.real),float(z.imag)]


def main():
    ref.initialize_native_controls()
    identity,p=ref.I,ref.P
    d=ref.D; phase=np.exp(1j*ref.phi)
    p0,pf,om,omd=ref.native.determinant_operators(16,tuple(range(16)))
    u=identity+(1/math.sqrt(2)-1)*(p0+pf)+(phase*omd-phase.conjugate()*om)/math.sqrt(2)
    ud=u.getH().tocsr()
    need(maxabs(ud@u-identity)<1e-13,'rotation is unitary')
    need(maxabs(u@p0@ud-p)<1e-13,'rotation reaches original phi projector')
    # Construct every dressed annihilator from each native v1002 CAR mode.
    dressed=[(u@c@ud).tocsr() for c in ref.ann]
    na=sp.csr_matrix((d,d),dtype=complex)
    for a in dressed: na+=a.getH()@a
    numbers=np.fromiter((s.bit_count() for s in range(d)),dtype=np.int8,count=d)
    nd=sp.diags(numbers.astype(float),format='csr')
    need(maxabs(ud@na@u-nd)<1e-12,'actual sum of dressed numbers')
    q=identity-p
    difference_unit=ud@(na-q)@u-(nd-(identity-p0))
    need(maxabs(difference_unit)<1e-12,'Delta=1 additive vs original flat Q')
    unit_norm=float(np.max(np.abs((nd-(identity-p0)).diagonal())))
    need(abs(unit_norm-15)<1e-12,'Delta=1 comparison norm')
    need(maxabs(na-(nd+8*(p0-pf-phase*omd-phase.conjugate()*om)))<1e-12,
         'v1027 explicit additive-number identity, phase extended')
    delta=2.0
    hadd=delta*na; hflat=2*q
    diff=hadd-hflat
    # Unitarly transported actual sparse difference must be diagonal; its
    # largest absolute diagonal element is then the true operator norm.
    diagonal_difference=delta*nd-2*(identity-p0)
    need(maxabs(ud@diff@u-diagonal_difference)<1e-12,'difference in same 16-mode basis')
    opnorm=float(np.max(np.abs(diagonal_difference.diagonal())))
    need(abs(opnorm-30)<1e-12,'independent operator norm')
    need(abs(hadd[d-1,0]+8*delta*phase)<1e-12 and abs(hflat[d-1,0]+phase)<1e-12,
         'empty-full generators at same native phase and time')
    # One- versus two-particle dressed states built from native U and bit states.
    one=u[:,1]; two=u[:,3]; a=dressed[0]
    comm_flat=hflat@a-a@hflat
    comm_add=hadd@a-a@hadd
    need(maxabs(comm_add+delta*a)<1e-12,'additive Heisenberg law for mode 0')
    # All 16 dressed modes have the identical linear generator law.
    all_res=max(maxabs(hadd@x-x@hadd+delta*x) for x in dressed)
    need(all_res<1e-12,'additive Heisenberg law for all native dressed modes')
    flat_one=float(np.linalg.norm((comm_flat@one+2*a@one).toarray()))
    flat_two=float(np.linalg.norm((comm_flat@two+2*a@two).toarray()))
    need(flat_one<1e-12 and abs(flat_two-2)<1e-12,'flat nonlinear field response on two sectors')
    # Evaluate both exact semigroups as functions of the actual U N U^dagger.
    t=.31; beta=1.0
    eadd=u@sp.diags(np.exp(-delta*t*numbers),format='csr')@ud
    eflat=math.exp(-2*t)*identity+(-math.expm1(-2*t))*p
    persistence_add=(two.getH()@eadd@two)[0,0]
    persistence_flat=(two.getH()@eflat@two)[0,0]
    need(abs(persistence_add-np.exp(-2*delta*t))<1e-12,'two-excitation additive persistence')
    need(abs(persistence_flat-np.exp(-2*t))<1e-12,'two-excitation flat persistence')
    # Euclidean conjugation, NOT real-time unitary Heisenberg evolution.
    invadd=u@sp.diags(np.exp(delta*t*numbers),format='csr')@ud
    invflat=math.exp(2*t)*identity+(1-math.exp(2*t))*p
    oldadd=invadd@ref.ann[0]@eadd
    oldflat=invflat@ref.ann[0]@eflat
    entries=[]
    for row,col in ((0,1),(2,3),(d-2,d-1)):
        entries.append({'row':row,'col':col,'additive':cj(oldadd[row,col]),'flat':cj(oldflat[row,col])})
    # Real Lorentzian/unitary time on every original bare and dressed field.
    vadd=(u@sp.diags(np.exp(-1j*delta*t*numbers),format='csr')@ud).tocsr()
    vflat=(np.exp(-2j*t)*identity+(1-np.exp(-2j*t))*p).tocsr()
    need(maxabs(vadd.getH()@vadd-identity)<1e-12,'additive real-time unitarity')
    need(maxabs(vflat.getH()@vflat-identity)<1e-12,'flat real-time unitarity')
    bare_flat_error=0.0; dressed_flat_error=0.0; dressed_add_error=0.0
    for c,a in zip(ref.ann,dressed,strict=True):
        bare_flat=(vflat.getH()@c@vflat).tocsr()
        predicted=c+(np.exp(-2j*t)-1)*(p@c)+(np.exp(2j*t)-1)*(c@p)
        bare_flat_error=max(bare_flat_error,maxabs(bare_flat-predicted))
        aflat=vflat.getH()@a@vflat
        dressed_flat_error=max(dressed_flat_error,maxabs(aflat-a-(np.exp(-2j*t)-1)*(p@a)))
        dressed_add_error=max(dressed_add_error,maxabs(vadd.getH()@a@vadd-np.exp(-1j*delta*t)*a))
    need(max(bare_flat_error,dressed_flat_error,dressed_add_error)<1e-12,
         'all16 actual real-time bare/dressed field laws')
    real_two_add=(two.getH()@vadd@two)[0,0]
    real_two_flat=(two.getH()@vflat@two)[0,0]
    need(abs(real_two_add-np.exp(-2j*delta*t))<1e-12,'real-time additive four-word')
    need(abs(real_two_flat-np.exp(-2j*t))<1e-12,'real-time flat four-word')
    # Both exact trace formulas retain all zero-source constants.
    zadd=(1+math.exp(-delta*beta))**16; zflat=1+(d-1)*math.exp(-2*beta)
    need(abs(np.exp(-delta*beta*numbers).sum()-zadd)<1e-9,'native additive zero-source trace')
    need(abs(1+(d-1)*math.exp(-2*beta)-zflat)<1e-12,'flat zero-source trace')
    files=[Path(ref.native.__file__),Path(ref.__file__),Path(__file__),
           Path(ref.native.__file__).parent/'v1027_signed_det_car_wall.py']
    report={'status':'pass','native_modes':16,'phase':ref.phi,
            'reference_rule':'verification/v1027_signed_det_car_wall.py:82-139; phase extension uses native v1002 PHI, not selected by v1027',
            'construct':'original v1002 annihilators -> a_i=U c_i U† -> N_a=sum a_i† a_i; H_add=Delta N_a; H_flat=2(I-P)',
            'diagnostic_Delta':delta,'diagnostic_time':t,'diagnostic_beta':beta,
            'comparison':'same time and same carrier; no independent time rescaling or physical beta identification',
            'norm_delta1_add_minus_flat_Q':unit_norm,
            'norm_add_minus_flat':opnorm,'hadd_full_empty':cj(hadd[d-1,0]),'hflat_full_empty':cj(hflat[d-1,0]),
            'all_dressed_additive_commutator_max_error':all_res,
            'flat_residual_norm_on_one_particle':flat_one,'flat_residual_norm_on_two_particle':flat_two,
            'two_particle_additive_persistence':cj(persistence_add),'two_particle_flat_persistence':cj(persistence_flat),
            'old_c_euclidean_conjugation_entries':entries,
            'all16_real_time_bare_flat_max_error':bare_flat_error,
            'all16_real_time_dressed_flat_max_error':dressed_flat_error,
            'all16_real_time_dressed_additive_max_error':dressed_add_error,
            'real_time_two_particle_additive_word':cj(real_two_add),
            'real_time_two_particle_flat_word':cj(real_two_flat),
            'real_time_laws':'For every native bare c: alpha_flat(c)=c+(exp(-2it)-1)P c+(exp(2it)-1)c P. For a=U c Udagger: alpha_flat(a)=a+(exp(-2it)-1)P a; alpha_add(a)=exp(-i Delta t)a. These are real-time unitary laws, distinct from inverse heat conjugation above.',
            'Z_additive':zadd,'Z_flat':zflat,
            'analytical_for_all_Delta':'H_add[F,0]=-8 Delta exp(i phi); H_flat[F,0]=-exp(i phi); additive two-excitation persistence exp(-2 Delta t); flat exp(-2t); Z_add=(1+exp(-Delta beta))^16; Z_flat=1+65535 exp(-2 beta).',
            'scope':'finite original 16-mode cluster; no derivation of full TFPT S/Z, no claim v1027 selected native phi, no source-only time fit, no interacting v1013 cell.',
            'primitive_H_adm_evaluation':{
                'status':'not_computed_unidentified_original_field_transfer_map',
                'matrix_element_full_empty':None,
                'reason':'Reviewed original seed/OS passages define the full primitive dynamics/reconstruction but supply no identified action on these native v1002 mirror modes. Neither evaluated parent is relabeled as that primitive H_adm.'},
            'sha256':{str(f.resolve()):hashlib.sha256(f.read_bytes()).hexdigest() for f in files},
            'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__}
    Path(__file__).with_name('original-time16-results.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__': main()
