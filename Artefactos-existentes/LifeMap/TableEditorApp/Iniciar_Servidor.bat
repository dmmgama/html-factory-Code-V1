@echo off
cd /d "%~dp0"
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8

REM 1) Arrancar o servidor (8765) numa janela propria — nao bloqueia este .bat.
REM    O env (PYTHONUTF8) e herdado pela janela nova.
where py >nul 2>nul && ( start "TableEditor Server" py acc_server.py & goto :openapp )
where python >nul 2>nul && ( start "TableEditor Server" python acc_server.py & goto :openapp )
echo ERRO: Python nao encontrado no PATH. Instala Python (ou o launcher py).
pause
goto :eof

:openapp
REM 2) Esperar ~2s o servidor arrancar e abrir a app no browser (file://).
timeout /t 2 /nobreak >nul
start "" "%~dp0MembrosInfo_Editor.html"
