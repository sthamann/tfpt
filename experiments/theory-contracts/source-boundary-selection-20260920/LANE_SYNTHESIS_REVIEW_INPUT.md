# Unabhängige Prüfung der Bridge-Rechnungen

Stand: 2026-09-20. Geprüft wurden ausschließlich `check_bridges.py`,
`bridge_checks.json`, `neutral_determinant_bridge.md` und
`time_source_bridge.md`. Der Checker wurde aus einer temporären Kopie
ausgeführt, damit kein geliefertes Ergebnis überschrieben wird.

## Ergebnis

Der Checker läuft mit **18/18 PASS**; die temporär erzeugte
`bridge_checks.json` ist inhaltlich identisch mit der gelieferten Datei. Die
endlichen algebraischen Aussagen sind korrekt. Das JSON markiert selbst
`native_P1_P2_selection_proved=false`, `full_cocycle_or_continuum_replay=false`,
`projected_response_suffices_for_full_source_functional=false` und
`physical_T1_T8_closed=[]`. Diese Reichweitenbegrenzungen sind sachgerecht.

Die beiden Berichte ziehen daraus im Wesentlichen die richtige Konsequenz:
Das vorhandene neutrale Determinantenfunktional ist ein phasentreuer,
reproduzierbarer Ausgangspunkt für eine weitere Source-Reduktion. Es ist noch
keine physische Mehrzeitantwort, keine 4D-chirale Maßwirkung, kein QCD-/EM-
Anomaliefunktional und kein Axionfeld.

## K/V-Konvention und Skalierungsdimensionen

Die Rechnung verwendet zwei verschiedene quadratische Formen, die getrennt
bleiben müssen:

```text
K = diag(1,...,1,-1)                 Signatur (9,1)
V = K + 2 K v v^T K                  positive Energieform
```

Die exakten Kontrollen liefern

```text
n^T K n = 0,       n^T V n / 2 = 1,       n.n / 2 = 9
z^T K z = 0,       z^T V z / 2 = 4,       z.z / 2 = 1
b^T K b = 2,       b^T V b / 2 = 1,       b.b / 2 = 5.
```

Außerdem ist `V` positiv mit Eigenwerten `1` achtfach sowie
`17±12 sqrt(2)`; der kleinste ist positiv. Damit sind sowohl die
`reconstructed_scaling_dimensions` `(1,4,1)` als auch die `free_scaling_dimensions`
`(9,1,5)` als die jeweils im Checker verwendeten Quadratikwerte korrekt.

Die Benennung als *Skalierungsdimension* ist aber nur algebraisch, solange
nicht zusätzlich ein physischer CFT-/Current-Kontext, eine Zustandsnormierung,
ein Stress-Tensor beziehungsweise eine Quelle für `V` hergeleitet ist. `K`
ist die Lorentz-artige Paarung; `V` ist eine eigens konstruierte positive
Energieform. Die Werte aus `V/2` dürfen nicht mit den freien `Euclid/2`-Werten
vermischt oder als bereits physisch ausgewählte Dimensionen ausgegeben werden.
Auch die Wurzelintegralität und die unimodulare Basis `W` liefern keine solche
physische Auswahl.

## Vollständiger Determinant gegenüber projizierter Antwort

Die Schur-Rechnung ist exakt, aber endlich und bedingt auf Invertierbarkeit:

```text
det D = det(D_QQ) det(S_P),
S_P = D_PP - D_PQ D_QQ^{-1} D_QP.
```

`retained_inverse` zeigt, dass die projizierte Antwort den entsprechenden
Schur-Block korrekt reproduziert. Der zusätzliche dunkle Faktor `q` lässt den
retained inverse unverändert, multipliziert aber den vollständigen
Determinanten mit `q`. Das beweist genau die beabsichtigte Warnung: Eine
projizierte Antwort bestimmt den vollen Determinanten nicht.

Die Formulierung „dark factor“ darf dabei nur für einen von allen geprüften
Parametern und Hintergründen unabhängigen Faktor als reine Normierung gelesen
werden. Sobald `q=q(phi,A)` oder eine Komplementdeterminante von einem
Hintergrund beziehungsweise einer Phasenfamilie abhängt, trägt sie selbst zur
Antwort und möglicherweise zur Phase bei. Dann ist sie kein wegwerfbarer
Normierungsfaktor. Bei Nullmoden oder nichtinvertierbarem `D_QQ` braucht die
Identität eine determinantlinienartige beziehungsweise regulierte Form; der
formale inverse Block im Checker deckt diesen Fall nicht ab.

Die Berichte ziehen diese Grenze bereits richtig: Ein Low-Window- oder
Current-Determinant genügt nicht, um die Komplementphase, den chiralen
Jacobian oder einen 4D-Wess--Zumino-Beitrag zu bestimmen. Der finite QWZ-
Determinant ist vollständig für das deklarierte endliche gaußsche Modell,
nicht vollständig für eine hypothetische TFPT-4D-Quelltheorie.

## Operatorwertiger Carry und zyklisches Q

Das Drei-Sektor-Beispiel ist ein gutes lokales Gegenbeispiel zur skalarisierten
Vakuumkompression. Die exakte Schurantwort reproduziert die projizierte
Resolvente, während

```text
Sigma[0,1] = j*k/(z-E1)
```

den im skalaren Vakuumansatz verlorenen Kreuzterm sichtbar macht. Das stützt
die Forderung nach einem operatorwertigen Übergangsmaß beziehungsweise nach
der vollständigen `P/Q`-Antwort.

Daraus folgt jedoch **kein universelles Nichtidentifizierbarkeitstheorem für
zyklische Q-Projektoren**. Bewiesen ist nur:

1. ein konkretes dreiteiliges Modell kann durch eine zu grobe skalare
   Kompression Information verlieren; und
2. eine ausdrücklich neutrale Spectator-/Completion-Konstruktion kann gleiche
   neutrale Determinanten bei verschiedener verdeckter History erzeugen.

Die volle operatorwertige Resolvente kann den Kreuzterm behalten. Für einen
allgemeinen zyklischen `Q`-Mechanismus wären zusätzliche Voraussetzungen über
Zustand, Hamiltonoperator, Projektoren, alle Übergangsecken und die gemessene
Antwort nötig. Die Berichte sollten daher „unter der angegebenen neutralen
Completion“ beziehungsweise „für diese skalare Kompression“ sagen und keine
universelle Unidentifizierbarkeit behaupten.

## Was die positiven Berichte tatsächlich tragen

Der QWZ-Linienbefund verbindet für den deklarierten Ein-Kopien-
`1+1D`-Grenzwert denselben Operator mit negativem Spektralzustand, lokaler
geladener CAR-Linie und Zeitentwicklung. Das ist ein echter gemeinsamer
Quellbaustein. Er liefert aber nur einen Kanal pro Rand; acht Querplätze sind
keine acht Materiesorten.

Das neutrale Funktional besitzt für die konkret geprüften geordneten Wörter
eine echte komplexe Phase. Seine Endpunkte sind jedoch zunächst räumliche
Randparameter und seine Vorzeichen formale Einfügeladungen. Eine Abbildung auf
eine gemeinsame physische Zeit, zwei verschiedene Down-/Lepton-
Massdeformationen und deren regulierte vollständige Maßwirkung fehlt.

Der `L_0`-gegen-`H_delta`-Vergleich ist als Warnung gegen neutrale Zeitchecks
korrekt: Zahlenerhaltende Ströme können den Zusatzterm übersehen, während
Paar- oder Spinorfelder ihn sehen. Die bedingte affine Auswahl von `H=aL_0+c`
setzt bereits einen gemeinsamen same-space-Current-Modenraum voraus; sie
beweist diese Quelle nicht.

Weder der Checker noch die Berichte liefern daher einen 4D-Beweis, einen
QCD-/EM-Anomaliebeweis, einen Axionbeweis oder eine physische Perioden-/
Domain-Wall-Aussage. Der korrekte nächste Test ist der bereits angegebene
vollständige Ward-Schur-Test einer **source-selektierten** parametrierten
Quellfamilie: dieselbe Quelle muss Zustand, geladene Zeit, beide
Phasentangenten, Komplementdeterminant, Regulator und Farb-/EM-Hintergründe
tragen. Erst danach sind Rang und kompaktes Phasengitter sinnvoll.

## Kurzfazit

- **18/18** endliche Checkeridentitäten bestätigt.
- K/V-Werte algebraisch korrekt, physische Skalierungsdimension offen.
- Full-vs-Schur-Unterscheidung korrekt; ein parameterabhängiger dunkler Faktor
  ist physische Antwort, keine Normierung.
- Carry-Gegenbeispiel korrekt für die konkrete skalare Kompression; kein
  universelles zyklisches-Q-Nichtidentifizierbarkeitstheorem.
- Neutrale komplexe Phase ist ein positiver Source-Reduktionsbaustein, aber
  noch keine 4D-/Axion-/Anomalieherleitung.
