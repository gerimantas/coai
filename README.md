# COAI Project

This project implements the COAI Stage I (MVP) plan. It includes a frontend (UI), backend (API), and project management structure.

## Structure
- `frontend/` – UI code (React/Next.js)
- `backend/` – Backend API (Python/Flask)
- `.coai/` – Project metadata, plans, and logs

## Launch Instructions

1. Install dependencies:
	- Frontend: `cd frontend && npm install`
	- Backend: `cd backend && pip install -r requirements.txt`

2. Start servers:
	- Frontend: `cd frontend && npm run dev` (http://localhost:3000)
	- Backend: `cd backend && python main.py` (http://localhost:5000)

3. Usage:
	- Open the UI in your browser at http://localhost:3000
	- Use the chat page to send messages to the backend
	- Project/file selection and file browser available in UI

See `coai_plan.md` and `coai_plan_copy.md` for the full plan and progress tracking.
