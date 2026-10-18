# TFPT verification

After the 2026-10-18 ownership split this project registers **707 modules** and maintains **788 ledger rows**. These are source counts, not a count of independent proofs.

TFPT retains physical compiler verification and the generic mathematical kernels actually consumed by it. Riemann–Hilbert flat-bundle modules v32/v33 remain because they concern the TFPT family connection, not the Riemann hypothesis.

Run from the repository root:

```sh
python3 verification/run_all.py
python3 verification/run_all.py --shard 1/6
python3 verification/make_script_index.py
python3 verification/audit_sync.py
```

Each registered module can also run directly. Install the repository requirements first; a subset of original modules needs experimental sources at the preserved relative paths. `run_all.py` executes the stated module checks and returns nonzero on a failed check. `audit_sync.py` checks source/registry/generated-surface consistency and executes no Lean proof. A full numerical suite and a fresh Lean build are separate operations.

Single sources: `script_registry.csv` (module index), `script_clusters.csv` (group metadata), `status_ledger.csv` (claim status). Generated indices must be regenerated through `make_script_index.py`. The original mathematical scopes, honest negative patterns, open hypotheses and historical module IDs remain authoritative.

An executed finite check does not establish the Riemann hypothesis or complete a physical field theory.
