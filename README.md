# Codex image prompting skill

Публичный prompt-first skill для Codex Desktop, который помогает превращать
сырой визуальный замысел в сильный промпт, а затем сразу запускать генерацию
или редактирование изображения, если в текущей среде доступен native image
generation.

Идея простая: перед генерацией полезно сначала спроектировать визуальную
задачу. Часто самая ценная часть работы — правильно описать артефакт: формат,
сетку, текст, визуальную иерархию, ограничения, режим публикации и ожидаемые
ошибки.

## Как он работает

1. Codex принимает сырой визуальный запрос.
2. Skill превращает его в структурированный промпт: формат, сетка, текст,
   визуальная иерархия, стиль, ограничения и ожидаемые ошибки.
3. Если пользователь просит именно картинку, Codex показывает или кратко
   фиксирует промпт и запускает native image generation.
4. Пользователь смотрит результат и дает правки; следующий проход уточняет
   промпт или делает edit prompt.

Так skill закрывает полный цикл: идея -> промпт -> картинка -> итерация.

## Что входит

| Файл | Назначение |
|---|---|
| `skills/codex-image-prompting/SKILL.md` | Skill-инструкция для Codex |
| `skills/codex-image-prompting/references/prompt-patterns.md` | Шаблоны промптов для разных визуальных задач |
| `examples/prompts/` | Нейтральные примеры промптов |
| `scripts/validate_skills.py` | Проверка структуры и public-safety |
| `scripts/check_carousel_geometry.py` | Проверка, годится ли master image для production-нарезки карусели |

## Когда использовать

Skill полезен, когда нужно подготовить промпт, сгенерировать картинку или
итеративно улучшить визуальный результат для:

- постера, обложки, social card или thumbnail;
- UI mockup;
- схемы, технической диаграммы или инфографики;
- data visualization concept;
- image edit prompt с сохранением важных элементов;
- seamless/panoramic carousel для соцсетей.

Skill не запускает локальные генераторы, не просит API keys и не содержит
оберток вокруг image API. Он использует native image generation там, где Codex
его предоставляет, а для production-aware задач отдельно фиксирует ограничения
по геометрии, тексту и нарезке.

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
Use $codex-image-prompting: generate a conference poster about a practical AI workflow. Show me the prompt and the image.
```

```text
Use $codex-image-prompting: generate a UI mockup for a dashboard that turns incoming research notes into tasks.
```

```text
Use $codex-image-prompting: сделай concept-картинку для бесшовной карусели из 5 слайдов про то, как команда превращает хаос задач в ясный план.
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
- Не заменяет native image generation там, где оно уже есть в Codex.
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
