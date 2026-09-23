# Vollständiger Vier-Record-Vertrag: unabhängige Prüfung und robuste Rohtrennung

14. September 2026. Root-Prüfer `exact_one_record_protocol.py` vollständig gelesen
und ohne Änderungen mit normalem Python sowie `-OO` erneut ausgeführt. Alle
**531 exakten Prüfungen** bestehen in beiden Läufen; die Ergebnisdateien sind
bytegleich. Die Replay-Ausgaben und der geprüfte Quellhash liegen ausschließlich
im Unterordner `robustness/`.

## 1. Die vollständige ideale Konstruktion trägt

Die 16-Gatter-Cliffordfolge bereitet ξ aus acht Nullen vor. Mit
P−03ξ=−√(3/8)Ω ist der Minus-Ausgang des ersten Records eine exakte
Präparation mit Rohgewicht 3/8; der abgebrochene Plus-Ausgang hat Gewicht 5/8.

Der tatsächliche Endtest besteht aus R03, Minus-Recordauswahl, Uξ† und acht
Rechenbasismessungen. Der akzeptierte Zeilenoperator ist

\[
\langle0^8|U_\xi^\dagger P^-_{03}
=\langle\xi|P^-_{03}=-\sqrt{3/8}\langle\Omega|.
\]

Der vollständige Endeffekt ist daher **(3/8)PΩ auf beliebigen Eingängen**.
Der Root-Prüfer berechnet den Zeilenoperator für alle 256 Basisvektoren aus den
tatsächlichen Gattern. Die Normierung folgt außerdem aus der unitären
Record-/Cliffordkonstruktion mit allen Messausgängen; sie ist nicht nur eine
Behauptung über bereits normalisierte Erfolgszustände.

Die beiden Echoaufrufe benutzen denselben Recordpointer oder zwei verschiedene
Pointer. Beim behaltenen Pointer wird vor dem zweiten Aufruf nicht gemessen oder
dephasiert; die Involution löscht den Record kohärent. Der frische Fall bleibt mit
beiden Pointern bis zur Endauswertung beschrieben. Der Prüfer addiert keine
unabhängig normalisierten Echozweige.

Pro **gestartetem Versuch** lautet die vollständige grob zusammengefasste
Flagverteilung:

| Gemeinsames Ereignis | Record behalten | Record frisch |
|---|---:|---:|
| Präparation abgebrochen; Ende nicht ausgeführt | 5/8 | 5/8 |
| Präparation gelungen; Endtest abgelehnt | 15/64 | 615/2048 |
| Präparation und Endtest gelungen | **9/64** | **153/2048** |
| Gesamt | 1 | 1 |

Die beiden echten Rohwahrscheinlichkeiten sind p_K=0.140625 und
p_F=0.07470703125. Ihr Verhältnis ist 17/32 und ihr Unterschied

\[
\boxed{D_0=p_K-p_F=135/2048=0.06591796875.}
\]

Der Endtest ist destruktiv. Seine Akzeptanz ist ein klassisches Testereignis;
sie wird nicht als verbleibende Ω-Fidelity der nach dem Endtest ausgelesenen
Materie interpretiert.

## 2. Ein gemeinsamer Fehlervertrag statt separater Normalisierungen

Für jeden Modus j∈{K,F} betrachten wir die **gesamte spurerhaltende Ausführung**:
Eingangspräparation, vier mögliche R-Aufrufe, Tick und inversen Tick,
End-Clifford, alle Hilfsregister sowie sämtliche Präp-/End-/Readoutflags.
Ein früher Abbruch wird als eigener orthogonaler Ausgang gespeichert. Die
Akzeptanzprojektion A selektiert gleichzeitig gelungenen Präp- und Endflag.

Seien V_j die idealen Stinespringisometrien und V'_j die kohärent gestörten
Realisierungen mit ||V'_j−V_j||≤η_j, auf demselben deklarierten Ein-/Ausgangsträger.
Für den festen gereinigten Eingang sind die akzeptierten Vektoren
v_j=A V_jψ und v'_j=A V'_jψ. Dann gelten ||v_j||²=p_j^0 und
||v'_j−v_j||≤η_j. Eine zusätzliche Abweichung der **vollständigen** Instrumente
in halber Diamantnorm sei höchstens q_j. Diese kann stochastische Readout-,
Reset-, Quell- und Controllerfehler enthalten.

Aus der Dreiecksungleichung und dem Effektwahrscheinlichkeitsbound folgt

\[
\boxed{|p_j-p_j^0|\le2\sqrt{p_j^0}\eta_j+\eta_j^2+q_j,}
\]

und etwas genauer die unsymmetrische gemeinsame Rohhülle

\[
\boxed{
\max(0,(\sqrt{p_j^0}-\eta_j)_+^2-q_j)
\le p_j\le
\min(1,(\sqrt{p_j^0}+\eta_j)^2+q_j).}
\]

Kein Bestandteil wird durch die gemessene Präperfolgsrate dividiert. Dieselbe
Argumentation kontrolliert jedes andere vollständige Flagereignis mit dessen
idealem Rohgewicht, etwa Präpabbruch oder Präperfolg plus Endablehnung. Durch
Messfehler fälschlich fortgesetzte Präpversuche sind bereits in diesem Instrument
und im q-Budget enthalten; ihre Eingänge werden nicht als exakte Ω eingesetzt.

Das bereits mit endlichen Q-Zeitfenstern realisierte R-Makro benötigt 70πℏ/Δ.
Für vier mögliche Aufrufe liefert Duhamel und die Teleskopsumme deshalb

\[
\eta_j\le 4\,70\pi\,\delta H/\Delta+\eta_{extra,j}.
\]

δH ist eine gleichmäßige Normgrenze für beliebige beschränkte, auch
nichtkommutierende, zeitabhängige Hamiltonfehler während der geplanten
Makrointervalle. η_extra enthält die nicht dadurch abgedeckten kohärenten Fehler
von ξ, Tick, Rücktick, Uξ†, Timing, Schaltflanken und Controller. Der Aufbau
hat somit höchstens vier Makrofehler pro gestartetem Versuch; die drei bei
Präpabbruch ausgelassenen Aufrufe werden im gemeinsamen Instrument kontrolliert
als Identitäten vervollständigt.

**Es werden keine kostenfreien Readouts oder Resets vorausgesetzt.** Für die reine
Erfolgsentscheidung braucht man den Präprecord, den Endrecord und acht abschließende
Materiebits. Wenn jedes dieser höchstens zehn Readouts einen auch bedingt auf die
Vorgeschichte gültigen vollständigen Instrumentfehler ≤f besitzt, genügt der
konservative Beitrag q_read≤10f. Die Echo-Pointer brauchen für diese
Erfolgsentscheidung nicht gemessen zu werden. Werden sie zusätzlich ausgelesen,
ist ihr Fehlerbudget entsprechend zu ergänzen. Ein bloßer klassischer Bitfehler
ohne Kontrolle einer zugleich fehlerhaften Messrückwirkung genügt nicht als
vollständiger Instrumentvertrag.

Jeder neue Versuch benötigt denselben kontrollierten Eingangs-/Hilfszustandsvertrag.
Fehler von Reset und erneuter ξ-Präparation gehören in q beziehungsweise η_extra.
Gedächtnis in wiederverwendeten Helpern oder Reservoirs darf nicht durch eine
unbelegte Unabhängigkeitsannahme entfernt werden. Für eine feste vollständige
kohärente Folge bleibt die Duhamel-Normabschätzung auf dem gemeinsamen Träger
gültig; eine über viele Versuche konstante Fehlerrate braucht einen entsprechenden
uniformen Reset-/Speichervertrag.

## 3. Ab wann die beiden Rohwahrscheinlichkeiten robust getrennt bleiben

Bereits die Summe der absoluten Fehlerbounds liefert

\[
p_K-p_F\ge D_0-B_K-B_F,
\quad B_j=2\sqrt{p_j^0}\eta_j+\eta_j^2+q_j.
\]

Mit denselben oberen Budgets η und q für beide Modi ist die unsymmetrische
Intervallhülle stärker. Solange η<√p_K^0 gilt

\[
\begin{aligned}
p_K-p_F
&\ge(\sqrt{p_K^0}-\eta)^2-q
 -(\sqrt{p_F^0}+\eta)^2-q\\
&=D_0-2(\sqrt{p_K^0}+\sqrt{p_F^0})\eta-2q.
\end{aligned}
\]

Die quadratischen Terme heben sich hier algebraisch auf; eine Korrelation oder
Fehlerauslöschung zwischen den beiden experimentellen Modi wird nicht angenommen.
Ein hinreichender strenger Trennvertrag ist deshalb

\[
\boxed{q<D_0/2,\qquad
\eta<\frac{D_0-2q}{2(\sqrt{p_K^0}+\sqrt{p_F^0})}.}
\]

Bei q=0 ist η<0.05083706496456328 ausreichend. Wenn ausschließlich der
Hamiltonfehler der vier Makros beiträgt, entspricht das

\[
\boxed{\delta H/\Delta<5.779264415281468\cdot10^{-5}.}
\]

Die absolute symmetrische Fehlerhülle wäre etwas konservativer mit
η<0.047375209474368324. Bei rein stochastischen Instrumentfehlern und η=0
genügt q<135/4096≈0.032958984375 **je vollständigem Modus**; das ist keine
zulässige Fehlerwahrscheinlichkeit für jedes einzelne Gatter.

Konkrete gemeinsame Budgets, jeweils η_extra=0 und q für alle übrigen Fehler:

| δH/Δ | q je Modus | sichere Untergrenze p_K | sichere Obergrenze p_F | garantierter Rohabstand |
|---:|---:|---:|---:|---:|
| 10⁻⁶ | 10⁻⁶ | 0.13996503931973117 | 0.07518966501243744 | **0.06477537430729373** |
| 10⁻⁵ | 10⁻⁴ | 0.13400503312596598 | 0.07969300880302842 | **0.054312024322937566** |
| 5·10⁻⁵ | 10⁻⁴ | 0.10947271959992069 | 0.10078447298523294 | **0.008688246614687756** |
| 6·10⁻⁵ | 10⁻⁴ | 0.10372652971093207 | 0.10644422752330678 | keine positive Trennung zertifiziert |

Die letzte Zeile ist ein Verlust dieser ausreichenden Garantie, kein berechnetes
Verschwinden des tatsächlichen Kontrasts. Ebenso braucht systematische
Trennbarkeit noch eine endliche statistische Auswertung der beobachteten Raten.
`one_record_end_review.json` enthält optional eine konservative Hoeffding-
Stichprobengröße für unabhängige gestartete Versuche bei 99 % Gesamtvertrauen;
die benötigte Unabhängigkeit wird nicht aus dem Resetnamen abgeleitet.

## 4. Wiederholungen und Zeiten gehören zu einem anderen Zählvertrag

Die Werte 9/64,153/2048 und die Vier-Aufruf-Fehlergrenze gelten für genau einen
gestarteten Versuch samt möglichem Präpabbruch. Der ideale nicht abgebrochene
Pfad benötigt vier R-Makros, also 280πℏ/Δ Hamiltonzeit.

Wiederholt man die Präparation bis zum ersten Erfolg und führt erst dann einmal
Echo und Endtest aus, beträgt die ideale mittlere Aufrufzahl 8/3+3=17/3.
Der entsprechende Mittelwert der Hamiltonzeit ist korrekt. Die Erfolgsraten
dieses anderen, bis zum Präperfolg wiederholten Ablaufs sind aber **3/8** und
**51/256**; sie sind bedingt auf die irgendwann erfolgreiche Präparation und
nicht 9/64 und 153/2048 pro initialem Versuch.

Für unbeschränkt viele Wiederholungen folgt aus η≤4·70πδH/Δ kein identischer
Fehlerbound an den gesamten bis dahin verwendeten Registern. Ein solcher Vertrag
braucht ein einheitliches Reset-/Neustartmodell und eine eigene Renewal- oder
Abbruchanalyse. Für die hier gewünschte unbedingte Rohprüfung werden deshalb
Präpabbrüche und Zähler aller gestarteten Versuche ausdrücklich aufbewahrt.

## Reproduktion und Ergebnis

`one_record_end_review.py` führt den Root-Prüfer mit Ausgabepfaden ausschließlich
im eigenen Unterordner aus, prüft Quellhash und Ergebnisgleichheit und rechnet die
Fehlerintervalle. `root_protocol_replay.json`, die optimierte Variante sowie
`one_record_end_review.json` sind die Belege. Die Root-Datei bleibt unverändert.
Die Prüfung bestätigt die komplette endliche Instrumentkonstruktion und liefert
eine gemeinsame quantitative Fehlertoleranz ihrer Rohsignatur; sie leitet weder
die Kontrollen aus P1/P2 her noch setzt sie eine unbezahlte Mess-/Resetumgebung ein.
