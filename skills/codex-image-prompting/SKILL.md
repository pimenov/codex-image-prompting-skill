---
name: codex-image-prompting
description: "Draft, repair, structure, and use prompts for Codex Desktop image generation or image editing through the native image tool when available, without local image API wrappers, CLI execution, key setup, or paid local generation paths. Use when the user asks to generate, create, draw, render, edit, improve, or prepare an image prompt, including image prompt, poster, social card, UI mockup, diagram, infographic, data visualization, hero image, carousel, seamless carousel, panoramic carousel, панорамная карусель, бесшовная карусель, or visual concept for Codex Desktop imagegen."
---

# Codex image prompting

## Purpose

Use this skill to turn a rough visual intent into a strong prompt, then generate or edit the image with Codex Desktop's native image tool when the user asks for an image and the tool is available.

Do not install or call local image-generation CLIs, local image API scripts, environment files, key setup, or paid local generation paths. Use the native Codex image tool instead of asking the user to copy prompts elsewhere.

## Operating loop

1. Classify the task: `new image`, `edit/reference image`, `inpaint-like edit`, `prompt only`, `prompt repair`, or `seamless carousel`.
2. Identify artifact type: poster, hero image, article cover, social card, UI mockup, infographic, research figure, technical diagram, product render, photo scene, storyboard, character sheet, data visualization, or carousel.
3. Capture hard constraints: exact visible text, language, aspect ratio, audience, brand/product, output use, reference images, must-keep elements, and must-avoid elements.
4. For ambiguous or high-polish work, ask at most one concise question. For clear requests, proceed.
5. Draft the image prompt in English by default, while preserving user-supplied display text exactly in its original language.
6. Put structure before style: canvas, layout, zones, subject, exact text, visual semantics, materials/light, quality constraints, avoid-line.
7. If the user asked for a prompt only, return the prompt in a fenced block plus one short note.
8. If the user asked for an image, briefly surface the polished prompt or prompt summary, then call native image generation with that prompt.
9. After generation, give a concise critique and next-iteration suggestion, especially for typography, geometry, and production-readiness.

## Core rules

- Put every required visible string in quotes.
- Start with format and layout, not adjectives.
- Use fixed regions for infographics, educational boards, posters, and diagrams.
- Write UI prompts like product specs: device, screen, information architecture, components, labels, values, states.
- For data/research figures, specify chart family, axes, legends, labels, arrows, panels, color semantics, and readability.
- For photorealistic scenes, specify capture context: camera position, lens feel, lighting, realistic surfaces, and concrete objects.
- For multi-panel work, specify panel count, grid, roles, consistent palette/style, and identity continuity.
- For image edits, state what to preserve before what to change.
- Use negation sparingly for likely failure modes: garbled text, fake logos, unreadable microtext, distorted hands, incoherent UI, cropped labels.

## Seamless carousel modes

Use `references/prompt-patterns.md` for full carousel templates.

- `concept`: Generate or draft a single wide visual direction. It may be low-resolution or not exactly slice-ready. Label it as concept-only.
- `production`: Require a deterministic canvas, such as `5400x1080` for five `1080x1080` slides. Overlay exact text after image generation and export slices deterministically.
- `overlap experiment`: Generate adjacent sections with overlap/reference edges. Treat this as exploratory, not pixel-perfect. Still use deterministic final layout if publishing.

Never present a small generated panorama cropped and upscaled into slides as production-ready. If the master is smaller than `slides * export_size` wide and `export_size` tall, call it a style reference or concept.

## When to read references

Read `references/prompt-patterns.md` when:

- the prompt must be client-ready or publication-ready;
- the request involves UI, diagrams, data visualization, posters, dense text, product renders, image editing, or carousels;
- the first draft would otherwise be generic;
- the user asks to make a prompt better or more precise.

## Output shapes

For prompt-only requests:

```text
Prompt:
<polished prompt>

Note:
<one sentence explaining the main prompt strategy>
```

For generation requests:

```text
Prompt used:
<polished prompt or compact prompt summary>

Generation:
<call native image generation with the full polished prompt>

Review:
<one or two concrete notes about what worked and what to refine next>
```

Do not ask the user to copy the prompt into another tool when native image generation is available.

For edit/reference-image requests:

```text
Edit prompt:
Preserve: <identity, layout, product, face, text, composition, colors>.
Change: <specific transformation>.
Output: <format, style, quality, avoid-line>.
```

For carousel requests:

```text
Carousel mode:
<concept | production | overlap experiment>

Master prompt:
<wide-scene prompt or deterministic-layout brief>

Slice notes:
<slide count, export size, safe zones, typography plan, geometry caveat>
```

For carousel concept generation, generate the wide concept image when the user asks to see it. Still label it as concept-only unless the master geometry is verified for production slicing.

## Source pattern

This skill adapts prompt-craft ideas from `wuyoscar/GPT-Image2-Skill`, but intentionally replaces local API/CLI execution with native Codex image generation when available.
