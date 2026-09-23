# TFPT / Universalraum: ein isolierter geladener Pol auf dem nativen Grundzustand

**Forschungsfortsetzung v1.6.3 · 15. September 2026**

## Ergebnis und Reichweite

Die Rechnung ist auf den tatsächlich bewiesenen Grundzustand des angegebenen
Fockmodells übergegangen. Dort besitzt die Antwort der **ursprünglichen
Fermionoperatoren** einen isolierten Entnahmepol mit streng positivem,
großem Gewicht. Das wird durch endliche Variationsräume, rationale
Spektralschranken, Symmetrie und exakte Momentidentitäten nachgewiesen.
Eine vollständige Diagonalisierung des Grundzustands oder sämtlicher
geladenen Zustände wird dafür nicht benötigt.

Für genau **μ=0 und g/Δ=1/20** gilt pro ursprünglicher Fermionmode:

\[
\boxed{0.007737\Delta<\epsilon_{\mathrm{low}}<0.062277\Delta,\qquad
0.864972353\ldots<Z_{\mathrm{low}}<0.9759375.}
\]

Das Spektrum der übrigen Entnahmeantwort beginnt oberhalb
\(0.379636\Delta\), das der Addition oberhalb \(0.329636\Delta\).
Die Energieintervalle sind **bewiesene Einschließungen**, keine gemessenen
Zentralwerte. Der Entnahmepol liegt in der retardierten Antwort bei
\(z=-\epsilon_{\mathrm{low}}\).

**Der Zusammenhang ist lokal und modellbedingt.** Der primitive gesamte
Operationssatz, die physische Auswahl von μ=0, ein vollständiges
relativistisches Feldwörterbuch und räumliche Ausbreitung sind weiterhin
nicht hergeleitet. Die nun bewiesene lokale Spektrallinie ist deshalb noch
kein Nachweis eines propagierenden relativistischen Teilchens.

## 1. Quellen, Fortsetzung und Prüfumfang

Grundlage sind die acht vom Nutzer benannten v1.6-, v1.6.1- und
v1.6.2-Dateien. Ihre SHA-256-Werte stehen in `input_manifest.json`.
Die sechs Markdown-Texte wurden mit Schwerpunkt auf Modellvertrag und
offenen Anschlussbedingungen gelesen; die beiden PDFs wurden extrahiert,
die einschlägigen Operations- und Zustandsabschnitte abgeglichen und
repräsentative Seiten visuell geprüft. Das ist kein neuer Vollaudit aller
168 Seiten des Hauptbuchs oder aller darin übernommenen älteren Ergebnisse.

Zusätzlich wurde das ursprüngliche Archiv
`TFPT_Native_Bank_Pruefpaket_2026-09-14.zip` in einer getrennten Arbeitskopie
vollständig normal und mit Python `-OO` ausgeführt. Beide Läufe endeten
erfolgreich. Die 14 abschließend erzeugten mathematischen JSON-Berichte
stimmen nach Entfernen von Laufzeitfeldern mit den archivierten Berichten
überein. Darin enthalten sind die vollständige Tensorrekonstruktion,
Casimirprüfung, N=4-Prüfung, vollständige Normsummen bis Ordnung vier,
die unabhängige Symmetriespurrechnung sowie die Grundzustandszertifikate.

Der neue Prüfer besteht normal und optimiert mit identischen JSON-Bytes:
**317 explizite Prüfbedingungen**. Komponentenprüfungen und Wiederholungen
sind darin enthalten; 317 ist keine Anzahl unabhängiger Entdeckungen.

Die Ausgangsdokumente und fremden Forschungsordner wurden nicht inhaltlich
verändert. Arbeitsaufforderungen innerhalb der Quellen wurden als
Quelleninhalt behandelt. Kein T1–T8-Tor wird geschlossen.

## 2. Ein durchgehender Modellvertrag

Es bleibt bei

\[
H=\Delta N_b+gX,\quad
X=Q_++Q_-,\quad Q_+=\sum_A b_A^\dagger P_A,\quad Q_-=Q_+^\dagger,
\]
\[
P_A=\sum_{i<j}W_{A,ij}f_jf_i,\quad
N=N_f+2N_b,\quad WW^\dagger=8I_{60}.
\]

Es gibt 64 Fermion- und 60 Bosonmoden. Die Fermionen erfüllen die CAR,
die Bosonen die CCR. Die 480 nichtverschwindenden Kopplungen behalten
ihre ursprünglichen Vorzeichen. Δ ist positiv, g reell; für die Zahlen
dieses Berichts wird g/Δ=1/20 verwendet. Energievariablen z haben
Energieeinheiten; Zeiten würden den Faktor ℏ enthalten.

Die ursprüngliche Tensorquelle hat SHA-256
`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.
Frisch geschriebene NPZ-Dateien können andere ZIP-Zeitstempel besitzen;
dieser Dateipin bezeichnet die ursprüngliche Quelldatei.

**Gesetzt bleiben:** Fockrealisierung, Hamiltonoperator, Energievergleich
zwischen Ladungssektoren und Testwert des Parameters. Aus der Rechnung
folgt keine Begründung, warum die physische Quelle genau diese Angaben wählt.

## 3. Operationssatz: Was die vorhandene Clock tatsächlich hinzufügt

### 3.1 Verfügbarkeit und mathematischer Abschluss sind verschieden

| Ebene | Was tatsächlich dokumentiert ist | Was zusätzlich benötigt wird |
|---|---|---|
| Matrixcompiler | Endliche markierte Matrizen, Wurzeloperationen und bedingte Clifford-Synthesen | Native Bereitstellung von Laboralphabet, Normalisierung, kohärenter Kontrolle und Records |
| Festes Fockmodell | Zeitentwicklung mit H | Unabhängiges Schalten von X und N_b folgt nicht allein aus der Angabe von H |
| Kontrollvertrag X, N_b | Berechenbare erzeugte Operatoralgebra | Jede beliebige Linearkombination ihrer Elemente ist nicht automatisch ein ausführbares Instrument |
| Vorzeichenrichtiger Clock-Lift G | Kovarianz mit W und J unter benannter Rahmenidentifikation | Vollständiger physischer Adapter; Clock ist kein nachgewiesener Hamiltonzeitschritt |
| Geladene Probe f | Mathematisch wohldefinierte Antwort und CAR | Ein ausführbares Instrument muss Ladung an einen Detektor übertragen können |

Der vorhandene Nachweis liefert somit keinen vollständigen primitiven
Operationskatalog. Er erlaubt aber, den **genau benannten erweiterten
Kontrollvertrag** quantitativ auszuschließen oder zu bestätigen.

### 3.2 Neuer exakter Abschluss im N=3-Sektor

Für \(\mathcal A=\operatorname{alg}^*(X,N_b,G)\) mit dem dokumentierten
Lift \(G^6=I\) wurden die Clock-Multiplizitäten in allen bisherigen
Spektralblöcken exakt bestimmt. Die Spalten gehören zu
\(\exp(2\pi i j/6)\), j=0,…,5.

| Raum / Multiplizitätsfaktor | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| Dunkler Dreifermionraum | 6384 | 6280 | 6280 | 6384 | 6280 | 6280 |
| Dunkler Boson-Fermionraum | 16 | 8 | 8 | 16 | 8 | 8 |
| Aktiver Faktor λ=7 | 560 | 440 | 440 | 560 | 440 | 440 |
| Aktiver Faktor λ=10 | 112 | 88 | 88 | 112 | 88 | 88 |
| Aktiver Faktor λ=12 | 80 | 40 | 40 | 80 | 40 | 40 |

Die aktiven Zeilen sind jeweils mit einem Zweiniveauraum zu multiplizieren.
Alle 45504 Zustände sind erfasst. Daher

\[
\dim\mathcal A=6(1+1+4+4+4)=84,
\]
\[
\dim\mathcal A'=240742144,
\qquad
\dim\operatorname{alg}^*(X,N_b)'=1444233216.
\]

Der Kommutant \(\mathcal A'\) besteht aus den Operatoren, die mit sämtlichen
Kontrollen vertauschbar sind. Er bleibt eine direkte Summe voller
Matrixalgebren auf den Tabellenmultiplizitäten; in den aktiven Faktoren
wirkt zusätzlich die Identität auf dem Zweiniveauraum.

**Beweisweg.** Auf dem 3840-dimensionalen Boson-Fermionraum wurde
\([G,C_3C_3^\dagger]=0\) geprüft. Die Spektralprojektoren sind ganzzahlige
Polynome in \(S=C_3C_3^\dagger\), geteilt durch bekannte ganze Nenner.
Ihre Spuren gegen G^k liefern die Charaktere. Im Dreifermionraum verwendet
man die Außenpotenzidentität
\(\operatorname{tr}\Lambda^3T=((\operatorname{tr}T)^3-
3\operatorname{tr}T\operatorname{tr}T^2+2\operatorname{tr}T^3)/6\)
und zieht die aktiven Anteile ab. Die Fourierzerlegung erfolgt exakt im
sechsten Kreisteilungskörper. Kein gerundetes Spektrum bestimmt die Ränge.

**Folge.** Die Clock unterscheidet zusätzliche Phasenklassen, beseitigt
aber weder die großen Multiplizitätsräume noch die Ladungserhaltung.
Wörter aus diesen neutralen Kontrollen erzeugen keinen Operator f_r.
Dass G existiert, macht die geladenen Präparations- und Messinstrumente
noch nicht verfügbar.

## 4. Der native Grundzustand ist unter dem Modellvertrag abgesichert

Der erneute Archivlauf bestätigt den vorhandenen Satz: Für
\(0<|g|/\Delta\le1/20\) besitzt H einen eindeutigen globalen Grundzustand
\(\Omega\) im Sektor N=64, invariant unter Spin(10)×SU(4).
Bei g/Δ=1/20 genügen hier die rationalen Einschließungen

\[
-1.158089\Delta<E_0<-1.129636\Delta,
\qquad \operatorname{gap}(H)>0.007737\Delta.
\]

Die Beweiskette ist vollständig modellintern:

1. Auf dem gesamten fermionischen Fockraum gilt
   \(V=\sum_AP_A^\dagger P_A=(15N_f-C_{10}-C_4)/2\).
2. Quadratvervollständigung und Casimiruntergrenzen schließen alle
   konkurrierenden Zahlensektoren einschließlich unendlich hoher
   Bosonenbesetzungen aus.
3. Der voll besetzte Zustand F und \(Q_+^kF\), k=0,…,4, geben eine
   fünfdimensionale Variationsmatrix unterhalb der Konkurrenzschranke.
4. Im N=64-Sektor ist der Nullbosonraum eindimensional. Sein Komplement
   liegt oberhalb −3Δ/4. Minimax beweist Eindeutigkeit; die Symmetrie
   erzwingt den Singulettcharakter.

Die exakten Normquadrate der fünf Vektoren sind
\(1,480,439680,575078400,952296652800\).
Der erste und dritte Schritt bestimmen **nicht den vollständigen
Eigenvektor**. Ein Variationswert wird hier nicht als exakte Energie ausgegeben.

### 4.1 Etwas engere Belegungsgrenzen

Schreibe \(\bar b=\langle\Omega|N_b|\Omega\rangle\). Dann
\(\langle N_f\rangle=64-2\bar b\). Aus Cauchy–Schwarz und
\(V\le480-15N_b\) im N=64-Sektor folgt

\[
E_0\ge\Delta\bar b-2|g|\sqrt{\bar b(480-15\bar b)}.
\]

Mit der rationalen Variationsobergrenze U=−1.129636 für E_0/Δ muss

\[
(\bar b-U)^2<\frac1{100}\bar b(480-15\bar b)
\]

gelten. Exakte Wurzelvergleiche liefern die leicht lesbare Einschließung

\[
\boxed{0.77<\bar b<1.45.}
\]

Sie verbessert die bisher verwendete Schranke
\(3/4<\bar b<135/92\). Sie ist weiterhin eine Schranke und kein
numerisch bestimmter Erwartungswert.

## 5. Relativistisches Feldwörterbuch: geprüfter Ausschluss und engerer Typ

Vor der physikalischen Deutung der Antwort wurde der tatsächliche Tensor
erneut im Grassmannraum geprüft. Für gleichhändige Weylfelder mit
**64 inneren** Labels gilt

\[
\varepsilon_{\alpha\beta}\psi_I^\alpha\psi_J^\beta
=\varepsilon_{\alpha\beta}\psi_J^\alpha\psi_I^\beta.
\]

Der antisymmetrische W-Tensor koppelt daher identisch zu null an einen
lokalen Lorentzskalar. Das wurde für alle 60 Tensorzeilen bestätigt.
Mit symmetrischen Spinorindizes sind dagegen alle drei Komponenten
für jede Tensorzeile nicht null. Es gilt

\[
\Lambda^2(S\otimes R)=
(\Lambda^2S\otimes\mathrm{Sym}^2R)
\oplus(\mathrm{Sym}^2S\otimes\Lambda^2R).
\]

W liegt im zweiten Anteil: der zugehörige Lorentztyp ist (1,0).
Die Invarianz von ε und der Abschluss der symmetrischen Spinortensoren
wurden an den drei komplexen sl(2)-Erzeugern geprüft. Die verwendeten
Zweikomponentenkonventionen und die Umwandlung unpunktierter in punktierte
Indizes beim Adjungieren sind in
[Dreiner, Haber und Martin, Abschnitt 2](https://arxiv.org/pdf/0812.1594)
dokumentiert. Die speziellen W-Null- und Nichtnulltests sind eigene Rechnungen.

### 5.1 Eine zusätzliche Schur-Grenze

\(R=16\otimes4\) ist irreduzibel unter der vollständigen inneren Gruppe
Spin(10)×SU(4). Deshalb ist ihr Kommutant auf diesen 64 Komponenten
nur \(\mathbb CI\). Auf **demselben** 64-dimensionalen Komponentenraum
kann daher keine unabhängige nichttriviale Lorentzspinorwirkung mit dieser
vollen inneren Wirkung kommutieren.

Die bloße Umnummerierung 64=2×32 schafft keine solche Wirkung. Bei
unveränderter innerer Darstellung benötigt die naheliegende kovariante
Erweiterung 2×64 Fermionfeldkomponenten und 3×60 Komponenten des
komplexen symmetrischen Vermittlers, jeweils mit den passenden
adjungierten Typen. Das sind **Feldkomponenten**, keine hier bewiesene
Anzahl propagierender Freiheitsgrade.

Ein algebraischer Kandidat wäre eine Kontraktion
\(C_A^{\alpha\beta}W_{A,IJ}\psi_{I\alpha}\psi_{J\beta}+\mathrm{h.c.}\),
mit symmetrischem C im dual passenden Spinortyp. In der Operatorladungskonvention
\([N,\psi]=-\psi\) muss C Ladung +2 besitzen; das Adjungierte trägt
Ladung −2 und punktierte Spinorindizes. **Das ist eine Typvorgabe**, keine
Identifikation des ursprünglichen einzelnen b_A mit einem vollständigen
relativistischen Feld. Kinetik, Positivität, Constraints, Lokalität und
ein Adapter zum Fockmodell fehlen.

Die folgenden Spektralsätze werden deshalb ausschließlich als Aussagen
über die originalen lokalen f-Operatoren bewiesen. Das ausgeschlossene
skalare Wörterbuch wird nicht erneut verwendet.

## 6. Die geladene Antwort auf genau diesem Grundzustand

Mit Im z>0 und \(H_n=H|_{N=n}\) lautet die retardierte Antwort

\[
G_{rs}(z)=
\langle\Omega|f_r(z+E_0-H_{65})^{-1}f_s^\dagger|\Omega\rangle
+\langle\Omega|f_s^\dagger(z-E_0+H_{63})^{-1}f_r|\Omega\rangle.
\]

Wegen innerer Symmetrie ist \(G_{rs}=\delta_{rs}G\).
Die Formel ist die exakte Definition mit den richtigen geladenen
Sektoren. Sie ist allein noch keine Auswertung der Resolventen.
Im v1.6.2-Markdown fehlt in Abschnitt 5.2 zwischen den zwei
Resolventenbeiträgen ein Pluszeichen; hier steht die additive CAR-konforme Form.

### 6.1 Gewichte und Momente ohne unbekannte Eigenvektorkomponenten

Seien dν_+(ε) und dν_−(ε) die positiven Additions- bzw. Entnahmemaße
für ε>0. Dann

\[
G(z)=\int\frac{d\nu_+(\epsilon)}{z-\epsilon}
+\int\frac{d\nu_-(\epsilon)}{z+\epsilon}.
\]

Ihre gesamten Gewichte sind exakt

\[
Z_+=\bar b/32,\qquad Z_-=1-\bar b/32.
\]

Für das signierte Spektralmaß dρ, mit Entnahmen bei ω=−ε, gelten

\[
\boxed{m_0=1,\qquad m_1=0,\qquad
m_2=g^2\left(15-\frac7{32}\bar b\right).}
\]

Die ersten **positiven Anregungsenergiemomente** sind in beiden Kanälen gleich:

\[
\boxed{\int\epsilon\,d\nu_+(\epsilon)
=\int\epsilon\,d\nu_-(\epsilon)
=a:=\frac{\Delta\bar b-E_0}{64}.}
\]

Die Mittelenergien der jeweiligen gesamten Kanäle sind folglich
\(\bar\epsilon_+=\Delta/2-E_0/(2\bar b)\) und
\(\bar\epsilon_-=(\Delta\bar b-E_0)/(64-2\bar b)\).
Ein Kanalmittel ist kein einzelner Pol.

| Größe pro ursprünglicher Mode | Bewiesenes offenes Intervall |
|---|---:|
| Additionsgewicht Z_+ | (0.0240625, 0.0453125) |
| Entnahmegewicht Z_- | (0.9546875, 0.9759375) |
| Zweites signiertes Moment m_2/Δ² | (0.03670703125, 0.03707890625) |
| Mittlere Additionsenergie /Δ | (0.889529655…, 1.252005844…) |
| Mittlere Entnahmeenergie /Δ | (0.030413640…, 0.042685581…) |

### 6.2 Beweis der neuen Momentidentitäten

Erweitere W antisymmetrisch zu M_{A,ij}. Dann

\[
[f_i,H]=g\sum_{A,j}M_{A,ij}f_j^\dagger b_A=:C_i,
\quad \{C_i,f_k^\dagger\}=0.
\]

Die zweite Gleichung beweist m_1=0 als Operatoridentität. CAR/CCR liefern

\[
\{C_i,C_k^\dagger\}=g^2\sum_{A,B,j,l}
M_{A,ij}\overline{M_{B,kl}}
\left(\delta_{AB}f_j^\dagger f_l+\delta_{jl}b_B^\dagger b_A\right).
\]

In einem invarianten Zustand sind die Einteilchendichten skalare Matrizen.
Die frisch geprüften Kontraktionen
\(\sum_{A,j}M_{A,ij}\overline{M_{A,kj}}=15\delta_{ik}\) und
\(\sum_{i,j}M_{A,ij}\overline{M_{B,ij}}=16\delta_{AB}\)
geben m_2. Die Identifikation mit dem zweiten Spektralmoment verwendet
Stationarität des Grundzustands.

Ferner ist \(\sum_if_i[H,f_i^\dagger]=-2gQ_+\).
Stationarität von N_b gibt \(\langle Q_+\rangle=\langle Q_-\rangle\),
und \(g\langle X\rangle=E_0-\Delta\bar b\). Daraus folgt a.
Die Operatoridentitäten wurden zusätzlich an einem unabhängig aufgebauten
Beispiel mit vier Fermion- und zwei überlappenden Bosonkanälen exakt geprüft.
Bei den CCR-Prüfungen wurden ausschließlich innere Besetzungen verwendet,
damit der endliche Bosoncutoff keine falsche Identität erzeugt.

## 7. Neuer Satz: Ein isolierter Entnahmepol mit großem Gewicht

### 7.1 Eine ganze 64er-Familie von Variationsräumen

Sei \(F=f_1^\dagger\cdots f_{64}^\dagger|0\rangle\) und
\(v_k=Q_+^kF\). Da f_r mit Q_+ kommutiert,

\[
u_{k,r}:=Q_+^kf_rF=f_rv_k.
\]

v_k ist invariant und hat Fermionenzahl 64−2k. Daher exakt

\[
\langle u_{k,r},u_{k,s}\rangle
=\delta_{rs}\frac{64-2k}{64}\|v_k\|^2.
\]

Für k=0,…,4 erhält man die neuen Normquadrate

\[
\boxed{1,\quad465,\quad412200,\quad521164800,\quad833259571200.}
\]

Die Hamiltonkompression auf diese 320-dimensionalen Versuchsräume ist
ein einziger 5×5-Jacobiblock, tensoriert mit I_64. Seine Diagonale lautet
0,Δ,2Δ,3Δ,4Δ, die quadrierten Nebendiagonalen
\(g^2\|u_{k+1,r}\|^2/\|u_{k,r}\|^2\).
Eine rationale LDL-Prüfung bei −1.095812Δ beweist 64 unabhängige
Variationsrichtungen unterhalb dieses Wertes. **Invarianz der
Versuchsräume unter H wird nicht behauptet und ist nicht erforderlich.**

Zusätzlich wurde die zweifache Konversion unabhängig und vollständig
in der Besetzungsbasis expandiert: alle 1830 ungeordneten Bosonpaare,
mit den ursprünglichen CAR-Vorzeichen und dem Faktor für identische
Bosonen. Sie reproduziert die Norm 439680 für v_2 und **für jeden der
64 entnommenen Modi** die Norm 412200. Die höheren angegebenen
Lochnormen folgen aus der ausgeschriebenen Symmetrieidentität und den
frisch wiederholten vollständigen Grundzustands-Normsummen.

### 7.2 Alle anderen N=63-Zustände werden kontrolliert

Der Nullbosonraum in N=63 hat Dimension 64 und trägt die irreduzible
konjugierte Darstellung der ursprünglichen Fermionen. Auf seinem
Komplement gilt N_b≥1. Die Casimirschranke für ungerade Fermionenzahl
liefert dort einen unteren Vergleich mit Diagonale bΔ, b=1,…,31,
und quadrierten Nebendiagonalen

\[
g^2(b+1)15(31-b).
\]

Alle rationalen LDL-Pivots nach Verschiebung um +3Δ/4 sind positiv.
Das gesamte Komplement liegt also oberhalb −3Δ/4. Nach Minimax
liegen **genau 64** Eigenzustände unter dieser Grenze.

Ihre Projektion auf den Nullbosonraum ist injektiv: Eine nichttriviale
Linearkombination im Komplement hätte zugleich eine Energieerwartung
unterhalb −1.095812Δ und oberhalb −3Δ/4. Das ist unmöglich.
Die Projektion ist zudem symmetrieverträglich und damit ein Isomorphismus
auf die irreduzible konjugierte 64. Schurs Lemma erzwingt, dass sämtliche
64 niedrigen Zustände **dieselbe Energie E_h** besitzen.

Aus der allgemeinen unteren N=63-Schranke und der neuen Variation folgt

\[
-1.121899\Delta<E_h<-1.095812\Delta.
\]

Im gesamten N=65-Sektor beweist ein weiterer rationaler Vergleich
\(H_{65}>-4\Delta/5\). Zusammen mit den E_0-Grenzen ergibt das

\[
0.007737<\frac{E_h-E_0}{\Delta}<0.062277,
\]

sowie die Restschwellen 0.379636Δ für höhere Entnahmen und
0.329636Δ für sämtliche Additionen.

### 7.3 Der Pol ist in der originalen f-Antwort sichtbar

Ein niedriges Eigenlevel allein würde seine Sichtbarkeit noch nicht beweisen.
Sei Z_low sein Gewicht in dν_− und c=0.379636Δ die Restschwelle.
Alle Entnahmeenergien sind größer als d=0.007737Δ. Dann

\[
a\ge dZ_{\mathrm{low}}+c(Z_--Z_{\mathrm{low}}).
\]

Mit den bewiesenen gemeinsamen Schranken für \(\bar b\) und E_0 folgt

\[
Z_{\mathrm{low}}>\frac{102938353}{119007680}
=0.864972353044778\ldots.
\]

Damit hat die Antwort tatsächlich die Form

\[
\boxed{G(z)=\frac{Z_{\mathrm{low}}}{z+\epsilon_{\mathrm{low}}}
+G_{\mathrm{rest}}(z),}
\]

mit positivem Restmaß, dessen Träger nur bei
\(\omega<-0.379636\Delta\) oder \(\omega>0.329636\Delta\) liegt.
Innerhalb dieses Fensters gibt es genau einen Pol der diagonalen f-Antwort.
Im vollen N=63-Hilbertraum ist sein Energieniveau 64-fach entartet.

**Noch nicht berechnet:** der exakte Wert von ε_low, das exakte Residuum,
alle Pole und Gewichte von G_rest sowie der vollständige Grundzustandsvektor.
Die neuen Aussagen sind strenge Intervalle und ein Existenz-/Isolationsbeweis.

## 8. Was mit dem kubischen 64er-Feld geschieht

Auf Ω mit N=64 liegen \(f_r\Omega\) im Sektor 63 und
\(\chi_r^\dagger\Omega\) im Sektor 67. Deshalb gilt für jede
ladungsneutrale Funktion des Hamiltonoperators

\[
\langle f_r\Omega,F(H)\chi_s^\dagger\Omega\rangle=0.
\]

Die frühere Identität auf zwei verschiedenen Referenzen,
\(f_r|R_4\rangle=-\chi_r^\dagger|0\rangle/\sqrt{32}\), bleibt richtig.
Sie liefert aber keine Operatorgleichung und keine Gleichsetzung beider
Anregungen auf Ω. Dies gilt einschließlich beliebiger neutraler Zwischenzeiten.

Die bekannte Kompositsummenregel liefert auf Ω jetzt das begrenzte Gewicht

\[
\langle\{\chi_r,\chi_s^\dagger\}\rangle
=\delta_{rs}\frac{23\bar b}{480},\qquad
0.036895833\ldots<\frac{23\bar b}{480}<0.069479167\ldots.
\]

Auch nach Zustandsnormierung wird daraus keine globale Operator-CAR.
Der neue isolierte Entnahmepol gehört ausdrücklich zu f, nicht zu einem
ungeprüft als frei angenommenen χ-Feld.

## 9. Eine konkrete operative Energiemessung und ihre Grenze

Für dieselbe stationäre N=64-Präparation unter \(H_\mu=H+\mu N\)
verschiebt sich das signierte Spektrum einheitlich um μ:
\(G_\mu(z)=G_0(z-\mu)\). Dann

\[
m_1=\mu,\qquad m_2=\mu^2+g^2(15-7Z_+),\qquad
g^2=\frac{m_2-m_1^2}{15-7Z_+}.
\]

Das zeigt, welche geladenen Spektraldaten die Parameter **relativ zu
einer festen Energie- und Zeitreferenz** bestimmen würden. Für eine
allgemeine μ-Wahl muss dieselbe Präparation nicht mehr globaler
Grundzustand sein; die Verschiebungsidentität setzt diese Eigenschaft
nicht voraus. Die Positivitäts- und Lückenaussagen der Abschnitte 6–7
beziehen sich auf μ=0.

Ein physisches Entnahmeinstrument könnte nur mit einer tatsächlich
verfügbaren Ladungssenke arbeiten, etwa einem Detektorfermion d:
\(H_{\rm int}=\kappa(d^\dagger f_r+f_r^\dagger d)\).
Es erhält die Gesamtladung von Bank plus Detektor, verletzt aber die
getrennte lokale Fermionparität beider Teile. **Diese Kopplung ist hier
eine zu prüfende Ressource, kein neu eingeführter nativer Hamiltonterm.**

Mit Detektorenergie ε_d ist nur die Differenz ε_d−μ messbar:

\[
\mu N_{\rm Bank}+\epsilon_dn_d
=\mu N_{\rm ges}+(\epsilon_d-\mu)n_d.
\]

Eine gemeinsame Verschiebung der Gesamtladungsenergie bleibt unsichtbar.
Ohne unabhängige Detektorkalibrierung wäre die Behauptung, der geladene
Test bestimme einen absoluten Wert μ=0, falsch. Ein innerhalb des
N=64-Sektors gewählter Energienullpunkt ersetzt diesen Test nicht.

## 10. Nächster konkreter Akzeptanzpunkt

Die bisherige Folge ist einen Schritt weiter:

**unveränderte Bank → abgesicherter modellinterner Grundzustand →
isolierter ursprünglicher Entnahmepol mit großem Gewicht.**

Für einen räumlichen Anschluss muss dieselbe Quelle nun folgende
zusammengehörige Daten bereitstellen:

1. Ein explizites Operationswort oder Instrument für Ladung-eins-Austausch
   zwischen operational bestimmten Teilen, einschließlich Detektor,
   Normierung und Ladungsbilanz. Die neutrale Algebra mit 84 Dimensionen
   liefert dieses Wort nicht.
2. Ein relativistisches Feld samt Adjungiertem und Kinetik, dessen
   Projektion tatsächlich das gerade untersuchte f und dessen native
   Zweipunktantwort reproduziert. Der skalare Weylkanal ist ausgeschlossen;
   die symmetrische Spinoralternative besteht bisher nur den Typtest.
3. Erst dann ein nichtverschwindendes ungerades Transfermatrixelement
   zwischen zwei Teilen auf demselben Hintergrund. Alleiniger
   Vermittlertransport lässt die bekannte lokale Paritätsschranke bestehen.
4. Für genau diesen Vertrag kann anschließend eine räumliche Skalierung
   mit Dispersion, Kegel, chiraler Struktur und Grenzwert beginnen.

Die sofort ausführbare mathematische Vertiefung ist enger: ε_low und
Z_low durch eine kontrollierte gemeinsame Reduktion der N=64- und
N=63-Räume bestimmen, inklusive Residuen- und Restfehlerzertifikat.
Eine große unkontrollierte Diagonalisierung oder ein willkürlich
hinzugefügtes Hopping wäre kein Ersatz.

## 11. Beweisstatus

| Aussage | Status |
|---|---|
| Vollständiger ursprünglicher nativer Grundzustandsprüflauf | Erneut bestanden im deklarierten Modell |
| Erweiterte N=3-Algebra mit dokumentiertem Clock-Lift | Exakt berechnet, Kontrollverfügbarkeit und Rahmen weiterhin bedingt |
| Scalar-Weyl-Nullkanal und symmetrischer Nichtnullkanal | Exakte Tensorprüfungen |
| Unabhängige Lorentzspinorwirkung auf denselben irreduziblen 64 Komponenten | Unter voller innerer Symmetrie ausgeschlossen |
| Gewichte und erste zwei Energiemomente auf Ω | Exakte Formeln und rationale Schranken |
| Isolierter sichtbarer f-Entnahmepol | Neu bewiesen mit Energie- und Gewichtsintervallen |
| Sämtliche Pole und Residuen der nativen Antwort | Offen |
| Nativer vollständiger Operationssatz / physische μ-Auswahl | Offen |
| Vollständige relativistische Feldrealisierung / räumliche Skalierung | Offen |
| T1–T8 insgesamt, Gravitation, RH, Faktorisierung, P versus NP | Kein neuer vollständiger Abschluss |

Die Beweise kombinieren analytische Argumente mit reproduzierbaren exakten
Rechnungen. Sie sind nicht vollständig in Lean formalisiert und wurden
nicht extern begutachtet oder experimentell bestätigt. „Neu“ bezeichnet
den Fortschritt gegenüber den bereitgestellten Dokumenten, keinen
geprüften Prioritätsanspruch gegenüber der gesamten Literatur.
