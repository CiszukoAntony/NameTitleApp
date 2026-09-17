@echo off
echo ==========================================
echo Instalando TitleNameApp localmente...
echo ==========================================

:: Instalar las dependencias del requirements.txt
pip install -r requirements.txt

:: Instalar el paquete actual en modo editable/desarrollo con pip
pip install -e .

echo ==========================================
echo ¡Instalacion completada con exito!
echo Ya puedes usar el comando: titlename
echo ==========================================
pause