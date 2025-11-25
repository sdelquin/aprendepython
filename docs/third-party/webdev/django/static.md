---
icon: material/folder-outline
---

# Estáticos { #static }

<span class="djversion basic">:simple-django: Básico :material-tag-multiple-outline:</span>

Los ficheros estáticos («assets») son ficheros que no necesitan un preprocesamiento y que se utilizan «tal cual son». Nos estamos refiriendo a:

- Imágenes.
- Vídeos.
- Fuentes tipográficas.
- Hojas de estilo CSS.
- Código JavaScript.

## Estáticos en desarrollo { #static-during-development }

Siempre y cuando tengamos activada la aplicación `#!python 'django.contrib.staticfiles'` (_que ya viene por defecto_) Django se encargará de servir los ficheros estáticos cuando así sea necesario.

!!! warning "Producción"

    Esto sólo es válido para un entorno de desarrollo, cuando pasamos a producción habrá que configurar el servidor web correspondiente para gestionar los ficheros estáticos.

## Ubicación { #location }

Los ficheros estáticos «deberían» estar ubicados en la carpeta `static` de cada [aplicación](apps.md) del proyecto. Cuando hacemos referencia a un estático usamos una ruta. Funciona de manera análoga a la [ubicación de las plantillas](templates.md#location).

Una aproximación inicial sería definir una _hoja de estilos_ CSS y una _carpeta de imágenes_ para todo el proyecto. Lo podríamos ubicar por <span class="example">ejemplo:material-flash:</span> en la aplicación [`shared`](apps.md#shared) para que los recursos sean compartidos por todo el proyecto:

``` hl_lines="1-2"
shared
└── static
    ├── css
    │   └── base.css
    └── images
        ├── logo.svg
        └── background.png
```

- La ruta para acceder a `base.css` sería `css/custom.css`
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

## Acceso a estáticos { #access }

En este apartado veremos cómo acceder a ficheros estáticos tanto desde una plantilla como desde una vista.

Hay dos variables importantes en `settings.py` que definen el comportamiento de los estáticos en un proyecto Django:

- [`STATIC_URL`](https://docs.djangoproject.com/en/stable/ref/settings/#std-setting-STATIC_URL): Define la URL que se utilizará cuando hagamos referencia a un fichero estático. Su valor por defecto es `#!python 'static/'`.
- [`STATICFILES_DIRS`](https://docs.djangoproject.com/en/stable/ref/settings/#std-setting-STATICFILES_DIRS): Define directorios adicionales donde Django irá a buscar ficheros estáticos. Su valor por defecto es `#!python []`.

### Estáticos en plantillas { #template-usage }

Para acceder a ficheros estáticos desde una plantilla Django debemos utilizar la etiqueta [`{% static %}`](https://docs.djangoproject.com/en/stable/ref/templates/builtins/#static).

Supongamos que tratamos de acceder a los ficheros estáticos definidos en el <span class="example">ejemplo:material-flash:</span> anterior del «blog»:

```htmldjango title="shared/templates/base.html" hl_lines="1 9 14 19"
{% load static %}<!--(1)!-->

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Blog</title>
    <link rel="stylesheet" href="{% static 'css/base.css' %}"><!--(2)!-->
  </head>

  <body>
    <header>
        <img src="{% static 'images/logo.svg' %}"/><!--(3)!-->
    </header>

    <p>
        I like this post
        <img src="{% static 'posts/images/like.png' %}"/><!--(4)!-->
    </p>
  </body>
</html>
```
{ .annotate }

1.  - Es necesario cargar la etiqueta `static`.
    - Debería escribirse al principio de la plantilla, eso sí, siempre después de [`{% extends %}`](templates.md#inheritance) que debe ser la primera..
2. URL generada: `/static/css/base.css`
3. URL generada: `/static/images/logo.svg`
4. URL generada: :material-arrow-right-box: `/static/posts/images/like.png`

!!! tip "Caché"

    Los navegadores web tratan de cachear[^1] todo el contenido que pueden para así acelerar la carga de las páginas. Es por ello que, a veces, no verás reflejados los cambios en ciertos ficheros estáticos.
    
    Si es tu caso, puedes probar a recargar el navegador sin caché:

    === "Windows :fontawesome-brands-windows:"

        <kbd>Ctrl + F5</kbd>
    
    === "Linux :simple-linux:"
    
        <kbd>Ctrl + F5</kbd>
        
    === "macOS :simple-apple:"
    
        <kbd>Cmd + Shift + R</kbd>          


### Estáticos en vistas { #view-usage }

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

## Bootstrap { #bootstrap }

<span class="djversion advanced">:simple-django: Avanzado :material-tag-multiple-outline:</span>

[Bootstrap :simple-bootstrap:](https://getbootstrap.com/) ofrece un conjunto de herramientas que facilitan el desarrollo de interfaces «frontend» para aplicaciones web.

### Instalación { #install-bootstrap }

Hay varias maneras de instalar Bootstrap y de integrarlo en un proyecto Django. En esta sección veremos cómo implantarlo usando [npm :simple-npm:](https://www.npmjs.com/) y acceso a ficheros estáticos.

Lo primero será [instalar](https://getbootstrap.com/docs/5.3/getting-started/download/#npm) los paquetes _JavaScript_ correspondientes:

```console
$ npm install bootstrap bootstrap-icons #(1)!
```
{ .annotate }

1. Desde el raíz de nuestro proyecto Django.

El comando anterior creará una carpeta `node_modules` con **multitud** de ficheros y subcarpetas, correspondientes a los paquetes *Node* instalados y a todas sus dependencias.

También creará dos ficheros `package.json` y `package-lock.json` donde quedan fijadas las versiones de los paquetes instalados.

!!! warning "Control de versiones"

    Recuerda excluir la carpeta `node_modules` del control de versiones añadiéndola al fichero `.gitignore` de tu proyecto.

### Configuración { #config-bootstrap }

Para poder acceder a los archivos creados en `node_modules` desde las plantillas Django, necesitamos especificar en la configuración del proyecto que dicha carpeta contiene **estáticos**.

Para ello añadimos la siguiente línea al fichero `settings.py`:

```python title="main/settings.py"
STATICFILES_DIRS = [BASE_DIR / 'node_modules']#(1)!
```
{ .annotate }

1. Esta variable permite añadir **rutas extras** donde Django irá a buscar ficheros estáticos.

### Plantillas { #templates-bootstrap }

Dado que Bootstrap utiliza ficheros `.css` y `.js` necesitamos cargarlos correctamente desde nuestras plantillas.

Suponiendo que disponemos de una [plantilla base](templates.md#inheritance) tendríamos que añadir lo siguiente:

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

:material-check-all:{ .blue } A partir de aquí ya podremos usar todos los recursos que nos proporciona Bootstrap para diseñar una interfaz de usuario moderna, responsiva y funcional.

[^1]: Guardar copias de datos de forma temporal en una ubicación de almacenamiento más rápida.
