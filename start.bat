@echo off
where python >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Python is not installed or not in PATH
    pause
    exit /b 1
)

where pip >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo pip is not installed or not in PATH
    pause
    exit /b 1
)
for %%p in (yt_dlp) do (
    python -c "import %%p" >nul 2>&1
    if %ERRORLEVEL% equ 0 (
        echo Package %%p is already installed
    ) else (
        echo Installing %%p...
        pip install %%p
    )
)
cls
python ytdlp.py
pause