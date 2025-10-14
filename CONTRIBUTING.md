# Contributing to Awesome AI Agents

Thank you for your interest in contributing to the Awesome AI Agents repository! This document provides guidelines for contributing to maintain the high quality and consistency of our curated list.

## 📋 Contribution Guidelines

### What We're Looking For

We accept AI agent frameworks and projects that meet these criteria:

#### ✅ **Quality Standards**
- **Active Maintenance**: Recent commits (within 6-12 months)
- **Community Adoption**: 
  - 500+ GitHub stars OR
  - Backing from established organizations (OpenAI, Microsoft, Google, Meta, Anthropic, etc.)
- **Production Readiness**: Well-documented with clear examples
- **Unique Value**: Offers distinct capabilities or approaches

#### ✅ **Technical Requirements**
- **Open Source**: Must have accessible source code
- **Agent Focus**: Specifically designed for building AI agents (not just general LLM tools)
- **Framework/Library**: Provides reusable components for agent development
- **Documentation**: Clear README, setup instructions, and usage examples

### What We Don't Accept

#### ❌ **Exclusion Criteria**
- **Commercial-only solutions** without open-source components
- **Experimental repos** with minimal code or documentation
- **Duplicate frameworks** or simple forks without significant improvements
- **General LLM libraries** that don't focus specifically on agents
- **Personal projects** without community adoption
- **Abandoned projects** with no recent activity

## 🚀 How to Contribute

### 1. **Check Existing Entries**
Before submitting, ensure your framework isn't already listed or substantially similar to existing entries.

### 2. **Gather Required Information**
Collect the following details for your submission:

- **Framework Name**
- **GitHub Repository URL**
- **Current Star Count**
- **Brief Description** (2-3 lines maximum)
- **Official Documentation/Blog/Paper Link**
- **Relevant Tags** (see categories below)
- **Maintenance Status** (last commit date)

### 3. **Choose the Right Category**

#### 🏆 **Top-Tier** (50K+ stars)
For established frameworks with massive adoption

#### 🚀 **High-Impact** (20K-50K stars)
For well-known frameworks with strong communities

#### 💎 **Specialized & Emerging**
For innovative or niche frameworks, organized by subcategories:
- **Research & Optimization**
- **Enterprise & Production** 
- **Developer Tools & Infrastructure**
- **Evaluation & Monitoring**

### 4. **Format Your Submission**

Use this exact format for the main table:

```markdown
| Framework Name | [github.com/owner/repo](https://github.com/owner/repo) | XXK | Brief description focusing on key capabilities and unique features | [docs-link.com](https://docs-link.com) | Tag1, Tag2, Tag3 |
```

**Example:**
```markdown
| CrewAI | [github.com/crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 35K | Cutting-edge framework for orchestrating role-playing, autonomous AI agents with seamless collaboration | [crewai.com](https://crewai.com) | Multi-Agent, Role-Playing, Orchestration |
```

### 5. **Select Appropriate Tags**

Choose 2-4 relevant tags from these categories:

#### **Core Functionality**
- `Framework`, `Autonomous Agent`, `Multi-Agent`, `Tool-Using Agent`

#### **Application Domain**
- `RAG Agent`, `Coding Agent`, `Research Agent`, `Planning Agent`

#### **Architecture**
- `Role-Playing`, `Orchestration`, `Conversation Framework`, `Graph Workflow`

#### **Target Audience**
- `Enterprise Framework`, `Lightweight Framework`, `Research Framework`

#### **Technical Features**
- `Type Safety`, `Structured Output`, `Local Execution`, `Cloud Infrastructure`

#### **Organization**
- `Microsoft`, `OpenAI`, `Google`, `Meta`, `Stanford Research`, etc.

## 📝 Pull Request Process

### Step-by-Step Instructions

1. **Fork the Repository**
   ```bash
   git clone https://github.com/your-username/awesome-ai-agents.git
   cd awesome-ai-agents
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b add-framework-name
   ```

3. **Make Your Changes**
   - Add your framework to the appropriate section
   - Update the repository statistics if needed
   - Ensure consistent formatting

4. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add [Framework Name] to [Category] section"
   ```

5. **Push and Create Pull Request**
   ```bash
   git push origin add-framework-name
   ```

### Pull Request Template

Use this template for your PR description:

```markdown
## Adding [Framework Name]

### Framework Details
- **Repository**: [GitHub URL]
- **Stars**: [Current count]
- **Last Commit**: [Date]
- **Category**: [Top-tier/High-impact/Specialized]

### Why This Framework Should Be Included
- [ ] Meets star count or organizational backing criteria
- [ ] Active maintenance (commits in last 6 months)  
- [ ] Unique capabilities or approach
- [ ] Production-ready with good documentation
- [ ] Focuses specifically on AI agents

### Verification Checklist
- [ ] Checked for duplicates
- [ ] Follows formatting guidelines
- [ ] Appropriate tags selected
- [ ] Links are working
- [ ] Description is concise and accurate
```

## ✅ Review Process

### What Reviewers Check

1. **Quality Verification**
   - Repository activity and maintenance
   - Community adoption metrics
   - Documentation quality
   - Unique value proposition

2. **Format Compliance**
   - Consistent markdown formatting
   - Proper link formatting
   - Appropriate categorization
   - Tag accuracy

3. **Content Standards**
   - Description clarity and accuracy
   - No marketing language or excessive claims
   - Appropriate technical level
   - Factual information

### Timeline

- **Initial Review**: Within 7 days
- **Feedback**: Provided if changes needed
- **Final Approval**: After all criteria met

## 🔄 Updating Existing Entries

### When to Update
- Star count changes significantly (>5K difference)
- Major version releases or feature additions
- Repository ownership changes
- Documentation updates

### How to Update
1. Follow the same PR process
2. Clearly indicate what's being updated
3. Provide reasoning for changes

## 🤝 Community Guidelines

### Code of Conduct
- Be respectful and constructive
- Focus on technical merits
- Avoid promotional language
- Help maintain quality standards

### Best Practices
- **Research thoroughly** before submitting
- **Test links** to ensure they work
- **Be patient** with the review process
- **Engage constructively** with feedback

## 📞 Getting Help

### Questions or Issues?
- **General Questions**: Open a GitHub Discussion
- **Bug Reports**: Create an Issue
- **Framework Suggestions**: Use the Issue template
- **Process Questions**: Comment on existing PRs for examples

### Resources
- **Awesome Lists Guidelines**: [awesome.re](https://awesome.re)
- **Markdown Guide**: [GitHub Markdown Documentation](https://docs.github.com/en/get-started/writing-on-github)
- **Git Workflow**: [GitHub Flow](https://guides.github.com/introduction/flow/)

---

**Thank you for helping us maintain the quality and usefulness of this curated list! 🙏**