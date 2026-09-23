# Endliche native Pauli- und Rohquellenprüfung

**Befund:** `PASS_EXACT_FINITE_NATIVE_PAULI_AND_RAW_AFFINE_SIGN_AUDIT`

Die im gepasteten Text angegebene Pauli-Formel war dort noch nicht gegen den
archivierten signierten nativen Tensor geprüft. Diese Restprüfung ist jetzt
geschlossen. Der neue Checker lädt das archivierte
`native_tensor.npz` mit SHA-256
`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`
und vergleicht es eintragsweise mit der unabhängigen Clifford-Rekonstruktion.
Beide liefern dasselbe ganzzahlige Tensorarray

\[
W\in\mathbb Z^{60\times2016},\qquad WW^T=8I_{60},
\]

mit genau 480 Nichtnull- und 120480 Nulleinträgen.

## 1. Pauli-Kommutator auf dem tatsächlichen signierten \(W\)

Aus jeder Zeile von \(W\) wurde die antisymmetrische Matrix \(Q_A\) gebaut,
mit

\[
P_A=\sum_{i<j}(Q_A)_{ij}f_jf_i,
\qquad a_A=P_A/\sqrt8.
\]

Der vollständige native Tensor erfüllt exakt

\[
\operatorname{Tr}(Q_B^\dagger Q_A)=16\delta_{AB}
\]

und daher

\[
\boxed{
[a_A,a_B^\dagger]
=\delta_{AB}I-\frac18 f^\dagger Q_B^\dagger Q_Af.
}
\]

Die Reihenfolge \(Q_B^\dagger Q_A\) wurde zusätzlich in einer direkten
viermodigen CAR-Darstellung mit echt komplexen Gaußschen Koeffizienten geprüft.
Die vertauschte Reihenfolge \(Q_A^\dagger Q_B\) scheitert; eine explizite
Matrixkomponente unterscheidet sich dort um \(12i\).

Jeder der 60 Kanäle ist eine signierte Paarung von 16 Fermionrichtungen. Über
alle Kanäle besitzt jede der 64 Richtungen Grad 15. Deshalb gilt exakt

\[
\boxed{
\sum_{A=1}^{60}Q_A^\dagger Q_A=15I_{64},
\qquad
\sum_A[a_A,a_A^\dagger]=60I-\frac{15}{8}N_f.
}
\]

Für eine unter der markierten Gruppe invariante Einteilchendichte
\(\rho_1=(\langle N_f\rangle/64)I\) folgt damit

\[
\langle[a_A,a_B^\dagger]\rangle
=\left(1-\frac{\langle N_f\rangle}{32}\right)\delta_{AB}.
\]

Leer ergibt \(+\delta_{AB}\), vollständig gefüllt
\(-\delta_{AB}\). Der Operator verschwindet bei mittlerer Besetzung nicht
automatisch. Die geordnete Familie der 3600 Matrizen
\(Q_B^\dagger Q_A\) besitzt über \(\mathbb Q\) exakt Rang 736 im
4096-dimensionalen Raum \(\operatorname{End}(\mathbb C^{64})\). Es wurde keine
Lie-Hülle berechnet.

## 2. Rückzug auf die rohe affine E8-Klammer

Der ältere Contract `source-dressed-native-20260920` bewies die vollständige
Zeichenverträglichkeit für die ungeraden Felder

\[
p_i=F(r_i)+e_R,
\qquad b_A=F(s_A)+2e_R.
\]

Neu geprüft wurde die tatsächlich offene rohe affine Tabelle ohne dieses
Dressing:

\[
F(r_i),\qquad F(s_A),\qquad
\epsilon(F(r_i),F(r_j)).
\]

Der Checker konstruiert diese Tabelle direkt neu. Nach einer einzigen
kohärenten Basiswahl stimmt sie mit allen 480 Vorzeichen des nativen \(W\)
überein; zugleich bleiben die vollständigen 40 \(D_5\)- und 12
\(D_3\)-Wurzelaktionen auf den 64 Fermion- und 60 Mediatorlabels kompatibel.
Das gemeinsame System umfasst 2032 Gleichungen in 176 Vorzeichen und hat über
\(\mathbb F_2\) Rang 167. Eine einzelne relative Tensorzeichenänderung ist
nicht durch Basisphasen absorbierbar.

Der Rückzug ist ein konkreter Cocycle-Befund. Mit

\[
\sigma_i=\epsilon(F(r_i),e_R)
\]

gilt

\[
\frac{\epsilon(F_i+e_R,F_j+e_R)}{\epsilon(F_i,F_j)}
=\sigma_i\sigma_j,
\]

für die Fermionwirkung entsprechend der Faktor
\(\sigma_\alpha=\epsilon(F_\alpha,e_R)\), während das
\(2e_R\)-Dressing der Mediatoren keinen Faktor hinterlässt. In der hier
festen expliziten Cocycle-Konvention ist \(\sigma_i=-1\) für alle 64
Fermionlabels und \(\sigma_\alpha=+1\) für alle 52 geprüften Produktgruppen-
Wurzeln. Die rohe und die gedresste Koeffiziententabelle stimmen daher in
dieser Eichung sogar direkt überein; der allgemeine Rückzug wurde trotzdem als
Cochain-Identität und über sämtliche 2032 Gleichungen geprüft.

Das schließt genau die bisher offene relative Phasenprüfung zwischen der rohen
affinen E8-Wurzelklammer und dem vollständigen nativen \(W\). Es ist eine
explizite Cocycle-Eichung, keine Herleitung einer physisch ausgezeichneten
Clock-Phase.

## 3. Beweisgrenze und Reproduktion

Der Befund identifiziert die signierte affine Klammer als den vollen nativen
Intertwiner. Er identifiziert affine Wurzelströme weiterhin nicht mit
kanonischen CAR-Feldern, erzeugt keine unabhängigen CCR-Mediatoren und leitet
weder den RR-Hamiltonoperator noch seine Zeit aus P1/P2 her. Die frühere
Zeitobstruktion und die physischen T1–T8-Gates bleiben davon unberührt.

Reproduktion:

```text
python3 check_native_pauli.py --output native_pauli_audit.json
python3 -OO check_native_pauli.py --output native_pauli_audit_optimized.json
```

Beide Dateien sind byteidentisch. SHA-256:

```text
57fb2dc0c1fd2f8cee862a3a27e935e028bbb75aac4c473bd6476bb8a315ebf2  native_pauli_audit.json
57fb2dc0c1fd2f8cee862a3a27e935e028bbb75aac4c473bd6476bb8a315ebf2  native_pauli_audit_optimized.json
9b6621f2272118848ca35fb3334a1aef9ca592e253fcb382f2ccf29e376d042a  check_native_pauli.py
```

Der Checker selbst verwendet keine Python-`assert`-Anweisungen. Den gepinnten
`native_source.py`-Prefix kompiliert er ausdrücklich mit `optimize=0`, sodass
auch beim äußeren `python -OO` dieselben sechs ursprünglichen `need`-Guards
ausgeführt werden. Es wurden keine Papers, Ledger, generierten Graphdateien
oder Projektverträge verändert.
