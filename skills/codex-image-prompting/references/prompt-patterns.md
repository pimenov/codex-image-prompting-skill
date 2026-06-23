# Prompt patterns for Codex Desktop imagegen

Use these patterns as prompt skeletons. Replace bracketed fields with concrete details. Keep user-provided display text exact.

## Table of contents

- Universal prompt skeleton
- Posters, covers, social cards
- Seamless social carousels
- UI mockups
- Research, technical, and system diagrams
- Data visualization concepts
- Infographics and field guides
- Product and food renders
- Photorealistic scenes
- Multi-panel boards and storyboards
- Image editing with references
- Quick repair checklist

## Universal prompt skeleton

```text
[Format/aspect/canvas]. Create [artifact type] for [audience/use].

Layout:
- [Region 1]: [role, visual weight, exact text if any]
- [Region 2]: [role, visual weight, exact text if any]
- [Region 3]: [role, visual weight, exact text if any]

Subject:
[Concrete subject, setting, objects, people, product, or system].

Text:
Accurately render the exact visible text: "[text 1]" / "[text 2]" / "[text 3]".

Style:
[Specific visual direction, medium, palette, material, lighting, camera or diagram grammar].

Quality constraints:
Crisp typography, clear hierarchy, readable labels, coherent spacing, no garbled text, no fake logos, no random extra text.
```

## Posters, covers, social cards

Use when making article covers, webinar cards, ads, posters, thumbnails, or event visuals.

```text
Design a [aspect ratio] [poster/article cover/social card] for [topic/event/product].

Promotional hierarchy:
1. Main title largest: "[exact title]"
2. Supporting line: "[exact subtitle]"
3. Metadata/CTA: "[date/author/action if needed]"

Composition:
[Hero object/person/scene] occupies [top/center/left] with [background/environment].
Leave clean negative space for the title. Make the title readable at thumbnail size.

Style:
[Editorial / conference poster / premium tech / calm expert / magazine cover] with [palette], [lighting], [texture].

Avoid:
Unreadable microtext, garbled letters, fake sponsor logos, stock-photo blandness, cluttered hierarchy.
```

## Seamless social carousels

Use for Instagram, Threads, LinkedIn, or similar carousels where one wide visual continues across slides.

### Concept mode

Use this mode to explore visual direction quickly.

```text
Create one ultra-wide [N]:1 panoramic concept artwork for a seamless social media carousel, designed to suggest [N] square slides.

Theme:
"[central idea]"

Slide plan:
1. [Hook scene] - blank message zone for "[short title]"
2. [Problem/contrast scene] - blank message zone for "[short title]"
3. [Method/process scene] - blank message zone for "[short title]"
4. [Proof/application scene] - blank message zone for "[short title]"
5. [Conclusion/CTA scene] - blank message zone for "[short title]"

Continuity:
A single visual element travels across all slides: [glowing line / road / ribbon / knowledge graph / timeline / river / cable].

Output constraints:
Continuous world, no hard panel borders, no random text, no dense microtext. This is concept art, not final production geometry.
```

### Production mode

Use this mode when the carousel must be publishable.

```text
Production brief for a seamless carousel:
- Slides: [N]
- Export size per slide: [1080x1080 or other]
- Required master canvas: [N*export_width] x [export_height]
- Typography: overlay after image generation
- Safe zones: keep essential text and subjects away from slice boundaries
- Continuity element: [line/road/ribbon/graph] drawn or composited across the full master canvas
- AI role: generate background/style assets or scene components, not final pixel geometry unless the generated master meets the required size
```

Before slicing, check pixel geometry. For `N` square slides exported at `1080x1080`, the master should be at least `N*1080` pixels wide and `1080` pixels tall. If it is smaller, either regenerate/extend at higher resolution or use it only as a style reference.

### Overlap experiment mode

Use this mode only when testing sequential generation of adjacent sections.

```text
Generate slide [K] of [N] with [overlap width] px overlap.
Preserve the incoming edge from the previous section: [describe edge/reference].
Continue the same palette, lighting, perspective, background geometry, and continuity element.
Keep important text out of the overlap area.
Output may need manual compositing and cleanup; do not assume pixel-perfect seams.
```

## UI mockups

Use when making app screens, dashboard previews, SaaS concepts, admin panels, or mobile UI.

```text
Create a production-quality UI mockup on a [device/canvas], for a fictional product named "[product name]".

Product context:
[Who uses it and what job the screen performs].

Screen structure:
- Header: include "[exact header text]", [controls].
- Primary panel: [main metric/table/chart/form].
- Secondary panel: [supporting cards, filters, status].
- Navigation: [tabs/sidebar/bottom nav labels].

Data and copy:
Use realistic values and labels: "[label 1]", "[value 1]", "[button text]", "[status]".

Visual system:
[Palette], [density], [typography feel], [icon style], [component spacing].

Quality constraints:
Crisp typography, precise alignment, real product density, no lorem ipsum, no broken icons, no incoherent chart labels.
```

## Research, technical, and system diagrams

Use when making architecture diagrams, AI agent workflows, security diagrams, research figures, or explainer graphics.

```text
Landscape 16:9 publication-grade technical diagram explaining [system/process].

Diagram grammar:
- Left zone: [input/source actors]
- Center zone: [processing modules/components]
- Right zone: [outputs/decisions]
- Bottom strip: [timeline/legend/evidence/status]

Relationships:
Use arrows for [flow], dashed lines for [risk/optional path], color [A] for [meaning], color [B] for [meaning].

Exact labels:
"[module 1]", "[module 2]", "[data type]", "[risk label]", "[output label]".

Style:
White or very light background, restrained palette, thin vector-like lines, large readable labels, conference-paper clarity.

Avoid:
Decorative sci-fi dashboard, tiny illegible labels, random math, fake company logos.
```

## Data visualization concepts

Use when the image is a visual concept of a chart, not a real computed chart. For analytical reports, prefer real data tooling.

```text
Create a [chart family] visualization concept about [metric/topic].

Structure:
[Small multiples / network graph / treemap / Sankey / timeline / choropleth] with [number of panels/groups].

Encodings:
- X axis: [field and units]
- Y axis: [field and units]
- Color: [meaning]
- Size/thickness: [meaning]

Labels:
Use exact labels: "[title]", "[axis label]", "[legend item]", "[annotation]".

Style:
Editorial, readable, generous margins, consistent scales, accessible contrast.

Avoid:
Fake precision, unreadable axes, inconsistent legends, random numbers unless supplied.
```

## Infographics and field guides

Use when the image should teach, compare, classify, or explain an object/process.

```text
Create a [aspect ratio] [field guide / museum catalog board / educational infographic] about [subject].

Fixed layout:
- Top title band: "[exact title]"
- Main illustration zone: [central object/process/cross-section]
- Annotation zone: [numbered labels and lead lines]
- Side panel: [summary, comparison, checklist]
- Bottom legend: [scale, materials, notes]

Annotation behavior:
Use thin lead lines, numbered callouts, readable labels, and consistent spacing.

Style:
[Scientific poster / museum board / classroom wall chart / editorial explainer] with [palette].

Avoid:
Cartoon chaos, unlabeled parts, garbled labels, excessive realism where clarity matters.
```

## Product and food renders

Use when multiple visual systems must be controlled: product, material, environment, particles, lighting.

```text
/* PRODUCT_RENDER_CONFIG: [short name]
   AESTHETIC: [premium commercial photography / editorial product render] */
{
  "canvas": "[aspect ratio]",
  "subject": "[product/food object]",
  "composition": "[hero angle, placement, scale]",
  "materials": ["[material 1]", "[surface detail]", "[texture]"],
  "environment": "[studio/table/location/background]",
  "lighting": "[softbox/natural/window/backlight/highlights]",
  "motion_or_details": ["[splash/steam/crumbs/particles/condensation]"],
  "palette": "[colors]",
  "output_mood": "[premium, calm, energetic, tactile]",
  "avoid": ["cheap e-commerce look", "plastic CGI", "fake brand marks", "unreadable label text"]
}
```

## Photorealistic scenes

Use when the desired result should feel captured, not designed.

```text
Create a photorealistic [scene] as if captured by [camera/capture context].

Capture:
[Eye level / crowd distance / handheld phone photo / 28 mm lens feel / natural morning side light].

Scene density:
Include [5-12 concrete nouns: objects, surfaces, signs, weather, reflections, tools, furniture].

Human/context details:
[People, gestures, scale, imperfections, lived-in traces].

Style constraints:
RAW, unpolished realism, natural color, plausible shadows, no glossy AI-ad look unless requested.
```

## Multi-panel boards and storyboards

Use for character sheets, proof sheets, storyboard grids, visual explorations, and concept boards.

```text
Create a [grid size] [storyboard / character sheet / exploration board] with [number] panels.

Global consistency:
Same [character/product/world], same palette, same identity markers, coherent lighting and style.

Panel roles:
1. [Panel role/shot]
2. [Panel role/shot]
3. [Panel role/shot]

For storyboards:
Add camera language in each panel: WIDE, OTS, CU, low angle, aerial, static, pan, match cut.

Quality constraints:
Clearly separated panels, readable captions if used, no identity drift, no random extra panels.
```

## Image editing with references

Use when a source image is attached or the user wants to preserve an existing image.

```text
Preserve:
[Identity, pose, product shape, logo/text if allowed, composition, color relationships, lighting direction, background elements].

Change:
[Specific requested edit: replace background, adjust outfit, add object, change style, remove distraction, extend canvas].

Output:
[Aspect ratio, style, final use, quality constraints].

Avoid:
Changing face/product identity, altering exact text, adding extra objects, changing camera angle unless requested.
```

## Quick repair checklist

- Does it say the artifact type and aspect ratio first?
- Are all required visible words quoted exactly?
- Is the layout explicit enough to prevent improvisation?
- Does the style name a real visual context, not only "beautiful"?
- Are labels, axes, panels, legends, and UI values specified where needed?
- Does the avoid-line target likely failures rather than generic negativity?
- For edits, are preserve/change instructions separated?
- For carousels, is the mode clearly marked as concept, production, or overlap experiment?
