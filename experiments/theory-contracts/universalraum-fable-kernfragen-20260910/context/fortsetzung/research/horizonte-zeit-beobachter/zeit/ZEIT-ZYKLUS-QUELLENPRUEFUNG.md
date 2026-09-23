# Relationale Zeit und der TFPT-Zyklus: ein exakter Übergang, offene Herkunft

Stand: 10. September 2026; gezielte Originalprüfung bei Repository-HEAD `66b91e40e245569f06ab440ead80f446c9be0ee5`.

**Zeit kann als Beziehung innerhalb eines gemeinsamen Zustands beschrieben werden. Daraus folgt bisher weder ein eindeutiger kosmischer Zeitfluss noch ein tatsächlich bewiesener TFPT-Zyklus.** Die wichtige nächste Frage ist konkret: Welche Teilalgebra fungiert als Uhr, welche Abbildung erzeugt die bedingten Zustände, und wie werden beide aus denselben TFPT-Daten ausgewählt?

**Was TFPT zum Zyklus tatsächlich enthält.** `origin_theory.tex:1026–1090` nennt die gesamte Lesart Kollaps → Horizont/Seam → Attraktor → neues Universum ausdrücklich eine physische Interpretation [C], nicht eine Ableitung. Der aktuelle Vertrag `CCC.SEAM.CROSSOVER.01` bestätigt diese Grenze. Sein mathematischer Unterbau enthält echte Struktur:

- Im markierten Möbius-System ist \(\tau(z)=-1/z\) eine Involution; \(z\tau(z)=-1\). Sie kehrt den Uhrgenerator um und vertauscht \(0,\infty\).
- Die Hopf-Abbildung verbindet die Seamsphäre mit einer dreidimensionalen Lens-Geometrie \(S^3/\mathbb Z_4\). Ein ausdrücklich gewähltes Lorentz-Metrikmodell \(g=\cos^{-2}T(-dT^2+g_{S^3})\) erfüllt \(\mathrm{Ric}=3g\).
- Ein endlicher dreizuständiger Kanal besitzt eine explizite Stinespring-Isometrie und eine exakt bekannte Kontraktionsrate.

Diese Aussagen identifizieren Symmetrie, Geometrie und Kanal. Sie liefern noch keine physische Entwicklung vom kollabierenden Universum durch die Seam in das folgende Universum. Auch die „eindeutige konforme Fortsetzung“ ist begrenzt: Die Ledgerzeile unterscheidet infinitesimale Steifigkeit und globale Eindeutigkeit innerhalb einer expliziten Obata-Familie; sie enthält keinen allgemeinen Satz über jede kosmologische Anfangsdatenmenge.

Die aktuellen offenen Anforderungen sind D1: wechselwirkende Algebra auf der Übergangsgeometrie mit passender Reflexionspositivität; D2: Übergangskanal als Isometrie auf Feldniveau; D3: Entscheidung zwischen Starobinsky-Inflation, Übergangs-/Gravitationswellenepoche oder berechnetem Hybrid. Der gespeicherte Planck-Suchlauf meldet `support:false`, \(p_{\rm global}=0{,}6733\). Dies ist ein negativer Befund für die untersuchte Scheibensignatur, kein beobachteter vorheriger Zyklus. Ich habe Ergebnisdatei und Vertragszeile gelesen; keine neue Analyse der Himmelskarte durchgeführt.

**Eine entscheidende Entropie- und Zeitpräzisierung.** Der tatsächlich eingesetzte Kanal lautet
\[
\Phi(\rho)=\sum_{i,j}T_{ij}|i\rangle\langle j|\rho|j\rangle\langle i|,
\qquad
T=P_*+\frac{64}{729}u_2u_2^*+\frac1{729}u_3u_3^*,
\]
mit \(P_*=\mathbf1\mathbf1^*/3\), \(u_2=(1,-1,0)/\sqrt2\), \(u_3=(1,1,-2)/\sqrt6\). Folglich
\[
\Phi^n(\rho)\longrightarrow I_3/3,
\qquad S(I_3/3)=\log3.
\]
Der Rang eins von \(P_*\) beschreibt den eindimensionalen verbleibenden **Populationsmodus**. Der zugehörige sichtbare Dichteoperator hat Rang drei und maximale Entropie. Dieser Mechanismus beweist daher keinen thermodynamischen Neustart mit niedriger sichtbarer Entropie. Die globale Isometrie kann Information in Umweltkorrelationen erhalten; dafür muss beim Übergang zur nächsten Ära aber erklärt werden, welche Freiheitsgrade übernommen werden.

Ebenso sind \(-\log T\) auf dem Populationsraum und der modulare Generator des Zustands \(I_3/3\) verschiedene Objekte. Auf \(M_3(\mathbb C)\) ist dessen Modularfluss trivial: \(\rho_*^{it}A\rho_*^{-it}=A\). Die exakte Formel \(T=e^{-H_{\rm mod}}\) erzeugt deshalb für sich keine nichttriviale physische Uhr des Attraktorzustands. Man kann eine andere Gibbs-Dichtematrix proportional zu \(T\) definieren; dann wurde ein anderer Zustand samt beobachtbarer Algebra eingeführt.

**Ein vollständig expliziter Übergang von einem Zustand zu einer Geschichte.** Die folgende endliche Konstruktion ist eine direkte Rechnung im Stil relationaler Uhrmodelle. Sie setzt keine kontinuierliche kanonische Uhr voraus. Page–Wootters beschreiben Entwicklung durch bedingte innere Uhranzeigen; die spätere Darstellung von Giovannetti–Lloyd–Maccone schreibt eine Geschichte als Korrelation zwischen Uhr und System. Dort wird der System-Hamiltonoperator bereits in den Constraint eingesetzt; die Beschreibung erzeugt ihn nicht aus einem beliebigen Zustand. [Page–Wootters, Originalartikel](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.27.2885), [Quantum Time, Gleichungen 1–15](https://arxiv.org/pdf/1504.04215).

Gegeben seien \(L\ge2\), eine orthonormale Uhrbasis \(|t\rangle\), ein unitärer Systemoperator \(U\) und \(\|\psi_0\|=1\). Definiere
\[
|\Psi\rangle=\frac1{\sqrt L}\sum_{t=0}^{L-1}|t\rangle\otimes U^t|\psi_0\rangle.
\]
Dann ist \(\Psi\) normiert, jede Uhranzeige hat Wahrscheinlichkeit \(1/L\), und der normalisierte bedingte Systemzustand lautet genau
\[
|\psi(t)\rangle=\sqrt L(\langle t|\otimes I)|\Psi\rangle=U^t|\psi_0\rangle.
\]
Das ist ein beweisbarer Zustands-/Dynamiktransfer. Jede Systemantwort \(\langle\psi(t)|A|\psi(t)\rangle\) lässt sich aus der passenden bedingten Antwort von \(\Psi\) wiedergewinnen.

Er erhält einen positiven stationären Constraint. Für \(|\Phi\rangle=\sum_t|t\rangle\phi_t\) setze
\[
\langle\Phi|H_{\rm prop}|\Phi\rangle
=\frac12\sum_{t=0}^{L-2}\|\phi_{t+1}-U\phi_t\|^2.
\]
Jeder Summand ist positiv. Daher ist \(H_{\rm prop}\Phi=0\) genau dann, wenn \(\phi_{t+1}=U\phi_t\). Sein Kern besteht aus allen Geschichten zu allen Anfangsvektoren. In endlicher Systemdimension \(d\) hat er Dimension \(d\). Ein stationärer Gesamtzustand kann somit bedingte Entwicklung enthalten; der Constraint allein wählt den Anfangszustand nicht aus.

Für eine **geschlossene Uhr** kommt der Term
\[
\frac12\|\phi_0-U\phi_{L-1}\|^2
\]
hinzu. Jetzt gilt zusätzlich \(U^L\phi_0=\phi_0\). Der zyklische Shift \(S_L\otimes U\) fixiert die Geschichte genau unter dieser Bedingung. Für sämtliche Anfangszustände braucht man \(U^L=I\). Eine vorgegebene Phasenverdrehung im Schließungsterm erlaubt entsprechend \(U^L\psi_0=e^{i\theta}\psi_0\); diese Verdrehung ist zusätzliche Randinformation. Eine offene Uhr benötigt keine Periodizität.

Beispiel: \(U=\mathrm{diag}(1,i)\), \(\psi_0=(1,1)/\sqrt2\), \(L=4\). Die vier Zustände sind \((1,i^t)/\sqrt2\); der Ring schließt exakt. Mit drei Anzeigen bleibt die offene Geschichte korrekt, aber derselbe Anfangszustand schließt nicht. Eine zyklische Symmetrie und ein dynamisch kompatibler Zustandszyklus sind deshalb getrennt zu prüfen.

Bereits eingegeben wurden: Uhr/System-Zerlegung, Uhrablesung, \(U\), Randbedingung und \(\psi_0\). Auch die Richtung wird nicht absolut festgelegt: Die Umbenennung \(t\mapsto L-1-t\) beschreibt dieselbe Geschichte mit \(U^*\) und Anfangszustand \(U^{L-1}\psi_0\). Ein thermodynamischer Pfeil braucht weitere Aussagen über Zustände, Umwelt und zugängliche Beobachtungen. Die reine bedingte Systementropie dieses Beispiels bleibt null.

**Thermische Zeit ist eine zusätzliche mögliche Anschlussstelle.** Für eine feste Algebra und einen geeigneten treuen Zustand liefert Modulartheorie einen bestimmten Automorphismenfluss. Connes–Rovelli schlagen die Identifikation dieses Flusses mit physischer Zeit als Hypothese vor. Für einen Gibbs-Zustand ergibt sich die bekannte Dynamik bis zur Temperatur-/Zeitskalierung; die Spezifikation der Observablen bleibt nötig. Der zustandsunabhängige Fluss *modulo inneren Automorphismen* ist ebenfalls keine eindeutige kosmische Uhr. [Connes–Rovelli, Einleitung und §4.1, insbesondere Gleichung 44](https://arxiv.org/pdf/gr-qc/9406019).

**Der nächste konkrete TFPT-Herkunftssatz.** Gesucht wird eine Konstruktion aus dem tatsächlichen gemeinsamen TFPT-Parent, die eine Uhr-Unteralgebra, einen Systemsektor, einen ausgewählten Zustand und einen Transfer \(U\) liefert, sodass ein isometrischer Einbettungsoperator \(J\) zugleich
\[
J\alpha^{\rm source}_n(A)J^*
=\alpha^{\rm clock}_n(JAJ^*)
\]
auf dem invarianten Bild erfüllt und alle relevanten Zustandsantworten erhält. Bei periodischer Lesart muss die Herkunft zusätzlich die Schließungsbedingung beweisen. Im offenen Fall muss die Uhrauflösung einschließlich physischer Kalibrierung wachsen können. Die Umkehrung zum reinen Symmetrieloop darf keine Dynamik oder Anfangsauswahl unterschieben. Der bestehende Vertrag `FTRANSFER.SK.RHO0.01` hält genau die globale Anfangszustandsauswahl weiterhin offen.

„Was war davor?“ wird damit präzise: Existiert eine abgeleitete Fortsetzung der Uhrkorrelationen und physikalischen Observablen über den Rand der gegenwärtigen Raumzeit? Eine algebraische Vorgängerrelation kann ohne äußere Uhr sinnvoll sein; ob sie ein physisches früheres Universum beschreibt, entscheidet erst der Herkunfts- und Fortsetzungssatz. Im bisherigen TFPT-Stand ist dieser Satz offen.

**Prüfumfang und Herkunft.** Codeentdeckung über den aktuellen MCP-Codegraph, dann Originalfunktion `v957_ccc_crossover_kinematics.run` und Modulpräambel gelesen; kein Modul/Suite-Neulauf. Gezielt gelesen: `origin_theory.tex:1026–1116`; `tfpt_research_contracts.tex:12470–12580,13822–13878`; drei volle Ledgerzeilen `CCC.SEAM.KINEMATICS.01`, `CCC.SEAM.CROSSOVER.01`, `FTRANSFER.SK.RHO0.01`; vollständige gespeicherte CCC-Ergebnisdatei. Externe Lektüre: Page–Wootters Originalabstract; Quantum Time §§II.A, Gleichungen 1–27 und Uhreninterpretation, keine vollständige Mehrzeit-Messungsprüfung; Connes–Rovelli Einleitung und §4.1. Keine allgemeine CCC-Literaturbewertung, kein unabhängiger Kosmologiedaten-Replikationslauf. Eigene Rechnung: `clock-checks.json` enthält **19 exakte Kontrollen**, darunter offene/geschlossene Uhr, Anfangsauswahl, Richtungsumkehr und tatsächlicher TFPT-Kanalfixpunkt. Die allgemeine positive-Constraint-Argumentation steht oben; die Beispielkontrollen ersetzen keine physische Herleitung.
