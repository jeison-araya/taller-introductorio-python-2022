# Create and configure the virtual enviroment for python3 with jupyter notebook.
# @Author: Jeison Araya Mena.
# @Date: 17/02/2021.
# @Email: jeison.arayamena@gmail.com

import os
import sys
import pip
import stat
import venv
import platform

from os import path
from shutil import rmtree

# Config.

venv_name = 'venv'
requirements_name = 'requirements.txt'
box_messages_border = ''
scripts_dir_name = ''

for x in range(50):
    box_messages_border += '='

def show_message(msg):
    print()
    print(box_messages_border)
    print(' ' + msg)
    print(box_messages_border)
    print()

def exec_command(command, get_output=False):
    if get_output:
        stream = os.popen(command)
        return stream.read()
    os.system(command)

def validate_python_version():
    if not sys.version_info.major == 3 and sys.version_info.minor >= 6:
        print('Python 3.6 o superior es necesario.')
        print('Usted está utilizando Python {}.{}.'.format(sys.version_info.major, sys.version_info.minor))
        sys.exit(1)

def venv_exist(venv_path):
    if path.exists(venv_path):
        if path.isdir(venv_path):
            return True
    return False

def file_exists(file_path):
    if path.exists(file_path):
        if path.isfile(file_path):
            return True
    return False

def create_venv(venv_path):
    venv.create(venv_path, clear=True, with_pip=True)
    
def update_venv(venv_path):
    global scripts_dir_name
    exec_command(path.join(venv_path, scripts_dir_name, 'pip install --upgrade pip --no-color'))    

def install_modules(venv_path, requirements_path):
    global scripts_dir_name
    exec_command(path.join(venv_path, scripts_dir_name, 'pip install -r {}'.format(requirements_path)))    

# Check python version.
validate_python_version()

# Check operative system.

operative_system = platform.system() 

if operative_system == 'Windows':
    scripts_dir_name = 'Scripts'
elif operative_system == 'Linux' or operative_system == 'Darwin':
    scripts_dir_name = 'bin'
else: 
    input('Error: Sistema operativo no soportado.')
    sys.exit(1)

# Paths 

dir_path = path.dirname(path.realpath(__file__))
venv_path = path.join(dir_path, venv_name)

# Init message.

show_message('Taller introductorio de pyton.')
print('Iniciando programa para crear y configurar el entorno virtual de programación (venv).')

# Check if there is an old venv.

if venv_exist(venv_path):
    print('Se encontró un entorno virtual.')
    print('Eliminando configuración existente...')

# Create venv

show_message('Creando entorno virtual')
print('Por favor, espere unos segundos...')
create_venv(venv_path)

if venv_exist(venv_path):
    print('Entorno virtual creado correctamente.')
else:
    input('Error: No se ha creado el entorno virtual.')
    sys.exit(1)  

# Update venv

show_message('Actualizando el sistema gestor de paquetes (pip)...')
update_venv(venv_path)
print('Se ha actualizado pip correctamente.')

# Install modules required.

requirements_path = path.join(dir_path, requirements_name)

show_message('Instalando dependencias.')

if file_exists(requirements_path):
    print('Archivo de dependencias encontrado.')
    print('Instalando dependencias...')
    install_modules(venv_path, requirements_path)
    print('Dependencias instaladas correctamente.')
else:
    print('No se requiere instalar ninguna dependencia.')

show_message('Entorno virtual configurado y listo para ser utilizado.')

input('Presione Enter para finalizar...')