#install el proyecto
poetry new (nombre del proyecto)
se debe eliminar el archivo pyproject.toml
poetry init para crear un nuevo archivo con las dependencias requeridas
en poetry.dependencies seleccionar pyleniumio
y en poetry.group.dev.dependencies autopep8 flake8
ejecutar poetry env info para obtener el path de la maquina virutal y agregarlo a command pallet del proyecto y agregar ese enlace a python: select interpreter
en command pallet nuevamente ingresar a python: configure test y seleccionar la carpeta test del proyecto
correr en la consola de comando poetry run pylenium init para inicializar el proyecto
