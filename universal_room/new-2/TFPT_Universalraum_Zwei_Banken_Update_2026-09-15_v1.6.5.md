# Kurzes Update v1.6.5 gegenüber v1.6.4

TFPT / Universalraum · 15. September 2026

## Neue eigene Ergebnisse

- Vollständige Energieschranke für den Einloch-Sektor zweier nativer Banken
  mit einem **zusätzlich deklarierten** Rotor-Link:
  \(\delta\ge .303549\Delta-\kappa/2\). Alle erlaubten Ladungsverteilungen
  und internen Zustände sind erfasst; keine künstliche Flussabschneidung.
- Gleichmäßige Auslaufnorm \(L\le2v/(\delta-2v)\), \(v=64|\tau|\), und
  Duhamel-Fehler \(\eta(t)\le|t|vL\) für die volle Entwicklung gegenüber
  der niedrigen Bandkompression.
- Bei \(g/\Delta=1/20\), \(\tau/\Delta=10^{-8}\),
  \(\kappa/\Delta=10^{-10}\), \(t\Delta=169500000\) und \(\hbar=1\):
  Zielwahrscheinlichkeit >99,2677105 % aus einem exakten niedrigen Lochzustand.
- Ohne anfänglichen Energiefilter, aus \(f_r\Omega/\sqrt\nu\):
  Wahrscheinlichkeit für die niedrige Lochlinie der anderen Bank
  >89,7260353 %. Diese Aussage verwendet die ursprüngliche Fermionantwort.
- Der Link ist außerhalb der bekannten lokal geraden Operationsalgebra.
  Dies gilt auch für adaptive Komposition gerader Krauszweige, aber nicht
  für beliebige bloß paritätskovariante Kanäle.

## Übernommene und geprüfte externe Ergebnisse

Die beiden gelieferten Prüfer wurden normal und optimiert byteidentisch zu
den Originalberichten reproduziert: 1.149 und 753 Prüfbedingungen.
Bestätigt wurden insbesondere die native interne Paarumwandlung, der
kontrollierte lokale Polrest und die Spektralzählungsgrenze gegen eine
direkte Identifikation der endlichen Bank mit dem vollen Logarithmusspektrum.
Das ältere Round37-Beispiel mit 99,8718 % ist ein anderes Vierfermion-Modell.

## Korrektur eines währenddessen geänderten Entwurfs

Unter der dort angegebenen Darstellungszerlegung ist der volle N=3-Raum
nicht multiplizitätsfrei: Drei helle Typen kommen doppelt vor. Die
Gruppenwirkung allein hat Kommutantendimension 16; zusammen mit den hellen
Paarmischungen und \(N_b\) verbleiben sieben zentrale Skalare. Sieben ist
keine Untergrenze für beliebige weitere, blockmischende Operationen.
Die eigentliche externe Darstellungszerlegung wurde in dieser Zusatzprüfung
nicht frisch reproduziert.

## Unveränderte offene Kernfragen

Ursprung und Verfügbarkeit des Links; Ursprung der Teilbereiche und der
Ladungsreferenz; ausführbare geladene Präparation; relativistischer
Feldadapter; gemeinsame skalierende 3+1D-Quelle; chirales SM-Maß; physische
Kopplungen und Massen; dynamischer Spin zwei. Alle T1–T8 bleiben offen.
Keine RH-, Faktorisierungs- oder P-versus-NP-Schließung.

## Zusätzlich integrierte letzte Anlagen

- Der innere Viererzyklus bleibt ein exakter W-Automorphismus nach Einsetzen
  der im gelieferten Stabilisatortest fehlenden Exteriorvorzeichen. Der
  explizite signierte Bosonlift erfüllt R⁴=I und R²≠I. Das ist ein positiver
  Anschluss, aber keine Gleichsetzung mit zentraler SU(4)-Phase oder Clock.
- Der gelieferte Kanal-Variationscode besitzt gegenüber P=f_jf_i einen
  relativen Vorzeichenfehler: Energie +0,0573648Δ statt −0,0196152Δ. Ein
  Phasenwechsel korrigiert die Variation; die bekannte native Schranke ist
  trotzdem viel stärker und Eindeutigkeit/Lücke bleiben bereits bewiesen.
- „Gravitativ 64“ wird nicht als reine 3+1D-Gravitationsanomalie übernommen.
  SU(4)³=16 gilt im deklarierten chiralen Feldvertrag; eine zusätzlich
  gleichgeladene U(1) kann eine gemischte U(1)-Gravitationsanomalie 64 liefern.
- Ein Dimension-vier-Energie-Impuls-Tensor und ein Zwei-Ableitungs-Kandidat
  für die Spinortensor-Kinetik widerlegen zwei zu pauschale Ausschlüsse.
  Positive Dynamik, Constraints, Quelle und ein Gravitonpol bleiben offen.
- Die 99,892-%-Rechnung ist ein numerischer Zeitfensterhöchstwert eines
  anderen Vierzustands-Paarmodells, kein neuer nativer Einloch-Satz.

## Nachweis und Lieferung

4.516 eigene Transferchecks, zehn Reichweitenchecks und 62 Nachtragschecks,
zusätzlich zu den 1.902 externen: insgesamt 6.490 Bedingungen, jeweils normal und optimiert
identisch. Das ist ein analytischer Beweis mit rationalen Zertifikaten,
keine neue formale Lean-Verifikation. Der ältere native Grundbeweis liegt
gepinnt bei, wurde aber nicht vollständig neu enumeriert.

Die Quellenprüfung erkannte eine parallele Änderung am alten Bericht und
stoppte zunächst. Die anschließende Verifikation gilt ausdrücklich für die
eingefrorene Version; die Abweichung zum Originalort bleibt protokolliert.
Ausführliche konsolidierte Markdown-Fassung, dieses kurze Update, einfache
Erklärung und Prüfpaket werden versioniert direkt in Documents bereitgestellt.
Keine Aktualisierung der großen Haupt-PDFs oder Webseite, kein Commit/Push.
