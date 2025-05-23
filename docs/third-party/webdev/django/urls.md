---
icon: fontawesome/solid/arrows-to-dot
---

# URLs { #urls }

<span class="djversion basic">:simple-django: Básico :material-tag-multiple-outline:</span>

Cuando Django recibe una petición HTTP lo primero que hace es intentar encontrar el patrón que coincide con la URL solicitada. En esta sección veremos cómo configurar estos patrones para lanzar las acciones oportunas.

## URLs de primer nivel { #main-urls }

Si hemos [creado el proyecto](setup.md#create-project) Django con la carpeta base `main` podremos encontrar las **URLs de primer nivel** en el fichero `main/urls.py`.

El contenido (por defecto) de este fichero es el siguiente:

```python title="main/urls.py"
from django.contrib import admin#(1)!

urlpatterns = [#(2)!
    path('admin/', admin.site.urls),#(3)!
]
```
{ .annotate }

1. Este módulo contiene las funcionalidades de la interfaz administrativa de Django.
2. Las URLs deben almacenarse en una **lista** con nombre **`urlpatterns`**.
3.  - Cada URL viene definida por la función [path](https://docs.djangoproject.com/en/stable/ref/urls/#path) que vincula (en general) una ruta con una vista.
    - En este caso se indica que si la URL de entrada es `/admin/` se pase el control al módulo [admin.site.urls](https://github.com/django/django/blob/main/django/contrib/admin/sites.py#L318).

## URLs de segundo nivel { #app-urls }

Cada aplicación de un proyecto Django puede tener sus propias URLs que definen el comportamiento de la misma.

Supongamos por <span class="example">ejemplo:material-flash:</span> que estamos desarrollando una aplicación llamada `posts` y queremos que las siguientes URLs cobren vida:

<div class="annotate" markdown>
- `/posts/`#(1)!
- `/posts/this-is-a-new-post/`#(2)!
</div>
1. Listado de todos los «posts» del «blog».
2. Detalle de un «post» en concreto con el slug `this-is-a-new-post`.

Lo primero será tocar el fichero de configuración de las [URLs de primer nivel](#main-urls) para añadir la delegación a la aplicación correspondiente:

```python title="main/urls.py" hl_lines="6"
from django.contrib import admin
from django.url import include#(1)!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls'))#(2)!
]
```
{ .annotate }

1. Importamos la función `include()`.
2.  - Indicamos que las URLs que comiencen por `/posts/` deben delegarse a las URLs de segundo nivel que están en `posts/urls.py`.
    - Las urls se especifican usando una cadena de texto «cualificada».
    - Cabe la posibilidad de especificar un argumento `namespace` para sobreescribir el valor asignado a `app_name` (`urls.py`).

!!! warning "Barra final"

    Para evitar problemas, recuerda siempre acabar las URLs con la barra `/` del final.  
    Por <span class="example">ejemplo:material-flash:</span> `#!python 'comments/'` en vez de `#!python 'comments`

Ahora ya podemos definir las **URLs de segundo nivel** en la aplicación `posts`:

```python title="posts/urls.py"
from django.urls import path

from . import views


app_name = 'posts'#(1)!

urlpatterns = [
    path('', views.post_list, name='post-list'),#(2)!
    path('<post_slug>/', views.post_detail, name='post-detail'),#(3)!
]
```
{ .annotate }

1. La variable `app_name` define el **espacio de nombres** de las URLs de cada aplicación.
2. Analicemos cada parámetro de la función `path` por separado:
    1. `#!python ''` :material-arrow-right-box: Si concatenamos `/posts/` con la cadena vacía, obtenemos que la URL resultante es: `/posts/`
    2. `#!python views.post_list` :material-arrow-right-box: vista que se lanzará si la URL casa con este patrón.
    3. `#!python name='post-list'` :material-arrow-right-box: nombre de la URL, que unido al espacio de nombres, lo identifican unívocamente en todo el proyecto. Por tanto será: `posts:post-list`.
3. Analicemos cada parámetro de la función `path` por separado:
    1. `#!python '<post_slug>'` :material-arrow-right-box: El uso de ángulos nos indica que se trata de un **parámetro variable**. Casa con cualquier entrada. Si concatenamos `/posts/` con `<post_slug>` obtenemos que la URL resultante es `/posts/this-is-a-new-post/`
    2. `#!python views.post_detail` :material-arrow-right-box: vista que se lanzará si la URL casa con este patrón.
    3. `#!python name='post-detail'` :material-arrow-right-box: nombre de la URL, que unido al espacio de nombres, lo identifican unívocamente en todo el proyecto. Por tanto será: `posts:post-detail`.

!!! tip "Nombres de URLs"

    Es habitual usar «slugs» en los nombres de URLs. Es decir, cuando utilizamos el parámetro `name` de la función `path`. En vez de `#!python name='post_list'` suele ser de buen estilo escribir `#!python name='post-list'`.

### Agrupar URLs

En el caso de tener distintos patrones de URLs en un mismo fichero `urls.py` se aconseja agrupar los patrones por similitud.

Un pequeño <span class="example">ejemplo:material-flash:</span> en el que se plantea este escenario:

=== "Peor :octicons-thumbsdown-16:"

    ```python title="urls.py"
    urlpatterns = [
        path('shop/', ...),
        path('api/', ...),
        path('shop/product/{int:product_pk}/', ...),
        path('api/apparel/{int:product_pk}/', ...),
        path('shop/purchase/{slug:article_slug}/', ...),
        path('api/goods/{slug:good_slug}/', ...),
    ]
    ```

=== "Mejor :octicons-thumbsup-16:"

    ```python title="urls.py"
    urlpatterns = [
        path('api/', ...),
        path('api/apparel/{int:product_pk}/', ...),
        path('api/goods/{slug:good_slug}/', ...),
        path('shop/', ...),
        path('shop/product/{int:product_pk}/', ...),
        path('shop/purchase/{slug:article_slug}/', ...),
    ]
    ```

## Conversores de rutas { #path-converters }

En las rutas dinámicas (aquellas que contienen parámetros variables) es posible indicar el tipo de cada parámetro para que Django realice una conversión «implícita» al tipo de dato correspondiente.

La sintaxis de un conversor de ruta es la siguiente: `path(<param:converter>, ...)`

### Conversores predefinidos { #builtin-path-converters }

Veamos una tabla resumen con los [conversores de rutas predefinidos](https://docs.djangoproject.com/en/stable/topics/http/urls/#path-converters) en Django:

| Conversor | Ejemplo |  Explicación |
| --- | --- | --- |
| `#!python path('<username>', ...)` | `/guido/`  | Por defecto se convierte a `#!python str` |
| `#!python path('<str:tag>', ...)` | `/python/` | Conversión explícita a `#!python str` |
| `#!python path('<int:post_id>', ...)` | `/4673/`  | Conversión explícita a `#!python int` |
| `#!python path('<slug:product_slug>', ...)` | `/display-23-inches/`  | Conversión explícita a `#!python str` |
| `#!python path('<uuid:token>', ...)` | `/075194d3-6885-417e-a8a8-6c931e272f00/`  | Conversión explícita a [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID) |

## URL desde nombre { #reverse }

<span class="djversion intermediate">:simple-django: Intermedio :material-tag-multiple-outline:</span>

Se considera una mala práctica «hardcodear»[^1] las URLs directamente ya que, ante un determinado cambio de una URL en el futuro, tendremos que localizar todas las ocurrencias de dicha URL en el código y modificarlas.

Por ello Django nos «anima» a utilizar **nombres de URLs** en la función [`path()`](https://docs.djangoproject.com/en/stable/ref/urls/#path) dentro de los distintos ficheros `urls.py`.

Pero si lo que queremos es el paso «inverso» de obtener la URL a partir de su nombre tendremos que usar la función [`reverse()`](https://docs.djangoproject.com/en/stable/ref/urlresolvers/#reverse).

Continuando con el <span class="example">ejemplo:material-flash:</span> previo del «blog», supongamos que queremos obtener el nombre de ciertas URLs. El uso de la función `reverse()` depende de si la URL tiene o no parámetros:

=== "URL sin parámetros"

    ```pycon
    >>> from django.urls import reverse

    >>> reverse('posts:post-list')
    '/posts/'
    ```

=== "URL con parámetros"

    ```pycon
    >>> from django.urls import reverse

    >>> reverse('posts:post-detail', kwargs={'post_slug': 'test'})#(1)!
    '/posts/test/'
    ```
    { .annotate }

    1. También se pueden pasar los argumentos mediante `#!python args=`

## Redirección { #redirect }

<span class="djversion intermediate">:simple-django: Intermedio :material-tag-multiple-outline:</span>

Django nos ofrece la función [`redirect()`](https://docs.djangoproject.com/en/stable/topics/http/shortcuts/#redirect) para hacer redirecciones. Esta función puede ser invocada de ~~tres~~ cuatro formas distintas según el argumento utilizado.

Veamos un <span class="example">ejemplo:material-flash:</span> en el que redireccionamos a la URL de un «post»:

=== "Pasando un modelo :octicons-database-16:"

    ```pycon
    >>> from django.shortcuts import redirect    
    >>> from posts.models import Post

    >>> post = Post.objects.get(slug='this-is-test-post')
    >>> redirect(post)#(1)!
    ```
    { .annotate }
    
    1.  - Django obtiene la URL llamando a [`post.get_absolute_url()`](models.md#canonical-url) y hace la redirección.
        - En este caso se haría una redirección a `/posts/this-is-a-test-post`.

=== "Pasando una vista :octicons-eye-16:"

    ```pycon
    >>> from django.shortcuts import redirect    
    >>> from posts.views import post_detail

    >>> redirect(post_detail, post_slug='this-is-a-test-post')#(1)!
    ```
    { .annotate }
    
    1.  - Django obtiene la URL llamando a [`reverse()`](#reverse) sobre la vista indicada.
        - Si la vista recibe argumentos, se pueden pasar en la propia llamada.
        - En este caso se haría una redirección a `/posts/this-is-a-test-post`.

=== "Pasando un nombre de URL :material-checkbox-multiple-blank-circle-outline:"

    ```pycon
    >>> from django.shortcuts import redirect    
    >>> from django.urls import reverse    

    >>> redirect(reverse('post-detail', kwargs={'post_slug': 'this-is-a-test-post'}))#(1)!
    ```
    { .annotate }
    
    1.  - Aquí es necesario usar la función [`reverse()`](#reverse) para obtener la URL a partir del nombre.
        - En este caso se haría una redirección a `/posts/this-is-a-test-post`.

=== "Pasando una URL :fontawesome-solid-arrows-to-dot:"

    ```pycon
    >>> from django.shortcuts import redirect    

    >>> redirect('https://www.djangoproject.com/')#(1)!
    ```
    { .annotate }
    
    1.  - La URL se indica de forma explícita como argumento.
        - Puede ser una URL relativa o absoluta.
        - En este caso se haría una redirección a `https://www.djangoproject.com/`.
    
??? tip "Redirección permanente"

    Django aplica por defecto una **redirección temporal**. Si lo que se quiere es realizar una **redirección permanente** habrá que usar el argumento `#!python permanent=True` en la función `redirect()`.
    
## Accesos directos en primer nivel { #main-shortcuts }

<span class="djversion intermediate">:simple-django: Intermedio :material-tag-multiple-outline:</span>

En las [URLs de primer nivel](#main-urls) podemos ir más allá del típico «include». En este sentido se abren dos posibilidades:

1. Apuntar a vistas.
2. Redireccionar a URLs.

### Apuntar a vistas { #view-target }

Es posible que queramos «apuntar» una determinada URL en `main/urls.py`{ .green } a una cierta vista de una aplicación concreta.

Esto por <span class="example">ejemplo:material-flash:</span> es muy habitual en las operaciones de [autenticación](auth.md). Suponiendo que el **inicio de sesión** y **cierre de sesión** están en una aplicación llamada `accounts`, tendríamos algo parecido a esto en las **URLs de primer nivel**:

```python title="main/urls.py"
from django.contrib import admin

import account.views#(1)!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', account.views.user_login, name='login')#(2)!
    path('logout/', account.views.user_logout, name='logout')#(3)!
]
```
{ .annotate }

1. En `main/urls.py` se recomienda importar las vistas de esta forma para evitar «colisiones» con otros espacios de nombres.
2. Se apunta a la vista de «login» de la aplicación `account`.
3. Se apunta a la vista de «logout» de la aplicación `account`.

### Redireccionar a URLs { #url-redirect }

Desde el propio fichero `urls.py` puede resultar cómodo hacer una redirección «sencilla».

Supongamos por <span class="example">ejemplo:material-flash:</span> un escenario en el que queremos redirigir la URL raíz de nuestro blog `/` al listado de «posts» que hay en la plataforma:

```python title="main/urls.py" hl_lines="6"
from django.shortcuts import redirect
from django.urls import path


urlpatterns = [
    path('', lambda _: redirect('posts:post-list'))#(1)!
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls'))
]
```
{ .annotate }

1.  - Simulamos una vista mediante una función [lambda](../../../core/modularity/functions.md#lambda).
    - Como no usamos el supuesto parámetro `request` escribimos `_` como primer argumento.
    - Poner la redirección «lambda» en primer lugar es una _buena práctica_ para visualizar más claramente las URLs.

## Expresiones regulares { #regex }

<span class="djversion advanced">:simple-django: Avanzado :material-tag-multiple-outline:</span>

A la hora de definir los patrones en las URLs, Django nos permite utilizar [expresiones regulares](https://docs.djangoproject.com/en/stable/topics/http/urls/#using-regular-expressions). Es una técnica muy potente ya que permite ir más allá de los formatos «básicos» y definir reglas más específicas.

En este escenario, en vez de utilizar la función `path()` usaremos la función [`re_path()`](https://docs.djangoproject.com/en/stable/ref/urls/#django.urls.re_path) que, como su propio nombre indica, nos permite definir rutas (URLs) mediante expresiones regulares (`re`).

Planteamos un <span class="example">ejemplo:material-flash:</span> en el que queremos mostrar los «posts» de un «blog» con una determinada **categoría**, pero con el matiz de que el _código de categoría_ es un «string» de 4 letras mayúsculas:

```python title="posts/urls.py"
from django.urls import re_path#(1)!
from . import views

urlpatterns = [
    re_path(#(2)!
        r'^(?P<category_code>[A-Z]{4})/$',#(3)!
        views.post_by_category,
        name='post-by-category'
    )
]
```
{ .annotate }

1. Importamos la función.
2. Utilizamos la función como el resto de patrones.
3.  - Es conveniente usar [cadenas en crudo](../../../core/datatypes/strings.md#raw) para las expresiones regulares.
    - También es recomendable empezar la cadena con `^` (_comienzo de línea_) y acabarla con `$` (_final de línea_) para delimitar el patrón.
    - Se utiliza un [grupo de captura nominal](https://docs.python.org/3/howto/regex.html#non-capturing-and-named-groups) `(?P<name>)` para el parámetro correspondiente.
    - La expresión regular viene a continuación. En este caso `[A-Z]{4}` indica cuatro apariciones de cualquier letra en mayúsculas.

??? tip "Mezclando patrones"

    Cuando usamos `re_path()` tenemos que utilizar expresiones regulares en toda la URL. No es posible mezclar patronces «convencionales» con patrones expresión regular.


[^1]: «Hardcodear» significa escribir literales/valores directamente en el código.
