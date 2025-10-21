---
icon: material/battery-charging-30
---

# Extras { #extras }

<span class="djversion advanced">:simple-django: Avanzado :material-tag-multiple-outline:</span>

Existe un ecosistema enorme de **paquetes de terceros** que ofrecen funcionalidades extras a Django. En esta sección veremos algunos de los más interesantes.

## Django Reload { #django-reload }

[`django-browser-reload`](https://github.com/adamchainz/django-browser-reload) es un paquete Python que recarga la web del proyecto en el navegador cada vez que detecta un cambio en los ficheros de código, **sin necesidad** de hacerlo _manualmente_.

### Instalación { #django-reload-install }

Una vez que **actives el entorno virtual** puedes ejecutar el siguiente comando:

```console
pip install django-browser-reload
```

??? note "requirements.txt"

    Recuerda [añadir la dependencia](setup.md#requirements) `django-browser-reload` a `requirements.txt`.

### Configuración { #django-reload-config }

Para configurar `django-browser-reload` debemos añadir ciertas líneas a `settings.py`:

```python title="main/settings.py"
INSTALLED_APPS = (
    # ...
    'django_browser_reload',
    # ...
)

MIDDLEWARE = [
    # ...
    'django_browser_reload.middleware.BrowserReloadMiddleware',
    # ...
]
```

También debemos añadir cierta configuración a las [URLs de primer nivel](urls.md#main-urls):

```python title="main/urls.py" hl_lines="5"
from django.urls import include, path

urlpatterns = [
    # ...
    path('__reload__/', include('django_browser_reload.urls')),
]
```

### Modo de uso { #django-reload-usage }

Una vez que lancemos el _servidor de desarrollo_ ya estaremos en disposición de trabajar con nuestro proyecto y ver los cambios en el navegador con **recarga automática**.

## Crispy Forms { #cripsy-forms }

[`django-crispy-forms`](https://django-crispy-forms.readthedocs.io/en/latest/) es un paquete Python que proporciona utilidades para renderizar formularios de una manera elegante y reutilizable en Django.

Este paquete permite trabajar con [distintos «frameworks» _CSS_](https://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs). Uno de los más utilizados es **Bootstrap**. En esta sección veremos cómo manejar formularios e integrarlos con estas herramientas.

### Instalación { #crispy-forms-install }

Lo primero será [integrar Bootstrap](static.md#bootstrap) en nuestro proyecto.

Hecho esto y dado que vamos a trabajar con Bootstrap, podemos utilizar directamente el paquete [`crispy-bootstrap5`](https://github.com/django-crispy-forms/crispy-bootstrap5) que, como su nombre indica, nos va a permitir usar Bootstrap v5 y que también nos instalará (como dependencia) el paquete `django-crispy-forms`.

Una vez que **actives el entorno virtual** puedes ejecutar el siguiente comando:

```console
pip install crispy-bootstrap5
```

??? note "requirements.txt"

    Recuerda [añadir la dependencia](setup.md#requirements) `crispy-bootstrap5` a `requirements.txt`.

### Configuración { #crispy-forms-config }

Para configurar `crispy-bootstrap5` debemos añadir ciertas líneas a `settings.py`:

```python title="main/settings.py"
INSTALLED_APPS = (
    # ...
    'crispy_forms',
    'crispy_bootstrap5',
    # ...
)

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'
```

### Modo de uso { #crispy-forms-usage }

Como <span class="example">ejemplo:material-flash:</span> de uso de `crispy-forms` vamos a implementar formularios y plantillas para [inicio de sesión](auth.md#login) y [registro de usuario](auth.md#signup).

#### Login { #crispy-forms-login }

```python title="accounts/forms.py" hl_lines="11-19"
from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):#(1)!
        super().__init__(*args, **kwargs)#(2)!
        self.helper = FormHelper()#(3)!
        self.helper.attrs = dict(novalidate=True)#(4)!
        self.helper.layout = Layout(#(5)!
            FloatingField('username'),#(6)!
            FloatingField('password'),#(7)!
            Submit('login', 'Login', css_class='w-100 mt-2 mb-2'),#(8)!
        )
```
{ .annotate }

1. Será necesario sobreescribir el constructor del formulario para definir las características del renderizado.
2. No puede faltar la llamada al constructor de la clase base.
3. La clase [`FormHelper`](https://django-crispy-forms.readthedocs.io/en/latest/form_helper.html) define el comportamiento del renderizado del formulario en `django-crispy-forms`.
4. Añadimos el atributo `novalidate` al formulario para indicar que [no se valide desde HTML](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation).
5. Utilizamos la clase [`Layout`](https://django-crispy-forms.readthedocs.io/en/latest/layouts.html) que permite cambiar la forma en la que se renderizan los campos del formulario en `django-crispy-forms`.
6. Incluimos en el «layout» el campo `username` del formulario como un [`FloatingField`](https://github.com/django-crispy-forms/crispy-bootstrap5?tab=readme-ov-file#whats-new) (presente en el paquete `crispy-bootstrap5`) que permite usar las [nuevas etiquetas flotantes](https://getbootstrap.com/docs/5.3/forms/floating-labels/) de Bootstrap.
7. Incluimos en el «layout» el campo `password` del formulario como un [`FloatingField`](https://github.com/django-crispy-forms/crispy-bootstrap5?tab=readme-ov-file#whats-new) (presente en el paquete `crispy-bootstrap5`) que permite usar las [nuevas etiquetas flotantes](https://getbootstrap.com/docs/5.3/forms/floating-labels/) de Bootstrap.
8.  - Incluimos en el «layout» un botón para enviar el formulario utilizando [`Submit`](https://django-crispy-forms.readthedocs.io/en/latest/api_layout.html#layout.Submit).
    - Es posible incluir clases CSS al control HTML mediante el parámetro `css_class`.

```htmldjango title="accounts/templates/accounts/login.html" hl_lines="1 17"
{% load crispy_forms_tags %}<!--(1)!-->

<div class="row justify-content-center mt-5">
  <div class="col-md-4">
    <div class="card border-dark">
      <h4 class="card-header">
        Login
      </h4>
      <div class="card-body">
        {% crispy form %}<!--(2)!-->
      </div>
      <div class="card-footer">
        Don't have an account? <a href="{% url 'signup' %}">Sign up</a> here.
      </div>
    </div>
  </div>
</div>
```
{ .annotate }

1. Cargamos las utilidades para plantillas del paquete `crispy-forms`.
2. Así de fácil se renderiza TODO el formulario :material-emoticon-happy:

#### Registro { #crispy-forms-signup }

```python title="accounts/forms.py" hl_lines="9-10 15-24" 
class SignupForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'first_name', 'last_name', 'email')
        required = ('username', 'password', 'first_name', 'last_name', 'email')
        widgets = dict(password=forms.PasswordInput)
        help_texts = dict(username=None)

    def __init__(self, *args, **kwargs):#(1)!
        super().__init__(*args, **kwargs)#(2)!

        for field in self.Meta.required:
            self.fields[field].required = True

        self.helper = FormHelper()#(3)!
        self.helper.attrs = dict(novalidate=True)#(4)!
        self.helper.layout = Layout(#(5)!
            FloatingField('username'),#(6)!
            FloatingField('password'),#(7)!
            FloatingField('first_name'),#(8)!
            FloatingField('last_name'),#(9)!
            FloatingField('email'),#(10)!
            Submit('signup', 'Sign up', css_class='btn-info w-100 mt-2 mb-2'),#(11)!
        )

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user = super().save(*args, **kwargs)
        return user
```
{ .annotate }

1. Será necesario sobreescribir el constructor del formulario para definir las características del renderizado.
2. No puede faltar la llamada al constructor de la clase base.
3. La clase [`FormHelper`](https://django-crispy-forms.readthedocs.io/en/latest/form_helper.html) define el comportamiento del renderizado del formulario en `django-crispy-forms`.
4. Añadimos el atributo `novalidate` al formulario para indicar que [no se valide desde HTML](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation).
5. Utilizamos la clase [`Layout`](https://django-crispy-forms.readthedocs.io/en/latest/layouts.html) que permite cambiar la forma en la que se renderizan los campos del formulario en `django-crispy-forms`.
6. Incluimos en el «layout» el campo `username` del formulario como un [`FloatingField`](https://github.com/django-crispy-forms/crispy-bootstrap5?tab=readme-ov-file#whats-new) (presente en el paquete `crispy-bootstrap5`) que permite usar las [nuevas etiquetas flotantes](https://getbootstrap.com/docs/5.3/forms/floating-labels/) de Bootstrap.
7. Incluimos en el «layout» el campo `password` del formulario como un [`FloatingField`](https://github.com/django-crispy-forms/crispy-bootstrap5?tab=readme-ov-file#whats-new) (presente en el paquete `crispy-bootstrap5`) que permite usar las [nuevas etiquetas flotantes](https://getbootstrap.com/docs/5.3/forms/floating-labels/) de Bootstrap.
8. Incluimos en el «layout» el campo `first_name` del formulario como un [`FloatingField`](https://github.com/django-crispy-forms/crispy-bootstrap5?tab=readme-ov-file#whats-new) (presente en el paquete `crispy-bootstrap5`) que permite usar las [nuevas etiquetas flotantes](https://getbootstrap.com/docs/5.3/forms/floating-labels/) de Bootstrap.
9. Incluimos en el «layout» el campo `last_name` del formulario como un [`FloatingField`](https://github.com/django-crispy-forms/crispy-bootstrap5?tab=readme-ov-file#whats-new) (presente en el paquete `crispy-bootstrap5`) que permite usar las [nuevas etiquetas flotantes](https://getbootstrap.com/docs/5.3/forms/floating-labels/) de Bootstrap.
10. Incluimos en el «layout» el campo `email` del formulario como un [`FloatingField`](https://github.com/django-crispy-forms/crispy-bootstrap5?tab=readme-ov-file#whats-new) (presente en el paquete `crispy-bootstrap5`) que permite usar las [nuevas etiquetas flotantes](https://getbootstrap.com/docs/5.3/forms/floating-labels/) de Bootstrap.
11.  - Incluimos en el «layout» un botón para enviar el formulario utilizando [`Submit`](https://django-crispy-forms.readthedocs.io/en/latest/api_layout.html#layout.Submit).
    - Es posible incluir clases CSS al control HTML mediante el parámetro `css_class`.

```htmldjango title="accounts/templates/accounts/signup.html" hl_lines="1 10"
{% load crispy_forms_tags %}<!--(1)!-->

<div class="row justify-content-center mt-5">
  <div class="col-md-4">
    <div class="card border-dark">
      <h4 class="card-header">
        Sign up
      </h4>
      <div class="card-body">
        {% crispy form %}<!--(2)!-->
      </div>
      <div class="card-footer">
        Already have an account? <a href="{% url 'login' %}">Login</a> here.
      </div>
    </div>
  </div>
</div>
```
{ .annotate }

1. Cargamos las utilidades para plantillas del paquete `crispy-forms`.
2. Así de fácil se renderiza TODO el formulario :material-emoticon-happy:

!!! example "Campos de fichero"

    Cuando implementamos un formulario que incluye campos de fichero, `crispy-forms` lo renderiza mostrando el fichero actual asignado y un botón para «limpiar» el contenido del mismo (siempre que no sea obligatorio).

    Para modificar este comportamiento y simplemente mostrar un control de selección de fichero, podemos modificar el «widget». Veamos un <span class="example">ejemplo:material-flash:</span> con **la imagen de «avatar»** en un _perfil de un usuario_:

    ```python title="users/forms.py" hl_lines="6"
    class EditProfileForm(forms.ModelForm):
        class Meta:
            model = Profile
            fields = ['avatar', 'bio']
            widgets = {
                'avatar': forms.FileInput(attrs={'accept': 'image/*'}),
            }
    ```

## Sorl Thumbnail { #sorl-thumbnail }

[`sorl-thumbnail`](https://sorl-thumbnail.readthedocs.io/en/latest/index.html) es un paquete Python que se integra con Django y permite generar miniaturas («thumbnails») de imágenes de manera sencilla.

### Instalación { #sorl-thumbnail-install }

Una vez que **actives el entorno virtual** puedes ejecutar el siguiente comando:

```console
pip install sorl-thumbnail
```

??? note "requirements.txt"

    Recuerda [añadir la dependencia](setup.md#requirements) `sorl-thumbnail` a `requirements.txt`.

### Configuración { #sorl-thumbnail-config }

Para configurar `sorl-thumbnail` debemos «instalar» la aplicación en `settings.py`:

```python title="main/settings.py"
INSTALLED_APPS = (
    # ...
    'sorl.thumbnail',
    # ...
)
```

!!! note "Cuidado con nombre"

    Cuidado porque la cadena que debemos añadir a `INSTALLED_APPS` es `'sorl.thumbnail'` (_con punto en el medio_).

### Modo de uso { #sorl-thumbnail-usage }

Aunque existen [múltiples casos de uso](https://sorl-thumbnail.readthedocs.io/en/latest/template.html) la forma más habitual de usar `sorl-thumbnail` es crear una miniatura en una plantilla.

Imaginemos por <span class="example">ejemplo:material-flash:</span> que estamos desarrollando una aplicación tipo «blog» donde cada «post» dispone de una [imagen de portada](models.md#file-fields) (atributo `cover`) que queremos mostrar en la plantilla pero en forma de miniatura:

```htmldjango title="posts/templates/posts/post/detail.html" hl_lines="1 5-7"
{% load thumbnail %}<!--(1)!-->

<div class="post">
  <h1>{{ post.title }}</h1>
  {% thumbnail post.cover "200x200" crop="center" format="PNG" as thumb %}<!--(2)!-->
    <img src="{{ thumb.url }}" alt="Post cover"><!--(3)!-->
  {% endthumbnail %}<!--(4)!-->
  <p>{{ post.content }}</p>
</div>
```
{ .annotate }

1. Cargamos las etiquetas/filtros del paquete `sorl-thumbnail`.
2. Usamos la etiqueta `{% thumbnail %}` indicando lo siguiente:
    - La imagen a transformar es `post.cover`.
    - El tamaño de la miniatura será de _200x200 píxeles_.
    - Recorte en la zona central mediante `#!python crop="center"`
    - Usar formato de imagen PNG.
    - Asignar el objeto miniatura a una variable `thumb` con `#!python as thumb`.
3. Utilizamos la variable `thumb` creada anteriormente y mostramos la imagen.
4. Hay que cerrar la etiqueta.

Desde esta forma habremos creado una miniatura de 200x200 píxeles para mostrar la imagen de portada del «post» en cuestión.

## Django Markdownify { #django-markdownify }

[`django-markdownify`](https://django-markdownify.readthedocs.io/en/latest/) es un paquete Python que se integra con Django y ofrece un filtro de plantilla para convertir Markdown en HTML.

### Instalación { #django-markdownify-install }

Una vez que **actives el entorno virtual** puedes ejecutar el siguiente comando:

```console
pip install django-markdownify
```

??? note "requirements.txt"

    Recuerda [añadir la dependencia](setup.md#requirements) `django-markdownify` a `requirements.txt`.
  
:material-check-all:{ .blue } Este paquete depende de [Python-Markdown](https://python-markdown.github.io/) que se instala automáticamente. Puede ser útil para usar su función [`markdown.markdown`](https://python-markdown.github.io/reference/) en vistas u otros componentes.

### Configuración { #django-markdownify-config }

Para configurar `django-markdownify` debemos «instalar» la aplicación en `settings.py`:

```python title="main/settings.py"
INSTALLED_APPS = (
    # ...
    'markdownify.apps.MarkdownifyConfig',
    # ...
)
```

??? info "Whitelist"

    Un detalle importante a tener en cuenta es que este paquete trabaja con una [«whitelist» de etiquetas](https://django-markdownify.readthedocs.io/en/latest/settings.html#whitelist-tags) que por defecto son: `a`, `abbr`, `acronym`, `b`, `blockquote`, `code`, `em`, `i`, `li`, `ol`, `strong`, `ul`.

    Si queremos modificar las etiquetas tendremos que tocar el fichero `settings.py`. Por <span class="example">ejemplo:material-flash:</span> para incluir también la etiqueta `<pre>` tendremos que hacer lo siguiente:

    ```python title="main/settings.py" hl_lines="14"
    MARKDOWNIFY = {
        "default": {
            "WHITELIST_TAGS": [
                'a',
                'abbr',
                'acronym',
                'b',
                'blockquote',
                'em',
                'i',
                'li',
                'ol',
                'p',
                'pre'
                'strong',
                'ul'
            ]
        }
    } 
    ```

### Modo de uso { #django-markdownify-usage }

El modo de uso es realmente sencillo. Veamos un <span class="example">ejemplo:material-flash:</span> en el que partimos de un objeto «post» cuyo contenido está en formato _markdown_:

```htmldjango title="posts/templates/posts/post/detail.html" hl_lines="1 4"
{% load markdownify %}

<h1>{{ post.title }}</h1>
<p>{{ post.content|markdownify }}</p>
```

## Django-RQ { #django-rq }

[`django-rq`](https://github.com/rq/django-rq) es un paquete Python que se integra con Django y permite **desacoplar tareas** enviándolas a una _cola de mensajes_ gestionada por [Redis](https://redis.io/es/).

Entre los casos de uso más habituales están aquellas tareas que consumen mucha CPU o realizan gran cantidad de operaciones de entrada/salida. No es recomendable tener al usuario esperando a que finalicen estas tareas para dar una respuesta HTTP.

Lo habitual es indicar al usuario de que la tarea «en cuestión» ya se está procesando y notificar a posteriori cuando se haya completado.

### Instalación { #django-rq-install }

Una vez que **actives el entorno virtual** puedes ejecutar el siguiente comando:

```console
pip install django-rq
```

??? note "requirements.txt"

    Recuerda [añadir la dependencia](setup.md#requirements) `django-rq` a `requirements.txt`.
  
:material-check-all:{ .blue } Es necesario igualmente [tener instalado el servicio Redis :simple-redis:](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/).

### Configuración { #django-rq-config }

Para configurar `django-rq` debemos añadir ciertas líneas a `settings.py`:

```python title="main/settings.py"
INSTALLED_APPS = (
    # ...
    'django_rq',#(1)!
    # ...
)

RQ_QUEUES = {#(2)!
    'default': {#(3)!
        'HOST': 'localhost',#(4)!
        'PORT': 6379,#(5)!
        'DB': 0,#(6)!
    },
}
```
{ .annotate }

1. Se «instala» la aplicación para que Django la reconozca.
2. Se definen las distintas _colas de mensajes_.
3. Existen la posibilidad de crear distintas prioridades. Con `default` tenemos suficiente (según el contexto).
4. Máquina en la que está instalado el servicio `redis` (en este caso _localhost_).
5. Puerto en el cual está escuchando el servicio `redis` (el habitual es 6379).
6.  - Número (identificador) de base de datos a utilizar dentro de `redis` (en este caso 0). Se podría usar cualquier otro identificador.
    - Especialmente para entornos de producción, si ya existe otro proceso RQ usando `DB=0` hay que usar un identificador no «ocupado», por ejemplo `DB=1`.

Aunque no es obligatorio, es **muy recomendable** añadir las URLs de gestión:

```python title="main/urls.py" hl_lines="9"
from django.contrib import admin
from django.urls import include, path

import notices.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # ...
    path('django-rq/', include('django_rq.urls')),#(1)!
]
```
{ .annotate }

1. Accediendo a http://localhost:8000/django-rq/ (o la URL correspondiente de producción) podremos gestionar las tareas que se envían a RQ.

Por último aplicamos las migraciones correspondientes a la aplicación:

```console hl_lines="1"
$ ./manage.py migrate django_rq
Operations to perform:
  Apply all migrations: django_rq
Running migrations:
  Applying django_rq.0001_initial... OK
```

### Modo de uso { #django-rq-usage }

Para desacoplar una tarea y enviarla a la cola de mensajes hay que realizar tres pasos:

1. Marcar la función en cuestión como una tarea.
2. Invocar el «desacople» de la misma.
3. Levantar un «worker» RQ para atender peticiones.

=== "Definir tarea :material-office-building:"

    ```python title="tasks.py"
    from django_rq import job#(1)!

    @job#(2)!
    def heavy_processing():#(3)!
      ...
    ```
    { .annotate }
    
    1. Importamos el decorador.
    2. Marcamos la función como una tarea _django-rq_.
    3.  - Definimos la función normalmente.
        - En este caso no tiene parámetros, pero se podrían definir aquellos parámetros necesarios.
        - En el caso de pasar argumentos estos deben ser **serializables**. Por defecto se [utiliza el módulo `pickle` como serializador](https://python-rq.org/docs/jobs/#job--queue-creation-with-custom-serializer), pero se podrían definir otros serializadores alternativos.

=== "Invocar tarea :octicons-megaphone-16:"

    ```python
    from .tasks import heavy_processing#(1)!

    heavy_processing.delay()#(2)!
    ```
    { .annotate }
    
    1. Importamos la función propia.
    2. Desacoplamos la tarea.

=== "Lanzar «worker» :octicons-gear-16:"

    ```console
    ./manage.py rqworker
    ```
    
    ??? tip "Recargar tras cambios"

        El comando `./manage.py rqworker` no recarga el proceso cuando hay cambios en el código. Suponiendo que las tareas RQ las estamos escribiendo en ficheros `tasks.py` podrías usar el siguiente comando para un _entorno de desarrollo_:

        ```bash
        watchmedo auto-restart --pattern=tasks.py --recursive -- ./manage.py rqworker #(1)!
        ```
        { .annotate }
        
        1. Si quisiéramos recargar tras modificar cualquier fichero Python tendríamos que modificar el argumento: `--pattern=*.py`

        :material-check-all:{ .blue } El comando `watchmedo` está disponible instalando el paquete [`watchdog`](https://github.com/gorakhargosh/watchdog) mediante `pip install watchdog`.

## Enviar correo { #sending-email }

Una tarea bastante habitual en cualquier aplicación web es notificar a los usuarios mediante correo electrónico. Es por ello que Django ofrece [una serie de funcionalidades de envío de correo](https://docs.djangoproject.com/en/stable/topics/email/), que hacen esta tarea realmente sencilla.

### Configuración { #sending-email-config }

Es necesario definir —al menos— las siguientes variables en el fichero de configuración del proyecto:

```python title="main/settings.py"
EMAIL_HOST = 'email-host'
EMAIL_PORT = 'email-port'
EMAIL_HOST_USER = 'email-host-user'
EMAIL_HOST_PASSWORD = 'email-host-password'
DEFAULT_FROM_EMAIL = 'default-from-email'#(1)!
```
{ .annotate }

1.  - Se trata del correo electrónico origen que verá el usuario notificado.
    - Aunque este dato no es olibatorio, resulta cómodo fijarlo aquí y poder usarlo en el resto de la aplicación.

#### Brevo { #brevo }

Basándome en mi experiencia, y sin buscar ningún tipo de publicidad (no me llevo nada), me gustaría comentar aquí el caso de [Brevo](https://www.brevo.com/es/) que proporciona [credenciales «gratuitas»](https://www.brevo.com/es/pricing/) para poder hacer uso de sus servicios SMTP.

Una vez dados de alta en _Brevo_, podemos acceder a la [sección de configuración SMTP](https://app.brevo.com/settings/keys/smtp) y tendremos la posibilidad de encontrar los datos de configuración que necesitamos para el envío de correo:

| Configuración | Valor |
| --- | --- |
| `EMAIL_HOST` | smtp-relay.brevo.com |
| `EMAIL_PORT` | 587 |
| `EMAIL_HOST_USER` | Tu correo electrónico de la cuenta [brevo.com](https://brevo.com) |
| `EMAIL_HOST_PASSWORD` | Valor de clave SMTP |

!!! danger "EMAIL_HOST_PASSWORD"

    Nunca expongas el contenido de `EMAIL_HOST_PASSWORD` ni lo incluyas en el control de versiones de tu proyecto.

### Modo de uso { #sending-email-usage }

Existen varias maneras de enviar correo a través de Django, pero aquí vamos a tratar el caso de uso mediante la clase [`EmailMessage`](https://docs.djangoproject.com/en/stable/topics/email/#the-emailmessage-class), ya que es la que ofrece mayor flexibilidad.

=== "Envío simple"

    ```python
    from django.core.mail import EmailMessage

    email = EmailMessage(
        subject='Email test',
        body='Hello there! This is the email body',
        to=['recipient@example.com'],
    )

    email.send()
    ```

=== "Envío con HTML"

    ```python hl_lines="8"
    from django.core.mail import EmailMessage
    
    email = EmailMessage(
        subject='Email test',
        body='<h3>Hello there!</h3> <p>This is the email body</p>',
        to=['recipient@example.com'],
    )
    email.content_subtype = 'html'
    
    email.send()
    ```

=== "Envío con HTML y adjunto"

    ```python hl_lines="9"
    from django.core.mail import EmailMessage
    
    email = EmailMessage(
        subject='Email test',
        body='<h3>Hello there!</h3> <p>This is the email body</p>',
        to=['recipient@example.com'],
    )
    email.content_subtype = 'html'
    email.attach_file('report.pdf')
    
    email.send()
    ```

??? tip "Múltiples destinatarios"

    En el caso de querer enviar el mismo correo a múltiples destinatarios, podemos usar el parámetro `to` (_formato lista_) del constructor sobre `EmailMessage()`.

    Pero una forma más «eficiente» de llevarlo a cabo es utilizando la función [`send_mass_mail()`](https://docs.djangoproject.com/en/stable/topics/email/#send-mass-mail) que sólo abre una única conexión con el servidor SMTP.

## Django ColorField { #django-colorfield }

[`django-colorfield`](https://github.com/fabiocaccamo/django-colorfield) es un paquete Python que proporciona un **«nuevo» campo para almacenar colores** en los modelos de Django.

Además ofrece un **«color picker»** muy agradable para seleccionar el color de manera visual en la interfaz administrativa de Django.

### Instalación { #django-colorfield-install }

Una vez que **actives el entorno virtual** puedes ejecutar el siguiente comando:

```console
pip install django-colorfield
```

??? note "requirements.txt"

    Recuerda [añadir la dependencia](setup.md#requirements) `django-colorfield` a `requirements.txt`.

### Configuración { #django-colorfield-config }

Para configurar `django-colorfield` debemos «instalar» la aplicación en `settings.py`:

```python title="main/settings.py"
INSTALLED_APPS = (
    # ...
    'colorfield',
    # ...
)
```

??? tip "Producción"

    Sólo en un escenario de producción, debes ejecutar también el siguiente comando para recopilar los ficheros estáticos y que el selector de color en la interfaz administrativa funcione correctamente:

    ```console
    python manage.py collectstatic
    ```

### Modo de uso { #django-color-usage }

Este paquete proporciona la clase [`ColorField`](https://github.com/fabiocaccamo/django-colorfield?tab=readme-ov-file#models) para almacenar colores.

Veamos un <span class="example">ejemplo:material-flash:</span> para almacenar el ^^color de la categoría de un «post»^^ en un proyecto de «blog»:

```python title="categories/models.py" hl_lines="8"
from colorfield.fields import ColorField
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256, unique=True)
    color = ColorField(default='#FF0000')#(1)!
```
{ .annotate }

1.  - Es posible definir un **color por defecto**.
    - En este caso se ha definido el rojo `#FF0000`.
