#!/usr/bin/env python3
"""Content checks for AI Systems Lab. Exit code 1 on any error.

- lessons, cases and questions follow their formats (dacospace parses them)
- no em dashes
- every URL in lessons/ and cases/ appears in docs/research/ (no invented sources)
- case files link only to lessons that exist, lessons link only to cases that exist
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
errors: list[str] = []
err = errors.append

URL = re.compile(r"\((https?://[^)\s]+)\)")
research = "\n".join(p.read_text() for p in (ROOT / "docs/research").glob("*.md"))
known = {u.rstrip(".,") for u in URL.findall(research)}

roadmap = {m.group(1) for m in re.finditer(r"^\| (\d{2}) \|", (ROOT / "PROGRESS.md").read_text(), re.M)}
cases = {p.stem for p in (ROOT / "cases").glob("*.md")}

LESSON_SECTIONS = ["The problem", "Why it is hard", "The idea", "In practice at Northwind",
                   "What strong engineers know", "Decide", "One sentence summary", "Check question", "Sources"]
CASE_SECTIONS = ["The system", "What was observed", "Stop and think", "What actually happened",
                 "Root causes", "What would have prevented it", "The lesson for your system", "Sources"]
Q_SECTIONS = ["Prompt", "Clarifications", "Follow-ups", "Rubric", "Pitfalls"]


def sections(text: str) -> list[str]:
    return [l[3:].strip() for l in text.splitlines() if l.startswith("## ")]


def in_order(found: list[str], wanted: list[str]) -> bool:
    i = 0
    for s in found:
        if i < len(wanted) and s.startswith(wanted[i]):
            i += 1
    return i == len(wanted)


def common(p: pathlib.Path, text: str):
    if "\u2014" in text:
        err(f"{p.relative_to(ROOT)}: contains an em dash")
    for u in URL.findall(text):
        if u.rstrip(".,") not in known:
            err(f"{p.relative_to(ROOT)}: URL not in docs/research: {u}")


for p in sorted((ROOT / "lessons").glob("*.md")):
    t = p.read_text()
    m = re.match(r"# Lesson (\d{2}) · .+\n\n\*\*Reading time:\*\* \d+ min · \*\*Module:\*\* [^·]+ · \*\*Concepts:\*\* .+\n\*\*Cases:\*\* (.*)\n", t)
    if not m:
        err(f"{p.name}: heading or meta lines do not match the lesson format")
    else:
        if m.group(1) not in roadmap or not p.name.startswith(m.group(1) + "-"):
            err(f"{p.name}: lesson number does not match the file name or PROGRESS.md")
        for slug in filter(None, re.split(r"[,\s]+", m.group(2))):
            if slug not in cases:
                err(f"{p.name}: links case '{slug}' which does not exist")
    if not in_order(sections(t), LESSON_SECTIONS):
        err(f"{p.name}: sections missing or out of order: {sections(t)}")
    common(p, t)

for p in sorted((ROOT / "cases").glob("*.md")):
    t = p.read_text()
    m = re.match(r"# Case · .+\n\n\*\*Category:\*\* (Security|Agents|Evals|Knowledge|Production) · \*\*Lessons:\*\* ([\d, ]+) · \*\*Severity:\*\* .+\n", t)
    if not m:
        err(f"{p.name}: heading or meta line does not match the case format")
    else:
        for nn in re.split(r"[,\s]+", m.group(2).strip()):
            if nn not in roadmap:
                err(f"{p.name}: links lesson {nn} which is not on the roadmap")
    if not in_order(sections(t), CASE_SECTIONS):
        err(f"{p.name}: sections missing or out of order: {sections(t)}")
    common(p, t)

for p in sorted((ROOT / "questions").glob("*.md")):
    t = p.read_text()
    fm = re.match(r"---\nid: (\S+)\ntitle: .+\nlevel: (junior|mid|senior)\ntopics: \[ai(, [a-z0-9-]+)*\]\nminutes: \d+\n---\n", t)
    if not fm:
        err(f"{p.name}: frontmatter must be id, title, level, topics (starting with ai), minutes")
    elif fm.group(1) != p.stem:
        err(f"{p.name}: id must match the file name")
    if sections(t) != Q_SECTIONS:
        err(f"{p.name}: sections must be exactly {Q_SECTIONS}, found {sections(t)}")
    common(p, t)

for e in errors:
    print("error:", e)
print(f"{len(list((ROOT / 'lessons').glob('*.md')))} lessons, {len(cases)} cases, "
      f"{len(list((ROOT / 'questions').glob('*.md')))} questions, {len(known)} known sources, {len(errors)} errors")
sys.exit(1 if errors else 0)
