# Unabhaengiges Scope- und Provenienz-Audit

21. September 2026  
Gegenstand: angehaengter Text `pasted-text.txt`, SHA256 `53960131dc9852042e464836b5e39a32e2aa276aa0b23cdb3c57cda19f6a8d69`

## Urteil

Der neue symmetrische E8-Stromproduktbefund ist als **algebraischer Quellenanschluss** belastbar und fuer die Flavorfrage relevant. Er schliesst eine echte Typisierungsluecke: `Sym^2(16,4)` enthaelt genau zwei Grad-2-Bildkanaele mit insgesamt symmetrischem Austauschtyp. Er konstruiert weder geladene Raumzeitfermionen noch einen Yukawa-Vertex, eine physische Familienclock oder eine Massentextur. Damit hilft er TFPT gezielt, vervollstaendigt TFPT aber nicht und schliesst kein T1-T8-Tor.

## 1. Darstellungsaussage: korrekt, mit einer Konventionspraezisierung

Die Zerlegung folgt strukturell aus

`Sym^2(V tensor W) = Sym^2(V) tensor Sym^2(W) + Lambda^2(V) tensor Lambda^2(W)`

und

- `16 tensor 16 = 10_s + 120_a + 126_s` fuer die gewaehlte Spin(10)-Chiralitaetskonvention,
- `4 tensor 4 = 10_s + 6_a` fuer SU(4).

Daher ist

`Sym^2(16,4) = (10,10) + (120,6) + (126,10)`.

Die Symmetrieindizes stimmen: `(10,10)` ist symmetrisch-mal-symmetrisch; `(120,6)` antisymmetrisch-mal-antisymmetrisch und damit im Gesamtpaar ebenfalls symmetrisch. Je nach Benennung der Spinorchiralitaet kann der komplexe letzte Faktor als `126` oder `bar(126)` erscheinen. Fuer einen invarianten Yukawa-Term wird ohnehin die duale skalare Darstellung benoetigt. Das Etikett allein ist deshalb noch keine Ladungs- oder Feldzuordnung.

Der Standard-SO(10)-Befund `16-16-10_s`, `16-16-120_a`, `16-16-bar(126)_s` ist in der Primaerliteratur explizit dokumentiert, etwa Nath/Syed, arXiv:hep-ph/0103165. Diese Literatur stuetzt die Austauschtypen, nicht die neue 820er E8-Produktrechnung.

## 2. Bell10: bedingt ein wirklicher Operatoranschluss, nicht nur eine Zahlengleichheit

Der vorhandene lokale Korpus enthaelt bereits zwei engere Operatoraussagen:

1. `compiler-current-descendant-20260919/PROOF.txt` konstruiert eine explizite SU(4)-aequivariante Isometrie `E: Bell10 = Sym^2(C^4) -> L(Lambda2)` in den einmal vorkommenden horizontalen SU(4)-Zehner bei A3-Gewicht `3/2`. Mit dem D5-Vektorgrundraum ergibt `I_D5 tensor E` einen 100-dimensionalen `(10_D5,10_A3)`-Unterraum des E8-Vakuummoduls bei Gesamtgrad zwei.
2. `compiler-current-product-20260919/grade2_origin_review.txt` konstruiert aus tatsaechlichen E8-Stromprodukten eine isometrische `bar(5) tensor 10_A3`-Teilstrecke und identifiziert den alten Bell-Readout-Projektor einschliesslich relativer Phasen. Dort wird ausdruecklich davor gewarnt, den unprojizierten 50-dimensionalen Produktzustand mit dem zehn-dimensionalen Bellbild gleichzusetzen.

Fuer die neue volle Karte `S` gilt unter denselben markierten E8_1-Konventionen: Ihr 100-dimensionales Bild ist ein `(10_D5,10_A3)`. In der festgelegten Glueklasse `D5-vector tensor A3-Lambda2`, mit D5 im Grundraum und A3 auf dem relevanten Nachfahrengrad, kommt dieser Typ einmal vor. Damit ist der Bildunterraum bedingt derselbe Unterraum wie `range(I_D5 tensor E)`, und die normierte Karte

`I_100 = S Pi_100 / sqrt(8)`

ist ein Intertwiner dorthin, bis auf die uebliche gemeinsame Phase eines irreduziblen Intertwiners.

Das ist staerker als die Koinzidenz `100=10*10`. Es ist weiterhin kein physischer Bell-Messoperator: Vorbereitung, Lokalitaet, Zustand, Ausleseinstrument und Zeit fehlen. Ausserdem enthaelt der angehaengte Text keine ausfuehrbare gemeinsame Basisdatei, mit der `I_100 I_100^dagger` direkt gegen den historischen Bell10-Projektor verglichen werden koennte. Der kleinste abschliessende Phasentest waere genau dieser Projektorvergleich in der gemeinsamen Chevalley-/Bellbasis.

## 3. Warum bosonische Stromprodukte keine geladenen Fermionen erzeugen

Die 64 Richtungen `(16,4)` sind Grad-1-Stroeme eines bosonischen holomorphen E8_1-VOA. `16` ist dabei ein **interner Spin(10)-Darstellungsname** und kein Beweis fuer halbzahligen Raumzeitspin. Die Grad-2-Produkte sind ebenfalls bosonische Quellenzustaende mit ganzzahligem konformen Gewicht.

Die Weyl-Identitaet

`epsilon_ab psi_I^a psi_J^b = epsilon_ab psi_J^a psi_I^b`

zeigt nur: Falls lokale gleichhaendige antikommutierende Raumzeitfelder `psi` bereits konstruiert sind, muss der Koeffizient in den vollstaendigen inneren Paarindizes symmetrisch sein. Die neue Karte liefert geeignete **innere Repraesentationsraeume** fuer einen solchen Koeffizienten. Sie liefert nicht:

- CAR/Spin-Statistik und lokale chirale Fermionfelder,
- eine Lorentz- und Raumzeitabbildung,
- ein skalares Feld in der dualen Darstellung,
- die tatsaechliche Dreipunktfunktion oder den 1PI-Vertex,
- Spiegelentkopplung, Zustand, Renormierung oder Kopplungsstaerke.

Besonders wichtig: Auch `(120,6)` ist im Gesamtpaar symmetrisch. Eine Auswahl nur des anschaulicheren `(10,10)` waere eine neue physische Auswahlregel. Unter `4=1+3` zerfaellt `Lambda^2 4` in `3 + bar(3)`; dieser Kanal ist nicht einfach der Raum symmetrischer drei-mal-drei Familienmatrizen.

## 4. Familienclock: exakte lineare Probe, aber keine volle Kovarianz ohne Spurionregel

Die Formel

`Y_+ = sigma^T A - A sigma`

ist tatsaechlich symmetrisch und die angegebene Determinante ist korrekt. Fuer generisches reelles `h` hat `Y_+` Rang drei. Das zeigt, dass ein **relativer** Transport der beiden Beine die alte Rang-zwei-Grenze eines einzelnen antisymmetrischen Tensors umgehen kann.

Diese Probe fuehrt `sigma` jedoch als zusaetzlichen nichtzentralen markierten Tensor ein. Unter einem allgemeinen Familienbasiswechsel ist die Konstruktion nur dann kovariant, wenn `sigma` als Spurion mittransformiert. Wird `sigma` festgehalten, bleibt nur sein Zentralisator als Symmetrie. Der Compiler muss daher noch herleiten, warum genau diese relative Wirkung, Orientierung und Phase physisch gewaehlt wird.

Die im Text erwaehnte CP-Probe ist nicht auditierbar: Die zwei komplexen Matrizen, Parameter und der volle schwachbasisinvariante Ausdruck fehlen. Ein einzelnes komplexes `Y_+` genuegt zudem nicht; physische CP-Verletzung verlangt einen nicht entfernbaren relativen Phaseninhalt mehrerer relevanter Matrizen. Die behauptete nichtverschwindende Kommutatorspur und erst recht eine gemessene CKM-/PMNS-Phase bleiben ungeprueft.

## 5. Quellen- und Reproduktionslage

In den geprueften Pfaden

- `/Users/stefanhamann/Documents/Codex/2026-09-21/`,
- `/Users/stefanhamann/Projekte/tfpt-theoryv4/`

wurde kein Originalpaket gefunden, das die charakteristischen Angaben des Anhangs gemeinsam enthaelt: 2080 Eingaenge, 1060 Ladungsbloecke, 4000 Eintraege, Spektrum `8^100 + 4^720 + 0^1260`, volle 52+8-Kovarianz, Grad-4-126-Test und die komplexe CP-Probe. Die `:chatgpt-content-reference{...}`-Marker im Anhang sind nicht aufloesbar und daher keine Quellenbelege.

Gefunden wurde das nahe, aber aeltere Paket

`experiments/theory-contracts/compiler-current-product-20260919/`

samt dem vorgelagerten Bell10-Paket `compiler-current-descendant-20260919/`. Beide Verzeichnisse sind im aktuellen Arbeitsbaum **untracked** (`git status` zeigt `??`); sie gehoeren somit nicht zum nachweisbaren Git-HEAD. Der Theoriegraph klassifiziert sie als `PARTIAL`, doch eine Graphaufnahme ungetrackter Arbeitsdateien ist kein Herkunftsnachweis. Das 2026-09-19-Paket prueft einen engeren 50-dimensionalen Stromproduktanschluss und den Bell-Projektor, nicht die neue volle 2080-zu-820-Karte.

Ein gestarteter Replay des aelteren Pakets reproduzierte die ersten beiden Zertifikate byteidentisch; der folgende lange Instrumenttest wurde nach mehr als 90 Sekunden abgebrochen. Ein vollstaendiger Replay dieses Pakets wird daher nicht behauptet. Am Repository wurde nichts veraendert.

## 6. Praeziser Nutzen fuer TFPT

Der Befund sollte als algebraischer Teilfortschritt uebernommen werden:

`markierte E8_1-Quelle -> kovariante Grad-2-Produktkarte -> zwei fest bestimmte positive innere Tensorraeume`.

Die erste noch offene kausale Kante lautet:

`bosonische Quellenoperatoren -> lokale geladene chirale Felder plus gemeinsamer skalarer 1PI-Vertex`.

Der kleinste entscheidende Herkunftstest ist deshalb keine weitere Gramrechnung. Er ist eine aus derselben Quelle hergeleitete lokale Dreipunktantwort `Gamma^(3)_(Phi psi psi)` mit festgelegten Feldern, Ladungen, Zustand und Zeit, deren innere Projektion auf `Pi_100` und `Pi_720` anschliessend gemessen wird. Bis dahin sind die Projektoren scharfe Pruefkriterien, aber keine physikalischen Kopplungen oder Massenskalen.

