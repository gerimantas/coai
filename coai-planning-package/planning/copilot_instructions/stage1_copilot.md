# Copilot Agent Instructions — Stage I (Minimal Working COAI Core)

## Objective
Implement Stage I tasks (1.x) from the COAI development plan.

## Rules
1. Work only on tasks in Stage I.
2. Follow numerical task order.
3. Use Python 3.10+, Next.js 14+, TailwindCSS, Flask.
4. Place backend code in `backend/`, frontend code in `frontend/`.
5. Keep `planning/master/coai_plan.md` read-only.

## Workflow
- Read task from `planning/master/coai_plan.md`.
- Implement feature in the correct folder.
- Test locally.
- Mark `[x]` in `planning/progress/stage1/stage1_plan_copy.md`.
- Commit with `stage1: completed <task_number>`.
- Update dashboard using `.coai/tools/update_progress.py`.
- Validate with `.coai/tools/validate_plans.py`.
