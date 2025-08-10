# COAI Planning Module (Ready-to-Drop Package)

This package adds a **planning module** to your COAI project that is reusable for other projects, too.
It provides:
- `planning/` — human plans (master, versions, stage plans, working copies, dashboard)
- `.coai/` — rules, schemas, automation scripts, logs
- One-way plan flow, read-only master, checkbox tracking in working copies
- Git discipline and optional local pre-commit hook

## Quick Install (Windows, COAI root at `C:\ai_projects\coai`)

1) Extract this ZIP **into** `C:\ai_projects\coai` (it will create/merge `planning\` and `.coai\`).
2) Mark the master plan read-only:
   ```powershell
   attrib +R "C:\ai_projects\coai\planning\master\coai_plan.md"
   ```
3) Initialize Git (if needed) and make the first commit:
   ```powershell
   cd C:\ai_projects\coai
   if (-not (Test-Path ".git")) { git init }
   git add planning\ .coai\ -A
   git commit -m "Add COAI planning module (master, versions, progress, rules, tools)"
   ```
4) (Optional) Install the local pre-commit hook described in `.githooks/README.md`.

## Daily Usage

- Update **only** the working copies:
  - `planning/progress/stage2/stage2_plan_copy.md`
  - `planning/progress/stage3/stage3_plan_copy.md`
- Run `.coai/tools/update_progress.py` to refresh the dashboard.
- Add ad-hoc tasks with `.coai/tools/add_task.py`.
- Validate with `.coai/tools/validate_plans.py` (e.g., in CI).
- Commit after every status change.

## Files to Know
- `planning/master/coai_plan.md` — source-of-truth (read-only, no checkboxes)
- `planning/versions/coai_plan_v2.md` — snapshot
- `planning/progress/coai_progress.md` — dashboard (auto-updated)
- `planning/progress/stage2/*` and `planning/progress/stage3/*`
- `.coai/rules/*` — numbering, validation, budget
- `.coai/tools/*` — scripts (update_progress, validate_plans, add_task, bump_version)
- `.githooks/README.md` — optional pre-commit protection

## Compatibility
- English-only content in files for clean automation & collaboration.
- Works on Windows PowerShell; Python 3.10+ recommended.
