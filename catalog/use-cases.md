# 📚 AI Agent Use Cases

_Last reviewed: October 2025_

A curated catalog of practical AI agent use cases organized by industry and framework, with patterns you can adapt in production. All external resources open in a new tab.

## 🏭 Industry Use Cases

| Use Case | Sector | Summary | Code / Notebook |
|---------|--------|---------|-----------------|
| Clinical report summarizer | Healthcare | Parse and condense clinical or lab reports with privacy safeguards | <a href="https://github.com/LibertFan/AI_Hospital" target="_blank" rel="noopener noreferrer">AI Hospital ↗</a> |
| Claims intake automation | Healthcare/Insurance | Triage claims, validate docs, notify stakeholders | <a href="https://aws-samples.github.io/amazon-bedrock-agents-healthcare-lifesciences/guides/" target="_blank" rel="noopener noreferrer">AWS Bedrock Agents ↗</a> |
| Quant strategy runner | Finance | Backtest and execute strategies with risk gates | <a href="https://github.com/AI4Finance-Foundation/FinRobot" target="_blank" rel="noopener noreferrer">FinRobot ↗</a> |
| Market intel researcher | Finance | Aggregate filings, news, and signals into briefs | <a href="https://www.youtube.com/watch?v=izW4abxIWe8" target="_blank" rel="noopener noreferrer">Trading workflow (video) ↗</a> |
| Resume-to-role matcher | HR | Parse profiles and rank against job criteria | <a href="https://www.make.com/en/how-to-guides/ai-recruiting-agent" target="_blank" rel="noopener noreferrer">Make guide ↗</a> |
| Auto-outreach and scheduling | HR | Personalized outreach + interview scheduling | <a href="https://www.uipath.com/solutions/department/hr-automation" target="_blank" rel="noopener noreferrer">UiPath HR agentic ↗</a> |
| Study companion | Education | Tutoring, quizzes, adaptive practice | <a href="https://github.com/microsoft/ai-agents-for-beginners" target="_blank" rel="noopener noreferrer">Agents for Beginners ↗</a> |
| Web navigator & extractor | Web Automation | Browse, scrape, and structure page data | <a href="https://blog.apify.com/ai-web-scraping-python/" target="_blank" rel="noopener noreferrer">Apify tutorial ↗</a> |
| Red-team probe agent | Cybersecurity | Automated vulnerability analysis and reporting | <a href="https://blogs.cisco.com/security/ai-agent-for-color-red" target="_blank" rel="noopener noreferrer">Cisco red-team flow ↗</a> |
| Alert triage & response | Cybersecurity | Triage alerts, hunt IOCs, generate reports | <a href="https://radiantsecurity.ai/learn/ai-agents/" target="_blank" rel="noopener noreferrer">SOC agents overview ↗</a> |

## 🔧 Framework-specific Examples

### CrewAI
- Communication assistant (email triage, responses)
- Meeting copilot (agenda, minutes, actions)
- Lead scoring and prioritization
- Hiring pipeline automation
- Trip planning and itinerary builder

### AutoGen / AG2
- Group-chat orchestration (manager + experts)
- Agentic RAG (retrieval + critic + synthesis)
- Nested conversations for sub-tasking
- Web/tools integration (search, SQL, Whisper)

### LangGraph
- Plan-and-execute templates
- Supervisor + hierarchical teams
- Corrective/self-reflective RAG flows
- SQL QA over enterprise data

### Agno
- Support assistant over documentation
- Literature review with citations
- Finance market snapshot agent
- Social/YouTube topic analyzer

## 🧩 Workflow Patterns (Reusable)
- Email automation (triage → draft → approval → send)
- Meetings (schedule → agenda → notes → follow-up)
- Recruiting (source → screen → outreach → schedule)
- Research (collect → assess → synthesize → cite)
- Data pipelines (scrape → validate → enrich → store)

## 🛠️ Implementation Notes
- Start narrow with clear acceptance criteria
- Add tools incrementally; ground with retrieval
- Instrument for observability and guardrails
- Evaluate with domain tasks; keep human-in-the-loop

Contributions welcome: propose new use cases via PRs or issues.