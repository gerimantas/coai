@echo off
echo.
echo =====================================
echo     COAI Cache Cleanup
echo =====================================
echo.

echo [1. Cleaning npm cache]
call npm cache clean --force
if %errorlevel%==0 (
    echo OK npm cache cleaned
) else (
    echo ERROR Failed to clean npm cache
)

echo.
echo [2. Cleaning frontend node_modules]
if exist "frontend\node_modules" (
    echo Removing frontend\node_modules...
    rmdir /s /q "frontend\node_modules"
    echo OK Frontend node_modules removed
) else (
    echo INFO Frontend node_modules not found
)

echo.
echo [3. Cleaning root node_modules]
if exist "node_modules" (
    echo Removing root node_modules...
    rmdir /s /q "node_modules"
    echo OK Root node_modules removed
) else (
    echo INFO Root node_modules not found
)

echo.
echo [4. Cleaning Python cache]
cd backend
if exist "__pycache__" (
    rmdir /s /q "__pycache__"
    echo OK Backend __pycache__ removed
)
if exist "app\__pycache__" (
    rmdir /s /q "app\__pycache__"
    echo OK Backend app __pycache__ removed
)
cd ..

echo.
echo =====================================
echo     Cache cleanup completed!
echo =====================================
echo.
echo Next: Run 'scripts\development\setup-dev.bat' to reinstall
echo.
