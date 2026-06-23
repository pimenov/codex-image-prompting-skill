# Codex image prompting skill

Публичный prompt-only skill для Codex Desktop, который помогает превращать
сырой визуальный замысел в сильный промпт для генерации или редактирования
изображений.

Идея простая: не каждый визуальный запрос должен начинаться с API, ключей и
локальных генераторов. Часто самая ценная часть работы — правильно описать
артефакт: формат, сетку, текст, визуальную иерархию, ограничения, режим
публикации и ожидаемые ошибки.

## Что входит

| Файл | Назначение |
|---|---|
| `skills/codex-image-prompting/SKILL.md` | Skill-инструкция для Codex |
| `skills/codex-image-prompting/references/prompt-patterns.md` | Шаблоны промптов для разных визуальных задач |
| `examples/prompts/` | Нейтральные примеры промптов |
| `scripts/validate_skills.py` | Проверка структуры и public-safety |
| `scripts/check_carousel_geometry.py` | Проверка, годится ли master image для production-нарезки карусели |

## Когда использовать

Skill полезен, когда нужно подготовить или улучшить промпт для:

- постера, обложки, social card или thumbnail;
- UI mockup;
- схемы, технической диаграммы или инфографики;
- data visualization concept;
- image edit prompt с сохранением важных элементов;
- seamless/panoramic carousel для соцсетей.

Skill не запускает локальную генерацию, не просит API keys и не содержит
оберток вокруг image API. Он проектирует промпт и production-aware workflow.

## Быстрая установка

```bash
git clone <repo-url>
cd codex-image-prompting-skill
python3 scripts/validate_skills.py
scripts/install.sh --dry-run
scripts/install.sh
```

По умолчанию installer копирует skill сюда:

```bash
${CODEX_HOME:-$HOME/.codex}/skills
```

Установить только этот skill:

```bash
scripts/install.sh --skill codex-image-prompting
```

После установки перезапустите Codex, чтобы skill появился в списке доступных.

## Примеры запросов

```text
Use $codex-image-prompting: prepare a prompt for a conference poster about a practical AI workflow.
```

```text
Use $codex-image-prompting: make this rough UI mockup request precise enough for Codex Desktop image generation.
```

```text
Use $codex-image-prompting: подготовь промпт для бесшовной карусели из 5 слайдов про то, как команда превращает хаос задач в ясный план.
```

Готовые примеры лежат в `examples/prompts/`.

## Панорамные карусели

Для seamless carousel skill различает три режима:

- `concept` — быстро получить визуальное направление; можно использовать native image generation и не требовать точной геометрии;
- `production` — собрать детерминированный холст нужного размера, наложить типографику и экспортировать слайды;
- `overlap experiment` — пробовать последовательную генерацию частей с нахлестом, но не считать ее пиксельно надежной.

Для 5 квадратных слайдов `1080x1080` master должен быть не меньше
`5400x1080`. Если генератор вернул маленькую панораму, например `2172x724`,
это style reference или concept art, а не production master. Кроп и upscale не
создают недостающие детали.

Проверить геометрию можно так:

```bash
python3 scripts/check_carousel_geometry.py --image path/to/master.png --slides 5 --export-size 1080
```

## Что этот пакет не делает

- Не содержит локального image API wrapper.
- Не настраивает API keys.
- Не гарантирует пиксельно точные seamless-переходы между независимо сгенерированными изображениями.
- Не заменяет Figma, Photoshop, HTML canvas или другой deterministic layout step для production assets.
- Не включает приватные case studies или приватные generated images.

## Атрибуция

Этот пакет вдохновлен prompt-craft подходом из
[`wuyoscar/GPT-Image2-Skill`](https://github.com/wuyoscar/GPT-Image2-Skill),
но не является зеркалом upstream-репозитория и не переносит его CLI/API слой.

Подробности: [NOTICE.md](NOTICE.md).

## Лицензия

MIT. См. [LICENSE](LICENSE).
