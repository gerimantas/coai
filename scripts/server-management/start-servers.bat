@echo off
chcp 65001 >nul
echo.
echo ====================================
echo     Paleidžiami COAI serveriai
echo ====================================
echo.

REM Pereiti į projekto šaknį
cd /d "c:\ai_projects\coai"

REM Tikrinti ar npm yra įdiegtas
where npm >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR npm nerastas! Įdiekite Node.js
    pause
    exit /b 1
)

REM Tikrinti ar Python yra įdiegtas
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR Python nerastas! Įdiekite Python
    pause
    exit /b 1
)

echo [Tikrinimas] Ar serveriai jau veikia...
curl -s http://localhost:3000 >nul 2>&1
if %errorlevel%==0 (
    echo WARNING Frontend jau veikia port 3000
)

curl -s http://localhost:5000 >nul 2>&1
if %errorlevel%==0 (
    echo WARNING Backend jau veikia port 5000
)

echo.
echo [Paleidimas] Pradedamas serverių paleidimas...
echo.

REM Patikrinti ar node_modules egzistuoja
if not exist "node_modules" (
    echo INFO Diegiamos dependencies...
    npm install
    if %errorlevel% neq 0 (
        echo ERROR npm install nepavyko
        pause
        exit /b 1
    )
)

REM Patikrinti ar frontend node_modules egzistuoja
if not exist "frontend\node_modules" (
    echo INFO Diegiamos frontend dependencies...
    cd frontend
    npm install
    if %errorlevel% neq 0 (
        echo ERROR frontend npm install nepavyko
        pause
        exit /b 1
    )
    cd ..
)

REM Patikrinti ar backend dependencies įdiegtos
cd backend
python -c "import flask" >nul 2>&1
if %errorlevel% neq 0 (
    echo INFO Diegiamos backend dependencies...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo ERROR pip install nepavyko
        pause
        exit /b 1
    )
)
cd ..

echo.
echo [Start] Paleidžiami serveriai...
echo.
echo Frontend bus pasiekiamas: http://localhost:3000
echo Backend bus pasiekiamas: http://localhost:5000
echo.
echo Spauskite Ctrl+C norėdami sustabdyti
echo.

REM Paleisti abu serverius kartu
start "COAI Frontend" cmd /k "cd /d c:\ai_projects\coai\frontend && npm run dev"
timeout /t 3 >nul
start "COAI Backend" cmd /k "cd /d c:\ai_projects\coai\backend && python main.py"

echo.
echo [Info] Serveriai paleidžiami atskiruose languose...
echo Laukiama kol serveriai pilnai pasileis...
echo.

REM Laukti kol serveriai pasileis
set /a attempts=0
:wait_loop
set /a attempts+=1
if %attempts% gtr 30 (
    echo TIMEOUT Serveriai nepasileidė per 30 sekundžių
    goto :end
)

timeout /t 2 >nul

curl -s http://localhost:3000 >nul 2>&1
set frontend_status=%errorlevel%

curl -s http://localhost:5000 >nul 2>&1
set backend_status=%errorlevel%

if %frontend_status% neq 0 (
    echo Laukiama frontend... ^(%attempts%/30^)
    goto :wait_loop
)

if %backend_status% neq 0 (
    echo Laukiama backend... ^(%attempts%/30^)
    goto :wait_loop
)

echo.
echo ====================================
echo     ✅ SERVERIAI SĖKMINGAI PALEISTI
echo ====================================
echo.
echo Frontend: http://localhost:3000 ✅
echo Backend:  http://localhost:5000 ✅
echo.
echo Naudokite:
echo - check-servers.bat - tikrinimui
echo - graceful-stop.bat - sustabdymui
echo - kill-servers.bat - priverstiniam sustabdymui
echo.

:end
pause
