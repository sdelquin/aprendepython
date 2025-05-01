---
icon: fontawesome/solid/wand-magic-sparkles
---

# Interfaz administrativa { #admin }

<span class="djversion basic">:simple-django: Básico :material-tag-multiple-outline:</span>

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

Pero es muy habitual querer mostrar los campos del objeto en vez de su representación «string» en la interfaz administrativa. Para ello haremos uso del atributo de clase `list_display`.

Si seguimos con el <span class="example">ejemplo:material-flash:</span> del «post» de un blog, tendríamos lo siguiente:

```python title="posts/admin.py" hl_lines="8"
from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'contents')#(1)!
```
{ .annotate }

1.  - Se puede usar tanto una **tupla** como una **lista**.
    - `slug`, `title` y `contents` son campos del modelo `Post`.

## Relaciones muchos a muchos { #many-to-many }

<span class="djversion advanced">:simple-django: Avanzado :material-tag-multiple-outline:</span>

Cuando disponemos de campos `ManyToMany` en nuestros modelos, Django presenta un **control de selección múltiple** que, en muchas ocasiones, es suficiente para manipular los datos.

Pero podemos mejorarlo muy fácilmente. Partiendo del <span class="example">ejemplo:material-flash:</span> en el que [un «post» puede tener muchas etiquetas](models.md#many-to-many), haríamos lo siguiente:

```python title="posts/admin.py" hl_lines="8"
from django.contrib import admin

from .models import Post


@admin.register(Joint)
class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('labels',)
```

:material-check-all:{ .blue } Este simple línea añade a la interfaz administrativa **dos paneles (horizontales)** con las _etiquetas disponibles_ y las _etiquetas elegidas_ a la hora de editar/crear un nuevo «post».

### Relaciones muchos a muchos con modelo intermedio { #many-to-many-with-intermediary }

Para poder visualizar (y gestionar) de mejor manera las [relaciones muchos a muchos con modelo intermedio](https://docs.djangoproject.com/en/stable/ref/contrib/admin/#working-with-many-to-many-intermediary-models) dentro de la interfaz administrativa, Django proporciona unos artefactos denominados «inlines».

La idea detrás de esto es poder «presentar» en la misma página del objeto aquellos otros objetos relacionados con el primero que conformen esta relación muchos a muchos.

Para ilustrar el modo de uso con un <span class="example">ejemplo:material-flash:</span>, vamos a retomar [este escenario](models.md#many-to-many-with-intermediary) en el que un «post» puede tener múltiples etiquetas y se añade una **razón** por la que asignar las etiquetas a los «posts»:

```python title="posts/admin.py"
from django.contrib import admin

from .models import Label, Reason, Post


@admin.register(Label)#(1)!
class LabelAdmin(admin.ModelAdmin):
    pass


class ReasonInline(admin.TabularInline):#(2)!
    model = Reason#(3)!
    extra = 1#(4)!


@admin.register(Post)#(5)!
class PostAdmin(admin.ModelAdmin):
    inlines = [ReasonInline]#(6)!
```
{ .annotate }

1. El modelo `Label` se registra con normalidad.
2.   - El modelo `Reason` (_modelo intermedio_) se registra mediante [`admin.TabularInline`](https://docs.djangoproject.com/en/stable/ref/contrib/admin/#django.contrib.admin.TabularInline).
    - También se puede usar aquí la clase [`admin.StackedInline`](https://docs.djangoproject.com/en/stable/ref/contrib/admin/#django.contrib.admin.StackedInline) que [cambia la disposición](https://stackoverflow.com/a/74438061) de los elementos.
3. Es obligatorio especificar el modelo mediante el atributo de clase `model`.
4. El atributo `extra` define el número _adicional_ de entradas del modelo.
5. Registramos el modelo `Post`.
6. El atributo `inlines` nos permite definir los «slots» de objetos `Reason` que aparecerán en la interfaz administrativa de `Post`.

## Comandos de gestión { #management-commands }

<span class="djversion advanced">:simple-django: Avanzado :material-tag-multiple-outline:</span>

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
                self.style.SUCCESS('Successfully deleted all comments for post #{post.pk}')
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

```console
$ ./manage.py delete_comments 45 23 17
```

> Con esto estaríamos borrando todos los comentarios de los «posts» con clave primaria #45, #23 y #17.
