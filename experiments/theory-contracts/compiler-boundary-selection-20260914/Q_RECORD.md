# Eine Markierung kann als Randrecord entstehen

14. September 2026. Exakte bedingte Konstruktion auf den ursprünglichen
Gaussian-Strahlen, unabhängig gegengeprüft. Kein neuer physischer Träger,
kein Born-Beweis und keine TOE-Promotion.

## Die ursprünglichen Markierungen sind in frühen Mittelwerten unsichtbar

Die sechs q-Markierungen wählen jeweils fünf tatsächliche Kontexte und damit
20 ursprüngliche Quellstrahlen. Diese fünf Kontexte sind gegenseitig unverzerrte
Basen. Für ihre korrelierten Kopienmomente

\[
M_k(q)=\frac1{20}\sum_{r\in q}P_r^{\otimes k}
\]

gilt exakt für jedes q:

\[
M_1=I_4/4,\qquad M_2=(I_{16}+\mathrm{Swap})/20.
\]

Auch die unaufgezeichnete uniforme Kontextmessung ist jeweils derselbe Kanal
D1/5. Die dritte Korrelation unterscheidet die Markierungen dagegen. Für einen
ursprünglichen Teststrahl psi ist

\[
\operatorname{Tr}(P_\psi^{\otimes3}M_3(q))=
\begin{cases}1/16,&\text{wenn sein Kontext in q liegt},\\
7/160,&\text{sonst}.\end{cases}
\]

Ein einzelner solcher Test trennt zwei von vier Markierungen, nicht alle sechs
auf einmal. Für jedes Paar unterschiedlicher Markierungen gibt es jedoch einen
solchen Quellstrahl-Zeugen. Dabei muss dieselbe verborgene Strahlwahl über die
drei Kopien korreliert sein. Bei unabhängigem Neuziehen werden alle Momente zum
Produkt von I4/4; die Information verschwindet dann für jede Kopienzahl.
Mit zugänglichen Kontextetiketten kann die Markierung schon im ersten Record
sichtbar sein. Der Drei-Kopien-Satz betrifft unetikettierte Quantenzustände.

Dies ist nicht die frühere geordnete Bargmann-Dreieramplitude: symmetrische
Kopienkorrelation und zeitlich geordnetes Wort sind verschiedene Objekte.

## Eine einfache positive Folge: ein kovariantes Markierungsinstrument

Schreibe M_q=M3(q) und Pi_sym für den Projektor auf Sym³(C4), Dimension20.
Aus den direkt geprüften Quellüberlappungen folgt

\[
\operatorname{Tr}(M_q^2)=1/16,\qquad
\operatorname{Tr}(M_qM_{q'})=19/400\quad(q\ne q').
\]

Für Mbar=sum_q M_q/6 ist daher Tr(Mbar²)=1/20. Alle M_q sind auf demselben
symmetrischen Raum getragen und haben Spur1. Folglich

\[
\|Mbar-\Pi_{\mathrm{sym}}/20\|_{\mathrm{HS}}^2=0,
\qquad \sum_qM_q=\frac3{10}\Pi_{\mathrm{sym}}.
\]

Das bestimmt die positiven Effekte

\[
E_q=\frac{10}{3}M_q,\qquad
E_\perp=I_{64}-\Pi_{\mathrm{sym}},\qquad
\sum_qE_q+E_\perp=I_{64}.
\]

Ein explizites Instrument braucht nicht einmal die vollständige Matrixwurzel
von M_q. Verwende die Krausoperatoren

\[
K_{q,r}=P_r^{\otimes3}/\sqrt6\quad(r\in q),\qquad
K_\perp=I_{64}-\Pi_{\mathrm{sym}}.
\]

Jeder Quellstrahl gehört genau zwei Markierungen; zusammen mit der obigen
Summenidentität beweist das die Vollständigkeit. Die ursprüngliche Gruppe
permutiert q und r gemeinsam. Das Instrument ist deshalb kovariant, ohne
vorab ein bestimmtes q in seine Bewegungsregel einzusetzen.

Starte nun mit drei unabhängigen zyklischen Randzuständen, also I64/64.
Für jedes q gilt genau

\[
\boxed{p(q)=5/96,\quad \rho_{\mathrm{nach}\ q}=M_q,\quad
p(\perp)=11/16.}
\]

Insgesamt treten q-Records mit Wahrscheinlichkeit5/16 auf. Bedingt auf
diesen Erfolg sind die sechs gleich wahrscheinlich. **Die Korrelationen
entstehen hier im Instrument; sie sind nicht schon in den Eingang hineingelegt.**

Alternativ liefert die Lüders-Realisierung sqrt(E_q) aus demselben
maximalgemischten Eingang dieselben bedingten Zustände. Sie ist aber auf
allgemeinen Eingängen NICHT dasselbe Instrument wie die obige Krausliste.
Diese Nicht-Eindeutigkeit wird nicht versteckt.

Die Konstruktion löst eine begrenzte Existenzfrage: Eine volle symmetrische
Regel kann eine unterschiedliche Markierung als stochastischen Randrecord
hervorbringen. Sie löst nicht den ursprünglichen Ankerselektor für qstar und
beweist keine native Tensorfaktorisierung oder Verfügbarkeit dieses Instruments.

## Präparation, Record und Compilerwort in einer Ausführung

Der neue Anschluss wird auch mit dem früheren Reflexionswort-Zeugen verbunden.
Alle Schritte beginnen gemeinsam bei (I4/4)^tensor3; ein reiner Eingang wird
nicht zusätzlich festgesetzt. Bewahre im obigen Instrument den Record(q,r)
auf und betrachte r=psi=(1,1,0,0)/sqrt2. Zwei q-Markierungen erlauben diesen
ursprünglichen Strahl. Für jedes der beiden Paare gilt ungefiltert p(q,r)=1/384;
der zugehörige bedingte Zustand ist P_psi^tensor3.

Auf der ersten Kopie folgen entweder W=R0 R+ R+i oder W'=R0 R+i R+ aus den
drei ursprünglichen Reflexionen. Der rechte Faktor wirkt jeweils zuerst.
Am Ende wird der ursprüngliche Strahl phi=(1,i,0,0)/sqrt2 getestet.

| Gewicht derselben vollständigen Geschichte | W | W' |
|---|---:|---:|
| Vorgegebener zulässiger Record(q,psi) und Endereignis | 1/384 | 0 |
| Beide zulässigen q summiert, psi und Endereignis erhalten | 1/192 | 0 |
| Bedingt auf den aufgezeichneten Präparationserfolg | 1 | 0 |

Alle Zahlen sind aus derselben Anfangsdichte und denselben Krausoperatoren
berechnet. Ohne Herold-/Randrecords bleibt die Anfangsdichte unter dem
nichtselektiven Instrument und den Wörtern invariant; der Endtest liefert
dann in beiden Fällen1/4. Die Information sitzt in den gemeinsamen Records,
nicht in einer nachträglich passend eingesetzten reinen Anfangsbedingung.

Für jede festgelegte Fortsetzung wird die gesamte endliche Statistik gemeinsam
durch p(o1,...,on)=Tr(K_on...K_o1 rho0 K_o1†...K_on†) bestimmt; ein gemeinsames
Record-Erzeugungsfunktional ist die entsprechende charakteristische Funktion
Z(chi)=sum_history exp(i sum_t chi_t(o_t)) p(history). Diese endliche
Formel ist kein bereits konstruierter Kontinuums-SK-Funktional für T8.

## Kein perfekter Decoder und kein erfundener fehlender Viererraum

Das verwandte Pretty-good-Messverfahren E_q identifiziert einen als M_q
vorbereiteten Zustand nur mit Wahrscheinlichkeit5/24; jedes falsche Label
hat Wahrscheinlichkeit19/120. Die Zustände sind nicht orthogonal.

Aus Tr(M_q²)=1/16 folgt NICHT, M_q sei ein normierter Rang16-Projektor.
Diese attraktive Hypothese wurde unabhängig für alle sechs Markierungen
widerlegt: Im 20×20-Gram G der symmetrischen Strahlwürfel gilt
G²≠(5/4)G; eine explizite Residuumskomponente ist3/16.
Ein vierdimensionaler fehlender Korrelationsraum ist also nicht nachgewiesen.
Die gültige Summen-/POVM-Konstruktion oben benutzt diese falsche Hypothese nicht.

## Physische Grenze

Gegenstand sind Quellenalgebra, Tensorprodukte und ein wohldefiniertes
Quanteninstrument unter der normalen endlichdimensionalen Quantenmechanik.
Die Verfügbarkeit genau dieser gemeinsam adressierten Kopien, Projektionen
und Records ist zusätzliche operative Struktur. Zahlen wie5/96 sind
Protokollwahrscheinlichkeiten, keine neuen Naturkonstanten.
Symmetrie allein wählt dieses Instrument nicht eindeutig aus.

Der ursprüngliche P1-Zustands-/Zeitvertrag und der gemeinsame 3+1D-Elternprozess
sind weiterhin nicht konstruiert. Alle T1–T8 bleiben offen.

Belege: marking/boundary_moments.py und dessen exakte Quellelemente;
q_record_completion.py prüft die rationalen Summen- und Normierungsschritte
aus dem archivierten Moment-Gram. Der Drei-Design-Hintergrund ist bekannte
Mathematik, nicht eine neue allgemeine TFPT-Entdeckung:
[Zhu, 2017](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.96.062336).
