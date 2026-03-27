@echo off
echo ========================================
echo  Sachin's Portfolio - Startup Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo [✓] Python found
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo [*] Creating virtual environment...
    python -m venv venv
    echo [✓] Virtual environment created
)

REM Activate virtual environment
echo [*] Activating virtual environment...
call venv\Scripts\activate.bat
echo [✓] Virtual environment activated
echo.

REM Install/Update dependencies
echo [*] Installing dependencies...
pip install -r requirements.txt >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)
echo [✓] Dependencies installed
echo.

REM Run the server
echo [*] Starting Flask server...
echo ========================================
echo Portfolio server running at:
echo http://localhost:5000
echo.
echo Admin panel at:
echo http://localhost:5000/admin
echo ========================================
echo.
python server.py

pause
