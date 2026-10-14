# Möbius × Viererclock: acht Kanäle aus einem (14. Oktober 2026)

Status: **PARTIAL**, keine Promotion. `python3 checker.py`: 26 exakte Prüfungen, < 1 s.

**Einfach gesagt.** Der Rand eines Möbiusbands läuft zweimal um die Naht. Die
Viererclock (Vierteldrehung) wird dort zu einer Achteldrehung, deren vierte Potenz
die Deckvertauschung ist. Faltet man einen einzigen chiralen Kanal entlang dieses
Rands auf ein Achtel, erhält man lokal **acht Kanäle (c = 8)** – ohne Kopien
einzusetzen: 2 (Doppeldeckung) × 4 (Marken).

**Was dabei herauskommt.**
- Bei periodischem Randkreis hat die geometrische Clock in E8 genau die Fixalgebra
  **A3 ⊕ D5** und die Gradverteilung 52/64/60/64 der TFPT-Gluegraduierung. Bei
  antiperiodischem Randkreis nie.
- Die gefalteten Nahtfermionen sind **nicht** die V16-Fermionen. Beide sind
  Fermionisierungen desselben E8 und hängen über Trialität zusammen. Schon der
  Träger D5 braucht in der gefalteten Beschreibung 24 Spinorströme.

**Offen.** Ein chiraler Kanal über den ganzen Möbiusrand (der QWZ-Kragen hat zwei
gegenläufige Ränder), die periodische Spinstruktur und die E8-Erweiterung selbst.
Die Faltung reduziert „acht eingesetzte Kopien" auf diese drei geometrischen
Bedingungen; sie leitet sie nicht her.

**Entscheidender Test.** Die vom Nutzer ausgearbeitete Cartan-Ladungsantwort,
angewandt auf die acht *gefalteten* Kanäle des tatsächlichen Nahtoperators mit
Möbiusverklebung: Trägt der Grad-1-Sektor (g²-Eigenwert i) Spinorladung bezüglich
der Faltungs-Cartan, liegt die TFPT-Klasse vor; antiperiodische oder nicht
chirale Verklebung schließt sie aus. Details: `PROOF.md`.
