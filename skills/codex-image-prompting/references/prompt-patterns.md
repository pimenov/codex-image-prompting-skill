# Prompt patterns for Codex Desktop imagegen

Use these patterns as prompt skeletons. Replace bracketed fields with concrete details. Keep user-provided display text exact.

## Table of contents

- Universal prompt skeleton
- Posters, covers, social cards
- Social carousel slides
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

## Common format menu

Use this quick mapping when the user describes the goal in plain language:

| User intent | Default format | Prompt focus |
|---|---|---|
| "picture for a post" | 16:9 social cover or 1:1 social card | one strong visual metaphor, one large headline |
| "carousel" | 3-7 separate 1:1 slides | one idea per slide, consistent style |
| "README / article image" | 16:9 article image | workflow, concept, or product idea without logos |
| "app idea / screen" | UI mockup | product context, screen structure, realistic labels |
| "explain how it works" | diagram or infographic | zones, arrows, labels, visual hierarchy |
| "product / object" | product render | materials, lighting, camera, environment |
| "realistic scene" | photorealistic scene | capture context, objects, people, lighting |

For visible text, start with one large headline. Add a subtitle only when it is short and necessary.

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
[User-requested style or a topic-appropriate visual style] with [palette], [lighting], [texture/material if relevant].

Avoid:
Unreadable microtext, garbled letters, fake sponsor logos, stock-photo blandness, cluttered hierarchy.
```

## Social carousel slides

Use for Instagram, Threads, LinkedIn, or similar carousels. For the first public version of this skill, prefer separate square slides in one consistent style. This is simpler, more reliable, and easier to iterate than a seamless panorama.

### Separate-slide carousel

Use this mode for practical social publishing.

```text
Create square 1:1 carousel slide [K] of [N] for [platform/audience].

Theme:
"[central idea]"

Visible text:
Render the exact large headline: "[short headline]"
Render the exact short subtitle if needed: "[short subtitle]"

Scene:
[What this slide shows: hook/problem/process/proof/punchline].

Continuity:
Keep the same visual system across all slides: [palette], [lighting], [character/object continuity], [icon style], [background grammar].

Output constraints:
Large readable text, one clear idea per slide, no random extra text, no tiny labels, no fake logos.
```

Recommended slide plan:

```text
1. Hook: "[short headline]"
2. Setup/problem: "[short headline]"
3. Method/process: "[short headline]"
4. Insight/proof: "[short headline]"
5. Punchline/CTA: "[short headline]"
```

### Panoramic concept

Use this mode only to explore a wide visual direction. Do not treat it as a guaranteed slice-ready master.

```text
Create one ultra-wide panoramic concept artwork for a social media carousel, designed to suggest [N] connected slides.

Theme:
"[central idea]"

Continuity:
A single visual element travels across the panorama: [glowing line / road / ribbon / knowledge graph / timeline / river / cable].

Output constraints:
Continuous world, no hard panel borders, no random text, no dense microtext. This is concept art for direction, not a production slicing workflow.
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
[User-requested diagram style or a simple readable diagram style], large readable labels, clear lines, consistent spacing, accessible contrast.

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
[User-requested visualization style or a simple readable chart style], generous margins, consistent scales, accessible contrast.

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
   AESTHETIC: [user-requested product/render aesthetic] */
{
  "canvas": "[aspect ratio]",
  "subject": "[product/food object]",
  "composition": "[hero angle, placement, scale]",
  "materials": ["[material 1]", "[surface detail]", "[texture]"],
  "environment": "[studio/table/location/background]",
  "lighting": "[softbox/natural/window/backlight/highlights]",
  "motion_or_details": ["[splash/steam/crumbs/particles/condensation]"],
  "palette": "[colors]",
  "output_mood": "[user-requested mood or topic-appropriate mood]",
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
- For carousels, is it clear whether this is a separate-slide set or only a panoramic concept?
