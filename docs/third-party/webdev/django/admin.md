---
icon: fontawesome/solid/wand-magic-sparkles
tags:
  - Paquetes de terceros
  - Desarrollo web
  - Django
---

# Interfaz administrativa { #admin }

<span class="dj-level">:material-signal-cellular-1: Django básico</span>

Como se ha [comentado previamente](./setup.md#admin) Django proporciona una interfaz administrativa para manejar los modelos de nuestro proyecto, prácticamente sin esfuerzo.

Pero existen una gran cantidad de opciones de personalización de la interfaz administrativa que iremos viendo en esta sección.

## Registrar un modelo { #register }

Supongamos un <span class="example">ejemplo:material-flash:</span> en el que tenemos un modelo `Post` y queremos gestionar dicho modelo desde la interfaz administrativa. Para ello debemos registrarlo en el siguiente fichero:

```python title="admin.py"
from django.contrib import admin#(1)!

from .models import Post#(2)!


@admin.register(Post)#(3)!
class PostAdmin(admin.ModelAdmin):#(4)!
    pass#(5)!
```
{ .annotate }

1. Necesitamos importar el módulo `admin` para utilizar sus funcionalidades.
2. Importamos el modelo que queremos activar. Es habitual que los modelos estén en la misma aplicación, por lo cual podemos importarlos desde `.models`
3. Este decorador registra el modelo que le pasamos como argumento.
4. Necesitamos crear una clase que hereda de `ModelAdmin`. El nombre de la clase (por convención) suele ser el nombre del modelo :material-plus-box: `Admin`.
5. No es necesario inicialmente que implementemos nada más.

:material-check-all:{ .blue } Cuando accedamos ahora a http://localhost/admin/ veremos que estará disponible un enlace [Posts]() para gestionar los objetos del modelo `Post`.

!!! abstract "Singular/Plural"

    El nombre del modelo debería estar escrito **en singular**. Esto se hace aún más evidente cuando Django nos lo muestra en plural desde la interfaz administrativa.

## Mostrar campos { #show-fields }

Cuando [registramos un modelo](#register), sus objetos aparecen en la interfaz administrativa a través del método `__str__()`. Si no está implementado veremos algo como: `#!python <Post: Post object (1)>`

:material-check-all:{ .blue } Por lo tanto es siempre recomendable implementar el método `#!python __str__()` de nuestros modelos.

Pero es muy habitual querer mostrar los campos del objeto (que interesen) en vez de su representación «string» en la interfaz administrativa. Para ello haremos uso del atributo de clase `list_display`.

Si seguimos con el <span class="example">ejemplo:material-flash:</span> del «post» de un blog, tendríamos lo siguiente:

```python title="posts/admin.py" hl_lines="8"
from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')#(1)!
```
{ .annotate }

1.  - Se puede usar tanto una **tupla** como una **lista**.
    - `title` y `slug` son campos del modelo `Post`.

Este sería el resultado en la interfaz administrativa:

![Dark image](images/admin/list_display-dark.png#only-dark)
![Light image](images/admin/list_display-light.png#only-light)

## Campos de búsqueda { #search-fields }

Django nos permite habilitar la búsqueda de objetos en la interfaz administrativa. Para ello simplemente tenemos que hacer uso del atributo [`search_fields`](https://docs.djangoproject.com/en/stable/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields).

Por <span class="example">ejemplo:material-flash:</span> vamos a añadir búsqueda de «posts» a través de su título y/o contenido:

```python title="posts/admin.py" hl_lines="9"
from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title', 'content')#(1)!
```
{ .annotate }

1.  - Se puede usar tanto una **tupla** como una **lista**.
    - `title` y `content` son campos del modelo `Post`.

Con este pequeño cambio veremos que aparece un cuadro de búsqueda en la interfaz administrativa:

![Dark image](images/admin/search_fields-dark.png#only-dark)
![Light image](images/admin/search_fields-light.png#only-light)

## Filtros de lista { #list-filter }

Otra de las funcionalidades que ofrece Django en la interfaz administrativa es añadir filtros de lista sobre determinados campos del modelo. Para ello tenemos que utilizar el atributo [`list_display`](https://docs.djangoproject.com/en/stable/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display).

Pensemos en un <span class="example">ejemplo:material-flash:</span> de «post» al que hemos añadido un campo `published` que indica si el «post» está o no publicado:

```python title="posts/models.py" hl_lines="8"
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)
    content = models.TextField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

Podemos añadir un filtro sobre dicho campo para consultar más fácilmente aquellos «posts» públicos y/o privados:

```python title="posts/admin.py" hl_lines="10"
from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title', 'content')
    list_filter = ('published',)#(1)!
```
{ .annotate }

1.  - Se puede usar tanto una **tupla** como una **lista**.
    - `published` es un campo del modelo `Post`.

Ahora ya disponemos de un «widget» donde poder filtrar:

![Dark image](images/admin/list_filter-dark.png#only-dark)
![Light image](images/admin/list_filter-light.png#only-light)

## Campos autocompletados { #prepopulated-fiels }

Otra de las funcionalidades existentes en la interfaz administrativa de Django es rellenar campos de manera automática a partir del valor de otros campos. Para conseguir este resultado tendremos que utilizar el atributo [`prepopulated_fields`](https://docs.djangoproject.com/en/stable/ref/contrib/admin/#django.contrib.admin.ModelAdmin.prepopulated_fields).

Por <span class="example">ejemplo:material-flash:</span> podríamos querer que el «slug» de un «post» se autocomplete mediante su título:

```python title="posts/admin.py" hl_lines="11"
from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title', 'content')
    list_filter = ('published',)
    prepopulated_fields = {'slug': ('title',)}#(1)!
```
{ .annotate }

1.  La estructura esperada es un **diccionario** donde:

    - Cada clave es un campo a autocompletar.
    - Cada valor es un iterable (lista o tupla) de campos desde los que se toma el contenido para autocompletar.

Con esto conseguimos que a medida que escribimos el título de un «post» se vaya autocompletando su «slug» correspondiente:

![Dark image](images/admin/prepopulated_fields-dark.gif#only-dark)
![Light image](images/admin/prepopulated_fields-light.gif#only-light)

## Acciones de administración { #admin-actions }

<span class="dj-level">:material-signal-cellular-2: Django intermedio</span>

En la interfaz administrativa de Django podemos realizar acciones sobre objetos de modelo. Estas acciones están predefinidas (añadir, borrar, editar, etc.), pero tenemos la posibilidad de incorporar nuevas acciones de administración personalizadas.

Supongamos un <span class="example">ejemplo:material-flash:</span> en el que pretendemos regenerar todos los «slugs» de los «posts» existentes en nuestra base de datos, a partir de cada uno de sus títulos:

```python title="posts/admin.py" hl_lines="17"
from django.contrib import admin
from django.utils.text import slugify

from .models import Post


@admin.action(description='Regenerate slug (from title) for selected posts')#(1)!
def regenerate_slug(modeladmin, request, queryset):#(2)!
    for post in queryset:#(3)!
        post.slug = slugify(post.title)#(4)!
        post.save()


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    actions = [regenerate_slug]#(5)!
```
{ .annotate }

1. Hay que registrar la acción indicando una descripción coherente.
2. La función recibe:
    - El modelo de administración (`PostAdmin` en este caso).
    - La petición HTTP.
    - El «queryset» con los objetos seleccionados desde la interfaz administrativa.
3. Recorremos todos los «posts» de la consulta.
4. Actualizamos su «slug».
5. El atributo `actions` define una lista de acciones.

De esta manera nos aparecerá una nueva acción a la hora de gestionar los «posts» en la interfaz administrativa:

![Dark image](images/admin/admin-action-dark.png#only-dark)
![Light image](images/admin/admin-action-light.png#only-light)

## Claves ajenas { #foreign-key }

<span class="dj-level">:material-signal-cellular-2: Django intermedio</span>

### Relaciones uno a muchos { #one-to-many }

Es habitual manejar claves ajenas en nuestros modelos. Por defecto, Django las muestra en la interfaz administrativa como **desplegables** donde seleccionar la instancia correspondiente.

Como <span class="example">ejemplo:material-flash:</span> vamos a partir de [este escenario](models.md#one-to-many) en el que un «post» puede tener varios comentarios.

El aspecto del formulario para añadir un comentario sería el siguiente:

![Dark image](images/admin/fk_dropdown-dark.png#only-dark)
![Light image](images/admin/fk_dropdown-light.png#only-light)

Veamos otras maneras de presentar la clave ajena a «post» para que sea más accesible:

=== "Búsqueda en ventana"

    Mediante el atributo [`raw_id_fields`](https://docs.djangoproject.com/en/stable/ref/contrib/admin/#django.contrib.admin.ModelAdmin.raw_id_fields) se pueden definir un conjunto de campos para los que se habilita una **búsqueda en ventana**.

    ```python title="comments/admin.py" hl_lines="8"
    from django.contrib import admin
    
    from .models import Comment
    
    
    @admin.register(Comment)
    class CommentAdmin(admin.ModelAdmin):
        raw_id_fields = ('post',)
    ```

    El formulario para añadir un comentario quedaría de la siguiente manera:

    ![Dark image](images/admin/raw_id_fields-dark.png#only-dark)
    ![Light image](images/admin/raw_id_fields-light.png#only-light)
    
=== "Búsqueda con autocompletado"

    Mediante el atributo [`autocomplete_fields`](https://docs.djangoproject.com/en/stable/ref/contrib/admin/#django.contrib.admin.ModelAdmin.autocomplete_fields) se pueden definir un conjunto de campos para los que se habilita una **búsqueda con autocompletado** (a medida que se escribe).
    
    ```python title="comments/admin.py" hl_lines="8"
    from django.contrib import admin
    
    from .models import Comment
    
    
    @admin.register(Comment)
    class CommentAdmin(admin.ModelAdmin):
        autocomplete_fields = ('post',)
    ```

    ??? danger "Error `admin.E040`"
    
        Es probable que el código anterior lance el siguiente error: `<class 'comments.admin.CommentAdmin'>: (admin.E040) PostAdmin must define "search_fields", because it's referenced by CommentAdmin.autocomplete_fields`.

        Si es así, lo que debemos hacer para solucionarlo es habilitar campos de búsqueda para los «posts»:

        ```python title="posts/models.py" hl_lines="8"
        from django.contrib import admin
        
        from .models import Post
        
        
        @admin.register(Post)
        class PostAdmin(admin.ModelAdmin):
            search_fields = ('title', 'content')
        ```

    El formulario para añadir un comentario quedaría de la siguiente manera:

    ![Dark image](images/admin/autocomplete_fields-dark.png#only-dark)
    ![Light image](images/admin/autocomplete_fields-light.png#only-light)

### Relaciones muchos a muchos { #many-to-many }

<span class="dj-level">:material-signal-cellular-3: Django avanzado</span>

Cuando disponemos de campos `ManyToMany` en nuestros modelos, Django presenta un **control de selección múltiple** que, en muchas ocasiones, es suficiente para manipular los datos.

Pero podemos mejorarlo muy fácilmente. Partiendo del <span class="example">ejemplo:material-flash:</span> en el que [un «post» puede tener varias etiquetas](models.md#many-to-many), haríamos lo siguiente:

```python title="posts/admin.py" hl_lines="8"
from django.contrib import admin

from .models import Post


@admin.register(Joint)
class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('labels',)
```

Esta simple línea añade a la interfaz administrativa **dos paneles (horizontales)** con las _etiquetas disponibles_ y las _etiquetas elegidas_ a la hora de editar/crear un nuevo «post»:

![Dark image](images/admin/filter_horizontal-dark.png#only-dark)
![Light image](images/admin/filter_horizontal-light.png#only-light)

#### Relaciones muchos a muchos con modelo intermedio { #many-to-many-with-intermediary }

Para poder visualizar (y gestionar) de mejor manera las [relaciones muchos a muchos con modelo intermedio](https://docs.djangoproject.com/en/stable/ref/contrib/admin/#working-with-many-to-many-intermediary-models) dentro de la interfaz administrativa, Django proporciona unos artefactos denominados «inlines».

La idea detrás de esto es poder «presentar» en la misma página del objeto aquellos otros objetos relacionados con el primero que conformen esta relación muchos a muchos.

Para ilustrar el modo de uso con un <span class="example">ejemplo:material-flash:</span>, vamos a retomar [este escenario](models.md#many-to-many-with-intermediary) en el que un «post» puede tener varias etiquetas y se añade el **detalle** del etiquetado (al asignar etiquetas a «posts»):

```python title="posts/admin.py" hl_lines="6-8 13"
from django.contrib import admin

from .models import Post, PostLabelingDetail


class PostLabelingDetailInline(admin.TabularInline):#(1)!
    model = PostLabelingDetail#(2)!
    extra = 1#(3)!


@admin.register(Post)#(4)!
class PostAdmin(admin.ModelAdmin):
    inlines = [PostLabelingDetailInline]#(5)!
```
{ .annotate }

1.  - El modelo `PostLabelingDetail` (_modelo intermedio_) se registra mediante [`admin.TabularInline`](https://docs.djangoproject.com/en/stable/ref/contrib/admin/#django.contrib.admin.TabularInline).
    - También se puede usar aquí la clase [`admin.StackedInline`](https://docs.djangoproject.com/en/stable/ref/contrib/admin/#django.contrib.admin.StackedInline) que [cambia la disposición](https://stackoverflow.com/a/74438061) de los elementos.

        ![Dark image](images/admin/stacked_inline-dark.png#only-dark)
        ![Light image](images/admin/stacked_inline-light.png#only-light)

2. Es obligatorio especificar el modelo mediante el atributo de clase `model`.
3. El atributo `extra` define el número _adicional_ de entradas del modelo.
4. Registramos el modelo `Post`.
5. El atributo `inlines` nos permite definir los «slots» de objetos `PostLabelingDetail` que aparecerán en la interfaz administrativa de `Post`.

Esta simple línea añade a la interfaz administrativa **un panel** con los detalles del etiquetado (**tabulados**) a la hora de editar/crear un nuevo «post»:

![Dark image](images/admin/tabular_inline-dark.png#only-dark)
![Light image](images/admin/tabular_inline-light.png#only-light)

Obviamente también podemos hacer uso de `raw_id_fields` o `autocomplete_fields` ([relaciones 1:N](#one-to-many)) en la clase `PostLabelingDetailInline` con el objetivo de mejorar la búsqueda de etiquetas.

## Comandos de gestión { #management-commands }

<span class="dj-level">:material-signal-cellular-3: Django avanzado</span>

Django ofrece la posibilidad de añadir [comandos personalizados](https://docs.djangoproject.com/en/stable/howto/custom-management-commands/) para ser ejecutados mediante `./manage.py <command>`. Hay escenarios en los que esto es realmente útil.

Vamos a partir del <span class="example">ejemplo:material-flash:</span> de un «blog» donde queremos implementar un _comando de gestión personalizado_ para borrar todos los comentarios de uno o varios «posts».

Para ello definimos el comando de la siguiente manera:

```python title="posts/management/commands/delete_comments.py"
from django.core.management.base import BaseCommand, CommandError#(1)!

from .models import Post#(2)!


class Command(BaseCommand):#(3)!
    help = 'Delete all comments for the given post.'#(4)!

    def add_arguments(self, parser):#(5)!
        parser.add_argument('post_pks', nargs='+', type=int)#(6)!

    def handle(self, *args, **options):#(7)!
        for post_pk in options['post_pks']:#(8)!
            try:
                post = Post.objects.get(pk=post_pk)#(9)!
            except Post.DoesNotExist:
                raise CommandError(f'Post #{post.pk} does not exist')#(10)!

            post.comments.delete()#(11)!

            self.stdout.write(#(12)!
                self.style.SUCCESS(f'Successfully deleted all comments for post #{post.pk}')
            )
```
{ .annotate }

1. Importamos las clases necesarias para definir el comando.
2. Importamos el modelo sobre el que vamos a trabajar.
3. Definimos la clase que contendrá el comando y que hereda de [`BaseCommand`](https://docs.djangoproject.com/en/stable/howto/custom-management-commands/#django.core.management.BaseCommand).
4. El atributo `help` permite definir el texto de ayuda explicativo al comando que saldrá en terminal.
5.  - En este caso el comando requiere de ciertos argumentos.
    - Este método se debe llamar exactamente así `add_arguments()`.
    - El parámetro `parser` es un objeto de tipo [`argparse.ArgumentParser`](https://docs.python.org/es/3/library/argparse.html#argparse.ArgumentParser).
6.  - El método [`add_argument()`](https://docs.python.org/es/3/library/argparse.html#argparse.ArgumentParser.add_argument) es muy versátil.
    - Añadimos el argumento `post_pks` que representa a las claves primarias de los «posts» que vamos a tratar.
7.  - El método `handle()` contiene el código a ejecutar por comando.
    - Debe tener esta signatura.
8.  - Los argumentos que se reciben por línea de comandos se almacenan en el diccionario `self.options`.
    - Recorremos las claves primarias de los «posts» indicados.
9.  Buscamos cada «post» en la base de datos.
10. - Si no se encuentra el «post» indicado lanzamos un error.
    - Django proporciona una clase [`CommandError`](https://docs.djangoproject.com/en/stable/howto/custom-management-commands/#django.core.management.CommandError) para estas situaciones.
11. Borramos todos los comentarios del «post» en cuestión.
12. - Mostramos por pantalla un mensaje de confirmación.
    - Es posible usar `self.stdout` para enviar a la salida estándar y `self.stderr` para enviar al error estándar.
    - En ambos casos se pueden utilizar [estilos](https://docs.djangoproject.com/en/stable/ref/django-admin/#syntax-coloring) que permiten colorear sintaxis en terminal.

!!! warning "Ubicación del comando"

    Es obligatorio que el comando se ubique dentro de la carpeta `management/commands` de la aplicación correspondiente. El nombre del fichero `.py` será el nombre del comando.

Para ejecutar el comando creado basta con ir a la terminal y escribir lo siguiente:

=== "*venv* :octicons-package-24:{.blue}"

    ```console
    $ ./manage.py delete_comments 45 23 17
    ```

=== "*uv* &nbsp;:simple-uv:{.uv}"

    ```console
    $ uv run manage.py delete_comments 45 23 17
    ```

> Con esto estaríamos borrando todos los comentarios de los «posts» con clave primaria #45, #23 y #17.
