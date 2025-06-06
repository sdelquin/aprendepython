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

Siempre y cuando tengamos activada la aplicación `#!python 'django.contrib.staticfiles'` (_que ya viene por defecto_) Django se encarga de servir los ficheros estáticos cuando así sea necesario.

!!! warning "Producción"

    Esto sólo es válido para un entorno de desarrollo, cuando pasamos a producción habrá que configurar el servidor web correspondiente para gestionar los ficheros estáticos.

## Ubicación { #location }

Los ficheros estáticos «deberían» estar ubicados en la carpeta `static` de cada [aplicación](apps.md) del proyecto. Cuando hacemos referencia a un estático usamos una ruta. Funciona de manera análoga a la [ubicación de las plantillas](templates.md#location).

Por <span class="example">ejemplo:material-flash:</span> en una aplicación `posts` para un proyecto de «blog» podríamos tener la siguiente estructura de estáticos:

```hl_lines="3 5"
posts
└── static
    ├── blog.svg
    └── posts
        └── book.svg
```

- La ruta para acceder a `blog.svg` sería `blog.svg`
- La ruta para acceder a `book.svg` sería `posts/book.svg`

Django se encarga de rastrear las carpetas `static` de las aplicaciones para encontrar los estáticos indicados.

:material-check-all:{ .blue } Por lo tanto los **espacios de nombres** también son importantes a la hora de organizar los estáticos de nuestro proyecto Django.

## Acceso a estáticos { #access }

En este apartado veremos cómo acceder a ficheros estáticos tanto desde una plantilla como desde una vista.

### Estáticos en plantillas { #template-usage }

Para acceder a ficheros estáticos desde una plantilla Django debemos utilizar la etiqueta [`{% static %}`](https://docs.djangoproject.com/en/stable/ref/templates/builtins/#static).

Supongamos que tratamos de acceder a las imágenes (ficheros estáticos) definidas en el <span class="example">ejemplo:material-flash:</span> anterior del «blog»:

```htmldjango 
{% load static %}<!--(1)!-->

<img src="<% static 'blog.svg' %>"/><!--(2)!-->
<img src="<% static 'posts/blog.svg' %>"/><!--(3)!-->
```
{ .annotate }

1. Es necesario cargar la etiqueta `static`.
2. Acceso a un fichero estático. En este caso se generará la URL :material-arrow-right-box: `/static/blog.svg`
3. Acceso a un fichero estático. En este caso se generará la URL :material-arrow-right-box: `/static/posts/blog.svg`

### Estáticos en vistas { #view-usage }

Para acceder a ficheros estáticos desde una vista Django debemos utilizar 

## Bootstrap { #bootstrap }

<span class="djversion advanced">:simple-django: Avanzado :material-tag-multiple-outline:</span>

[Bootstrap :simple-bootstrap:](https://getbootstrap.com/) ofrece un conjunto de herramientas que facilitan el desarrollo de interfaces «frontend» para aplicaciones web.

### Instalación { #install-bootstrap }

Hay varias maneras de instalar Bootstrap y de integrarlo en un proyecto Django. En esta sección veremos cómo implantarlo usando [npm :simple-npm:](https://www.npmjs.com/) y acceso a ficheros estáticos.

Lo primero será [instalar](https://getbootstrap.com/docs/5.3/getting-started/download/#npm) los paquetes _JavaScript_ correspondientes:

```bash
npm install bootstrap bootstrap-icons #(1)!
```
{ .annotate }

1. Desde el raíz de nuestro proyecto Django.

El comando anterior creará una carpeta `node_modules` con **multitud** de ficheros y carpetas, correspondientes a los paquetes instalados y a todas sus dependencias.

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
