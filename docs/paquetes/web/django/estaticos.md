---
icon: material/folder-outline
tags:
  - Paquetes de terceros
  - Desarrollo web
  - Django
---

# Estáticos

<span class="dj-level">:material-signal-cellular-1: Django básico</span>

Los ficheros estáticos («assets») son ficheros que no necesitan un preprocesamiento y que se utilizan «tal cual son». Nos estamos refiriendo a:

- Imágenes.
- Vídeos.
- Fuentes tipográficas.
- Hojas de estilo CSS.
- Código JavaScript.

## Estáticos en desarrollo

Siempre y cuando tengamos activada la aplicación `#!python 'django.contrib.staticfiles'` (_que ya viene por defecto_) Django se encargará de servir los ficheros estáticos cuando así sea necesario.

!!! warning "Producción"

    Esto sólo es válido para un entorno de desarrollo, cuando pasamos a producción habrá que configurar el servidor web correspondiente para gestionar los ficheros estáticos.

## Ubicación

Los ficheros estáticos «deberían» estar ubicados en la carpeta `static` de cada [aplicación](aplicaciones.md) del proyecto. Cuando hacemos referencia a un estático usamos una ruta. Funciona de manera análoga a la [ubicación de las plantillas](plantillas.md#ubicacion).

Una aproximación inicial sería definir una _hoja de estilos_ CSS y una _carpeta de imágenes_ para todo el proyecto. Lo podríamos ubicar por <span class="example">ejemplo:material-flash:</span> en la aplicación [`shared`](aplicaciones.md#aplicacion-compartida) para que los recursos sean compartidos por todo el proyecto:

``` hl_lines="1-2"
shared
└── static
    ├── css
    │   └── base.css
    └── images
        ├── logo.svg
        └── background.png
```

- La ruta para acceder a `base.css` sería `css/base.css`
- La ruta para acceder a `logo.svg` sería `images/logo.svg`

:material-check-all:{ .blue } Django se encargará de rastrear las carpetas `static` de las aplicaciones para encontrar los estáticos indicados. Por lo tanto los **espacios de nombres** también son importantes a la hora de organizar los estáticos de nuestro proyecto Django.

Una buena práctica (en el caso de estáticos específicos de una aplicación concreta) es crear una subcarpeta con el nombre de la aplicación. Supongamos por <span class="example">ejemplo:material-flash:</span> que queremos guardar ciertas imágenes específicas de un «post»:

``` hl_lines="1-3"
posts
└── static
    └── posts
        └── images
            ├── fav.png
            └── like.png
```

- La ruta para acceder a `fav.png` sería `posts/images/fav.png`
- La ruta para acceder a `like.png` sería `posts/images/like.svg`

## Acceso a estáticos

En este apartado veremos cómo acceder a ficheros estáticos tanto desde una plantilla como desde una vista.

Hay dos variables importantes en `settings.py` que definen el comportamiento de los estáticos en un proyecto Django:

- [`STATIC_URL`](https://docs.djangoproject.com/en/stable/ref/settings/#std-setting-STATIC_URL): Define la URL que se utilizará cuando hagamos referencia a un fichero estático. Su valor por defecto es `#!python 'static/'`.
- [`STATICFILES_DIRS`](https://docs.djangoproject.com/en/stable/ref/settings/#std-setting-STATICFILES_DIRS): Define directorios adicionales donde Django irá a buscar ficheros estáticos. Su valor por defecto es `#!python []`.

### Estáticos en plantillas

Para acceder a ficheros estáticos desde una plantilla Django debemos utilizar la etiqueta [`{% static %}`](https://docs.djangoproject.com/en/stable/ref/templates/builtins/#static).

Vamos por <span class="example">ejemplo:material-flash:</span> a definir una hoja de estilos _mínima_ para nuestro proyecto:

```css title="shared/static/css/base.css"
body {
    background-color: beige;
}
```

Ahora tenemos que enlazarla desde la plantilla base de nuestro proyecto:

```htmldjango title="shared/templates/base.html" hl_lines="1 9"
{% load static %}<!--(1)!-->

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{% if title %}{{ title }} | {% endif %}Blog</title>
    <link rel="stylesheet" href="{% static 'css/base.css' %}"><!--(2)!-->
  </head>

  <body>
    {% include "header.html" %}
    <div class="container">
        {% block content %}{% endblock %}
    </div>
  </body>
</html>
```
{ .annotate }

1.  - Es necesario cargar la etiqueta `static`.
    - Debería escribirse al principio de la plantilla, eso sí, siempre después de [`{% extends %}`](plantillas.md#herencia) que debe ser la primera..
2. URL generada: `/static/css/base.css`

Si ahora recargas la página del «blog» podrás ver un bonito color _beige_ de fondo.

!!! tip "Caché"

    Los navegadores web tratan de cachear[^1] todo el contenido que pueden para así acelerar la carga de las páginas. Es por ello que, a veces, no verás reflejados los cambios en ciertos ficheros estáticos.
    
    Si es tu caso, puedes probar a recargar el navegador sin caché:

    === "Windows :fontawesome-brands-windows:"

        <kbd>Ctrl + F5</kbd>
    
    === "Linux :simple-linux:"
    
        <kbd>Ctrl + Shift + R</kbd>
        
    === "macOS :simple-apple:"
    
        <kbd>Cmd + Shift + R</kbd>          


### Estáticos en vistas

Lo más habitual es utilizar ficheros estáticos directamente en plantillas, pero puede darse el caso donde necesitemos acceso a los estáticos en las vistas. Se diferencian dos aproximaciones:

:one: Acceso a la ruta en la URL.  
:two: Acceso a la ruta en el sistema de ficheros.

=== "URL :octicons-browser-16:"

    Para obtener la ruta en la URL de un determinado estático podemos utilizar la misma etiqueta `static` pero desde `django.templatetags.static`.

    Veamos un <span class="example">ejemplo:material-flash:</span>:

    ```python title="posts/views.py"
    from django.templatetags.static import static as static_url#(1)!


    def my_view(request):
        # ...
        like_url_path = static_url('posts/images/like.png')#(2)!
    ```
    { .annotate }

    1. Es necesario importar la función `static()`.
    2. En este caso se devolverá la URL :material-arrow-right-box: `/static/posts/images/like.png`

=== "Sistema de ficheros :fontawesome-solid-floppy-disk:"

    Para obtener la ruta en el sistema de ficheros de un determinado estático podemos utilizar la función `path` desde `django.contrib.staticfiles`.

    Veamos un <span class="example">ejemplo:material-flash:</span>:

    ```python title="posts/views.py"
    from django.contrib.staticfiles.storage import path as static_path #(1)!


    def my_view(request):
        # ...
        like_file_path = static_path('posts/images/like.png')#(2)!
    ```
    { .annotate }

    1. Es necesario importar la función `path()`.
    2. En este caso se devolverá la ruta :material-arrow-right-box: `/home/guido/dev/blog/posts/static/posts/images/like.png`

## Tailwind

<span class="dj-level">:material-signal-cellular-3: Django avanzado</span>

[Tailwind :simple-tailwindcss:](https://tailwindcss.com/) ofrece un conjunto de herramientas que facilitan el desarrollo de interfaces «frontend» para aplicaciones web.

### Instalación

Hay varias maneras de [instalar](https://tailwindcss.com/docs/installation/) Tailwind y de integrarlo en un proyecto Django. En esta sección veremos cómo implantarlo usando [npm :simple-npm:](https://www.npmjs.com/) y acceso a ficheros estáticos.

Lo primero será instalar [tailwind y sus herramientas en línea de comandos](https://tailwindcss.com/docs/installation/tailwind-cli):

```console
$ npm install tailwindcss @tailwindcss/cli #(1)!
```
{ .annotate }

1. Desde el raíz de nuestro proyecto Django.

El comando anterior creará una carpeta `node_modules` con **multitud** de ficheros y subcarpetas, correspondientes a los paquetes *Node* instalados y a todas sus dependencias.

!!! warning "Control de versiones"

    Recuerda excluir la carpeta `node_modules` del control de versiones añadiéndola al fichero `.gitignore` de tu proyecto.

<div class="annotate" markdown>
También se crearán dos ficheros de seguimiento de paquetes (1):

- `package.json` que almacena las versiones (mínimas) de los paquetes instalados.
- `package-lock.json` que almacena las dependencias de los paquetes instalados.
</div>

1. En el caso de utilizar [`uv`](../../../entornos/ide/uv.md) (gestión de paquetería Python), podríamos decir que:

    - `package.json` $\approx$ `pyproject.toml`
    - `package-lock.json` $\approx$ `uv.lock`

### Configuración

Debemos crear alguna hoja de estilos desde la que importemos _tailwind_:

```css title="shared/static/css/app.css"
@import "tailwindcss";
```

La parte «curiosa» que tiene Tailwind es que «rastrea» nuestro HTML en busca de clases CSS que le «pertenezcan». Así, una vez identificadas, genera un CSS de salida que realmente es el que deberemos incluir en nuestras plantillas.

Por tanto necesitamos **lanzar un proceso** (en el entorno de desarrollo) que «escuche» los cambios que realizamos en las plantillas y se encargue de regenerar (compilar) esas reglas de estilo.

En nuestro <span class="example">ejemplo:material-flash:</span> ejecutaremos el siguiente comando:

```console
$ npx tailwindcss -i shared/static/css/app.css -o shared/static/css/tailwind.css --watch
```

??? abstract "justfile"

    Consulta la receta [`tailwind-watch`](justfile.md#justfile-para-django) para incluirla en tu `justfile`.

Aquí identificamos tres elementos:

1. `app.css` es el «punto de entrada» (_input_).
2. `tailwind.css` es el fichero generado/compilado (_output_).
3. Mantenemos una «escucha» a los cambios (_watch_).

??? note "Producción"

    En un entorno de producción no es necesario «escuchar» los cambios, lo único que necesitamos es generar directamente el fichero compilado CSS:

    ```console
    $ npx tailwindcss -i shared/static/css/app.css -o shared/static/css/tailwind.css
    ```

    ??? abstract "justfile"

        Consulta la receta [`tailwind`](justfile.md#justfile-para-django) para incluirla en tu `justfile`.

### Plantillas

Ya solo nos queda incluir el fichero _tailwind_ procesado de reglas CSS en nuestras plantillas.

Para el <span class="example">ejemplo:material-flash:</span> del «blog» usaremos la plantilla base:

```htmldjango title="shared/templates/base.html" hl_lines="9"
{% load static %}

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title></title>
    <link rel="stylesheet" href="{% static 'css/tailwind.css' %}"><!--(1)!-->
    <link rel="stylesheet" href="{% static 'css/custom.css' %}"><!--(2)!-->
  </head>

  <body>
    <div class="container">
      {% block content %}
      {% endblock %}
    </div>
  </body>
</html>
```
{ .annotate }

1. Enlazamos el archivo compilado de Tailwind.
2. Podemos enlazar estilos propios CSS.

Así todas las plantillas que hereden de `base.html` dispondrán del enorme catálogo de clases Tailwind para mejorar la interfaz de usuario.

### Modo de uso

La [documentación](https://tailwindcss.com/docs/) de Tailwind es muy completa y explica cada una de las muchas clases CSS que pone a disposición.

Un <span class="example">ejemplo:material-flash:</span> sencillo sería modificar el color de fondo de nuestro «blog»:

```htmldjango title="shared/templates/base.html" hl_lines="13"
{% load static %}

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title></title>
    <link rel="stylesheet" href="{% static 'css/tailwind.css' %}">
    <link rel="stylesheet" href="{% static 'css/custom.css' %}">
  </head>

  <body class="bg-violet-300"><!--(1)!-->
    <div class="container">
      {% block content %}
      {% endblock %}
    </div>
  </body>
</html>
```
{ .annotate }

3. Añadimos un fondo de [color](https://tailwindcss.com/docs/colors) violeta claro.

## Lucide

<span class="dj-level">:material-signal-cellular-3: Django avanzado</span>

Siempre resulta útil disponer de un conjunto de iconos para utilizar en el «frontend» de nuestros proyectos web. Lamentablemente Tailwind no dispone de iconos «propios» con lo que necesitamos alguna librería externa.

Hay cientos de recursos para incorporar iconos, pero en este caso me centraré en [Lucide :simple-lucide:](https://lucide.dev/). Se trata de un proyecto con mucha relevancia y que incorpora gran cantidad de iconos.

### Instalación

Lucide proporciona distintos [paquetes](https://lucide.dev/packages) en función del _framework_ «frontend» que estemos utilizando. Para este <span class="example">ejemplo:material-flash:</span> vamos a utilizar la [versión estática](https://lucide.dev/guide/static/):

```console
$ npm install lucide-static #(1)!
```
{ .annotate }

1. Desde el raíz de nuestro proyecto Django.

El comando anterior creará una carpeta `node_modules` con **multitud** de ficheros y subcarpetas, correspondientes a los paquetes *Node* instalados y a todas sus dependencias.

!!! warning "Control de versiones"

    Recuerda excluir la carpeta `node_modules` del control de versiones añadiéndola al fichero `.gitignore` de tu proyecto.

### Configuración

Para poder acceder a los archivos creados en `node_modules` desde las plantillas Django, necesitamos especificar en la configuración del proyecto que dicha carpeta contiene **estáticos**.

Para ello añadimos la siguiente línea al fichero `settings.py`:

```python title="main/settings.py"
STATICFILES_DIRS = [BASE_DIR / 'node_modules']#(1)!
```
{ .annotate }

1.  - Esta variable permite añadir **rutas extras** donde Django irá a buscar ficheros estáticos.
    - Puedes añadirla donde quieras, pero un buen lugar podría ser junto a la variable `STATIC_URL`.

### Plantillas

Simplemente necesitamos cargar el archivo `lucide.css` desde nuestra plantilla base:

```htmldjango title="shared/templates/base.html" hl_lines="10"
{% load static %}

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title></title>
    <link rel="stylesheet" href="{% static 'css/tailwind.css' %}">
    <link rel="stylesheet" href="{% static 'lucide-static/font/lucide.css' %}">
    <link rel="stylesheet" href="{% static 'css/custom.css' %}">
  </head>

  <body class="bg-violet-300">
    <div class="container">
      {% block content %}
      {% endblock %}
    </div>
  </body>
  <footer >
</html>
```

### Modo de uso

Para incluir un icono en una plantilla de nuestro proyecto, primero tendremos que [buscar](https://lucide.dev/icons/) en la web de Lucide y localizar el **identificador del icono**.

Por <span class="example">ejemplo:material-flash:</span> vamos a incluir el icono :lucide-archive: cuyo identificador es [`archive`](https://lucide.dev/icons/archive) en el listado de «posts» de nuestro blog. Para ello usaremos una etiqueta `#!html <i class="icon-archive"></i>` siempre con el prefijo `icon` en la clase CSS:

```htmldjango title="posts/templates/posts/post/list.html" hl_lines="3"
<ul>
    {% for post in posts %}
        <li><i class="icon-archive"></i> {{ post }}</li>
    {% endfor %}
</ul>
```

??? tip "Etiqueta de plantilla"

    Aquí podría ser muy útil implementar una [etiqueta personalizada simple de plantilla](plantillas.md#devolviendo-html) que devolviera el código HTML del icono a partir de su identificador:

    === "Etiqueta"
    
        ```python title="shared/templatetags/shared_extras.py"
        from django import template
        from django.utils.html import format_html
        
        register = template.Library()
        
        
        @register.simple_tag
        def icon(icon_id: str) -> str:
            return format_html('<i class="icon-{}"></i>', icon_id)
        ```
    
    === "Plantilla"
    
        ```htmldjango title="posts/templates/posts/post/list.html" hl_lines="1 5"
        {% load shared_extras %}

        <ul>
            {% for post in posts %}
                <li>{% icon "archive" %} {{ post }}</li>
            {% endfor %}
        </ul>
        ```


## Bootstrap

<span class="dj-level">:material-signal-cellular-3: Django avanzado</span>

[Bootstrap :simple-bootstrap:](https://getbootstrap.com/) ofrece un conjunto de herramientas que facilitan el desarrollo de interfaces «frontend» para aplicaciones web.

> En el momento de la escritura de este documento, **Bootstrap** figura entre los 30 proyectos con más :star: de GitHub[^2].

### Instalación

Hay varias maneras de instalar Bootstrap y de integrarlo en un proyecto Django. En esta sección veremos cómo implantarlo usando [npm :simple-npm:](https://www.npmjs.com/) y acceso a ficheros estáticos.

Lo primero será [instalar](https://getbootstrap.com/docs/5.3/getting-started/download/#npm) los paquetes _JavaScript_ correspondientes:

```console
$ npm install bootstrap bootstrap-icons #(1)!
```
{ .annotate }

1. Desde el raíz de nuestro proyecto Django.

<div class="annotate" markdown>
También se crearán dos ficheros de seguimiento de paquetes (1):

- `package.json` que almacena las versiones (mínimas) de los paquetes instalados.
- `package-lock.json` que almacena las dependencias de los paquetes instalados.
</div>

1. En el caso de utilizar [`uv`](https://docs.astral.sh/uv/) (gestión de paquetería Python), podríamos decir que:

    - `package.json` $\approx$ `pyproject.toml`
    - `package-lock.json` $\approx$ `uv.lock`

### Configuración

Para poder acceder a los archivos creados en `node_modules` desde las plantillas Django, necesitamos especificar en la configuración del proyecto que dicha carpeta contiene **estáticos**.

Para ello añadimos la siguiente línea al fichero `settings.py`:

```python title="main/settings.py"
STATICFILES_DIRS = [BASE_DIR / 'node_modules']#(1)!
```
{ .annotate }

1.  - Esta variable permite añadir **rutas extras** donde Django irá a buscar ficheros estáticos.
    - Puedes añadirla donde quieras, pero un buen lugar podría ser junto a la variable `STATIC_URL`.

### Plantillas

Dado que Bootstrap utiliza ficheros `.css` y `.js` necesitamos cargarlos correctamente desde nuestras plantillas.

Suponiendo que disponemos de una [plantilla base](plantillas.md#herencia) tendríamos que añadir lo siguiente:

```htmldjango title="shared/templates/base.html" hl_lines="1 9-10 21"
{% load static %}<!--(1)!-->

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title></title>
    <link rel="stylesheet" href="{% static 'bootstrap/dist/css/bootstrap.min.css' %}"><!--(2)!-->
    <link rel="stylesheet" href="{% static 'bootstrap-icons/font/bootstrap-icons.min.css' %}"><!--(3)!-->
    <link rel="stylesheet" href="{% static 'css/custom.css' %}"><!--(4)!-->
  </head>

  <body>
    <div class="container"><!--(5)!-->
      {% block content %}
      {% endblock %}
    </div>
  </body>

  <script type="text/javascript" src="{% static 'bootstrap/dist/js/bootstrap.bundle.min.js' %}"></script><!--(6)!-->
</html>
```
{ .annotate }

1. Necesitamos cargar las utilidades para estáticos.
2. Cargamos los estilos de Bootstrap.
3. Cargamos los iconos de Bootstrap.
4. Cargamos estilos propios (opcional).
5. La clase [`container`](https://getbootstrap.com/docs/5.3/layout/containers/) es el bloque fundamental de Bootstrap.
6. Cargamos los scripts de Bootstrap.

:material-check-all:{ .blue } A partir de aquí ya podremos usar [todos los recursos](https://getbootstrap.com/docs/) que nos proporciona Bootstrap para diseñar una interfaz de usuario moderna, responsiva y funcional.

### Modales

La implementación de **ventanas modales** suele ser una estrategia interesante para confirmar acciones y mostrar mensajes informativos.

A continuación se presenta una _propuesta_ de modal con _Bootstrap_ mediante una [etiqueta personalizada](plantillas.md#etiquetas-personalizadas) poniendo como <span class="example">ejemplo:material-flash:</span> de uso su aplicación al ^^borrar un «post» del «blog»^^:

=== "Etiqueta"

    ```python title="shared/templates/shared_extras.py"
    import uuid

    from django import template
    from django.urls import reverse

    register = template.Library()


    @register.inclusion_tag('includes/modal.html')
    def modal(
        btn_text,#(1)!
        url,#(2)!
        *url_args,#(3)!
        title='Attention',#(4)!
        body='Are you sure to continue?',#(5)!
        action='Continue',#(6)!
        btn_classes='btn btn-primary',#(7)!
        btn_icon='',#(8)!
    ):
        url = reverse(url, args=url_args)
        modal_id = uuid.uuid4()
        return dict(
            modal_id=modal_id,
            title=title,
            body=body,
            action=action,
            url=url,
            btn_text=btn_text,
            btn_classes=btn_classes,
            btn_icon=btn_icon,
        )
    ```
    { .annotate }
    
    1. Texto del botón que lanza el modal.
    2. Nombre de URL a ejecutar si se «confirma» el modal.
    3. Argumentos para conformar la URL.
    4. Título de la ventana modal.
    5. Texto para el cuerpo de la ventana modal.
    6. Texto del botón de confirmación en la ventana modal.
    7. Clases CSS a aplicar sobre el botón que lanza el modal.
    8. Icono a mostrar en el botón que lanza el modal.

=== "Plantilla"

    ```htmldjango title="shared/templates/includes/modal.html"
    <!-- ↓ Button to launch modal -->
    <button type="button" class="{{ btn_classes }}" data-bs-toggle="modal" data-bs-target="#{{ modal_id }}">
      <i class="{{ btn_icon }}"></i>
      {{ btn_text }}
    </button>
    
    <!-- ↓ Modal window -->
    <div class="modal fade" id="{{ modal_id }}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">{{ title }}</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            {{ body }}
          </div>
          <div class="modal-footer">
            <a href="{{ url }}" class="btn btn-primary">{{ action }}</a>
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
    ```

=== "Modo de uso"

    ```htmldjango title="posts/templates/posts/post/delete.html"
    {% modal
        "Delete post"
        "posts:delete-post" post.slug
        title="Confirm"
        body="Do you want to delete this post?"
        btn_classes="btn btn-danger btn-sm"
        btn_icon="bi bi-journal-x"
    %}
    ```   



[^1]: Guardar copias de datos de forma temporal en una ubicación de almacenamiento más rápida.
[^2]: Información via [git-stars.org](https://git-stars.org/es/repositories).
