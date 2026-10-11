# Research dossiers

The source material behind every lesson, case file and design question. Each dossier was built
from primary sources (engineering blogs, postmortems, papers, court decisions, official docs) that
were opened and read, and lists them with dates.

Rule for contributors: a URL may appear in `lessons/` or `cases/` only if it appears here first.
`python3 scripts/check.py` enforces it.

| Dossier | Covers |
|---|---|
| [security.md](security.md) | prompt injection, exfiltration, MCP and agent supply chain |
| [agent-reliability.md](agent-reliability.md) | workflows vs agents, context, loops, multi-agent, approvals |
| [evals-observability.md](evals-observability.md) | error analysis, LLM judges, agent evals, tracing, postmortems |
| [rag-enterprise-knowledge.md](rag-enterprise-knowledge.md) | RAG failure points, retrieval, permissions, grounding, liability |
| [production-governance.md](production-governance.md) | cost, latency, outages, guardrails, governance, privacy |
| [hands-on-landscape.md](hands-on-landscape.md) | existing labs, benchmarks, eval tools, local models |
