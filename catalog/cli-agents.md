# 💻 CLI & Terminal Agents

Developer-focused agents that operate in the shell to automate workflows, generate code, and manage systems.

## Why it matters
- Integrates naturally into developer workflows (CI/CD, DevOps, data)
- Works in restricted environments without GUIs
- Enables reproducible automations with low overhead

---

## Key Projects

| Name | Link | Type | Highlights |
|------|------|------|------------|
| Qodo Command | https://www.qodo.ai/command | CLI | Multi-step terminal workflows, agent memory |
| Goose CLI | https://github.com/goose-cli/goose | CLI | Local LLM-first terminal assistant |
| Amazon Q CLI | https://aws.amazon.com/q/developer/ | CLI | AWS-native dev & ops automation |
| Continue | https://github.com/continuedev/continue | VS Code | In-IDE agent assistant with tasks |
| Open Interpreter | https://github.com/KillianLucas/open-interpreter | CLI/Local | Natural language → code execution locally |

Note: Include additional OSS/paid options via PRs.

---

## Patterns
- Command planner → executor → verifier loop
- Idempotent scripts and dry-runs for safety
- Secrets handling: env vars, vaults
- Telemetry: command logs, exit codes, diffs

---

## Security & Governance
- Principle of least privilege (scoped creds, roles)
- Read-only defaults; explicit elevation gates
- Audit trails: full command history, redaction

---

## Examples to Add (Roadmap)
- Infra provisioning (Terraform plan/apply with review)
- Release automation (changelogs, tagging, publishing)
- Data pipelines (extract/transform/load with checkpoints)

Contributions welcome: add more CLI agents, patterns, and real-world recipes.
