@echo off
chcp 65001 >nul
echo.
echo =====================================
echo     COAI Development Setup
echo =====================================
echo.

echo [1. Installing root dependencies]
call npm install
if %errorlevel%==0 (
    echo OK Root dependencies installed
) else (
    echo ERROR Failed to install root dependencies
    goto :end
)

echo.
echo [2. Installing frontend dependencies]
cd frontend
call npm install
if %errorlevel%==0 (
    echo OK Frontend dependencies installed
) else (
    echo ERROR Failed to install frontend dependencies
    cd ..
    goto :end
)
cd ..

echo.
echo [3. Installing backend dependencies]
cd backend
call pip install -r requirements.txt
if %errorlevel%==0 (
    echo OK Backend dependencies installed
) else (
    echo ERROR Failed to install backend dependencies
    cd ..
    goto :end
)
cd ..

echo.
echo =====================================
echo     Setup completed successfully!
echo =====================================
echo.
echo Next steps:
echo 1. Run 'npm run dev' to start servers
echo 2. Open http://localhost:3000 for frontend
echo 3. Open http://localhost:5000 for backend
echo.

:end
