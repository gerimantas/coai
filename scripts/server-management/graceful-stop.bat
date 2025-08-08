@echo off
chcp 65001 >nul
echo.
echo ====================================
echo     Švelniai stabdomi COAI serveriai
echo ====================================
echo.

REM Bandyti švelniai sustabdyti per API
echo [API] Bandomas švelnus sustabdymas...

REM Bandyti siųsti shutdown signalą backend'ui (jei turi shutdown endpoint)
curl -s -X POST http://localhost:5000/api/shutdown >nul 2>&1
if %errorlevel%==0 (
    echo OK Backend shutdown signalas išsiųstas
) else (
    echo INFO Backend shutdown endpoint nepasiekiamas
)

REM Laukti 3 sekundes
echo [Wait] Laukiama 3 sekundes...
timeout /t 3 >nul

REM Tikrinti ar serveriai dar veikia
curl -s http://localhost:3000 >nul 2>&1
set frontend_running=%errorlevel%

curl -s http://localhost:5000 >nul 2>&1
set backend_running=%errorlevel%

if %frontend_running% neq 0 if %backend_running% neq 0 (
    echo.
    echo ====================================
    echo     ✅ SERVERIAI ŠVELNIAI SUSTABDYTI
    echo ====================================
    echo.
    goto :end
)

echo.
echo [Process] Bandomas procesų sustabdymas...

REM Bandyti rasti ir švelniai sustabdyti Node.js procesus
for /f "tokens=2" %%a in ('tasklist /fi "imagename eq node.exe" /fo csv ^| find "node.exe"') do (
    echo Sustabdomas Node.js PID: %%a
    taskkill /pid %%a >nul 2>&1
)

REM Bandyti rasti ir švelniai sustabdyti Python procesus su main.py
for /f "tokens=2" %%a in ('wmic process where "name='python.exe' and commandline like '%%main.py%%'" get processid /format:csv') do (
    if not "%%a"=="" if not "%%a"=="ProcessId" (
        echo Sustabdomas Python main.py PID: %%a
        taskkill /pid %%a >nul 2>&1
    )
)

REM Laukti dar 3 sekundes
timeout /t 3 >nul

REM Patikrinti ar serveriai sustabdyti
curl -s http://localhost:3000 >nul 2>&1
set frontend_running=%errorlevel%

curl -s http://localhost:5000 >nul 2>&1
set backend_running=%errorlevel%

if %frontend_running% neq 0 if %backend_running% neq 0 (
    echo.
    echo ====================================
    echo     ✅ SERVERIAI SĖKMINGAI SUSTABDYTI
    echo ====================================
    echo.
) else (
    echo.
    echo ====================================
    echo     ⚠️ SERVERIAI DAR VEIKIA
    echo ====================================
    echo.
    echo Liko veikiantys serveriai:
    
    if %frontend_running%==0 (
        echo - Frontend ^(port 3000^)
    )
    
    if %backend_running%==0 (
        echo - Backend ^(port 5000^)
    )
    
    echo.
    echo Naudokite kill-servers.bat priverstiniam sustabdymui
    echo.
    exit /b 1
)

:end
echo Serveriai sustabdyti. Galite paleisti juos vėl su start-servers.bat
echo.
