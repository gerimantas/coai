# Copilot Instructions: COAI Stage I Plan Execution, Progress Tracking, and Ad Hoc Task Management

---

## Purpose

- Track and manage every step of the Stage I (MVP) plan for the COAI project.
- Mark each step as [ ] not started, [x] done, [v] verified, [a] approved, or [!] blocked/problem.
- Add, describe, and track ad hoc (unplanned) tasks without changing the original plan.
- Record all plan changes in git commits and an optional log file.
- Enforce read-only policy on the master plan.

---

## Key Files

- **Read-only plan:**  
  `C:\ai_projects\coai\coai_plan.md`
- **Editable working copy:**  
  `C:\ai_projects\coai\coai_plan_copy.md`
- **Optional log for changes:**  
  `C:\ai_projects\coai\.coai\logs\plan_changes.log`

---

## Workflow and Rules

### 1. Prepare the working plan copy

- If `coai_plan_copy.md` does not exist, copy `coai_plan.md` to create it.
- Set file permissions so `coai_plan.md` is read-only for all users.
- Never modify the original master plan. All changes happen in the working copy.

### 2. Marking progress

- To mark a task:
    - Change its status marker in `coai_plan_copy.md`:
        - `[ ]` – not started
        - `[x]` – done
        - `[v]` – verified/tested
        - `[a]` – approved/final
        - `[!]` – blocked/problem
    - Optionally, append a timestamp, initials, or comment, e.g.:  
      `[x] 2. App (backend) integration with UI (frontend) | 2024-08-07, GM`
- Never edit or remove completed/approved tasks—only mark status and add logs.

### 3. Adding ad hoc (unplanned) tasks

- New tasks that arise during work are only added to `coai_plan_copy.md`.
- Insert with logical numbering (e.g., 2.1, 4.2) or in a special section (“Ad Hoc Tasks” as A.1, A.2, etc.).
- Always include:
    - Description
    - Date added
    - Author/initiator
    - (Optional) Reason/context
    - Example:  
      `[ ] 3.2. Add endpoint for health check (added 2024-08-07 by AI agent, reason: ops requirement)`
- Optionally log new tasks and all changes in `.coai/logs/plan_changes.log`.

### 4. Committing every plan update

- After marking progress or adding tasks:
    - Stage and commit changes:  
      `git add coai_plan_copy.md`
      `git commit -m "Mark step 3.2 as done / Add task 4.1 in COAI Stage I plan"`
- Optionally:  
    - Append to log:  
      `echo "2024-08-07: Step 3.2 done, by GM" >> .coai/logs/plan_changes.log`

### 5. Restrictions

- Never edit `coai_plan.md`.
- Only update progress and add new tasks in `coai_plan_copy.md`.
- Always commit after any update.
- Never rewrite history—only add, mark, and log.

---

## Task List for Stage I (to be tracked and updated in `coai_plan_copy.md`)

```markdown
# Stage I: Minimal Working COAI Core (MVP)

## [ ] 0. Directory structure setup

1. [ ] Create directories:
    - [ ] `C:\ai_projects\coai\frontend\`
    - [ ] `C:\ai_projects\coai\backend\`
    - [ ] `C:\ai_projects\coai\.coai\`
2. [ ] Create a `README.md` file in each folder with a brief explanation.
3. [ ] In the root, create a central `README.md` describing project launch and structure.

## [ ] 1. Template setup

1. [ ] Copy the template from `C:\ai_projects\coai\ui-template` to `C:\ai_projects\coai\frontend`
2. [ ] Copy the template from `C:\ai_projects\coai\app-template` to `C:\ai_projects\coai\backend`
3. [ ] Ensure internal template structure matches COAI plan (see file tree).
4. [ ] In `frontend`, run `npm install` and `npm run dev`.
5. [ ] In `backend`, run `pip install -r requirements.txt` and `python main.py`.
6. [ ] Verify both apps start: UI at http://localhost:3000, backend at http://localhost:5000.

## [ ] 2. App (backend) integration with UI (frontend)

1. [ ] On `/chat` page in `frontend`, send POST requests to `http://localhost:5000/api/chat`.
2. [ ] Verify requests from frontend reach backend and return a response.
3. [ ] If needed, in `frontend`, create `.env.local` with `NEXT_PUBLIC_API_URL=http://localhost:5000`.
4. [ ] If needed, enable CORS in backend (`pip install flask-cors`).

## [ ] 3. User interface (frontend) – Chat page

1. [ ] Create `/chat` page with:
    - [ ] Text input, Send button (Enter shortcut)
    - [ ] Message area (user/AI, code blocks)
    - [ ] Project/file dropdown (dummy data)
    - [ ] Loader/progress indicator
    - [ ] Error/status area
2. [ ] Connect "send" to POST request to backend.
3. [ ] Display backend response.
4. [ ] Test full message flow (UI → backend → UI).

## [ ] 4. Task processing center / Prompt preprocessor (backend)

1. [ ] Add `/api/chat` endpoint (accepts POST with `{"message": "..."}`).
2. [ ] Add context (project, file info) to prompt as needed.
3. [ ] Send prompt to Copilot/LLM agent in English.
4. [ ] Return response to frontend.
5. [ ] Log each action (query, prompt, response).

## [ ] 5. Orchestrator (backend)

1. [ ] Create orchestrator layer (module/function).
2. [ ] Ensure sequential module communication (frontend → preprocessor → orchestrator → agent).
3. [ ] Log all orchestration actions.

## [ ] 6. AI agent module (backend)

1. [ ] Implement function to send prompt to Copilot (GPT-4.1) or OpenAI API.
2. [ ] Only accept well-prepared prompts.
3. [ ] Return response to orchestrator.

## [ ] 7. File system access and management (backend)

1. [ ] Add `/api/files/{filename}` endpoint.
2. [ ] Read files (read-only, path security).
3. [ ] In frontend, display file list (dummy for MVP).

## [ ] 8. Project management (single project, backend)

1. [ ] Use `.coai` directory for metadata: `C:\ai_projects\coai\.coai`
2. [ ] Implement basic .coai file read/write (plans, logs) in backend.
3. [ ] Show active project info in frontend (dummy for MVP).

## [ ] 9. Testing and documentation

1. [ ] Update `README.md` with launch and usage instructions.
2. [ ] Add unit tests for backend (`pytest`), frontend (e.g., React Testing Library).
3. [ ] Test end-to-end: message from UI through backend to agent and back.
4. [ ] Use English or bilingual code/comments.

## Ad Hoc / Additional Tasks

- [ ] A.1. <describe any extra task here, with date, reason, and author>
