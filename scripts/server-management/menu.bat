@echo off
chcp 65001 >nul
echo.
echo ====================================
echo    COAI Server Management Menu
echo ====================================
echo.
echo Pasirinkite veiksmą:
echo.
echo 1. Paleisti serverius          (start-servers.bat)
echo 2. Sustabdyti serverius        (graceful-stop.bat)  
echo 3. Perkrauti serverius         (restart-servers.bat)
echo 4. Priverstinai sustabdyti     (kill-servers.bat)
echo 5. Tikrinti serverių būseną    (check-servers.bat)
echo 6. Stebėti procesus            (ps-check.bat)
echo 7. Konfigūracija               (config.bat)
echo 8. Dokumentacija               (README.md)
echo 9. Išeiti
echo.

set /p choice="Įveskite pasirinkimą (1-9): "

if "%choice%"=="1" (
    echo.
    echo Paleidžiami serveriai...
    call start-servers.bat
    goto menu
)

if "%choice%"=="2" (
    echo.
    echo Švelniai sustabdomi serveriai...
    call graceful-stop.bat
    goto menu
)

if "%choice%"=="3" (
    echo.
    echo Perkraunami serveriai...
    call restart-servers.bat
    goto menu
)

if "%choice%"=="4" (
    echo.
    echo Priverstinai sustabdomi serveriai...
    call kill-servers.bat
    goto menu
)

if "%choice%"=="5" (
    echo.
    echo Tikrinama serverių būsena...
    call check-servers.bat
    goto menu
)

if "%choice%"=="6" (
    echo.
    echo Stebimi procesai...
    call ps-check.bat
    goto menu
)

if "%choice%"=="7" (
    echo.
    echo Rodoma konfigūracija...
    call config.bat
    pause
    goto menu
)

if "%choice%"=="8" (
    echo.
    echo Atidaroma dokumentacija...
    start README.md
    goto menu
)

if "%choice%"=="9" (
    echo.
    echo Išeinama...
    exit /b 0
)

echo.
echo Neteisingas pasirinkimas! Bandykite dar kartą.
echo.

:menu
echo.
echo Grįžtama į meniu...
timeout /t 2 >nul
cls
goto :eof
