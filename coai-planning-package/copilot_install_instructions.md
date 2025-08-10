# Copilot Instructions — Integrate Planning Module into COAI

## Objective
Integrate this planning module into `C:\ai_projects\coai`, keep the master plan read-only,
enable progress tracking via working copies, and wire up automation scripts and Git flow.

## Steps (execute one by one)
1. Ensure folders exist:
   - `C:\ai_projects\coai\planning\master`
   - `C:\ai_projects\coai\planning\versions`
   - `C:\ai_projects\coai\planning\progress\stage2`
   - `C:\ai_projects\coai\planning\progress\stage3`
   - `C:\ai_projects\coai\.coai\{logs,rules,schemas,tools}`
2. Copy files from this package into those locations (preserve structure).
3. Set master read-only:
   ```powershell
   attrib +R "C:\ai_projects\coai\planning\master\coai_plan.md"
   ```
4. Initialize Git (if needed), add and commit all new files.
5. Confirm the Stage working copies exist:
   - `stage2_plan_copy.md`, `stage3_plan_copy.md` (with checkboxes)
6. Run `.coai\tools\update_progress.py`, commit the dashboard changes.
7. Add one ad-hoc task to Stage II using `.coai\tools\add_task.py II 12 "Health check endpoint"` and commit.
8. Run `.coai\tools\validate_plans.py` and ensure it prints “Validation OK.”
9. Optionally install the pre-commit hook from `.githooks/README.md`.
10. Done — Planning module operational.
