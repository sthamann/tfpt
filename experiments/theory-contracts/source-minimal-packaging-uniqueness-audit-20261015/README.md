# Eindeutigkeit der minimalen Verpackung: Quellen-Typisierung (15. Oktober 2026)

Status **PARTIAL**, keine Promotion. `python3 checker.py`: 24 Stellenpins, keine Modellrechnung.

* **U1:** 01:646–653 behauptet einen eindeutigen B_min. Der Beweis reduziert die Eindeutigkeit
  aber nur auf die nicht gelieferte Klassifikation des minimalen Stratums (01:587–593). Der
  zitierte „boundary reconstruction theorem“ existiert in den Auszügen nicht. Der vorhandene
  Rekonstruktionssatz (01:94–170) startet von einem gegebenen T_bound, das B_Σ enthält. Das ist
  Rekonstruktion, keine Eindeutigkeit. Ein Gegenbeispiel wird nicht behauptet.
* **U2:** Das Korollar 01:605–620 braucht, dass C_seed das minimale Stratum trifft. Dafür gibt
  es nur eine Beweisarchitektur (01:516–521).
* **U3 (enger gefasst):** Der fehlende Tupel-Slot beweist nichts. Vorhanden ist die
  OS-Rekonstruktion (A_loc, Θ, ω) ↦ (H_+, T_s); DHR kodiert die Sektoren im Netz. Es fehlen (G)
  T_s ↦ D_coll/D_+ und eine netzerhaltende Abbildung A_loc ↦ A_+. Sektorauswahl ist damit weder
  gezeigt noch ausgeschlossen.
* **U4:** Physical operationality (01:622–625) verlangt nur ein Objekt in Seed_op, keine
  Minimalität. Die Quelle räumt das ein (04_qft:2103–2109).
* **U5 (korrigiert):** Getrennt werden der positive Transferoperator U_Σ (06:16–25), der unitäre
  K¹-Repräsentant u_Σ und eine spektralflusstragende Familie (nicht angegeben). Ohne Familie ist
  SF dort nicht definiert. Einzige Verbindung: tfpt-42:7248–7253, Windung von arg det_adm U_Σ,
  ohne Familie. An den geprüften Stellen wird kein zulässiger SF = 1-Zeuge geliefert; das ist
  keine globale Nichtexistenzaussage.
* **Vorbestand:** source-three-route-closure SELECTION.md (bedingt K/G) und
  source-boundary-lift-selection §1/§3 (Nullordnung, Domäne, Kato–Rellich-Reparatur).

Details: `PROOF.md`.
