<a href="https://www.python.org">
    <img src="https://icon-icons.com/icons2/2107/PNG/128/file_type_python_icon_130221.png" alt="Python logo" title="Python" align="right" height="72"/>
</a>

## Configuración de entorno virtual para el Taller introductorio a Python

**¿Qué es un entorno virtual de python?**




Para más información sobre entorno virtuales en python puede consultar los siguientes enlaces:
* [venv - Creation of virtual environments.](https://docs.python.org/3/library/venv.html)
* [Tutorial de Python: virtualenv y por qué deberías utilizar entornos virtuales.](https://www.youtube.com/watch?v=N5vscPTWKOk)


En este apartado se encuentran las instrucciones para crear y configurar un entorno virtual de python 3.8 o superior. Debe seguir los pasos según el sistema operativo que tenga instalado en su computadora.

---
<img src="https://cdn.icon-icons.com/icons2/836/PNG/512/Windows_Phone_icon-icons.com_66782.png" alt="Windows OS" title="Windows Logo" align="right" height="32"  style="margin: 30px" />

### Pasos para configurar un entorno virtual en Windows

**📌Opción 1:**

* Abra la carpeta donde se encuentran los archivos del taller <small>(carpeta descrompimida en el paso 4 de la guía de instalación) </small>

* Luego, ejecute el archivo `venv_installer.py`.

    <a href="static\venv_installer_icon.png">
        <img src="static\venv_installer_icon.png" alt="Venv installer" title="Python"/>
    </a>

    * Nota: Asegurese de tener instalado python 3.8 o superior para realizar este paso. En caso de presentarse algún error, vuelva a realizar el paso 1  de la guía de instalación.

* Este programa se encarga de:
    1. Crear un entorno virtual, dentro de la carpeta donde están los archivos del taller:
    
        <a href="static\venv_installer_o1.png">
            <img src="static\venv_installer_o1.png" alt="Venv installer" title="Python"/>
        </a>
    <br>

    2. Actualizar el sistema de gestor de paquetes (pip):
    
        <a href="static\venv_installer_o2.png">
            <img src="static\venv_installer_o2.png" alt="Venv installer output" title="Python"/>
        </a>
        
        <small>Nota: En caso de encontrarse con un mensaje de error como el marcado en la imagen anterior, proceda a omitirlo ya que no es fundamental para el propósito del taller.</small>
    <br>

    3. Instalar las dependencias contenidas en el archivo `requirements.txt`:
        <a href="static\venv_installer_o3.png">
            <img src="static\venv_installer_o3.png" alt="Venv installer output" title="Python"/>
        </a>
    
    Una vez finalizada la instalación de las dependencias, debe obtener el siguiente mensaje.
        
    <a href="static\venv_installer_o4.png">
        <img src="static\venv_installer_o4.png" alt="Venv installer output" title="Python"/>
    </a>

    Como resultado se crea un nuevo directorio llamado `venv`, el cual contiene una versión de Python independiente a la instalada en el sistema.

    <a href="static\venv_installer_o5.png">
        <img src="static\venv_installer_o5.png" alt="Venv installer output" title="Python" align="center"/>
    </a>

    De esta forma se concluye con la instalación del entorno virtual. En caso de tener dudas o inconvenientes, puede comunicarse con los desarrolladores del taller.
    
**📌Opción 2:**

Siga los siguientes pasos para crear y configurar el entorno virtual de forma manual. 

**⚙️ Crear entorno virtual:**

* Abrir una [terminal CMD](), con permisos de administrador, donde se encuentra los archivos del  [taller-introductorio-python-2021](https://github.com/jeison-araya/taller-introductorio-python-2021/archive/main.zip "taller-introductorio-python-2021").
* Ejecute el siguiente comando:
`python -m venv venv`. Esta instrucción creará un nuevo directorio llamado `venv` con los archivos relacionados con el entorno virtual que se va a utilizar en este taller.
    * Para activar el entorno virtual debe ingresar el siguiente comando: `.\venv\Scripts\activate.bat`.
* Una vez creado el entorno virtual, se debe instalar los módulos necesarios para el desarrollo de este taller.

**⚙ Instalar módulos requeridos:**

* Antes de instalar los módulos se recomienda actualizar el sistema gestor de paquetes de python ([pip](https://pypi.org/project/pip/ "pip")), para esto se debe ejecutar el siguiente comando: `pip install --upgrade pip`
* Los módulos necesarios para este taller, se encuentran listados en el archivo `requirements.txt`. Al ejecutar el comando `pip install -r requirements.txt`, el sistema gestor de paquetes ([pip](https://pypi.org/project/pip/ "pip")), instalará todos los módulos que contiene este archivo.
---

<div   style="margin: 30px">
    <img src="https://cdn.icon-icons.com/icons2/1/PNG/256/social_apple_mac_65.png" alt="Linux OS" title="Linux penguin" align="right" height="32"  style="margin: 5px" />
    <img src="https://cdn.icon-icons.com/icons2/46/PNG/128/linux_penguin_animal_9362.png" alt="Linux OS" title="Linux penguin" align="right" height="32" style="margin: 5px" />
</div>

### Pasos para configurar un entorno virtual en Linux y MacOS

**⚙️ Crear entorno virtual:**

* Abrir una [terminal de comandos](), con permisos de administrador, donde se encuentra los archivos del  [taller-introductorio-python-2021](https://github.com/jeison-araya/taller-introductorio-python-2021/archive/main.zip "taller-introductorio-python-2021").
* Ejecute el siguiente comando:
`python3 -m venv venv`. Esta instrucción creará un nuevo directorio llamado `venv` con los archivos relacionados con el entorno virtual que se va a utilizar en este taller.
    * Para activar el entorno virtual debe ingresar el siguiente comando: `source venv/bin/activate`.
* Una vez creado el entorno virtual, se debe instalar los módulos necesarios para el desarrollo de este taller.

**⚙ Instalar módulos requeridos:**

* Antes de instalar los módulos se recomienda actualizar el sistema gestor de paquetes de python ([pip](https://pypi.org/project/pip/ "pip")), para esto se debe ejecutar el siguiente comando: `pip install --upgrade pip`
* Los módulos necesarios para este taller, se encuentran listados en el archivo `requirements.txt`. Al ejecutar el comando `pip install -r requirements.txt`, el sistema gestor de paquetes ([pip](https://pypi.org/project/pip/ "pip")), instalará todos los módulos que contiene este archivo.