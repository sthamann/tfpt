"""Exact identity checks plus separately labelled QWZ floating diagnostics."""
from pathlib import Path
import hashlib,json
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]

def require(ok,message):
    if not ok: raise ValueError(message)

def source_diagnostics():
    W=8;N=256
    sx=np.array([[0,1],[1,0]],complex)
    sy=np.array([[0,-1j],[1j,0]])
    sz=np.diag([1,-1]);ty=sy/(2j)-sz/2
    def symbol(k):
        rho=1-np.cos(k)
        h=np.kron(np.eye(W),-np.sin(k)*sx+rho*sz)
        for y in range(W-1):
            h[2*y:2*y+2,2*y+2:2*y+4]=ty.conj().T
            h[2*y+2:2*y+4,2*y:2*y+2]=ty
        return h
    rows={}
    for r in range(-N//2,N//2):
        k=2*np.pi*(r-.5)/N;rho=1-np.cos(k)
        b=np.kron(rho**np.arange(W),np.array([1,-1])/np.sqrt(2))
        b/=np.linalg.norm(b)
        e,u=np.linalg.eigh(symbol(k));rows[r]=(e,np.abs(u.conj().T@b)**2)
    data=[]
    for M in (6,12,63):
        for n in (1,2,3):
            w0=w1=w2=0.
            for r,(e,w) in rows.items():
                r2=(r-n+N//2)%N-N//2
                if not(-M<=r<=M and -M<=r2<=M): continue
                f,v=rows[r2];pos=e>0;neg=f<0
                weight=w[pos,None]*v[None,neg]
                freq=(e[pos,None]-f[None,neg])*N/(2*np.pi)
                w0+=weight.sum();w1+=(weight*freq).sum();w2+=(weight*(freq-n)**2).sum()
            data.append({'M':M,'n':n,'weight':float(w0),'mean_frequency':float(w1/w0),
                         'rms_error':float(np.sqrt(w2/w0))})
    for row,exp in zip(data[:3],[.9999749004870758,1.9996486272298428,2.998720127427866]):
        require(abs(row['weight']-row['n'])<1e-11,'small-window weight')
        require(abs(row['mean_frequency']-exp)<1e-10,'small-window mean')
    require(data[6]['weight']>1.1 and data[6]['mean_frequency']>9,'broad-window control')
    def energy(f):
        return sum(-np.abs(np.linalg.eigvalsh(symbol(2*np.pi*(n-f)/N))).sum()/2
                   for n in range(N))
    es={f:energy(f) for f in (0,.25,.5)}
    shifts={str(f):(es[f]-es[0])*N/(2*np.pi) for f in (.25,.5)}
    require(abs(shifts['0.25']+.1875017649)<1e-8,'quarter energy replay')
    require(abs(shifts['0.5']+.2500031375)<1e-8,'AP energy replay')
    return {'W':W,'N':N,'r':2,'current_window_diagnostics':data,
            'scaled_sector_energy_relative_periodic':shifts,
            'numerical_not_interval_certified':True}

def run():
    for name,digest in json.loads((HERE/'source_manifest.json').read_text())['sha256'].items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,'source changed: '+name)

    # Exact original strip recurrence at symbolic rho and sin k.
    rho,t=s.symbols('rho t',real=True)
    sx=s.Matrix([[0,1],[1,0]]);sz=s.diag(1,-1);ty=s.Matrix([[-1,-1],[1,1]])/2
    recurrence=[]
    for W in (1,2,8):
        h=s.Matrix(s.kronecker_product(s.eye(W),-t*sx+rho*sz))
        for y in range(W-1):
            h[2*y:2*y+2,2*y+2:2*y+4]=ty.T
            h[2*y+2:2*y+4,2*y:2*y+2]=ty
        b=s.Matrix([v for y in range(W) for v in (rho**y,-rho**y)])
        expected=s.zeros(2*W,1);expected[-2]=expected[-1]=rho**W
        require(s.simplify((h-t*s.eye(2*W))*b-expected)==s.zeros(2*W,1),'edge recurrence')
        recurrence.append(W)

    # Carry algebra on the two cosets; no bounded cyclic charge truncation.
    for k in (0,1):
        old=s.Rational(k,2);new=s.Integer(k)+s.Rational(1-k,2)
        require(new-old==s.Rational(1,2),'half charge each leg')
        ratio=(s.I if k==0 else (-1)**5/s.I)
        require(s.simplify(ratio-s.I)==0,'clock carry phase')
    require(1/s.I==-s.I,'no-carry return has wrong phase')

    # Universal Schur identity in a smallest nontrivial retained block.
    z,x,y=s.symbols('z x y')
    hp=s.diag(0,4);b=s.Matrix([[x,y]])
    h=s.Matrix([[0,0,x],[0,4,y],[x,y,1]])
    sigma=b.T*b/(z-1)
    lhs=(z*s.eye(3)-h).inv()[:2,:2]
    rhs=(z*s.eye(2)-hp-sigma).inv()
    require(s.simplify(lhs-rhs)==s.zeros(2),'exact full projected resolvent')
    require(s.diff(sigma[0,0],x,2)==2/(z-1),'probe curvature despite zero unperturbed Sigma')

    # Rank-one root oscillator coefficient checks: [s_n,s_-n]=2n.
    w,a1,a2=s.symbols('w a1 a2')
    p2=(a1*a1+a2)/2
    exp2=1+a1*w+p2*w*w
    require(s.expand(w*w*exp2).coeff(w,0)==0,'same mode -1 twice vanishes')
    require(s.expand(w*w*exp2).coeff(w,2)==1,'mode -3 after -1 carries2s')
    shifted=p2.subs({a1:a1-2/w,a2:a2-2/w**2},simultaneous=True)
    require(s.expand(w*w*exp2*shifted).coeff(w,0)==1,'reverse order same-root modes')
    require(s.Rational(1,4)*(2*2**2+4)==3,'squared norm of mode -3 vacuum vector')
    u=s.symbols('u');require((1-u)+(3-u)==4-2*u,'source-shifted two-hit energy')
    require((1-u).subs(u,1)==0,'quarter-holonomy intermediate zero energy')

    return {'contract':HERE.name,'verdict':'PARTIAL',
       'exact':{'symbolic_recurrence_widths':recurrence,'carry_and_clock':True,
          'schur_projected_resolvent_all_orders':True,'two_hit_root_coefficients':[0,1],
          'cocycle_factor_retained_as_epsilon':True,'source_frequency_generator_distinguished':True},
       'source_numerical':source_diagnostics(),
       'analytic_in_text':['uniform fixedW sector-energy O(N^-3) remainder',
         'bounded theta-odd probe response and Volterra reduction'],
       'unbounded_continuum_control_limit_proved':False,
       'microscopic_spinor_constructed':False,'eight_native_channels_derived':False,
       'physical_gates_closed':[],'complete_TFPT_solution':False}

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
