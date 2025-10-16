# 🔗 LangGraph Use Cases

_Last reviewed: October 2025_

LangGraph specializes in stateful agent workflows with supervisors, hierarchical teams, and corrective RAG patterns.

## 🧠 Workflow Orchestration

| Use Case | Description | Code / Guide |
|---|---|---|
| Multi-Agent Workflow | Agent supervisor orchestrating multiple experts | <a href="https://github.com/langchain-ai/langgraph" target="_blank" rel="noopener noreferrer">Code ↗</a> |
| Hierarchical Agent Teams | Top-level supervisor delegating to sub-agents | <a href="https://github.com/langchain-ai/langgraph" target="_blank" rel="noopener noreferrer">Code ↗</a> |
| Multi-Agent Collaboration | Specialized agents working together on tasks | <a href="https://github.com/langchain-ai/langgraph" target="_blank" rel="noopener noreferrer">Code ↗</a> |
| Plan-and-Execute Agent | Generate multi-step plan then execute sequentially | <a href="https://github.com/langchain-ai/langgraph" target="_blank" rel="noopener noreferrer">Code ↗</a> |

## 🗄️ Data & SQL

| Use Case | Description | Code / Guide |
|---|---|---|
| SQL Agent | NL-to-SQL with schema inspection and error handling | <a href="https://github.com/langchain-ai/langgraph" target="_blank" rel="noopener noreferrer">Code ↗</a> |

## 🧪 Agentic RAG Patterns

| Use Case | Description | Code / Guide |
|---|---|---|
| Adaptive RAG | Dynamic retrieval strategy based on query complexity | <a href="https://github.com/langchain-ai/langgraph" target="_blank" rel="noopener noreferrer">Code ↗</a> |
| Adaptive RAG (Local) | Local models and retrieval for offline operation | <a href="https://github.com/langchain-ai/langgraph" target="_blank" rel="noopener noreferrer">Code ↗</a> |
| Agentic RAG | Agent determines strategy before generation | <a href="https://github.com/langchain-ai/langgraph" target="_blank" rel="noopener noreferrer">Code ↗</a> |
| Agentic RAG (Local) | Agentic RAG extended to local environments | <a href="https://github.com/langchain-ai/langgraph" target="_blank" rel="noopener noreferrer">Code ↗</a> |
| Corrective RAG (CRAG) | Evaluate and refine retrieved docs before generation | <a href="https://github.com/langchain-ai/langgraph" target="_blank" rel="noopener noreferrer">Code ↗</a> |
| Corrective RAG (Local) | CRAG using local resources | <a href="https://github.com/langchain-ai/langgraph" target="_blank" rel="noopener noreferrer">Code ↗</a> |
| Self-RAG | Reflect on responses, retrieve more if needed | <a href="https://github.com/langchain-ai/langgraph" target="_blank" rel="noopener noreferrer">Code ↗</a> |
| Self-RAG (Local) | Self-RAG with local models and data sources | <a href="https://github.com/langchain-ai/langgraph" target="_blank" rel="noopener noreferrer">Code ↗</a> |

## 🧪 QA & Evaluation

| Use Case | Description | Code / Guide |
|---|---|---|
| Chatbot Simulation Evaluation | Simulate user interactions to evaluate chatbot performance | <a href="https://github.com/langchain-ai/langgraph" target="_blank" rel="noopener noreferrer">Code ↗</a> |
| Reflection Agent | Critique and revise outputs for higher quality | <a href="https://github.com/langchain-ai/langgraph" target="_blank" rel="noopener noreferrer">Code ↗</a> |
| Reflexion Agent | Reflect on actions and outcomes for iterative improvement | <a href="https://github.com/langchain-ai/langgraph" target="_blank" rel="noopener noreferrer">Code ↗</a> |

---

### 🔧 Implementation Notes
- Use Supervisor for branching task orchestration
- Persist state across nodes for reliability and retries
- Combine with vector stores for robust agentic RAG

**← [Back to Use Cases](use-cases.md)**