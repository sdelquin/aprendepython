---
icon: simple/uv
tags:
  - Entornos de desarrollo
  - Entorno integrado de desarrollo
  - uv
---

# uv

![Banner](images/uv/banner.jpg)
/// caption
Imagen generada con Inteligencia Artificial
///

[uv](https://docs.astral.sh/uv/getting-started/features/) proporciona características esenciales para el desarrollo con Python — desde instalar Python y manejar «scripts» sencillos hasta trabajar en proyectos de gran entidad que soportan múltiples versiones de Python y plataformas. Es [extremadamente rápida](https://github.com/astral-sh/uv/blob/main/BENCHMARKS.md) y está escrita en lenguaje [Rust](https://www.rust-lang.org/es).

Hay que aclarar que uv no forma parte del «tooling» oficial de Python. Está desarrollado por la empresa [Astral](https://astral.sh/) y sus dirigientes establecen el rumbo y toman las decisiones correspondientes. Pero también es justo decir que el nivel de adopción de la comunidad Python sobre sus herramientas está siendo enorme y se está convirtiendo en una especia de «estándar de facto» para trabajar con Python.

## Instalación

Proporciona métodos de **instalación** muy sencillos:

- [Instalación para macOS :simple-apple: y Linux :simple-linux:](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1).
- [Instalación para Windows :fontawesome-brands-windows:](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2).

??? tip "cURL"

    [cURL](https://curl.se/) es una [herramienta muy utilizada](https://github.com/curl/curl) para transferir datos sobre Internet. Gran parte del software que instalamos se puede descargar utilizando `curl`.

    Métodos de instalación:

    === ":fontawesome-brands-windows: Windows"

        ```console
        $ winget install -e --id cURL.cURL
        ```

    === ":simple-apple: macOS"

        ```console
        $ brew install curl
        ```

    === ":simple-linux: Linux"

        ```console
        $ sudo apt-get install -y curl
        ```

Para comprobar que hemos instalado bien la herramienta, podemos ejecutar lo siguiente:

```console
$ uv --version #(1)!
uv 0.12.13 (aarch64-unknown-linux-gnu)
```
{ .annotate }

1. Tu versión es muy probable que difiera de lo aquí documentado.

## Versiones de Python

Una vez instalado, podemos empezar a dar nuestros primeros pasos con uv. Supongamos que lo primero que queremos es ver qué versiones de Python tenemos instaladas en nuestro sistema:

```console
$ uv python list
cpython-3.15.0rc2-linux-aarch64-gnu                 <download available>
cpython-3.15.0rc2+freethreaded-linux-aarch64-gnu    <download available>
cpython-3.14.7-linux-aarch64-gnu                    <download available>
cpython-3.14.7+freethreaded-linux-aarch64-gnu       <download available>
cpython-3.13.15-linux-aarch64-gnu                   <download available>
cpython-3.13.15+freethreaded-linux-aarch64-gnu      <download available>
cpython-3.12.14-linux-aarch64-gnu                   <download available>
cpython-3.11.16-linux-aarch64-gnu                   <download available>
cpython-3.10.21-linux-aarch64-gnu                   <download available>
cpython-3.9.25-linux-aarch64-gnu                    <download available>
cpython-3.8.20-linux-aarch64-gnu                    <download available>
pypy-3.11.15-linux-aarch64-gnu                      <download available>
pypy-3.10.16-linux-aarch64-gnu                      <download available>
pypy-3.9.19-linux-aarch64-gnu                       <download available>
pypy-3.8.16-linux-aarch64-gnu                       <download available>
graalpy-3.13.0-linux-aarch64-gnu                    <download available>
graalpy-3.12.0-linux-aarch64-gnu                    <download available>
graalpy-3.11.0-linux-aarch64-gnu                    <download available>
graalpy-3.10.0-linux-aarch64-gnu                    <download available>
graalpy-3.8.5-linux-aarch64-gnu                     <download available>
```

Es posible que algunas de las [versiones de Python](../desarrollo/python.md#versiones-de-python) puedan estar ya instaladas en nuestro sistema. En ese caso veremos la ruta de nuestro sistema operativo que lleva a dicha versión.

Ahora vamos a instalar una versión de Python:

```console
$ uv python install #(1)!
Installed Python 3.14.7 in 3.10s
 + cpython-3.14.7-linux-aarch64-gnu (python3.14)
```
{ .annotate }

1.  - Este comando instala la **última versión de Python disponible**.
    - En el caso de que queramos una versión concreta, podemos hacer:
        ```console
        $ uv python install 3.10
        ```

Podemos comprobar que efectivamente se ha instalado y nos aparece en el listado de versiones disponibles:

```console hl_lines="5-6"
$ uv python list
cpython-3.15.0rc2-linux-aarch64-gnu                 <download available>
cpython-3.15.0rc2+freethreaded-linux-aarch64-gnu    <download available>
cpython-3.14.7-linux-aarch64-gnu                    .local/bin/python3.14 -> .local/share/uv/python/cpython-3.14-linux-aarch64-gnu/bin/python3.14
cpython-3.14.7-linux-aarch64-gnu                    .local/share/uv/python/cpython-3.14-linux-aarch64-gnu/bin/python3.14
...
...
```

!!! info "Ruta de instalación"

    Una de las cosas interesantes de `uv` es que instala las versiones de Python en una carpeta del HOME del usuario, concretamente en `~/.local/share/uv/`

### Intérprete de Python

Ahora mismo podríamos lanzar el intérprete de Python directamente desde la terminal utilizando:

```console
$ python3.14
Python 3.14.7 (main, Sep  1 2026, 14:16:03) [Clang 22.1.3 ] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

uv por defecto solo instala «ejecutables versionados» (`python3.14`). Pero es posible instalar `python` como ejecutable mediante la siguiente opción:

```console hl_lines="9-10 17"
$ uv python install --default
warning: The `--default` option is experimental and may change without warning. Pass `--preview-features python-install-default` to disable this warning
Installed Python 3.14.7 in 57ms
 + cpython-3.14.7-linux-aarch64-gnu (python, python3)

$ uv python list
cpython-3.15.0rc2-linux-aarch64-gnu                 <download available>
cpython-3.15.0rc2+freethreaded-linux-aarch64-gnu    <download available>
cpython-3.14.7-linux-aarch64-gnu                    .local/bin/python3.14 -> .local/share/uv/python/cpython-3.14-linux-aarch64-gnu/bin/python3.14
cpython-3.14.7-linux-aarch64-gnu                    .local/bin/python3 -> .local/share/uv/python/cpython-3.14-linux-aarch64-gnu/bin/python3.14
cpython-3.14.7-linux-aarch64-gnu                    .local/bin/python -> .local/share/uv/python/cpython-3.14-linux-aarch64-gnu/bin/python3.14
cpython-3.14.7-linux-aarch64-gnu                    .local/share/uv/python/cpython-3.14-linux-aarch64-gnu/bin/python3.14
...
...

$ python
Python 3.14.7 (main, Sep  1 2026, 14:16:03) [Clang 22.1.3 ] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Es posible igualmente instalar otra versión de Python indicando a la vez que sea la versión «por defecto»:

```console hl_lines="16-17 24"
$ uv python install --default 3.10
warning: The `--default` option is experimental and may change without warning. Pass `--preview-features python-install-default` to disable this warning
Installed Python 3.10.21 in 58ms
 + cpython-3.10.21-linux-aarch64-gnu (python, python3)

$ uv python list
cpython-3.15.0rc2-linux-aarch64-gnu                 <download available>
cpython-3.15.0rc2+freethreaded-linux-aarch64-gnu    <download available>
cpython-3.14.7-linux-aarch64-gnu                    .local/bin/python3.14 -> .local/share/uv/python/cpython-3.14-linux-aarch64-gnu/bin/python3.14
cpython-3.14.7-linux-aarch64-gnu                    .local/share/uv/python/cpython-3.14-linux-aarch64-gnu/bin/python3.14
cpython-3.14.7+freethreaded-linux-aarch64-gnu       <download available>
cpython-3.13.15-linux-aarch64-gnu                   <download available>
cpython-3.13.15+freethreaded-linux-aarch64-gnu      <download available>
cpython-3.12.14-linux-aarch64-gnu                   <download available>
cpython-3.11.16-linux-aarch64-gnu                   <download available>
cpython-3.10.21-linux-aarch64-gnu                   .local/bin/python3.10 -> .local/share/uv/python/cpython-3.10-linux-aarch64-gnu/bin/python3.10
cpython-3.10.21-linux-aarch64-gnu                   .local/bin/python3 -> .local/share/uv/python/cpython-3.10-linux-aarch64-gnu/bin/python3.10
cpython-3.10.21-linux-aarch64-gnu                   .local/bin/python -> .local/share/uv/python/cpython-3.10-linux-aarch64-gnu/bin/python3.10
cpython-3.10.21-linux-aarch64-gnu                   .local/share/uv/python/cpython-3.10-linux-aarch64-gnu/bin/python3.10
...
...

$ python
Python 3.10.21 (main, Sep  1 2026, 14:15:44) [Clang 22.1.3 ] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

## Proyectos

Al igual que ocurría con los [entornos virtuales nativos de Python](../desarrollo/python.md#entornos-virtuales), `uv` ofrece la posibilidad de trabajar con proyectos que (internamente) disponen de un entorno virtual.

### Inicializar un proyecto

Lo primero será crear una carpeta de trabajo:

```console
$ mkdir proyecto
$ cd proyecto
```

Y ahora inicializamos el proyecto `uv` de la siguiente manera:

```console hl_lines="1"
$:~/proyecto> uv init --bare --no-project #(1)!
Initialized project `proyecto`
```
{ .annotate }

1. Aunque las opciones `--bare` y `--no-project` no son estrictamente necesarias, suelo utilizarlas para crear un proyecto completamente vacío y que no dependa de posibles proyectos «superiores».

La creación del proyecto es «simplemente» la inclusión del fichero `pyproject.toml` con las especificaciones del proyecto:

```console
$:~/proyecto> ls
pyproject.toml

$:~/proyecto> cat pyproject.toml
[project]
name = "proyecto"
version = "0.1.0"
requires-python = ">=3.14"
dependencies = []
```

!!! tip "Versión específica"

    Por defecto `uv` siempre trata de utilizar (instalar) la última versión disponible de Python. Pero si queremos que nuestro proyecto trabaje con una versión específica de Python, podemos indicarlo a la hora de inicializar el proyecto.

    Por <span class="example">ejemplo:material-flash:</span> si vamos a utilizar Python 3.11:

    ```console
    $ uv init -p3.11 --bare --no-project
    ```

### Añadir dependencias

Ahora resulta muy sencillo añadir una dependencia a nuestro proyecto. Supongamos que queremos hacer uso del «famoso» paquete [`requests`](../../paquetes/redes/requests.md):

```console
$:~/proyecto> uv add requests
Using CPython 3.14.7
Creating virtual environment at: .venv
Resolved 6 packages in 384ms
Installed 5 packages in 21ms
 + certifi==2026.7.22
 + charset-normalizer==3.5.1
 + idna==3.19
 + requests==2.34.2
 + urllib3==2.7.0
```

Aquí acaban de ocurrir varias cosas:

1. Al ser `requests` la primera dependencia del proyecto, no había un [entorno virtual](../desarrollo/python.md#entornos-virtuales) creado previamente. Es por ello que se crea en la carpeta `.venv` usando la «última» versión disponible de Python.
2. Posteriormente se instala el paquete `requests` junto a todas sus dependencias.

Podemos confirmar la instalación:

```console
$:~/proyecto> cat pyproject.toml | grep -A3 dependencies #(1)!
dependencies = [
    "requests>=2.34.2",
]

$:~/proyecto> cat uv.lock | perl -lne 'print if /^name =/ && !/proyecto/' #(2)!
name = "certifi"
name = "charset-normalizer"
name = "idna"
name = "requests"
name = "urllib3"
```
{ .annotate }

1. La dependencia `requests` se ha añadido al fichero `pyproject.toml`.
2. Las dependencias de `requests` se han añadido al fichero `uv.lock`.

#### Dependencias de desarrollo

Es muy útil poder añadir dependencias que solo deben ser tenidas en cuenta en algún contexto de nuestra aplicación.

Supongamos que necesitamos utilizar el paquete [`django-debug-toolbar`](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html) pero solo en nuestro entorno de desarrollo.

Para añadirlo al proyecto utilizamos el modificador `--dev` tal y como se indica a continuación:

```console
$:~/proyecto> uv add --dev django-debug-toolbar
Resolved 11 packages in 558ms
Prepared 4 packages in 928ms
Installed 4 packages in 155ms
 + asgiref==3.12.1
 + django==6.1.1
 + django-debug-toolbar==8.0.0
 + sqlparse==0.6.0
```

Esta dependencia se ha incluido en `pyproject.toml` dentro del grupo `dev`:

```console hl_lines="10-13"
$:~/proyecto> cat pyproject.toml
[project]
name = "proyecto"
version = "0.1.0"
requires-python = ">=3.14"
dependencies = [
    "requests>=2.34.2",
]

[dependency-groups]
dev = [
    "django-debug-toolbar>=8.0.0",
]
```

#### Otras dependencias

Lo bueno de `uv` es que permite definir cualquier grupo de dependencias (aunque el grupo `dev` ya existe por defecto).

Esto nos brinda la posibilidad, por ejemplo, de definir dependencias que son exclusivamente para un entorno de producción. Supongamos que queremos desplegar una aplicación web [Django](../../paquetes/web/django/) utilizando el paquete [`gunicorn`](https://gunicorn.org/):

```console
$:~/proyecto> uv add --group prod gunicorn
Resolved 12 packages in 463ms
Installed 1 package in 25ms
 + gunicorn==26.2.0
```

Comprobamos el estado del fichero de configuración del proyecto:

```console hl_lines="14-16"
$:~/proyecto> cat pyproject.toml
[project]
name = "proyecto"
version = "0.1.0"
requires-python = ">=3.14"
dependencies = [
    "requests>=2.34.2",
]

[dependency-groups]
dev = [
    "django-debug-toolbar>=8.0.0",
]
prod = [
    "gunicorn>=26.2.0",
]
```

#### Fijar una versión

Es posible que —en determinadas circunstancias— interese instalar una versión concreta de un paquete. Esto es posible hacerlo con uv de forma muy sencilla.

Supongamos que nos interesa [una versión](https://github.com/yaml/pyyaml/releases) un poco más antigua del paquete `pyyaml`:

```console
$:~/proyecto> uv add pyyaml==6.0.2
Resolved 13 packages in 382ms
      Built pyyaml==6.0.2                                                                                                                  Prepared 1 package in 3.79s
Installed 1 package in 1ms
 + pyyaml==6.0.2 
```

### Listar dependencias

Llegado el caso podríamos querer consultar las dependencias que tenemos actualmente instaladas en el ~~entorno virtual~~ proyecto.

Para ello podemos utilizar la herramienta [`pip`](../../entornos/desarrollo/python/#gestion-de-paquetes) a través de uv[^1]:

```console
$:~/proyecto> uv pip list
Package              Version
-------------------- ---------
asgiref              3.12.1
certifi              2026.7.22
charset-normalizer   3.5.1
django               6.1.1
django-debug-toolbar 8.0.0
idna                 3.20
requests             2.34.2
sqlparse             0.6.0
urllib3              2.8.0
```

En el caso de que queremos visualizar el **árbol de dependencias** que forma `pyproject.toml` + `uv.lock` podemos ejecutar el siguiente comando:

```console
$:~/proyecto> uv tree --all-groups
Resolved 12 packages in 1ms
proyecto v0.1.0
├── requests v2.34.2
│   ├── certifi v2026.7.22
│   ├── charset-normalizer v3.5.1
│   ├── idna v3.20
│   └── urllib3 v2.8.0
├── django-debug-toolbar v8.0.0 (group: dev)
│   ├── django v6.1.1
│   │   ├── asgiref v3.12.1
│   │   └── sqlparse v0.6.0
│   └── sqlparse v0.6.0
└── gunicorn v26.2.0 (group: prod)
```

!!! warning "Dependencias declaradas"

    El comando `uv tree` no muestra las dependencias instaladas, muestra las **dependencias declaradas** en el proyecto.

### Sincronizar dependencias

Una de las características más potentes de uv es que puede recrear el entorno virtual (con todas sus dependencias) de una forma totalmente exacta y muy rápidamente.

Para sincronizar dependencias utilizamos el comando `uv sync`.

Vamos a «romper» nuestro entorno virtual y volver a recrearlo:

```console hl_lines="1"
$:~/proyecto> rm -rf .venv
$:~/proyecto> uv pip list
Using Python 3.14.7 environment at: /root/.local/share/uv/python/cpython-3.14.7-linux-aarch64-gnu
Package Version
------- -------
pip     26.2.1
```

Ahora mismo ni siquiera tenemos un entorno virtual creado ya que hemos borrado la carpeta `.venv` por tanto no hay ninguna dependencia Python instalada.

Para volver a **sincronizar** el proyecto ejecutamos:

```console
$ $:~/proyecto> uv sync
Using CPython 3.14.7
Creating virtual environment at: .venv
Resolved 12 packages in 1ms
Installed 9 packages in 585ms
 + asgiref==3.12.1
 + certifi==2026.7.22
 + charset-normalizer==3.5.1
 + django==6.1.1
 + django-debug-toolbar==8.0.0
 + idna==3.20
 + requests==2.34.2
 + sqlparse==0.6.0
 + urllib3==2.8.0
```

Comprobamos ahora las dependencias instaladas:

```console
$:~/proyecto> uv pip list
Package              Version
-------------------- ---------
asgiref              3.12.1
certifi              2026.7.22
charset-normalizer   3.5.1
django               6.1.1
django-debug-toolbar 8.0.0
idna                 3.20
requests             2.34.2
sqlparse             0.6.0
urllib3              2.8.0
```

Es importante señalar que las dependencias de «producción» no se han instalado, porque por defecto no tiene en cuenta los grupos adicionales que hemos creado. Si queremos tenerlas en cuenta basta indicarlo en el propio comando:

```console
$:~/proyecto> uv sync --all-groups
Resolved 12 packages in 1ms
Installed 1 package in 12ms
 + gunicorn==26.2.0
```

#### Seleccionando dependencias

Hay mucha flexibilidad a la hora de indicar las dependencias que queremos instalar (sincronizar) mediante los grupos creados.

Un claro <span class="example">ejemplo:material-flash:</span> de ello lo vemos al recrear el proyecto en un **entorno de producción**. En este escenario nos interesa:

1. Instalar todas las dependencias «generales».
2. No instalar las dependencias de desarrollo.
3. Instalar las dependencias de producción.

Esto lo conseguimos ejecutando el siguiente comando:

```console
$:~/proyecto> uv sync --no-group dev --group prod
Resolved 12 packages in 1ms
Uninstalled 4 packages in 96ms
 - asgiref==3.12.1
 - django==6.1.1
 - django-debug-toolbar==8.0.0
 - sqlparse==0.6.0
```

Por tanto si ahora listamos las dependencias instaladas en el sistema solo veremos las «generales» y las de producción, sin que aparezcan las de desarrollo:

```console
$:~/proyecto> uv pip list
Package            Version
------------------ ---------
certifi            2026.7.22
charset-normalizer 3.5.1
gunicorn           26.2.0
idna               3.20
requests           2.34.2
urllib3            2.8.0
```

### Borrar dependencias

Para borrar una dependencia en un proyecto utilizamos el comando `uv remove` con el nombre del paquete a eliminar.

Por <span class="example">ejemplo:material-flash:</span> supongamos que ya no necesitamos el paquete `requests` en nuestro proyecto:

```console
$:~/proyecto> uv remove requests
Resolved 7 packages in 326ms
Uninstalled 6 packages in 7ms
Installed 4 packages in 582ms
 + asgiref==3.12.1
 - certifi==2026.7.22
 - charset-normalizer==3.5.1
 + django==6.1.1
 + django-debug-toolbar==8.0.0
 - gunicorn==26.2.0
 - idna==3.20
 - requests==2.34.2
 + sqlparse==0.6.0
 - urllib3==2.8.0
```

No solo hemos borrado el paquete `requests` sino también todas sus dependencias (que no fueran requeridas por algún otro paquete del proyecto).

## Scripts

Es posible «empaquetar» todas las dependencias de un proyecto en un único script y ejecutarlo de forma transparente sin necesidad de gestionar el entorno virtual asociado.

Esto es muy potente ya que podemos «distribuir» artefactos software hechos en Python en un único archivo que podrá ser ejecutado en cualquier contexto (siempre y cuando exista `uv` en el sistema).

### Inicializar un script

Para comentar el desarrollo de un script podemos ejecutar:

```console hl_lines="1"
$ uv init --script fichero.py
Initialized script at `fichero.py`
```

Podemos comprobar el contenido del fichero:

``` hl_lines="2-5"
$:~/proyecto> cat fichero.py
# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///


def main() -> None:
    print("Hello from fichero.py!")


if __name__ == "__main__":
    main()
```

uv añade una cabecera (como comentarios Python) que le permiten conocer la versión de Python a utilizar y las dependencias que se deben incluir al ejecutar.

### Ejecutar un script

Para ejecutar un script hacemos lo siguiente:

```console
$ uv run fichero.py
Hello from fichero.py!
```

### Añadir dependencias

Añadir dependencias a un script es análogo a cuando las [añadimos a un proyecto](#anadir-dependencias).

Supongamos que vamos a incluir el paquete `requests` en nuestro script porque necesitamos realizar ciertas llamadas a recursos de red:

```console
$ uv add --script fichero.py requests
Resolved 5 packages in 191ms
```

Si comprobamos la cabecera del script veremos que se ha actualizado la sección de dependencias:

```console hl_lines="5"
$ head fichero.py
# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "requests>=2.34.2",
# ]
# ///
```

### Hacer ejecutable

Es muy habitual que el script pueda ser ejecutable. Para conseguir esto seguimos dos sencillos pasos:

1. Añadir en la primera línea del fichero este [shebang](https://weblinus.com/que-es-el-shebang-y-como-usarlo-en-sistemas-gnu-linux-tipos-de-interprete-de-comandos/): `#!/usr/bin/env -S uv run --script`
2. Dar permisos de ejecución al fichero.

Para nuestro <span class="example">ejemplo:material-flash:</span> quedaría de la siguiente manera:

Shebang...

```console hl_lines="2"
$ cat fichero.py
#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "requests>=2.34.2",
# ]
# ///


def main() -> None:
    print("Hello from fichero.py!")


if __name__ == "__main__":
    main()
```

Permisos de ejecución...

```console
$ chmod +x fichero.py
```

Tras esto, podemos ejecutar el script sin necesidad (aparente) de invocar a ninguna otra herramienta:

```console
$ ./fichero.py #(1)!
Installed 5 packages in 25ms
Hello from fichero.py!

$ ./fichero.py #(2)!
Hello from fichero.py!
```
{ .annotate }

1. La primera vez que se invoca instala los paquetes necesarios (en un entorno virtual temporal).
2. Las siguientes veces que se ejecuta, siempre y cuando no hayan cambiado las dependencias, no vemos ningún mensaje relacionado con gestión de dependencias.

## Herramientas

Otra de las ventajas de utilizar `uv` es que nos permite gestionar herramientas Python de una forma muy sencilla y a la vez muy potente.

### Instalar herramientas

Para instalar herramientas utilizamos el comando `uv tool install` indicando el paquete correspondiente.

Por <span class="example">ejemplo:material-flash:</span> vamos a instalar el paquete [`cowsay`](https://github.com/VaasuDevanS/cowsay-python) **como herramienta**:

```console hl_lines="1"
$ uv tool install cowsay
Resolved 1 package in 431ms
Prepared 1 package in 121ms
Installed 1 package in 9ms
 + cowsay==6.1
Installed 1 executable: cowsay
```

Al tenerlo instalado de esta manera, su «ejecutable» está disponible para poderlo invocar directamente:

```console
$ cowsay -t holi
  ____
| holi |
  ====
    \
     \
       ^__^
       (oo)\_______
       (__)\       )\/\
           ||----w |
           ||     ||
```

### Listar herramientas

Como era de esperar, hay una forma fácil de listar las herramientas instaladas:

```console hl_lines="1"
$ uv tool list
cowsay v6.1
- cowsay
```

### Borrar herramientas

También tenemos la posibilidad de borrar herramientas ya instaladas:

```console hl_lines="1"
$ uv tool uninstall cowsay
Uninstalled 1 executable: cowsay

$ uv tool list
No tools installed
```

### Actualizar herramientas

De cuando en cuando los paquetes que tenemos instalados (como herramientas) reciben actualizaciones. Es posible actualizar una herramienta de la siguiente manera:

```console hl_lines="1"
$ uv tool upgrade cowsay
Nothing to upgrade
```

### Ejecutar herramientas al vuelo

No es obligatorio instalar una herramienta para poder utilizarlo. Gracias a un rendimiento espectacular de `uv` es posible invocar herramientas al vuelo sin necesidad de tenerlas instaladas previamente.

```console hl_lines="4"
$ uv tool list
No tools installed

$ uv tool run cowsay -t 'al vuelo'
  ________
| al vuelo |
  ========
        \
         \
           ^__^
           (oo)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
```

Al ser algo tan «atractivo» han creado un ~~comando~~ alias para esto:

```console
$ uvx cowsay -t 'al vuelo' #(1)!
  ________
| al vuelo |
  ========
        \
         \
           ^__^
           (oo)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
```
{ .annotate }

1. `uvx` $\equiv$ `uv tool run`

### Python como herramienta

Uno de los casos de uso típico de «herramienta» en `uv` es lanzar una versión específica de Python pero con **dependencias** al vuelo.

Supongamos el siguiente <span class="example">ejemplo:material-flash:</span> en el que nos interesa lanzar un intérprete de Python 3.8 con el paquete `requests`:

```console hl_lines="1"
$ uvx --with requests python@3.8
Installed 5 packages in 27ms
Python 3.8.20 (default, Oct  2 2024, 15:14:40)
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> requests.get('https://aprendepython.es')
<Response [200]>
>>>
```


[^1]: uv proporciona [una interfaz para trabajar con pip](https://docs.astral.sh/uv/pip/).
