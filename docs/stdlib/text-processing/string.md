---
icon: material/code-string
---

# string { #string }

![Fork](images/string/ball.jpg)
(1)
{ .annotate }

1. :fontawesome-regular-copyright: [Steve Johnson](https://unsplash.com/@steve_j) :material-at: [Unsplash](https://unsplash.com) 

El módulo [string](https://docs.python.org/es/3/library/string.html) proporciona **operaciones y constantes** muy útiles para manejo de [cadenas de texto](../../core/datatypes/strings.md), además de distintas estrategias de **formateado de cadenas**.

## Constantes { #constants }

Las constantes definidas en este módulo son las siguientes:

| Constante | Valor |
| --- | --- |
| `string.ascii_lowercase` | `#!python 'abcdefghijklmnopqrstuvwxyz'` |
| `string.ascii_uppercase` | `#!python 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'` |
| `string.ascii_letters` | `#!python 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'` |
| `string.digits` | `#!python '0123456789'` |
| `string.octdigits` | `#!python '01234567'` |
| `string.hexdigits` | `#!python '0123456789abcdefABCDEF'` |
| `string.punctuation` | `#!python '!"#$%&\'()*+,-./:;<=>?@[\\]^_``{|}~'` |
| `string.printable` | `#!python '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_``{|}~ \t\n\r\x0b\x0c'` |
| `string.whitespace` | `#!python ' \t\n\r\x0b\x0c'` |

!!! exercise "Ejercicio"

    [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `all-ascii`

## Plantillas { #templates }

El módulo `string` también nos permite usar **plantillas con interpolación de variables**. Algo similar a los [f-strings](../../core/datatypes/strings.md#fstrings) pero con otro tipo de sintaxis.

Veamos un <span class="example">ejemplo:material-flash:</span> en el que definimos una sencilla plantilla:

```pycon
>>> from string import Template#(1)!

>>> tmpl = Template('$lang is the best programming language in the $place!')#(2)!
```
{ .annotate }

1. Importamos la clase `Template` desde el módulo.
2. Las variables que queramos interporlar deben ir precedidas del signo dólar `#!python $`

Ahora podemos aplicar la _interpolación_ (sustitución) de variables con los valores que nos interesen:

```pycon
>>> tmpl.substitute(lang='Python', place='World')#(1)!
'Python is the best programming language in the World!'

>>> tmpl.substitute({'lang': 'Python', 'place': 'World'})#(2)!
'Python is the best programming language in the World!'
```
{ .annotate }

1. Podemos usar [argumentos nominales](../../core/modularity/functions.md#kwargs).
2. Podemos usar un [diccionario](../../core/datastructures/dicts.md).

Hay que prestar atención cuando el identificador de variable está seguido por algún carácter que, a su vez, puede formar parte del identificador. En este caso hay que utilizar llaves para evitar la ambigüedad.

En el siguiente <span class="example">ejemplo:material-flash:</span> se muestra un ejemplo de _pluralización_:

```pycon hl_lines="1"
>>> tmpl = Template('Congratulations! You won several ${gift}s')

>>> tmpl.substitute(gift='phone')
'Congratulations! You won several phones'
```

### Sustitución segura { #safety-sub }

En el caso de que alguna de las variables que estamos interpolando no exista o no tenga ningún valor, obtendremos un error al sustituir:

```pycon
>>> tmpl = Template('$lang is the best programming language in the $place!')

>>> tmpl.substitute(lang='Python')
Traceback (most recent call last):
  Cell In[2], line 1
    tmpl.substitute(lang='Python')
  File ~/.local/share/uv/python/cpython-3.13.2-macos-aarch64-none/lib/python3.13/string.py:121 in substitute
    return self.pattern.sub(convert, self.template)
  File ~/.local/share/uv/python/cpython-3.13.2-macos-aarch64-none/lib/python3.13/string.py:114 in convert
    return str(mapping[named])
KeyError: 'place'
```

Para estos casos el módulo proporciona el método `self_substitute()` que no emite error si alguna variable no es especificada:

```pycon
>>> tmpl.safe_substitute(lang='Python')
'Python is the best programming language in the $place!'
```

### Casos de uso { #tmpl-use-cases }

A primera vista podría parecer que este sistema de plantillas no aporta gran ventaja sobre los [f-strings](../../core/datatypes/strings.md#fstrings) que ya hemos visto. Sin embargo hay ocasiones en los que puede resultar muy útil.

La mayoría de estas escenarios tienen que ver con **la oportunidad** de definir el «string». Si en el momento de crear la plantilla aún no están disponibles las variables de sustitución, podría interesar utilizar la estrategia que nos proporciona este módulo.

Supongamos un <span class="example">ejemplo:material-flash:</span> en el que tenemos una estructura de «url» y queremos únicamente sustituir una parte de ella. Para no tener que repetir la cadena de texto completa en un «f-string», podríamos seguir este enfoque:

```pycon
>>> from string import Template

>>> urlbase = Template('https://python.org/3/library/$module.html')

>>> for module in ('string', 're', 'difflib'):
...     url = urlbase.substitute(module=module)
...     print(url)
...
https://python.org/3/library/string.html
https://python.org/3/library/re.html
https://python.org/3/library/difflib.html
```
