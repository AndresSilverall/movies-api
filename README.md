#Movies API REST

API basada en la arquitectura REST, la cual permitirá listar diferentes películas, agregar reseñas y almacenar las películas favoritas del usuario. La API cuenta con un sistema de autenticación (Registro, login y logout) y otorga diferentes permisos a los usuarios para acceder a los endpoints, desarrollada con Django Rest Framework.


## Tecnologías usadas

- Python versión 3.8.5
- Django rest framework versión 3.14.0
- IDE (Visual studio code)
- GIT versión 2.37.2.windows.2


## Instalación

1. Clona este repositorio: `https://github.com/AndresSilverall/movies-api.git`
2. Navega a la carpeta del proyecto: `cd movies-api`
3. Ejecuta un entorno virtual de Python para la ejecución de la App


### Instalar un entorno virtual en Python 

- Instalar desde el gestor de paquetes de Python: `pip install pipenv`.
- Crear un entorno virtual: `pipenv install`.
- Una vez ya creado el entorno virtual con `pipenv install` se instalará todas las dependencias necesarias para la API alojadas en el archivo `Pipfile`.
- Activar entorno virtual: `pipenv shell`.
- Para salir del entorno virtual: `exit`.


4. Ejecuta el servidor de desarrollo: `python manage.py runserver`
5. Abre tu navegador y ve al siguiente endpoint: `http://127.0.0.1:8000/api/movies`


### Atajos de comandos dentro del entorno virtual

```python
server = "python manage.py runserver 127.0.0.1:8000"
make = "python manage.py makemigrations"
migrate = "python manage.py migrate"

```

- Ejecutar servidor `pipenv run server`
- Realizar migraciones de los modelos `pipenv run make`
- Migrar modelos `pipenv run migrate`