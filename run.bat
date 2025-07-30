@echo off
cd /d "%~dp0"

:main
cls
echo --------------------------------------
echo Starting Streamlit app...
echo --------------------------------------

start /b streamlit run app.py

:menu
echo.
echo --------------------------------------
echo [R] Reload the app
echo [C] Close the app
echo --------------------------------------
choice /c RC /n /m "Your choice (R/C): "
if errorlevel 2 (
    taskkill /f /im streamlit.exe >nul 2>&1
    echo Streamlit closed.
    exit
)
if errorlevel 1 (
    taskkill /f /im streamlit.exe >nul 2>&1
    goto main
)
