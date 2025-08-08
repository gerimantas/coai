@echo off
chcp 65001 >nul
echo.
echo ====================================
echo     Perkraunami COAI serveriai
echo ====================================
echo.

REM Pereiti į projekto šaknį
cd /d "c:\ai_projects\coai"

echo [1/3] Sustabdomi serveriai...
echo.

REM Švelniai sustabdyti serverius
call "scripts\server-management\graceful-stop.bat"

if %errorlevel% neq 0 (
    echo WARNING Švelnaus sustabdymo klaida, bandomas priverstinis...
    call "scripts\server-management\kill-servers.bat"
)

echo.
echo [2/3] Laukiama 3 sekundes...
timeout /t 3 >nul

echo.
echo [3/3] Paleidžiami serveriai...
echo.

REM Paleisti serverius
call "scripts\server-management\start-servers.bat"

if %errorlevel%==0 (
    echo.
    echo ====================================
    echo     ✅ SERVERIAI SĖKMINGAI PERKRAUTI
    echo ====================================
    echo.
) else (
    echo.
    echo ====================================
    echo     ❌ SERVERIŲ PERKROVIMO KLAIDA
    echo ====================================
    echo.
    echo Bandykite:
    echo 1. kill-servers.bat
    echo 2. start-servers.bat
    echo.
)

pause
