# Getting Started with AI Agents 🚀

This guide helps you choose the right AI agent framework and get started quickly with practical examples.

## 🧭 Quick Decision Tree

### 1. What type of agent do you need?

#### 🤖 **Single Agent** (One AI doing focused tasks)
- **AutoGPT**: General purpose, autonomous task execution
- **GPT Researcher**: Specialized for research and report generation  
- **Open Interpreter**: Code execution and computer interaction
- **Phidata**: Type-safe agents with structured outputs

#### 👥 **Multi-Agent** (Team of AIs collaborating)
- **CrewAI**: Role-based teams (Researcher + Writer + Analyst)
- **AutoGen**: Conversation-based collaboration
- **MetaGPT**: Software company simulation
- **OpenAI Swarm**: Lightweight agent handoffs

#### 🔗 **RAG-Enhanced** (Agents with knowledge retrieval)
- **LangChain**: Comprehensive framework with RAG support
- **LlamaIndex**: Data-focused agent applications
- **LangGraph**: Stateful workflows with memory

### 2. What's your experience level?

#### 🌱 **Beginner** (New to AI agents)
- **Start with**: CrewAI or AutoGPT
- **Why**: Simple setup, great documentation, visual interfaces
- **Time to first agent**: 30 minutes

#### 💼 **Intermediate** (Some AI/ML experience)
- **Start with**: LangChain or AutoGen
- **Why**: More flexibility, production-ready features
- **Time to first agent**: 2-3 hours

#### 🔬 **Advanced** (AI researcher/engineer)
- **Start with**: LangGraph, DSPy, or build from scratch
- **Why**: Full control, cutting-edge features, research capabilities
- **Time to first agent**: 1-2 days

### 3. What's your deployment target?

#### 💻 **Local Development**
- **OpenAI Swarm**: Minimal dependencies, quick prototyping
- **Open Interpreter**: Local code execution
- **BabyAGI**: Simple task management

#### ☁️ **Cloud Production**
- **LangChain + LangSmith**: Enterprise monitoring
- **Semantic Kernel**: Microsoft ecosystem integration
- **Azure AutoGen**: Hosted multi-agent systems

#### 🔌 **MCP Integration** (Cutting-edge interoperability)
- **OpenAI Agents SDK**: Native MCP support
- **MCP Agent Framework**: Built specifically for MCP
- **Claude Desktop**: Consumer MCP applications

## 🚀 Quick Start Recipes

### Recipe 1: CrewAI Multi-Agent Team (Beginner)

**Use Case**: Create a research and content creation team

```bash
# Install CrewAI
pip install crewai crewai-tools
```

```python
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool, WebsiteSearchTool

# Define tools
search_tool = SerperDevTool()
web_tool = WebsiteSearchTool()

# Create agents
researcher = Agent(
    role='Senior Researcher',
    goal='Research comprehensive information on AI agents',
    backstory='Expert researcher with 10+ years in AI/ML',
    tools=[search_tool, web_tool],
    verbose=True
)

writer = Agent(
    role='Technical Writer',
    goal='Write engaging, accurate blog posts',
    backstory='Skilled writer who transforms research into compelling content',
    verbose=True
)

# Define tasks
research_task = Task(
    description='Research latest trends in AI agent frameworks for 2025',
    agent=researcher,
    expected_output='Detailed research report with key findings and sources'
)

write_task = Task(
    description='Write a 1000-word blog post based on the research findings',
    agent=writer,
    expected_output='Well-structured blog post with introduction, body, and conclusion'
)

# Create and run crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    verbose=True
)

result = crew.kickoff()
print(result)
```

**Expected outcome**: A research report and blog post created collaboratively

### Recipe 2: LangGraph Stateful Workflow (Intermediate)

**Use Case**: Build a customer support agent with memory

```bash
pip install langgraph langchain-openai
```

```python
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated
from operator import add

# Define state
class AgentState(TypedDict):
    messages: Annotated[list, add]
    user_info: dict
    context: str

# Initialize LLM
llm = ChatOpenAI(model="gpt-4")

# Define agent functions
def classify_query(state):
    """Classify the user query type"""
    messages = state['messages']
    last_message = messages[-1]
    
    # Simple classification logic
    if "technical" in last_message.lower():
        return {"context": "technical_support"}
    elif "billing" in last_message.lower():
        return {"context": "billing_support"}
    else:
        return {"context": "general_support"}

def handle_technical(state):
    """Handle technical support queries"""
    response = llm.invoke([
        {"role": "system", "content": "You are a technical support agent. Help with technical issues."},
        {"role": "user", "content": state['messages'][-1]}
    ])
    return {"messages": [response.content]}

def handle_billing(state):
    """Handle billing queries"""
    response = llm.invoke([
        {"role": "system", "content": "You are a billing support agent. Help with account and payment issues."},
        {"role": "user", "content": state['messages'][-1]}
    ])
    return {"messages": [response.content]}

# Build workflow graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("classify", classify_query)
workflow.add_node("technical", handle_technical)
workflow.add_node("billing", handle_billing)

# Define routing logic
def route_query(state):
    if state['context'] == "technical_support":
        return "technical"
    elif state['context'] == "billing_support":
        return "billing"
    else:
        return "technical"  # default

# Add edges
workflow.set_entry_point("classify")
workflow.add_conditional_edges("classify", route_query)
workflow.add_edge("technical", END)
workflow.add_edge("billing", END)

# Compile and run
app = workflow.compile()

# Test the workflow
result = app.invoke({
    "messages": ["I'm having technical issues with my API integration"],
    "user_info": {"id": "user123"},
    "context": ""
})

print(result['messages'][-1])
```

**Expected outcome**: Context-aware responses routed to appropriate specialists

### Recipe 3: MCP-Powered Agent (Advanced)

**Use Case**: Build an agent with external data access via MCP

```bash
pip install mcp openai
```

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import openai
import asyncio

class MCPAgent:
    def __init__(self, openai_api_key):
        self.client = openai.OpenAI(api_key=openai_api_key)
        self.mcp_session = None
    
    async def connect_mcp_server(self, server_command, server_args):
        """Connect to MCP server"""
        server_params = StdioServerParameters(
            command=server_command,
            args=server_args
        )
        
        self.read, self.write = await stdio_client(server_params).__aenter__()
        self.mcp_session = await ClientSession(self.read, self.write).__aenter__()
        
        # List available tools
        tools = await self.mcp_session.list_tools()
        print(f"Available MCP tools: {[tool.name for tool in tools.tools]}")
        return tools.tools
    
    async def use_mcp_tool(self, tool_name, arguments):
        """Execute MCP tool"""
        if not self.mcp_session:
            raise Exception("MCP session not connected")
        
        result = await self.mcp_session.call_tool(tool_name, arguments)
        return result.content[0].text if result.content else "No result"
    
    def chat_with_tools(self, user_message, available_tools):
        """Chat with tool calling capability"""
        # Prepare tool definitions for OpenAI
        tool_definitions = []
        for tool in available_tools:
            tool_definitions.append({
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.inputSchema
                }
            })
        
        # Call OpenAI with tools
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant with access to external tools."},
                {"role": "user", "content": user_message}
            ],
            tools=tool_definitions,
            tool_choice="auto"
        )
        
        return response.choices[0].message

# Example usage
async def main():
    agent = MCPAgent("your-openai-api-key")
    
    # Connect to GitHub MCP server
    tools = await agent.connect_mcp_server(
        "npx", 
        ["-y", "@modelcontextprotocol/server-github"]
    )
    
    # Chat with the agent
    response = agent.chat_with_tools(
        "What are the recent issues in the microsoft/semantic-kernel repository?",
        tools
    )
    
    # Handle tool calls
    if response.tool_calls:
        for tool_call in response.tool_calls:
            tool_result = await agent.use_mcp_tool(
                tool_call.function.name,
                eval(tool_call.function.arguments)
            )
            print(f"Tool result: {tool_result}")
    else:
        print(f"Response: {response.content}")

# Run the async function
# asyncio.run(main())
```

**Expected outcome**: Agent with live access to GitHub data via MCP

## 🛀️ Framework Selection Matrix

| Need | Framework | Complexity | Setup Time | Best For |
|------|-----------|------------|------------|----------|
| **Quick Prototype** | AutoGPT, OpenAI Swarm | Low | 15 min | MVP, demos |
| **Team Collaboration** | CrewAI, AutoGen | Medium | 1 hour | Multi-step workflows |
| **Production App** | LangChain, Semantic Kernel | High | 1 day | Enterprise systems |
| **Research & Reports** | GPT Researcher | Low | 30 min | Content creation |
| **Code & Automation** | Open Interpreter | Medium | 45 min | DevOps, scripting |
| **Data Applications** | LlamaIndex, DB-GPT | High | 2-3 hours | Analytics, BI |
| **MCP Integration** | OpenAI Agents SDK | Medium | 1-2 hours | Interoperable systems |

## 🔧 Development Environment Setup

### Essential Tools

```bash
# Python environment
python -m venv agent_env
source agent_env/bin/activate  # On Windows: agent_env\Scripts\activate

# Core dependencies
pip install openai anthropic python-dotenv

# Popular frameworks (choose based on your needs)
pip install crewai          # Multi-agent teams
pip install langchain       # Comprehensive framework
pip install autogen-agentchat # Microsoft AutoGen
pip install phidata         # Type-safe agents
```

### Environment Variables

```bash
# Create .env file
echo "OPENAI_API_KEY=your_key_here" >> .env
echo "ANTHROPIC_API_KEY=your_key_here" >> .env
echo "SERPER_API_KEY=your_key_here" >> .env  # For web search
```

### IDE Setup

**VS Code Extensions**:
- Python
- Pylance  
- GitHub Copilot (for AI-assisted development)
- REST Client (for API testing)

**Jupyter Notebook**:
```bash
pip install jupyter
jupyter notebook
```

## 🐛 Common Issues & Solutions

### API Rate Limits
**Problem**: "Rate limit exceeded" errors

**Solution**:
```python
import time
from functools import wraps

def rate_limit(calls_per_minute=60):
    def decorator(func):
        last_called = [0.0]
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            left_to_wait = 60.0 / calls_per_minute - elapsed
            if left_to_wait > 0:
                time.sleep(left_to_wait)
            ret = func(*args, **kwargs)
            last_called[0] = time.time()
            return ret
        return wrapper
    return decorator

@rate_limit(calls_per_minute=30)
def call_llm_api(prompt):
    # Your API call here
    pass
```

### Memory Management
**Problem**: Agents running out of context or memory

**Solution**: Implement conversation summarization
```python
def summarize_conversation(messages, max_tokens=1000):
    if len(messages) < 10:  # Only summarize long conversations
        return messages
    
    # Keep system message and recent messages
    system_msg = messages[0]
    recent_msgs = messages[-5:]
    middle_msgs = messages[1:-5]
    
    # Summarize middle messages
    summary = llm.invoke(f"Summarize this conversation: {middle_msgs}")
    
    return [system_msg, {"role": "system", "content": f"Previous context: {summary}"}] + recent_msgs
```

### Debugging Agent Behavior
**Problem**: Agent making unexpected decisions

**Solution**: Add detailed logging
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DebuggableAgent:
    def __init__(self):
        self.decision_log = []
    
    def make_decision(self, context):
        reasoning = self.get_reasoning(context)
        decision = self.choose_action(reasoning)
        
        # Log the decision process
        log_entry = {
            "timestamp": time.time(),
            "context": context,
            "reasoning": reasoning,
            "decision": decision
        }
        self.decision_log.append(log_entry)
        logger.info(f"Decision: {decision}, Reasoning: {reasoning}")
        
        return decision
```

## 📈 Next Steps

### 1. Choose Your Framework
Based on the decision tree above, select the framework that best fits your needs.

### 2. Build Your First Agent
Start with one of the quick start recipes and modify it for your use case.

### 3. Add Evaluation
Implement basic evaluation metrics to track your agent's performance:

```python
def evaluate_agent(agent, test_cases):
    results = []
    for test in test_cases:
        result = agent.run(test['input'])
        success = check_success(result, test['expected'])
        results.append({
            'input': test['input'],
            'output': result,
            'success': success
        })
    
    success_rate = sum(r['success'] for r in results) / len(results)
    return success_rate, results
```

### 4. Scale to Production
- Add error handling and retry logic
- Implement monitoring and logging
- Set up CI/CD pipelines
- Consider cost optimization

### 5. Join the Community
- Follow framework-specific Discord/Slack channels
- Contribute to open source projects
- Share your experiences and learnings

---

**Remember**: Start simple, iterate quickly, and don't try to build the perfect agent on day one. The AI agent ecosystem is rapidly evolving, so focus on learning and experimenting!

*Need help? Check out our [evaluation guide](../catalog/evaluation.md) for measuring agent performance or explore [MCP integration](../catalog/mcp.md) for advanced interoperability.*