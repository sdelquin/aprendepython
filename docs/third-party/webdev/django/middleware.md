---
icon: material/middleware-outline
---

# Middleware { #middleware }

<span class="djversion intermediate">:simple-django: Intermedio :material-tag-multiple-outline:</span>

Un [«middleware»](https://docs.djangoproject.com/en/stable/topics/http/middleware/) —en el contexto de Django— es un artefacto de software que se sitúa entre la petición y la respuesta HTTP y permite alterar la entrada o la salida a conveniencia de manera global.

``` mermaid
graph LR
  req[HttpRequest] --> middleware[Middleware]
  middleware --> resp[HttpResponse]
```

## Middleware disponible { #available-middleware }

Django proporciona una serie de [«middleware» predefinido](https://docs.djangoproject.com/en/stable/ref/middleware/) que podemos **activar** bajo demanda.

Si nos fijamos en un proyecto nuevo («fresh») de Django podremos observar que muchos de estos «middleware» ya se encuentran activados por defecto:

```python title="main/settings.py"
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

Cada «middleware» define una o varias clases que aportan distintas funcionalidades:

| Middleware | Ruta | Descripción | ¿Por defecto? |
| --- | --- | --- | --- |
| [Cache](https://docs.djangoproject.com/en/stable/ref/middleware/#module-django.middleware.cache) | `#!python 'django.middleware.cache.UpdateCacheMiddleware'`<br>`#!python 'django.middleware.cache.FetchFromCacheMiddleware'` | Habilita la caché de Django | :material-cancel:{.red} |
| [Common](https://docs.djangoproject.com/en/stable/ref/middleware/#module-django.middleware.common) | `#!python 'django.middleware.common.CommonMiddleware'` | Realiza distintas acciones comunes | :material-check:{.green} |
| [GZip](https://docs.djangoproject.com/en/stable/ref/middleware/#module-django.middleware.gzip) | `#!python 'django.middleware.gzip.GZipMiddleware'` | Comprime contenido en formato [GZip](https://es.wikipedia.org/wiki/Gzip) | :material-cancel:{.red} |
| [Conditional GET](https://docs.djangoproject.com/en/stable/ref/middleware/#module-django.middleware.http) | `#!python 'django.middleware.http.ConditionalGetMiddleware'` | Maneja operaciones GET condicionales | :material-cancel:{.red} |
| [Locale](https://docs.djangoproject.com/en/stable/ref/middleware/#module-django.middleware.locale) | `#!python 'django.middleware.locale.LocaleMiddleware'` | Habilita la selección de idioma sobre los datos de la petición | :material-cancel:{.red} |
| [Message](https://docs.djangoproject.com/en/stable/ref/middleware/#module-django.contrib.messages.middleware) | `#!python 'django.contrib.messages.middleware.MessageMiddleware'` | Habilita el soporte para mensajes | :material-check:{.green} |
| [Security](https://docs.djangoproject.com/en/stable/ref/middleware/#module-django.middleware.security) | `#!python 'django.middleware.security.SecurityMiddleware'` | Proporciona mejoras de seguridad al ciclo petición/respuesta | :material-check:{.green} |
| [Session](https://docs.djangoproject.com/en/stable/ref/middleware/#module-django.contrib.sessions.middleware) | `#!python 'django.contrib.sessions.middleware.SessionMiddleware'` | Habilita el soporte de sesiones | :material-check:{.green} |
| [Site](https://docs.djangoproject.com/en/stable/ref/middleware/#module-django.contrib.sites.middleware) | `#!python 'django.contrib.sites.middleware.CurrentSiteMiddleware'` | Añade el atributo `site` a la petición | :material-cancel:{.red} |
| [Authentication](https://docs.djangoproject.com/en/stable/ref/middleware/#module-django.contrib.auth.middleware) | `#!python 'django.contrib.auth.middleware.AuthenticationMiddleware'`<br>`#!python 'django.contrib.auth.middleware.LoginRequiredMiddleware'`<br>`#!python 'django.contrib.auth.middleware.RemoteUserMiddleware'`<br>`#!python 'django.contrib.auth.middleware.PersistentRemoteUserMiddleware'` | Habilita los mecanismos de autenticación |  :material-check:{.green} |
| [CSRF protection](https://docs.djangoproject.com/en/stable/ref/middleware/#csrf-protection-middleware) | `#!python 'django.middleware.csrf.CsrfViewMiddleware'` | Añade protección contra CSRF | :material-check:{.green} |
| [X-Frame-Options](https://docs.djangoproject.com/en/stable/ref/middleware/#x-frame-options-middleware) | `#!python 'django.middleware.clickjacking.XFrameOptionsMiddleware'` | Añade protección simple contra [«clickjacking»](https://en.wikipedia.org/wiki/Clickjacking) | :material-check:{.green} |

### Mensajes { #message-middleware }

El [«middleware» de mensajes](https://docs.djangoproject.com/en/stable/ref/contrib/messages/) permite crear y publicar mensajes en nuestro proyecto web de manera rápida y sencilla.

Django ya lo tiene habilitado _por defecto_, pero si no fuera así, para activarlo simplemente tendríamos que añadirlo a la lista [`MIDDLEWARE`](https://docs.djangoproject.com/en/stable/ref/settings/#std-setting-MIDDLEWARE) en el fichero de configuraciones:

```python title="main/settings.py" hl_lines="7"
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

Mediante este «middleware» Django proporciona un objeto `messages` (disponible en vistas y plantillas) que contendrá la lista de mensajes que queremos notificar.

Para cada mensaje podemos indicar el [nivel informativo](https://docs.djangoproject.com/en/stable/ref/contrib/messages/#message-tags) asociado. El módulo `messages` dentro de `django.contrib` contiene las siguientes constantes:

| Nivel | Etiqueta | Objetivo |
| --- | --- | --- |
| `DEBUG` | `debug` | Mensaje de depuración |
| `INFO` | `info` | Mensajes informativo |
| `SUCCESS` | `success` | Mensaje de operación exitosa |
| `WARNING` | `warning` | Mensaje de advertencia |
| `ERROR` | `error` | Mensaje de error |

Supongamos un <span class="example">ejemplo:material-flash:</span> en el que queremos notificar al usuario que el «post» de un «blog» ha sido borrado satisfactoriamente (o no):

=== "Vista"

    ```python title="posts/views.py" hl_lines="1 11 13"
    from django.contrib import messages#(1)!
    from django.shortcuts import render

    from .models import Post


    def delete_post(request, post_slug: str):
        try:
            post = Post.objects.get(slug=post_slug)
            post.delete()
            messages.success(request, 'Post deleted successfully')#(2)!
        except Post.DoesNotExist:
            messages.error(request, 'Post does not exist')#(3)!
        posts = Post.objects.all()
        return render(request, 'posts/post/list.html', {'posts': posts})#(4)!
    ```
    { .annotate }
    
    1. Importamos el objeto `messages` para gestionar los mensajes.
    2.  - Añadimos un **mensaje de éxito** mediante el método [`add_message()`](https://docs.djangoproject.com/en/stable/ref/contrib/messages/#django.contrib.messages.add_message).
        - Atajo para: `#!python messages.add_message(request, messages.SUCCESS, 'Post delete successfully')`
    3.  - Añadimos un **mensaje de error** mediante el método [`add_message()`](https://docs.djangoproject.com/en/stable/ref/contrib/messages/#django.contrib.messages.add_message).
        - Atajo para: `#!python messages.add_message(request, messages.ERROR, 'Post does not exist')`
    4. No es necesario incluir los mensajes en el contexto porque el «middleware» ya se encarga de ello.

=== "Plantilla"

    ```htmldjango title="posts/post/list.html" hl_lines="1-9"
    {% if messages %}
    <ul class="messages">
        {% for message in messages %}
            <li{% if message.tags %} class="{{ message.tags }}"{% endif %}><!--(1)!-->
                {{ message }}
            </li>
        {% endfor %}
    </ul>
    {% endif %}

    <ul class="posts">
    {% for post in posts %}
        <li><a href="{% url 'posts:post-detail' post.slug %}">{{ post.title }}</a></li>
    {% endfor %}
    </ul>
    ```
    { .annotate }
    
    1. Cada mensaje dispone de una etiqueta `tag` que se está usando como _clase CSS_ del mensaje.

    El código HTML generado para el bloque de mensajes es similar a:

    ```html
    <ul class="messages">
        <li class="success">
            Post deleted successfully
        </li>
    </ul>
    ```

    :material-check-all:{ .blue } El bloque de mensajes `#!html <ul>...</ul>` es apropiado para [incluirlo](templates.md#include) en plantillas base.

## Middleware personalizado { #custom-middleware }

<span class="djversion advanced">:simple-django: Avanzado :material-tag-multiple-outline:</span>

Más allá de los [«middleware» existentes](#available-middleware) en Django, es posible implementar un «middleware» personalizado para aquellas tareas que sean necesarias aplicar de manera global en el ciclo petición/respuesta.

Lo único que necesitamos hacer es escribir una clase sobreescribiendo unos ciertos métodos predefinidos y activar el citado «middleware».

Imaginemos un <span class="example">ejemplo:material-flash:</span> en el que queremos medir el tiempo de carga de cada petición en el proyecto del «blog»:

=== "Middleware"

    ```python title="shared/middleware.py"
    import time
    import logging

    logger = logging.getLogger(__name__)#(1)!


    class RequestTimeMiddleware:#(2)!
        def __init__(self, get_response):#(3)!
            self.get_response = get_response
        
        def __call__(self, request):#(4)!
            # Code execution before view calling ↓
            start_time = time.time()
            # View calling ↓
            response = self.get_response(request)
            # Code execution after view calling ↓
            duration = time.time() - start_time
            logger.info(f'Request to {request.path} took {duration:.4f} seconds')
            return response
        
        def process_exception(self, request, exception):#(5)!
            ...
    ```    
    { .annotate }
    
    1. Utilizamos las herramientas de [logging](https://docs.djangoproject.com/en/stable/topics/logging/) que proporciona Django.
    2. Por convención se suele añadir el sufijo `Middleware` al nombre de la clase que implementa el «middleware».
    3. El constructor recibe la función [`get_response()`](https://docs.djangoproject.com/en/stable/topics/http/middleware/#init-get-response).
    4.  - Podríamos decir que el método `__call__()` es el punto más interesante donde podemos modificar «cosas».
        - Recibe la petición HTTP como `request`.
    5.  - El método [`process_exception()`](https://docs.djangoproject.com/en/stable/topics/http/middleware/#process-exception) se llama cuando una vista lanza una excepción.
        - Recibe la petición HTTP como `request` y la excepción lanzada como `exception`.
    
=== "Activación"

    ```python title="main/settings.py" hl_lines="9"
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'shared.middleware.RequestTimeMiddleware'
    ] 
    ```

Ahora cada vez que se realice una petición a nuestro «blog» quedará registrado su tiempo de carga por pantalla.
