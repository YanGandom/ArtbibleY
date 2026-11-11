@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if not errorlevel 1 (
  py -3 package_release.py
  goto finish
)
if exist "%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" (
  "%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" package_release.py
  goto finish
)
where python >nul 2>nul
if not errorlevel 1 (
  python package_release.py
  goto finish
)
echo Python 3 is required. Please install Python 3 and try again.
:finish
pause
