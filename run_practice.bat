@echo off
REM Double-click this file to auto-generate and push 3-4 new
REM Python practice solutions to your python-daily-practice repo.

cd /d "%~dp0"

echo Running daily practice generator...
echo.

python generate_and_push.py
if errorlevel 1 (
    echo.
    echo Something went wrong - see the messages above.
) else (
    echo.
    echo All done - check GitHub to see the new commits.
)

echo.
pause
