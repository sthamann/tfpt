# Universalraum v1.4 — Abarbeitung der sechs Follow-ups

14. September 2026. Anschluss an
[`universalraum-five-source-frontier-20260914`](../universalraum-five-source-frontier-20260914/README.md)
und an die sechs Fragen in `universal_room/TFPT_Followups_2026-09-14_v1.4.md`.

Forschungsstand, **keine** Promotion nach `verification/`, Ledger, Papers oder Website.
Keine T1–T8-Schließung, kein RH-, Faktorisierungs- oder P-versus-NP-Resultat.
Alle Prüfer bauen ihre Objekte selbst und importieren keinen fremden TFPT-Prüfer.

## Ergebnis in einem Satz

Alle sechs Fragen haben jetzt eine belegte Antwort: vier sind **positiv
entschieden** (Architektur, Primitivliste, Quartett, gemeinsame
Parametrisierung), zwei als **Unmöglichkeit mit exakter Schranke** abgeschlossen
(gemeinsame Welt, gekoppelte Probe). Die Entscheidung zur Architektur **kehrt
zwei Kennzahlen von v1.4 um**: die kantenlokale Bandschranke 0,7 Δ und der
Lückenkoeffizient −11,9555 ε² gehören zu einem Vertrag, den die Quelle nicht
liefert; der zertifizierte Wert ist 0,55043 J.

## Die Prüfer

| Datei | Frage | Bedingungen | Laufzeit |
|---|---|---:|---:|
| `architecture.py` | 2 — welche Bauweise ist vorgeschrieben | 1076 exakt | 0,06 s |
| `primitives.py` | 1 — wer bedient das Labor (+ T2-Halbladung) | 65 | 1,7 s |
| `native_family.py` | 5 — entsteht eine gemeinsame Welt | 97 | 29 s |
| `quartet_cert.py` | 3 — Vierfachheit zertifizieren | 3933 | 100 s |
| `coupled_cells.py` | 4 — gekoppelte Probe, Fehler, Kosten | 71 | 4 s |
| `matching_joint.py` | 6 — gemeinsame Parametrisierung | 18 | 4 s |

```sh
python3 -B architecture.py     # exakte E8-Wurzelarithmetik, kein Gleitkomma in der Entscheidung
python3 -B primitives.py
python3 -B native_family.py
python3 -B replay.py                    # leichte Module: normal und -OO bytegleich, Mutanten
python3 -B replay.py --only quartet_cert  # schwer, ~200 s, nur auf Anforderung
```

`replay.py` (fünf leichte Module): **1327 Bedingungen**, alle fünf Ausgaben
normal/-OO bytegleich, **zehn** gezielte Mutanten erkannt — darunter „zweite
Geschwindigkeit auf derselben Kette", „Bindungslabel aus der falschen
Kombination", „Brücke als antisymmetrische statt symmetrische Halbsumme" und
„falsche c3-Potenz in der Amplitudenrelation".

`replay.py --only quartet_cert`: **3933 Bedingungen**, bytegleich
(`sha256 498b93c0…`), zwei weitere Mutanten erkannt — der falsche
Tauschkoeffizient im Labelblock der geteilten Bank und das mit falschem
Vorzeichen addierte Kreuzglied.

Zusammen **5260 maschinengeprüfte Bedingungen** und **zwölf** erkannte Mutanten.

## Frage 2 — entschieden: die Bank ist wurzelindiziert

Der Vermittler eines Bindungsübergangs ist eine **Wurzel des (10,6)-Sektors**.
Exakt geprüft: die 16 Orte sind D5-Spinorgewichte, die 40 Bindungen tragen
**zehn** Labels zu je **vier paarweise disjunkten** Kanten, und die Abbildung
(Kante, Trägerpaar) → Wurzel ist **genau 4-zu-1** auf die 60 Wurzeln. E8 ist
einfach geschnürt, jeder Wurzelraum ist eindimensional (248 = 8 + 240).

Damit zerfällt die Trichotomie von v1.4 ohne Spektralvergleich:

| Bauweise | Status |
|---|---|
| gemeinsame globale Bank | ausgeschlossen: eine Algebra beschriftet 16 Orte, ein Netz aus L Zellen hat 16L |
| **eine Bank pro Zelle** | **abgeleitet**: eine Algebrakopie je Zelle, 60 Wurzelräume, vier gleichlabelige Kanten teilen eine Mode |
| eine Bank pro Kante | ausgeschlossen: verlangt 240 unabhängige Moden in einem 60-Wurzel-Sektor, also dim g_α = 4 |

Die offene Fock-Frage der Fugen-Analyse öffnet das nicht wieder: jeder Fockraum
über der Adjungierten trägt eine Mode je Erzeuger, also ist der Vermittler durch
seine Wurzel beschriftet und vergisst, welche der vier Kanten ihn erzeugt hat.

**Folge:** der zertifizierte Bandabstand des abgeleiteten Vertrags ist 2Δ/5, nicht
0,7 Δ; der Lückenkoeffizient ist +13,901769 ε², nicht −11,955494 ε². Frage 3 muss
daher den geteilten Operator zertifizieren, nicht den kantenlokalen.

## Frage 1 — entschieden: drei unabhängige Zusatzressourcen

Die Primitivliste ist in `primitives.json` eingefroren. Nach allen Reduktionen
(Messung ⟸ Record + Registerbit; Belegungsabfrage ⟸ derselbe Record auf dem
Vermittlerzahlsektor; Reset ⟸ Messung + frischer Träger) bleiben genau **drei**
Ressourcen übrig, jede durch eine **andere** Invariante von den übrigen getrennt:

1. **Isolierter Stern/isolierte Kante** — bricht die Zeittranslationsinvarianz.
   Der elementare Kommutator zweier Bindungen an einem Ort hat Norm 0,433 J; ein
   Clebsch-Stern hat 20 solche Paare. Das garantierte Faktorisierungsfenster bei
   Infidelität 10⁻⁶ ist 4,8·10⁻⁴ ℏ/J, der Filter braucht 31,73 ℏ/J —
   **Fehlbetrag 6,6·10⁴**.
2. **Resonanter Record** — bricht den A3-Sektorinhalt. Sym²(4) kommt in der 248
   nicht vor (exakte Gewichtsmultimengen), und erscheint erst in der 3875:
   Λ⁴(16) ⊃ (10_D5, Λ³(6)) mit der exakten Identität
   Λ³(6) = Sym²(4) + Sym²(4̄), Dimension 200. Damit ist Punkt 3 der
   Fugen-Rangfolge in seiner Existenzhälfte erledigt.
3. **Reset** — bricht die Unitalität. Freie Entwicklung plus klassische Uhr
   erzeugt ausschließlich unitale Kanäle; unitale Kanäle senken keine Entropie,
   also ist kein reiner Zielzustand erreichbar. Der 13-Faktor-Filter ist nicht
   unital und genau deshalb kein kostenloser Projektor.

**Zugabe T2 (Halbladung):** Eine Halbladungsverschiebung verlangt die Verdopplung
der Glue-Gruppe auf Z8. Über 98 469 Gittershifts geprüft: jeder Kandidat hat
Normquadrat 1/2 mod 1, also konformes Gewicht 1/4 oder 3/4 — nie ganzzahlig.
Die Obstruktion liegt **in dieser Quelle**, nicht in einer hinzugefügten
Ladungsgitter-CFT. Das war die im Follow-up benannte fehlende Beweiskante.

## Frage 3 — entschieden: die Vierfachheit ist symmetrieerzwungen

Der Prüfer baut das 24024-dimensionale Singulettmodul selbst auf und
diagonalisiert den **abgeleiteten geteilten** Operator H = H0 + F4_shared/800.

| Größe | Wert |
|---|---|
| Grundzustand | 11,739295743279031 J |
| erste Anregung | 12,289721091749387 J, **vierfach** |
| nächstes Niveau | 13,210602489415791 J |
| Muster der untersten zehn | 1 + 4 + 5 (der Fünferblock ist rechts abgeschnitten) |
| Lücke, Gleitkomma | 0,550425348470355 J |
| **zertifizierte untere Schranke** | **0,5504253482676765 J** |
| Residuen der zehn Eigenpaare | 2,3·10⁻¹⁴ bis 1,3·10⁻¹² |

Die Vierfachheit ist keine Beobachtung, sondern eine **Folge der Symmetrie**: der
Eigenraum trägt einen Charakter mit ⟨χ,χ⟩ = 1 bei Dimension 4, exakt ausgewertet
über alle 1920 Elemente von Aut(C16) mit Murnaghan–Nakayama. Er ist also eine
**irreduzible** vierdimensionale Darstellung; jede symmetrieerhaltende Störung
lässt die Vierfachheit stehen. Diese Irreduzible kommt im Modul 80-mal vor — dass
genau **eine** Kopie unten liegt, trennen die zertifizierten Einschließungen vom
nächsten Niveau bei 13,2106 J.

Damit ist die in Frage 2 vorhergesagte Zahl bestätigt: **0,55043 J** ist genau der
Wert des geteilten Vertrags. Die Erwartungswerte trennen die beiden Bauweisen
zusätzlich sauber: F4_shared = 555,4885 gegen F4_edge = 732,1203.

Nebenbei exakt bewiesen und für Frage 4 gebraucht: die Kreuzglied-Schranke
**D ≥ 12 H0 − 480 I** (uniform D ≥ −480 I) aus dem exakten 24-dimensionalen
Labelblock mit Spektrum {−48¹, −16⁹, 0⁴, 16⁹, 48¹}, und daraus
F4_shared ≥ H0² − 64 H0 + 960 I.

**Ehrlich offen:** Der Ausschluss der Nicht-Singulett-Sektoren bleibt
**bedingt**. Er stützt sich auf ein nicht zertifiziertes nacktes
Nicht-Singulett-Minimum 12,133537 und liefert damit die Schranke 12,546883 —
Abstand 0,257161 zum Quartett. Der Ausschluss überlebt unter dieser Annahme,
**nicht** unbedingt.

## Frage 4 — entschieden: eine exakte Bodenschranke, kein Fehlerbudget-Problem

Der Prüfer baut die gekoppelte Zweizellenprobe **vollständig** auf dem echten
65536-dimensionalen Raum (zwei Tetramerzellen, Brücke V = (I + S_ab)/2) und
verlässt sich nirgends auf eine effektive Trunkierung. Der invariante Unterraum
von Kapitel 5 wird aus dem tatsächlichen Brückenoperator reproduziert:
⟨0|V|0⟩ = 5/8, ⟨0|V|1⟩ = √15/8, ⟨1|V|1⟩ = 3/8, und H_red hat exakt die
angegebene 2×2-Form. Sparse-Lanczos auf allen 65536 Komponenten bestätigt
E₀, E₁ und die Lücke an drei Kopplungen.

**Das eigentliche Ergebnis ist kein Fehlerbudget, sondern eine Unmöglichkeit.**
Der wahre gekoppelte Grundzustand Ψ₋ ist verschränkt; jedes Protokoll aus
**reinen Produktoperationen** E_A ⊗ E_B kann diese Verschränkung nicht
herstellen. Der Überlappdefekt

  q(λ/J) = 1 − |⟨Ω_A Ω_B|Ψ₋⟩|² = (15/1024)(λ/J)² + O((λ/J)³)

ist damit eine **untere Schranke an die stationäre Infidelität** jedes rein
lokalen Rückkopplungsprotokolls, das Ω_A ⊗ Ω_B weiter als Ziel behandelt. Ich
habe die Reihe unabhängig symbolisch nachgerechnet: der Koeffizient ist exakt
15/1024, es gibt kein lineares Glied.

| λ/J | Bodenschranke q |
|---:|---:|
| 0,1 | 1,48·10⁻⁴ |
| 0,25 | 9,42·10⁻⁴ |
| 0,5 | 3,86·10⁻³ |
| **1,0 (Default)** | **1,5877·10⁻²** |
| 2,0 | 6,25·10⁻² |

Die größte Kopplung, die 10⁻⁶ noch zulässt, ist **λ/J = 0,008258112**. Die
Default-Probe λ = J verfehlt das Ziel um **Faktor 15 877** — die v1.4-Aussage
„explizit außerhalb von 10⁻⁶" ist damit nicht nur bestätigt, sondern beziffert
und als *prinzipielle* Schranke ausgewiesen, nicht als Protokollschwäche.

**Unabhängige Zellen bleiben beherrschbar.** Der eigenständig nachgebaute
544D-Sternfilter fixiert Ω, die Kontraktionsrate ist 0,97542071045
(β = 0,4100970508, Reset-Überlapp 1/24), und nach **556 Zyklen** liegt die
Einzelzellinfidelität unter 10⁻⁶. Die Kontraktionsschranke r^m wurde an jedem
geprüften Zyklus eingehalten.

**Überraschung im Zeitbudget: nicht die Uhr ist der Engpass.** Die 13
Filterzeiten summieren sich zu 3172,83 ℏ/Δ (der gemeinsame Start-/Endversuch
auf 6345,66 ℏ/Δ). Die nötige *relative* Uhrengenauigkeit für 10⁻⁶ ist
1,166·10⁻³ (unabhängiger Jitter) bzw. 1,219·10⁻³ (systematischer Ratenversatz)
— das ist eine milde Anforderung. Bindend ist stattdessen die **Kenntnis des
Hamiltonians**: δH + δE₀ ≤ 7,88·10⁻⁸ Δ, also **14 797-mal schärfer** als die
Uhr. Die Formulierung „exakte Zeitwahl ist eine starke Ressource" trifft in
dieser Probe den falschen Adressaten.

**Entropiekosten, beziffert.** Bei 8 Farbbits pro Reset, 3 Recordbits pro Zyklus
und Vorbereitungswahrscheinlichkeit p = 0,161915 (im Mittel 6,176 Versuche)
kostet ein erfolgreicher Einzelzellenlauf mindestens **6157,41 k_BT ln 2**. Die
Union-Bound-Stichprobe mit 4096 Zellen und 890 Zyklen ergibt
**4,027·10⁷ k_BT ln 2**.

**Die logarithmische Zyklenzahl überträgt sich nicht.** Die Union-Bound-Schranke
für unabhängige Zellen, N·r^m, geht mit wachsender Zyklenzahl gegen null — die
wahre gekoppelte Infidelität friert dagegen bei q(λ/J) > 0 ein, für **jedes**
λ > 0. Das Verhältnis von Wahrheit zu Schranke divergiert also mit der
Zyklenzahl: oberhalb λ/J = 0,008258 erreicht **keine** Zyklenzahl mehr 10⁻⁶.
Mehr Zyklen sind bei gekoppelten Zellen kein Ausweg, sondern machen die
Schranke nur zunehmend irreführend.

**Ehrlich offen:** L = 3, 4 als wirklich wachsende Kette wurde aus Budgetgründen
**nicht** gerechnet, ebenso wenig die Vielzyklen-Monte-Carlo-Trajektorie des
zusammengesetzten Kanals; die Bodenschranke ersetzt sie als exaktes Argument.
Die eben genannte Divergenz ist qualitativ belegt, aber nicht als Zahlentabelle
über L. Die Brücke λV ist nicht aus c3 = 1/(8π) oder g_car = 5 abgeleitet.

## Frage 5 — abgeschlossen als Unmöglichkeit in der nativen Familie

Vier Forderungen, ein Prüfstand:

- **Dimension: Eingabe, keine Ausgabe.** Die Wärmespur eines kartesischen
  Produkts faktorisiert exakt (gegen ein vollständig ausgeschriebenes Produkt
  geprüft), also liefert jede Familie G □ (Z/L)^d genau das eingeklebte d. Der
  Test hat null Unterscheidungskraft.
- **Gemeinsamer Lichtkegel: bestanden, exakt.** Eine einzige Geschwindigkeit
  π/4 reproduziert den Grundzustand in **allen vier** N-alitätssektoren
  (n = 6…12, Sektordimensionen 180 bis 369 600) und die angeregten Bänder in
  zwei Farbsektoren bei zwei Ringgrößen. Niedrigstes Primärband
  x = 0,74982 (n=8) und 0,74219 (n=12) gegen 3/4.
- **Chirales Maß: bestanden, exakt.** Jedes angeregte Band zerfällt in gleich
  große links- und rechtslaufende Hälften; das Stromband trägt genau **drei**
  linkslaufende und **drei** rechtslaufende Cartan-Ströme bei relativem Impuls
  ±1, mit x = 0,96715 (n=8) → 0,99403 (n=12) gegen 1.
- **Spin 2: unmöglich.** Der TT-Projektor hat in d Raumdimensionen den Rang
  (d+1)(d−2)/2, also 0, 0, 2, 5, 9 für d = 1…5. Die native Nahtfamilie hat eine
  Raumdimension und damit **null** transversal-spurfreie Polarisationen.

**Fazit:** Zwei der vier Eigenschaften sind auf der nativen Familie Resultate,
nicht Eingaben. Die beiden anderen scheitern gemeinsam an derselben Stelle: die
Quelle beschriftet eine Zelle, jede größere Probe braucht eine Klebregel, und die
einzige Klebregel, die die Quelle motiviert (die Naht, Z4-Eichung, (D5)₁×(A3)₁ ⊂
(E8)₁), hat eine Raumdimension. **Fehlende Zutat:** eine Klebregel mit drei
Raumdimensionen, die die eine Geschwindigkeit der Naht behält.

## Frage 6 — entschieden: die Spannung überlebt das gesamte Korrekturbudget

Ein einziger Fit über (n_s, ln 10¹⁰A_s, r) mit dem einen Parameter N und festem
c3 statt drei getrennter Kalibrierungen:

| Größe | Wert |
|---|---|
| bester Fit | N = 56,634 |
| χ² / dof | 12,291 / 1 → p = 4,55·10⁻⁴ |
| Pull n_s | −3,505 σ (trägt den ganzen χ²) |
| Pull ln 10¹⁰A_s | +0,087 σ |
| r bei bestem Fit | 0,003741, unter der Schranke r < 0,038 |

**Das Korrekturbudget schließt die Lücke nicht.** Für p > 0,05 bräuchte man
Δn_s = +0,00464 (das 1,55-fache der ACT-Unsicherheit) oder −24,5 % auf A_s
(entspricht −3,94 % in c3; die exakte Zentralwertanpassung reproduziert die
−9,61 % der Vorrunde). Die unabhängig nachgerechnete exakte Slow-Roll-NLO-
Korrektur liefert auf n_s nur +0,00128 — **Faktor 3,63 zu klein** — und auf A_s
+10,31 %, also **falsches Vorzeichen** (mehr statt weniger Amplitude) und
zusätzlich Faktor 2,4 zu klein.

**Reheating-Budget.** Für T_reh ∈ [10³, 10¹⁶] GeV, gedeckelt durch die physikalische
Obergrenze bei sofortigem Reheating T_reh,max = 2,596·10¹⁵ GeV, ergibt sich
N ∈ [46,08; 55,61]. Der tilt-bevorzugte Zweig N = 80,65 liegt **25,0 e-Faltungen**
darüber — robust ausgeschlossen, unabhängig von der Amplitudenspannung. Der
amplitudenbevorzugte Zweig N = 56,62 liegt 1,01 e-Faltungen darüber; dieser
Abstand ist von der Größenordnung der Systematik der Matching-Relation selbst und
wird hier als **marginal**, nicht als Ausschluss geführt.

**r ist die einzige echte Vorhersage dieser Runde**: r spielt beim Festlegen von N
keine Rolle. r = 0,00374 liegt bei 7,5 σ für CMB-S4 (σ(r) = 5·10⁻⁴) und 3,7 σ für
LiteBIRD (σ(r) = 10⁻³) — entscheidbar, derzeit weder ausgeschlossen noch bestätigt.

**Flavour: Parameterdefizit 1.** Die unabhängig neu gebauten Overlap-Operatoren mit
Fluss 3 auf 8×8 und 10×10 liefern exakt drei Nullmoden (GW-Defekt < 1,2·10⁻¹³) und
beim konstanten Profil exakt Y = I. Über einen einparametrigen Gauß-Profilscan gibt
es **keinen** Wert, der m_μ/m_τ und m_e/m_τ gleichzeitig auf Faktor 2 trifft — auf
keinem der beiden Gitter. Es fehlt mindestens ein zweiter unabhängiger Parameter.

Als „assumed" markiert und bei jeder Zahl mitgeführt: σ(ln 10¹⁰A_s) = 0,0042
(Proxy, nicht direkt aus Tabelle 5 von 2503.14452v2 gelesen), die Rückfallvariante
0,012 für den Sensitivitätslauf, und die nicht beschaffte Korrelation zwischen
n_s und A_s (auf 0 gesetzt). Der Sensitivitätslauf ändert das Ergebnis nicht
(N = 56,708, p = 4,68·10⁻⁴).

## RH-Aktualitätsprüfung: Ursache benannt

Nicht physikalisch blockiert, sondern durch **einen** fehlenden Pfad:
`external_sources_config.json` wurzelt auf
`/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2`; das Verzeichnis
`~/Documents/Codex` existiert auf dieser Maschine nicht. Elf Review-Pins
(`codex-rh-scha-2:*`) hängen daran. `rh/catalog/map/rh_concept_map.json` ist
vorhanden. Es wurden keine Pins geändert und keine Beweismarker angehoben.

## Grenzen

Entschieden heißt hier: entschieden **unter der Lesart** „Ort = D5-Spinorgewicht"
der Fugen-Analyse und unter dem benannten C16-Modell. Die Lesart selbst ist nicht
abgeleitet. Die beiden dynamischen Schranken von Frage 1 (Kommutatornorm,
Isolationsfenster) sind numerisch und obere Schranken; sie zeigen, dass Isolation
nicht garantiert ist, nicht dass sie unmöglich ist. Alle T1–T8-Tore bleiben offen.
