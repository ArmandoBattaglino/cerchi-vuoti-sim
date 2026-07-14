@echo off
REM ==========================================================================
REM  avvia-lab.bat — Avvia il lanciatore Python del Void Lab e apre il browser.
REM  Porta opzionale come primo argomento (default 8777).
REM ==========================================================================
setlocal
cd /d "%~dp0"

set PORT=%1
if "%PORT%"=="" set PORT=8777

REM Avvia il server in una finestra separata (resta aperto a servire).
start "Void Lab server" cmd /k python "%~dp0avvia-lab.py" %PORT%

REM Attende che il server sia su, poi apre la pagina di test dello STRATO A.
timeout /t 2 /nobreak >nul
start "" "http://127.0.0.1:%PORT%/dati-test.html"

endlocal
