# Pi/N relation gate — frozen before new benchmark results

2026-09-08; follow-up authorized by user. One concrete rule, no tuning across rules.
No RH claim and no claim that pi supplies a regulator. Test useful congruences instead.

For input odd nonsquare N, let a=ceil(sqrt(N)), M=65536, K=16384. Candidate offset
j in 0..M-1 represents x=a+j and Q=x^2-N. Read an 8-digit key from the verified
2M-digit pi prefix, at zero-based address (N mod 2M + 8j) mod 2M, wrapping.
Stable-sort offsets by keys; take first K. Leading zeros and key ties retained.
Keys determine ordering only; no Q-smoothness or factors used before selection.

Check Q exactly for B-smoothness using the eligible quadratic-residue prime base.
B=200,500,1200,2500 for actual N bit-lengths 32,40,48,56. Binary exponent Gaussian
elimination yields square dependencies. Verify every congruence X²=Y² mod N,
then gcd(X-Y,N) and gcd(X+Y,N). Continue through the complete K-candidate budget,
including after a factor is found; record first-factor index separately. Only
fundamental dependencies produced by this fixed elimination order are tried;
no exhaustive dependency-combination search and no large-prime variant.

Controls: same digit-key ordering from e and sqrt2; five random 8-digit-key
orderings with seeds fixed from N and control index; classical sequential first K.
All share precisely the same candidate pool, eligible factor base, exact arithmetic,
linear algebra and stopping rules. Digit sources are 2M finite prefixes, not
unbounded oracles. Full key decoding, all M keys sorted, exact candidate screening,
linear algebra and factor extraction timed. Precompute-pi generation cost from the
verified earlier run counted once, plus read/hash cost: report both corpus-amortized
and per-input cold-generation total costs. Comparisons concern these implementations,
not state-of-the-art QS/NFS, universal lower bounds or cryptographic-size factoring.

128 NEW distinct balanced semiprimes, 16 per bit size per split, exact N bit length,
p != q, deterministic next-prime fixture generation. Separate discovery seed
202609081101 and validation seed 202609081102; forbid every N from the previous
factor screen. Runtime is a separate script reading ONLY public N list and digit files;
answer-key file read only by independent verification after outputs exist.

Primary endpoint: number of fully smooth distinct accepted relations per K calls.
Paired comparisons pi vs mean of five random controls, and pi vs sequential.
One-sided sign-flip tests of mean per-N relation-yield differences, 19999 flips;
report the symmetry/exchangeability assumption and full individual rows.
Holm over four comparisons (two controls x two fixed splits). Candidate requires
positive difference and corrected p<.05 in both splits against BOTH controls,
and at least 2x independent relation rank per measured total cost in validation
against both. Require no worsening of factor-success count. Exact congruences
and factors alone validate the classical machinery, not pi specificity.

Descriptive endpoints: rank, dependency count, successful proper congruences,
factor-success rate by bit size and split, first factor candidate index, cost,
smooth yield per 1000 candidates and rank per second. Include all failures and
resource caps. No parameter extension because of poor results. Weak power/finite
scope explicitly reported. This is an internal frozen plan, not external preregistration.
