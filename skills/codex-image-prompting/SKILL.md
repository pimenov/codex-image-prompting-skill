---
name: codex-image-prompting
description: "Turn rough visual ideas into clear prompts for Codex Desktop ImageGen, then generate or edit images with the native image tool when available. Use when the user asks to create, generate, draw, render, edit, improve, or prepare an image prompt for posters, social cards, thumbnails, carousel slides, UI mockups, diagrams, infographics, data visualization concepts, README or article images, product renders, photo scenes, storyboards, or visual concepts. This skill is for prompt design and ImageGen iteration, not local API wrappers, CLI execution, key setup, deterministic layout tooling, or paid local generation paths."
---

# Codex image prompting

## Purpose

Use this skill to turn a rough visual intent into a strong prompt, then generate or edit the image with Codex Desktop's native image tool when the user asks for an image and the tool is available.

Keep the first public version simple: prompt design plus native ImageGen iteration. Do not install or call local image-generation CLIs, local image API scripts, environment files, key setup, paid local generation paths, canvas exporters, or deterministic typography tooling. Use the native Codex image tool instead of asking the user to copy prompts elsewhere.

## Operating loop

1. Classify the task: `new image`, `edit/reference image`, `prompt only`, `prompt repair`, or `carousel slides`.
2. Identify artifact type: poster, hero image, article cover, social card, thumbnail, UI mockup, infographic, research figure, technical diagram, product render, photo scene, storyboard, character sheet, data visualization, README image, article image, or carousel slide set.
3. Capture hard constraints: exact visible text, language, aspect ratio, audience, brand/product, output use, reference images, must-keep elements, and must-avoid elements.
4. For ambiguous or high-polish work, ask at most one concise question. For clear requests, proceed.
5. Draft the image prompt in English by default, while preserving user-supplied display text exactly in its original language.
6. Put structure before style: canvas, layout, zones, subject, exact text, visual semantics, materials/light, quality constraints, avoid-line.
7. If the user asked for a prompt only, return the prompt in a fenced block plus one short note.
8. If the user asked for an image, briefly surface the polished prompt or prompt summary, then call native image generation with that prompt.
9. After generation, give a concise critique and next-iteration suggestion, especially for text readability, composition, style fit, and whether the prompt should be simplified.

## Core rules

- Put every required visible string in quotes.
- Start with format and layout, not adjectives.
- Use fixed regions for infographics, educational boards, posters, and diagrams.
- Write UI prompts like product specs: device, screen, information architecture, components, labels, values, states.
- For data/research figures, specify chart family, axes, legends, labels, arrows, panels, color semantics, and readability.
- For photorealistic scenes, specify capture context: camera position, lens feel, lighting, realistic surfaces, and concrete objects.
- For multi-panel work, specify panel count, grid, roles, consistent palette/style, and identity continuity.
- For image edits, state what to preserve before what to change.
- For visible text, prefer short, large, high-contrast phrases. Long text, small labels, and many exact captions are likely to fail in ImageGen.
- Use negation sparingly for likely failure modes: garbled text, fake logos, unreadable microtext, distorted hands, incoherent UI, cropped labels.

## Style Neutrality

Do not apply a house style by default. The skill should follow the user's requested style, brand, medium, genre, mood, and palette as closely as possible.

- If the user names a style, use that style and do not replace it with a generic tech/editorial look.
- If the user does not name a style, infer a lightweight style from the artifact and audience, then state it briefly before generation.
- Do not reuse palettes or aesthetics from examples unless the user asks for them.
- Do not default to any recurring aesthetic from prior examples, prior generations, or the assistant's own taste.
- When style is underspecified, offer or choose a neutral fit such as clean, readable, high-contrast, and topic-appropriate rather than a fixed palette.
- If a result drifts into an unintended style, repair the next prompt by naming both the desired style and the styles to avoid.

## Text Strategy

For the first version, do not route text through a separate overlay step. Try to get ImageGen to render text directly, but keep it simple.

- Good ImageGen text: one short headline, one short subtitle, large type, high contrast, clean background.
- Risky ImageGen text: paragraphs, dense labels, tables, small UI copy, many exact captions, long Cyrillic strings.
- If text fails, simplify the words and regenerate before proposing external design tools or manual layout.
- If the user explicitly asks for a production layout, explain that this skill focuses on prompting and ImageGen, not deterministic design assembly.

## Carousel Guidance

Use `references/prompt-patterns.md` for full carousel templates.

Prefer `separate-slide carousel` for social publishing: generate 3-7 square slides with one idea and one short headline per slide, while keeping the same visual system across prompts.

Use `panoramic carousel concept` only to explore a wide visual direction. Do not promise pixel-perfect seamless slicing or production geometry. If the user wants a publishable carousel, make a clear slide plan and generate separate slides unless they explicitly ask for a production design workflow outside this skill.

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
<separate-slide carousel | panoramic concept>

Slide plan:
<numbered list of slide messages and visuals>

Generation:
<generate the requested slide(s) with native ImageGen>
```

For carousel generation, start with either a full slide plan or the first 1-2 slides if the user wants to explore direction. Keep text large and short.

## Source pattern

This skill adapts prompt-craft ideas from `wuyoscar/GPT-Image2-Skill`, but intentionally replaces local API/CLI execution with native Codex image generation when available.
