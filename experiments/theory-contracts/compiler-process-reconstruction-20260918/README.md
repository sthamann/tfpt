# Restart from the original marked operations

`UR.COMPILER.PROCESS_RECONSTRUCTION.08`, verdict **PARTIAL**.

The original marked Gaussian E8 matrix-order bridge gives 60 root rays:
24 one-qubit Clifford operations and 36 rank-one Pauli input/output pairs.
All 3,600 pair compositions close projectively, including the retained
complex amplitude or zero. Choi state encoding and the Lorentz-cone map
respect the same composition. This integrates existing algebraic source
structures; it does not derive a common physical execution law.

The simplest uniform instrument, with its outcome discarded, is exactly
completely depolarizing and cannot injectively intertwine the original
TFPT transport with eigenvalues 1, 2/3, 1/3. The uniform candidate is stopped
at this discriminating test. No new physical Hamiltonian is introduced.

Read `PROOF.txt`, `certificate.json` and `replay.json`.

```sh
python3 -B checker.py --out /tmp/tfpt-process-normal
python3 -B -OO checker.py --out /tmp/tfpt-process-optimized
```

Python 3, SymPy and the inherited source adapter (NumPy) are required.
Pinned sources and transitive guards are checked; own checks use explicit
exceptions. Only research output is written. No original verification,
ledger, paper, website or empirical scorecard promotion; no physical gate.

T1–T8 bleiben offen. Die physikalische Ausfuehrungsregel ist nicht hergeleitet.
