# Statistiktransport durch den Halbstring der Quelle (15. Oktober 2026)

Status: **PARTIAL**, keine Promotion. `python3 checker.py`: 144 Prüfungen
(Struktur exakt, Zahlen mit Gleitkomma-Toleranz) am unveränderten
`v988_psi_lambda_reduction.py:75–96`.

Die erste vorhandene Quellformel ist der Halbstring `D = (Viertelphasen-String)²`
(`half-twist-grade-carry`, §4). Am Originaloperator:

* `D H_r D = H_{r+2} − RD`, R nur am fernen Bogenende, `‖R‖ = 2`, `rank R = 2N_y`.
  Sektorwechsel r → r+2, also α = ¼ ↔ ¾.
* Fock-Lift `Γ = (−1)^{N_Bogen}`: fermionischer Erzeuger `c_x → −c_x` auf dem Bogen;
  bosonischer Bilinear `c_x†c_y → χ(x)χ(y) c_x†c_y`; Zeit
  `Γ dΓ(H_r) Γ = dΓ(H_{r+2}) − dΓ(RD)`.
* Monodromie −1 = `exp(2πi v·s)` mit dem Quellfermion, wie für den Spinorsektor nötig.

Nicht geliefert: das Feld endlicher Energie (Vakuumüberschuss des scharfen Strings,
bulkkorrigierter Halbstring mit Carry U_s offen) und eine Calderón-Formel. Details:
`PROOF.md`.
