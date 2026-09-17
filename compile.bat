@echo off
echo ==========================================
echo Compilando nueva version de NameTitleApp...
echo ==========================================

pyinstaller --onefile --name nametitleapp src/main.py --clean

echo ==========================================
echo ¡Compilacion finalizada! Revisa la carpeta dist/
echo ==========================================
pause