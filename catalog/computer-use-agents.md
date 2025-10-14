# 🖥️ Computer Use Agents (Desktop Automation)

Agents that can control desktop apps and the web browser to complete tasks end-to-end. This is the fastest-evolving agent category (2024–2025).

> Structured dataset: See [data/computer_use.csv](../data/computer_use.csv) for modalities, scope, sandboxing, and update dates.

## Why it matters
- Enables real-world task completion beyond APIs (GUI automation, file ops, multi-app workflows)
- Unlocks enterprise workflows where APIs are unavailable or insufficient
- Bridges research prototypes and practical automation at scale

## Key Capabilities
- GUI control: mouse/keyboard, window focus, app switching
- Vision grounding: on-screen element detection, OCR, layout understanding
- Safety: constrained execution, audit trails, human-in-the-loop
- Recovery: error detection, retries, fallback strategies

---

## Flagship Platforms

### Claude Computer Use (Anthropic)
- Overview: Anthropic’s platform feature for secure, supervised desktop/browser control
- Strengths: strong vision + reasoning, robust guardrails, enterprise focus
- Learn more: claude.com, Anthropic news posts, community tutorials

### OpenAI Operator / Computer-Using Agent (OpenAI)
- Overview: OpenAI’s computer-use agent for web + desktop automation (2025)
- Strengths: deep tool-use integration, ecosystem momentum, API ergonomics
- Learn more: OpenAI product blog, operator announcements

---

## Open-Source Frameworks and Tools

| Name | GitHub | Stars (approx) | Description | Notes |
|------|--------|----------------|-------------|-------|
| Nanobrowser | https://github.com/nanobrowser/nanobrowser | 7.1k | Browser agent for navigating and acting on the web | Vision + DOM strategies |
| UI-TARS | https://github.com/Sanster/UI-TARS | 6.5k | General GUI agent for desktop automation | Multimodal control |
| Skyvern | https://github.com/Skyvern-AI/skyvern | 4k | Autonomous web agent with vision and HTML extraction | Strong web focus |
| OpenManus | https://github.com/openmanus/openmanus | 600+ | Open-source alternative to Manus/Operator-style control | Early but promising |
| Cradle | https://github.com/andyz245/Cradle | 1k | General computer control via LLM planning | Research-oriented |

Note: Star counts should be periodically refreshed.

---

## Evaluation & Research
- Windows Agent Arena (2024): large-scale evaluation of multimodal OS agents
- The Dawn of GUI Agent (Claude Computer Use study, 2024)
- Cradle: Empowering Foundation Agents Towards General Computer Control (2024)

Benchmark themes:
- Task success under UI changes
- Robustness to visual ambiguity
- Error recovery and retries
- Latency vs. accuracy trade-offs

---

## Security & Governance
- Principle of least privilege: minimize OS and app permissions
- Sandboxing: browser profiles, VM/containers, file access controls
- Human-in-the-loop: escalation, approvals, halting conditions
- Logging & replay: full session recordings for auditability

---

## Quickstart Patterns

### Pattern 1: Browser-first Automation
- Use a browser automation agent (e.g., Nanobrowser / Skyvern)
- Add retrieval for site schemas/templates
- Chain with a planner + evaluator loop for reliability

### Pattern 2: Desktop Workflows with Vision
- Use a GUI agent (e.g., UI-TARS / OpenManus)
- Define high-level tasks with checkpoints and visual assertions
- Add rollback and retry policies

---

## Roadmap for this Section
- Add hands-on recipes (browser purchase flow, spreadsheet ops)
- Add video demos and reproducible notebooks
- Track new releases from Anthropic/OpenAI; surface best practices

---

Contributions welcome: PRs with new frameworks, evaluations, or tutorials are encouraged. Please include links, a short description, security notes, and a minimal demo if possible.
