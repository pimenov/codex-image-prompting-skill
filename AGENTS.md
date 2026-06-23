# AGENTS.md

## Scope

This repository is a public reusable Codex skill package for image prompt design.

## Rules

- Keep committed content safe for public sharing.
- Do not add secrets, tokens, private keys, full env files, cookies, auth state, or service credentials.
- Do not add personal local paths, private project names, private tracker links, private customer data, or machine-specific access assumptions.
- Keep examples generic. Do not include private brands, client materials, private generated assets, or non-public screenshots.
- The skill is prompt-only. Do not add local image API wrappers, API-key setup, paid generation code paths, or CLI execution flows.
- Use neutral examples for public docs. Keep personal case studies outside this public package unless intentionally approved.
- Update README, examples, and validation when changing the skill surface.
- Run validation before finishing:

```bash
python3 scripts/validate_skills.py
scripts/install.sh --dry-run
python3 scripts/check_carousel_geometry.py --image path/to/master.png --slides 5 --export-size 1080
git diff --check
```

## Style

- Write skill instructions in concise procedural English.
- Write public explanatory docs in clear Russian unless the target audience or file convention calls for English.
- Prefer behavior, gates, and examples over motivational prose.
- Keep exact visible text in prompt examples quoted.
