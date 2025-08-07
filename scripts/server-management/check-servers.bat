@echo off
chcp 65001 >nul
echo.
echo ====================================
echo    COAI Serveriu Busenos Tikrinimas
echo ====================================
echo.

echo [Frontend - Next.js]
curl -s http://localhost:3000 >nul 2>&1
if %errorlevel%==0 (
    echo OK Frontend VEIKIA ^(port 3000^)
) else (
    echo NO Frontend NEVEIKIA
)

echo.
echo [Backend - Python Flask]
curl -s http://localhost:5000 >nul 2>&1
if %errorlevel%==0 (
    echo OK Backend VEIKIA ^(port 5000^)
) else (
    echo NO Backend NEVEIKIA
)

echo.
echo [Portu tikrinimas]
netstat -ano | findstr :3000 >nul 2>&1
if %errorlevel%==0 (
    echo OK Port 3000 uzimtas
) else (
    echo NO Port 3000 laisvas
)

netstat -ano | findstr :5000 >nul 2>&1
if %errorlevel%==0 (
    echo OK Port 5000 uzimtas
) else (
    echo NO Port 5000 laisvas
)

echo.
echo [Procesu tikrinimas]
tasklist | findstr node.exe >nul 2>&1
if %errorlevel%==0 (
    echo OK Node.js procesas veikia
) else (
    echo NO Node.js procesas nerastas
)

tasklist | findstr python.exe >nul 2>&1
if %errorlevel%==0 (
    echo OK Python procesas veikia
) else (
    echo NO Python procesas nerastas
)

echo.
echo ====================================
echo    Tikrinimas baigtas
echo ====================================
echo.
