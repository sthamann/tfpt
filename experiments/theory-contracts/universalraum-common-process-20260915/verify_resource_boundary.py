"""Exact resource boundaries: coherent histories and charge references."""
import json
import sympy as s
checks=[]
def eq(A,B,name):
    d=A-B
    ok=all(s.simplify(x)==0 for x in d) if isinstance(d,s.MatrixBase) else s.simplify(d)==0
    if not ok:raise RuntimeError(name)
    checks.append(name)

def main():
    I=s.eye(2);Z=s.diag(1,-1);X=s.Matrix([[0,1],[1,0]])
    # Same channel on a complete operator basis, but not the same marked
    # vector-amplitude Gram kernel. A coherent-control resource distinguishes.
    for i in range(2):
        for j in range(2):
            E=s.zeros(2);E[i,j]=1
            eq(Z*E*Z,(-Z)*E*(-Z),'same channel on matrix unit '+str((i,j)))
    omega=s.Matrix([1,0])
    for i,u in enumerate((I,X,Z)):
        for j,v in enumerate((I,X,Z)):
            eq(((u*omega).H*(v*omega))[0],(omega.H*(u.H*v)*omega)[0],
               'all first-row words determine every kernel entry '+str((i,j)))
    eq((omega.H*Z*omega)[0],1,'positive marked word kernel')
    eq((omega.H*(-Z)*omega)[0],-1,'different marked word kernel for same channel')
    cp=s.diag(1,1,1,-1);cm=s.diag(1,1,-1,1)
    seed=s.kronecker_product(s.Matrix([1,1])/s.sqrt(2),omega)
    probe=s.kronecker_product(X,I)
    eq((seed.H*cp.H*probe*cp*seed)[0],1,'coherent-control positive interference')
    eq((seed.H*cm.H*probe*cm*seed)[0],-1,'coherent-control negative interference')
    # S charge 0/4 and R charge 0/4: neutral exchange is a joint operation.
    Q=s.diag(0,4);up=s.Matrix([[0,0],[1,0]]);down=up.H
    V=s.kronecker_product(up,down)+s.kronecker_product(down,up)
    QT=s.kronecker_product(Q,I)+s.kronecker_product(I,Q)
    eq(QT*V-V*QT,s.zeros(4),'joint charge transfer is neutral')
    theta=s.symbols('theta',real=True)
    psi=s.Matrix([0,s.cos(theta),-s.I*s.sin(theta),0])
    eq(QT*psi,4*psi,'joint reference history has fixed total charge four')
    eq((psi.H*psi)[0],1,'joint reference history normalized')
    eq(s.I*psi.diff(theta),V*psi,'joint reference history solves exact Schrodinger equation')
    eq(psi.subs(theta,0),s.Matrix([0,1,0,0]),'joint reference initial state')
    rho=psi*psi.H
    reduced=s.Matrix(2,2,lambda i,j:sum(rho[2*i+k,2*j+k] for k in range(2)))
    eq(reduced,s.diag(s.cos(theta)**2,s.sin(theta)**2),'orthogonal reference sectors remove reduced cross-charge coherence')
    isolated=s.Matrix([s.cos(theta),-s.I*s.sin(theta)])
    eq((isolated*isolated.H)[0,1]-reduced[0,1],s.I*s.sin(theta)*s.cos(theta),
       'joint neutral process is not isolated coherent number-breaking drive')
    print(json.dumps({'status':'PASS','exact_checks':len(checks),'checks':checks,
        'interpretation':'GNS theorem intact; marked coherent kernels are stronger data than channels without coherent branch control.',
        'native_resources_derived':False},indent=2,sort_keys=True))

if __name__=='__main__':main()
