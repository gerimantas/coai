# Copilot Agent Instructions — Stage II (Advanced Core)

## Objective
Implement Stage II tasks (10.x–15.x) from the COAI development plan.

## Rules
1. Work only on tasks in Stage II.
2. Follow task order and update `planning/progress/stage2/stage2_plan_copy.md`.
3. Use Python 3.10+, Next.js 14+, TailwindCSS, Flask.
4. Place backend code in `backend/`, frontend in `frontend/`.
5. Keep master plan read-only.

## Workflow
- For each task:
  1. Implement according to `planning/master/coai_plan.md`.
  2. Run tests relevant to the change.
  3. Mark `[x]` in `stage2_plan_copy.md`.
  4. Commit with `stage2: completed <task_number>`.
- After batch of tasks: update dashboard with `.coai/tools/update_progress.py`.
- Validate with `.coai/tools/validate_plans.py` before pushing.
