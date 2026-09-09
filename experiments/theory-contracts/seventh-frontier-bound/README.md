# Complete grade-seven source: conditional cubic ideal-error bound

2026-09-08. **NON-RH, original conditional parent, local theory experiment.**

This derives a positive, volume-independent ideal-error budget for the
FORMAL source Z49 plus all twelve electric words of weighted degree seven,
where M has weight one and E has weight two. It does not evaluate their
complete combined cubic amplitude. No old probability is reused, no
occupation interval is produced, and the separate numerical configuration
error is not part of the ideal bound. The physical edge construction is
pinned through `third-electric-cubic` and `seventh-frontier-edge`.

At T=1 the formal upgraded bound is **7.400313083220603e-7**, compared
with the old Round49 ideal bound 2.9183911450664386e-6. Its positive
partition is 6.880370706606023e-7 from the newly continued boundaries,
1.347809920385205e-8 from retained explicit degree-eight boundaries, and
3.85161384576059e-8 from first E after at least six M events. The last
part includes the nonzero infinite-tail bound 4.475665868270932e-15.
These are bounds for different source targets, not two error bars around
the same unchanged numerical column.

## Source and boundary partition

The twelve additions are MEMMMM, MMEMMM, MMMEMM, MEEE, MEEMM, MEMEM,
MMEEM, MEMME, MMEME, MMMEE, MMMMEM and MMMMME. These are actual original
operator-source definitions, using the already checked M/E recursions;
some complete cubic sums have not been executed. Every new word p has
two outgoing remainders pM and pE. The seven older boundary words retained
are pME for p in {MEMM,MMEM,MMME,MEE}, and pE for p in {MMMME,MEME,MMEE}.
All first-E-after-q-M branches with q>=6 are also retained, including the
infinite tail after level twelve. The boundary languages are disjoint.

Equivalently, all 26 electric words of degree at most seven are evaluated
by the formal ideal source, along with the resummed pure-M branch. There
are 31 finite first-omitted boundary words; every subsequent word starts
with exactly one of those, or has its first E after at least six M events.
The independent language test checks this partition beyond the retained
orders, not just the names of the new twelve words.

The code reconstructs the complete Round49 bound as a sum of positive
terms BEFORE replacing anything. It then checks a second exact identity:
old bound = all removed degree-seven terms + all retained terms. No
unassigned residual is discarded through subtraction.

## Matter transport, all literal legs retained

For old arity d and positive species tensors a,b,f (simplex moment,
phase-gradient moment, final-current-length moment), the original rows give

  W=[[53/96,1/4],[1/4,0]], J=[[29/48,1/4],[1/4,0]].

Let S_W and S_J be their d-leg Kronecker sums. Appending M gives

  a'=S_W a,
  f'<=S_W f+S_J a,
  b'<=S_W(b+f)+S_J a.

Old difference vectors acquire a last zero. Consequently the extra last
simplex interval contributes exactly its current length times a, while
the triangle inequality bounds the changed length. These formulas apply
to all three or five literal legs, not just annihilator legs. They are
used twice on the pinned Round48 full-operator moments. Entire zero CAR
words can be omitted before the commutator because [V,0]=0. Zero action
on the selected preparation is not a valid omission rule.

Round49 stored only CAR species marginals c=(c_L,c_H), not full tensors.
For those two families define A=sum(c)/d, A_C=c dot C,
C=(sqrt(107/2048),sqrt(1/96)), mu=77/96, nu=41/48, and Lmax=2n-1.
A conservative one-M continuation is

  A_C' <= mu(d-1) A_C + c dot (W C),
  B' <= d mu (B+Lmax A)+d nu A.

For the first term, sum each replaced leg's new C exactly and bound the
row norm multiplying the other d-1 legs by mu. The second is the tensor
formula above with f<=Lmax A and row sums bounded by d mu,d nu.
No nonexistent full tensor is reconstructed from the two marginals.

## Electric transport and first E after five M events

The pinned third-electric experiment supplies the measured full MEEE
moments and the positive E-transport theorem for the three other new-E
leaves. Its seven-leg CAR bound keeps the fourth-E outgoing remainder.

For first E after five M events, the old k=0 polynomial moment is 1 and
its gradient moment is sum_i L_i. The inherited full-cubic matter hierarchy
provides an upper bound for that sum, resolved by species. The same
link-incidence proof as in the third-electric experiment yields

  a'_(alpha,beta,s) <= F_(alpha,beta) b_s,
  b'_(alpha,beta,s) <= (43 F_(alpha,beta)+G_(alpha,beta)) b_s,
  F=[[29/144,1/12],[1/12,0]], G=[[17/72,1/12],[1/12,0]].

Here 43=5²+2(2*5-1), from L_i<=2i-1. Tests compare these moments with
actual original fifth-level first-E paths, not just a symbolic matrix.

## What the bound establishes, conditionally

For every newly added degree-seven source with k electric events,

  R_pM <= kappa^k A_C T8/8!,
  R_pE <= kappa^(k+1) (53/288) B T9/9!, kappa=1/100.

Together with the retained degree-eight branches and the entire remaining
first-E tail, these give an O(T8) ideal budget on |T|<=1. The outer
remainder is propagated by the full physical H, so all later M/E events
remain present. This uses the inherited strong-dynamics and E0-domain
assumptions; it does NOT construct the infinite-volume dynamics or prove
all-E convergence. Exact finite-edge jets are an independent consistency
check, not the proof of the full-cubic norm bound.

The bound applies only after all twelve sources are included in the
mathematical target. Applying it to Z49 or the partial Round50 source
would be incorrect. The numerical Round44 configuration error can begin
at a lower time order and must be added separately after the changed
combined column is actually evaluated.

### Independent finite-time physical matrix check

`edge_time_check.py` constructs all 26 electric words independently as a
prefix tree on the original physical edge, with 14492 total raw paths,
and reproduces all twelve pinned grade-seven raw counts. It evaluates
the complete source at T=1, including its resummed pure-M part, on all
four E0 inputs in the original neutral-six/charged-four sectors. It also
evaluates exp(i H_Q)c_H,0 exp(-i H_N) directly from the two physical
Hamiltonians. No two-level or auxiliary matter-only substitute is used
for the latter calculation.

The exact rational matrices are stored in `edge-time-validation.json`.
The Frobenius bound for their difference, with all scalar, source and
Hamilton-polynomial numerical errors included, is 8.4480691969e-14.
The numerical part is bounded by 2e-24 at the stored outward precision.
Thus the entire E0 operator, including arbitrary coherent inputs, passes
this FINITE-edge check. The small edge error is not a new cubic error
estimate and does not replace the full-cubic derivation above.

## Reproduction and scope

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/seventh-frontier-bound/checker.py --output experiments/theory-contracts/seventh-frontier-bound/validation.json
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/seventh-frontier-bound/edge_time_check.py --output experiments/theory-contracts/seventh-frontier-bound/edge-time-validation.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/seventh-frontier-bound -p 'test_*.py'
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/seventh-frontier-bound -p 'test_*.py'
```

Result values, all positive moment bounds and source hashes are in the
record. This is a conditional mathematical research certificate, not
empirical confirmation or a proof-assistant certificate. T1-T8, dynamical
parameter/preparation selection, the chiral continuum and universal spin
two remain open. No paper/website/ledger/verification/scorecard changes,
commit or push are included.
