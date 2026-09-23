"""Exact local-observable boundary-response tests for chosen Bell chains.

NON-RH. General locality proof in README.md. Finite tests do not establish
a thermodynamic limit by extrapolation; that uses a separate standard theorem.
"""
import json
import sympy as s


def require(ok, message):
    if not ok:
        raise ValueError(message)


def identity(n):
    return s.SparseMatrix.eye(n)


def kron(*args):
    return s.SparseMatrix(s.kronecker_product(*args))


def chain(n,d):
    phi=s.SparseMatrix(d*d,1,{(a*d+a,0):1 for a in range(d)})
    pair=phi*phi.T/d
    out=(n-1)*identity(d**n)
    for j in range(n-1):
        out-=kron(identity(d**j),pair,identity(d**(n-j-2)))
    return out


def comm(h,a):
    return h*a-a*h


def finite(n,d):
    small=chain(n,d)
    large=chain(n+2,d)
    x=s.SparseMatrix.eye(d)
    x[0,0]=x[1,1]=0
    x[0,1]=x[1,0]=1
    a_small=kron(x,identity(d**(n-1)))
    a_large=kron(a_small,identity(d*d))
    first=None
    for k in range(n+1):
        difference=a_large-kron(a_small,identity(d*d))
        if k<n:
            require(difference==s.SparseMatrix.zeros(d**(n+2)),
                    'remote boundary cannot appear before nested commutator reaches it')
        else:
            require(difference!=s.SparseMatrix.zeros(d**(n+2)),
                    'negative control: boundary is not absent forever')
            norm=sum(s.conjugate(v)*v for v in difference.values())/d**(n+2)
            require(norm>0,'exact nonzero boundary-response witness')
            first=k
        if k<n:
            a_small=comm(small,a_small)
            a_large=comm(large,a_large)
    return {'old_length':n,'new_length':n+2,'d':d,
            'first_changed_commutator_order':first,
            'normalized_squared_Hilbert_Schmidt_difference':str(norm)}


def main():
    cases=[finite(3,2),finite(5,2),finite(3,3),finite(3,4)]
    print(json.dumps({'scope':'NON-RH exact finite local response',
        'cases':cases,'exact_finite_volume_dynamics_embedding':False,
        'infinite_limit_inferred_from_tests':False,'T1_T8_closed':[]},sort_keys=True))


if __name__=='__main__':
    main()
