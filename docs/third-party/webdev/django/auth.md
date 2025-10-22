---
icon: material/key-chain-variant
---

# Autenticación { #auth }

<span class="djversion intermediate">:simple-django: Intermedio :material-tag-multiple-outline:</span>

Django proporciona un [sistema de autenticación](https://docs.djangoproject.com/en/stable/topics/auth/default/) —incorporado en el propio framework— que facilita en gran medida la gestión de accesos y de usuarios.

## Usuario { #user }

Existe un modelo [`User`](https://docs.djangoproject.com/en/stable/ref/contrib/auth/#user-model) que ya viene predefinido en Django. A continuación se muestran sus atributos más destacados:

| Atributo | Descripción |
| --- | --- |
| [`username`](https://docs.djangoproject.com/en/stable/ref/contrib/auth/#django.contrib.auth.models.User.username) | Nombre de usuario |
| [`password`](https://docs.djangoproject.com/en/stable/ref/contrib/auth/#django.contrib.auth.models.User.password) | Contraseña |
| [`first_name`](https://docs.djangoproject.com/en/stable/ref/contrib/auth/#django.contrib.auth.models.User.first_name) | Nombre |
| [`last_name`](https://docs.djangoproject.com/en/stable/ref/contrib/auth/#django.contrib.auth.models.User.last_name) | Apellido(s) |
| [`email`](https://docs.djangoproject.com/en/stable/ref/contrib/auth/#django.contrib.auth.models.User.last_name) | Correo electrónico |

??? tip "Password"

    El **password** se almacena [«hasheado»](https://docs.djangoproject.com/en/stable/topics/auth/passwords/#password-management-in-django) en la base de datos. Django utiliza —por defecto— el algoritmo [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) con una función «hash» [SHA256](https://es.wikipedia.org/wiki/SHA-2), aunque se podría cambiar. El formato utilizado es: `<algorithm>$<iterations>$<salt>$<hash>`

    Un <span class="example">ejemplo:material-flash:</span> de «password» en la base de datos sería:

    ```pycon
    >>> user.password
    'pbkdf2_sha256$1000000$Y9opN6ZKNLMm9E1vAPrBzi$dNDnlbmN+phNora6ZUnok05NTH7BEgWjpg/mqulk3Yw='
    ```

### Acceso al modelo { #user-model }

Este modelo se encuentra en la clase `#!python django.contrib.auth.models.User`, pero es posible «suplantarla» con un modelo propio de usuario. Es por ello que ^^no se recomienda^^ acceder directamente a esta clase a través de un `import` sino utilizar otros «atajos» más genéricos.

Para **acceder al modelo de usuario** disponemos de dos vías:

| Para uso en... | Importación | Acceso | Descripción | Valor por defecto |
| --- | --- | --- | --- | --- |
| [Claves ajenas](models.md#foreign-keys) | `#!python from django.conf import settings` | `settings.AUTH_USER_MODEL` | Cadena de texto cualificada | `#!python 'auth.User'` |
| [Vistas](views.md) y/o [formularios](forms.md) | `#!python from django.contrib.auth import get_user_model`  | `get_user_model()` | Función que devuelve el modelo | `django.contrib.auth.models.User` |

### Acceso a la instancia { #user-instance }

Para **acceder a la instancia del usuario logeado** en Django disponemos de dos vías:

| Para uso en... | Acceso |
| --- | --- |
| [Vistas](views.md) | `request.user` |
| [Plantillas](templates.md) | `#!htmldjango {{ user }}` |

Veamos un <span class="example">ejemplo:material-flash:</span> en el que accedemos a la instancia de un usuario:

```pycon
>>> from django.contrib.auth import get_user_model
>>> User = get_user_model()

>>> guido = User.objects.get(username='guido')

>>> guido
<User: guido>
>>> guido.first_name
'Guido'
>>> guido.last_name
'van Rossum'
```

!!! info "Usuario anónimo"

    Cuando el usuario que interactúa con la web aún no está autenticado, Django lo identifica como [`AnonymousUser`](https://docs.djangoproject.com/en/stable/ref/contrib/auth/#anonymoususer-object).

## Aplicación { #app }

Se recomienda [crear una aplicación](apps.md#creation) `accounts` (o similar) donde implementar todos los artefactos necesarios para la autenticación de usuarios.

En las URLs de primer nivel deberíamos incluir algo así:

```python title="main/urls.py" hl_lines="7"
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('', include('accounts.urls')),
]
```

De tal forma que tendremos acceso «directo» a las funcionalidades de autenticación desde la raíz de la URL:

- `/login/`
- `/logout/`
- `/signup/`

!!! warning "Nombre"

    No podemos llamar `auth` a esta aplicación porque entraría en conflicto con la aplicación [`django.contrib.auth`](https://docs.djangoproject.com/en/stable/ref/contrib/auth/#django-contrib-auth) de Django.

## Login { #login }

Para implementar el procedimiento de **inicio de sesión** debemos desarrollar varios elementos:

- [x] Formulario.
- [x] Plantilla.
- [x] Vista.
- [x] URL.
- [x] Enlace.

### Formulario de login { #login-form }

```python title="accounts/forms.py"
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)#(1)!
```
{ .annotate }

1. El [«widget»](forms.md/#widgets) nos permite cambiar el elemento HTML al renderizar el campo de formulario.

### Plantilla de login { #login-template }

```htmldjango title="accounts/templates/accounts/login.html"
<form method="post">
  {% csrf_token %}
  {{ form }}
  <input type="submit" value="Login">
</form>
```

### Vista de login { #login-view }

```python title="accounts/views.py"
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm

def user_login(request):#(1)!
    FALLBACK_REDIRECT = 'index'#(2)!

    if request.user.is_authenticated:#(3)!
        return redirect(reverse(FALLBACK_REDIRECT))
    if request.method == 'POST':
        if (form := LoginForm(request.POST)).is_valid():#(4)!
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if user := authenticate(request, username=username, password=password):#(5)!
                login(request, user)#(6)!
                return redirect(request.GET.get('next', reverse(FALLBACK_REDIRECT)))#(7)!
            else:
                form.add_error(None, 'Incorrect username or password.')#(8)!
    else:
        form = LoginForm()
    return render( request, 'accounts/login.html', {'form': form})
```
{ .annotate }

1. No podemos llamar `login` a nuestra vista ya que entraría en conflicto con la función [`login`](https://docs.djangoproject.com/en/stable/topics/auth/default/#django.contrib.auth.login) de Django.
2. Indica aquí un nombre de URL a la que redirigir (por defecto).
3. Si el usuario ya está autenticado lo redirigimos a una URL predefinida.
4. El formulario debe estar validado para poder continuar.
5. La función [`authenticate`](https://docs.djangoproject.com/en/stable/topics/auth/default/#django.contrib.auth.authenticate) de Django verifica si las credenciales de usuario son correctas. En tal caso devuelve el usuario en cuestión. En otro caso devuelve `#!python None`.
6. La función [`login`](https://docs.djangoproject.com/en/stable/topics/auth/default/#django.contrib.auth.login) de Django se encarga de «logear» (iniciar sesión) al usuario.
7. Si todo ha ido bien redirigimos a la siguiente URL `next` (si es que existe) o a la URL por defecto `FALLBACK_REDIRECT`, en otro caso.
8.  - Añadimos un error al formulario indicando que las credenciales son incorrectas.
    - El primer parámetro de la función `add_error()` es el campo al que queremos añadir el error, y el segundo parámetro es el mensaje de error en sí mismo.
    - Como estos errores son «generales» a todo el formulario, indicamos `#!python None` en el campo.

### URL de login { #login-url }

```python title="accounts/urls.py" hl_lines="6"
from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
]
```


!!! info "LOGIN_URL"

    Es importante definir en el fichero `settings.py` la variable `LOGIN_URL` que le indica a Django a qué URL debe redirigir al usuario para hacer «login».

    ```python title="main/settings.py"
    LOGIN_URL = 'login'#(1)!
    ```
    { .annotate }

    1. Vale tanto una URL como una URL nombrada.

    :material-check-all:{ .blue } Da igual el «lugar» en el que pongamos estas variables dentro de `settings.py`. Una buena práctica sería **agrupar** aquellas configuraciones que tengan que ver entre sí.

### Enlace de login { #login-link }

En algún punto de nuestras plantillas deberemos añadir un enlace para iniciar sesión:

```htmldjango
<a href="{% url 'login' %}">Login</a><!--(1)!-->
```
{ .annotate }

1. Puedes usar condiciones para saber si el usuario está autenticado :material-arrow-right-box: `#!htmldjango {% if user.is_authenticated %}`.

## Logout { #logout }

Para implementar el procedimiento de **cierre de sesión** debemos desarrollar varios elementos:

- [ ] Formulario.
- [ ] Plantilla.
- [x] Vista.
- [x] URL.
- [x] Enlace.

### Vista de logout { #logout-view }

```python title="accounts/views.py"
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse


def user_logout(request):
    FALLBACK_REDIRECT = 'index'

    logout(request)#(1)!
    return redirect(reverse(FALLBACK_REDIRECT))
```
{ .annotate }

1. La función [`logout`](https://docs.djangoproject.com/en/stable/topics/auth/default/#django.contrib.auth.logout) de Django se encarga de cerrar la sesión del usuario actualmente «logeado».

### URL de logout { #logout-url }

```python title="accounts/urls.py" hl_lines="6"
from django.urls import path

from . import views

urlpatterns = [
    path('logout/', views.user_logout, name='logout'),
]
```

### Enlace de logout { #logout-link }

En algún punto de nuestras plantillas deberemos añadir un enlace para cerrar sesión:

```htmldjango
<a href="{% url 'logout' %}">Logout</a><!--(1)!-->
```
{ .annotate }

1. Puedes usar condiciones para saber si el usuario está autenticado :material-arrow-right-box: `#!htmldjango {% if user.is_authenticated %}`.

## Registro { #signup }

Para implementar el procedimiento de **registro de usuario** debemos desarrollar varios elementos:

- [x] Formulario.
- [x] Plantilla.
- [x] Vista.
- [x] URL.
- [x] Enlace.

### Formulario de registro { #signup-form }

```python title="accounts/forms.py"
from django import forms
from django.contrib.auth import get_user_model


class SignupForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'first_name', 'last_name', 'email')
        widgets = dict(password=forms.PasswordInput)#(1)!
        help_texts = dict(username=None)#(2)!
    
    def save(self, *args, **kwargs):#(3)!
        user = super().save(commit=False)#(4)!
        user.set_password(self.cleaned_data['password'])#(5)!
        user = super().save(*args, **kwargs)#(6)!
        return user#(7)!
```
{ .annotate }

1. Necesitamos modificar el _widget_ para que no se vea la contraseña en pantalla.
2. Si no ponemos esto, nos aparecerá un mensaje (largo) en el formulario indicando todos los requisitos del nombre de usuario.
3. Sobreescribimos el método [`save()`](https://docs.djangoproject.com/en/stable/topics/forms/modelforms/#the-save-method) del formulario de modelo para realizar ciertas operaciones adicionales.
4. Construimos el objeto `user` «en memoria» con la llamada al constructor de la clase base `forms.ModelForm`.
5. Utilizamos la función [`set_password`](https://docs.djangoproject.com/en/stable/ref/contrib/auth/#django.contrib.auth.models.User.set_password) de Django para poder almacenar la contraseña de usuario «hasheada».
6. Escribimos la instancia en la base de datos.  
7. :fontawesome-solid-circle-exclamation:{.red} El método `save()` de un formulario ^^siempre^^ debe devolver la instancia creada.

??? example "Campos requeridos"

    Cuando implementamos un [formulario de modelo](forms.md#model-forms) los campos requeridos se infieren directamente desde el propio modelo. Pero hay ocasiones en las que no tenemos acceso directo al modelo, como es el caso que nos ocupa donde estamos utilizando el modelo `User` que proporciona Django.

    El modelo `User` sólo define como requeridos el nombre de usuario y la contraseña. Si quisiéramos añadir otros atributos como requeridos tendríamos que implementar otra estrategia. A continuación se muestra el código del formulario añadiendo un atributo `required` donde indicamos los campos requeridos y son modificamos en el constructor de la clase:

    ```python title="accounts/forms.py" hl_lines="9 13-17"
    from django import forms
    from django.contrib.auth import get_user_model


    class SignupForm(forms.ModelForm):
        class Meta:
            model = get_user_model()
            fields = ('username', 'password', 'first_name', 'last_name', 'email')
            required = ('username', 'password', 'first_name', 'last_name', 'email')
            widgets = dict(password=forms.PasswordInput)
            help_texts = dict(username=None)
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        
            for field in self.Meta.required:
                self.fields[field].required = True
        
        def save(self, *args, **kwargs):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data['password'])
            user = super().save(*args, **kwargs)
            return user
    ```

### Plantilla de registro { #signup-template }

```htmldjango title="accounts/templates/accounts/signup.html"
<form method="post">
  {% csrf_token %}
  {{ form }}
  <input type="submit" value="Sign up">
</form>
```

### Vista de registro { #signup-view }

```python title="accounts/views.py"
from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import SignupForm


def user_signup(request):
    FALLBACK_REDIRECT = 'index'

    if request.user.is_authenticated:#(1)!
        return redirect(reverse(FALLBACK_REDIRECT))
    if request.method == 'POST':
        if (form := SignupForm(request.POST)).is_valid():
            user = form.save()#(2)!
            login(request, user)#(3)!
            return redirect(FALLBACK_REDIRECT)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})
```
{ .annotate }

1. Si el usuario ya está autenticado lo redirigimos a una URL predefinida.
2. Guardamos el formulario de modelo con lo que obtenemos una instancia de usuario.
3. «Logear» al usuario tras el registro es algo opcional. Depende del contexto.

### URL de registro { #signup-url }

```python title="main/urls.py" hl_lines="6"
from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.user_signup, name='signup')
]
```

### Enlace de registro { #signup-link }

En algún punto de nuestras plantillas deberemos añadir un enlace para registro de usuario:

```htmldjango
<a href="{% url 'signup' %}">Sign up</a><!--(1)!-->
```
{ .annotate }

1. Puedes usar condiciones para saber si el usuario está autenticado :material-arrow-right-box: `#!htmldjango {% if user.is_authenticated %}`.

## Requisito estar logeado { #login-required }

Si necesitamos que ciertas vistas de nuestra aplicación sean ^^accesibles únicamente^^ para **usuarios logeados** podemos hacer uso del decorador [`@login_required`](https://docs.djangoproject.com/en/stable/topics/auth/default/#the-login-required-decorator) que nos proporciona Django.

Supongamos por <span class="example">ejemplo:material-flash:</span> que una persona sólo puede escribir un «post» en nuestro «blog» si está previamente logeada:

```python title="posts/views.py"
from django.contrib.auth.decorators import login_required


@login_required
def add_post(request):
    # rest of the view code here
```

!!! warning "Redirección para login"

    Si un usuario no logeado trata de acceder a una vista «protegida», será redirigido a la URL de «login» que venga especificada en la variable [`LOGIN_URL`](#login-url) del fichero `settings.py`.
