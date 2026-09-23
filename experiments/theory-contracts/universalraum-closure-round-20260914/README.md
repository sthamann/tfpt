# universalraum-closure-round-20260914

Closure round on the Universalraum consolidation state of 2026-09-14
(`universal_room/TFPT_Universalraum_Gesamtkonstrukt_2026-09-14.md`,
`universal_room/Konsolidierte_Fortsetzung.md`). Everything here is
experiment-side (firewall): no promotion, no ledger, no RH/TOE claim.

## Checkers and results

| Script | Checks | Content | Result file |
|---|---|---|---|
| `coherence_audit.py` | 16/16 | Exact vertex coherence: K†K = I−S, ordered-history rank rise 6→12, η-interpolation, U_W unitary (symbolic), H_22 spectrum, H_bad ground spaces (24 / 108), Clebsch label structure (40 edges / 10 labels / 4 each, 4-cycle pairing uniqueness), local symmetry mechanism (hᵢ = hⱼ + cI) | `coherence_audit.json` |
| `dressed_star.py` | 16/16 | Dressed microscopic 4-star: exact spectrum E(g) = (Δ−√(Δ²+4t²(6−2g)))/2, gap 0.00243396875137 (≠ bare J/2), dressed-ground bare weight 0.9856429311786321, rephase error at bare filter time 0.2746 rad, corrected degree-7 filter projects exactly (error 2.4e-14) | `dressed_star.json` |
| `selection_principle.py` | 15/15 | T1-micro: exact anchors (B²=4I+3J₁₅, CCᵀ=4I, FFᵀ=12I, CFᵀ=0, rank T=30, spectrum); H_C max at a=1/7 vs H_R max at a=1/13 (symbolic, unique); R = 14T−2I is a 12-regular ray adjacency with spec {12,4¹⁵,2⁹,−2³⁰,−6⁵}; COMPLETE exceptional set in [0,1]: rank 30 at a=1/7, rank 55 at a=1/3, else 60 | `selection_principle.json` |
| `weil_bridge_probe.py` | 12/12 | Beilage-E requirements measured on the real L* object (z=16, S=367, N_w=184): wall reproduced (0.99983248 / 1.00003660); Q_n = I−BₙᵀBₙ PSD to half-filling, fails one degree past; removing archimedean lags explodes λ_max to ~1.6e49 (boundary terms ARE the contraction); image condition exact (consistent defect 1.8e-11 vs foreign 0.56, indefinite for every diagonal c); Cholesky factor reconstructs Q₁₈₄ to 5.6e-16 but cannot extend | `weil_bridge_probe.json` |
| `nonsinglet_sectors.py` | 64/64 sectors | Full SU(4) sector decomposition of the C16 Clebsch exchange Hamiltonian: completeness Σ d_λ f_λ = 4¹⁶ exact; singlet anchor 11.045398337068 reproduced to 8.9e-15; **singlet IS the global ground state**; lowest non-singlet sector (5,4,4,3) at 12.133537149348 (gap 1.088138812280 J); full model gap 0.516363785734 J (singlet quartet) | `nonsinglet_sectors.json` (+ `nonsinglet_sectors_partial.json` during the run) |

## Conventions

- No original research code imported; all objects rebuilt from definitions.
  `weil_bridge_probe.py` imports only the standalone document builders of
  `rh/problem/verify_lstar_instance.py` (read-only use of the L* definition).
- Every checker aborts with an error on the first failed criterion; normal
  and `-OO` runs are intended to be byte-identical.
- Scope: exact finite linear algebra / symbolic checks + controlled double
  precision Lanczos (residuals reported per sector). Not interval-certified;
  no CAR/native-phase identification; no thermodynamic limit; NO RH CLAIM.

## User-facing summary

`~/Documents/TFPT_UNIVERSALRAUM_ERGEBNISSE_2026-09-14.md` (German, with the
updated open-problem map for goals a/b/c).
