# Frozen protocol — 2026-09-08

Written before computing the new outcomes. Exploratory research, no RH or factoring claim.
Decimal indexing is one based AFTER the decimal point. Leading zeros are retained.
Primary interpretation: B_p = digits[p-1:2*p-1], exactly p digits starting at p.
Secondary interpretation: C_p = digits[p-1:p-1+len(str(p))].

Generate 2,000,000 decimals of pi, e and sqrt(2) with MPFR, repeat pi at increased
precision, independently compare the first million to the Angio published file.
Discovery position range 2..250000; validation 600001..1000000 (prime starts).
Thus the full length-p blocks occupy disjoint digit ranges, at most 1..499999
and 600001..1999999. Fixed-window tests use the same starts and ranges.
The small historical prefix is not new data; the later disjoint range is the
prospective internal replication. Pi itself is deterministic: random nulls are
models for comparisons, not a theorem of normality or independence of pi.

Freeze metrics per range: prime-position digit mean and digit chi-square;
chi(-4) digit contrast; next-prime-gap vs digit; normalized length-p block mean
and mean square; length-p sum residues mod 3 and mod 9; C_p divisible by p;
C_p itself prime; six-digit extracted integer prime; six-digit values at prime
positions vs values at all positions (rate difference); reverse correlation
of chi(-4) of a six-digit prime value and of its prime position; self-locating
strings at all positions and at prime positions. No after-the-fact metric search.
All integer primality here is exact within a sieve up to 10^7.

Calibrate the whole extraction pipeline on 999 independent uniform decimal
streams using the exact same positions, overlapping windows, zero handling and
statistics. Two-sided Monte Carlo inclusive equal-tail rank p values (twice the smaller tail),
add-one rule, capped at one. This implementation detail was made explicit before
the first outcome run; it also handles asymmetric and discrete statistics.
Apply Holm across BOTH ranges and all primary metrics together. Report all
metrics, including negatives. Compare e and sqrt(2) descriptively with same nulls.
A discovery needs corrected p<.05 AND same-direction nominal p<.05 in disjoint
validation; even this is a candidate for an independently enlarged sample.
Include planted prime-digit signal and its detector result as positive control.

Reverse named-sequence catalog fixed now: all ten sixfold repetitions,
123456, 654321, 0123456789, 9876543210, 314159, 271828, 161803, 235711,
112358, 16470, 44899, 424242, and theory integers 240, 480, 1024, 65536,
1048576. Retrieve all overlapping matches, first position, prime status and
factorization of first position. Test prime-position enrichment by 9999 random
circular shifts of the position-prime mask, preserving sequence occurrence
spacing, Holm across this catalog. Named strings were chosen from pi folklore
or project history, hence historical selection bias is NOT eliminated by Holm.
No-hit strings are right-censored, never evidence of absence in infinite pi.

Reconstruct self-locating strings and first-occurrence chains (start 169 and 211),
with finite search bounds. Cycles of a finite lookup map are descriptive.
Factorization bridge: frozen 200 semiprimes, 16..24 bits, generator seed
2026090802 independent of digit seed. Try 32 six-digit pi-derived gcd candidates
at positions computed ONLY from N, compare identical e/sqrt2 and 999 uniform
six-digit candidate streams. Include digit generation in cost accounting; this
is a bounded factor-information screen, not an implementation of the regulator
algorithm or a complexity result. Report small-factor and modular structural
confounds. Factor values are confined to fixture generation and scoring.

## Audit amendment after the preliminary 999-run results

The first outcome scan had no primary pi p below .064. A design audit found
that 999 draws give a two-sided minimum p=.002, hence the 30-test Holm floor
is .06: even a perfect signal cannot pass the declared family threshold.
A failing regression reproduced this. Increase the primary draws to 1999
(same seed, the original first 999 are retained identically); floor is now .03.
No metric, position range or threshold changed. Preliminary results are retained.
This is an internal prospective split, not an external preregistration.

The factor-screen null initially sampled independent six-digit integers. The
final null instead generates full uniform digit streams and uses the exact
N-derived extraction addresses, preserving duplicate N and overlapping digit
reads just as in pi. The first result is retained as preliminary. Constant-digit
positive control makes gap correlation undefined; assign zero ONLY in that
zero-variance case, without treating it as evidence. All actual data and random
streams have positive variance. These changes do not tune a pi signal.

A subsequent source audit corrected chi_4(2) from the generic non-1-mod-4
branch (-1) to its exact value zero in the reverse character diagnostic.
All final null draws and observed statistics were rerun with this correction.
