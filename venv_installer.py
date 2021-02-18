# Create and configure the virtual enviroment for python3 with jupyter notebook.
# @Author: Jeison Araya Mena.
# @Date: 17/02/2021.
# @Email: jeison.arayamena@gmail.com

import os
import sys
import pip
import venv
import platform

from os import path
from shutil import rmtree

# Configuration.

venv_dir_name = 'venv'
scripts_dir_name = ''
box_messages_border = ''
requirements_file_name = 'requirements.txt'

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
    if sys.version_info.major != 3 and sys.version_info.minor <= 7:
        print('Python 3.7 o superior es necesario.')
        print('Usted está utilizando Python {}.{}.'.format(sys.version_info.major, 
                                                           sys.version_info.minor))
        sys.exit(1)

def validate_os():
    global scripts_dir_name
    operative_system = platform.system() 

    if operative_system == 'Windows':
        # Windows.
        scripts_dir_name = 'Scripts'
    elif operative_system == 'Linux' or operative_system == 'Darwin':
        # Linux and Mac.
        scripts_dir_name = 'bin'
    else: 
        # Other os.
        input('Error: Sistema operativo no soportado.')
        sys.exit(1)
        
def dir_exist(dir_path):
    return path.exists(dir_path) and path.isdir(dir_path)

def file_exists(file_path):
    return path.exists(file_path) and path.isfile(file_path)

def create_venv(venv_path):
    venv.create(venv_path, clear=True, with_pip=True)
    
def update_venv(venv_path):
    global scripts_dir_name
    exec_command(path.join(venv_path, scripts_dir_name, 'pip install --upgrade pip --no-color'))    

def install_modules(venv_path, requirements_path):
    global scripts_dir_name
    # Verify if file exists.
    if file_exists(requirements_path):
        print('Archivo de dependencias encontrado.')
        print('Instalando dependencias...')
        exec_command(path.join(venv_path, scripts_dir_name, 
                               'pip install -r {}'.format(requirements_path)))    
    else:
        print('No se requiere instalar ninguna dependencia.')

def validate_modules_required(venv_path, requirements_path):
    global scripts_dir_name
    if file_exists(requirements_path):
        # Get modules required
        file = open(requirements_path, "r")
        modules_required = file.read()
        # Get modules installed
        modules_installed = exec_command(path.join(venv_path, scripts_dir_name, 'pip freeze'), 
                                                   get_output=True)    
        return modules_installed == modules_required
    else:
        # Dependencies are not required.
        return True
    
# Check python version.

validate_python_version()

# Check operative system.

validate_os()

# Paths 

dir_path = path.dirname(path.realpath(__file__))
venv_path = path.join(dir_path, venv_dir_name)

# Init message.

show_message('Taller introductorio de pyton.')
print('Iniciando programa para crear y configurar el entorno virtual de programación (venv).')

# Check if there is an old venv.

if dir_exist(venv_path):
    print('Se encontró un entorno virtual.')
    print('Eliminando configuración existente...')

# Create venv

show_message('1. Creando entorno virtual')
print('Por favor, espere unos segundos...')
create_venv(venv_path)

if dir_exist(venv_path):
    print('Entorno virtual creado correctamente.')
else:
    input('Error: No se ha creado el entorno virtual.')
    sys.exit(1)  

# Update venv

show_message('2. Actualizando sistema gestor de paquetes (pip)...')
update_venv(venv_path)
print('Se ha actualizado pip correctamente.')

# Install modules required.

requirements_path = path.join(dir_path, requirements_file_name)

show_message('3. Instalando dependencias.')
install_modules(venv_path, requirements_path)
if validate_modules_required(venv_path, requirements_path):
    print('Las dependencias necesarias han sido instaladas.')
else:
    print('No se han logrado instalar todas las dependencias.')

# End message.

show_message('Entorno virtual configurado y listo para ser utilizado.')

input('Presione Enter para finalizar...')