# Enterprise AI Projects Showcase (Areganti)

Source: https://areganti.notion.site/Enterprise-AI-Projects-Showcase-25bc91fa3236804b8765e54dde771262

## Why this matters
- Problem-first blueprints for enterprise-grade AI
- Emphasis on evaluation plans, guardrails, and cost/latency budgets
- Real-world categories you can adapt directly to your org

## Representative categories
- Medical documentation assistant (provider-facing, HIPAA-aware)
- Financial insights & analyst co-pilot (agentic RAG + tools)
- Retail & support automations (multi-agent routing + escalation)
- SRE co-pilot (incident triage, remediation playbooks)
- Compliance & audits (claims processing, doc review, redaction)
- Cloud cost control & FinOps monitoring (policy-based actions)
- Investor relations & proposal assistants (briefing kits)
- Voice interview coach & learning assistants
- Real-estate pricing, planning, and scheduling agents

## Map to this repository
- Use Cases → Map each category to existing industry tables:
  - Healthcare, Finance, Support, Productivity, Security, Development
- Framework picks by pattern:
  - Multi-agent routing: CrewAI, AutoGen, LangGraph
  - Stateful workflows & eval loops: LangGraph
  - Research/briefs with citations: Agno, GPT Researcher
  - Data compliance pipelines: LangChain + policy engines
- Observability & guardrails:
  - AgentOps, LangSmith, eval suites; PII redaction, hallucination checks

## Implementation notes
- Start with an eval plan (tasks, metrics, success thresholds)
- Define guardrails (PII, redaction, content policy)
- Budget cost/latency with SLAs per user journey
- Add observability from day one (traces, errors, retries)
- Pilot with narrow scope, expand with measured wins

## Contribute
Have a concrete case brief (problem → approach → outcome)?
- Open a PR adding it under the relevant industry category
- Include links to code/notebooks and evaluation notes
