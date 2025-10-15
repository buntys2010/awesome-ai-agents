# AgentBench: Getting Started Guide

Quick setup and smoke test guide for running AgentBench evaluation on your agents.

## 🎯 What is AgentBench?

AgentBench is the most comprehensive benchmark for LLM-based agents, testing across 8 different environments:
- Operating System tasks
- Database operations
- Knowledge graph queries
- Digital card games
- Lateral thinking puzzles
- Household simulations
- Web shopping
- Web browsing

**Repository**: [THUDM/AgentBench](https://github.com/THUDM/AgentBench)

---

## 🚀 Quick Setup

### Prerequisites
- Python 3.8+
- Docker (for sandboxed environments)
- OpenAI API key or local model setup

### Installation
```bash
# Clone the repository
git clone https://github.com/THUDM/AgentBench.git
cd AgentBench

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with your API keys
```

### Configuration
```python
# config/agents/my_agent.json
{
  "name": "my_agent",
  "model": "gpt-4",
  "max_tokens": 2048,
  "temperature": 0.7,
  "system_message": "You are a helpful AI agent that can complete various tasks."
}
```

---

## 🎯 Running Your First Evaluation

### Smoke Test (Web Shopping Environment)
```bash
# Run a single environment with minimal tasks
python run_benchmark.py \
  --agent_config config/agents/my_agent.json \
  --environment web_shopping \
  --num_tasks 5 \
  --output results/smoke_test

# View results
python analyze_results.py results/smoke_test
```

### Full Evaluation
```bash
# Run all 8 environments (takes 2-4 hours)
python run_benchmark.py \
  --agent_config config/agents/my_agent.json \
  --all_environments \
  --output results/full_eval_$(date +%Y%m%d)
```

---

## 📈 Understanding Results

### Key Metrics
- **Success Rate**: Percentage of tasks completed successfully
- **Partial Credit**: Partial completion scores
- **Efficiency**: Steps taken vs optimal path
- **Error Analysis**: Common failure patterns

### Sample Output
```json
{
  "overall_score": 0.68,
  "environment_scores": {
    "os": 0.75,
    "database": 0.65,
    "web_shopping": 0.70,
    "web_browsing": 0.60
  },
  "task_breakdown": {
    "completed": 34,
    "partial": 8,
    "failed": 8
  }
}
```

---

## ⚡ Performance Tips

### Reduce Evaluation Time
```bash
# Run subset of tasks per environment
python run_benchmark.py \
  --environment os \
  --num_tasks 10 \
  --fast_mode

# Parallel execution (if resources allow)
python run_benchmark.py \
  --parallel \
  --max_workers 4
```

### Cost Optimization
```python
# Use cheaper models for initial testing
{
  "model": "gpt-3.5-turbo",  # Instead of gpt-4
  "max_tokens": 1024,        # Reduced token limit
  "temperature": 0.1         # More deterministic
}
```

---

## 🔧 Custom Agent Integration

### Integrating Your Framework
```python
# agents/my_framework_agent.py
from agentbench.agent_base import Agent

class MyFrameworkAgent(Agent):
    def __init__(self, config):
        super().__init__(config)
        # Initialize your agent framework here
    
    def act(self, observation, available_actions):
        # Implement your agent's decision-making logic
        # observation: current state/context
        # available_actions: list of possible actions
        
        # Your framework's logic here
        action = self.your_agent.decide_action(observation, available_actions)
        return action
    
    def reset(self):
        # Reset agent state between tasks
        self.your_agent.reset()
```

### Registration
```python
# Register your agent in the evaluation system
from agents.my_framework_agent import MyFrameworkAgent

AGENT_REGISTRY = {
    "my_framework": MyFrameworkAgent,
    # ... other agents
}
```

---

## 📊 Benchmark Comparison

### Current Leaderboard (approximate)
| Agent | Overall Score | OS | Database | Web | Notes |
|-------|---------------|----|---------|----- |-------|
| GPT-4 + CoT | 0.50 | 0.72 | 0.45 | 0.38 | Chain-of-thought prompting |
| Claude-3.5-Sonnet | 0.48 | 0.70 | 0.42 | 0.35 | Strong reasoning |
| GPT-3.5-Turbo | 0.33 | 0.58 | 0.28 | 0.25 | Cost-effective option |

---

## 🔗 Additional Resources

- **Official Documentation**: [AgentBench Docs](https://github.com/THUDM/AgentBench/blob/main/README.md)
- **Paper**: [AgentBench: Evaluating LLMs as Agents](https://arxiv.org/abs/2308.03688)
- **Leaderboard**: [Current Results](https://llmbench.ai/agent)
- **Community**: [GitHub Discussions](https://github.com/THUDM/AgentBench/discussions)

---

*This guide provides a quick start for AgentBench evaluation. For comprehensive testing, refer to the official documentation and consider running the full benchmark suite.*