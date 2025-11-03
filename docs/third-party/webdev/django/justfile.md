---
icon: material/list-box
---

# Justfile { #justfile }

[just](https://github.com/casey/just) es un lanzador de comandos. Aunque no es imprescindible para desarrollar proyectos software, es altamente recomendable incluirlo porque permite automatizar muchas tareas que son habituales en el día a día.

Basta con tener [instalada la herramienta `just`](https://github.com/casey/just?tab=readme-ov-file#pre-built-binaries) y crear un fichero `justfile` en el raíz de nuestro proyecto. Este fichero se compone de «recetas» identificadas por un nombre que luego podemos ejecutar desde línea de comandos.

!!! tip "Alias"

    Un `alias j=just` suele ser interesante ya que nos permite «ahorrar» aún más en la escritura de las recetas.

## Justfile para Django { #django-justfile }

A continuación se muestra un `justfile` con _recetas_ para un proyecto Django, suponiendo que se está utilizando [`uv`](../../../core/devenv/real-context.md#uv) como gestor de entornos virtuales y paquetería Python:

```makefile title="justfile" linenums="1"
# Run development server
[group('server')]
dev port="8000":
    uv run manage.py runserver {{ port }}

# Run development server with external access
[group('server')]
dev0 port="8000":
    #!/usr/bin/env bash
    IP=$(ip -br a | perl -lane 'print $1 if /^enp/ && $F[2] =~ m{([^/]+)}')
    if grep -q $IP main/settings.py; then
        uv run ./manage.py runserver 0.0.0.0:{{ port }}
    else
        echo "Add \"$IP\" to ALLOWED_HOSTS in main/settings.py"
    fi
    uv run manage.py runserver 0.0.0.0:80

alias c:=check
# Check Django project
[group('migrations')]
check:
    uv run manage.py check

alias mm:=makemigrations
# Make model migrations
[group('migrations')]
makemigrations app="":
    uv run manage.py makemigrations {{app}}

alias m:=migrate
# Apply model migrations
[group('migrations')]
migrate app="":
    uv run manage.py migrate {{app}}

# Create a superuser (or update if already exists)
[group('data')]
create-su username="admin" password="admin" email="admin@example.com":
    #!/usr/bin/env bash
    uv run manage.py shell -v0 -c '
    from django.contrib.auth.models import User
    user, _ = User.objects.get_or_create(username="{{ username }}")
    user.email = "{{ email }}"
    user.set_password("{{ password }}") 
    user.is_superuser = True
    user.is_staff = True
    user.save()
    ' 
    echo "✔ Created superuser → {{ username }}:{{ password }}"

# Create a normal user (or update if already exists)
[group('data')]
create-user username password email:
    #!/usr/bin/env bash
    uv run manage.py shell -v0 -c '
    from django.contrib.auth.models import User
    user, _ = User.objects.get_or_create(username="{{ username }}")
    user.email = "{{ email }}"
    user.set_password("{{ password }}") 
    user.is_superuser = False
    user.is_staff = False
    user.save()
    '
    echo "✔ Created user → {{ username }}:{{ password }}"

# Add a new app and install it on settings.py
[group('config')]
startapp app:
    #!/usr/bin/env bash
    uv run manage.py startapp {{ app }}
    APP_CLASS={{ app }}
    APP_CONFIG="{{ app }}.apps.${APP_CLASS^}Config"
    perl -0pi -e "s/(INSTALLED_APPS *= *\[)(.*?)(\])/\1\2    '$APP_CONFIG',\n\3/smg" ./main/settings.py
    echo "✔ App '{{ app }}' created & added to settings.INSTALLED_APPS"

alias sh:=shell
# Open project (django) shell
[group('shell')]
shell:
    uv run manage.py shell

alias dbsh:=dbshell
# Open database shell
[group('shell')]
dbshell:
    uv run manage.py dbshell

# Setup new project
[group('config')]
setup: && migrate create-su set-tz
    #!/usr/bin/env bash
    uv sync
    uv run django-admin startproject main .

# Set Django TimeZone
[group('config')]
set-tz timezone="Atlantic/Canary":
    #!/usr/bin/env bash
    sed -i -E "s@(TIME_ZONE).*@\1 = '{{ timezone }}'@" ./main/settings.py
    if [ $? -eq 0 ]; then
        echo "✔ Fixed TIME_ZONE='{{ timezone }}' and LANGUAGE_CODE='es-es'"
    fi

# Remove migrations and database. Reset DB artefacts.
[confirm("⚠️ All migrations and database will be removed. Continue? [yN]:")]
[group('migrations')]
reset-db: && makemigrations migrate create-su
    #!/usr/bin/env bash
    find . -path "*/migrations/*.py" ! -path "./.venv/*" ! -name "__init__.py" -delete
    find . -path "*/migrations/*.pyc" ! -path "./.venv/*" -delete
    rm -f db.sqlite3

# Remove virtualenv
[confirm("⚠️ Virtualenv './venv' will be removed. Continue? [yN]:")]
[group('utils')]
rm-venv:
    rm -fr .venv

# Kill existent manage.py processes
[group('utils')]
kill:
    pkill -f "[Pp]ython.*manage.py runserver" || echo "No process"

# Launch tests
[group('utils')]
test pytest_args="":
    uv run pytest -s {{ pytest_args }}

# Generate random secret key
[group('production')]
secret-key:
    #!/usr/bin/env bash
    uv run manage.py shell -v0 -c '
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
    '
```

## Invocar recetas { #invoke-recipes }

Si queremos levantar el servidor de desarrollo basta con ejecutar:

```console
$ just dev
```

O simplemente `just` ya que la primera receta es la _receta por defecto_.

## Listar recetas { #list-recipes }

Para ^^listar todas las recetas disponibles^^ podemos hacer:

```console
$ just -l
```

## Parámetros { #recipe-params }

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
