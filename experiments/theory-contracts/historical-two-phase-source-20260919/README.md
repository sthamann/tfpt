# Historical two-phase source contract — 2026-09-19

This is an `experiments` theory contract. It registers the historical
`a_top != a_QCD` distinction and the exact rank-one necessary condition for a
photon-active QCD-flat direction. The same-field energy bound applies only to
the declared local same-well identification and therefore does not refute the
historical two-field TFPT branch.

The checker is a copied reproduction of the scoped source calculation. Run:

```bash
python3 -B check_joint_constraints.py
```

Expected result: 17/17 checks pass (13 symbolic, 4 numerical controls), with
`verdict=PARTIAL`. The contract is firewall-only: no ledger promotion, no
closed gates, no T1--T8 closure, and no new claim IDs. See [PROOF.txt](PROOF.txt),
[joint_constraints.json](joint_constraints.json), and the pinned evidence in
[source_manifest.json](source_manifest.json) and [sources/EXCERPTS.md](sources/EXCERPTS.md).
