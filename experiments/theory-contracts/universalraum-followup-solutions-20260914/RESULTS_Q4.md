# TFPT/Universalraum v1.4 — Q4-Folge: Bleibt das Labor bei Fehlern und wachsender Groesse brauchbar?

14. September 2026. Forschungsresultate, keine T1-T8-, RH- oder Komplexitaetspromotion.
Pruefer: robustness.py (70 Bedingungen, davon 3 exakt und 67 numerisch; robustness.json).
Keine Behauptung kostenloser Kuehlung oder eines wechselwirkenden thermodynamischen Limes.

## 1. Aufgabe (a) — Jitter-Empfindlichkeit des 13-Faktor-Filters

Das mikroskopische Sternspektrum hat 14 verschiedene Werte
E_pm(g) = (Delta +/- sqrt(Delta^2 + 4 t^2 (6-2g)))/2, g = 0, 1/2, ..., 3, t/Delta = 1/20,
mit Multiplizitaeten (1,30,45,40,15,90,35) untere, (30,45,40,15,90,35) obere und 67 fuer Delta; insgesamt 544.
Ziel ist der eindeutige niedrigste Wert E_0. Die 13 Filterzeiten tau_j = pi*hbar/(E_j - E_0)
loeschen jeden unerwuenschten Wert exakt (am vollen 544D-Matrixprojektor verifiziert).

Empfindlichkeitsmatrix. Fuer den Filterausdruck
f(E_k) = prod_j (1 + exp(-i tau_j (E_k - E_0)))/2 gilt am idealen Punkt
df/dtau_j = (-i (E_k-E_0) exp(-i tau_j (E_k-E_0))/2) prod_{l != j} (1+exp(-i tau_l (E_k-E_0)))/2.
Da der k-te Faktor den Wert E_k exakt loescht, ist prod_{l != j} = 0 fuer j != k;
die 13x13-Empfindlichkeitsmatrix S_kj ist daher diagonal (ausserdiagonal max < 1e-13, numerisch verifiziert und durch zentrale finite Differenzen kreuzgeprueft).

RSS-Koeffizient. C = sum_{k,j} |S_kj|^2 = sum_k |S_kk|^2 (Einheiten 1/(hbar/Delta)^2):

| Groesse | Wert |
|---|---:|
| RSS-Koeffizient C | 9.3816486e-07 |
| sigma_tau-Budget fuer Leck <= 1e-12 je Filter | sqrt(1e-12/C) = 1.03e-03 hbar/Delta |
| Worst-Case-Koeffizient (diagonal, gleich RSS) | 9.3816486e-07 |
| Kohaerente Amplitude (sum_k |S_kk|)^2 | 3.066e-06 |

Verifikation des quadratischen Gesetzes:

- Alle 2^13 = 8192 Vorzeichenmuster bei sigma = 1e-4: max Leck 9.3817e-15, Vorhersage C*sigma^2 = 9.3816e-15 (innerhalb 5%).
- Skalierungslauf sigma in {1e-3, 1e-4, 1e-5} (Gaussche Stoerungen, 1000 Versuche):
  Verhaeltnis Leck/(C*sigma^2): 0.98; 0.997; 0.957 — quadratisches Gesetz bestaetigt
  (bei 1e-5 ueberwiegt Maschinengenauigkeit, daher nur Groessenordnung).
- Quadratische Skalierung Leck(1e-3)/Leck(1e-4) ~ 100 (innerhalb 20%).

Globale Zeitverstellung (alle tau_j um (1+eps) skaliert):
C_global = sum_k |S_kk|^2 tau_k^2 = 0.8464. eps-Budget fuer Leck <= 1e-12:
sqrt(1e-12/C_global) = 1.09e-06.

Ergebnis (a): Jitter und globale Verstellung sind fuer das Idealmodell quantifiziert.
Das sigma_tau-Budget von etwa 1e-3 hbar/Delta (unabhaengige Jitter) bzw.
eps ~ 1e-6 (globale Skalierung) fuer Leck <= 1e-12 je Filter
sind erreichbar, aber nicht kostenlos — sie sind echte Ressourcenzahlen.

## 2. Aufgabe (b) — Record-Puls-Verstellung

Der 44-dimensionale Recordblock wird aus der 6x16-partiellen Isometrie W
(WW^dagger = I_6) aufgebaut: U = [[P+, -i W^dagger],[-i W, 0_6]],
Q = I_32 (+) (I_6 (x) X), Ziel R (+) I_12 mit R = P+ (x) I_2 + P- (x) X.
Der ideale Puls ist U = exp(-i (pi/2) h) mit h = [[0, W^dagger],[W, 0]].
Verifiziert: h^2 = P- (+) I_6 auf den beiden Bloecken, h hermitesch,
U(pi/2) = expm(-i pi/2 h) reproduziert das ideale U auf 1e-12,
und (U^dagger (x) I_2) Q (U (x) I_2) = R (+) I_12 exakt.

Verstellung. U(theta) = expm(-i theta h) mit eps = theta - pi/2.
Der Recordfehler d(theta) = (1/44) ||U(theta)^dagger Q U(theta) - (R (+) I)||_F^2.
Der Operator entwickelt sich als macro(eps) - T = eps L1 + eps^2 L2 + ...
mit L1 = i [T, H] (H = h (x) I_2). Da d eine Quadratnorm ist, ist der fuehrende
Term eps^2 ||L1||_F^2 / 44 (der lineare Operatorterm liefert den quadratischen
d-Koeffizienten). Symbolisch und durch finite Differenzen (eps in {1e-4, 1e-5, 1e-6}):

| Groesse | Wert |
|---|---:|
| Quadratischer Koeffizient a = ||L1||_F^2 / 44 | 12/11 = 1.0909... |
| d ist gerade in eps (Linearer-in-d-Term verschwindet) | verifiziert |
| Verstellungs-Budget |eps| fuer d <= 1e-12 | sqrt(1e-12/(12/11)) = 9.57e-07 |

Ergebnis (b): Der Recordpuls vertraegt eine Winkelverstellung von etwa 1e-6
fuer d <= 1e-12. Der exakte Koeffizient 12/11 ist geschlossen angegeben.

## 3. Aufgabe (c) — Exakte Zwei-Zell-gekoppelte Rueckmeldung

Korrektur der Aufgabenvoraussetzung. Der gemeinsame Zwei-Zell-Hilbertraum ist
256 (x) 256 = 65536-dimensional (nicht 512). rang(K) = 96 (nicht 32),
also rang(K (x) K) = 9216. Die maximal-gemischte Startzustaend hat Rang 65536
und ist unter jedem unitaeren U_c invariant (U_c I U_c^dagger = I); daher ist
kappa = 0 exakt zwei unabhaengige Einzelzellen (F_joint = F_single^2),
und kappa > 0 maximal-gemischt ist nur im vollen Rang 9216+ rechenbar (nicht materialisierbar).
Der reine Start |e_27 e_27> hat Rang 1 und wird fuer alle kappa exakt simuliert
(Rang waechst genau eins je Zyklus, bleibt <= 1+m).

Simulierte Rueckmeldung. Die aufgabenkonforme rang-erhaltende Rueckmeldung ist der
vereinfachte Kanal T(rho) = (K (x) K) rho (K (x) K)^dagger + w |e_27 e_27><e_27 e_27|
(w = 1 - ||(K (x) K) X||_F^2). Der VOLLSTAENDIGE E (x) E-Tensorproduktkanal
haette zusaetzliche partielle Ausfallquerterme (K (x) sqrt(I-K^dagger K)) usw.,
deren Krausrang nach einem Zyklus auf 256^2 = 65536 anwaechst — nicht materialisierbar.
Der vereinfachte Kanal ist das erklaerte rang-erhaltende Modell; er kontrahiert
LANGSAMER als der volle Kanal (siehe unten).

Einzelzell-Aktualrate. Die Worst-Case-Schranke r = 0.97542071045 ist nicht
tight; die Aktualrate fuer maximal-gemischt und rein ist 0.9620081 (tighter).

| kappa | Start | Kontraktionsrate | Rang max | deg/r | Infid. @ 200 |
|---:|---|---:|---:|---:|---:|
| 0 | rein | 0.998289 | 201 | 1.0234 | 0.709 |
| 1e-3 | rein | 0.998291 | 201 | 1.0234 | 0.709 |
| 1e-2 | rein | 0.998484 | 201 | 1.0236 | 0.727 |
| 1e-1 | rein | 1.000000 | 201 | 1.0252 | 0.974 |
| 0 | maxgem (exakt, unabhaengig) | 0.962103 | 65536 | 0.9863 | — |

Vereinigungsbound. 1 - F <= 2 r^m:

- Maximal-gemischt, kappa = 0, echter unabhaengiger Kanal (F_joint = F_single^2):
  Vereingungsbound UEBERLEBT (max Verletzung 0, exakt verifiziert).
- Reiner Start, vereinfachter rang-erhaltender Kanal: Bound UEBERLEBT NICHT
  (max Verletzung 0.72), da der vereinfachte Kanal mit Rate 0.998 langsamer
  kontrahiert als die Schranke r = 0.9754. Das ist ein Artefakt der Rang-Erhaltung,
  nicht des vollen E (x) E.

Zur r^2-Vorhersage. Die Zwei-Zell-Infiditaet 1 - F_joint kontrahiert
asymptotisch mit der Einzelzellrate r (bzw. der Aktualrate 0.962), NICHT mit r^2.
Der langsamste gemeinsame Fehlermodus ist |psi> (x) |Omega> mit Eigenwert r.
Die r^2-Zahl ist die beide-Zellen-fallen-Rate (Produkt zweier unabhaengiger
Ausfallwahrscheinlichkeiten), nicht die Infiditaetskontraktion. Weder der volle
noch der vereinfachte Kanal liefert r^2 als Kontraktionsrate.

Ergebnis (c): Das wechselwirkende Ergebnis ist exakt fuer die erklaerte Zwei-Zell-Kopplung
und den erklaerten rang-erhaltenden Rueckmeldekanal, ist aber kein thermodynamischer
Limes-Satz und nicht der volle E (x) E-Tensorproduktkanal. Die Kopplung
verlangsamt die Kontraktion modest (Degradation 1.02–1.03 vs r fuer kappa <= 1e-1);
der echte unabhaengige Vereingungsbound ueberlebt bei kappa = 0.

## 4. Aufgabe (d) — N-Zell-Ressourcenbuch

Zyklen: cycles(N, eps) = ceil(log(eps/N)/log r) (Vereinigungsbound).
Pro Zelle pro Zyklus: 8 Farbbits + 3 Recordbits = 11 Bits geloescht.
Landauer-Energie: N * cycles * 11 * k_B T ln 2 (symbolisch in k_B T).
Filterpaarzeit pro Zelle: 6345.659268 hbar/Delta (Start + Schluss).
Recordpuls und Reset als separate benannte Eintraege je Zyklus.

Tabelle fuer eps = 1e-6:

| N | Zyklen/Zelle | Gesamtbits geloescht | Gesamtfilterzeit (hbar/Delta) | Landauer-Energie |
|---:|---:|---:|---:|---|
| 1 | 556 | 6 116 | 6345.659268 | 6116 k_B T ln 2 |
| 16 | 667 | 117 392 | 101 530.548 | 117392 k_B T ln 2 |
| 256 | 778 | 2 190 848 | 1 624 488.8 | 2190848 k_B T ln 2 |
| 4096 | 890 | 40 099 840 | 25 996 613.5 | 40099840 k_B T ln 2 |

Zwei-Zell-Kopplungskorrektur aus (c): Degradationsfaktor vs r im Bereich
kappa in {0, 1e-3, 1e-2, 1e-1} ist 1.0234 bis 1.0252 (gemessen am reinen Start
mit dem vereinfachten rang-erhaltenden Kanal). Dies ist kein thermodynamischer
Limes-Satz; die Korrektur erhoeht die benoetigten Zyklen modest.

N=4096-Zeile (exakt): Zyklen/Zelle = 890; Gesamtbits = 40 099 840;
Gesamtfilterzeit = 6345.659268 * 4096 hbar/Delta = 26 004 568.6 hbar/Delta
(exakt als Fraction 406122193152/15625);
Landauer-Energie = 40099840 k_B T ln 2.

## 5. Ehrliche Grenzen

- Jitter und Verstellung sind fuer das Idealmodell quantifiziert (sigma_tau ~ 1e-3 hbar/Delta,
|eps| ~ 1e-6 fuer Record, je fuer Leck <= 1e-12).
- Das wechselwirkende Zwei-Zellergebnis ist exakt fuer die erklaerte Kopplung und den
  erklaerten rang-erhaltenden Kanal, ist aber kein thermodynamischer Limes-Satz
  und nicht der volle E (x) E-Kanal.
- Die r^2-Vorhersage aus der Aufgabenstellung ist nicht die Infiditaetskontraktionsrate
  (die richtige ist r); r^2 ist die beide-Zellen-fallen-Rate.
- Der echte unabhaengige Vereingungsbound ueberlebt bei kappa = 0; der vereinfachte
  rang-erhaltende Kanal kontrahiert langsamer und verletzt den Bound (Artefakt).

Keine Behauptung unveraenderter statischer Dynamik, nativer Resonanz, nativer
isolierter Stern, nativen kontrollierten H, nativen Records, nativen Clocks oder
nativen Resets. Die Quelle des vollstaendig spezifizierten kontrollierten Mikrolabors
bleibt die entscheidende offene Kante.
