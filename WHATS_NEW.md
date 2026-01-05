# What’s New (last 7 days)

## LangChain
- Release langchain-core==1.2.6 (2026-01-02)
- Release langchain-xai==1.2.0 (2026-01-02)
- Commit 659eab2: release(core): 1.2.6 (#34586) (2026-01-02)
- Commit 458a186: chore(core): Update LangChainTracer to use Pydantic v2 methods (#34541) (2026-01-02)
- Commit 9da28ba: release(xai): 1.2.0 (#34555) (2025-12-31)
- Commit 5517ef3: docs(core): add docstrings to internal helper functions (#34525) (2025-12-31)
- Commit 2bbe421: docs(core): refresh `content.py` docstrings (#34546) (2025-12-31)
- Commit fcc02f7: chore(deps): Update outdated GitHub Actions versions (#34544) (2025-12-31)
- Commit 721bf15: fix(langchain): resolve race condition in `ShellSession.execute()` (#34535) (2025-12-30)
- Commit dcfd9c0: fix(infra): use `langchain_v1` for dev container deps (#34534) (2025-12-30)
- Commit e03d6b8: chore(deps): bump mypy to v1.19 and ruff to v1.14 (#34521) (2025-12-30)
- Commit ea25f5e: chore(text-splitters): bump dependency locks for python 3.14 (#34522) (2025-12-29)
- Commit 04c0c1b: chore(langchain-classic): bump markupsafe lock for python 3.14 (#34523) (2025-12-29)
- Commit c1f5d09: fix: typo: saved the world  'wether' -> 'whether' (#34524) (2025-12-29)
- Commit e81f00f: docs(standard-tests): remove autodoc comment (#34532) (2025-12-29)
- Commit 7ce68f2: fix(docs): correct Code of Conduct link in README (#34518) (2025-12-29)

## OpenDevin/OpenHands
- Release 1.1.0 (2025-12-30)
- Commit 6f86e58: feat: allow manual reinstallation for gitlab resolver (#12184) (2026-01-05)
- Commit 5bd8695: feat: Add configurable sandbox host_port and container_url_pattern for remote access (#12255) (2026-01-05)
- Commit 8c73c87: Add extra_hosts support to agent-server containers (#12236) (2026-01-03)
- Commit 40c25cd: fix: use Auth.Token for PyGithub authentication (#12248) (2026-01-03)
- Commit 2ebde25: fix: Handle LiteLLM v1.80+ 404 response for new users (#12250) (2026-01-02)
- Commit cdc4213: fix: replace deprecated get_matching_events with search_events (#12249) (2026-01-02)
- Commit 903c047: Replace deprecated PyPDF2 with pypdf (#12203) (2026-01-02)
- Commit ee2ad16: fix: update pythonjsonlogger.jsonlogger to pythonjsonlogger.json (#12247) (2026-01-02)
- Commit a96b47e: chore(deps): bump posthog-js from 1.312.0 to 1.313.0 in /frontend in the version-all group (#12241) (2026-01-02)
- Commit 5a08277: fix(backend): stabilize gitlab resolver in saas (#12231) (2026-01-02)
- Commit 1bae1fc: doc: correct Slack channel to #dev-ui-ux (#12239) (2026-01-02)
- Commit 15bc78f: Remove VSCode extension integration from OpenHands repo (#12234) (2026-01-01)
- Commit 437046f: chore(deps): bump the version-all group in /frontend with 2 updates (#12232) (2026-01-01)
- Commit f9b3164: fix: prevent nested buttons in tooltip button (#12177) (2025-12-31)
- Commit 96d073e: fix(frontend): add missing onClose prop to conversation panel modals (#12219) (2025-12-31)
- Commit f7d416a: refactor(frontend): remove HeroUI BaseModal and migrate MetricsModal (#12174) (2025-12-31)
- Commit b7d5f90: fix(frontend): Agent Tools & Metadata not available for V1 conversations  (#12180) (2025-12-31)
- Commit 2734a5a: fix(frontend): show stop action button for running or starting conversations (#12215) (2025-12-31)
- Commit 51868ff: chore(deps): bump @tanstack/react-query from 5.90.15 to 5.90.16 in /frontend in the version-all group (#12225) (2025-12-31)
- Commit 4c0f0a1: feat: Support Tau-Bench and BFCL evaluation benchmarks (#11953) (2025-12-31)
- Commit 82e0aa7: chore(deps): bump ncipollo/release-action from 1.16.0 to 1.20.0 (#11851) (2025-12-31)
- Commit 6f9c0aa: fix: display conversation title in delete confirmation modal (#11818) (2025-12-31)
- Commit 232dcf4: fix(ci): update PAT_TOKEN to ALLHANDS_BOT_GITHUB_PAT for enterprise preview (#12216) (2025-12-30)
- Commit ffdd953: fix(backend): invalid api key (#12217) (2025-12-30)
- Commit bfe8275: hotfix(test): add top-level mock for custom-toast-handlers in conversation-panel tests (#12220) (2025-12-30)
- Commit 06a97fc: Bump SDK packages to v1.7.3 (#12218) (2025-12-30)

## LlamaIndex
- Release v0.14.12 (2025-12-30)
- Commit 2a6f4dd: Release 0.14.12 (#20432) (2025-12-30)
- Commit 9090943: docs: improve Ollama embeddings README with comprehensive documentation (#20414) (2025-12-29)
- Commit f57903e: test(node_parser): add unit tests for Java CodeSplitter (#20423) (2025-12-29)
- Commit 152b8dd: fix: crash in log_vector_store_query_result when result.ids is None (#20427) (2025-12-29)

## CrewAI
- Commit 467ee29: Improve EventListener and TraceCollectionListener for improved event… (#4160) (2025-12-30)

## CAMEL
- Release v0.2.83a1 (2026-01-02)
- Commit 6a60fe6: Update README to remove project links (#3656) (2026-01-04)
- Commit e56fa93: chore: terminal toolkit venv setting using symlinks=True (#3655) (2026-01-02)
- Commit 39c083b: Update WeChat QR code via QR Code Updater (2026-01-02)

## Phidata
- Commit 26b9daa: fix: a typo in cookbook (#5875) (2026-01-02)
- Commit 1e0c32b: fix: broken link to evals/performance in README (#5854) (2025-12-29)

## E2B Sandbox
- Commit ca556d8: docs: remove inaccurate set timeout comment (#1059) (2026-01-02)
- Commit 7bc9eb5: Dependencies update (#1058) (2025-12-31)

## LangGraph
- Commit 0acd5de: fix: typo: saved the world "BaseMessge" to "BaseMessage"  (#6639) (2025-12-31)

## PydanticAI
- Commit c8df8a3: Update `thoughtSignature` for Vertex Gemini 3 compatibility (#3882) (2025-12-31)
- Commit 468b02b: Bump minimum version of `mistralai` (#3873) (2025-12-29)

## Cognee
- Commit b339529: Fix: Add top_k parameter support to MCP search tool (#1954) (2026-01-03)
- Commit 6a5ba70: docs: Add comprehensive docstrings and fix default top_k consistency (2026-01-03)
- Commit 7ee36f8: Fix: Add top_k parameter support to MCP search tool (2026-01-03)
- Commit 5b42b21: Enhance CONTRIBUTING.md with example setup instructions (2025-12-29)

