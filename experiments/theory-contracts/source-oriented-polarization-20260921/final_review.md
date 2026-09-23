# Finale Fachreview: UR.SOURCE.ORIENTED_POLARIZATION.01

## Urteil

**Fachlich freigabefähig nach einer kleinen epistemischen Formulierungskorrektur.** Die tragenden Rechnungen stimmen; ich finde keinen Fehler, der den PARTIAL-Befund, die skalare CR-Rekonstruktion, den v210-Ausschluss oder die lokalisierte Spinlift-Lücke umstößt.

## Eine konkrete Korrektur

PROOF.md, derzeit Zeile 126, sagt:

> Die Normalflächen-Kompaktifizierung zu S² folgt ab Zeile 1640.

Die zitierte Originalstelle tfpt_1_architecture_e8.tex:1639–1660 ist selbst mit \(\mC\) markiert und nennt dies ein „Hardening (P1)“. Daher sollte „folgt“ nicht wie ein geschlossener geometrischer Satz klingen. Belastbare Formulierung:

> Die Normalflächen-Kompaktifizierung zu S² wird in tfpt_1_architecture_e8.tex:1639–1660 als \(\mC\)-Hardening von P1 eingesetzt. Bedingt auf diese Geometrie besitzt S² eine eindeutige Spinstruktur, deren von einer Scheibe induzierte Randstruktur bounding ist.

Die nachfolgende Grenze bleibt richtig: Selbst unter dieser bedingten Geometrie fehlt die Abbildung des geladenen P1-Feldgenerators auf das induzierte Spinbündel.

## Geprüfte tragende Punkte

- **Skalarer CR-Kern:** \(\ker(\Lambda+i\partial_s)\) und die Scheibenrechnung \((|n|-n)e_n\) sind korrekt. Der Vorzeichenwechsel bei Orientierungsumkehr ist ausreichend offengelegt.
- **Weyl-Transformation:** \(\Lambda\) und die Einheitstangentialableitung skalieren beide mit \(e^{-\sigma_b}\). Der Text trennt korrekt den invarianten glatten Kern vom dichteabhängigen orthogonalen \(L^2\)-Projektor.
- **Voller positiver v210-Operator:** Aus \(f\ge4e^{-8}>0\) folgt als Formungleichung
  \[
  |D|-D+M_f\ge(\min f)I>0.
  \]
  Deshalb ist der CR-Kern leer und \((|D|+M_f)1=f\ne0\). Dieser Ausschluss ist analytisch und hängt nicht vom Fourier-Cutoff ab. Die ursprünglichen Clock-Kommutatorresultate werden dadurch nicht bestritten.
- **Self-duale CAR:** Der periodische Nullmodendefekt, die Ergänzung durch \(C_0\), Rang 8 bei Reinheit und die Unmöglichkeit einer zugleich reinen und voll \(Spin(16)\)-invarianten Nullmodenkovarianz sind korrekt. Der Text unterscheidet die interne \(Spin(16)\)-Wirkung ausdrücklich von räumlichem Spinlift und Lorentzspin.
- **Geometrischer Spinlift:** v492/v506/v510 werden korrekt als Konsequenzrechnungen innerhalb eines gewählten beziehungsweise geometrisch gedeuteten Lifts gelesen. Die bloße unsigned Deck-Permutation erzwingt das NS-Vorzeichen nicht auf einem noch nicht identifizierten geladenen Feldraum.
- **Ursprünglicher Transfer:** Gleichung (10) ist ausdrücklich bedingt auf denselben freien positiven Rotations-/Zylindergenerator. Der Contract behauptet keine P1-Zeitantwort und setzt die TFPT-Energien 3,4,5 nicht ein.
- **Korrelationskonvention:** Für \(z=\tau-i\theta\), \(\tau>0\), gilt
  \[
  \sum_{r\in\mathbb N_0+1/2}e^{-rz}=\frac1{2\sinh(z/2)}.
  \]
  Mit dem deklarierten Maß \(d\theta/(2\pi)\) fehlt kein zusätzlicher \(2\pi\)-Faktor. Das ist der positive-Zeit-Zweig; die volle fermionische zeitgeordnete Distribution würde durch die antisymmetrische Fortsetzung auf \(\tau<0\) ergänzt. Weil der Text ausdrücklich \(\tau>0\) sagt, liegt kein Fehler vor. Optional kann dieser letzte Satz zur Vermeidung einer Überlesung ergänzt werden.

## Reichweite der Freigabe

Freigegeben werden können:

1. die konstruktive skalare Richtungsrekonstruktion;
2. der exakte Nachweis, dass der wörtliche positive additive v210-Operator kein masseloser skalarer Laplace-DtN auf diesem Raum ist;
3. die bedingte NS-CAR-Konstruktion nach geliefertem Feld-/Spin-/Transferintertwiner;
4. die Identifikation von \(\iota_{\rm spin}\) als erster fehlender Ursprungskante.

Nicht freigegeben und im Contract auch nicht behauptet sind die physische P1-Spinorfeldidentifikation, eine ursprüngliche Ladungsverbindung, der tatsächliche Transfer, die E8-Felderweiterung oder eine vollständige TFPT-Lösung.
