# COAI Project Test Coverage


## 1. Backend (Flask API)

### 1.1. Test list
[x] 1. `/api/chat` endpoint: POST request, checks for `reply` field in response, status code, error handling. *(test_main.py)*
[x] 2. `/api/files/<filename>` endpoint: GET request, checks file content retrieval, status code, error handling for missing or forbidden files. *(test_main.py)*
[x] 3. `/api/files/list` endpoint: GET request, checks file tree structure retrieval and security (forbidden paths).
[x] 4. `/api/chat/history` endpoint: GET request, checks chat history retrieval and error handling.
[x] 5. `/api/orchestrator/status` endpoint: GET request, checks orchestrator status response.
[x] 6. `/api/chat` endpoint: POST with empty message, checks for error response.
[x] 7. `/api/chat` endpoint: POST with too long message, checks for error response.
[x] 8. `/api/files/<filename>` endpoint: GET with invalid path, checks for error response.

## 2. Frontend (React)

### 2.1. Test list
[x] 1. `Button` component: renders with text, calls `onClick` when clicked. *(Button.test.js)*
[ ] 2. Loader, Alert, StatusBar, Card, Sidebar, Toolbar components: render and props handling.
[ ] 3. FileBrowser component: renders file list, handles props, displays errors.
[ ] 4. `/chat` page: input, send action, displays response and errors.
[ ] 5. File view page: displays file content, handles errors.
[ ] 6. UI → API integration: message sent from UI reaches backend and response is displayed.
[ ] 7. FileBrowser integration: requests file list from backend and displays it.

---

*Legend:*
- **Implemented tests**: already present in the codebase.
- **Recommended additional tests**: should be added for full coverage and reliability.
