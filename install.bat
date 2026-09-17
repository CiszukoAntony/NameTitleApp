@echo off
echo ==========================================
echo Verificando dependencias de entorno...
echo ==========================================

:: Verificar si uv está instalado, si no, instalarlo usando pip
python -m uv --version >nul 2>&1
if errorlevel 1 (
    echo uv no esta instalado. Instalandolo con pip...
    pip install uv
)

echo ==========================================
echo Instalando NameTitleApp con uv...
echo ==========================================

:: Instalar dependencias con uv (mucho mas rapido)
uv pip install -r requirements.txt
uv pip install -e .

echo ==========================================
echo ¡Instalacion completada con exito!
echo Ya puedes usar el comando: titlename
echo ==========================================
pause