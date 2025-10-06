---
icon: material/form-select
---

# Formularios { #forms }

<span class="djversion basic">:simple-django: Básico :material-tag-multiple-outline:</span>

Los [formularios](https://www.w3schools.com/html/html_forms.asp) son componentes web que permiten al usuario introducir información en una aplicación web. Veremos cómo manejar y gestionar los formularios a través de Django.

## Tipos de formularios { #form-types }

En función de la forma de implementarlos, podemos distinguir los siguientes tipos de formularios:

:one: [Formularios de plantilla](#template-forms).  
:two: [Formularios de clase](#class-forms).  
:three: [Formularios de modelo](#model-forms).

### Formularios de plantilla { #template-forms }

Este tipo de formularios se construyen a partir de una **plantilla HTML**.

Supongamos por <span class="example">ejemplo:material-flash:</span> que creamos un formulario en una plantilla para añadir un nuevo «post» en un «blog». Tendríamos algo similar a lo siguiente:

```htmldjango title="posts/templates/posts/post/add.html"
<form method="post"><!--(1)!-->
    {% csrf_token %}<!--(2)!-->
    <input type="text" name="post-title"><!--(3)!-->
    <textarea name="post-content"></textarea><!--(4)!-->
    <input type="submit" value="Enviar"><!--(5)!-->
</form>
```
{ .annotate }

1.  - Un formulario se puede enviar con método **«get»** o con método **«post»**. Cada uno tiene sus [ventajas e inconvenientes](https://www.baeldung.com/cs/http-get-vs-post).
    - En un modelo [SSR](webdev.md#ssr) es recomendable validar el envío del formulario en el servidor. Para ello desactivamos la validación HTML → `#!html <form method="post" novalidate>`
2. Django proporciona este mecanismo de seguridad contra CSRF. [Genera un token](https://www.geeksforgeeks.org/csrf-token-in-django/) único que debe ser enviado en la petición para que sea válida.
3. Los nombres que damos a los «widgets» son importantes. En este caso el nombre es `post-title` y contendrá el título del post que introduzca el usuario.
4. Los nombres que damos a los «widgets» son importantes. En este caso el nombre es `post-content` y contendrá el contenido del post que introduzca el usuario.
5. Necesitamos un botón para realizar el envío.

El envío de este formulario llegará al correspondiente fichero [`urls.py`](urls.md) que ejecutará una determinada vista dentro del fichero [`views.py`](views.md).

Veamos cómo procesar esta solicitud, siguiendo con el <span class="example">ejemplo:material-flash:</span> anterior de creación de un «post»:

```python title="posts/views.py"
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.text import slugify

from .models import Post


def add_post(request):
    if request.method == 'POST':#(1)!
        post_title = request.POST.get('post-title')#(2)!
        post_content = request.POST.get('post-content')#(3)!
        if post_title and post_content:#(4)!
            post_slug = slugify(post_title)#(5)!
            Post.objects.create(#(6)!
                title=post_title,
                content=post_content,
                slug=post_slug
            )
            return redirect('posts:post-list')#(7)!
        else:
            return HttpResponse('Title and content are required!')#(8)!
    return render(request, 'posts/add_post.html')#(9)!
```
{ .annotate }

1. Distinguimos el [método de la petición](views.md#request-method) HTTP.
2. En `#!python request.POST` tenemos un **diccionario** con todos los datos que provienen de la petición «post». La clave que buscamos debe coincidir con el atributo `name` del correspondiente «input» del formulario HTML.
3. En `#!python request.POST` tenemos un **diccionario** con todos los datos que provienen de la petición «post». La clave que buscamos debe coincidir con el atributo `name` del correspondiente «input» del formulario HTML.
4. «Validación» del formulario → debe existir un título y un contenido para el post.
5. Creamos el «slug» a partir del título del «post».
6. Se [crea](models.md#create-objects) un nuevo «post» a partir del título, contenido y «slug».
7. Todo ha ido bien → Redirigimos (por ejemplo) a la página con el listado de todos los «posts».
8. En el caso de que falte algún campo de entrada, habrá que informar del error.
9. Devolvemos la plantilla renderizada.

### Formularios de clase { #class-forms }

Este tipo de formularios se construyen a partir de una **clase Python**.

Django nos ofrece funcionalidades para poder escribir los [formularios usando código Python](https://docs.djangoproject.com/en/stable/topics/forms/#building-a-form-in-django) en vez de tener que usar código HTML.

En realidad lo que hacemos es definir una clase Python que posteriormente se transformará en el correspondiente código HTML («widget») inyectándolo en la plantilla.

#### Campos de formulario { #fields }

La siguiente tabla muestra la información más relevante de los distintos [campos de formulario](https://docs.djangoproject.com/en/stable/ref/forms/fields/#built-in-field-classes) que ofrece Django:

<div class="annotate" markdown>
| Campo :material-focus-field: | Objeto Python :material-language-python: | «Widget» :material-widgets-outline: | Parámetros :material-cube-outline: |
| --- | --- | --- | --- |
| [`BooleanField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#booleanfield) | [`bool`](../../../core/datatypes/numbers.md#booleans) | [`CheckboxInput`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.CheckboxInput) | |
| [`CharField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#charfield) | [`str`](../../../core/datatypes/strings.md) | [`TextInput`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.TextInput) | `max_length`(1)<br>`min_length`(2)<br>`strip`(3)<br>`empty_value`(4) |
| [`ChoiceField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#choicefield) | [`str`](../../../core/datatypes/strings.md) | [`Select`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.Select) | `choices`:octicons-key-asterisk-24:{ .red } (5) |
| [`DateField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#datefield) | [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date) | [`DateInput`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.DateInput) | `input_formats`(6) |
| [`DateTimeField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#datetimefield) | [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime) | [`DateTimeInput`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.DateTimeInput) | `input_formats`(7) |
| [`DecimalField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#decimalfield) | [`decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal) | [`NumberInput`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.NumberInput) | `max_value`(8)<br>`min_value`(9)<br>`max_digits`(10)<br>`decimal_places`(11)<br>`step_size`(12) |
| [`DurationField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#durationfield) | [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta) | [`TextInput`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.TextInput) | |
| [`EmailField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#emailfield) | [`str`](../../../core/datatypes/strings.md) | [`EmailInput`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.EmailInput) | `max_length`(13)<br>`min_length`(14)<br>`empty_value`(15) |
| [`FileField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#filefield) | [`UploadedFile`](https://docs.djangoproject.com/en/stable/ref/files/uploads/#django.core.files.uploadedfile.UploadedFile) | [`ClearableFileInput`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.ClearableFileInput) | `max_length`(16)<br>`allow_empty_file`(17) |
| [`FilePathField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#filepathfield) | [`str`](../../../core/datatypes/strings.md) | [`Select`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.Select) | `path`:octicons-key-asterisk-24:{ .red } (18)<br>`recursive`(19)<br>`match`(20)<br>`allow_files`(21)<br>`allow_folders`(22) |
| [`FloatField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#floatfield) | [`float`](../../../core/datatypes/numbers.md#floats) | [`NumberInput`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.NumberInput) | `max_value`(23)<br>`min_value`(24)<br>`step_size`(25) |
| [`GenericIPAddressField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#genericipaddressfield) | [`str`](../../../core/datatypes/strings.md) | [`TextInput`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.TextInput) | `protocol`(26)<br>`unpack_ipv4`(27)<br>`max_length`(28) |
| [`ImageField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#imagefield) | [`UploadedFile`](https://docs.djangoproject.com/en/stable/ref/files/uploads/#django.core.files.uploadedfile.UploadedFile) | [`ClearableFileInput`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.ClearableFileInput) | |
| [`IntegerField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#integerfield) | [`int`](../../../core/datatypes/numbers.md#integers) | [`NumberInput`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.NumberInput) | `max_value`(29)<br>`min_value`(30)<br>`step_size`(31) |
| [`JSONField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#jsonfield) | [`dict`](../../../core/datastructures/dicts.md) o [`list`](../../../core/datastructures/lists.md) | [`Textarea`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.Textarea) | `encoder`(32)<br>`decoder`(33) |
| [`MultipleChoiceField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#multiplechoicefield) | [`list`](../../../core/datastructures/lists.md)[[`str`](../../../core/datatypes/strings.md)] | [`SelectMultiple`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.SelectMultiple) | `choices`:octicons-key-asterisk-24:{ .red } (34) |
| [`NullBooleanField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#nullbooleanfield) | [`bool`](../../../core/datatypes/numbers.md#booleans) o [`None`](../../../core/controlflow/conditionals.md#none) | [`NullBooleanSelect`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.NullBooleanSelect) | |
| [`RegexField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#regexfield) | [`str`](../../../core/datatypes/strings.md) | [`TextInput`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.TextInput) | `regex`:octicons-key-asterisk-24:{ .red } (35) |
| [`SlugField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#slugfield) | [`str`](../../../core/datatypes/strings.md) | [`TextInput`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.TextInput) | `allow_unicode`(36)<br>`empty_value`(37) |
| [`TimeField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#timefield) | [`datetime.time`](https://docs.python.org/3/library/datetime.html#datetime.time) | [`TimeInput`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.TimeInput) | `input_formats`(38) |
| [`TypedChoiceField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#typedchoicefield) | Argumento `coerce` | [`Select`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.Select) | `coerce`(39)<br>`empty_value`(40) |
| [`TypedMultipleChoiceField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#typedmultiplechoicefield) | Argumento `coerce` | [`SelectMultiple`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.SelectMultiple) | `coerce`(41)<br>`empty_value`(42) |
| [`URLField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#urlfield) | [`str`](../../../core/datatypes/strings.md) | [`URLInput`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.URLInput) | `max_length`(43)<br>`min_length`(44)<br>`empty_value`(45) |
| [`UUIDField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#uuidfield) | [`UUID`](https://docs.python.org/3/library/uuid.html#uuid.UUID) | [`TextInput`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.TextInput) | |
| [`ComboField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#combofield) | [`str`](../../../core/datatypes/strings.md) | [`TextInput`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.TextInput) | `fields`:octicons-key-asterisk-24:{ .red } (46) |
| [`MultiValueField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#multivaluefield) | Argumento `compress` | [`TextInput`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.TextInput) | `fields`:octicons-key-asterisk-24:{ .red } (47)<br>`require_all_fields`(48)<br>`widget`(49)<br>`compress`(50) |
| [`SplitDateTimeField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#splitdatetimefield) | [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime) | [`SplitDateTimeWidget`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.SplitDateTimeWidget) | `input_date_formats`(51)<br>`input_time_formats`(52) |
| [`ModelChoiceField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#modelchoicefield) | Instancia de modelo | [`Select`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.Select) | `queryset`:octicons-key-asterisk-24:{ .red } (53)<br>`empty_label`(54)<br>`to_field_name`(55)<br>`blank`(56)<br>`iterator`(57) |
| [`ModelMultipleChoiceField`](https://docs.djangoproject.com/en/stable/ref/forms/fields/#modelmultiplechoicefield) | [QuerySet](https://docs.djangoproject.com/en/stable/ref/models/querysets/#queryset-api) | [`SelectMultiple`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.SelectMultiple) | `queryset`:octicons-key-asterisk-24:{ .red } (58)<br>`to_field_name`(59)<br>`iterator`(60) |
</div>
1. Tamaño máximo permitido.
2. Tamaño mínimo permitido.
3. Si es `#!python True` se aplicará [`strip()`](../../../core/datatypes/strings.md#strip) sobre el valor.
4.  - Valor usado para representar «vacío».
    - Por defecto es [la cadena vacía](../../../core/datatypes/strings.md#empty-string).
5. Iterable de [tuplas](../../../core/datastructures/tuples.md) de dos elementos.
6. Iterable de formatos para convertir un «string» a un objeto `datetime.date`.
7. Iterable de formatos para convertir un «string» a un objeto `datetime.datetime`.
8. Máximo valor permitido.
9. Mínimo valor permitido.
10. Número máximo de dígitos permitido.
11. Número máximo de lugares decimales permitido.
12. Limita la entrada válida a un múltiplo de este valor.
13. Tamaño máximo permitido.
14. Tamaño mínimo permitido.
15. - Valor usado para representar «vacío».
    - Por defecto es [la cadena vacía](../../../core/datatypes/strings.md#empty-string).
16. Longitud máxima de fichero permitida.
17. Si es `#!python True` permite que el contenido del fichero esté vacío.
18. - Ruta absoluta al directorio desde el que listar el contenido.
    - La ruta debe existir.
19. - Si es `#!python True` se listará recursivamente todo el contenido de la ruta indicada.
    - Por defecto es `#!python False`.
20. Patrón de expresión regular para limitar la búsqueda.
21. - Si es `#!python True` permite el listado de ficheros.
    - Por defecto es `#!python True`.
22. - Si es `#!python True` permite el listado de directorios.
    - Por defecto es `#!python False`.
23. Máximo valor permitido.
24. Mínimo valor permitido.
25. Limita la entrada válida a un múltiplo de este valor.
26. Limita la entrada al protocolo especificado.
27. Desempaqueta direcciones IPv4.
28. Tamaño máximo permitido.
29. Máximo valor permitido.
30. Mínimo valor permitido.
31. Limita la entrada válida a un múltiplo de este valor.
32. Una subclase de [`JSONEncoder`](https://docs.python.org/3/library/json.html#json.JSONEncoder) para serializar los tipos de datos no soportados por el serializador JSON.
33. Una subclase de [`JSONDecoder`](https://docs.python.org/3/library/json.html#json.JSONDecoder) para deserializar la entrada.
34. Iterable de [tuplas](../../../core/datastructures/tuples.md) de dos elementos.
35. Expresión regular a aplicar.
36. - Si es `#!python True` permite que se acepten letras [Unicode](../../../core/datatypes/strings.md#unicode).
    - Por defecto es `#!python False`.
37. - Valor usado para representar «vacío».
    - Por defecto es [la cadena vacía](../../../core/datatypes/strings.md#empty-string).
38. Iterable de formatos para convertir un «string» a un objeto `datetime.time`.
39. Función que toma un argumento y devuelve el valor «coercionado».
40. - Valor usado para representar «vacío».
    - Por defecto es [la cadena vacía](../../../core/datatypes/strings.md#empty-string).
41. Función que toma un argumento y devuelve el valor «coercionado».
42. - Valor usado para representar «vacío».
    - Por defecto es [la cadena vacía](../../../core/datatypes/strings.md#empty-string).
43. Tamaño máximo permitido.
44. Tamaño mínimo permitido.
45. - Valor usado para representar «vacío».
    - Por defecto es [la cadena vacía](../../../core/datatypes/strings.md#empty-string).
46. Lista de campos que se deberían usar para validar el valor.
47. Tupla de campos cuyos valores se limpian y se combinan en un único valor.
48. - Si es `#!python True` se lanza un error de validación si algún campo está vacío.
    - Por defecto es `#!python True`.
49. Widget que se usará para los controles.
50. Toma una lista de valores válidos y returna una versión «comprimida» de dichos valores.
51. Lista de formatos para convertir un «string» a un objeto `datetime.date`.
52. Lista de formatos para convertir un «string» a un objeto `datetime.time`.
53. [`QuerySet`](https://docs.djangoproject.com/en/stable/ref/models/querysets/#queryset-api) de objetos desde donde tomar las opciones del campo.
54. Texto del «widget» que indica el valor vacío.
55. Campo a usar como valor de las opciones del «widget».
56. Indica si se creará una opción vacía al usar el «widget» [`RadioSelect`](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.RadioSelect).
57. Iterador usado para generar las opciones desde el «queryset».
58. [`QuerySet`](https://docs.djangoproject.com/en/stable/ref/models/querysets/#queryset-api) de objetos desde donde tomar las opciones del campo.
59. Campo a usar como valor de las opciones del «widget».
60. Iterador usado para generar las opciones desde el «queryset».

<small>:octicons-key-asterisk-24:{ .red }</small> Parámetro requerido.

Para explicar la creación y el uso de _formularios de clase_ vamos a utilizar el mismo <span class="example">ejemplo:material-flash:</span> que en el apartado anterior en el cual creamos un nuevo «post» de un «blog» a partir de los datos introducidos por el usuario.

Lo primero que debemos hacer es definir nuestro formulario en un fichero `forms.py` dentro de la correspondiente aplicación:

```python title="posts/forms.py"
from django import forms


class AddPostForm(forms.Form):#(1)!
    title = forms.CharField()#(2)!
    content = forms.CharField()#(3)!
```
{ .annotate }

1.  - Aunque no es una regla fija, sí es de «buen estilo» añadir el sufijo `Form` al nombre de una clase de formulario.
    - Una clase de formulario debe heredar de `#!python django.forms.Form`.
2. Los campos se definen «manualmente» pero utilizando los [tipos de campos para formularios](https://docs.djangoproject.com/en/stable/ref/forms/fields/#built-in-field-classes) que ofrece Django.
3.  - Los campos se definen «manualmente» pero utilizando los [tipos de campos para formularios](https://docs.djangoproject.com/en/stable/ref/forms/fields/#built-in-field-classes) que ofrece Django.

Ahora veamos cuál es el código que debemos introducir en la plantilla:

```htmldjango title="posts/templates/posts/post/add.html"
<form method="post"><!--(1)!-->
    {% csrf_token %}<!--(2)!-->
    {{ form }}<!--(3)!-->
    <input type="submit" value="Enviar"><!--(4)!-->
</form>
```
{ .annotate }

1.  - Diseñamos el formulario usando petición «post».
    - En un modelo [SSR](webdev.md#ssr) es recomendable validar el envío del formulario en el servidor. Para ello desactivamos la validación HTML → `#!html <form method="post" novalidate>`
2. Django proporciona este mecanismo de seguridad contra CSRF. [Genera un token](https://www.geeksforgeeks.org/csrf-token-in-django/) único que debe ser enviado en la petición para que sea válida.
3. Con esto basta para que se renderice el contenido del formulario en HTML.
4. Es necesario incluir un botón para enviar el formulario.

Por último veamos cómo implementar la vista que debe procesar el formulario:

```python title="posts/views.py"
from django.shortcuts import render, redirect
from django.utils.text import slugify

from .forms import AddPostForm
from .models import Post


def add_post(request):
    if request.method == 'POST':
        if (form := AddPostForm(request.POST)).is_valid():#(1)!
            post_title = form.cleaned_data['title']#(2)!
            post_content = form.cleaned_data['content']#(3)!
            post_slug = slugify(post_title)#(4)!
            Post.objects.create(#(5)!
                title=post_title,
                content=post_content,
                slug=post_slug
            )
            return redirect('posts:post-list')#(6)!
    else:
        form = AddPostForm()#(7)!
    return render(request, 'posts/add_post.html', dict(form=form))#(8)!
```
{ .annotate }

1.  - La petición ha sido «post».
    - Instanciamos (construimos) el formulario con los datos que provienen de la propia petición «post».
    - El método `is_valid()` comprueba si los datos del formulario son válidos.
2.  - Los formularios disponen un atributo [`cleaned_data`](https://docs.djangoproject.com/en/stable/ref/forms/api/#django.forms.Form.cleaned_data) (`dict`) con los datos ya «limpios» y transformados al tipo correspondiente según su definición.
    - Extraemos el título del «post» → La clave `#!python 'title'` debe coincidir con el nombre que se le dio al campo en `forms.py`.
3.  - Los formularios disponen un atributo [`cleaned_data`](https://docs.djangoproject.com/en/stable/ref/forms/api/#django.forms.Form.cleaned_data) (`dict`) con los datos ya «limpios» y transformados al tipo correspondiente según su definición.
    - Extraemos el contenido del «post» → La clave `#!python 'content'` debe coincidir con el nombre que se le dio al campo en `forms.py`.
4. Creamos el «slug» a partir del título del «post».
5. Se [crea](models.md#create-objects) un nuevo «post» a partir del título, contenido y «slug».
6. Todo ha ido bien → Redirigimos (por ejemplo) a la página con el listado de todos los «posts».
7.  - La petición ha sido «get».
    - Construimos un formulario vacío ya que debemos mostrarlo así para que se introduzcan los datos.
8. Renderizamos la plantilla pasando el formulario como contexto y la devolvemos.

### Formularios de modelo { #model-forms }

Este tipo de formularios se construyen a partir de un **modelo Django**.

Cuando estamos trabajando con un modelo y queremos pedir datos en un formulario que finalmente constituirán un objeto de dicho modelo, Django nos ofrece los [`ModelForm`](https://docs.djangoproject.com/en/stable/topics/forms/modelforms/).

El formulario se diseña especificando el **modelo al que está vinculado** y los **campos a utilizar**.

!!! note "Correspondencia de campos"

    Cada (tipo de) campo de modelo tiene su [correspondencia](https://docs.djangoproject.com/en/stable/topics/forms/modelforms/#field-types) con un (tipo de) campo de formulario.

A partir del <span class="example">ejemplo:material-flash:</span> ya visto, vamos a preparar un formulario de modelo para crear un «post» de un «blog»:

```python title="posts/forms.py"
from django import forms

from .models import Post


class AddPostForm(forms.ModelForm):#(1)!
    class Meta:#(2)!
        model = Post#(3)!
        fields = ('title', 'content')#(4)!
```
{ .annotate }

1.  - Aunque no es una regla fija, sí es de «buen estilo» añadir el sufijo `Form` al nombre de una clase de formulario.
    - Una clase **formulario de modelo** debe heredar de `#!python django.forms.ModelForm`.
2. Django permite añadir metadatos a una clase incorporando otra clase interior llamada `Meta`.
3. En el atributo de clase `models` indicamos el modelo al que vincular el presente formulario.
4.  - En el atributo de clase `fields` indicamos los campos del modelo a incluir en el formulario.
    - Puede ser tanto una **tupla** como una **lista**.
    - Si queremos seleccionar todos los campos del modelo, basta con: `#!python fields = '__all__'`
    - También podemos usar el atributo `exclude` para excluir ciertos campos del modelo.

Ahora veremos cómo es el código de la plantilla:

```htmldjango title="posts/templates/posts/post/add.html"
<form method="post"><!--(1)!-->
    {% csrf_token %}<!--(2)!-->
    {{ form }}<!--(3)!-->
    <input type="submit" value="Enviar"><!--(4)!-->
</form>
```
{ .annotate }

1.  - Diseñamos el formulario usando petición «post».
    - En un modelo [SSR](webdev.md#ssr) es recomendable validar el envío del formulario en el servidor. Para ello desactivamos la validación HTML → `#!html <form method="post" novalidate>`
2. Django proporciona este mecanismo de seguridad contra CSRF. [Genera un token](https://www.geeksforgeeks.org/csrf-token-in-django/) único que debe ser enviado en la petición para que sea válida.
3. Con esto basta para que se renderice el contenido del formulario en HTML.
4. Es necesario incluir un botón para enviar el formulario.

Por último veamos cómo implementar la [vista](views.md) que debe procesar el formulario:

=== "Estructura estándar :octicons-organization-24:"

    ```python title="posts/views.py"
    from django.shortcuts import redirect, render
    from django.utils.text import slugify

    from .forms import AddPostForm


    def add_post(request):
        if request.method == 'POST':
            if (form := AddPostForm(request.POST)).is_valid():#(1)!
                form.save()#(2)!
                return redirect('posts:post-list')#(3)!
        else:
            form = AddPostForm()#(4)!
        return render(request, 'posts/add_post.html', dict(form=form))#(5)!
    ```
    { .annotate }

    1.  - La petición ha sido «post».
        - Instanciamos (construimos) el formulario con los datos que provienen de la propia petición «post».
        - El método `is_valid()` comprueba si los datos del formulario son válidos.
    2. Una llamada a `form.save()` en un formulario de modelo guarda el objeto de modelo en la base de datos y lo devuelve.
    3. Todo ha ido bien → Redirigimos (por ejemplo) a la página con el listado de todos los «posts».
    4.  - La petición ha sido «get».
        - Construimos un formulario vacío ya que debemos mostrarlo así para que se introduzcan los datos.
    5. Renderizamos la plantilla pasando el formulario como contexto y la devolvemos.

=== "Forma «compacta» :material-view-compact-outline:"

    ```python title="posts/views.py"
    from django.shortcuts import redirect, render
    from django.utils.text import slugify

    from .forms import AddPostForm


    def add_post(request):
        if (form := AddPostForm(request.POST or None)).is_valid():#(1)!
            form.save()#(2)!
            return redirect('posts:post-list')#(3)!
        return render(request, 'posts/add_post.html', dict(form=form))#(4)!
    ```
    { .annotate }

    1.  - Construimos el formulario.
        - Si hay información en `request.POST` lo usamos, en otro caso pasamos `#!python None` para construir un formulario vacío.
        - El método `is_valid()` comprueba si los datos del formulario son válidos.
    2. Una llamada a `form.save()` en un formulario de modelo guarda el objeto de modelo en la base de datos y lo devuelve.
    3. Todo ha ido bien → Redirigimos (por ejemplo) a la página con el listado de todos los «posts».
    5. Renderizamos la plantilla pasando el formulario como contexto y la devolvemos.

=== "Con lógica adicional :material-calculator:"

    Veamos cómo implementar cierta lógica adicional.
    
    En este <span class="example">ejemplo:material-flash:</span> convertimos a «slug» el título del «post» antes de almacenarlo:

    ```python title="posts/views.py"
    from django.shortcuts import redirect, render
    from django.utils.text import slugify

    from .forms import AddPostForm


    def add_post(request):
        if request.method == 'POST':
            if (form := AddPostForm(request.POST)).is_valid():#(1)!
                post = form.save(commit=False)#(2)!
                post.slug = slugify(post.title)#(3)!
                post.save()#(4)!
                return redirect('posts:post-list')#(5)!
        else:
            form = AddPostForm()#(6)!
        return render(request, 'posts/add_post.html', dict(form=form))#(7)!
    ```
    { .annotate }

    1.  - La petición ha sido «post».
        - Instanciamos (construimos) el formulario con los datos que provienen de la propia petición «post».
        - El método `is_valid()` comprueba si los datos del formulario son válidos.
    2.  - Una llamada a `form.save()` en un formulario de modelo guarda el objeto de modelo en la base de datos y lo devuelve.
        - El problema es que aquí necesitamos generar el «slug» antes de guardar definitivamente. Es por ello que usamos el argumento `#!python commit=False` para que no se escriba aún en disco.
    3.  - Creamos el «slug» a partir del título del «post».
        - Nótese que ya podemos acceder a la variable `post` como un objeto de tipo `Post`.
    4. Ahora sí que definitivamente guardamos el objeto en la base de datos.
    5. Todo ha ido bien → Redirigimos (por ejemplo) a la página con el listado de todos los «posts».
    6.  - La petición ha sido «get».
        - Construimos un formulario vacío ya que debemos mostrarlo así para que se introduzcan los datos.
    7. Renderizamos la plantilla pasando el formulario como contexto y la devolvemos.

!!! info "Acceso a datos"

    En un formulario de modelo, salvo casos excepcionales, deberíamos guardar el objeto de modelo con `save()` y no acceder a través de `cleaned_data`.

### Formularios de edición { #edit-forms }

Es habitual que, además de crear formularios para añadir/crear objetos, necesitemos formularios para editar/modificar dichos objetos.

No es un tipo en sí mismo, pero cabe destacarlos por la forma especial en la que se procesan los datos. Se puede aplicar tanto para [formularios de clase](#class-forms) como para [formularios de modelo](#model-forms).

Seguimos con el <span class="example">ejemplo:material-flash:</span> anterior y vamos a implementar una solución para editar título y contenido de un determinado «post».

Lo primero será definir un [formulario de modelo](#model-forms) para editar «posts»:

```python title="posts/forms.py"
from django import forms

from .models import Post


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
```

La presentación de este modelo en **la plantilla** no difiere mucho de lo que ya se ha visto en apartados anteriores:

```htmldjango title="posts/templates/posts/post/edit.html"
<h1>Editando post "{{ post.title }}"</h1><!--(1)!-->

<form method="post"><!--(2)!-->
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Guardar">
</form>
```
{ .annotate }

1. Aprovechamos para mostrar el título del «post» en la plantilla.
2. En un modelo [SSR](webdev.md#ssr) es recomendable validar el envío del formulario en el servidor. Para ello desactivamos la validación HTML → `#!html <form method="post" novalidate>`

Por último escribimos **la vista** que procesará este formulario:

```python title="posts/views.py" hl_lines="11"
from django.shortcuts import redirect, render
from django.utils.text import slugify

from .forms import EditPostForm
from .models import Post


def edit_post(request, post_slug: str):#(1)!
    post = Post.objects.get(slug=post_slug)#(2)!
    if request.method == 'POST':
        if (form := EditPostForm(request.POST, instance=post)).is_valid():#(3)!
            post = form.save(commit=False)#(4)!
            post.slug = slugify(post.title)#(5)!
            post.save()#(6)!
            return redirect('posts:post-list')#(7)!
    else:
        form = EditPostForm(instance=post)#(8)!
    return render(request, 'posts/edit_post.html', dict(post=post, form=form))#(9)!
```
{ .annotate }

1. Necesitamos conocer el «slug» (u otro campo único) del «post» ya que estamos editando dicho objeto.
2. Buscamos el «post» en la base de datos a través de su «slug».
3.  - La petición ha sido «post».
    - Instanciamos (construimos) el formulario con los datos que provienen de la propia petición «post» pero **además** debemos pasar la ^^instancia^^ actual del objeto que estamos editando mediante el parámetro `instance`.
    - El método `is_valid()` comprueba si los datos del formulario son válidos.
4.  - Una llamada a `form.save()` en un formulario de modelo guarda el objeto de modelo en la base de datos y lo devuelve.
    - El problema es que aquí necesitamos generar el «slug» antes de guardar definitivamente. Es por ello que usamos el argumento `#!python commit=False` para que no se escriba aún en disco.
5.  - Creamos el «slug» a partir del título del «post».
    - Nótese que ya podemos acceder a la variable `post` como un objeto de tipo `Post`.
6. Ahora sí que definitivamente guardamos el objeto en la base de datos.
7. Todo ha ido bien → Redirigimos (por ejemplo) a la página con el listado de todos los «posts».
8.  - La petición ha sido «get».
    - Construimos el formulario con los datos que provienen del «post» que estamos editando.
9. Renderizamos la plantilla pasando el «post» y el formulario como contexto y la devolvemos.

## Widgets { #widgets }

Un «widget» es la representación Django de componente HTML para formulario. El «widget» maneja el renderizado del HTML y la extración de datos desde el correspondiente diccionario GET/POST.

Django proporciona una gran cantidad de [widgets «built-in»](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#built-in-widgets). Cuando definimos un campo de formulario, este tiene asignado un [«widget» por defecto](#fields), pero tenemos la posibilidad personalizar el «widget» o incluso de asignar otro.

### Modificando widgets { #modify-widgets }

Para modificar el «widget» de un determinado campo de formulario hay que distinguir si estamos trabajando con un [formulario de clase](#class-forms) o con un [formulario de modelo](#model-forms).

Retomando el <span class="example">ejemplo:material-flash:</span> de los «posts» de un «blog», veamos cómo asignar un «widget» `Textarea` para el campo «contenido» de un «post»:

=== "Formulario de clase :material-form-select:"

    ```python title="posts/forms.py" hl_lines="5"
    from django import forms

    class AddPostForm(forms.Form):
        title = forms.CharField()
        content = forms.CharField(widget=forms.Textarea)#(1)!
    ```
    { .annotate }

    1. Usamos el parámetro `widget` en el constructor del campo `CharField` indicando que queremos usar un «widget» de tipo `Textarea`.
    

=== "Formulario de modelo :material-form-dropdown:"

    ```python title="posts/forms.py" hl_lines="5"
    class AddPostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ('title', 'content')
            widgets = { 'content': forms.Textarea() }#(1)!
    ```
    { .annotate }
    
    1. El atributo `widgets` de la clase `Meta` nos permite asignar un diccionario donde las claves sean los nombres de los campos y los valores sean los «widgets» que queremos asignar.

### Modificando atributos { #modify-attributes }

Para modificar los atributos HTML de un «widget» podemos hacer uso de la propiedad `attrs` que disponen todos los «widgets». El método para llevar esto a cabo depende de si estamos trabajando con un [formulario de clase](#class-forms) o con un [formulario de modelo](#model-forms).

Continuando con el <span class="example">ejemplo:material-flash:</span> de los «posts» de un blog, veamos cómo modificar el ^^identificador^^ del **campo título** y la ^^clase^^ del **campo contenido**:

=== "Formulario de clase :material-form-select:"

    Una primera aproximación sería modificar la definición de los campos:

    ```python title="posts/forms.py"
    class AddPostForm(forms.Form):
        title = forms.CharField(widget=forms.TextInput(attrs={'id': 'post-title'}))
        content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    ```

    Pero también es posible hacerlo de manera programática:

    ```python title="posts/forms.py"
    class AddPostForm(forms.Form):
        title = forms.CharField()
        content = forms.CharField(widget=forms.Textarea)

        title.widget.attrs.update({'id': 'post-title'})
        content.widget.attrs.update({'class': 'form-control'})
    ```

=== "Formulario de modelo :material-form-dropdown:"

    Una primera aproximación sería modificar la definición en la clase `Meta`:

    ```python title="posts/forms.py"
    class AddPostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ('title', 'content')
            widgets = {
                'title': forms.TextInput(attrs={'id': 'post-title'}),
                'content': forms.Textarea(attrs={'class': 'form-control'}),
            }
    ```

    Pero también es posible hacerlo de manera programática:

    ```python title="posts/forms.py"
    class AddPostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ('title', 'content')
            widgets = {
                'content': forms.Textarea(),
            }
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['title'].widget.attrs.update({'id': 'post-title'})
            self.fields['content'].widget.attrs.update({'class': 'form-control'})
    ```

Si queremos modificar atributos de todos los campos visibles del formulario, podemos aplicar lo siguiente:

```python title="posts/forms.py"
from django import forms

from .models import Post


class AddPostForm(forms.ModelForm):#(1)!
    class Meta:
        model = Post
        fields = ('title', 'content')
    
    def __init__(self, *args, **kwargs):#(2)!
        super().__init__(*args, **kwargs)#(3)!
        for visible in self.visible_fields():#(4)!
            visible.field.widget.attrs['class'] = 'form-control'#(5)!
```
{ .annotate }

1. También es aplicable a formularios de clase que hereden de `forms.Form`.
2. Debemos implementar el constructor del formulario para realizar cambios cuando se construye cada instancia.
3. Llamada al constructor de la clase base `forms.ModelForm`.
4. Recorremos los campos visibles del formulario. Fuente: https://stackoverflow.com/a/29717314
5. Asignamos la clase CSS `form-control`.

#### Campos de tipo fecha/hora { #datetime-widgets }

Uno de los «widgets» que suele ser más complicado de ajustar es el de fecha/hora.

Veamos un <span class="example">ejemplo:material-flash:</span> en el que creamos un formulario de clase para añadir un post que incluye _fecha de publicación_:

```python title="posts/forms.py" hl_lines="4"
class AddPostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    published_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
```

Con esta configuración obtendremos un control interactivo para seleccionar la fecha. Este ajuste también es aplicable tanto a campos de tipo `DateTimeField()` como a formularios de modelo.

## Guardar de forma personalizada { #override-save }

<span class="djversion intermediate">:simple-django: Intermedio :material-tag-multiple-outline:</span>

Hay ocasiones en las que nos interesa personalizar el guardado de un formulario para modificar determinados atributos o realizar otras acciones. Esto se consigue sobreescribiendo el método `save()` del formulario.

### Escenario sin claves ajenas { #override-save-no-fk }

Vamos a retomar el <span class="example">ejemplo:material-flash:</span> del [formulario de modelo](#model-forms) `AddPostForm` donde pretendíamos convertir a «slug» el título del «post» antes de guardarlo definitivamente en disco.

```python title="posts/forms.py" hl_lines="10-14"
from django import forms
from django.utils.text import slugify


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
    
    def save(self, *args, **kwargs):#(1)!
        post = super().save(commit=False)#(2)!
        post.slug = slugify(post.title)#(3)!
        post = super().save(*args, **kwargs)#(4)!
        return post#(5)!
```
{ .annotate }

1.  - Sobreescribimos el método `save()` de la clase `forms.ModelForm`.
    - Esto también sería válido para `forms.Form`.
2.  - Guardamos el formulario _sin escribir en disco_.
    - Con ello obtendremos un objeto `Post` en memoria que podremos manipular.
3. Generamos el «slug» del «post» a partir del título.
4. Ahora ya podemos almacenar el objeto `post` en disco llamando al método de la clase base.
5. :fontawesome-solid-circle-exclamation:{.red} El método `save()` de un formulario ^^siempre^^ debe devolver la instancia creada.

Con este diseño de formulario, crear un nuevo «post» a partir de su _formulario de modelo_ es muy sencillo:

```python title="posts/views.py" hl_lines="10"
from django.shortcuts import redirect, render
from django.utils.text import slugify

from .forms import AddPostForm


def add_post(request):
    if request.method == 'POST':
        if (form := AddPostForm(request.POST)).is_valid():
            post = form.save()#(1)!
            return redirect('posts:post-list')
    else:
        form = AddPostForm()
    return render(request, 'posts/add_post.html', dict(form=form))#(7)!
```
{ .annotate }

1. Toda la «lógica» de generación del «slug» queda encapsulada en el propio formulario.

### Escenario con claves ajenas { #override-save-fk }

Veamos ahora un <span class="example">ejemplo:material-flash:</span> algo más elaborado, en el que no sólo tenemos un «post» sino que tenemos una [clave ajena](models.md#foreign-keys) al ^^usuario^^ que lo escribió.

Por tanto queremos que cuando se cree un nuevo «post» desde el formulario de modelo, también se almacene de forma «automática» el usuario que lo escribió.

Veamos a continuación dos enfoques según lo que necesitemos:

=== "Lógica directa"

    La forma más «directa» de realizar esta tarea sería la siguiente:

    ```python title="posts/forms.py" hl_lines="10-14"
    from django import forms
    from django.utils.text import slugify


    class AddPostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ('title', 'content')
        
        def save(self, user, *args, **kwargs):#(1)!
            post = super().save(commit=False)#(2)!
            post.user = user#(3)!
            post = super().save(*args, **kwargs)#(4)!
            return post
    ```
    { .annotate }

    1. Pasamos el usuario como primer parámetro del método de guardado.
    2. Construimos el «post» en memoria (sin aún escribir en disco).
    3. Asignamos el usuario a la clave ajena correspondiente en el «post».
    4. Guardamos definitivamente el objeto en la base de datos.

    Ahora podremos simplificar el código de la vista correspondiente:

    ```python title="posts/views.py" hl_lines="4"
    def add_post(request):
        if request.method == 'POST':
            if (form := AddPostForm(request.POST)).is_valid():
                post = form.save(request.user)#(1)!
                return redirect('home')
        else:
            form = AddPostForm()
        return render(request, 'posts/add_post.html', dict(form=form))
    ```
    { .annotate }

    1. El primer parámetro que pasamos al método de guardado es el usuario.

=== "Lógica de constructor"

    Es posible que necesitemos realizar alguna lógica adicional en el constructor:

    ```python title="posts/forms.py" hl_lines="12 16"
    from django import forms
    from django.utils.text import slugify


    class AddPostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ('title', 'content')
        
        def __init__(self, user, *args, **kwargs):#(1)!
            super().__init__(*args, **kwargs)#(2)!
            self.user = user#(3)!
            # Manejo posterior de "user"
        
        def save(self, *args, **kwargs):
            post = super().save(commit=False)
            post.user = self.user#(4)!
            post = super().save(*args, **kwargs)
            return post
    ```
    { .annotate }

    1.  - Necesitamos sobreescribir el constructor del formulario.
        - El detalle importante aquí es que el primer parámetro del constructor será el usuario `user` que escribió el «post».
    2. Llamada al constructor de la clase base `forms.ModelForm`.
    3. Guardamos «temporalmente» el usuario que escribió el «post» para utilizarlo posteriormente.
    4. Asignamos el usuario a la clave ajena correspondiente en el «post».

    Ahora podremos simplificar el código de la vista correspondiente:

    ```python title="posts/views.py" hl_lines="4"
    def add_post(request):
        if request.method == 'POST':
            if (form := AddPostForm(request.user, request.POST)).is_valid():#(1)!
                post = form.save()#(2)!
                return redirect('home')
        else:
            form = AddPostForm(request.user)#(3)!
        return render(request, 'posts/add_post.html', dict(form=form))
    ```
    { .annotate }

    1.  - El primer parámetro que pasamos al constructor del formulario es el usuario.
        - El segundo parámetro son los datos propios del formulario.
    2. Simplemente con guardar el formulario ya se estará ejecutando toda la «lógica» necesaria.
    3. Al construir el formulario «vacío» también debemos pasar el usuario.

## Validación { #validation }

<span class="djversion advanced">:simple-django: Avanzado :material-tag-multiple-outline:</span>

Django permite añadir [validación personalizada](https://docs.djangoproject.com/en/stable/ref/forms/validation/) a los formularios. La validación de un un formulario se puede hacer en varios contextos:

1. Validación individual.
2. Validación cruzada.

### Validación individual { #single-validation }

En este tipo de validación analizamos cada campo por separado. Si el formulario dispone de un campo llamado `foo` se podrá personalizar su validación implementando el método de instancia `clean_foo()`.

Supongamos un <span class="example">ejemplo:material-flash:</span> en el que queremos añadir una validación al campo _email_ en un [formulario de registro](auth.md#signup-form) para que no pueda haber dos usuarios con la misma dirección de correo electrónico.

```python title="accounts/forms.py" hl_lines="3 11-15"
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class SignupForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

    def clean_email(self):#(1)!
        email = self.cleaned_data['email']#(2)!
        if self._meta.model.objects.filter(email=email).count() > 0:#(3)!
            raise ValidationError('A user with that email already exists.')#(4)!
        return email#(5)!
```
{ .annotate }

1. Dado que queremos ~~limpiar~~ validar el campo `email` tendremos que implementar el método de instancia `clean_email()`.
2. Extraemos el valor del campo `email`.
3.  - Hacemos una consulta para ver si existe algún usuario con el mismo _email_.
    - Estamos usando un «atajo» para acceder al [modelo de usuario](auth.md#user-model) mediante `self._meta.model`.
4. Lanzamos una excepción de tipo [`ValidationError`](https://docs.djangoproject.com/en/stable/ref/forms/validation/#raising-validationerror) cuando queremos informar de un error de validación.
5. :fontawesome-solid-triangle-exclamation:{ .red } **Siempre** debemos devolver el valor del campo.

### Validación cruzada { #cross-validation }

Cuando la validación que queremos hacer involucra más de un campo, es adecuado implementar un método de instancia `clean()` para esta tarea.

Continuando con el <span class="example">ejemplo:material-flash:</span> anterior del formulario de registro, supongamos ahora que queremos validar que el `first_name` del usuario coincida con el `username` pero en formato _título_:

```python title="accounts/forms.py" hl_lines="3 11-15"
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class SignupForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

    def clean(self):#(1)!
        username = self.cleaned_data['username']#(2)!
        first_name = self.cleaned_data['first_name']#(3)!
        if first_name != username.title():#(4)!
            raise ValidationError('First name must be like username as title.')#(5)!
```
{ .annotate }

1. Validación «cruzada» por tanto tendremos que implementar el método de instancia `clean()`.
2. Extraemos el nombre de usuario.
3. Extramos el nombre «de pila».
4. Comprobamos que coincidan en formato «título».
5. Lanzamos una excepción de tipo [`ValidationError`](https://docs.djangoproject.com/en/stable/ref/forms/validation/#raising-validationerror) cuando queremos informar de un error de validación.

??? info "Acceso a errores"

    Para acceder a estos errores en una plantilla podemos utilizar `#!htmldjango {{ form.non_field_errors }}`.
