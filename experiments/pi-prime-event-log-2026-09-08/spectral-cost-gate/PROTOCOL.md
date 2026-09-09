# Frozen protocol: exact periodic events and their computational cost

Written before generating this experiment's inputs or running its benchmarks, 2026-09-08.

Question: Does an explicit finite Fourier reconstruction reduce total work relative to a sparse modular-root sieve when both encode exactly the same divisibility events? This is a cost experiment, not a further digit-pattern search or an RH test.

For each public semiprime N, a=ceil(sqrt(N)), Q_j=(a+j)^2-N, 0<=j<65536. For eligible factor-base primes p<=43 and powers q=p^k<=4096, multiply S_j by p whenever q divides Q_j. Rank the exact integers R_j=Q_j/S_j, breaking ties by j, and select 16384 candidates. Truncation at q=4096 is deliberate and differs from the previous arithmetic gate's unbounded removal of small-prime powers.

Three implementations:

1. `direct_mod`: dense integer divisibility tests Q_j modulo every q.
2. `root_stride`: enumerate small modular roots and lift them exhaustively, including p=2; update only the corresponding arithmetic progressions of j.
3. `fourier_fft`: use the SAME modular roots as root_stride to construct Fourier coefficients C_k=sum_s exp(-2*pi*i*k*s/q), s=(root-a) mod q; reconstruct each full period with inverse FFT, round to a binary mask, and repeat the mask across the pool. Integer phase reduction precedes floating point exponentiation. Reject residuals above 1e-10, imaginary residuals above 1e-10, and nonbinary rounding. No exact-mask fallback repairs the FFT output.

All methods must give identical full R arrays, selected offsets, smooth relations, rank, and factor certificates. This equality is checked outside the timed region. Runtime uses N only, never the answer key. Small root generation is charged to the two methods needing it; no shared N-dependent cache. The unchanged relation-gate engine (SHA256 9e8d72b9e6d91f4e64808ecf3b03939a6889552d1f976acd9480a28c2d22b54d) supplies eligible factor bases (bounds 200/500/1200/2500), exact screening, binary elimination, and congruence/gcd checks. Full budget continues after the first factor.

128 fresh, distinct, balanced, actual 32/40/48/56-bit semiprimes: 16 per size per cohort, seeds 202609083301 and 202609083302, excluding all three preceding fixture sets. Separate public inputs and answer key. Five complete repetitions for every method/input, rotating method order by input and repetition. No outcome-dependent parameter tuning. Report sum of per-input median full runtimes and selection times by cohort and bit size, paired bootstrap 95% intervals for runtime ratios (19999 resamples, seed 202609083399). Intervals describe this benchmark's fixture variation, not hardware-independent uncertainty.

An FFT cost advantage requires at least 2x full-pipeline speed versus root_stride in BOTH cohorts, lower bootstrap bounds above 1, and no mismatched results. Any selector-only speed advantage must not be called full factorization speed. Performance is local Python/NumPy evidence and excludes common interpreter/import overhead and diagnostic serialization, but includes per-N factor-base setup, selection setup and evaluation, sorting, exact screen, precision guards, elimination and gcd checks. Report complete batch wall time separately. Allocation costs are included in timers; peak process memory is descriptive and shared across methods.

Additional prespecified scale check: first validation input at each bit size, pools 65536/262144/1048576, select one quarter, five selector repetitions in rotating order. Check exact equality; measure selectors only, not factorization at these larger pools. Include prime-root setup. These are illustrative scaling samples, not a separate success gate.

Independent audit: brute-force all residues for root lifting and Fourier masks on small nonsquare odd composites; independently reconstruct saved square products and gcd certificates against the separately generated answer key. No result implies a universal no-go theorem or a new factoring algorithm. The existing r644 `regulator_relation_probe.py` already implements lifted modular roots and stride updates: improved sieve costs here would be a classical implementation result.

Sources: [DLMF 27.10](https://dlmf.nist.gov/27.10), [NumPy inverse FFT](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft.html). The finite Fourier representation is classical; its use of pi does not expose decimal digits of pi as factor information.
