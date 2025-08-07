# 🖥️ VS Code Terminalo ir Komandų Valdymo Dokumentas

## ⚠️ KRITINĖ PROBLEMA: Serverių Terminalas Blokuoja Komandas

**✅ IŠSPRĘSTA! VS Code settings.json konfliktas pašalintas**

**Problema**: Kai serveriai veikia terminale (`npm run dev`), jis blokuoja visas kitas komandas!

**SPRENDIMAS - 3 būdai**:

### 1. NAUJAS TERMINALAS (Rekomenduojama) ⭐
```
Ctrl+Shift+`     # Naujas terminalas Command Prompt
```
Arba: Terminal → New Terminal → Automatiškai atidarys "Command Prompt"

### 2. SPLIT TERMINAL
```
Ctrl+Shift+5     # Padalinti terminalą
```
Viename - serveriai veikia, kitame - vykdote komandas

### 3. TERMINALŲ PROFILIAI
- Spauskite ▼ prie terminalo tab
- Pasirinkite reikiamą profilį
- Default: "Command Prompt" (normalūs terminalai)

---

## **✅ COAI Sistema VEIKIA!**

### **🎯 Greitas Paleidimas**
1. **VS Code**: `Ctrl+Shift+P` → "Tasks: Run Task" → "🚀 Start All Servers"
2. **Terminalas**: `npm run dev` (abu serveriai paraleliai)
3. **Serveriai pasiekiami**:
   - Frontend: http://localhost:3000 (Next.js)
   - Backend: http://localhost:5000 (Python Flask)

### **🔧 npm-run-all Valdymas**
```bash
npm run dev          # Abu serveriai paraleliai
npm run frontend     # Tik Next.js (port 3000)
npm run backend      # Tik Python Flask (port 5000)
```

### **🔍 Serverių Būsenos Tikrinimas**
**Windows CMD komandos** (veiks bet kuriame terminale):

| Komanda | Paskirtis | Rezultatas |
|---------|-----------|------------|
| `curl http://localhost:3000` | Frontend statusas | Jei veikia: HTML turinys |
| `curl http://localhost:5000` | Backend statusas | Jei veikia: JSON response |
| `netstat -ano \| findstr :3000` | Port 3000 tikrinimas | Jei užimtas: rodys PID |
| `netstat -ano \| findstr :5000` | Port 5000 tikrinimas | Jei užimtas: rodys PID |

**VS Code Terminalo Profiliai** (dropdown meniu ▼):

| Profilis | Paskirtis | Kada naudoti |
|----------|-----------|--------------|
| `🚀 COAI Servers` | Serverių paleidimas | npm run dev, serverių valdymas |
| `📊 Server Monitor` | Serverių stebėjimas | HTTP tikrinimas, diagnostika |
| `Command Prompt` | Normalūs terminalai | Failų valdymas, git komandos |

**Code Snippets** (tik VS Code terminale su IntelliSense):

| Snippet | Komanda | Paskirtis |
|---------|---------|-----------|
| `check-servers` | Serverių būsena | ✅/❌ Frontend ir Backend status |
| `ps-check` | Procesų monitoringas | Node.js ir Python procesai |
| `kill-servers` | Sustabdyti | Užbaigti visus serverius |
| `coai-dev` | Dev komandos | Pagrindinės COAI komandos |

### **📊 Kaip Suprasti Ar Serveriai Veikia**

**Greitam tikrinimui Windows CMD:**
```cmd
REM Tikrinti abu serverius vienu metu:
curl http://localhost:3000 & curl http://localhost:5000

REM Jei curl nėra įdiegtas, naudokite:
powershell -Command "try { Invoke-WebRequest http://localhost:3000 -UseBasicParsing | Select-Object StatusCode } catch { 'Frontend NEVEIKIA' }"
powershell -Command "try { Invoke-WebRequest http://localhost:5000 -UseBasicParsing | Select-Object StatusCode } catch { 'Backend NEVEIKIA' }"
```

**VS Code snippet rezultatas:**
```bash
# Įveskite VS Code terminale:
check-servers

# Rezultatas jei VEIKIA:
✅ Frontend VEIKIA (port 3000)
✅ Backend VEIKIA (port 5000)
✅ Port 3000 užimtas
✅ Port 5000 užimtas

# Rezultatas jei NEVEIKIA:
❌ Frontend NEVEIKIA
❌ Backend NEVEIKIA
❌ Port 3000 laisvas
❌ Port 5000 laisvas
```

### **📊 Sistema Ready for Development!**
- ✅ npm-run-all package įdiegtas (134 dependencies)
- ✅ Frontend Next.js 15.4.4 su Shadcn UI  
- ✅ Backend Python Flask su AI agents
- ✅ VS Code tasks ir terminal profiles (išvalyti)
- ✅ Scripts aplankas organizuotas (server-management/, development/, git-helpers/)
- ✅ .bat komandos serverių valdymui ir development tools
- ✅ Kompletiškas dokumentas su hotkeys
- ✅ Code snippets VS Code terminalui

---

## 📋 **Turinys**
- [Terminalo Hotkey'ai](#terminalo-hotkey'ai)
- [Terminalo Profiliai](#terminalo-profiliai)
- [COAI Projekto Komandos](#coai-projekto-komandos)
- [Code Snippets Terminale](#code-snippets-terminale)
- [Serverių Diagnostika](#serverių-diagnostika)
- [Git Workflow](#git-workflow)
- [Debugging ir Troubleshooting](#debugging-ir-troubleshooting)
- [VS Code Tasks](#vs-code-tasks)
- [Terminalų Organizavimas](#terminalų-organizavimas)

---

## ⌨️ **Terminalo Hotkey'ai**

### **Pagrindiniai Terminalų Hotkey'ai**
| Hotkey | Veiksmas | Aprašymas |
|--------|----------|-----------|
| `Ctrl + `` ` | Atidaryti/Uždaryti terminalą | Toggle terminalo panelės |
| `Ctrl + Shift + `` ` | Naujas terminalas | Sukurti naują terminalo langą |
| `Ctrl + Shift + 5` | Split terminalas | Padalinti terminalą pusiau |
| `Ctrl + PageUp` | Ankstesnis terminalas | Perjungti į kairėje esantį terminalą |
| `Ctrl + PageDown` | Kitas terminalas | Perjungti į dešinėje esantį terminalą |
| `Ctrl + Shift + C` | Kopijuoti terminale | Kopijuoti pažymėtą tekstą |
| `Ctrl + Shift + V` | Įklijuoti terminale | Įklijuoti tekstą terminale |

### **Terminalų Valdymo Hotkey'ai**
| Hotkey | Veiksmas | Aprašymas |
|--------|----------|-----------|
| `Ctrl + Shift + K` | Išvalyti terminalą | Clear terminalo turinį |
| `Ctrl + C` | Nutraukti procesą | Sustabdyti veikiantį procesą |
| `Ctrl + D` | Uždaryti terminalą | Uždaryti aktyvų terminalą |
| `Alt + ←/→` | Naršyti terminuose | Greitai perjungti tarp terminalų |

---

## 🎯 **Code Snippets Terminale**

### **❗ Svarbu: Snippet'ų Veikimo Sąlygos**
- **Code snippets veikia TIK VS Code terminale** su IntelliSense
- **Windows CMD/PowerShell** - naudokite tiesiogines komandas
- **Aktivavimas**: Pradėkite rašyti prefix'ą ir spauskite `Tab`

### **❗ SVARBI PROBLEMA: VS Code Terminal Default Profile**

**🔧 Sprendimas terminalų konflikto:**
1. **Manual terminalo keitimas**: `Ctrl+Shift+`` ` → pasirinkite "📦 Package Manager" arba "Command Prompt"
2. **Default profilio keitimas**: `Ctrl+Shift+P` → "Terminal: Select Default Profile" → "Command Prompt"
3. **Greitas terminalo valdymas**: Naudokite terminalo dropdown meniu (▼ šalia terminalo pavadinimo)

**🎯 Kaip Vykdyti Script'us:**
```cmd
REM Serverių valdymas (iš bet kurio terminalo):
scripts\server-management\check-servers.bat    # Serverių būsenos tikrinimas
scripts\server-management\ps-check.bat         # Procesų monitoringas  
scripts\server-management\kill-servers.bat     # Sustabdyti visus serverius

REM Development tools:
scripts\development\setup-dev.bat              # Pilnas COAI setup
scripts\development\clean-cache.bat            # Cache išvalymas

REM Git helpers:
scripts\git-helpers\quick-commit.bat "message" # Greitas commit su push
```

### **Windows CMD Alternatyvos**
**✅ Organizuoti .bat script'ai COAI projekte:**

```cmd
REM Serverių valdymas:
scripts\server-management\check-servers.bat    # Serverių būsenos tikrinimas
scripts\server-management\ps-check.bat         # Procesų monitoringas  
scripts\server-management\kill-servers.bat     # Sustabdyti visus serverius

REM Development tools:
scripts\development\setup-dev.bat              # Pilnas COAI setup
scripts\development\clean-cache.bat            # Cache išvalymas

REM Git helpers:
scripts\git-helpers\quick-commit.bat "message" # Greitas commit su push
```

**Manual komandos:**
```cmd
REM Vietoj check-servers snippet'o:
curl http://localhost:3000 & curl http://localhost:5000
netstat -ano | findstr :3000
netstat -ano | findstr :5000

REM Vietoj ps-check snippet'o:
tasklist | findstr node.exe
tasklist | findstr python.exe

REM Vietoj kill-servers snippet'o:
taskkill /F /IM node.exe
taskkill /F /IM python.exe
```

### **Snippet'ų Naudojimas VS Code Terminale**
1. Atidarykite VS Code terminalą (`Ctrl+`` `)
2. Pradėkite rašyti snippet prefix'ą (pvz., `check`)
3. Paspauskite `Tab` arba `Enter` kad praplėsti snippet'ą
4. Komandos automatiškai įvykdomos terminale

### **COAI Snippet'ų Katalogas**

| Prefix | Komandos | Aprašymas |
|--------|----------|-----------|
| `coai-dev` | Development commands | Pagrindinės COAI komandos |
| `check-servers` | Server status check | ✅/❌ Serverių būsenos analizė |
| `ps-check` | Process monitoring | Node.js/Python procesų tikrinimas |
| `kill-servers` | Kill all servers | Sustabdyti visus serverius |
| `git-quick` | Git workflow | Add → Commit → Push |

### **Snippet'ų Pavyzdžiai**
```bash
# Įveskite terminale:
check-servers

# Išplečiama į:
echo === COAI Serverių Būsenos Tikrinimas ===
curl -s http://localhost:3000 > nul && echo ✅ Frontend VEIKIA...
curl -s http://localhost:5000 > nul && echo ✅ Backend VEIKIA...
# + port'ų tikrinimas
```

---

## 🎨 **Terminalo Profiliai**

### **COAI Projekto Terminalo Profiliai**
```json
{
  "terminal.integrated.profiles.windows": {
    "🚀 COAI Servers": {
      "path": "cmd.exe",
      "args": ["/k", "echo === COAI SERVERIU TERMINALAS === && cd /d C:\\ai_projects\\coai && echo. && echo Paleidimui naudokite: npm run dev && echo Sustabdymui: Ctrl+C && echo."],
      "icon": "server",
      "color": "terminal.ansiGreen"
    },
    "� Server Monitor": {
      "path": "cmd.exe",
      "args": ["/k", "cd /d C:\\ai_projects\\coai && echo === COAI SERVER MONITOR === && echo Frontend: http://localhost:3000 && echo Backend: http://localhost:5000 && echo. && echo Naudokite: && echo - scripts\\server-management\\check-servers.bat && echo - curl http://localhost:3000 && echo - curl http://localhost:5000 && echo."],
      "icon": "pulse",
      "color": "terminal.ansiCyan"
    },
    "� Git Commands": {
      "path": "C:\\Program Files\\Git\\bin\\bash.exe",
      "args": ["--login"],
      "icon": "git-branch", 
      "color": "terminal.ansiBlue"
    },
    "🔧 Backend Dev": {
      "path": "cmd.exe",
      "args": ["/k", "cd /d C:\\ai_projects\\coai\\backend && echo Backend Development"],
      "icon": "tools",
      "color": "terminal.ansiYellow"
    },
    "🌐 Frontend Dev": {
      "path": "cmd.exe",
      "args": ["/k", "cd /d C:\\ai_projects\\coai\\frontend && echo Frontend Development"],
      "icon": "browser",
      "color": "terminal.ansiMagenta"
    },
    "📦 Package Manager": {
      "path": "powershell.exe",
      "args": ["-NoExit", "-Command", "cd C:\\ai_projects\\coai; Write-Host 'Package Management' -ForegroundColor Green"],
      "icon": "package",
      "color": "terminal.ansiRed"
    }
  }
}
```

### **Terminalo Profilių Naudojimas**
1. **Dropdown meniu** - spragtelėkite ▼ šalia terminalo pavadinimo
2. **Serverių terminalas**: Pasirinkite "🚀 COAI Servers" → `npm run dev`
3. **Serverių monitoringas**: Pasirinkite "📊 Server Monitor" → HTTP tikrinimas
4. **Command Palette** - `Ctrl + Shift + P` → "Terminal: Select Default Profile"
5. **Greitas pasirinkimas** - `Ctrl + Shift + `` ` → pasirinkite profilį

### **🎯 Kaip Rasti Serverių Terminalą**
1. Spragtelėkite ▼ prie terminalo tab
2. Sąraše rasite:
   - **🚀 COAI Servers** - serverių paleidimui (`npm run dev`)
   - **📊 Server Monitor** - serverių stebėjimui ir tikrinimui
3. Pasirinkite reikiamą ir gausite specialų terminalą su instrukcijomis

---

## 🚀 **COAI Projekto Komandos**

## **🎯 COAI Projekto Komandų Valdymas**

### **Code Snippets Terminale (Naujas!)**
VS Code terminale galite naudoti **code snippet prefix'us**:

```bash
# Serverių valdymas
coai-dev              # Pagrindinės COAI komandos
check-servers         # Detali serverių būsenos analizė  
ps-check             # Procesų ir port'ų monitoringas
kill-servers         # Sustabdyti visus serverius

# Git workflow
git-quick            # Greitas add → commit → push
```

### **Serverių Valdymas (npm-run-all)**
```bash
# SETUP - Pirmas paleidimas
npm install                           # Įdiegti npm-run-all ir dependencies
cd frontend && npm install            # Įdiegti frontend dependencies
cd ../                               # Grįžti į root

# Pagrindinės komandos  
npm run dev                           # Paleisti abu serverius paraleliai
npm run frontend                      # Tik frontend serveris
npm run backend                       # Tik backend serveris

# Dependencies valdymas
npm run install-deps                  # Įdiegti visas dependencies (full setup)
npm install                          # Root package dependencies
```

### **🎯 npm-run-all Veikimo Principas**
```bash
# Kas vyksta kai paleidžiate:
npm run dev
# ↓
run-p frontend backend
# ↓ 
# [0] cd frontend && npm run dev    (Next.js serveris)
# [1] cd backend && python main.py  (Python serveris)
```

### **Serverių Komandos Detaliai**
```bash
# Frontend (terminalas: 🌐 Frontend Dev)
cd frontend
npm install                          # Įdiegti frontend dependencies
npm run dev                         # Paleisti Next.js dev serverį
npm run build                       # Build production versijai
npm run lint                        # Paleisti ESLint

# Backend (terminalas: 🔧 Backend Dev)  
cd backend
pip install -r requirements.txt     # Įdiegti Python dependencies
python main.py                      # Paleisti Flask/FastAPI serverį
python -m pytest                   # Paleisti testus
```

### **Serverių Status Tikrinimas**
```bash
# HTTP užklausos serverių tikrinimui
curl http://localhost:3000          # Frontend status
curl http://localhost:5000          # Backend status

# Portų tikrinimas Windows
netstat -an | findstr :3000        # Patikrinti port 3000
netstat -an | findstr :5000        # Patikrinti port 5000

# Procesų tikrinimas
tasklist | findstr node            # Node.js procesai
tasklist | findstr python          # Python procesai
```

---

## 📂 **Git Workflow**

### **Git Terminalas (📁 Git Commands)**
```bash
# Kasdieninis Git workflow
git status                          # Patikrinti repo būseną
git add .                          # Stage'inti visus pakeitimus  
git add filename.js                # Stage'inti konkretų failą
git commit -m "commit message"     # Commit su žinute
git push                          # Push į remote repo
git pull                          # Pull pakeitimus iš remote

# Branch'ų valdymas
git branch                        # Parodyti visus branch'us
git checkout -b feature-name      # Sukurti ir pereiti į naują branch
git checkout main                 # Pereiti į main branch
git merge feature-name            # Merge branch į dabartinį

# Istorijos peržiūra
git log --oneline                 # Trumpa commit istorija
git log --graph --pretty=format:'%h - %s (%cr) <%an>' --abbrev-commit
```

### **Git Aliases (Git Bash)**
```bash
# Pridėti į ~/.gitconfig arba naudoti komandas:
git config --global alias.st status
git config --global alias.co checkout  
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage 'reset HEAD --'

# Naudojimas:
git st                           # vietoj git status
git co main                      # vietoj git checkout main
```

---

## 🐛 **Debugging ir Troubleshooting**

### **🚨 VS Code Terminal Problema**
**Problema**: Bet kuris naujas VS Code terminalas atidaromas kaip "🚀 COAI Servers" profilis

**✅ Sprendimai:**
1. **Greitas terminalo keitimas**: 
   - Spauskite ▼ šalia terminalo pavadinimo
   - Pasirinkite "📦 Package Manager" arba "Command Prompt"

2. **Default profilio keitimas**:
   - `Ctrl+Shift+P` → "Terminal: Select Default Profile"
   - Pasirinkite "Command Prompt"

3. **Script'ų vykdymas**:
   - Naudokite pilnus kelius: `scripts\server-management\check-servers.bat`
   - Arba pakeiskite į tinkamą terminalą prieš vykdant komandas

### **Serverių Diagnostika (Script'ai)**
```bash
# 1. Patikrinti ar serveriai veikia (script)
scripts\server-management\check-servers.bat    # Detali analizė

# 2. Procesų monitoringas (script)
scripts\server-management\ps-check.bat         # Node.js ir Python procesai

# 3. Sustabdyti problematinius procesus (script)  
scripts\server-management\kill-servers.bat     # Sustabdyti visus serverius

# 4. Port'ų tikrinimas (manual)
netstat -ano | findstr :3000    # Frontend port
netstat -ano | findstr :5000    # Backend port
```

### **COAI Serverių Problemų Sprendimas**
```bash
# Jei serveriai nepaleidžiami
npm run dev -- --verbose           # Verbose output
npm cache clean --force            # Išvalyti npm cache
rm -rf node_modules && npm install # Reinstall node_modules

# Jei portai užimti
netstat -ano | findstr :3000      # Rasti procesą port 3000
taskkill /PID <process_id> /F      # Nutraukti procesą

# Backend Python problemos
python --version                   # Tikrinti Python versiją
pip list                          # Parodyti įdiegtas bibliotekas
pip install --upgrade pip         # Atnaujinti pip
```

### **VS Code Terminalo Problemos**
```bash
# Jei terminlas neatsidaro
Ctrl + Shift + P → "Developer: Reload Window"

# Jei keisti terminalo profile
Ctrl + Shift + P → "Terminal: Select Default Profile"

# Jei terminalo encoding problemos  
Ctrl + Shift + P → "Terminal: Configure Terminal Settings"
```

---

## ⚙️ **VS Code Tasks**

### **COAI Tasks (.vscode/tasks.json)**
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "🚀 Start All Servers",
      "type": "shell", 
      "command": "npm",
      "args": ["run", "dev"],
      "group": {
        "kind": "build",
        "isDefault": true
      }
    }
  ]
}
```

### **Tasks Naudojimas**
| Hotkey/Komanda | Veiksmas |
|----------------|----------|
| `Ctrl + Shift + P` → "Tasks: Run Task" | Atidaryti tasks sąrašą |
| `Ctrl + Shift + B` | Paleisti default build task |
| `F5` | Paleisti debug task |

---

## 📊 **Terminalų Organizavimas**

### **Recommended Terminalo Setup COAI Projektui**

#### **Terminalas #1: 🚀 Serveriai**
```bash
# Terminalo pavadinimas: "COAI Servers"
npm run dev
# [0] Frontend: ▲ Next.js running on http://localhost:3000
# [1] Backend: * Running on http://127.0.0.1:5000
```

#### **Terminalas #2: 📁 Git** 
```bash
# Terminalo pavadinimas: "Git Workflow"
git status
git add .
git commit -m "feature implementation"
git push
```

#### **Terminalas #3: 📦 Package Management**
```bash
# Terminalo pavadinimas: "Dependencies"
npm install new-package
pip install requests
npm run build
```

#### **Terminalas #4: 🧪 Testing/Debugging**
```bash
# Terminalo pavadinimas: "Testing"
npm test
python -m pytest
curl http://localhost:3000/api/test
```

### **Terminalo Panelės Konfigūracija**
```json
{
  "terminal.integrated.defaultLocation": "panel",
  "terminal.integrated.fontSize": 14,
  "terminal.integrated.fontFamily": "Consolas, 'Courier New', monospace",
  "terminal.integrated.cursorStyle": "line",
  "terminal.integrated.cursorBlinking": true,
  "terminal.integrated.scrollback": 10000
}
```

---

## 🎯 **Quick Reference Commands**

### **Greiti Development Commands**
```bash
# COAI development start
npm run dev                        # Start both servers
code .                            # Open VS Code
git status && git pull            # Check status and pull latest

# Quick server restart
Ctrl + C                          # Stop servers  
npm run dev                       # Restart servers

# Quick commit
git add . && git commit -m "quick fix" && git push
```

### **Emergency Commands**
```bash
# Kill all node processes
taskkill /IM node.exe /F
taskkill /IM python.exe /F

# Reset development environment
npm run dev
# or if broken:
npm install && npm run dev
```

---

## 📝 **Pastabos ir Patarimai**

1. **Terminalo skaitymas**: Naudokite terminalų pavadinimus su emoji geresniam vizualiam atpažinimui
2. **Git workflow**: Visada darykite `git status` prieš commit
3. **Serverių restart**: `Ctrl + C` terminale su `npm run dev` sustabdo abu serverius
4. **Debugging**: Naudokite `console.log()` frontend ir `print()` backend
5. **Performance**: Uždaryti nepanaudojamus terminus (Ctrl + D)

---

**Sukurta COAI projektui | VS Code Terminal Management**
