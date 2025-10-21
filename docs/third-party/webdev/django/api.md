---
icon: material/api
---

# API { #api }

<span class="djversion specialized">:simple-django: Especializado :material-tag-multiple-outline:</span>

En el ecosistema Django podemos encontrar un paquete muy «conocido» llamado [Django Rest Framework - DRF](https://www.django-rest-framework.org/) que está enfocado al desarrollo de una API. Desde luego es una muy buena opción para determinados escenarios.

Pero en esta sección no vamos a desarrollar DRF sino que vamos a explicar mecanismos implícitos en Django para implementar una API. Al final y al cabo no deja de ser un potente «backend» con gran cantidad de utilidades.

## Serialización { #serialization }

La serialización es el proceso de convertir un objeto o estructura de datos en un formato que pueda ser almacenado o transmitido y luego reconstruido (generalmente en comunicación cliente-servidor).

En el contexto de una API, serializar un objeto se traduce en **convertirlo a una cadena de texto**. Esta representación puede venir en distintos formatos. El más habitual suele ser JSON.

En el ámbito de Python, un objeto JSON vendría a ser un [diccionario](../../../core/datastructures/dicts.md) o una [lista de diccionarios](../../../core/datastructures/lists.md) en formato [cadena de texto](../../../core/datatypes/strings.md).

### JSON { #json }

Python dispone del paquete [`json`](https://docs.python.org/es/3/library/json.html) dentro de la _librería estándar_ que permite codificar y decodificar objetos en formato JSON:

- [`json.dumps()`](https://docs.python.org/es/3/library/json.html#json.dumps) recibe un objeto Python y devuelve una cadena de texto en formato JSON.
- [`json.loads()`](https://docs.python.org/es/3/library/json.html#json.loads) recibe una cadena de texto en formato JSON y devuelve un objeto Python.

A la hora de la transformación Python :material-arrow-right-box: JSON **no todos los tipos de datos Python son compatibles**. A continuación se muestra una tabla con los ^^tipos de datos compatibles^^ y cómo se mapean a JSON:

| Python :material-language-python: | JSON :simple-json: |
| --- | --- |
| `#!python dict` | `#!js object` |
| `#!python list`, `#!python tuple` | `#!js array` |
| `#!python str` | `#!js string` |
| `#!python int`, `#!python float` | `#!js number` |
| `#!python bool` | `#!js true` / `#!js false` |
| `#!python None` | `#!js null` |

!!! warning "Tipos de datos incompatibles"

    Cualquier otro tipo/estructura de datos que usemos en Python y que queramos convertir a JSON habrá que transformarlo previamente a alguno de los tipos de datos compatibles indicados en la tabla anterior.

    Estamos habando de objetos personalizados (clases), conjuntos, fecha/hora, etc.

Veamos un <span class="example">ejemplo:material-flash:</span> de transformación:

=== "Python"

    ```python
    {
        'name': 'Ana',
        'age': 25,
        'city': 'Barcelona',
        'is_student': True,
        'marks': [8.5, 9.0, 7.5],
        'extra': None
    }
    ```

=== "JSON"

    ```json
    {
        "name": "Ana",
        "age": 25,
        "city": "Barcelona",
        "is_student": false,
        "marks": [8.5, 9.0, 7.5],
        "extra": null
    }
    ```
    
### Modelos { #serialize-models }

Por norma general, una API trabajará con modelos (base de datos) que tendremos que serializar para transmitir desde el lado servidor al al lado cliente. Como ya se ha citado, lo más habitual es hacerlo en formato JSON.

Veamos a continuación una propuesta de **serializador (base) para instancias de modelo**, del que luego podremos derivar distintos serializadores concretos:

```python title="shared/serializers.py"
import json
from abc import ABC
from typing import Iterable

from django.http import HttpRequest, JsonResponse


class BaseSerializer(ABC):#(1)!
    def __init__(
        self,
        to_serialize: object | Iterable[object],#(2)!
        *,
        fields: Iterable[str] = [],#(3)!
        request: HttpRequest = None,#(4)!
    ):
        self.to_serialize = to_serialize
        self.fields = fields
        self.request = request

    def build_url(self, path: str) -> str:#(5)!
        return self.request.build_absolute_uri(path) if self.request else path

    # To be implemented by subclasses
    def serialize_instance(self, instance: object) -> dict:#(6)!
        raise NotImplementedError

    def __serialize_instance(self, instance: object) -> dict:#(7)!
        serialized = self.serialize_instance(instance)
        return {f: v for f, v in serialized.items() if not self.fields or f in self.fields}

    def serialize(self) -> dict | list[dict]:#(8)!
        if not isinstance(self.to_serialize, Iterable):
            return self.__serialize_instance(self.to_serialize)
        return [self.__serialize_instance(instance) for instance in self.to_serialize]

    def to_json(self) -> str:#(9)!
        return json.dumps(self.serialize())

    def json_response(self) -> str:#(10)!
        return JsonResponse(self.serialize(), safe=False)#(11)!
```
{ .annotate }

1. Definimos la clase como _abstracta_ para que no se puede crear una instancia de esta clase base.
2. Datos a serializar (**instancias de modelo**), que puede ser tanto un único objeto como un iterable de objetos.
3. Se puede pasar un iteriable de campos para utilizar únicamente ese subconjunto a la hora de serializar.
4. Es posible pasar la _petición HTTP_ desde una vista si queremos construir URLs absolutas en ciertos campos.
5. Este método construye una URL absoluta a partir de una ruta indicada.
6. Este método es el que debe ser implementado en clases derivadas y se encarga de serializar una instancia concreta.
7. Este método utiliza el método anterior `serialize_instance()` pero añade el filtrado de campos según lo indicado en el constructor.
8.  - Este método será el que utilicemos «habitualmente» y serializa los datos teniendo en cuenta su naturaleza.
    - Si se trata de una única instancia se devolverá un diccionario.
    - Se se trata de múltiples instancias se devolverá una lista de diccionarios.
9. Este método convierte el objeto serializado a formato JSON (como cadena de texto).
10. Este método puede ser muy útil para utilizarlo desde una vista, ya que nos devuelve una respuesta JSON con el objeto serializado.
11. - Se devuelve una respuesta [`JsonResponse`](https://docs.djangoproject.com/en/stable/ref/request-response/#jsonresponse-objects).
    - El parámetro `#!python safe=False` es necesario ya que si fuera `#!python True` sólo manejaría diccionarios, y hay ocasiones en las que tenemos listas de diccionarios.

Ahora supongamos un <span class="example">ejemplo:material-flash:</span> en el que queremos serializar los «posts» de un «blog». Empecemos definiendo su modelo:

```python title="posts/models.py"
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)
    content = models.TextField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

Nuestro serializador quedaría de la siguiente manera:

```python title="posts/serializers.py"
from shared.serializers import BaseSerializer#(1)!


class PostSerializer(BaseSerializer):#(2)!
    def serialize_instance(self, instance) -> dict:#(3)!
        return {#(4)!
            'id': instance.pk,#(5)!
            'title': instance.title,#(6)!
            'slug': instance.slug,#(7)!
            'content': instance.content,#(8)!
            'created_at': instance.created_at.isoformat(),#(9)!
            'updated_at': instance.updated_at.isoformat(),#(10)!
        }
```
{ .annotate }

1. Importamos el serializador base desde la ruta en la que se encuentre.
2. Heredamos de dicho serializador para poder reutilizar sus funcionalidades.
3. Definimos el método para serializar una instancia de modelo (en este caso de un «post»).
4. Este método retorna un diccionario.
5. Suele ser habitual incluir un campo `id` en la respuesta (no tiene por qué coincidir con la clave primaria).
6. Título del «post».
7. «Slug» del «post».
8. Contenido del «post».
9. - No es posible serializar directamente un objeto [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime).
    - Por ello utilizamos el método [`isoformat()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.isoformat) que devuelve una _cadena de texto_ con la representación del objeto.
10. - No es posible serializar directamente un objeto [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime).
    - Por ello utilizamos el método [`isoformat()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.isoformat) que devuelve una _cadena de texto_ con la representación del objeto.

Un objeto «post» quedaría serializado de la siguiente manera:

```python
{
    'id': 63,
    'title': 'How to implement APIs in Python',
    'slug': 'how-to-implement-apis-in-python'
    'content': 'Remember that first step is to serialize data',
    'created_at': '2019-05-18T15:17:08.132263',
    'updated_at': '2024-02-09T12:45:03.197632',
}
```

## Gestión de peticiones { #request-management }

Al implementar una API hay que tener en cuenta varios aspectos a la hora de gestionar las peticiones.

### URLs { #urls }

El diseño de las URLs de una API no dista especialmente del diseño habitual de [URLs](urls.md) que ya hemos visto. Quizás el único matiz tiene que ver con cuestiones de «estilo» sobre cómo organizar los **recursos** que se van a ofrecer.

En el contexto de una API se suele hablar de [«entrypoint»](https://smartbear.com/learn/performance-monitoring/api-endpoints/) (punto de entrada) al referirnos a una URL concreta.

Algo ~~importante~~ interesante sería usar el prefijo `/api` en el diseño de nuestras URLs para la API. Esto no implica generar una única aplicación `api` en la que tengamos toda la lógica de negocio. Se pueden seguir creando aplicaciones que respondan a la semántica de nuestr contexto para luego redirigir a las vistas correspondientes.

En el <span class="example">ejemplo:material-flash:</span> de un «blog» podríamos organizar las URLs de primer nivel de la siguiente manera:

```python title="main/urls.py"
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', include('posts.urls')),
    path('api/categories/', include('categories.urls')),
]
```

A partir de aquí habría que ir definiendo las URLs para cada recurso:

| URL | Descripción |
| --- | --- |
| `/api/posts/` | Todos los «posts» del «blog» |
| `/api/posts/?category=nature` | Todos los «posts» del «blog» con categoría «Nature» |
| `/api/posts/add/` | Añadir un «post» al «blog» |
| `/api/posts/this-is-django/` | Detalle del «post» con «slug» `this-is-django` |
| `/api/posts/this-is-django/delete/` | Borrar el «post» con «slug» `this-is-django` |
| ... | ... |
        
:material-check-all:{ .blue } El diseño de las URLs de una API puede llegar a ser un proceso «artesanal» que depende del contexto del problema y de los recursos que se quieran ofrecer.

### Métodos HTTP { #http-methods }

Existen distintos [métodos HTTP](https://restfulapi.net/http-methods/) (o verbos) que acompañan a una petición HTTP y que definen la forma en la que viaja la información y el tipo de operación a realizar.

| Método | Descripción |
| --- | --- |
| `GET` | Solicita datos del servidor (solo lectura). |
| `POST` | Envía datos al servidor para crear un recurso. |
| `PUT` | Actualiza un recurso existente o lo crea si no existe. |
| `PATCH` | Modifica parcialmente un recurso existente. |
| `DELETE` | Elimina un recurso del servidor. |
| `HEAD` | Similar a GET, pero solo devuelve los encabezados. |
| `OPTIONS` | Devuelve los métodos HTTP permitidos en un recurso. |
| `TRACE` | Devuelve la solicitud recibida para diagnóstico. |

:material-check-all:{ .blue } Aunque no es obligatorio utilizar estos métodos, sí se considera una buena práctica porque sigue el estándar de diseño de APIs y puede facilitar su diseño e implementación.

Django [ofrece funcionalidades](https://docs.djangoproject.com/en/stable/topics/http/decorators/#allowed-http-methods) para obligar a que una determinada vista sólo acepte ciertos métodos HTTP:

=== "Sólo `GET`"

    ```python
    from django.views.decorators.http import require_GET

    @require_GET
    def only_get_view(request):
        # ...
    ```

=== "Sólo `POST`"

    ```python
    from django.views.decorators.http import require_POST

    @require_POST
    def only_post_view(request):
        # ...
    ```

=== "`GET` o `POST`"

    ```python
    from django.views.decorators.http import require_http_methods

    @require_http_methods(['GET', 'POST'])#(1)!
    def only_get_or_post_view(request):
        # ...
    ```
    { .annotate }
    
    1. Obviamente aquí se pueden indicar otros verbos HTTP.

En el caso de que se realice una petición HTTP con un método no permitido, Django devolverá una respuesta [`HttpResponseNotAllowed`](https://docs.djangoproject.com/en/stable/ref/request-response/#django.http.HttpResponseNotAllowed).

#### GET y POST { #get-post }

Simplificando mucho, podríamos implementar una API únicamente sobre dos métodos HTTP: `GET` y `POST`.

A la hora de elegir cuál debemos aplicar se podrían seguir estas sencillas instrucciones:

| Lectura :octicons-database-24: | Escritura :octicons-database-24: | Método HTTP |
| --- | --- | --- |
| | | `GET`{ .green } |
| ✔ | | `GET`{ .green } |
| | ✔ | `POST`{ .blue } |
| ✔ | ✔ | `POST`{ .blue } |


### CSRF { #csrf }

En el apartado de [formularios](forms.md#template-forms) ya hemos visto algo sobre CSRF.

Para poder trabajar de forma «sencilla» con la API vamos a introducir el decorador [`csrf_exempt`](https://docs.djangoproject.com/es/stable/ref/csrf/#django.views.decorators.csrf.csrf_exempt). Django proporciona este decorador para dejar exenta a una vista de aplicarle los mecanismos de seguridad sobre CSRF:

```python
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def csrf_exempt_view(request):
    # ...
```

:material-check-all:{ .blue } Por lo tanto al «consumir» la API estaremos evitando tener que pasar un token CSRF.

### JSON { #json }

#### Recibiendo un JSON { #json-receive }

Habitualmente una API recibe datos en formato JSON en el «body» (cuerpo) de una petición POST.

Django inyecta dichos datos en el atributo [`body`](https://docs.djangoproject.com/en/stable/ref/request-response/#django.http.HttpRequest.body) de `HttpRequest`. Necesitaremos **deserializarlos** para obtener el objeto Python correspondiente:

```python
import json


def process_data(request):
    payload = json.loads(request.body)#(1)!
```
{ .annotate }

1.  - Si el JSON es inválido (mal formado) se lanzará una excepción de tipo [`JSONDecodeError`](https://docs.python.org/es/3/library/json.html#json.JSONDecodeError).
    - `payload` será (casi con total seguridad) un **diccionario**.

#### Enviando un JSON { #json-send }

Como se ha comentado previamente, una API que serializa datos **suele** devolverlos en formato JSON.

Para ello, Django nos proporciona el objeto [`JsonResponse`](https://docs.djangoproject.com/en/stable/ref/request-response/#jsonresponse-objects) que recibe un objeto Python serializable y devuelve una respuesta con la representación de dicho objeto en formato JSON:

```python
from django.http import JsonResponse
import datetime

from posts.models import Post


def now(request):
    return JsonResponse({'now': datetime.datetime.now().isoformat()})#(1)!
```
{ .annotate }

1.  - Si lo que fuéramos a serializar no fuera un diccionario, habría que pasar `#!python safe=False`
    - Admite un parámetro `status` para indicar el código de estado de la respuesta HTTP.

##### Códigos de estado HTTP { #http-status-code }

Los [códigos de estado HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) permiten enviar en la respuesta (JSON o HTTP) una indicación del ^^resultado de la operación solicitada^^. Aunque existen una gran variedad de códigos de estado, en [esta tabla](views.md#response-types) se resumen los más importantes.

Por tanto, para hacer uso de estos códigos de estado al enviar una respuesta JSON, podríamos recurrir a ciertas partes del siguiente código:

```python
from django.http import JsonResponse

return JsonResponse({'error': 'Message for Bad request'}, status=400)
return JsonResponse({'error': 'Message for Unauthorized'}, status=401)#(1)!
return JsonResponse({'error': 'Message for Forbidden'}, status=403)#(2)!
return JsonResponse({'error': 'Message for Not Found'}, status=404)
return JsonResponse({'error': 'Message for Method Not Allowed'}, status=405)
return JsonResponse({'error': 'Message for Internal Server Error'}, status=500)
```
{ .annotate }

1. «Unauthorized» indica que el usuario no se ha [autenticado](#auth) correctamente.
2. «Forbidden» indica que el usuario sí se ha [autenticado](#auth) correctamente pero que no tiene permisos para acceder al recurso solicitado.

:material-check-all:{ .blue } Cuando no se especifica el parámetro `status` en `JsonResponse` su valor por defecto es [`200`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200) indicando que todo ha ido bien.

## Autenticación { #auth }

Es posible que existan ciertas operaciones en una API que requieran autenticación.

La autenticación en una API se puede llevar a cabo mediante distintos métodos:

- Autenticación básica con nombre de usuario y contraseña.
- Autenticación mediante «bearer token» (token portador).
- [Autentación JWT](https://auth0.com/blog/how-to-handle-jwt-in-python/).
- [Autenticación OAuth 2.0](https://medium.com/@fyattani/api-authentication-using-oauth-in-python-5d3b6a6778f2).

!!! info "Bearer Token"

    En este apartado nos centraremos en autenticación mediante **«bearer token»** («token» portador). Se trata de un esquema relativamente sencillo de implementar pero que ofrece la funcionalidad necesaria.

### Modelo { #bearer-token-model } 

Lo primero será definir un modelo que nos permita ^^almacenar el token de autenticación^^ de cada usuario/a.

A continuación se presenta _una propuesta de modelo_ para almacenar los «tokens» de autenticación:

```python title="users/models.py"
import uuid

from django.conf import settings
from django.db import models


class Token(models.Model):
    key = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)#(1)!
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#(2)!
    created_at = models.DateTimeField(auto_now_add=True)#(3)!

    def __str__(self):
        return str(self.key)
```
{ .annotate }

1.  - Este campo almacenará el valor de la clave (token) de tipo UUID.
    - Le damos un valor por defecto que en este caso será un «callable» (función) [`uuid.uuid4()`](https://docs.python.org/3/library/uuid.html#uuid.uuid4)
    - Indicar `editable=False` hace que no se pueda editar desde la interfaz administrativa.
2. Necesitamos vincularlo con la clase [`User`](auth.md#user) que nos proporciona Django.
3.  - Añadimos un atributo para tener el momento en el que se creó el token.
    - También se podría haber añadido un atributo `expires_at` que indica cuándo expira.

### Obtener token { #get-auth-token }

Para obtener el «token» de autenticación tendremos que implementar una vista que reciba usuario y contraseña a través de un JSON sobre una petición POST:

```python title="users/views.py"
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@require_POST
def auth(request):
    payload = json.loads(request.body)#(1)!
    if user := authenticate(#(2)!
        username=payload['username'], password=payload['password']
    ):
        return JsonResponse({'token': user.token.key})#(3)!
    return JsonResponse({'error': 'Invalid credentials'}, status=401)#(4)!
```
{ .annotate }

1. Decodificamos el contenido JSON de la petición.
2. Comprobamos las credenciales de usuario enviadas en el JSON.
3. Si todo ha ido bien, devolvemos el «token» de autenticación.
4. En caso de error devolvemos un mensaje informativo con el [código de respuesta HTTP](views.md#response-types) a **401**.

Obviamente habrá que definir una URL que gestione esta petición. Una propuesta podría ser `/api/auth/`:

```python title="main/urls.py" hl_lines="7"
from django.urls import path

import users.views

urlpatterns = [
    # ...
    path('api/auth/', users.views.auth, name='auth'),
    # ...
]
```

### Comprobar token { #check-auth-token }

_OAuth 2.0_ define en el [RFC 6750](https://oauth.net/2/bearer-tokens/#:~:text=Bearer%20Tokens%20are%20the%20predominant,such%20as%20JSON%20Web%20Tokens.) un estándar de autenticación mediante [bearer token](https://www.oauth.com/oauth2-servers/making-authenticated-requests/). En dicha especificación se indica que el «token» debe viajar en la **cabecera de la petición HTTP** (Headers) con un formato determinado:

<div class="annotate" markdown>
=== "Petición :material-network-outline:"

    ```mermaid
    erDiagram
        "HTTP Request" {
            URL _
            Method _
            Headers token
            Body _
        }
    ```

=== "Formato :material-format-columns:"

    Podemos entender las cabeceras de una petición [HTTP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) como un «diccionario»:

    | Clave | Valor |
    | --- | --- |
    | `Authorization`(1) | `Bearer <token>`(2) |

</div>
1. Para acceder a los datos enviados en las cabeceras HTTP, Django nos ofrece un diccionario alojado en [`requests.headers`](https://docs.djangoproject.com/en/stable/ref/request-response/#django.http.HttpRequest.headers).
2. Aunque la **clave del token** puede ser casi cualquier valor, en nuestro caso vamos a trabajar con UUID.

Necesitaremos algún artefacto que se encargue de controlar el acceso de un ~~cliente~~ usuario mediante la comprobación del «token» de autenticación.

Aunque esta funcionalidad se puede implementar mediante cualquier otro mecanismo, parece que encaja bien en un **decorador**, ya que lo vamos a aplicar sobre distintas vistas del proyecto.

A continuación se presenta _una propuesta de decorador_ para gestionar el acceso mediante «bearer token»:

```python title="users/decorators.py"
import re

from django.http import JsonResponse

from .models import Token


def auth_required(func):
    BEARER_TOKEN_REGEX = (
        r'Bearer (?P<token>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})'#(1)!
    )

    def wrapper(request, *args, **kwargs):
        if not (m := re.fullmatch(BEARER_TOKEN_REGEX, request.headers.get('Authorization', ''))):#(2)!
            return JsonResponse({'error': 'Invalid authentication token'}, status=400)#(3)!
        try:
            token = Token.objects.get(key=m['token'])#(4)!
        except Token.DoesNotExist:
            return JsonResponse({'error': 'Unregistered authentication token'}, status=401)#(5)!
        request.user = token.user#(6)!
        return func(request, *args, **kwargs)#(7)!

    return wrapper
```
{ .annotate }

1. Definimos una expresión regular para el formato que debe tener «bearer token».
2. - Extraemos de las cabeceras el contenido de la clave `Authorization`.
    - Comprobamos si casa con la expresión regular definida previamente.
3. Si no se cumple el formato se devuelve una respuesta 400 indicando que el valor del «token» no es válido.
4. Buscamos el «token» en la base de datos.
5. Si no existe el token se devuelve una respuesta 401 indicando que el «token» no está registrado.
6.  - Inyectamos el usuario en la `request` para poder manejarlo posteriormente en la vista.
    - Este paso no es obligatorio, pero puede ser útil.
7. Proseguimos con la ejecución de la función decorada (_vista_).

## Ejemplos de vistas { #view-examples }

A continuación se muestran algunas **vistas** (API) sobre el <span class="example">ejemplo:material-flash:</span> de un «blog»:

=== "Ver todos los «posts» :material-view-list:"

    ```python title="posts/views.py"
    from django.views.decorators.csrf import csrf_exempt
    from django.views.decorators.http import require_GET

    from .models import Post
    from .serializers import PostSerializer


    @csrf_exempt
    @require_GET
    def post_list(request):
        posts = Post.objects.all()#(1)!
        serializer = PostSerializer(posts)#(2)!
        return serializer.json_response()#(3)!
    ```
    { .annotate }
    
    1. Obtenemos todos los «posts» existentes.
    2. Utilizamos el serializador propio sobre la «queryset» de «posts».
    3. Retornamos mediante el método del serializador que ya devuelve una respuesta JSON.

=== "Detalle de un «post» :octicons-eye-16:"

    ```python title="posts/views.py"
    from django.http import JsonResponse
    from django.views.decorators.csrf import csrf_exempt
    from django.views.decorators.http import require_GET

    from .models import Post
    from .serializers import PostSerializer


    @csrf_exempt
    @require_GET
    def post_detail(request, post_slug: str):
        try:
            post = Post.objects.get(slug=post_slug)#(1)!
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)#(2)!
        serializer = PostSerializer(post)#(3)!
        return serializer.json_response()#(4)!
    ```
    { .annotate }
    
    1. Obtenemos el «post» concreto mediante su «slug».
    2. Si no lo encontramos, devolvemos una respuesta JSON con el código HTTP correspondiente y mensaje informativo de error.
    3. Utilizamos el serializador propio sobre la instancia del «post».
    4. Retornamos mediante el método del serializador que ya devuelve una respuesta JSON.

=== "Dar de alta un «post» :octicons-diff-added-24:"

    ```python title="posts/views.py"
    import json

    from django.http import JsonResponse
    from django.views.decorators.csrf import csrf_exempt
    from django.views.decorators.http import require_POST
    from django.utils.text import slugify

    from users.decorators import auth_required

    from .models import Post


    @csrf_exempt
    @require_POST
    @auth_required#(1)!
    def add_post(request):
        try:
            payload = json.loads(request.body)#(2)!
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON body'}, status=400)#(3)!
        post = Post.objects.create(#(4)!
            title=payload['title'],
            slug=slugify(payload['title']),
            content=payload['content'],
        )
        return JsonResponse({'id': post.pk})#(5)!
    ```
    { .annotate }
    
    1. Este decorador [comprueba el acceso a la vista](#check-auth-token) mediante «bearer token».
    2. Cargamos el JSON que nos viene en la petición y lo convertimos a objeto Python.
    3. Si el JSON es inválido, devolvemos una respuesta JSON con el código HTTP correspondiente y mensaje informativo de error.
    4. Creamos un nuevo objeto «post» extrayendo los valores de los campos.
    5. Devolvemos una respuesta JSON con el identificador del «post» creado.
