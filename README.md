# Omnipro-test

* python 3.10
* django 4.1.5
* django rest framework 3.14.0
* postgresql 15.1

# Base De Datos.

En la raiz del proyecto se encuentra un archivo .env con las variables de entorno para la base de datos, en este caso se
utilizo postgreSql.
si se quiere usar la bases de datos local, se debe comentar las credenciales de la base de datos remota en el archivo
.env y descomentar las credenciales de la base de datos local en el archivo .env,
si se quiere usar la base de datos remota, se deja el archivo .env como esta.



## Descripción

En la raiz del proyecto se encuentra una carpeta llamada "exercise", donde se encuentras los ejercicios propuestos del 1
al 4.
dentro de la carpeta "exercise" se encuentra una carpeta llamada "exercise_1", donde se encuentra el ejercicio 1, y asi
sucesivamente.
dentro de cada carpeta de ejercicio se encuentra un archivo .py, donde se encuentra el codigo de cada ejercicio, que se
debe ejecutar ("RUN") para ver el resultado.



## 5. Cosntruccion API

* se debe ejecutar el archivo "requirements.txt" para instalar las dependencias necesarias para el proyecto.
  `pip install -r requirements.txt`
* Dentro de la raiz del proyecto se encuentra una carpeta llamada "scripts", dentro de esta se encuentra un archivo .py
  llamado "seeds.py", el cual se debe ejecutar para crear los datos de prueba.
  `python scripts/seeds.py`

- al ejecutar el archivo "seeds.py":
    - se crean 10 paises.
    - se crean 5 estados por pais. (50 estados en total).
    - se crean 2 ciudades por estado. (100 ciudades en total).
    - se crean 8 tiendas.
    - se crean 10 clientes.
    - Los clientes con id 5,8,9 debe cambiar el nombre por Julián (el script debe ser secuencial)
    - Los clientes con id 1,7,6 debe tener la tienda con el id 5 como tienda favorita.

* ahora solo queda ejecutar el archivo "manage.py" para correr el proyecto.
  `python manage.py runserver`

[//]: # (subtitulo)

## Endpoints

http://127.0.0.1:8000/api/clients/ - GET, POST.
http://127.0.0.1:8000/api/clients/{id}/ - GET, PUT, DELETE.

http://127.0.0.1:8000/api/stores/ - GET, POST.
http://127.0.0.1:8000/api/stores/{id}/ - GET, PUT, DELETE.

http://127.0.0.1:8000/api/cities/ - GET, POST.
http://127.0.0.1:8000/api/cities/{id}/ - GET, PUT, DELETE.

http://127.0.0.1:8000/api/states/ - GET, POST.
http://127.0.0.1:8000/api/states/{id}/ - GET, PUT, DELETE.

http://127.0.0.1:8000/api/countries/ - GET, POST.
http://127.0.0.1:8000/api/countries/{id}/ - GET, PUT, DELETE.


[//]: # (subtitulo)




# omniprotest
