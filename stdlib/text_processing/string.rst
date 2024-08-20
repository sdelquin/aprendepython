######
string
######

.. image:: img/steve-johnson-8VO-UxlJ-Lw-unsplash.jpg

El módulo `string`_ proporciona una serie de constantes muy útiles para manejo de "strings", además de distintas estrategias de formateado de cadenas. [#string-unsplash]_

**********
Constantes
**********

Las constantes definidas en este módulo son las siguientes::

    >>> import string

    >>> string.ascii_lowercase
    'abcdefghijklmnopqrstuvwxyz'

    >>> string.ascii_uppercase
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    >>> string.ascii_letters
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    >>> string.digits
    '0123456789'

    >>> string.hexdigits
    '0123456789abcdefABCDEF'

    >>> string.octdigits
    '01234567'

    >>> string.punctuation
    '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    >>> string.printable
    '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

    >>> string.whitespace
    ' \t\n\r\x0b\x0c'

.. admonition:: Ejercicio

    :pypas:`all-ascii`

**********
Plantillas
**********

El módulo ``string`` también nos permite usar plantillas con interpolación de variables. Algo similar a los :ref:`f-strings <core/datatypes/strings:"f-strings">` pero con otro tipo de sintaxis.

Lo primero es definir la plantilla. Las variables que queramos interporlar deben ir precedidas del signo dólar ``$``::

    from string import Template

    tmpl = Template('$lang is the best programming language in the $place!')

Ahora podemos realizar la sustitución con los valores que nos interesen::

    >>> tmpl.substitute(lang='Python', place='World')
    'Python is the best programming language in the World!'

    >>> tmpl.substitute({'lang': 'Python', 'place': 'World'})
    'Python is the best programming language in the World!'

Hay que prestar atención cuando el identificador de variable está seguido por algún carácter que, a su vez, puede formar parte del identificador. En este caso hay que utilizar llaves para evitar la ambigüedad::

    >>> tmpl = Template('You won several ${price}s')

    >>> tmpl.substitute(price='phone')
    'You won several phones'

Sustitución segura
==================

En el caso de que alguna de las variables que estamos interpolando no exista o no tenga ningún valor, obtendremos un error al sustituir::

    >>> tmpl = Template('$lang is the best programming language in the $place!')

    >>> tmpl.substitute(lang='Python')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'place'

Para ello Python nos ofrece el método ``safe_substitute()`` que no emite error si alguna variable no es especificada::

    >>> tmpl.safe_substitute(lang='Python')
    'Python is the best programming language in the $place!'

Casos de uso
============

A primera vista podría parecer que este sistema de plantillas no aporta gran ventaja sobre los :ref:`f-strings <core/datatypes/strings:"f-strings">` que ya hemos visto. Sin embargo hay ocasiones en los que puede resultar muy útil.

La mayoría de estas situaciones tienen que ver con **la oportunidad** de definir el "string". Si en el momento de crear la plantilla aún no están disponibles las variables de sustitución, podría interesar utilizar la estrategia que nos proporciona este módulo.

Supongamos un ejemplo en el que tenemos una estructura de "url" y queremos únicamente sustituir una parte de ella. Para no tener que repetir la cadena de texto completa en un "f-string", podríamos seguir este enfoque::

    >>> urlbase = Template('https://python.org/3/library/$module.html')

    >>> for module in ('string', 're', 'difflib'):
    ...     url = urlbase.substitute(module=module)
    ...     print(url)
    ...
    https://python.org/3/library/string.html
    https://python.org/3/library/re.html
    https://python.org/3/library/difflib.html

.. --------------- Footnotes ---------------

.. [#string-unsplash] Foto original de portada por `Steve Johnson`_ en Unsplash.

.. --------------- Hyperlinks ---------------

.. _Steve Johnson: https://unsplash.com/@steve_j?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
.. _string: https://docs.python.org/es/3/library/string.html
