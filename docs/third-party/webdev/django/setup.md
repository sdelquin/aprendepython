---
icon: material/engine-outline
---

# Puesta en marcha { #setup }

<span class="djversion basic">:simple-django: Básico :material-tag-multiple-outline:</span>

## Entorno de trabajo { #workspace }

Suponiendo que disponemos de [Python](../../../core/devenv/real-context.md#python) ya instalado en nuestra máquina, debemos configurar ciertos aspectos para preparar el entorno de desarrollo de **Django**.

### Carpeta del proyecto { #project-folder }

Imaginemos que el proyecto se va a llamar `blog`. Crearemos una carpeta con dicho nombre:

```console
$ mkdir blog
$ cd blog
```

### Entorno virtual { #virtualenv }

Es altamente recomendable utilizar un [entorno virtual](../../../core/devenv/real-context.md#virtualenvs) a la hora de comenzar cualquier proyecto Python. Django no iba a ser un caso especial.

=== "*venv* :octicons-package-24:{.blue}"

    Una vez ==dentro de la carpeta del proyecto== vamos a crear el citado entorno virtual. Para ello haremos lo siguiente:

    ```console
    $ python -m venv .venv --prompt blog
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
    (blog)$ 
    ```

    !!! tip "Recuerda activar"

        Todas las intervenciones que hagamos durante el desarrollo del proyecto requieren tener el entorno virtual activado para disponer de las distintas librerías y paquetes previamente instaladas. ¡Recuerda activar el entorno virtual!

    #### Desactivar el entorno virtual { #desactivate-venv }

    Para desactivar el entorno virtual basta con ejecutar el siguiente comando:

    ```console
    $ deactivate
    ```

=== "*uv* &nbsp;:simple-uv:{.uv}"

    Una vez ==dentro de la carpeta del proyecto== vamos a crear un [proyecto (_uv_)](https://docs.astral.sh/uv/guides/projects/) que gestiona de forma transparente el _entorno virtual_. Para ello haremos lo siguiente:

    ```console
    $ uv init --bare #(1)!
    Initialized project `blog`
    ```
    { .annotate }
    
    1. Se creará un fichero `pyproject.toml` (en la carpeta del proyecto) con el siguiente contenido:

        ```toml
        [project]
        name = "blog"
        version = "0.1.0"
        requires-python = ">=3.13"
        dependencies = [] 
        ```

## Nuevo proyecto { #new-project }

Suponiendo que ya hemos [creado la carpeta](#project-folder) y el [entorno virtual](#virtualenv) vamos a crear un **nuevo proyecto Django**.

### Instalación de dependencias { #install-dependencies }

=== "*venv* :octicons-package-24:{.blue}"

    [Activamos el entorno virtual](#activate-venv) e ^^instalamos^^ el paquete _Django_:

    ```console
    $ pip install django
    ```

    !!! tip "Recuerda activar"

        Todas las intervenciones que hagamos durante el desarrollo del proyecto requieren tener el entorno virtual activado para disponer de las distintas librerías y paquetes previamente instaladas. ¡Recuerda activar el entorno virtual!

=== "*uv* &nbsp;:simple-uv:{.uv}"

    ```console
    $ uv add django #(1)!
    Using CPython 3.13.2
    Creating virtual environment at: .venv
    Resolved 5 packages in 281ms
    Installed 3 packages in 128ms
     + asgiref==3.9.2
     + django==5.2.6
     + sqlparse==0.5.3
    ```
    { .annotate }
    
    1.  1. Crea el entorno virtual (si no existía).
        2. Instala `django` (y sus dependencias) en el entorno virtual.
        3. Añade `django` como requerimiento a `pyproject.toml`
        4. Crea el archivo `uv.lock` con las dependencias necesarias.

### Creación del proyecto { #create-project }

Cuando instalamos Django, este paquete ofrece un ejecutable llamado [`django-admin`](https://docs.djangoproject.com/en/stable/ref/django-admin/).

Supongamos que el proyecto se va a llamar `blog` y que ya estamos dentro de una carpeta llamada `blog`.

Para crear el proyecto lanzamos el siguiente comando:

=== "*venv* :octicons-package-24:{.blue}"

    ```console
    $ django-admin startproject main .
    ```

=== "*uv* &nbsp;:simple-uv:{.uv}"

    ```console
    $ uv run django-admin startproject main .
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

El fichero `manage.py` nos permite ejecutar una [gran variedad de acciones](https://docs.djangoproject.com/en/stable/ref/django-admin/) sobre el proyecto Django. Su funcionalidad es la misma que `django-admin` pero además establece la variable de entorno [`DJANGO_SETTINGS_MODULE`](https://docs.djangoproject.com/en/stable/topics/settings/#envvar-DJANGO_SETTINGS_MODULE) apuntando a las configuraciones del proyecto `main/settings.py`.

??? tip "main"

    El hecho de haber elegido `main` como nombre del proyecto es simplemente porque se crea una carpeta con ese nombre dentro del proyecto con los elementos «principales» (_main_).

    Pero se podría haber utilizando cualquier otro nombre que denotara ese lugar preferente: `core`, `base`, `kernet`, etc.

## Primer arranque { #first-launch }

Para verificar que todo está en orden podemos comprobar el estado del proyecto con el siguiente comando:

=== "*venv* :octicons-package-24:{.blue}"

    ```console
    $ ./manage.py check
    System check identified no issues (0 silenced).
    ```

=== "*uv* &nbsp;:simple-uv:{.uv}"

    ```console
    $ uv run manage.py check
    System check identified no issues (0 silenced).
    ```

Antes de arrancar nuestro proyecto Django por primera vez, necesitamos aplicar las [migraciones](models.md#migrations). Aunque se verán con más profundidad en futuras secciones, en este punto podemos entender que hay una serie de acciones a llevar a cabo en la base de datos para que Django pueda disponer de una estructura sobre la que trabajar.

Para ello ejecutamos el siguiente comando:

=== "*venv* :octicons-package-24:{.blue}"

    ```console
    $ ./manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, sessions
    Running migrations:
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying admin.0002_logentry_remove_auto_add... OK
      Applying admin.0003_logentry_add_action_flag_choices... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying auth.0007_alter_validators_add_error_messages... OK
      Applying auth.0008_alter_user_username_max_length... OK
      Applying auth.0009_alter_user_last_name_max_length... OK
      Applying auth.0010_alter_group_name_max_length... OK
      Applying auth.0011_update_proxy_permissions... OK
      Applying auth.0012_alter_user_first_name_max_length... OK
      Applying sessions.0001_initial... OK
    ```

=== "*uv* &nbsp;:simple-uv:{.uv}"

    ```console
    $ uv run manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, sessions
    Running migrations:
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying admin.0002_logentry_remove_auto_add... OK
      Applying admin.0003_logentry_add_action_flag_choices... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying auth.0007_alter_validators_add_error_messages... OK
      Applying auth.0008_alter_user_username_max_length... OK
      Applying auth.0009_alter_user_last_name_max_length... OK
      Applying auth.0010_alter_group_name_max_length... OK
      Applying auth.0011_update_proxy_permissions... OK
      Applying auth.0012_alter_user_first_name_max_length... OK
      Applying sessions.0001_initial... OK
    ```

Ahora ya estamos en disposición de «levantar» el **servidor de desarrollo** de Django:

=== "*venv* :octicons-package-24:{.blue}"

    ```console
    $ ./manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...
    
    System check identified no issues (0 silenced).
    September 28, 2025 - 21:41:23
    Django version 5.2.6, using settings 'main.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    
    WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
    For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/
    ```

=== "*uv* &nbsp;:simple-uv:{.uv}"

    ```console
    $ uv run manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...
    
    System check identified no issues (0 silenced).
    September 28, 2025 - 21:41:23
    Django version 5.2.6, using settings 'main.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    
    WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
    For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/
    ```

Siempre y cuando no haya surgido algún inconveniente de última hora, con esto ya tendremos accesible el proyecto en la URL http://127.0.0.1:8000/ (1)
{ .annotate }

1. También estará disponible en http://localhost:8000/

!!! question "Detener el servidor"

    Para detener el servidor de desarrollo basta con pulsar ++ctrl+c++

!!! warning "Puerto en uso"

    Es posible que en algún momento —al arrancar el servidor de desarrollo— nos aparezca este mensaje: <span class="acc">«Error: That port is already in use.»</span> Ello se debe a que ya existe un proceso escuchando en el puerto 8000.

    Para resolverlo debemos «matar» el proceso (o procesos) bloqueantes:
    
    ```bash
    pkill -f "[Pp]ython.*manage.py runserver" || echo "No process"
    ```

### Interfaz administrativa { #admin }

Django proporciona «automágicamente» una [interfaz administrativa](admin.md) que permite interactuar con la base de datos de manera cómoda y accesible.

Para poder acceder a dicha interfaz administrativa, obviamente necesitaremos unas **credenciales**. Vamos a aprovechar este momento para crear una cuenta de **«superusuario»** (_administrador_) mediante el subcomando `createsuperuser`:

=== "*venv* :octicons-package-24:{.blue}"

    ```console
    $ ./manage.py createsuperuser
    Username (leave blank to use 'sdelquin'): admin
    Email address: admin@example.com
    Password:
    Password (again):
    Superuser created successfully.
    ```

=== "*uv* &nbsp;:simple-uv:{.uv}"

    ```console
    $ uv run manage.py createsuperuser
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

:material-alarm-light:{.acc} Esto no será necesario si ya estás trabajando en un repositorio `git`(GitHub) creado previamente.

### Ignorando archivos { #ignoring-files }

Es fundamental **excluir ciertos archivos** del sistema de control de versiones. Para ello es necesario crear un fichero `.gitignore` en el raíz de nuestro proyecto.

Aunque existen [plantillas prediseñadas `.gitignore`](https://github.com/github/gitignore) para cada tipo de proyecto, a continuación se muestra un contenido mínimo para un proyecto Django:

```bash title=".gitignore"
.venv #(1)!
db.sqlite3 #(2)!
*.pyc #(3)!
.mypy_cache #(4)!
```
{ .annotate }

1. Carpeta que contiene el [entorno virtual](#virtualenv).
2. Nombre (por defecto) de la base de datos [sqlite](../../../stdlib/data-access/sqlite.md) en Django.
3. Ficheros con [«bytecode»](../../../core/introduction/machine.md#compilers) compilado de Python.
4. Caché de [mypy](https://mypy-lang.org/) (si procede).

## Requerimientos { #requirements }

Para que los proyectos (Python) puedan ser reproducibles en otros entornos (por ejemplo en producción) es altamente recomendable añadir un fichero con los requerimientos.

=== "*venv* :octicons-package-24:{.blue}"

    El fichero de requerimientos se suele denominar `requirements.txt` y contiene una línea por cada paquete/librería Python que utilicemos en el proyecto.

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

=== "*uv* &nbsp;:simple-uv:{.uv}"

    La gestión de los requerimientos por parte de `uv` es transparente. Maneja dos ficheros que permiten definir los requerimientos del proyecto:

    <div class="annotate" markdown>

    - [x] `pyproject.toml`(1)
    - [x] `uv.lock`(2)

    </div>

    1. Aquí se definen los requerimientos (paquetes instalados con `uv add`)
    2. Aquí se establecen las dependencias de los paquetes «primarios» instalados previamente.

    :material-alarm-light:{.acc} Ambos ficheros deberían estar en el **control de versiones**.

## Lanzando comandos { #lauch-commands }

[just](https://github.com/casey/just) es un lanzador de comandos. Aunque no es imprescindible para desarrollar proyectos software, es altamente recomendable incluirlo porque permite automatizar muchas tareas que son habituales en el día a día.

Basta con tener [instalada la herramienta `just`](https://github.com/casey/just?tab=readme-ov-file#pre-built-binaries) y crear un fichero `justfile` en el raíz de nuestro proyecto. Este fichero se compone de «recetas» identificadas por un nombre que luego podemos ejecutar desde línea de comandos.

!!! tip "Alias"

    Un `alias j=just` suele ser interesante ya que nos permite «ahorrar» aún más en la escritura de las recetas.

### Primer justfile { #first-justfile }

A continuación se muestra un <span class="example">ejemplo:material-flash:</span> ^^mínimo^^ de `justfile` para un proyecto Django:

=== "*venv* :octicons-package-24:{.blue}"

    ```makefile title="justfile"
    # Run development server
    dev:
        ./manage.py runserver

    # Check Django project
    check:
        ./manage.py check

    # Create a superuser (or update it if already exists)
    create-su username="admin" password="admin" email="admin@example.com":
        #!/usr/bin/env bash
        ./manage.py shell -c '
        from django.contrib.auth.models import User
        user, _ = User.objects.get_or_create(username="{{ username }}")
        user.email = "{{ email }}"
        user.set_password("{{ password }}") 
        user.is_superuser = True
        user.is_staff = True
        user.save()
        ' 
        echo "✔ Created superuser → {{ username }}:{{ password }}"

    # Kill existent manage.py processes
    kill:
        pkill -f "[Pp]ython.*manage.py runserver" || echo "No process"
    ```

=== "*uv* &nbsp;:simple-uv:{.uv}"

    ```makefile title="justfile"
    # Run development server
    dev:
        uv run manage.py runserver

    # Check Django project
    check:
        uv run manage.py check
    
    # Create a superuser (or update it if already exists)
    create-su username="admin" password="admin" email="admin@example.com":
        #!/usr/bin/env bash
        uv run manage.py shell -c '
        from django.contrib.auth.models import User
        user, _ = User.objects.get_or_create(username="{{ username }}")
        user.email = "{{ email }}"
        user.set_password("{{ password }}") 
        user.is_superuser = True
        user.is_staff = True
        user.save()
        ' 
        echo "✔ Created superuser → {{ username }}:{{ password }}"
    
    # Kill existent manage.py processes
    kill:
        pkill -f "[Pp]ython.*manage.py runserver" || echo "No process"
    ```

### Invocar recetas { #invoke-recipes }

Si queremos levantar el servidor de desarrollo basta con ejecutar:

```console
$ just dev #(1)!
```
{ .annotate }

1. O simplemente `just` ya que la primera receta es la _receta por defecto_.

### Listar recetas { #list-recipes }

Para ^^listar todas las recetas disponibles^^ podemos hacer:

```console
$ just -l
Available recipes:
    check # Check Django project
    create-su username="admin" password="admin" email="admin@example.com" # Create a superuser (or update it if already exists)
    dev   # Run development server
    kill  # Kill existent manage.py processes
```

### Parámetros { #recipe-params }

Aquellas recetas que tienen parámetros (por <span class="example">ejemplo:material-flash:</span> `create-su`) admiten ^^argumentos^^ en línea de comandos:

=== "Crear superusuario (por defecto)"

    El siguiente comando creará el superusuario `admin` con contraseña `admin` y correo `admin@example.com` ya que son los valores por defecto indicados en la receta.

    ```console
    $ just create-su
    ```

=== "Actualizar superusuario"

    Suponiendo que ya existe un usuario `admin` y que hemos olvidado (o queremos cambiar) su contraseña, el siguiente comando actualizará su contraseña a `space`:
    
    ```console
    $ just create-su admin space
    ```

=== "Crear superusuario (personalizado)"

    El siguiente comando creará el superusuario `admin` con contraseña `jupyter` y correo `admin@jupyter.com`:

    ```console
    $ just create-su admin jupyter admin@jupyter.com
    ```

[^1]: También se denominan **dependencias** del proyecto.
[^2]: Viene del verbo «pin» en inglés.
[^3]: La interfaz administrativa ha sido generada por Django sin escribir una sola línea de código adicional.
