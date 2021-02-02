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
:: Check python version.
call python3 --version > temp.txt
set /p python_version=<temp.txt
del temp.txt
echo Version de python: %python_version%
echo.
:: Create python venv
echo Creando entorno virtual...
call python3 -m venv venv
:: Check venv folder
if exist venv (
    echo Entorno virtual creado correctamente!
    echo.
) else (
    echo Error al crear el entorno virtual.
    goto end
)
:: Activate venv
echo Iniciando entorno virtual...
echo.
call .\venv\Scripts\activate.bat
:: Update pip
echo Actualizando gestor de paquete de python (pip)...
call pip install --upgrade pip
color 02 
echo.
:: Check requirements file
echo Comprobando modulos requeridos...
echo.
if exist requirements.txt (
    :: Install modules required
    echo Instalando modulos adicionales...
    echo.
    call pip install -r requirements.txt
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