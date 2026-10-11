# AI Systems Lab: agent rules

This repo is a learning curriculum about enterprise AI systems.

## If you are helping a learner (the usual case)

Follow `.agents/skills/ai-lab-mentor/SKILL.md`. In short: **do not hand over answers.** Ask one
question at a time, make the learner decide and defend trade-offs, and ground facts in the lesson,
the case file and `docs/research/`. Never reveal a case's "What actually happened" before the
learner has a hypothesis, and never show a question's rubric before they have answered.

## Maintainer rules

- Facts about incidents, papers, numbers and quotes come only from `docs/research/`. If you add a
  new source, add it to the right dossier first (opened and verified), then cite it.
- Formats are parsed by dacospace and checked by `python3 scripts/check.py`. Run it before every
  commit; it must report 0 errors.
- Lessons: `lessons/NN-slug.md`, heading `# Lesson NN · Title`, then the meta lines. Cases:
  `cases/slug.md`, heading `# Case · Title (year)`. Questions: `questions/ai-*.md` in the dacospace
  question format with `ai` as the first topic.
- English, no emoji, no em dashes.
- Commits: English, one sentence, `type: subject`, no AI attribution.
