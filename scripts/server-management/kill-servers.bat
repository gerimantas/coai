@echo off
chcp 65001 >nul
echo.
echo =====================================
echo     Stabdoma visi COAI serveriai
echo =====================================
echo.

echo [Node.js procesai]
taskkill /F /IM node.exe 2>nul
if %errorlevel%==0 (
    echo OK Node.js procesai sustabdyti
) else (
    echo INFO Node.js procesu nerasta
)

echo.
echo [Python procesai]
taskkill /F /IM python.exe 2>nul
if %errorlevel%==0 (
    echo OK Python procesai sustabdyti
) else (
    echo INFO Python procesu nerasta
)

echo.
echo =====================================
echo      Serveriai sustabdyti
echo =====================================
echo.
