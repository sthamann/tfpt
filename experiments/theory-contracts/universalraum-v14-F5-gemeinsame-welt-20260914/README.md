# universalraum-v14-F5-gemeinsame-welt-20260914

NON-RH. Exploration (`experiments/theory-contracts/`). Keine Promotion: kein Marker
in `verification/`, Ledger, Papers oder Website. **T3, T4, T5, T7 bleiben offen.**

Anschluss an Follow-up-Frage 5 von v1.4, Ergebnisse §9 (T3/T4/T5/T7) und Fugen
§§3+6 (Clebsch, Z4-Glue). Vorgänger der *getrennten* Diagnostiken:
`universalraum-five-source-frontier-20260914/frontier.py` (gepinnt).

## Eine Familie, nicht vier Modelle

Kandidat **F** = Clebsch-Graph C16 × (ℤ/Lℤ)^d, mit nativer Clebsch-Kopplung
(E8-Superaustausch, stark regulär (16,5,0,2)), Overlap-Dirac auf dem 2-Torus-Faktor
mit eingesetztem U(1)-Fluss, bilinearem Tensorobservable auf demselben Box-Laplace
und Sinus-Weyl-Symbol auf denselben Momenta. Alle Diagnostiken lesen denselben
Parameterblock in `checker.py` (`FAMILY`).

Die Z4-gekoppelte Alternative SU(4)-Ring ⊗ 10 Majoranas ist ein *anderes*
Hilbert-Raum-Objekt (1D-Ring, Glue-Gesetz noch nicht konstruiert) und wird als
Negativkontrolle geführt, nicht als zweite Welt.

## Ergebnis

**Keine gemeinsame Welt.** F trägt die Teiltests, nicht gleichzeitig gemeinsamen
Kegel, 3+1D-Propagation, Spiegelgap, chirales Maß und masselosen Spin-2.

| Teilresultat (nicht Welt-Ableitung) | Zahl |
|---|---|
| Wärmespur faktorisiert exakt; t=8, L=64 ⇒ ds ≈ 1.0167118 d für d=1..4; L=16,32,64; Dimension-in = Dimension-out | T3-heat |
| Overlap D = I + γ5 sign(γ5 D_W); Fluss 3 auf 8×8 und 10×10: 3 Nullmoden, Index −3, GW-Defekt < 1.2e−13 | T4-torus |
| Fluss 0: 2 Nullmoden, Index 0; Fluss 1 bzw. 4: andere Zahlen | T4-Kontrolle |
| Freie Bilinear-Schwelle 2m; TT-Projektor Rang 2, kein Pol; Ward (g1−g2)(p3−p1)=0 | T7-frei |
| Sinus-Weyl d=3: 8 Knoten, chirale Gesamtladung 0 | T7-Weyl |
| Clebsch dreiecksfrei: K4-Vierfachzelle nicht einbettbar | T5-negativ |

**Fehlende Selektoren (No-go):**

1. **Familie+Kegel-Auswahl.** Dieselbe Familie gibt jede eingesetzte Dimension
   zurück; zwei Geschwindigkeiten passen auf denselben Graphen; die Clebsch-Faser
   ist kompakt (Durchmesser 2); der Wärmekern ist am Antipodenpunkt positiv,
   also kein kausaler Propagator.
2. **Fluss/Geometrie-Herkunft.** Der Index ist der *hineingesteckte* Fluss.
   Spectator-C16 kopiert Nullmoden ×16 (48 statt 3). Drei Nullmoden brauchen
   eine extra interne Masseprojektion auf den eindeutigen Clebsch-Nullmode.
3. **3+1D-Propagation + Spiegelgap.** Overlap ist räumlich 2D; Wärme behandelt
   d=1,2,3,4 gleich; Weyl-Doubler löschen die Nettoladung. Kein Spiegelgap.
4. **Masseloser Spin-2 aus derselben Quelle.** TT ist kinematisch; die freie
   Bilinearform ist bei 2m gegappt; Ward erzwingt universelle Kopplung nur
   *falls* ein weicher Pol existiert — F liefert keinen.
5. **T5-Zelle vs. nativer Graph.** K4 steckt nicht im Clebsch-Graphen.
   CAR/F4 leben auf einem anderen Raum.

Firewall: Verdict `NO_GO_MISSING_SELECTORS`. Search target, kein Claim, kein `[E]`.

## Reproduktion

```sh
cd experiments/theory-contracts/universalraum-v14-F5-gemeinsame-welt-20260914
python3 -B checker.py validation.json
python3 -B -m unittest test_checker          # auch mit -OO
```

Abhängigkeiten: numpy, scipy, sympy. Keine Änderung an Ledger, Papieren, Katalogen.
