:: Create and configure the virtual enviroment for python3 with jupyter notebook.
:: @Author: Jeison Araya Mena.
:: @Date: 02/02/2021.
:: @Email: jeison.arayamena@gmail.com
@echo off
title Configuracion de entorno virtual.
cls
color 02 
echo =====================================
echo   Taller introductorio Python 2021.  
echo =====================================
echo.
:: Set Directory.
set my_path=%~dp0
set my_path=%my_path:~0, -1%
:: Check python version.
set "temp_path=%my_path%\temp.txt"
call python --version > %temp_path%
set /p python_version=< %temp_path%
del %temp_path%
echo Version de python: %python_version%
echo.
:: Create python venv
echo Creando entorno virtual...
set "venv_path=%my_path%\venv"
call python -m venv %venv_path%
:: Check venv folder
if exist %venv_path% (
    echo Entorno virtual creado correctamente
    echo Directorio del entorno virtual: %venv_path%
    echo.
) else (
    echo Error al crear el entorno virtual.
    goto end
)
:: Activate venv
echo Iniciando entorno virtual...
echo.
call %venv_path%\Scripts\activate.bat
:: Update pip
echo Actualizando gestor de paquetes de python (pip)...
call pip install --upgrade pip
color 02 
echo.
:: Check requirements file
echo =====================================
echo   Comprobando modulos requeridos... 
echo =====================================
echo.
set "requirements_path=%my_path%\requirements.txt"
if exist %requirements_path% (
    :: Install modules required
    echo Instalando modulos adicionales...
    echo.
    call pip install -r %requirements_path%
) else (
    echo No se necesitan modulos adicionales.
    echo.
    goto end
)
echo.
echo ==============================================
echo El entorno virtual configurado correctamente!
echo ==============================================
echo.
:End
pause
