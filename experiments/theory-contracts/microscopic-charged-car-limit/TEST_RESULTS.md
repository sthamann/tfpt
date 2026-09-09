# Verification record

Completed 2026-09-09 at 06:07:46 UTC. Full transcripts, Python version,
input/source references and new-artifact SHA256 values are in
[verification.json](verification.json). The recorded artifact hashes were
checked again against disk after the run.

| Suite | Normal | Python -OO |
|---|---:|---:|
| microscopic-neutral-limit | 11 PASS | 11 PASS |
| source-current-symbol-match | 9 PASS | 9 PASS |
| microscopic-energy-linearization | 10 PASS | 10 PASS |
| current-truncation-bridge | 13 PASS | 13 PASS |
| history-reference-transport | 11 PASS | 11 PASS |
| polarization-history-bridge | 14 PASS | 14 PASS |
| clock-interaction-provenance | 7 PASS | 7 PASS |
| current-fourpoint-limit | 15 PASS | 15 PASS |
| microscopic-fourpoint-limit | 12 PASS | 12 PASS |
| clock-rotor-joint-charge | 10 PASS | 10 PASS |
| **microscopic-charged-car-limit (new)** | **19 PASS** | **19 PASS** |
| **Total** | **131 PASS** | **131 PASS** |

All 22 isolated suite processes completed successfully. The new runner
reuses the pinned preceding ten-suite runner and appends this new suite;
none of the previous tests or sources was modified. Normal and -OO are
regression modes, not independent mathematical proofs.

## New diagnostic observations

For the fixed labels j=-1,0,1, the maximum observed errors are:

| N | Wrong raw vacuum occupation | Raw scaled generator error | Polarized scaled generator error |
|---:|---:|---:|---:|
| 32 | 3.43003e-4 | 0.153142 | 0.0125121 |
| 64 | 2.48427e-5 | 0.0766670 | 0.00313510 |
| 128 | 1.66237e-6 | 0.0383455 | 0.000784218 |
| 256 | 1.07329e-7 | 0.0191743 | 0.000196082 |

These float64 measurements check the formulas. The O(N^-4), O(N^-1),
O(N^-2) rates respectively follow from the written inequalities, not from
fitting this table. The full 16N-source polarization intertwiner residual
is at most 2.39e-15 on N=8,16,32; every occupied and empty bulk mode was
retained when constructing the original covariance.

The separate finite CAR matrix checks cover the entire 16-dimensional
four-mode Fock space, including particle/hole signs and relative charge.
The sparse excitation test uses original strip eigenmodes, not a substituted
effective Hamiltonian. A complex timed four-field word compares the full
source covariance with direct target CAR matrix multiplication, within
the independently evaluated telescoping bound.

## Known warning and evidence limits

The old source `seam_state_derivation_probe.py:366` emits its existing
ResourceWarning about an unclosed read handle in the two Clock regression
suites, in both interpreter modes. It is preserved in the transcripts;
no source edit or warning suppression was used to obtain PASS.

There is no independent mathematical review or proof-assistant certificate
for the new written proof in this round. The result remains a scoped local
research artifact, not full T2, T1--T8, a 3+1D theory, RH or TOE completion.
Paper, website, ledger and verification sources are unchanged.

## Reproduce

From the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
experiments/tfpt-discovery/.venv/bin/python \
experiments/theory-contracts/microscopic-charged-car-limit/checker.py \
--output experiments/theory-contracts/microscopic-charged-car-limit/diagnostics.json

PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
experiments/tfpt-discovery/.venv/bin/python \
experiments/theory-contracts/microscopic-charged-car-limit/run_verification.py \
--output experiments/theory-contracts/microscopic-charged-car-limit/verification.json
```
