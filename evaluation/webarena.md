# WebArena: Getting Started Guide

Quick setup guide for evaluating web navigation agents using WebArena's realistic web tasks.

## 🎯 What is WebArena?

WebArena tests agents on realistic web navigation and interaction tasks across:
- **E-commerce** - Product search, shopping carts, checkout
- **Social Media** - Reddit-like posting and interaction
- **Collaborative Software** - GitLab repository management
- **Content Management** - CMS administration

**Website**: [webarena.dev](https://webarena.dev/)  
**Repository**: [web-arena-x/webarena](https://github.com/web-arena-x/webarena)

---

## 🚀 Quick Setup

### Prerequisites
- Python 3.9+
- Chrome/Chromium browser
- 8GB+ RAM (for running websites locally)
- Docker (for environment isolation)

### Installation
```bash
# Clone repository
git clone https://github.com/web-arena-x/webarena.git
cd webarena

# Install Python dependencies
pip install -r requirements.txt

# Install browser dependencies
playwright install chromium
```

### Environment Setup
```bash
# Set up local websites (takes 10-15 minutes)
docker-compose up -d

# Wait for services to be ready
./scripts/wait_for_services.sh

# Configure agent settings
cp config/agent_config.example.json config/my_agent.json
```

---

## 🎯 Running Evaluations

### Smoke Test (5 tasks)
```bash
# Quick test with simple tasks
python run_evaluation.py \
  --agent_config config/my_agent.json \
  --task_ids 1,5,10,15,20 \
  --result_dir results/smoke_test

# Check results
python analyze_results.py results/smoke_test
```

### Full Evaluation (812 tasks)
```bash
# Complete benchmark (takes 4-8 hours)
python run_evaluation.py \
  --agent_config config/my_agent.json \
  --task_file config/test.raw.json \
  --result_dir results/full_eval_$(date +%Y%m%d) \
  --max_steps 15
```

---

## 🔧 Agent Integration

### Basic Agent Implementation
```python
# agents/web_agent.py
from playwright.sync_api import sync_playwright
import json

class WebArenaAgent:
    def __init__(self, config):
        self.config = config
        self.browser = None
        self.page = None
        
    def setup(self):
        """Initialize browser and page"""
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
            headless=True,
            args=['--no-sandbox']
        )
        self.page = self.browser.new_page()
        
    def act(self, task, observation):
        """Take action based on current page state"""
        # Get current page content
        page_content = self.page.content()
        
        # Your agent logic here
        # Example: use LLM to decide next action
        action = self.decide_action(task, observation, page_content)
        
        return self.execute_action(action)
    
    def decide_action(self, task, observation, page_content):
        """Use LLM to decide next action"""
        prompt = f"""
        Task: {task}
        Current page: {page_content[:2000]}...
        
        What action should I take next? Reply with one of:
        - click: <element_selector>
        - type: <text_to_type>
        - navigate: <url>
        - scroll: <direction>
        - wait: <seconds>
        """
        
        # Your LLM call here
        response = self.llm.generate(prompt)
        return self.parse_action(response)
    
    def execute_action(self, action):
        """Execute the decided action"""
        action_type = action.get('type')
        
        if action_type == 'click':
            self.page.click(action['selector'])
        elif action_type == 'type':
            self.page.fill(action['selector'], action['text'])
        elif action_type == 'navigate':
            self.page.goto(action['url'])
        elif action_type == 'scroll':
            self.page.evaluate(f"window.scrollBy(0, {action['distance']})")
        elif action_type == 'wait':
            self.page.wait_for_timeout(action['duration'] * 1000)
        
        return self.get_observation()
    
    def get_observation(self):
        """Get current page state for next decision"""
        return {
            'url': self.page.url,
            'title': self.page.title(),
            'content': self.page.content()[:5000],  # Truncate for context
            'screenshot': self.page.screenshot()  # Optional: for vision models
        }
    
    def cleanup(self):
        """Clean up resources"""
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
```

---

## 📊 Understanding Results

### Success Metrics
- **Task Completion**: Binary success/failure
- **Step Efficiency**: Fewer steps = better score
- **Error Recovery**: Ability to handle unexpected states
- **Goal Achievement**: Meeting task objectives

### Common Failure Modes
1. **Element Not Found**: Selector issues or page changes
2. **Timeout**: Tasks taking too long
3. **Navigation Errors**: Getting lost or stuck
4. **Form Submission**: Missing required fields

### Debugging Tips
```bash
# Run with screenshots for debugging
python run_evaluation.py \
  --agent_config config/my_agent.json \
  --task_ids 1 \
  --save_screenshots \
  --result_dir debug

# Enable detailed logging
DEBUG=1 python run_evaluation.py ...
```

---

## 🔄 Optimization Strategies

### 1. **Prompt Engineering**
```python
# Better system message
system_message = """
You are a web navigation expert. For each task:
1. Analyze the current page content
2. Identify the most direct path to complete the objective
3. Take one clear action at a time
4. If stuck, try alternative approaches
5. Always verify your actions succeeded before proceeding

Available actions: click, type, navigate, scroll, wait
"""
```

### 2. **Multi-Modal Approach**
```python
# Use both HTML and screenshots
def enhanced_observation(page):
    return {
        'html': page.content()[:3000],
        'screenshot': page.screenshot(),
        'url': page.url,
        'clickable_elements': page.query_selector_all('[onclick], a, button, input')
    }
```

### 3. **Error Recovery**
```python
# Implement retry logic
def robust_action(self, action, max_retries=3):
    for attempt in range(max_retries):
        try:
            result = self.execute_action(action)
            if self.verify_action_success(action, result):
                return result
        except Exception as e:
            if attempt == max_retries - 1:
                return {'error': str(e)}
            time.sleep(1)  # Wait before retry
    return {'error': 'Max retries exceeded'}
```

---

## 🏆 Performance Targets

### Baseline Scores to Beat
- **GPT-4 + Advanced Prompting**: 35.8% overall
- **Claude-3.5-Sonnet**: 28.3% overall
- **GPT-3.5-Turbo**: 15.2% overall

### Environment-Specific Targets
| Environment | Good Score | Great Score | Notes |
|-------------|------------|-------------|-------|
| E-commerce | >40% | >60% | Focus on search and checkout flows |
| Social Media | >30% | >50% | Text generation and interaction |
| GitLab | >25% | >45% | Complex multi-step workflows |
| CMS | >35% | >55% | Content creation and management |

---

## 🚀 Next Steps

1. **Run smoke test** to validate setup
2. **Analyze failure modes** from initial results
3. **Iterate on agent design** based on weaknesses
4. **Compare against baselines** using standard metrics
5. **Submit results** to community leaderboard (optional)

---

## 🔗 Related Resources

- **[Agent Evaluation Overview](../catalog/evaluation.md)** - Complete benchmark comparison
- **[SWE-bench Guide](swebench.md)** - For coding-focused evaluation
- **[τ-Bench Guide](taubench.md)** - For real-world reliability testing

---

*Last updated: January 2025 | Based on WebArena v1.0 and latest evaluation protocols*