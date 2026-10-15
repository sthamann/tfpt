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

## U3 – Was die Minimierung typmäßig liefern kann

* **Codomäne:** Objekte von SBord^adm sind (A_+, H_+, D_+, J, Γ) (01:630–643). Die Ausgabe des
  Funktors ist T_∂(S) = (A_+, H_+, D_+, J, Γ, B_Σ) (01:505–512). Das lokale Netz A_loc, die
  Zeit τ_t und der Zustand ω kommen darin nicht vor.
* **Defekte:** Die vier Koordinaten (01:545–558) sind |SF|, wesentlicher endlicher Rang,
  Determinantengrad und reduzierte Randnullität. Im Quellkern gibt es keine DHR-,
  Superauswahl-, Orbifold- oder Twisted-Sector-Daten (Pins U3).
* **Typlücke im Funktorbeweis:** H_+ wird als OS-Raum aus dem positiven Netz rekonstruiert
  (01:516–521). Verlangt ist dagegen ein elliptischer Dirac-Operator auf einem einseitigen
  Kragen (01:630–643) mit kommutativem Zentrum, dessen Gelfand-Spektrum eine Mannigfaltigkeit
  ist (01:66–80). Die Abbildung vom OS-Vielteilchenraum auf diese Spektraltripeldaten ist nicht
  angegeben.

**Folgerung (Typaussage, kein Nicht-Eindeutigkeitssatz):** Selbst eine bewiesene Eindeutigkeit
von B_min bestimmt nur ein einseitiges Randdatum. Eine Sektorerweiterung D8 → D8 ∪ (D8+s) und ein
Operator, der sie konsumiert, liegen nicht im Wertebereich dieser Minimierung. Sie könnten nur
aus A_loc selbst kommen, also aus einer Seed-Eingabe, und zwar über eine Transportabbildung,
die C_seed nicht angibt. Ob Seeds mit verschiedener Sektorstruktur verschiedene Defektvektoren
haben, bleibt offen, weil C_seed nicht explizit ist.

## Erste nicht gegebene Quellaussage

Benötigt wird eines von beiden:

1. eine explizite Klassifikation von Σ_min samt deklariertem Referenzsektor und expliziter
   C_seed-Konstruktion, mit dem Nachweis, dass C_seed Σ_min trifft;
2. ein zulässiges minimales Gegenpaar mit geprüfter Reflexionspositivität, SF, Rang,
   Determinantengrad, Nullität und relativer Wirkung.

Für die Sektorfrage braucht es zusätzlich eine Transportabbildung von A_loc in die gewählte
Ausgabe. In den geprüften Originalen steht keines davon.
