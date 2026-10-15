# Liefert die minimale Verpackung eine echte Eindeutigkeit von B_Σ und der Algebra?

Auftrag (Codex, 15.10.): Prüfen, ob das abschließende Boundary-Reconstruction-Theorem eine
echte Eindeutigkeit von B_Σ bzw. der Algebra liefert oder nur die Rekonstruktion aus einem
bereits gegebenen vollständigen Randdatum. Zuerst sind vorhandene Ausschlüsse zu prüfen. Keine
Perturbationsfamilie, kein universeller Nicht-Eindeutigkeitssatz.

Status **PARTIAL** (Quellen-Typisierung), keine Promotion. `python3 checker.py`: 24
Stellenpins in `_archive/tfpt-45/source_extracts/01_boundary_kernel_source.tex` (zitiert als
„01“) und in den Vorgänger-Contracts; keine Modellrechnung.

## Vorhandene Ausschlüsse (nicht neu)

* `source-three-route-closure-20260922/SELECTION.md:5–60`: Die vier Defekte liefern für sich
  keinen Eindeutigkeitsbeweis. Bedingte Eindeutigkeit gibt es nur relativ zu einem schon
  ausgewählten vollständigen Schwingerkern (K) und einer injektiven Generatorabbildung (G).
* `source-boundary-lift-selection-20260922/PROOF.md` §1 und §3:
  - Terme nullter Ordnung sind durch das Hauptsymbol nicht festgelegt (Bär–Ballmann §3.2).
  - Dieselbe elliptische Klasse bedeutet nicht dieselbe Domäne (Gegenbeispiel D_α).
  - Der beschränkte Nullordnungsschritt ist per Kato–Rellich repariert. Das beweist Zulässigkeit,
    keine Auswahl.

## U1 – Die Eindeutigkeit ist reduziert, nicht bewiesen

* 01:646–653 behauptet einen bis auf unitäre Äquivalenz **eindeutigen** essentialisierten
  defektminimalen Vertreter B_min.
* Der Beweis (01:672–683) liefert die Existenz aus der Wohlfundiertheit von N⁴. Für die
  Eindeutigkeit verweist er auf den Invarianzsatz und auf „the boundary reconstruction theorem“
  (01:678–683).
* Der Invarianzsatz zeigt nur, dass Minimierer unter streng monotonen Koordinatenwechseln und
  Äquivalenzen erhalten bleiben. Sein eigener Beweis sagt (01:587–593): „Uniqueness is then
  reduced to classification of the final minimized stratum …“.
* Ein Satz mit dem Namen bzw. Label „boundary reconstruction theorem“ existiert in den
  Quellauszügen nicht (Pin U1, über alle `source_extracts/*.tex`).
* Der nächstliegende Rekonstruktionssatz (01:94–170) beginnt mit „Let T_bound be as above“, und
  T_bound enthält B_Σ bereits (01:66–80). Er rekonstruiert τ_dbl, ι_C, D_ref und D_rel **aus**
  dem gegebenen Datum.

**Ergebnis:** In der Quelle steht eine Rekonstruktion aus einem gegebenen vollständigen
Randdatum. Die Eindeutigkeit von B_min, also von D_+ und damit B_Σ über die Kragennormalform
01:676–678, ist genau so stark wie die nicht gelieferte Aussage „das minimale Stratum
Σ_min = {B : 𝔇(B) = 𝔇_min}/≅ ist einelementig“.

Hier wird **kein** Gegenbeispiel behauptet. Entscheidend wäre eine explizite Klassifikation von
Σ_min oder ein tatsächlich zulässiges minimales Gegenpaar. Beides liegt nicht vor. Dafür müssten
außerdem der „declared reference sector“ (01:640) und damit die Endlichkeit der relativen
Wirkung konkret gegeben sein.

## U2 – Die Korollarlücke (Codex' Punkt, bestätigt)

Korollar 01:605–620 benutzt: Minimieren über Seed_op ist äquivalent zum Minimieren über ganz
SBord^adm. Logisch gilt nur min_{Seed_op} 𝔇∘C_seed ≥ min_{SBord} 𝔇. Gleichheit gilt genau dann,
wenn das Bild von C_seed das minimale Stratum trifft. C_seed(S_min) = B_min verlangt zusätzlich
U1.

Für C_seed steht nur eine „Proof architecture“ (01:516–521). Dass der Funktor dieses Stratum
erreicht, ist dort nicht gezeigt.

## U3 – Welche natürlichen Abbildungen vorhanden sind und welche fehlen (enger gefasst)

Ein fehlender eigener Slot im Ausgabetupel beweist **nicht**, dass Sektoren oder Zeit in
(A_+, H_+, D_+, J, Γ) nicht kodiert sein können. Die frühere Formulierung („liegt nicht im
Wertebereich“) ist zurückgenommen. Konkret:

* **Vorhanden (Architektur, Standardmathematik):** Die OS-Rekonstruktion bildet
  (A_loc, Θ, ω) auf den OS-Raum H_+ und die Transfersemigruppe T_s = e^{−sH} ab (01:516–521).
  Damit ist die Zeit τ_t über T_s in H_+ kodierbar.
  Zu den Sektoren: Nach Doplicher–Haag–Roberts kodiert ein Vakuumnetz seine lokalisierten
  Sektoren selbst. Ein Sektorinhalt könnte also über das Netz in die Ausgabe gelangen.
* **Fehlend 1 – Generatorabbildung (G):** T_s ↦ D_+ bzw. D_coll ist im Original nicht
  angegeben. Dass D_coll auf demselben Raum H_+ wirkt, wird ebenfalls nicht gesagt. Der Vorgänger
  `source-three-route-closure-20260922/SELECTION.md` führt das als (G).
* **Fehlend 2 – Netz zu Algebra:** Eine Abbildung A_loc ↦ A_+ fehlt. Sie müsste die
  Lokalisierungsstruktur erhalten, und A_+ hat ein kommutatives Zentrum mit Gelfand-Spektrum M_+
  (01:66–80). DHR braucht das Netz, nicht eine einzelne Algebra.
  Ein einzelnes lokales von-Neumann-Algebra-Objekt legt die Sektoren nicht fest: Verschiedene
  Netze haben dieselbe hyperfinite Typ-III₁-Lokalalgebra, vgl.
  `articles/2026-08-30/mmst_charged_scaling_limit_en.tex` (L4).
  Ob A_+ die Netzstruktur mitführt, sagt die Definition 01:630–643 nicht.

Folgerung: Ob die Minimierung eine Sektorerweiterung D8 → D8 ∪ (D8+s) samt konsumierendem
Operator auswählt, ist weder gezeigt noch ausgeschlossen. Es hängt an den beiden fehlenden
Abbildungen. Unabhängig davon besteht die Typlücke zwischen OS-Vielteilchenraum H_+ und den
Dirac-Kragendaten (01:630–643).

## U4 – Physical operationality verlangt keine Minimalität

Das Axiom 01:622–625 sagt nur: „The physically realized world is represented by an object of
Seed_op.“ Daraus und aus der Wohlfundiertheit folgt, dass ein defektminimales Seed existiert.
Es folgt nicht, dass die physikalische Welt dieses Seed ist.

Die Quelle räumt das selbst ein. `04_qft_source.tex:2103–2109` („Primitive honesty“): Bewiesen
sei der Übergang „from a minimal operational seed“, und es werde „internal rigidity before
ultimate primitive minimality“ etabliert. Physikalische Minimalität ist also eine zusätzliche,
nicht als Axiom formulierte Prämisse.

Nebenbefund: Die Orientierungsfassung `00_orientation_source.tex:251` nennt Eckenzahl und
Kerndimension als Koordinaten. 01:562–567 nimmt die Eckenzahl ausdrücklich heraus. Das ist ein
Versionsunterschied, kein neuer Einwand.

## U5 – Gibt es SF = 1 in derselben Zulässigkeitsklasse?

Der Beweis 01:672–675 schließt aus der Nichtleere der Menge positiver Werte: „hence the minimal
positive value is |SF| = 1“. Dafür braucht es einen Zeugen mit SF = 1 in der Klasse.

* **Was U_Σ in den Originalen explizit ist:**
  - `06_cosmology_source.tex:16–25` (= tfpt-42.tex:9758–9760): U_Σ := P_adm e^{−ℓ|B_Σ|} P_adm,
    positiv und spurklasse, mit 0 < U_Σ < P_adm;
  - `03_em_flavor_source.tex:94–100`: U_Σ^min := |ψ_Σ⟩⟨ψ_Σ|, ein Rang-1-Projektor;
  - `05_metrology_source.tex:1390–1393`: eine Skalenfamilie in −log det_adm(1 − U_Σ).

  Keines davon ist ein Unitärloop. Für jeden normstetigen Weg mit 0 < U < P_adm kreuzt kein
  Eigenwert die Niveaus 0 oder 1. Der Spektralfluss durch diese Niveaus ist deshalb null.
  Diese Objekte können SF(U_Σ) = 1 nicht tragen.
* **Das Objekt mit SF = 1** ([u_Σ] ∈ K¹(S¹), tfpt-42.tex:2323–2353) wird nur behauptet:
  „Along a single positive seam circuit the spectral flow changes by one“. Konstruiert wird es
  nicht. Die Definition von SBord^adm (01:630–643) sagt nicht, wie U_Σ aus dem Tupel B entsteht.
  Im Seed ist [u_Σ] ein eigener Eintrag, ohne Kopplung an die Bedingungen (i), (ii) und (iv)
  (01:486–495).
* **Vorhandene Zeugen außerhalb der Klasse:** `verification/v991_detline_bulk_edge.py:3–25`
  (v367-QWZ-Kragen) gibt Kantenzweig unten SF = +1, oben −1 über die Verdrillungsschleife und
  Chern +1. Das ist ein endlicher Gitterschatten. Er ist kein elliptischer Dirac-Kragen nach
  01:630–643, und Reflexionspositivität sowie relative Wirkung sind dort nicht geprüft.
  Standardmathematisch hat −i∂_θ + t auf S¹, t ∈ [0, 1], SF = 1; das ist nicht in der Quelle und
  nicht gegen (ii) und (iii) geprüft.

**Ergebnis:** Eine primitive SF = 1-Konstruktion **innerhalb** der Zulässigkeitsklasse liegt
weder im Original noch in vorhandenen Resultaten vor. Zusätzlich fehlt im Original die
Zuordnung B ↦ U_Σ(B) als Unitärloop. Auch die Werte von d_1, d_2 und d_3 auf dem minimalen
Stratum sind in den Auszügen nur definiert (01:545–558), nicht berechnet.

## Erste nicht gegebene Quellaussage

Benötigt wird eines von beiden:

1. eine explizite Klassifikation von Σ_min samt deklariertem Referenzsektor und expliziter
   C_seed-Konstruktion, mit dem Nachweis, dass C_seed Σ_min trifft;
2. ein zulässiges minimales Gegenpaar mit geprüfter Reflexionspositivität, SF, Rang,
   Determinantengrad, Nullität und relativer Wirkung.

Für die Sektorfrage braucht es zusätzlich die Abbildungen (G) und A_loc ↦ A_+ samt Netzstruktur.
Für d_0 braucht es die Zuordnung B ↦ U_Σ(B) als Unitärloop samt einem zulässigen SF = 1-Zeugen. In den geprüften Originalen steht keines davon.
