# Gemeinsamer Identifikationstest Träger ↔ Familie an den Originalen

Frage (Codex): Gibt das Original einen wirklichen Collar → SU(4)/SU(3)-Operatortransport
oder eine gemeinsame Kovarianz, die die getrennten Faktoren verbindet? Wie belastbar ist
die globale Auswahl in `_archive/tfpt-45/source_extracts/02_carrier_source.tex:2814–2994`
und `:3250–3292`?

## A3 [E] – Codex' Parallelitäts-Ausschluss bestätigt

Am exakten `v117`-Vertreter (`verification/v117_monodromy_weyl_a3.py:53–57`,
`M_k = U^k M0 U^{−k}`, `U = diag(1, i, −i)`): Produkt = I, Gruppenordnung 12,
`tr[M0,M1] = −1`, Kommutant auf C³ eindimensional (irreduzibel). Eine diagonale
Determinantenrichtung auf 3 ⊕ 1, die alle `M_k ⊕ 1` parallel erhält, hat die Form
(b,b,b,−3b). Mit `β = m + ½` ist die Familiennorm `12(r+½)²`, die
Familienprojektion `3t²(2r+1)²`; das ist nie 2 oder 4. Kein 2+2-Gewicht, auch nicht
m_A, kommutiert. **Die gemeinsame parallele Identifikation ist ausgeschlossen.** Das
ist kein TFPT-No-go, denn die beiden Faktoren sind nach `origin_theory.tex:1210–1218`
verschiedene Seiten derselben Geometrie.

## Audit der Archivauswahl

### A1 [E] – Die explizite Monodromieformel ist in sich widersprüchlich (Bestätigung)
Dieser Defekt war bereits im Contract `source-boundary-lift-selection-20260922`
gespeichert; hier ist er unabhängig bestätigt.

`03_em_flavor_source.tex:1095–1118` setzt `ρ_F(γ₁) = D`, `ρ_F(γ_i) = PDP⁻¹`,
`ρ_F(γ₋₁) = P²DP⁻²` mit `D = diag(1, ω, ω²)`. Alle drei sind **diagonal**; die
Gruppe ist abelsch, und `ρ_F(γ_{−i}) = I`. Das widerspricht der eigenen Voraussetzung
(lokales Spektrum {1, ω, ω²} an jeder Marke) und der irreduziblen A4-Gruppe von v117.
Der Eindeutigkeitssatz `thm:rigid-family-local-system` (`:1189–1235`) stützt [∇_F*]
auf genau diese Rigiditätsaussage. Der tatsächlich irreduzible Vertreter ist v117 –
dessen Identifikation mit der analytischen Monodromie ist dort [N] (ODE-Abgleich
1e−7, `v117:40–43`).

### Voraussetzungen von `thm:joint-discrete-admissible-sector` (`02:2814–2994`)
* **[∇_F*] steht im Singleton-Datum, wird im Beweis (Schritte 1–5) aber nicht
  hergeleitet.** Es kommt erst über `03:1189` hinein (A1).
* Schritt 2: „lifted spin action closes only after 4π, so one primitive winding is
  realized by four quarter-turn corners" – von 4π (zwei Halbdrehungen) zu vier
  Vierteldrehungen ist ein zusätzlicher Schritt; die faithful-D4-Wirkung wird
  angenommen.
* Schritte 3 und 5 benutzen physikalische Auswahlforderungen: Existenz eines
  seam-geraden Higgsdubletts, Fehlen eines leichten Farbtripletts,
  primitiver Yukawa-Erzeuger (`thm:yukawa-forces-32`, `02:2443ff`). Schritt 3 setzt
  `dim E+ = 2` aus dem Higgs-Index voraus, Schritt 5 leitet die Determinantenklasse
  aus derselben Higgs-Forderung ab.
* Die einzige Verbindung Träger ↔ Familie im Beweis ist die Zählprüfung
  `Oadm = N_fam · dim S⁺ = 48`, ausdrücklich als „derived consistency check".

### Gefundene Träger→Familie-Übergänge im Archiv
1. **Cusp-Zuordnung (A4, [E] als Arithmetik):** `prop:dual-root-generation`
   (`02:1274–1310`): `{1, ⅔, ⅓} = {2y₊, −2y₋, 2(y₊+y₋)}` aus `Y = diag(−⅓³, ½²)`.
   `exp(2πi·Cusp)` = {1, ω, ω²} stimmt mit den lokalen v117-Spektren an allen vier
   Marken überein. **Aber:** Der Beweis setzt die Cusps aus
   `thm:exact-transport-closure` ein, und dieser nennt sie „obtained from the
   singlet-projected hypercharge spectrum" (`03:1242–1246`) – zirkulär. Es ist eine
   Mengengleichheit von Eigenwerten, keine Operatorabbildung. Der wechselseitige
   Verweis allein beweist noch keinen logischen Zirkel; belastbar ist, dass daraus
   **kein unabhängiger physischer Cusp-Selektor oder Collartransport** geliefert
   wird.
2. **Yukawa-Holonomieformel:** `(Y_f)_ij = λ^{L+L}⟨e_i, Hol_{Γ_ij}(∇_F*) e_j⟩`
   (`03:1252–1262`, `02:2645–2667`). Das ist ein echter Operator, der die
   SU(3)_F-Holonomie mit dem Higgs-Träger E₂ und S⁺ koppelt – auf Ebene „Proof
   sketch", gestützt auf [∇_F*] aus A1.
3. **SU(4)/A3-Glue:** In den geprüften Archivdateien
   `_archive/tfpt-45/source_extracts/*.tex` kommt SU(4) bzw. die A3-Verklebung nicht vor. E8 erscheint nur als „downstream scale grammar"
   (`technical_companion_source.tex:1519–1547`) und als Zählung
   `|R(E8)| = 240 = 5·48`.

## Ergebnis

* In den geprüften Archivstellen fehlt ein Collar → **SU(4)**-Transport.
* Ein Collar → **SU(3)_F**-Anschluss erscheint dort nur als (i) Eigenwert-Mengengleichheit
  der Cusps mit dem Hyperladungsspektrum (ohne unabhängigen Selektor) und (ii) die
  Yukawa-Holonomieformel, die [∇_F*] voraussetzt. [∇_F*] hängt an einer explizit
  widersprüchlichen Monodromieformel; der tragfähige Vertreter ist v117 mit
  numerischer [N]-Identifikation.
* Die „globale Auswahl" `02:3264–3284` erbt diese Voraussetzungen: Sie ist eine
  Eindeutigkeitsaussage *gegeben* die physikalischen Auswahlforderungen und die
  Familienrigidität, kein Operatortransport vom Collar.

**Erste nicht gelieferte Struktur:** eine Operatorabbildung vom Collar (D_coll) auf
die Familie, die mehr als Eigenwerte festlegt – mindestens eine gemeinsame unitäre
Abbildung, die vier Collartransporte `H_k` zugleich auf `M_k` und die Deckwirkung auf
U abbildet (so formuliert in `source-three-route-closure-20260922/PROOF.md:100–104`).
In den geprüften Stellen ist sie nicht vorhanden.

**Positiver Bestand, nicht zu übergehen:** `source-native-clock-flavor-bridge-20260922/PROOF.md:20–129`
liefert ein exaktes, orientierungsgetwistetes Operatorwörterbuch Q/Σ/G/T/P ↔ M/U mit
N-Metrik und markierten Zuordnungen. Das ist kein roher Collartransport, aber mehr als
eine Eigenwertgleichheit. Fortsetzung: `../native-vertex-marking-bridge-20261014`.
