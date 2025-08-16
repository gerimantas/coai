# VS Code Terminal Guide for Beginners

## Table of Contents
1. [Terminal Basics](#terminal-basics)
2. [Multiple Terminals Management](#multiple-terminals-management)
3. [Navigation Between Terminals](#navigation-between-terminals)
4. [Terminal Profiles Setup](#terminal-profiles-setup)
5. [COAI Project Commands](#coai-project-commands)
6. [Server Management](#server-management)
7. [Troubleshooting](#troubleshooting)

## Terminal Basics

### Opening Terminal
| Action | Keyboard Shortcut | Menu Path |
|--------|------------------|-----------|
| Open/Close terminal | `Ctrl + `` ` | Terminal > New Terminal |
| Open new terminal | `Ctrl + Shift + `` ` | Terminal > New Terminal |
| Split terminal | `Ctrl + Shift + 5` | Terminal > Split Terminal |

### Basic Terminal Operations
| Action | Keyboard Shortcut | Description |
|--------|------------------|-------------|
| Clear terminal | `Ctrl + Shift + K` | Clear all terminal content |
| Stop running process | `Ctrl + C` | Stop current command/process |
| Close terminal | `Ctrl + D` | Close current terminal |
| Copy text | `Ctrl + Shift + C` | Copy selected text |
| Paste text | `Ctrl + Shift + V` | Paste clipboard content |

## Multiple Terminals Management

### Creating Multiple Terminals

#### Method 1: New Terminal Windows
```
1. Press Ctrl + Shift + `
2. Each press creates a new terminal tab
3. Terminal tabs appear at the bottom panel
```

#### Method 2: Split Terminals
```
1. Press Ctrl + Shift + 5
2. Current terminal splits horizontally
3. Both terminals share the same tab but different panes
```

#### Method 3: Profile Selection
```
1. Click dropdown arrow next to terminal tab
2. Select different terminal profile
3. Creates new terminal with specific configuration
```

### Terminal Layout Options

| Layout Type | Pros | Cons | Best For |
|-------------|------|------|----------|
| Separate Tabs | Easy switching, clean UI | Takes more space | Different projects |
| Split Panes | See both simultaneously | Less screen space | Monitoring + commands |
| Multiple Windows | Maximum screen usage | Complex management | Power users |

## Navigation Between Terminals

### Tab Navigation
| Action | Keyboard Shortcut | Alternative |
|--------|------------------|-------------|
| Next terminal | `Ctrl + PageDown` | Click terminal tab |
| Previous terminal | `Ctrl + PageUp` | Click terminal tab |
| Go to terminal 1 | `Ctrl + 1` | Click first tab |
| Go to terminal 2 | `Ctrl + 2` | Click second tab |

### Quick Terminal Selection
```
Method 1: Dropdown Menu
1. Click ▼ arrow next to terminal name
2. See list of all open terminals
3. Click desired terminal

Method 2: Command Palette
1. Press Ctrl + Shift + P
2. Type "Terminal: Focus"
3. Select specific terminal from list
```

### Professional Terminal Organization

#### Recommended Terminal Setup for Development
```
Terminal 1: Server Processes
- Purpose: Run long-running processes (npm run dev, python main.py)
- Keep this terminal running
- Don't execute other commands here

Terminal 2: Command Execution  
- Purpose: Git commands, file operations, quick tasks
- Primary working terminal
- Execute short commands here

Terminal 3: Testing/Debugging
- Purpose: Run tests, check logs, debugging
- Temporary commands and monitoring

Terminal 4: Package Management
- Purpose: Install packages, dependency management
- npm install, pip install commands
```

## Terminal Profiles Setup

### Available Profiles in COAI Project

| Profile Name | Purpose | Default Directory | Best For |
|--------------|---------|------------------|----------|
| Command Prompt | General commands | C:\ai_projects\coai | Git, file operations |
| PowerShell | Advanced scripting | C:\ai_projects\coai | Package management |
| COAI Servers | Server management | C:\ai_projects\coai | Running npm run dev |
| Git Bash | Git operations | C:\ai_projects\coai | Git workflows |

### Selecting Terminal Profile
```
Method 1: During Terminal Creation
1. Press Ctrl + Shift + `
2. Click dropdown arrow in terminal panel
3. Select desired profile

Method 2: Set Default Profile
1. Press Ctrl + Shift + P
2. Type "Terminal: Select Default Profile"
3. Choose your preferred profile
```

## COAI Project Commands

### Server Management Commands
```bash
# Start both servers (Frontend + Backend)
npm run dev

# Start only frontend (Next.js)
npm run frontend

# Start only backend (Python Flask)
npm run backend

# Install all dependencies
npm run install-deps
```

### Server Status Checking
```bash
# Check if frontend is running
curl http://localhost:3000

# Check if backend is running  
curl http://localhost:5000

# Check port usage
netstat -ano | findstr :3000
netstat -ano | findstr :5000

# Check running processes
tasklist | findstr node.exe
tasklist | findstr python.exe
```

### Development Workflow
```bash
# Initial setup
npm install
cd frontend && npm install
cd ../backend && pip install -r requirements.txt

# Daily development
npm run dev
# Keep this terminal running
# Use another terminal for other commands

# Git workflow (in separate terminal)
git status
git add .
git commit -m "your message"
git push
```

## Server Management

### Starting Servers

#### Recommended Approach: Dedicated Terminal
```
1. Open new terminal (Ctrl + Shift + `)
2. Select "COAI Servers" profile if available
3. Run: npm run dev
4. Leave this terminal running
5. Open another terminal for other commands
```

#### What Happens When You Run npm run dev
```
Terminal Output:
[0] > frontend@0.1.0 dev
[0] > next dev
[1] > python main.py
[1] Starting backend server...

Frontend: http://localhost:3000
Backend: http://localhost:5000
```

### Stopping Servers
```bash
# In the terminal running npm run dev:
Press Ctrl + C

# This stops both frontend and backend servers
# You will see:
# [0] Terminated
# [1] Terminated
```

### Server Troubleshooting

#### Common Issues and Solutions

| Problem | Symptoms | Solution |
|---------|----------|----------|
| Port already in use | Error: EADDRINUSE | Run: `netstat -ano \| findstr :3000` then `taskkill /PID <pid> /F` |
| Servers won't start | npm run dev fails | Check: `npm install` and dependencies |
| Can't access servers | Browser shows error | Verify servers are running: `curl http://localhost:3000` |
| Terminal blocked | Can't run commands | Open new terminal: `Ctrl + Shift + `` ` |

#### Process Management Commands
```bash
# Kill all Node.js processes
taskkill /IM node.exe /F

# Kill all Python processes  
taskkill /IM python.exe /F

# Kill specific process by PID
taskkill /PID 1234 /F

# Find process using specific port
netstat -ano | findstr :3000
```

## Troubleshooting

### Terminal Not Opening
```
Solution 1: Check VS Code Settings
1. Press Ctrl + Shift + P
2. Type "Preferences: Open Settings"
3. Search "terminal.integrated"
4. Verify terminal path is correct

Solution 2: Reset Terminal
1. Press Ctrl + Shift + P
2. Type "Developer: Reload Window"
3. Try opening terminal again
```

### Cannot Execute Commands
```
Problem: Commands not recognized
Cause: Wrong terminal profile or path issues

Solution:
1. Check current terminal profile (shown in terminal tab)
2. Switch to "Command Prompt" or "PowerShell"
3. Verify you're in correct directory: pwd (Linux/Mac) or cd (Windows)
```

### Multiple Terminals Confusion
```
Organization Strategy:
1. Name your terminals descriptively
2. Use consistent terminal layout
3. Keep server terminal always in same position
4. Close unused terminals regularly

Terminal Naming:
- Right-click terminal tab
- Select "Rename"
- Use clear names: "Servers", "Git", "Commands"
```

### Performance Issues
```
Too Many Terminals:
- Close unused terminals (Ctrl + D)
- Limit to 3-4 active terminals
- Use split panes instead of multiple tabs when possible

Memory Usage:
- Restart VS Code if terminals become slow
- Clear terminal history: Ctrl + Shift + K
```

## Professional Tips

### Efficient Terminal Workflow
1. **Dedicated Purpose**: Assign specific purpose to each terminal
2. **Consistent Layout**: Always keep servers in terminal 1, commands in terminal 2
3. **Regular Cleanup**: Close terminals you don't need
4. **Keyboard Navigation**: Use Ctrl + PageUp/PageDown for quick switching
5. **Profile Usage**: Use appropriate terminal profiles for different tasks

### Best Practices
1. Never run multiple commands in server terminal
2. Always check server status before starting development
3. Use separate terminal for git operations
4. Keep terminal count manageable (3-4 maximum)
5. Name terminals clearly for easy identification

## Git Commands

### Basic Git Operations
```bash
# Check repository status
git status

# Stage files for commit
git add .
git add filename.js

# Commit changes
git commit -m "your commit message"

# Push to remote repository
git push

# Pull latest changes
git pull
```

### Branch Management
```bash
# List all branches
git branch

# Create and switch to new branch
git checkout -b feature-name

# Switch to existing branch
git checkout main

# Merge branch into current branch
git merge feature-name
```

## Advanced Server Management Scripts

### Using Server Management Scripts
```bash
# Check server status
scripts\server-management\check-servers.bat

# Monitor running processes
scripts\server-management\ps-check.bat

# Stop all servers
scripts\server-management\kill-servers.bat

# Start servers with full setup
scripts\server-management\start-servers.bat

# Restart servers
scripts\server-management\restart-servers.bat
```

### Development Helper Scripts
```bash
# Setup development environment
scripts\development\setup-dev.bat

# Clean cache and dependencies
scripts\development\clean-cache.bat

# Quick git commit and push
scripts\git-helpers\quick-commit.bat "commit message"
```
