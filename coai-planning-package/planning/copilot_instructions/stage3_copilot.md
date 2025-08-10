# Copilot Agent Instructions — Stage III (Pro/Enterprise)

## Objective
Implement Stage III tasks (16.x–24.x) from the COAI development plan.

## Rules
1. Work only on tasks in Stage III.
2. Follow numerical order and update `planning/progress/stage3/stage3_plan_copy.md`.
3. Use Python 3.10+, Next.js 14+, TailwindCSS, Flask.
4. Place backend code in `backend/`, frontend in `frontend/`.
5. Keep master plan read-only.

## Workflow
- Implement each feature fully before moving to the next.
- Test locally and ensure compatibility with previous stages.
- Mark `[x]` in `stage3_plan_copy.md`.
- Commit with `stage3: completed <task_number>`.
- Update dashboard using `.coai/tools/update_progress.py`.
- Validate with `.coai/tools/validate_plans.py`.
