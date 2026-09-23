# TFPT Universalraum v1.4 — Abarbeitung der sechs Follow-ups

**Stand:** 14. September 2026
**Vertrag:** `experiments/theory-contracts/universalraum-followups-closure-20260914/`
**Status:** Forschungsstand. Keine Promotion nach `verification/`, Ledger, Papers oder
Website. Keine T1–T8-Schließung, kein RH-, Faktorisierungs- oder P-vs-NP-Resultat.

---

## Kurzfassung

Alle sechs offenen Fragen aus `TFPT_Followups_2026-09-14_v1.4.md` haben jetzt eine
belegte Antwort. Vier sind positiv entschieden, zwei sind als Unmöglichkeit mit
exakter Schranke abgeschlossen.

Das wichtigste Einzelergebnis ist unangenehm: **v1.4 hat die Vermittler-Architektur
offen gelassen und dabei zwei Kennzahlen aus dem falschen Vertrag berichtet.** Die
Quelle schreibt die Bauweise vor, und zwar ohne jeden Spektralvergleich — allein aus
der Wurzelarithmetik von E8. Die kantenlokale Bandschranke 0,7 Δ und der
Lückenkoeffizient −11,9555 ε² gehören zu einer Bauweise, die die Quelle nicht liefert.
Der richtige, jetzt zertifizierte Wert ist **0,55043 J**.

Zwei weitere Ergebnisse kehren Erwartungen um:

- Bei der gekoppelten Probe ist das Problem **kein Fehlerbudget**, sondern eine
  prinzipielle Verschränkungsschranke. Kein rein lokales Rückkopplungsprotokoll kann
  das Ziel erreichen, egal wie gut die Hardware ist.
- Im Zeitbudget ist **nicht die Uhr** der Engpass, sondern die Kenntnis des
  Hamiltonians — um einen Faktor 14 797.

Maschinell geprüft: **5260 Bedingungen**, sechs unabhängige Prüfer, alle Ausgaben
bytegleich zwischen normalem und `-OO`-Lauf, **zwölf** gezielt eingebaute Fehler
(Mutanten) werden erkannt.

---

## Frage 2 — Welche Bauweise schreibt die Quelle vor?

**Entschieden: die Bank ist wurzelindiziert, eine Kopie pro Zelle.**

v1.4 hatte drei Kandidaten nebeneinander stehen lassen — eine globale Bank, eine Bank
pro Zelle, eine Bank pro Kante — und wollte zwischen ihnen spektral entscheiden. Das
ist nicht nötig. Die Entscheidung fällt in exakter Ganzzahlarithmetik auf dem
E8-Wurzelsystem, ohne eine einzige Gleitkommazahl:

- Die 16 Orte des Clebsch-Graphen sind D5-Spinorgewichte.
- Die 40 Bindungen tragen **zehn** Labels zu je **vier paarweise disjunkten** Kanten.
- Die Abbildung (Kante, Trägerpaar) → Wurzel ist **genau 4-zu-1** auf die 60 Wurzeln
  des (10,6)-Sektors.
- E8 ist einfach geschnürt, jeder Wurzelraum ist eindimensional (248 = 8 + 240).

Daraus folgt unmittelbar:

| Bauweise | Status |
|---|---|
| gemeinsame globale Bank | **ausgeschlossen** — eine Algebra beschriftet 16 Orte, ein Netz aus L Zellen hat 16L |
| **eine Bank pro Zelle** | **abgeleitet** — eine Algebrakopie je Zelle, 60 Wurzelräume, vier gleichlabelige Kanten teilen eine Mode |
| eine Bank pro Kante | **ausgeschlossen** — verlangt 240 unabhängige Moden in einem 60-Wurzel-Sektor, also dim g_α = 4 |

Die in der Fugen-Analyse offen gebliebene Fock-Frage öffnet das nicht wieder: jeder
Fockraum über der Adjungierten trägt eine Mode je Erzeuger. Der Vermittler ist durch
seine Wurzel beschriftet und **vergisst**, welche der vier Kanten ihn erzeugt hat.

**Konsequenz für v1.4:** Bandabstand 2Δ/5 statt 0,7 Δ, Lückenkoeffizient +13,901769 ε²
statt −11,955494 ε². Frage 3 musste daher den geteilten Operator zertifizieren, nicht
den kantenlokalen.

1076 exakte Bedingungen.

---

## Frage 3 — Ist die Vierfachheit echt?

**Entschieden: sie ist symmetrieerzwungen, nicht zufällig.**

Der Prüfer baut das 24024-dimensionale SU(4)-Singulettmodul selbst auf und
diagonalisiert den **abgeleiteten geteilten** Operator H = H₀ + F4_shared/800.

| Größe | Wert |
|---|---|
| Grundzustand | 11,739295743279031 J |
| erste Anregung | 12,289721091749387 J, **vierfach** |
| nächstes Niveau | 13,210602489415791 J |
| Muster der untersten zehn | 1 + 4 + 5 (der Fünferblock ist rechts abgeschnitten) |
| Lücke, Gleitkomma | 0,550425348470355 J |
| **zertifizierte untere Schranke** | **0,5504253482676765 J** |
| Residuen der zehn Eigenpaare | 2,3·10⁻¹⁴ … 1,3·10⁻¹² |

Die Vierfachheit ist eine **Folge der Symmetrie**, keine Beobachtung: der Eigenraum
trägt einen Charakter mit ⟨χ,χ⟩ = 1 bei Dimension 4, exakt ausgewertet über alle 1920
Elemente von Aut(C16) mit Murnaghan–Nakayama. Er ist also eine **irreduzible**
vierdimensionale Darstellung, und jede symmetrieerhaltende Störung lässt die
Vierfachheit stehen. Diese Irreduzible kommt im Modul 80-mal vor; dass genau eine Kopie
unten liegt, trennen die zertifizierten Einschließungen vom nächsten Niveau bei
13,2106 J.

Damit ist die Vorhersage aus Frage 2 bestätigt: 0,55043 J ist exakt der Wert des
geteilten Vertrags. Die Erwartungswerte trennen die Bauweisen zusätzlich sauber:
F4_shared = 555,4885 gegen F4_edge = 732,1203.

Nebenprodukt, für Frage 4 gebraucht: die exakte Kreuzglied-Schranke
**D ≥ 12 H₀ − 480 I** aus dem 24-dimensionalen Labelblock mit Spektrum
{−48¹, −16⁹, 0⁴, 16⁹, 48¹}, und daraus F4_shared ≥ H₀² − 64 H₀ + 960 I.

**Ehrlich offen:** Der Ausschluss der Nicht-Singulett-Sektoren bleibt **bedingt**. Er
stützt sich auf ein nicht zertifiziertes nacktes Nicht-Singulett-Minimum 12,133537 und
liefert damit 12,546883 — Abstand 0,257161 zum Quartett. Der Ausschluss überlebt unter
dieser Annahme, nicht unbedingt.

3933 Bedingungen.

---

## Frage 1 — Wer bedient das Labor?

**Entschieden: genau drei unabhängige Zusatzressourcen, keine mehr und keine weniger.**

Nach allen Reduktionen (Messung ⟸ Record + Registerbit; Belegungsabfrage ⟸ derselbe
Record auf dem Vermittlerzahlsektor; Reset ⟸ Messung + frischer Träger) bleiben drei
Ressourcen übrig. Entscheidend ist, dass jede durch eine **andere** Invariante von den
übrigen getrennt wird — sie sind also nicht weiter reduzierbar:

1. **Isolierter Stern / isolierte Kante** — bricht die Zeittranslationsinvarianz.
   Der elementare Kommutator zweier Bindungen an einem Ort hat Norm 0,433 J; ein
   Clebsch-Stern hat 20 solche Paare. Das garantierte Faktorisierungsfenster bei
   Infidelität 10⁻⁶ ist 4,8·10⁻⁴ ℏ/J, der Filter braucht 31,73 ℏ/J — **Fehlbetrag
   6,6·10⁴**.
2. **Resonanter Record** — bricht den A3-Sektorinhalt. Sym²(4) kommt in der 248 nicht
   vor (exakte Gewichtsmultimengen) und erscheint erst in der 3875:
   Λ⁴(16) ⊃ (10_D5, Λ³(6)) mit der exakten Identität Λ³(6) = Sym²(4) + Sym²(4̄),
   Dimension 200. Damit ist Punkt 3 der Fugen-Rangfolge in seiner Existenzhälfte
   erledigt.
3. **Reset** — bricht die Unitalität. Freie Entwicklung plus klassische Uhr erzeugt
   ausschließlich unitale Kanäle, und unitale Kanäle senken keine Entropie; ein reiner
   Zielzustand ist so nicht erreichbar. Der 13-Faktor-Filter ist nicht unital und genau
   deshalb kein kostenloser Projektor.

**Zugabe: die T2-Halbladungsobstruktion ist geschlossen.** Eine
Halbladungsverschiebung verlangt die Verdopplung der Glue-Gruppe auf Z8. Über 98 469
Gittershifts geprüft: jeder Kandidat hat Normquadrat 1/2 mod 1, also konformes Gewicht
1/4 oder 3/4 — **nie ganzzahlig**. Die Obstruktion liegt in dieser Quelle, nicht in
einer hinzugefügten Ladungsgitter-CFT. Das war die im Follow-up benannte fehlende
Beweiskante.

65 Bedingungen.

---

## Frage 4 — Bleibt das Labor bei Fehlern und wachsender Größe brauchbar?

**Entschieden — und die Antwort ist grundsätzlicher als erwartet.**

Der Prüfer baut die gekoppelte Zweizellenprobe **vollständig** auf dem echten
65536-dimensionalen Raum auf (zwei Tetramerzellen, Brücke V = (I + S_ab)/2), ohne
effektive Trunkierung. Der invariante Unterraum von Kapitel 5 wird aus dem
tatsächlichen Brückenoperator reproduziert: ⟨0|V|0⟩ = 5/8, ⟨0|V|1⟩ = √15/8,
⟨1|V|1⟩ = 3/8. Sparse-Lanczos auf allen 65536 Komponenten bestätigt E₀, E₁ und die
Lücke an drei Kopplungen.

**Das Ergebnis ist kein Fehlerbudget, sondern eine Unmöglichkeit.** Der wahre
gekoppelte Grundzustand Ψ₋ ist verschränkt. Jedes Protokoll aus **reinen
Produktoperationen** E_A ⊗ E_B kann diese Verschränkung nicht herstellen. Der
Überlappdefekt

> q(λ/J) = 1 − |⟨Ω_A Ω_B|Ψ₋⟩|² = (15/1024)·(λ/J)² + O((λ/J)³)

ist damit eine **untere Schranke an die stationäre Infidelität** jedes rein lokalen
Rückkopplungsprotokolls, das Ω_A ⊗ Ω_B weiter als Ziel behandelt. Ich habe die Reihe
unabhängig symbolisch nachgerechnet: der Koeffizient ist exakt 15/1024, ein lineares
Glied existiert nicht.

| λ/J | Bodenschranke q |
|---:|---:|
| 0,1 | 1,48·10⁻⁴ |
| 0,25 | 9,42·10⁻⁴ |
| 0,5 | 3,86·10⁻³ |
| **1,0 (Default)** | **1,5877·10⁻²** |
| 2,0 | 6,25·10⁻² |

Die größte Kopplung, die 10⁻⁶ noch zulässt, ist **λ/J = 0,008258112**. Die
Default-Probe λ = J verfehlt das Ziel um **Faktor 15 877**. Die v1.4-Aussage „explizit
außerhalb von 10⁻⁶" ist damit nicht nur bestätigt, sondern beziffert — und als
prinzipielle Schranke ausgewiesen, nicht als Protokollschwäche.

**Unabhängige Zellen bleiben beherrschbar.** Der eigenständig nachgebaute
544D-Sternfilter fixiert Ω, die Kontraktionsrate ist 0,97542071045 (β = 0,4100970508,
Reset-Überlapp 1/24), und nach **556 Zyklen** liegt die Einzelzellinfidelität unter
10⁻⁶. Die Kontraktionsschranke r^m wurde an jedem geprüften Zyklus eingehalten.

**Im Zeitbudget ist nicht die Uhr der Engpass.** Die 13 Filterzeiten summieren sich zu
3172,83 ℏ/Δ, der gemeinsame Start-/Endversuch auf 6345,66 ℏ/Δ. Die nötige *relative*
Uhrengenauigkeit für 10⁻⁶ ist 1,166·10⁻³ bei unabhängigem Jitter und 1,219·10⁻³ bei
systematischem Ratenversatz — eine milde Anforderung. Bindend ist stattdessen die
**Kenntnis des Hamiltonians**: δH + δE₀ ≤ 7,88·10⁻⁸ Δ, also **14 797-mal schärfer als
die Uhr**. Die Formulierung „exakte Zeitwahl ist eine starke Ressource" trifft in
dieser Probe den falschen Adressaten.

**Entropiekosten, beziffert.** Bei 8 Farbbits pro Reset, 3 Recordbits pro Zyklus und
Vorbereitungswahrscheinlichkeit p = 0,161915 (im Mittel 6,176 Versuche) kostet ein
erfolgreicher Einzelzellenlauf mindestens **6157,41 k_BT ln 2**. Die
Union-Bound-Stichprobe mit 4096 Zellen und 890 Zyklen ergibt **4,027·10⁷ k_BT ln 2**.

**Die logarithmische Zyklenzahl der unabhängigen Zellen überträgt sich nicht.** Die
Union-Bound-Schranke N·r^m geht mit wachsender Zyklenzahl gegen null — die wahre
gekoppelte Infidelität friert dagegen bei q(λ/J) > 0 ein, für **jedes** λ > 0. Das
Verhältnis von Wahrheit zu Schranke divergiert also mit der Zyklenzahl: oberhalb
λ/J = 0,008258 erreicht **keine** Zyklenzahl mehr 10⁻⁶. Mehr Zyklen sind bei
gekoppelten Zellen kein Ausweg, sondern machen die Schranke nur zunehmend irreführend.

**Ehrlich offen:** L = 3, 4 als wirklich wachsende Kette wurde aus Budgetgründen nicht
gerechnet, ebenso wenig die Vielzyklen-Monte-Carlo-Trajektorie des zusammengesetzten
Kanals; die Bodenschranke ersetzt beides als exaktes Argument. Die eben genannte
Divergenz ist qualitativ belegt, aber nicht als Zahlentabelle über L. Die Brücke λV ist
nicht aus c3 = 1/(8π) oder g_car = 5 abgeleitet.

71 Bedingungen.

---

## Frage 5 — Entsteht eine gemeinsame Welt?

**Abgeschlossen als Unmöglichkeit in der nativen Familie.**

Vier Forderungen, ein Prüfstand:

- **Dimension: Eingabe, keine Ausgabe.** Die Wärmespur eines kartesischen Produkts
  faktorisiert exakt (gegen ein vollständig ausgeschriebenes Produkt geprüft). Jede
  Familie G □ (Z/L)^d liefert also genau das eingeklebte d zurück. Der Test hat **null
  Unterscheidungskraft** — das ist ein Befund über den Test, nicht über die Theorie.
- **Gemeinsamer Lichtkegel: bestanden, exakt.** Eine einzige Geschwindigkeit π/4
  reproduziert den Grundzustand in **allen vier** N-alitätssektoren (n = 6…12,
  Sektordimensionen 180 bis 369 600) und die angeregten Bänder in zwei Farbsektoren bei
  zwei Ringgrößen. Niedrigstes Primärband x = 0,74982 (n=8) und 0,74219 (n=12) gegen 3/4.
- **Chirales Maß: bestanden, exakt.** Jedes angeregte Band zerfällt in gleich große
  links- und rechtslaufende Hälften; das Stromband trägt genau drei linkslaufende und
  drei rechtslaufende Cartan-Ströme bei relativem Impuls ±1, mit x = 0,96715 (n=8) →
  0,99403 (n=12) gegen 1.
- **Spin 2: unmöglich.** Der TT-Projektor hat in d Raumdimensionen den Rang
  (d+1)(d−2)/2, also 0, 0, 2, 5, 9 für d = 1…5. Die native Nahtfamilie hat **eine**
  Raumdimension und damit **null** transversal-spurfreie Polarisationen.

**Fazit:** Zwei der vier Eigenschaften sind auf der nativen Familie echte Resultate,
keine Eingaben. Die beiden anderen scheitern gemeinsam an derselben Stelle: die Quelle
beschriftet **eine** Zelle, jede größere Probe braucht eine Klebregel, und die einzige
Klebregel, die die Quelle motiviert — die Naht, Z4-Eichung, (D5)₁×(A3)₁ ⊂ (E8)₁ — hat
eine Raumdimension.

**Fehlende Zutat, präzise benannt:** eine Klebregel mit drei Raumdimensionen, die die
eine Geschwindigkeit der Naht behält.

97 Bedingungen.

---

## Frage 6 — Hält eine gemeinsame Parametrisierung?

**Entschieden: die Spannung überlebt das gesamte Korrekturbudget.**

Statt drei getrennter Kalibrierungen ein einziger Fit über (n_s, ln 10¹⁰A_s, r) mit dem
einen Parameter N und festem c3:

| Größe | Wert |
|---|---|
| bester Fit | N = 56,634 |
| χ² / dof | 12,291 / 1 → p = 4,55·10⁻⁴ |
| Pull n_s | **−3,505 σ** (trägt den ganzen χ²) |
| Pull ln 10¹⁰A_s | +0,087 σ |
| r bei bestem Fit | 0,003741, unter der Schranke r < 0,038 |

**Das Korrekturbudget schließt die Lücke nicht.** Für p > 0,05 bräuchte man
Δn_s = +0,00464 (das 1,55-fache der ACT-Unsicherheit) oder −24,5 % auf A_s (entspricht
−3,94 % in c3; die exakte Zentralwertanpassung reproduziert die −9,61 % der Vorrunde).
Die unabhängig nachgerechnete exakte Slow-Roll-NLO-Korrektur liefert auf n_s nur
+0,00128 — **Faktor 3,63 zu klein** — und auf A_s +10,31 %, also **falsches Vorzeichen**
(mehr statt weniger Amplitude) und zusätzlich Faktor 2,4 zu klein.

**Reheating-Budget.** Für T_reh ∈ [10³, 10¹⁶] GeV, gedeckelt durch die physikalische
Obergrenze bei sofortigem Reheating T_reh,max = 2,596·10¹⁵ GeV, ergibt sich
N ∈ [46,08; 55,61]. Der tilt-bevorzugte Zweig N = 80,65 liegt **25,0 e-Faltungen**
darüber und ist damit robust ausgeschlossen, unabhängig von der Amplitudenspannung. Der
amplitudenbevorzugte Zweig N = 56,62 liegt 1,01 e-Faltungen darüber; dieser Abstand hat
die Größenordnung der Systematik der Matching-Relation selbst und wird als **marginal**
geführt, nicht als Ausschluss.

**r ist die einzige echte Vorhersage dieser Runde**, denn r spielt beim Festlegen von N
keine Rolle. r = 0,00374 liegt bei 7,5 σ für CMB-S4 (σ(r) = 5·10⁻⁴) und 3,7 σ für
LiteBIRD (σ(r) = 10⁻³) — entscheidbar, derzeit weder ausgeschlossen noch bestätigt.

**Flavour: Parameterdefizit 1.** Die unabhängig neu gebauten Overlap-Operatoren mit
Fluss 3 auf 8×8 und 10×10 liefern exakt drei Nullmoden (GW-Defekt < 1,2·10⁻¹³) und beim
konstanten Profil exakt Y = I. Über einen einparametrigen Gauß-Profilscan gibt es
**keinen** Wert, der m_μ/m_τ und m_e/m_τ gleichzeitig auf Faktor 2 trifft — auf keinem
der beiden Gitter. Es fehlt mindestens ein zweiter unabhängiger Parameter.

Als „assumed" markiert und bei jeder Zahl mitgeführt: σ(ln 10¹⁰A_s) = 0,0042 (Proxy,
nicht direkt aus Tabelle 5 von 2503.14452v2 gelesen), die Rückfallvariante 0,012 für den
Sensitivitätslauf, und die nicht beschaffte Korrelation zwischen n_s und A_s (auf 0
gesetzt). Der Sensitivitätslauf ändert das Ergebnis nicht (N = 56,708, p = 4,68·10⁻⁴).

18 Bedingungen.

---

## RH-Aktualitätsprüfung

Nicht physikalisch blockiert, sondern durch **einen** fehlenden Pfad:
`external_sources_config.json` wurzelt auf
`/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2`; das Verzeichnis
`~/Documents/Codex` existiert auf dieser Maschine nicht. Elf Review-Pins
(`codex-rh-scha-2:*`) hängen daran. `rh/catalog/map/rh_concept_map.json` ist vorhanden.
Es wurden keine Pins geändert und keine Beweismarker angehoben.

---

## Prüfstand

Sechs unabhängige Prüfer. Jeder baut seine Objekte selbst und importiert **keinen**
fremden TFPT-Prüfer.

| Datei | Frage | Bedingungen | Laufzeit |
|---|---|---:|---:|
| `architecture.py` | 2 — Bauweise | 1076 exakt | 0,06 s |
| `primitives.py` | 1 — Primitivliste + T2 | 65 | 1,7 s |
| `native_family.py` | 5 — gemeinsame Welt | 97 | 29 s |
| `quartet_cert.py` | 3 — Vierfachheit | 3933 | 100 s |
| `coupled_cells.py` | 4 — gekoppelte Probe | 71 | 4 s |
| `matching_joint.py` | 6 — Parametrisierung | 18 | 4 s |
| **Summe** | | **5260** | |

**Replay-Disziplin.** Alle sechs Ausgaben sind bytegleich zwischen `python3 x.py` und
`python3 -OO x.py`. Zwölf gezielt eingebaute Fehler werden erkannt, darunter „Brücke als
antisymmetrische statt symmetrische Halbsumme", „falsche c3-Potenz in der
Amplitudenrelation", „zweite Geschwindigkeit auf derselben Kette" und „Bindungslabel aus
der falschen Kombination".

```sh
cd experiments/theory-contracts/universalraum-followups-closure-20260914
python3 -B replay.py                      # fünf leichte Module, 1327 Bedingungen
python3 -B replay.py --only quartet_cert  # schwer, ~200 s, 3933 Bedingungen
```

---

## Was diese Runde **nicht** zeigt

Ich führe das ausdrücklich auf, weil der Wert der obigen Zahlen davon abhängt, dass die
Grenze klar ist.

- **Entschieden heißt: entschieden unter der Lesart „Ort = D5-Spinorgewicht"** der
  Fugen-Analyse und unter dem benannten C16-Modell. Diese Lesart selbst ist **nicht**
  abgeleitet. Sie ist die tragende, ungeprüfte Voraussetzung der gesamten Runde.
- Die beiden dynamischen Schranken von Frage 1 (Kommutatornorm, Isolationsfenster) sind
  numerisch und **obere** Schranken. Sie zeigen, dass Isolation nicht garantiert ist,
  nicht dass sie unmöglich ist.
- Der Nicht-Singulett-Ausschluss in Frage 3 ist **bedingt** (siehe dort).
- In Frage 4 fehlen die wirklich wachsende Kette L = 3, 4 und die Vielzyklen-Trajektorie;
  die Brücke λV ist ein Modellinput, nicht aus den Axiomen abgeleitet.
- Frage 6 hat mit 18 Prüfbedingungen das dünnste Sicherungsnetz aller sechs Module. Ich
  habe deshalb zwei Mutanten nachgerüstet, die den c3-Exponenten und die Tilt-Relation
  wirklich treffen — aber der Fit selbst (χ², Pulls, r) ist nicht einzeln abgesichert.
- **Alle T1–T8-Tore bleiben offen.** Kein RH-Resultat, keine Faktorisierung, keine TOE.

---

## Was als Nächstes wirklich etwas bewegt

Nach dieser Runde sind drei Fronten übrig, und sie sind sehr ungleich wertvoll:

1. **Die Lesart „Ort = D5-Spinorgewicht" ableiten statt annehmen.** Sie trägt Frage 2,
   und über Frage 2 die Fragen 3 und 4. Fällt sie, fällt der größte Teil dieser Runde.
   Das ist die mit Abstand höchste Hebelwirkung.
2. **Eine Klebregel mit drei Raumdimensionen finden, die die Nahtgeschwindigkeit
   behält.** Frage 5 hat exakt diese eine fehlende Zutat isoliert. Ohne sie gibt es in
   der nativen Familie kein Spin 2 — nicht „noch nicht gefunden", sondern Rang 0.
3. **Den zweiten Flavour-Parameter identifizieren.** Frage 6 hat das Defizit auf genau 1
   beziffert. Das ist eine scharfe, gut angreifbare Aussage.

Die Spannung in n_s ist damit **nicht** repariert und lässt sich nach dieser Runde auch
nicht mehr als Rechenungenauigkeit oder fehlende Schleifenordnung erklären. Sie ist ein
echter Konflikt der Matching-Relation mit ACT, und r = 0,00374 ist die Zahl, an der die
nächste Messgeneration darüber entscheidet.
