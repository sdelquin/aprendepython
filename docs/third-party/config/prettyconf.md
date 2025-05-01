---
icon: material/image-filter-center-focus-weak
---

# Pretty Conf { #prettyconf }

[`prettyconf`](https://prettyconf.readthedocs.io/en/latest/index.html) es un paquete Python que facilita la creación de ficheros de configuración mediante la parametrización de sus variables.

Es habitual no incluir credenciales o datos sensibles en el control de versiones de ciertos proyectos de software. Para esto hay varias soluciones, pero la que nos propone `prettyconf` es utilizar una función genérica `config()` que se encargará de recuperar estos datos bien desde _variables de entorno_ o bien desde un fichero `.env`.

## Instalación { #install }

```console
pip install prettyconf
```

## Modo de uso { #usage }

Su modo de uso es muy sencillo:

=== "Valor obligatorio"

    ```python title="settings.py"
    from prettyconf import config

    PASSWD = config('PASSWORD')#(1)!
    ```
    { .annotate }
    
    1.  - Se busca `PASSWORD` en ^^variables de entorno^^ o en fichero `.env`
        - Si se encuentra, se asigna su valor a la variable `PASSWD`
        - Si no se encuentra, se eleva una excepción `UnknownConfiguration`.
    
=== "Valor opcional"

    ```python title="settings.py"
    from prettyconf import config

    UNAME = config('USERNAME', default='guido')#(1)!
    ```
    { .annotate }
    
    1.  - Se busca `USERNAME` en ^^variables de entorno^^ o en fichero `.env`
        - Si se encuentra, se asigna su valor a la variable `UNAME`
        - Si no se encuentra, se asigna el valor por defecto `#!python 'guido'` a `UNAME`

## Ficheros .env { #dotenv }

Aunque también existe la posibilidad de definir los valores mediate _variables de entorno_ suele ser habitual utilizar un fichero de configuración `.env` para ello.

Su estructura es realmente simple:

```ini title=".env"
USERNAME="thisisme"
PASSWORD=verycomplicated#(1)!
MESSAGE="Talk is cheap, show me the code"
```
{ .annotate }

1. Aunque podría ir sin comillas dobles, lo más fácil —para evitar errores— es ponerlas siempre.

!!! danger "Fuera de control de versiones"

    Es crucial dejar fuera del **control de versiones** el archivo `.env` mediante su inclusión en el fichero `.gitignore`.

## Conversiones { #casts }

Por defecto, cualquier valor que le demos a una variable mediante `prettyconf` se interpretará como una **cadena de texto** (`#!python str`).

Pero es posible indicar **conversiones explícitas** en la propia llamada a la función:

<div class="annotate" markdown>
| Conversión | Explicación | Valor `ITEM` | Ejemplo |
| --- | --- | --- | --- |
| `config.boolean` | Convierte a [booleano](../../core/datatypes/numbers.md#booleans)(1) | `#!python 'On'` | `#!python config(ITEM, cast=config.boolean)` :material-arrow-right-box: `#!python True`
| `config.list` | Convierte a [lista](../../core/datastructures/lists.md)(2) | `#!python 'A,B,C'` | `#!python config(ITEM, cast=config.list)` :material-arrow-right-box: `#!python ['A','B','C']`
| `config.tuple` | Convierte a [tupla](../../core/datastructures/tuples.md)(3) | `#!python 'A,B,C'` | `#!python config(ITEM, cast=config.tuple)` :material-arrow-right-box: `#!python ('A','B','C')`
| `config.json` | Convierte a objeto Python(4) | `#!python '{"a": [1, 2], "b": [3, 4]}'` | `#!python config(ITEM, cast=config.json)` :material-arrow-right-box: `#!python {'a': [1, 2], 'b': [3, 4]}`
</div>
1. Ejemplos: `On|Off`, `1|0`, `yes|no`, `true|false`, `t|f`
2. Desde cadenas de texto separadas por **comas**.
3. Desde cadenas de texto separadas por **comas**.
4. Desde cadena de texto con objeto JSON.

### Conversiones personalizadas { #custom-casts }

Además de las conversiones predefinidas es posible crear conversiones personalizadas mediante una función propia.

Por <span class="example">ejemplo:material-flash:</span>, supongamos una configuración que almacena **latitud y longitud** de un determinado lugar (_geolocalización_):

```python title="settings.py"
def geoloc(loc: str) -> tuple[float, float]:
    return tuple(float(v) for v in loc.split(','))

TEIDE_GPS = config('TEIDE_GPS', cast=geoloc)
```

Con esto podríamos «leer» un fichero de configuración tipo:

```ini title=".env"
TEIDE_GPS="28.2723364,-16.6631076"#(1)!
```
{ .annotate }

1. Esto se convertiría en una tupla: `#!python (28.2723364, -16.6631076)` (_cuyos valores ya estarían en formato flotante_).
