"""Exact finite-energy arithmetic-state queries in the designated TFPT loop model.

Run without arguments for two concrete queries at K=50. The computation reports
state preparation size and energy; it does not simulate preparation or dynamics.
"""
import argparse
from fractions import Fraction
import json


def query(a, m, n, b, radius):
    if min(m,n) < 1 or radius < 1:
        raise ValueError('m,n and K must be positive integers')
    size=2*radius+1
    if m==n:
        count=(radius-b)//n-((-radius-b-1)//n) if a==b else 0
    elif (b-a) % (m-n):
        count=0
    else:
        q=(b-a)//(m-n)
        count=int(-radius <= n*q+b <= radius)
    value=Fraction(count,size)
    target=Fraction(1,n) if m==n and a==b else Fraction(0)
    return {'operation':{'a':a,'m':m,'n':n,'b':b},
            'meaning':'|n*q+b> maps to |m*q+a>; zero outside the input residue class',
            'finite_state_answer':str(value),'critical_state_answer':str(target),
            'exact_error':str(abs(value-target)),'proven_error_bound':str(Fraction(1,size))}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--K',type=int,default=50)
    parser.add_argument('--a',type=int,default=0)
    parser.add_argument('--m',type=int)
    parser.add_argument('--n',type=int)
    parser.add_argument('--b',type=int,default=0)
    args=parser.parse_args()
    if args.K<1:parser.error('K must be positive')
    if (args.m is None)!=(args.n is None):parser.error('Supply both m and n')
    words=[(0,4,4,0),(0,2,1,0)] if args.m is None else [(args.a,args.m,args.n,args.b)]
    result={'status':'EXACT_FINITE_STATE_QUERY',
            'state':'uniform mixture of W^k Omega_0 for -K <= k <= K',
            'K':args.K,'number_of_preparation_components':2*args.K+1,
            'kappa':'1/100','mean_electric_energy_neutral_plaquette':str(Fraction(args.K*(args.K+1),150)),
            'queries':[query(*w,args.K) for w in words],
            'scope':'Declared neutral loop model and fixed affine queries. No physical preparation performed, no replacement of electric dynamics by norm time, no RH or factoring solution.'}
    print(json.dumps(result,indent=2,ensure_ascii=False))


if __name__=='__main__':main()
