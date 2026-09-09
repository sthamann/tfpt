# Execution record

2026-09-08. All times below are unittest-reported wall times on this host.

| Suite | Tests | Normal | `-OO` | Result |
|---|---:|---:|---:|---|
| New parent-selection audit | 15 | 1.046 s | 1.083 s | PASS / PASS |
| Existing plaquette-gap-certificate | 16 | 0.725 s | 0.727 s | PASS / PASS |
| Existing ground-state-loop-response | 14 | 1.501 s | 1.501 s | PASS / PASS |

45 tests per mode, not 45 TOE obligations. The new complete-record replay
and inherited source pins pass. The original modules were not modified.
The eight directly pinned files include the current TOE ledger; the original
Round37 input chain is also validated. Broader prior suites and long Round50
executions were not rerun in this targeted audit.

The first checker execution completed its mathematical checks but could not
save its JSON because the repo is outside the launcher write sandbox. The
same scoped command was then authorized and saved the result successfully.
There was no scientific test failure or need to weaken an assertion.

Validation SHA-256:
`5825b4581b97d36d6d33bdd51f910264f32e197a5b9b50c2ce407b0c9af3db56`

There is no proof-assistant certificate, independent external peer review,
interacting phase computation, selected TFPT Hamiltonian, or TOE closure.
The rational/symbolic tests check the analytic derivations and source match
documented in README.md. This execution record is descriptive metadata and
is not part of the validation JSON's three source-file hashes.
