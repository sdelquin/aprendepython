---
icon: material/engine-outline
---

# Puesta en marcha { #setup }

<span class="djversion basic">:simple-django: Básico :material-tag-multiple-outline:</span>

## Entorno de trabajo { #workspace }

Suponiendo que disponemos de [Python](../../../core/devenv/real-context.md#python) ya instalado en nuestra máquina, debemos configurar ciertos aspectos para preparar el entorno de desarrollo de **Django**.

### Carpeta del proyecto { #project-folder }

Supongamos que el proyecto se va a llamar `matraka`. Crearemos una carpeta con dicho nombre:

```console
$ mkdir matraka
$ cd matraka
```

### Entorno virtual { #virtualenv }

Es altamente recomendable utilizar un [entorno virtual](../../../core/devenv/real-context.md#virtualenvs) a la hora de comenzar cualquier proyecto Python. Django no iba a ser un caso especial.

Una vez ==dentro de la carpeta del proyecto== vamos a crear el citado entorno virtual. Para ello haremos lo siguiente:

```console
$ python -m venv .venv --prompt matraka 
```

!!! danger "Carpeta del proyecto"

    Es importante que estemos dentro de la carpeta del proyecto cuando creemos el entorno virtual.

#### Activar el entorno virtual { #activate-venv }

Para activar el entorno virtual usamos el siguiente comando:

```console
$ source .venv/bin/activate
```

:material-check-all:{ .blue } Cuando el entorno virtual está activado, suele aparecer el nombre del «prompt» del proyecto entre paréntesis delante del símbolo del sistema:

```console
(matraka)$ 
```

!!! tip "Recuerda activar"

    Todas las intervenciones que hagamos durante el desarrollo del proyecto requieren tener el entorno virtual activado para disponer de las distintas librerías y paquetes previamente instaladas. ¡Recuerda activar el entorno virtual!

#### Desactivar el entorno virtual { #desactivate-venv }

Para desactivar el entorno virtual basta con ejecutar el siguiente comando:

```console
$ deactivate
```

## Nuevo proyecto { #new-project }

Suponiendo que ya hemos [creado la carpeta](#project-folder) y el [entorno virtual](#virtualenv) vamos a crear un **nuevo proyecto Django**.

### Instalación de dependencias { #install-dependencies }

[Activamos el entorno virtual](#activate-venv) e ^^instalamos^^ el paquete _Django_:

```console
$ pip install django
```

!!! tip "Recuerda activar"

    Todas las intervenciones que hagamos durante el desarrollo del proyecto requieren tener el entorno virtual activado para disponer de las distintas librerías y paquetes previamente instaladas. ¡Recuerda activar el entorno virtual!

### Creación del proyecto { #create-project }

Cuando instalamos Django, este paquete ofrece un ejecutable llamado `django-admin`

Supongamos que el proyecto se va a llamar `matraka` y que ya estamos dentro de una carpeta llamada `matraka`.

Para crear el proyecto lanzamos el siguiente comando:

```console
$ django-admin startproject main . 
```

El proyecto habrá quedado con la siguiente estructura:

```python
.
├── main
│   ├── __init__.py#(1)!
│   ├── asgi.py#(2)!
│   ├── settings.py#(3)!
│   ├── urls.py#(4)!
│   └── wsgi.py#(5)!
└── manage.py#(6)!
```
{ .annotate }

1. Identifica la carpeta como un paquete Python.
2. Configuraciones para el servidor de aplicación ASGI.
3. Configuraciones del propio proyecto.
4. URLs de primer nivel.
5. Configuraciones para el servidor de aplicación WSGI.
6. Herramienta (manejador) para gestión del proyecto.

## Primer arranque { #first-launch }

Para verificar que todo está en orden podemos comprobar el estado del proyecto con el siguiente comando:

```console
$ ./manage.py check
```

Antes de «levantar» nuestro proyecto Django por primera vez, necesitamos aplicar las migraciones. En este punto podemos entender que hay una serie de acciones a llevar a cabo en la base de datos para que Django pueda disponer de una estructura sobre la que trabajar.

Para ello ejecutamos el siguiente comando:

```console
$ ./manage.py migrate
```

Ahora ya estamos en disposición de levantar el servidor de desarrollo de Django:

```console
$ ./manage.py runserver
```

Siempre y cuando no haya surgido algún inconveniente de última hora, con esto ya tendremos accesible el proyecto en la URL http://127.0.0.1:8000/

!!! question "Detener el servidor"

    Para detener el servidor de desarrollo basta con pulsar ++ctrl+c++

### Interfaz administrativa { #admin }

Django nos ofrece una **interfaz administrativa** para poder interactuar con la base de datos.

Lo primero será crear una cuenta de «superusuario» mediante el subcomando `createsuperuser`:

```console
$ ./manage.py createsuperuser
Username (leave blank to use 'sdelquin'): admin
Email address: admin@example.com
Password:
Password (again):
Superuser created successfully.
```

Ahora ya podremos acceder a la **interfaz administrativa**[^3] en la URL http://127.0.0.1:8000/admin/ con las credenciales anteriores.

## Control de versiones { #version-control }

Es muy habitual usar un sistema de control de versiones sobre los proyectos de desarrollo de software. Más concretamente [git](https://git-scm.com/) se ha convertido es un estándar «de-facto» en el mundo del desarrollo.

Para crear un nuevo repositorio, usaremos el siguiente comando:

```console
$ git init
```

### Ignorando archivos { #ignoring-files }

Es fundamental **excluir ciertos archivos** del sistema de control de versiones. Para ello es necesario crear un fichero `.gitignore` en el raíz de nuestro proyecto.

Aunque existen [plantillas prediseñadas `.gitignore`](https://github.com/github/gitignore) para cada tipo de proyecto, a continuación se muestra un contenido mínimo para un proyecto Django:

```title=".gitignore"
.venv(1)
db.sqlite3(2)
*.pyc(3)
.mypy_cache(4)
```
{ .annotate }

1. Carpeta que contiene el [entorno virtual](#virtualenv).
2. Nombre (por defecto) de la base de datos [sqlite](../../../stdlib/data-access/sqlite.md) en Django.
3. Ficheros con [«bytecode»](../../../core/introduction/machine.md#compilers) compilado de Python.
4. Caché de [mypy](https://mypy-lang.org/) (si procede).

## Requerimientos { #requirements }

Para que los proyectos (Python) puedan ser reproducibles en otros entornos (por ejemplo en producción) es altamente recomendable añadir un fichero con los requerimientos.

Este fichero se suele denominar `requirements.txt` y contiene una línea por cada paquete/librería Python que utilicemos en el proyecto.

En el caso de un proyecto Django, inicialmente sólo tendremos este requerimiento[^1]:

```title="requirements.txt"
django
```

Pero también es posible fijar[^2] la versión exacta del paquete que estamos utilizando. Esto ayuda a que sea más fácil reproducir el proyecto en otro entorno.

Para añadir el número de versión al fichero de requisitos simplemente lo agregamos a cada línea:

```title="requirements.txt"
django==5.1.1
```

Una forma más «directa» de hacer esto es mediante utilidades de línea de comandos:

```console
$ pip freeze | grep -i django >> requirements.txt
```

## Lanzando comandos { #lauch-commands }

[just](https://github.com/casey/just) es un lanzador de comandos. Aunque no es necesario para desarrollar proyectos software, es altamente recomendable incluirlo porque permite automatizar muchas tareas que son habituales en el día a día.

Basta con tener [instalada la herramienta](https://github.com/casey/just?tab=readme-ov-file#pre-built-binaries) y crear un fichero `justfile` en el raíz de nuestro proyecto.
Este fichero se compone de «recetas» identificadas por un nombre que luego podemos ejecutar desde línea de comandos.

A continuación se muestra un <span class="example">ejemplo:material-flash:</span> ^^mínimo^^ de `justfile` para un proyecto Django:

```makefile
# Levantar el servidor de desarrollo
dev:
    ./manage.py runserver

# Comprobar el proyecto Django
check:
    ./manage.py check
```

Si queremos levantar el servidor de desarrollo basta con ejecutar:

```console
$ just dev
```

O simplemente `just` ya que la primera receta es la _receta por defecto_.

!!! tip "Alias"

    Un `alias j=just` suele ser interesante ya que nos permite «ahorrar» aún más en la escritura de las recetas.



[^1]: También se denominan **dependencias** del proyecto.
[^2]: Viene del verbo «pin» en inglés.
[^3]: La interfaz administrativa ha sido generada por Django sin escribir una sola línea de código adicional.
