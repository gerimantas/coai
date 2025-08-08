@echo off
REM ===================================
REM COAI Server Management Configuration
REM ===================================

REM Serverių portai
set FRONTEND_PORT=3000
set BACKEND_PORT=5000

REM Serverių URL
set FRONTEND_URL=http://localhost:%FRONTEND_PORT%
set BACKEND_URL=http://localhost:%BACKEND_PORT%

REM Projekto keliai
set PROJECT_ROOT=c:\ai_projects\coai
set FRONTEND_DIR=%PROJECT_ROOT%\frontend
set BACKEND_DIR=%PROJECT_ROOT%\backend

REM Timeout nustatymai (sekundėmis)
set STARTUP_TIMEOUT=30
set SHUTDOWN_TIMEOUT=10
set RESTART_DELAY=3

REM Dependency check
set CHECK_DEPENDENCIES=1
set AUTO_INSTALL_DEPS=1

REM Logging
set LOG_LEVEL=INFO
set LOG_TO_FILE=0

REM Error handling
set EXIT_ON_ERROR=1
set SHOW_ERROR_DETAILS=1

REM UI nustatymai
set USE_COLORS=1
set SHOW_PROGRESS=1
set PAUSE_ON_EXIT=1

REM Process management
set KILL_ALL_NODE=0
set KILL_ALL_PYTHON=0
set GRACEFUL_FIRST=1

echo COAI Server Configuration loaded
echo Frontend: %FRONTEND_URL%
echo Backend:  %BACKEND_URL%
echo Project:  %PROJECT_ROOT%
