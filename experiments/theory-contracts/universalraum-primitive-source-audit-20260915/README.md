# Primitive-source audit — 15 September 2026

User-requested restart from distinctions, composition and consistency. This
branch does not extend the old Fock mechanism and does not promote TOE claims.

- [Research report and proofs](RESULTS.md)
- [One-page reconstruction kernel](EINSEITER.md)
- [Exact finite witnesses](checker.py)
- [Normal results](normal.json)
- [Optimized results](optimized.json)

Run from this directory:

```sh
python3 -B checker.py --output normal.json
python3 -B -OO checker.py --output optimized.json
cmp normal.json optimized.json
```

The script needs SymPy and NumPy. It pins the original native W and hashes
the attachment and selected local sources before and after testing. Other
papers, ledgers and experiments are not rewritten. Finite checks illustrate
the written general proofs; their count is not a count of independent results.

This is a **partial mathematical result**: a minimal observable reconstruction
and exact sufficiency/non-uniqueness tests, not a uniquely derived primitive
physical source and not an impossibility theorem for every common source.
