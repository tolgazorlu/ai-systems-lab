# AI Systems Lab

Learn to design, break and defend enterprise AI systems: tool-using agents, RAG over company data,
evals, security, and the operations around them. Built for software engineers who already know
backend systems and want to be the person their company trusts with AI in production.

Everything here comes from real incidents and primary sources: engineering postmortems, security
disclosures, papers, court decisions, official docs. The research behind it is in
[`docs/research/`](docs/research/README.md), and `scripts/check.py` refuses any link that is not in it.

## What is inside

| | |
|---|---|
| `lessons/` | 23 lessons, 15-20 minutes each. A real problem, why it is hard, the ideas that work, what strong engineers know, a decision to make, a check question. |
| `cases/` | Incident files. You get the system and the symptoms, form a hypothesis, then reveal what actually happened, the root causes and the defenses. |
| `questions/` | Senior AI system design interview questions with clarifications, follow-ups, rubric and pitfalls. |
| `docs/research/` | The source dossiers: every incident, paper and number, with links. |
| `PROGRESS.md` | The roadmap, module by module. |

Modules: Foundations, Agents, Security, Evals, Knowledge (RAG), Production, Capstone.

Most examples use **Northwind Supply**, a fictional B2B distributor, and **Desk**, its AI assistant
that answers dealers from internal documents, looks up orders, issues credits and reads support
email. Desk is fiction; the incidents next to it are not.

## How to use it

The best way is [dacospace](https://github.com/tolgazorlu/dacospace), which renders this repo under
**AI**: lessons with progress, case files with a hypothesis box and a Reveal button, practice pages
for the design questions, and copy-paste prompts that turn any coding assistant into a tutor,
an incident commander or an interviewer.

Clone it next to dacospace:

```sh
git clone https://github.com/tolgazorlu/ai-systems-lab.git
```

A good rhythm: one lesson a day, its case files the same day, and the design question in the
Interview tab every other day.

## Working with an AI assistant

`AGENTS.md` (also `CLAUDE.md`) and the skill in `.agents/skills/ai-lab-mentor/` tell any assistant
how to teach with this repo: ask before telling, make you decide trade-offs, never hand over the
reveal or the rubric early, and never invent facts beyond the sources.

## Hands-on missions (next)

The next part is a runnable, deliberately flawed version of Desk (local model via Ollama, no paid
API needed) with missions that mirror the lessons: inject it through a support email, watch it
leak data through a markdown image, make its refund tool idempotent, build its eval set, calibrate
an LLM judge, put permissions into retrieval. Each mission will be measured before it ships.

## Checks

```sh
python3 scripts/check.py
```
