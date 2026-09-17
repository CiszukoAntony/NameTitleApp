@echo off
echo ==========================================
echo Compilando nueva version de NameTitleApp...
echo ==========================================

pyinstaller --onedir --icon="public/images/icon.ico" --version-file="file_version_info.txt" --console --hidden-import=typer --hidden-import=rich --paths=src src/main.py --name nametitle --clean

echo ==========================================
echo ¡Compilacion finalizada! Revisa la carpeta dist/
echo ==========================================
pause