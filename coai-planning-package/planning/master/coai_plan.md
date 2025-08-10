# COAI Development Plan — v2 (Hierarchical Numbering, No Checkboxes)

## Stage I — Minimal Working COAI Core (MVP) ✅ (Completed)
- 1.1 Set up directories: frontend, backend, .coai
- 1.2 Template setup and launch (Next.js + Flask)
- 1.3 Frontend-Backend integration (/api/chat)
- 1.4 Chat UI (send, loader, error, response)
- 1.5 Prompt preprocessor endpoint
- 1.6 Orchestrator layer
- 1.7 AI agent module (Copilot/OpenAI)
- 1.8 File access (read-only)
- 1.9 Basic tests & docs

## Stage II — Advanced Core (Optimized)
- 10.1 Multi-project management & migration
- 10.2 Project selection UI in frontend
- 10.3 Dynamic project configs/rules/plans loading in backend
- 10.4 Migration tool (single-project → multi-project)
- 10.5 Tests for project switching/migration integrity
- 11.1 Agent instructions & rules in `.coai\rules\`
- 11.2 Edit rules via UI (syntax highlighting)
- 11.3 Apply changes dynamically (no restart)
- 11.4 Per-agent and global rules support
- 11.5 Rules tests (load/apply/persist)
- 12.1 Action plan generation for larger tasks
- 12.2 Step progress tracking
- 12.3 UI progress filters (e.g., incomplete only)
- 12.4 Integration with plan copy/markers
- 12.5 Multi-step plan tests
- 13.1 Track API calls, tokens, costs
- 13.2 UI usage views (daily/weekly/monthly)
- 13.3 Budget limits in `.coai\usage\config.json`
- 13.4 UI alerts on thresholds
- 13.5 Usage & alerts tests
- 14.1 Error logs with context (project, agent, request)
- 14.2 UI filtering by date/project/type
- 14.3 Frequent issues analysis, suggestions
- 14.4 Export reports to CSV/JSON
- 14.5 Log/filters/export tests
- 15.1 Integration tests for multi-project
- 15.2 Performance/load tests
- 15.3 Security tests (file access, API endpoints)
- 15.4 CI automation

## Stage III — Pro/Enterprise
- 16.1 Project structure & code optimization module
- 16.2 Automatic junk cleanup
- 16.3 Session/mission management
- 16.4 User profile & preferences
- 16.5 Multi-user & team mode
- 16.6 External tool integrations
- 16.7 Advanced context management
- 16.8 Safety & rollback
- 16.9 Cloud storage (optional)
