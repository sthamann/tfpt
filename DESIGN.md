---
name: TFPT research website
description: Light mathematical reading surfaces with explicit visual operations
colors:
  paper: "#fcfbf8"
  ink: "#20384f"
  action-blue: "#284d7a"
  carrier-blue: "#294ab6"
  family-sage: "#426c58"
  line: "#b3c1cf"
typography:
  headline:
    fontFamily: "Newsreader, Georgia, serif"
    lineHeight: 1.1
    letterSpacing: "-0.02em"
  body:
    fontFamily: "Inter, system-ui, sans-serif"
    lineHeight: 1.8
rounded:
  control: "6px"
spacing:
  control-gap: "0.6rem"
  diagram-gap: "1.5rem"
components:
  button-selected:
    backgroundColor: "{colors.action-blue}"
    textColor: "#ffffff"
    rounded: "{rounded.control}"
    padding: "0.7rem 1rem"
  button-outline:
    backgroundColor: "transparent"
    textColor: "{colors.action-blue}"
    rounded: "{rounded.control}"
    padding: "0.7rem 1rem"
---

# Design System: TFPT research website

## Overview

**Creative North Star: "Follow the mathematical operation"**

This records the implemented central reading surfaces inspected on 2 November 2026. It describes the incumbent visual system; it is not a claim that a separate visual comp was approved. The light paper ground, serif headings and restrained blue and sage diagrams make dense mathematics readable.

A diagram shows an actual state, coordinate, projection or dependence. Controls let the reader perform the named operation. Explanatory text and the result remain visible together.

**Key Characteristics:**
- Light reading surfaces.
- Explicit mathematical operations.
- Stable quantity identities across views.
- Local source and hypothesis links.

## Colors

Primary action blue identifies controls and links. Carrier blue and family sage distinguish the two lattice contributions in the shared structure bridge. Paper, ink and fine lines establish reading hierarchy. These roles record the implemented components; they are not universal scientific status colours.

**The Identity Rule.** A quantity retains its label and colour as it moves between the two sides of an explanatory diagram.

## Typography

Newsreader carries section hierarchy. Inter carries explanation, controls and numerical readings. KaTeX renders mathematics with semantic labels and copyable source. Tabular numerals align comparative values.

Reading measures are generally 65 to 76 characters. Long formulas scroll inside their own region. Diagram SVG styles must target authored diagrams explicitly, so they cannot alter KaTeX radicals or other mathematical SVGs.

## Layout

The central explanation uses a constrained reading shell. Parallel inputs or related operators can sit beside one another on desktop. At the observed 760px component breakpoint, operation and vector layouts stack in sequence. The chapter strip scrolls horizontally on narrow screens while the page itself stays within its viewport.

The surface strategy is recorded separately in .impeccable/surfaces/theory-guide.md.

## Elevation & Depth

Central teaching surfaces use spacing, thin dividers and pale selected states. Flat diagram regions retain the actual geometry. Shadows and decorative depth are not needed to communicate a calculation.

## Shapes

Controls use small corners with fine borders and a filled selected state. Root coordinates use rectangular cells grouped into their five and three dimensional blocks. Circles represent an actual seam, transport cycle or selected state when that geometry has mathematical meaning.

## Components

Buttons expose the selected state through both colour and aria-pressed. Each control names its operation. Keyboard focus remains visible. Selects choose a carrier slot; insertion, removal and reset operate on the currently shown state. Repeated insertion into an occupied slot visibly produces zero.

Chapter links open the promised interactive state, including repeated navigation to the same hash. Disclosure summaries reveal optional calculation or provenance detail. Home comparison links reveal their containing disclosure before scrolling to the selected measurement.

The shared structure bridge carries quantities into successive calculations. The matrix projection shows input, map and output. The Bell example shows coordinates, complex amplitudes, phase action and an exact operator check. Reduced motion preserves the same content and controls.

## Do's and Don'ts

### Do
- Do show the actual input and resulting state together.
- Do preserve labels, units, source conditions and numerical grouping.
- Do inspect 390px, 768px and desktop layouts using real content.
- Do keep source links close to their corresponding operation.

### Don'ts
- Don't substitute a repeated number for the map that relates two objects.
- Don't let diagram styling affect mathematical typesetting.
- Don't label an inventory or deterministic precision as experimental confirmation.
- Don't duplicate the historical presentation inside the current introductory route.
