# Ad Hoc / Additional Tasks

[x] A.1. Atkurta ir aktyvuota tamsi UI tema (Tailwind dark mode), atnaujinti komponentų stiliai | 2025-08-07, AI agent, reason: user request
[x] A.2. Orchestrator integravimas į routes.py ir testavimas | 2025-08-07, AI agent, reason: Stage 5 completion verification
[x] A.3. AI agents method signature klaidos pataisymas orchestrator.py faile | 2025-08-07, AI agent, reason: runtime error fix - process_request() signature mismatch
[x] A.4. Stage 0-2 dokumentacijos headers atnaujinimas iš [ ] į [x] | 2025-08-07, AI agent, reason: documentation accuracy - all sub-tasks completed
[x] A.5. Git istorijos išvalymas ir GitHub push problemos sprendimas | 2025-08-07, AI agent, reason: 147MB Next.js SWC file exceeded GitHub limits, created clean repository
[x] A.6. Failų naršyklės lazy loading ir tree vizualizacijos optimizacija | 2025-08-09, AI agent, reason: performance & usability improvement
[x] A.7. Backend path security enhancement for file access | 2025-08-09, AI agent, reason: security compliance

[ ] A.8. Implementation of UI design and file browser centralization/optimization plans:
    | 2025-08-09, AI agent, reason: centralized UI improvement and file browser UX enhancement
    [x] A.8.1. Dizaino pataisymai: pašalintos ikonos, mėlynos spalvos, subtilesnys šriftas | 2025-08-10, AI agent, reason: user request - minimalist design matching original
    [x] A.8.2. Tikslaus pavyzdžio kopijos sukūrimas su SVG ikonų biblioteka | 2025-08-10, AI agent, reason: pixel-perfect UI template creation
    [x] A.8.3. Dizaino atkūrimas po nesėkmingo eksperimento | 2025-08-10, AI agent, reason: rollback to working minimalist design

    **UI_CENTRAL_PLAN.md – UI Centralization Plan**
    [ ] 1. Color and Style Management: global CSS/Tailwind config, main colors, fonts, border radius, shadows, CSS variables or Tailwind themes.
    [ ] 2. UI Component Library: shared components (`Button`, `Card`, `Tab`, `StatusBar`, `Loader`, `Alert`, `Sidebar`, `Toolbar`), clear props, all pages use these.
    [ ] 3. Layout and Structure: main `Layout` component, common structure (sidebar, toolbar, statusbar, main content), all pages use this layout.
    [ ] 4. Navigation: `Tab` or `NavBar` component, active tab highlighting, centralized style/functionality.
    [ ] 5. Dark/Light Mode: support via Tailwind or CSS variables, affects all components.
    [ ] 6. Responsiveness: all components responsive, layout adapts to screen size.
    [ ] 7. Centralized Functionality: status, notifications, loaders, errors via shared components; API/user/project info via shared context (`React Context`/`zustand`).
    [ ] 8. Icons and Visuals: shared icon library (Heroicons, FontAwesome), integrated via props.
    [ ] 9. Documentation: document component usage, props, style change principles in README/UI guidelines.
    [ ] Actions: create/configure global style/theme, refactor pages to use shared components, create/apply layout, navigation, status, notification components, document UI change principles.
    [ ] Result: any design/functionality changes are applied to the entire UI quickly and centrally.
    [UI_CENTRAL_PLAN.md](UI_CENTRAL_PLAN.md)

    **UI_FILES_OPTIMIZATION.md – UI Files Page Optimization Proposals**
    [ ] 1. Lazy Loading: load only opened folders, not entire tree; improves load time/performance.
    [ ] 2. Large File Content Limiting: show part of large files or warning; prevents UI slowdown.
    [ ] 3. File Search: add search box for quick file/folder finding.
    [ ] 4. Multiple File Preview: allow opening multiple files (tabs) for comparison/multitasking.
    [ ] 5. Context Menu: right-click menu with actions (download, copy path, delete).
    [ ] 6. Skeleton Loader: visual skeleton loader instead of "Loading..." for modern UI.
    [ ] 7. Error Handling: clearer messages for inaccessible files, permission denied, errors.
    [ ] 8. Style and UX: more Tailwind/other UI framework styles for modern, user-friendly browser.
    [ ] 9. Breadcrumbs Navigation: show full path at top for easy folder navigation.
    [UI_FILES_OPTIMIZATION.md](UI_FILES_OPTIMIZATION.md)
# Stage I: Minimal Working COAI Core (MVP)

---

## [x] 0. Directory structure setup | 2025-08-07, AI agent, reason: All directories created, README files in place

### Goal
Create a clear, standardized project folder and file structure.

### Instructions
1. [x] Create directories:
    - [x] `C:\ai_projects\coai\frontend\` – user interface (Next.js, React) | 2025-08-07, AI
    - [x] `C:\ai_projects\coai\backend\`  – server part (Flask, API, orchestrator, agents) | 2025-08-07, AI
    - [x] `C:\ai_projects\coai\.coai\`     – COAI metadata (plans, logs, rules, usage) | 2025-08-07, AI
2. [x] Create a main `README.md` file in each folder with a brief explanation. | 2025-08-07, AI
3. [x] In the project root, create a central `README.md` describing project launch and structure. | 2025-08-07, AI

---

## [x] 1. Template setup | 2025-08-07, AI agent, reason: Templates copied, npm/pip installs completed, both servers running successfully

### Goal
Use prepared UI and backend templates for the COAI system.

### Instructions
1. [x] Copy the template from `C:\ai_projects\coai\ui-template` to `C:\ai_projects\coai\frontend` | 2025-08-07, AI
2. [x] Copy the template from `C:\ai_projects\coai\app-template` to `C:\ai_projects\coai\backend` | 2025-08-07, AI
3. [x] Check that the internal template structure matches COAI plan requirements (see file tree below) | 2025-08-07, AI
4. [x] In the `frontend` folder, run:
    - `npm install` | 2025-08-07, AI
    - `npm run dev` | 2025-08-07, AI
5. [x] In the `backend` folder, run:
    - `pip install -r requirements.txt` | 2025-08-07, AI
    - `python main.py` | 2025-08-07, AI
6. [x] Check that both projects start: UI – http://localhost:3000, backend – http://localhost:5000 | 2025-08-07, AI (UI & backend OK)

---

## [x] 2. App (backend) integration with UI (frontend) | 2025-08-07, AI agent, reason: Frontend/backend communication working, CORS enabled, API endpoints functional

### Goal
Ensure frontend and backend can exchange data via API.

### Instructions
1. [x] On the `frontend` `/chat` page, send POST requests to the backend API endpoint:  
    `http://localhost:5000/api/chat` | 2025-08-07, AI
2. [x] Check that the request from the frontend reaches the backend and returns a response. | 2025-08-07, AI
3. [x] If needed, in the `frontend` folder, create a `.env.local` file with the API endpoint. | 2025-08-07, AI
4. [x] In the backend, enable CORS (`pip install flask-cors`) to allow API calls from `frontend`. | 2025-08-07, AI

---

## [x] 3. User interface (frontend) – Chat page | 2025-08-07, AI

### Goal
Create a basic chat page that lets you send queries to the backend and view responses.

### Instructions
1. [x] Create a `/chat` page:
    - [x] Text input field, "Send" button (with Enter shortcut) | 2025-08-07, AI
    - [x] Message area (user/AI messages, code blocks) | 2025-08-07, AI
    - [x] Project/file selection dropdown (dummy data for MVP) | 2025-08-07, AI
    - [x] Loader/progress indicator | 2025-08-07, AI
    - [x] Error/status message area | 2025-08-07, AI
2. [x] Connect the "send" action to a POST request to the backend:  
    URL: `http://localhost:5000/api/chat` | 2025-08-07, AI
3. [x] Display the backend response | 2025-08-07, AI
4. [x] Test the message flow (UI → backend → UI) | 2025-08-07, AI

---

## [x] 4. Task processing center / Prompt preprocessor (backend) | 2025-08-07, AI

### Goal
Receive queries from frontend, prepare prompts for the Copilot/LLM agent.

### Instructions
1. [x] Add endpoint `/api/chat`:
    - [x] Accepts POST with `{"message": "..."}` (JSON) | 2025-08-07, AI
    - [x] Adds basic context (e.g., project name, file info) | 2025-08-07, AI
    - [x] If needed, extract prompt optimization to a separate module | 2025-08-07, AI
2. [x] Prepare so that the prompt is sent to the Copilot/LLM agent in English | 2025-08-07, AI
3. [x] Return the AI response to the frontend | 2025-08-07, AI
4. [x] Log actions (query, prompt, response) | 2025-08-07, AI

---

## [x] 5. Orchestrator (backend) | 2025-08-07, AI agent

### Goal
Coordinate requests between frontend, prompt preprocessor, and AI agents.

### Instructions
1. [x] Create an Orchestrator layer (module or function). | 2025-08-07, AI (created app/orchestrator.py with COAIOrchestrator class)
2. [x] Ensure communication between modules happens sequentially (frontend → preprocessor → orchestrator → agent). | 2025-08-07, AI (full pipeline implemented)
3. [x] Log each request in the actions log. | 2025-08-07, AI (integrated with logger.py)

---

## [x] 6. AI agents module (backend) | 2025-08-07, AI agent, reason: CopilotAgent implemented with mock responses, integrated with orchestrator, tested successfully

### Goal
Create an agent interface with Copilot (GPT-4.1) or OpenAI API.

### Instructions
1. [x] Implement a function that receives a prompt and sends it to the LLM (Copilot/OpenAI) | 2025-08-07, AI (implemented CopilotAgent with mock responses, method signature fixed)
2. [x] Ensure the agent accepts only properly prepared prompts | 2025-08-07, AI (validation in AIAgent base class)
3. [x] Receive and process the response, return it to the orchestrator | 2025-08-07, AI (integrated with orchestrator.py, tested via curl)

---

## [x] 7. File system access and management module (backend) | 2025-08-09, AI agent

### Goal
Allow the backend to read basic project files.

### Instructions
1. [x] Add endpoint `/api/files/{filename}` | 2025-08-09, AI agent, reason: implemented in backend/app/routes.py
2. [x] Read files in "read" mode only, check path (security!) | 2025-08-09, AI agent, reason: path security and read-only enforced in backend
3. [x] In the frontend, display a file list (dummy data for MVP) | 2025-08-09, AI agent, reason: file browser implemented with lazy loading

---


## [x] 8. Project management module (single project, backend) | 2025-08-09, AI agent, reason: Backend .coai failų skaitymas/rašymas įgyvendintas, UI rodo aktyvaus projekto informaciją

### Goal
Manage project meta-information and COAI files (single-project mode).

### Instructions
1. [x] Use a single `.coai` directory for the project:  
    `C:\ai_projects\coai\.coai` | 2025-08-09, AI agent
2. [x] In the backend, implement basic .coai file read/write (plans, logs) | 2025-08-09, AI agent (API endpointai /api/coai/<filename> GET/POST)
3. [x] In the frontend, show active project info (dummy for MVP) | 2025-08-09, AI agent (UI blokas MainContent.js)

---

## [ ] 9. Testing and basic documentation

### Goal
Check if the full MVP flow works.

### Instructions
1. [ ] In the project `README.md`, briefly describe launch and main usage instructions.
2. [ ] Add basic unit tests for backend (`pytest`), frontend (e.g., React Testing Library)
3. [ ] Test end-to-end flow: message from UI goes through backend to agent and back to UI
4. [ ] Code samples and comments – in English or bilingual

---

## Initial file structure tree (MVP)

```plaintext
C:\ai_projects\coai\
│
├── frontend\                      # Next.js, React UI
│   ├── src\
│   │   ├── app\
│   │   │   ├── layout.js
│   │   │   ├── page.js
│   │   │   ├── chat\page.js
│   │   │   ├── agents\page.js
│   │   │   ├── servers\page.js
│   │   │   ├── projects\page.js
│   │   │   ├── logs\page.js
│   │   │   ├── settings\page.js
│   │   │   └── globals.css
│   │   ├── components\
│   │   │   ├── Toolbar.js
│   │   │   ├── Sidebar.js
│   │   │   ├── StatusBar.js
│   │   │   ├── Card.js
│   │   │   ├── Button.js
│   │   │   └── MainContent.js
│   │   └── styles\
│   ├── public\
│   ├── package.json
│   ├── next.config.mjs
│   ├── tailwind.config.js
│   ├── postcss.config.mjs
│   ├── jsconfig.json
│   └── README.md
│
├── backend\                       # Flask API, orchestrator, agents
│   ├── app\
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── utils.py
│   │   ├── orchestrator.py
│   │   ├── agents.py
│   │   └── models.py
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
│
├── .coai\                         # COAI metadata
│   ├── plans\
│   ├── logs\
│   ├── usage\
│   ├── rules\
│   └── README.md
│
├── README.md
└── .gitignore
```
