@echo off
cd /d "%~dp0"
git add .
git commit -m "Daily Python Practice"
git push
pause