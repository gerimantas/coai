# Stage I: Minimal Working COAI Core (MVP)

---

## [ ] 0. Directory structure setup

### Goal
Create a clear, standardized project folder and file structure.

### Instructions
1. [ ] Create directories:
    - [ ] `C:\ai_projects\coai\frontend\` – user interface (Next.js, React)
    - [ ] `C:\ai_projects\coai\backend\`  – server part (Flask, API, orchestrator, agents)
    - [ ] `C:\ai_projects\coai\.coai\`     – COAI metadata (plans, logs, rules, usage)
2. [ ] Create a main `README.md` file in each folder with a brief explanation.
3. [ ] In the project root, create a central `README.md` describing project launch and structure.

---

## [ ] 1. Template setup

### Goal
Use prepared UI and backend templates for the COAI system.

### Instructions
1. [ ] Copy the template from `C:\ai_projects\coai\ui-template` to `C:\ai_projects\coai\frontend`
2. [ ] Copy the template from `C:\ai_projects\coai\app-template` to `C:\ai_projects\coai\backend`
3. [ ] Check that the internal template structure matches COAI plan requirements (see file tree below)
4. [ ] In the `frontend` folder, run:
    - `npm install`
    - `npm run dev`
5. [ ] In the `backend` folder, run:
    - `pip install -r requirements.txt`
    - `python main.py`
6. [ ] Check that both projects start: UI – http://localhost:3000, backend – http://localhost:5000

---

## [ ] 2. App (backend) integration with UI (frontend)

### Goal
Ensure frontend and backend can exchange data via API.

### Instructions
1. [ ] On the `frontend` `/chat` page (or other), send POST requests to the backend API endpoint:  
    `http://localhost:5000/api/chat`
2. [ ] Check that the request from the frontend reaches the backend and returns a response.
3. [ ] If needed, in the `frontend` folder, create a `.env.local` file with the API endpoint, e.g.:  
    `NEXT_PUBLIC_API_URL=http://localhost:5000`
4. [ ] In the backend, if needed, enable CORS (`pip install flask-cors`) to allow API calls from `frontend`.

---

## [ ] 3. User interface (frontend) – Chat page

### Goal
Create a basic chat page that lets you send queries to the backend and view responses.

### Instructions
1. [ ] Create a `/chat` page:
    - [ ] Text input field, "Send" button (with Enter shortcut)
    - [ ] Message area (user/AI messages, code blocks)
    - [ ] Project/file selection dropdown (dummy data for MVP)
    - [ ] Loader/progress indicator
    - [ ] Error/status message area
2. [ ] Connect the "send" action to a POST request to the backend:  
    URL: `http://localhost:5000/api/chat`
3. [ ] Display the backend response
4. [ ] Test the message flow (UI → backend → UI)

---

## [ ] 4. Task processing center / Prompt preprocessor (backend)

### Goal
Receive queries from frontend, prepare prompts for the Copilot/LLM agent.

### Instructions
1. [ ] Add endpoint `/api/chat`:
    - [ ] Accepts POST with `{"message": "..."}` (JSON)
    - [ ] Adds basic context (e.g., project name, file info)
    - [ ] If needed, extract prompt optimization to a separate module
2. [ ] Prepare so that the prompt is sent to the Copilot/LLM agent in English
3. [ ] Return the AI response to the frontend
4. [ ] Log actions (query, prompt, response)

---

## [ ] 5. Orchestrator (backend)

### Goal
Coordinate requests between frontend, prompt preprocessor, and AI agents.

### Instructions
1. [ ] Create an Orchestrator layer (module or function).
2. [ ] Ensure communication between modules happens sequentially (frontend → preprocessor → orchestrator → agent).
3. [ ] Log each request in the actions log.

---

## [ ] 6. AI agents module (backend)

### Goal
Create an agent interface with Copilot (GPT-4.1) or OpenAI API.

### Instructions
1. [ ] Implement a function that receives a prompt and sends it to the LLM (Copilot/OpenAI)
2. [ ] Ensure the agent accepts only properly prepared prompts
3. [ ] Receive and process the response, return it to the orchestrator

---

## [ ] 7. File system access and management module (backend)

### Goal
Allow the backend to read basic project files.

### Instructions
1. [ ] Add endpoint `/api/files/{filename}`
2. [ ] Read files in "read" mode only, check path (security!)
3. [ ] In the frontend, display a file list (dummy data for MVP)

---

## [ ] 8. Project management module (single project, backend)

### Goal
Manage project meta-information and COAI files (single-project mode).

### Instructions
1. [ ] Use a single `.coai` directory for the project:  
    `C:\ai_projects\coai\.coai`
2. [ ] In the backend, implement basic .coai file read/write (plans, logs)
3. [ ] In the frontend, show active project info (dummy for MVP)

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
