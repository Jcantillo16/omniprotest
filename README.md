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

## Validaciones y Automatizaciones

se crearon 5 apps para la construccion de la API, las cuales son:

- client
- store
- country
- city
- state
-

### Client

- esta app se encarga de la creacion de los clientes,
- y valida que los estados y ciudades que se le asignen, tengan relacion con el pais que se le asigno al cliente.
- tambien valida que el cliente tenga una tienda favorita, y que esta tienda exista.
- valida que la ciudad tenga relacion con el estado y el estado con el pais.

### Store

- esta app se encarga de la creacion de las tiendas,
- esta app genera de forma automatica un codigo de tienda, el cual es unico para cada tienda.
- el codigo de tienda se genera de la siguiente manera:
    - el codigo de tienda esta compuesto por 3 letras mayusculas y 3 numeros.
    - las letras se generan de 3 primeras letras del nombre de la tienda.
    - los numeros se generan de forma aleatoria.
    - el codigo de tienda no puede repetirse.

** Los modelos de Country, City y State, se encuentran en la misma app "country", ya que estos modelos son de uso
general para las demas apps.

### Country

- esta app se encarga de la creacion de los paises,
- esta app genera de forma automatica un codigo de pais, el cual es unico para cada pais.
- el codigo de pais se genera de la siguiente manera:
    - el codigo de pais esta compuesto por 3 letras mayusculas y 3 numeros.
    - las letras se generan de 3 primeras letras del nombre del pais.
    - los numeros se generan de forma aleatoria.
    - el codigo de pais no puede repetirse.

### City

- esta app se encarga de la creacion de las ciudades,
- esta app genera de forma automatica un codigo de ciudad, el cual es unico para cada ciudad.
- el codigo de ciudad se genera de la siguiente manera:
    - el codigo de ciudad esta compuesto por 3 letras mayusculas y 3 numeros.
    - las letras se generan de 3 primeras letras del nombre de la ciudad.
    - los numeros se generan de forma aleatoria.
    - el codigo de ciudad no puede repetirse.
      -se valida que la ciudad tenga relacion con el estado y el estado con el pais.

### State

- esta app se encarga de la creacion de los estados,
- esta app genera de forma automatica un codigo de estado, el cual es unico para cada estado.
- el codigo de estado se genera de la siguiente manera:
    - el codigo de estado esta compuesto por 3 letras mayusculas y 3 numeros.
    - las letras se generan de 3 primeras letras del nombre del estado.
    - los numeros se generan de forma aleatoria.
    - el codigo de estado no puede repetirse.

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

## Documentacion API

https://documenter.getpostman.com/view/18241310/2s8Z73yr6L






