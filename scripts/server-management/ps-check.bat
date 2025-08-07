@echo off
chcp 65001 >nul
echo.
echo ===================================
echo    Aktyvus COAI Procesai
echo ===================================
echo.

echo [Node.js procesai]
tasklist | findstr node.exe
if %errorlevel%==0 (
    echo OK Node.js procesas veikia
) else (
    echo NO Node.js nerastas
)

echo.
echo [Python procesai] 
tasklist | findstr python.exe
if %errorlevel%==0 (
    echo OK Python procesas veikia
) else (
    echo NO Python nerastas
)

echo.
echo [Portu uzimtumas]
echo Port 3000:
netstat -ano | findstr ":3000 .*LISTENING"
if %errorlevel%==0 (
    echo OK Port 3000 klausosi
) else (
    echo NO Port 3000 laisvas
)

echo.
echo Port 5000:
netstat -ano | findstr ":5000 .*LISTENING"
if %errorlevel%==0 (
    echo OK Port 5000 klausosi
) else (
    echo NO Port 5000 laisvas
)

echo.
echo ===================================
echo    Tikrinimas baigtas
echo ===================================
echo.
