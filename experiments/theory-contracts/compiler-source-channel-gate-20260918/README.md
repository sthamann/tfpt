# Actual source channel gate and marked clock dictionary

Research ID: `UR.COMPILER.SOURCE_CHANNEL_GATE.07`. Verdict: **PARTIAL**.

The original one-copy QWZ strip has one complex chiral channel per edge.
Its 256 transverse bilinear matrix units have a leading top-edge current
Gram of rank one. The eight rows cannot substitute for the independent
copies used by the older rank-eight E8 realization. This is a result about
the specified free source and its established scaling limit.

The numerical identification `16 Majorana copies = dim S+` is also checked
against the native compact Spin10 action. The complex half-spinor cannot be
a real 16-dimensional vector. The correct `10+6` real-vector dictionary was
already present in v113 and is retained, with its local-source premise open.

The marked geometric seam deck is exactly `T=G^2 A` on the full E8 charge
lattice: the square of the pre-existing glue clock times the marked family
rotation. The known half-twist/charge-carry and index-two D8 extension facts
are inherited, not new results.

Read `PROOF.txt`, `certificate.json` and `replay.json`.

```sh
python3 -B checker.py --out /tmp/tfpt-source-channel-normal
python3 -B -OO checker.py --out /tmp/tfpt-source-channel-optimized
```

Dependencies: Python 3, NumPy, SymPy. Source hashes and the adapter's
transitive pins are validated. Checks do not rely on Python assertions.
Firewall: experiments. No physical gate, publication or empirical promotion.
