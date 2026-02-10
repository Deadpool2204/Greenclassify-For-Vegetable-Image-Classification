@echo off
REM GreenClassify Setup Script for Windows
REM This script sets up the Python environment and installs dependencies

echo ========================================
echo GreenClassify - Setup Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo [✓] Python detected
python --version
echo.

REM Create virtual environment
echo [*] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)
echo [✓] Virtual environment created
echo.

REM Activate virtual environment
echo [*] Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)
echo [✓] Virtual environment activated
echo.

REM Upgrade pip
echo [*] Upgrading pip...
python -m pip install --upgrade pip
echo [✓] pip upgraded
echo.

REM Install requirements
echo [*] Installing dependencies...
echo This may take a few minutes...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    echo Try running: pip install --no-cache-dir -r requirements.txt
    pause
    exit /b 1
)
echo [✓] Dependencies installed
echo.

REM Display next steps
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Run the Flask app:
echo    python app.py
echo.
echo 2. Open your browser:
echo    http://localhost:5000/
echo.
echo To deactivate the virtual environment later, run:
echo    deactivate
echo.
pause
