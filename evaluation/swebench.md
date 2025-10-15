# SWE-bench: Getting Started Guide

Quick setup guide for evaluating coding agents using SWE-bench's real GitHub issues and repositories.

## 🎯 What is SWE-bench?

SWE-bench evaluates agents on **real software engineering tasks** from GitHub:
- **2,294 GitHub issues** from popular Python repositories
- **Real codebases** including Django, Flask, Matplotlib, Scikit-learn
- **Automated verification** against existing test suites
- **Diverse problem types** - bugs, features, documentation

**Website**: [swebench.com](https://www.swebench.com/)  
**Repository**: [princeton-nlp/SWE-bench](https://github.com/princeton-nlp/SWE-bench)

---

## 🚀 Quick Setup

### Prerequisites
- Python 3.9+
- Git
- Docker (recommended for isolation)
- 16GB+ RAM (for large repositories)
- OpenAI API key or local model setup

### Installation
```bash
# Clone SWE-bench
git clone https://github.com/princeton-nlp/SWE-bench.git
cd SWE-bench

# Create virtual environment
python -m venv swe_env
source swe_env/bin/activate  # On Windows: swe_env\Scripts\activate

# Install dependencies
pip install -e .

# Download evaluation data
cd data
wget https://github.com/princeton-nlp/SWE-bench/releases/download/v1.0/swe-bench.json
```

### Configuration
```python
# config/my_agent.json
{
  "model": "gpt-4",
  "temperature": 0.1,
  "max_tokens": 4096,
  "timeout_per_task": 1800,  # 30 minutes
  "max_iterations": 10,
  "enable_tests": true,
  "sandbox_mode": true
}
```

---

## 🎯 Running Your First Evaluation

### Smoke Test (5 issues)
```bash
# Test with easy issues first
python evaluate.py \
  --agent my_agent \
  --dataset_name swe-bench-lite \
  --instance_ids django__django-12345,flask__flask-1234 \
  --output_dir results/smoke_test

# View results
python analyze_results.py results/smoke_test
```

### Full Evaluation Subset
```bash
# Run on SWE-bench Lite (300 verified instances)
python evaluate.py \
  --agent my_agent \
  --dataset_name swe-bench-lite \
  --output_dir results/lite_eval_$(date +%Y%m%d) \
  --max_workers 4
```

---

## 🔧 Agent Implementation

### Basic SWE-bench Agent
```python
# agents/swe_agent.py
import os
import subprocess
from typing import Dict, List, Optional

class SWEAgent:
    def __init__(self, config: Dict):
        self.config = config
        self.current_repo = None
        self.work_dir = None
        
    def solve_issue(self, instance: Dict) -> Dict:
        """
        Solve a GitHub issue from SWE-bench
        
        Args:
            instance: Contains repo, issue description, test files, etc.
        
        Returns:
            Dict with solution patch and metadata
        """
        repo = instance['repo']
        issue_text = instance['problem_statement']
        
        # Step 1: Set up repository
        self.setup_repository(repo, instance['version'])
        
        # Step 2: Understand the issue
        understanding = self.analyze_issue(issue_text)
        
        # Step 3: Locate relevant files
        relevant_files = self.find_relevant_files(understanding)
        
        # Step 4: Generate solution
        solution = self.generate_solution(understanding, relevant_files)
        
        # Step 5: Test solution
        test_results = self.test_solution(instance.get('test_patch', ''))
        
        return {
            'patch': solution,
            'test_results': test_results,
            'files_modified': relevant_files,
            'reasoning': understanding
        }
    
    def setup_repository(self, repo: str, version: str):
        """Clone and checkout specific version"""
        self.work_dir = f"./repos/{repo.replace('/', '_')}_{version}"
        
        if not os.path.exists(self.work_dir):
            subprocess.run([
                'git', 'clone', f'https://github.com/{repo}', self.work_dir
            ])
        
        os.chdir(self.work_dir)
        subprocess.run(['git', 'checkout', version])
        
        # Install dependencies
        if os.path.exists('requirements.txt'):
            subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
        elif os.path.exists('setup.py'):
            subprocess.run(['pip', 'install', '-e', '.'])
    
    def analyze_issue(self, issue_text: str) -> Dict:
        """Use LLM to understand the issue"""
        prompt = f"""
        Analyze this GitHub issue and provide:
        1. Issue type (bug/feature/documentation)
        2. Key files likely involved
        3. Potential solution approach
        4. Test strategy
        
        Issue:
        {issue_text}
        """
        
        response = self.llm_call(prompt)
        return self.parse_analysis(response)
    
    def find_relevant_files(self, understanding: Dict) -> List[str]:
        """Find files to examine/modify"""
        suggested_files = understanding.get('key_files', [])
        
        # Search codebase for relevant patterns
        search_terms = understanding.get('search_terms', [])
        found_files = []
        
        for term in search_terms:
            result = subprocess.run([
                'grep', '-r', '-l', term, '.', '--include=*.py'
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                found_files.extend(result.stdout.strip().split('\n'))
        
        # Combine suggested and found files
        all_files = list(set(suggested_files + found_files))
        return all_files[:10]  # Limit scope
    
    def generate_solution(self, understanding: Dict, files: List[str]) -> str:
        """Generate code patch"""
        file_contents = {}
        for file_path in files:
            try:
                with open(file_path, 'r') as f:
                    file_contents[file_path] = f.read()
            except:
                continue
        
        prompt = f"""
        Based on this issue analysis:
        {understanding}
        
        And these relevant files:
        {file_contents}
        
        Generate a minimal patch to fix the issue.
        Provide the patch in unified diff format.
        """
        
        patch = self.llm_call(prompt)
        return patch
    
    def test_solution(self, test_patch: str) -> Dict:
        """Run tests to validate solution"""
        if test_patch:
            # Apply test patch first
            with open('test.patch', 'w') as f:
                f.write(test_patch)
            subprocess.run(['git', 'apply', 'test.patch'])
        
        # Run tests
        test_result = subprocess.run([
            'python', '-m', 'pytest', '--tb=short'
        ], capture_output=True, text=True)
        
        return {
            'passed': test_result.returncode == 0,
            'output': test_result.stdout,
            'errors': test_result.stderr
        }
    
    def llm_call(self, prompt: str) -> str:
        """Make LLM API call - implement based on your setup"""
        # Your LLM integration here
        pass
```

---

## 📊 Performance Analysis

### Current Leaderboard (Approximate)
| Agent | Solve Rate | Notes |
|-------|------------|-------|
| **Devin** | 13.86% | Proprietary, full automation |
| **SWE-agent** | 12.29% | Specialized for SWE tasks |
| **CodeActAgent** | 8.96% | Action-based code generation |
| **AutoCodeRover** | 7.94% | Automated program repair |
| **GPT-4 Baseline** | 1.96% | Direct prompting without tools |

### Difficulty Breakdown
| Repository | Easy (>15%) | Medium (5-15%) | Hard (<5%) | Notes |
|------------|-------------|----------------|------------|-------|
| **Django** | 18% | 12% | 3% | Large codebase, complex ORM |
| **Flask** | 22% | 15% | 8% | Smaller, more focused |
| **Matplotlib** | 15% | 10% | 4% | Visualization complexity |
| **Scikit-learn** | 20% | 13% | 6% | ML algorithms and APIs |

---

## ⚡ Optimization Tips

### 1. **Repository Understanding**
```bash
# Analyze codebase structure first
find . -name "*.py" | head -20
tree -d -L 3
grep -r "class.*Exception" --include="*.py" . | head -10
```

### 2. **Test-Driven Development**
```python
# Always run existing tests first
def validate_baseline(self):
    """Ensure we don't break existing functionality"""
    result = subprocess.run(['python', '-m', 'pytest'], capture_output=True)
    if result.returncode != 0:
        raise Exception("Baseline tests failing - repository setup issue")
```

### 3. **Incremental Changes**
```python
# Make minimal changes and test frequently
def iterative_solution(self, issue_analysis):
    changes = self.plan_incremental_changes(issue_analysis)
    
    for change in changes:
        self.apply_change(change)
        test_result = self.run_tests()
        
        if not test_result['passed']:
            self.revert_change(change)
            self.try_alternative_approach(change)
```

---

## 🔗 Additional Resources

- **Official Paper**: [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770)
- **Leaderboard**: [Official Results](https://www.swebench.com/)
- **Community**: [GitHub Discussions](https://github.com/princeton-nlp/SWE-bench/discussions)
- **Tools**: [SWE-agent Implementation](https://github.com/princeton-nlp/SWE-agent)

---

*This guide provides a foundation for SWE-bench evaluation. Success requires combining code understanding, testing, and iterative problem-solving approaches.*