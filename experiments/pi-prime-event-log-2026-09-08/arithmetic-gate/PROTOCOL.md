# Arithmetic-conditioned pi test and phase-filter audit

2026-09-08. Frozen before fresh inputs/outcomes, continuing user-authorized research.
Scope: one arithmetic-conditioned digit rule plus a specified finite phase approximation.
Do not reinterpret success of classical sieving as pi-digit information or RH positivity.

Classical identity: P_q(Q)=(1/q)sum_{k=0}^{q-1}exp(2 pi i k Q/q) equals
1_{q divides Q}. It follows from a finite geometric series. Consequently full
phase data contains precisely the divisibility predicate already available by mod.

Runtime receives only N, selected fixed method and optional constant digit prefix.
Reuse verified relation screen/combine from ../relation-gate/engine.py with pinned hash.
No modifications to the earlier experiment. Same full factor-base bounds by bit length,
M=65536 candidate offsets, K=16384 full screenings, exact certificates, all-budget policy.

Compute all Q_j=(ceil sqrt N+j)^2-N in the M-pool. Cheap classical information:
remove ALL powers of eligible primes <=43 from each Q to obtain cofactor R_j.
This scans the full pool and is charged to selection cost; it is not free prefiltering.
No large-prime/full-smoothness result is computed before candidate selection.

New pi rule: order by (bit_length(R_j), pi eight-digit key_j, j). Eight-digit
keys use the previously defined address (N mod 2Mdigits +8j) mod 2Mdigits. The
bit-length bucket is fixed now, not fit to observed successes. It discards some
known information; compare both matched bucket controls and an unquantized baseline.
Matched controls use e, sqrt2, five random key streams in the same bucket. Additional
arithmetic baseline sorts by exact (R_j,j); sequential baseline uses j=0..K-1.

Phase approximation: for each eligible p<=43 and each q=p^a<=4096 define
F_8(r/q)=|sum_{k=0}^8 exp(2 pi i k r/q)/9|². Score
sum_{q=p^a} log(p) F_8((Q mod q)/q) - log(Q); highest first, ties increasing j.
Finite lookup tables computed and charged within selection. This is a normalized
Fejer-type filter, NOT the exact full Fourier projector, and not an RH test.
All remainder reductions done in exact integers before floating phase evaluation.
Independent higher-precision reconstruction tests ordering sensitivity on selected inputs.

Eleven methods total: sequential, exact_cofactor, phase8, bucket_pi, bucket_e,
bucket_sqrt2, bucket_random0..4. 128 new unique balanced semiprimes with exact
32/40/48/56 bits, 16 per size per split. Seeds 202609082201 / 202609082202;
exclude previous direct-gcd and relation-gate N. Public N/answer separation retained.

Primary digital comparisons: bucket_pi smooth-count per K vs mean of five matched
random buckets and vs exact_cofactor, in each split. One-sided paired sign flips
19999 replicates, Holm across four tests; state symmetry assumptions. A pi-digit
candidate must win all four corrected comparisons with p<.05, reach 2x validation
independent-rank per full amortized cost vs both and not reduce factor successes.

Phase8 comparisons are separately exploratory: report all outcomes/costs vs
exact_cofactor and sequential; no post-hoc optimized phase width or power cutoff.
All input types are diagnostic, not practical RSA sizes; costs include full-pool
selection, source generation/load, exact screen, elimination and gcd. No claim
of best QS/NFS baseline, regulator recovery, normality, or universal no-go.
