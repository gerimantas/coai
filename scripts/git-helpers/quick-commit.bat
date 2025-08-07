@echo off
echo.
echo =====================================
echo     Quick Git Commit
echo =====================================
echo.

if "%1"=="" (
    echo Usage: quick-commit.bat "commit message"
    echo Example: quick-commit.bat "fix frontend bug"
    goto :end
)

echo [1. Checking git status]
git status

echo.
echo [2. Adding all changes]
git add .

echo.
echo [3. Committing with message: %1]
git commit -m "%1"

echo.
echo [4. Pushing to remote]
git push

echo.
echo =====================================
echo     Quick commit completed!
echo =====================================

:end
