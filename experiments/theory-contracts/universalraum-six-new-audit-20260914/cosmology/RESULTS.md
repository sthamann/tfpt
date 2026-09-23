# Festes TFPT-Massenmatching mit vollständigem Hintergrund und Modentransfer

14. September 2026. Eigenständige numerische Fortsetzung von v1.5.
Experiments only. Keine Likelihood, kein Intervallzertifikat, keine T-Promotion.

## Ergebnis

**Die numerische Integration des exakten FLRW-Skalarhintergrunds und der
linearen skalaren und tensorartigen Moden schließt die Abweichung zum
eingefrorenen ACT-Ziel nicht.** Bei unveränderter Masse trifft die skalare
Amplitude den Zielwert bei N*=54.24134 E-Faltungen vor dem Inflationsende;
dort folgt ns≈0.9644213 statt 0.9752. Wählt man den Pivot für ns≈0.9752,
ist die Amplitude etwa **2.04921-mal** zu groß.

Die Observablen werden hier aus integrierten Moden nach ihrem Einfrieren
bestimmt, nicht aus Potential-Slow-Roll-Formeln. Die frühere Einschränkung
auf Potential-Slow-Roll ist damit für diese konkrete numerische Diagnose
beseitigt. Ein universeller analytischer Ausschlusssatz für alle Pivots
oder alle möglichen TFPT-Erweiterungen folgt daraus nicht.

| Größe | Amplitude passender Pivot | Tilt passender Pivot |
|---|---:|---:|
| N* bis εH=1 | 54.2413415055 | 78.5313001630 |
| As | 2.13702549604×10⁻⁹ | 4.37921720792×10⁻⁹ |
| ns | 0.964421293064 | 0.975200003598 |
| r=PT/PR | 0.00364471896815 | 0.00179288490068 |
| As / Ziel | 1 bis zur numerischen Nullstellensuche | 2.04921149333 |

Die langen Dezimalwerte dienen der Reproduzierbarkeit. Die angemessenen
Ergebniszahlen sind ns≈0.9644213, r≈0.00364472 und das Amplitudenverhältnis
≈2.04921; eine Zertifizierung sämtlicher ausgegebener Stellen wird nicht
behauptet. Der Tiltpivot wurde zunächst mit BD-Start 300 bestimmt und
anschließend mit BD-Start 3000 ausgewertet; sein verbleibender Tiltrest ist
3.60×10⁻⁹.

## Fixierter Vertrag und Primärquellen

In reduzierten Planckeinheiten Mp=ℏ=1 wird ausschließlich

\[
V(\phi)=\frac34M^2(1-e^{-\sqrt{2/3}\phi})^2,
\quad c_3=\frac1{8\pi},\quad M^2=c_3^7
\]

gerechnet. Zahlen: M²=1.5787776955488534×10⁻¹⁰ und
M=1.2564942083228452×10⁻⁵. **Die Masse wird in keinem Schritt nachgefittet.**
Variiert wird nur N*, der Zeitpunkt des Horizontaustritts des Referenzmodus.

Das festgehaltene Ziel ist As=exp(3.062)×10⁻¹⁰ und ns=0.9752, aus
[ACT DR6 v2, Tabelle 5, Spalte P-ACT-LB2](https://arxiv.org/pdf/2503.14452v2).
Die Modengleichungen und die Bunch-Davies-Anfangsform sind gegen
[Ellis et al., Appendix C](https://arxiv.org/html/2510.18656v1#A3) geprüft.
Der dortige Satz über Auswertung beim Horizontaustritt wird **nicht** als
Ersatz für das spätere Einfrieren verwendet. Die gegenwärtige Rechnung
misst dessen Unterschied ausdrücklich.

Modellannahmen: räumlich flaches expandierendes FLRW, ein kanonisches
Skalarfeld in Einstein-Gravitation, der oben fixierte Potentialzweig,
Inflationsattraktor und das subhorizontale Vakuum. Diese Voraussetzungen
sowie das physische Massenmatching werden hier nicht aus der mikroskopischen
TFPT-Quelle abgeleitet. Eine Reheating-Geschichte, die N* eindeutig an
0.05 Mpc⁻¹ bindet, wird ebenfalls nicht eingesetzt.

## Hintergrund: die vollständigen Gleichungen

Sei n=ln(a) vorwärts laufend und p=dφ/dn. Dann sind die verwendeten
Hintergrundgleichungen exakt innerhalb des genannten klassischen Modells:

\[
\phi'=p,\qquad
p'=-(3-\epsilon_H)(p+V_\phi/V),\qquad
\epsilon_H=p^2/2,\qquad H^2=V/(3-\epsilon_H).
\]

Die Integration beginnt bei φ=6.5 mit p=−Vφ/V als Anfangswahl. Danach
werden die vollständigen Gleichungen bis zum Ereignis εH=1 gelöst.
Der Endpunkt liegt bei φend=0.614643994273; die ganze Hintergrundstrecke
umfasst 148.131825551 E-Faltungen. Der früheste im präzisen Amplitudenlauf
verwendete Modenstart liegt **85.88248 E-Faltungen nach** diesem
Hintergrundstart. Die Anfangsnäherung wird daher nicht als exakte
Attraktorlösung am Pivot ausgegeben.

Zur Kontrolle wurde mit φinitial=6.7 und halbierter anfänglicher
Geschwindigkeit sowie engeren Hintergrundtoleranzen neu gestartet. Bei
demselben N* verändert dies As nur um 5.92×10⁻¹³ relativ und ns um
4.00×10⁻¹¹. Der bewertete Abschnitt ist gegenüber dieser deutlich
geänderten Hintergrundinitialisierung stabil.

Am Amplitudenpivot liegen φ*=5.30501163714,
εH*=0.000233875616552 und H*=6.20011395165×10⁻⁶.

## Tatsächlicher skalarer und tensorartiger Modentransfer

Die Feldfluktuation Qk erfüllt in n-Koordinaten

\[
Q_k''+(3-\epsilon_H)Q_k'
+\left[(k/(aH))^2+m_\mathrm{eff}^2/H^2\right]Q_k=0,
\]

mit

\[
\frac{m_\mathrm{eff}^2}{H^2}
=\frac{V_{\phi\phi}}{H^2}-\frac{p^4}{2}
+\frac{2pV_\phi}{H^2}+3p^2.
\]

Als unabhängige Formulierung wird zusätzlich Rk=Qk/p direkt integriert:

\[
R_k''+(3-\epsilon_H+2p'/p)R_k'+(k/(aH))^2R_k=0.
\]

Die Identität zwischen beiden Massen-/Reibungsformen wird symbolisch
geprüft. Die beiden unabhängig integrierten Gleichungen stimmen in As
am präzisen Pivot auf **1.34×10⁻¹³ relativ** überein.

Für jeden Modus wird sein eigener Start bei k/(aH)=ρBD bestimmt.
Die endlichen Bunch-Davies-Anfangsdaten sind

\[
Q_k(n_0)=\frac1{a_0\sqrt{2k}},\qquad
Q_k'(n_0)=(-1-i\rho_\mathrm{BD})Q_k(n_0).
\]

Eine für die Leistung irrelevante Gesamtphase wurde auf eins gesetzt.
ρBD=300,1000,3000 werden getrennt geprüft. Ein endlicher Start ist eine
Approximation des asymptotischen Vakuums, kein Beweis des Grenzwerts.

Jede tensorartige Polarisation h besitzt dieselbe Gleichung ohne den
effektiven Massenterm. Die kanonische Normierung ist h=2QT; beide
Polarisationen werden mitgezählt. Deshalb werden

\[
P_R(k)=\frac{k^3}{2\pi^2}|Q_k/p|^2,
\qquad
P_T(k)=\frac{4k^3}{\pi^2}|Q_{T,k}|^2
\]

ausgewertet. ns wird durch zentrierte Differenzen von ln(PR) bei
ln(k/k*)=±0.02 bestimmt, zusätzlich mit ±0.01 kontrolliert. Der Hintergrund
und die Pivotskala bleiben dabei für die benachbarten Moden gleich.

Die abschließende Leistung wird zwölf E-Faltungen nach dem Pivot gemessen.
Zwischen zehn und zwölf E-Faltungen ändert sich PR um −1.95×10⁻⁹ relativ
und PT um −2.03×10⁻⁹. Der skalare kanonische Wronskian ist beim
Horizontdurchgang auf 4.25×10⁻¹¹ relativ erhalten.

**Negative Kontrolle:** Direkt am Horizont wäre PR um den Faktor
1.990728273 zu groß. Die Gleichung korrekt zu integrieren und die Leistung
zu früh auszulesen wäre hier ein nahezu zweifacher Normierungsfehler.

## Getrennte numerische Konvergenz

Alle folgenden ersten fünf Läufe benutzen denselben vorläufigen
Amplitudenpivot N*=54.2416640009. Die letzte Amplitudenpassung wurde erst
danach mit den genaueren Einstellungen wiederholt.

| Änderung gegenüber BD300, rtol=2×10⁻¹⁰ | relative Änderung As | Änderung ns |
|---|---:|---:|
| Nur früherer Start BD1000 | +1.07141×10⁻⁵ | −5.49×10⁻⁹ |
| Nur rtol=2×10⁻¹², atol=2×10⁻¹⁴ | −6.62×10⁻¹⁰ | −4.22×10⁻¹¹ |
| BD1000 und engere Toleranzen | +1.07149×10⁻⁵ | −5.43×10⁻⁹ |
| BD3000 und engere Toleranzen | +1.14713×10⁻⁵ | +1.49×10⁻⁹ |

Von BD1000 zu BD3000 bei enger Toleranz beträgt die verbleibende Änderung
von As ungefähr **7.56×10⁻⁷ relativ**, von ns ungefähr 6.92×10⁻⁹.
Dies sind beobachtete Konvergenzunterschiede, keine rigorosen
Fehlerobergrenzen. Die frühe Vakuuminitialisierung dominiert die
hier getestete Integratortoleranz deutlich.

Nach erneutem Amplitudenmatching mit BD3000 verschiebt sich N* um
−0.0003224954 und ns gegenüber dem vorläufigen Amplitudenmatch um
−2.04×10⁻⁷. Die Halbierung des ln(k)-Differenzenschritts am endgültigen
Pivot verändert ns um 1.18×10⁻⁹. Das Ergebnis bleibt weit von einer
Verschiebung um die benötigten 0.01078 entfernt.

## Unabhängiger analytischer Normierungsfall

`sanity_check.py` benutzt denselben Modenintegrator auf einem anderen,
exakt lösbaren Hintergrund mit konstantem εH=0.01. Dessen Hankel-Lösung
hat

\[
\nu=\frac{3-\epsilon_H}{2(1-\epsilon_H)},\quad
n_s=1-\frac{2\epsilon_H}{1-\epsilon_H},\quad r=16\epsilon_H,
\]

\[
A_s=\frac{H_*^2}{8\pi^2\epsilon_H}
\frac{2^{2\nu-1}\Gamma(\nu)^2}{\pi}
(1-\epsilon_H)^{2\nu-1}.
\]

Bei H*=10⁻⁵ und BD3000 beträgt die relative Amplitudenabweichung
−9.99×10⁻⁸, die Tiltabweichung 1.24×10⁻¹⁰ und die Abweichung von
r=0.16 nur −8.33×10⁻¹⁷. Das kontrolliert unabhängig die
Feld-/Krümmungsnormierung, den Wellenzahlderivativ und den Faktor für beide
Tensorpolarisationen. Weglassen einer Polarisation und voreilige
Horizontauslesung werden als falsche Varianten erkannt.

## Bedeutung für v1.5 und Grenzen

Die v1.5-Potential-Slow-Roll-Rechnung fand beim Amplitudenmatching
ns≈0.9642233954. Die tatsächlich integrierten linearen Moden erhöhen
diesen Wert um ungefähr 0.00019790 auf 0.9644212931. Die Verbesserung ist
real innerhalb der festgelegten Näherungskette, sie reicht für das Ziel
0.9752 nicht aus. Beim umgekehrten Tiltmatching sinkt der frühere
Amplitudenfaktor etwa 2.0653 auf 2.04921; der gemeinsame Zentralwertabgleich
bleibt damit deutlich verfehlt.

Die Hintergrundgleichungen wurden vollständig integriert; die
Perturbationen sind aber weiterhin **linear** und die Quantenkorrelationen
auf diesem Hintergrund auf Baumebene beschrieben. Höhere
Perturbationsordnungen, Schleifen, veränderte Potentiale und eine
physikalisch abgeleitete Reheating-Geschichte sind nicht eingeschlossen.
Die beobachteten Daten werden nicht mit einem Boltzmann-/Likelihoodlauf
neu analysiert. Insbesondere wird aus den zwei Zentralwertvergleichen
keine gemeinsame Signifikanz oder Ausschlusswahrscheinlichkeit berechnet.

## Dateien und Reproduktion

- `mode_transfer.py`: Hintergrund, Moden, Pivotsuche, getrennte Konvergenz;
- `verification.json`: alle Modenwerte, Einstellungen, Quellhash und 26 Guards;
- `sanity_check.py` und `sanity_check.json`: symbolische Massenidentität,
  analytische Hankel-Normierung und negative Kontrollen.

Aus dem Ordner ausführen:

```sh
/opt/homebrew/bin/python3 -B mode_transfer.py
/opt/homebrew/bin/python3 -B sanity_check.py
```

Die volle Rechnung wurde tatsächlich ausgeführt. Eine zweite gesamte
Python-`-OO`-Reproduktion wird nicht behauptet; die physikalisch relevanten
Wiederholungen sind die oben ausgewiesenen unabhängigen Start-, Toleranz-,
Gleichungs- und Hankelkontrollen. Alle Ausgabedateien liegen ausschließlich
in diesem eigenen Experimentordner.
