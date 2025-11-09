@echo off
REM -----------------------------------------
REM run_hypercontrol_elevated.bat
REM - Elevates via UAC if not admin, then runs the Python script in this folder.
REM - Place this file in the same folder as remote_controller_full.py
REM -----------------------------------------

:: Check for admin by trying a privileged command
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Requesting Administrator privileges...
    powershell -Command "Start-Process -FilePath '%~f0' -Verb RunAs"
    exit /b
)

:: We are running as admin now
title HyperControl - Running
cd /d "%~dp0"

echo ===============================
echo Starting HyperControl...
echo (Press Ctrl+C to stop)
echo ===============================

:: Use 'python' from PATH. If you want to force a specific python.exe, replace 'python' with full path:
:: "C:\Path\To\Python\python.exe" remote_controller.py

python remote_controller.py

echo Script exited. Press any key to close.
pause >nul
