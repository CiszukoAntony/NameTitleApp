@echo off
setlocal
title NameTitleApp

:: 1. Verificar entorno virtual
if not exist ".venv\Scripts\python.exe" (
    echo [ERROR CRITICO] No se encuentra el archivo .venv\Scripts\python.exe
    goto :error
)

:: 2. Ejecutar pasando la ruta absoluta o controlada
.venv\Scripts\python.exe src/main.py

if %errorlevel% neq 0 (
    echo.
    echo [AVISO] El script termino con codigo de error: %errorlevel%
)