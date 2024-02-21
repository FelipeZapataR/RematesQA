# RematesQA
Proyecto diseñado con el fin de testear las caracteristicas de la pagina web reamtesQA.

## Instalación y Configuración

Este proyecto utiliza Poetry para la gestión de dependencias. Sigue los pasos a continuación para configurar tu entorno de desarrollo.

### Creación del Proyecto

1. **Crear un nuevo proyecto:**
   
   Utiliza Poetry para crear la estructura base del proyecto:
   
   ```bash
   poetry new rematesqa 
   ```

2. **Recrear *pyproject.toml***
    
   Editar el archivo es necesario para poder instalar las dependencias que se requieren en el proyecto

   ```bash
    [tool.poetry]
    name = "rematesqa"
    version = "0.1.0"
    description = ""
    authors = ["FelepeX"]
    readme = "README.md"

    [tool.poetry.dependencies]
    python = "^3.12"
    pyleniumio = "^1.20.0"

    [tool.poetry.group.dev.dependencies]
    autopep8 = "^2.0.4"
    flake8 = "^7.0.0"

    [build-system]
    requires = ["poetry-core"]
    build-backend = "poetry.core.masonry.api"
   ```
3. **Configurar el ambiente de VSCode**

    En command pallet de debe agregar el path de la maquina virtual el cual obtenemos con el comando
    ```bash
    poetry env info 
    ```
    Con este obtendremos el path de la maquina virtual el cual debemos reemplazar en el command pallet de VSCode especificamente en python: Select Interpreter donde deberemos pegar el path obtenido.
    
    Nuevamente ingresaremos al Command pallet de VSCode y configuramos python:Configure test y seleccionamos la carpeta test del proyecto

4. **inicializar Pylenium**

    Se debe correr un ultimo comando con el cual inicializaremos pylenium del proyecto

    ```bash
    poetry run pylenium init
    ```
