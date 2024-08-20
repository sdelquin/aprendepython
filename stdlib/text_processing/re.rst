###
re
###

.. image:: img/alice-butenko-zstWUZFj77w-unsplash.jpg

El módulo `re`_ permite trabajar con `expresiones regulares`_. [#regex-unsplash]_

.. hint::
    Si tienes un problema y lo intentas resolver con expresiones regulares, entonces tienes dos problemas 😅 -- Anónimo (Nótese la ironía)

******************************
¿Qué es una expresión regular?
******************************

Una **expresión regular** (también conocida como **regex** o **regexp** por su contracción anglosajona **reg**-ular **exp**-ression) es una cadena de texto que conforma un **patrón de búsqueda**. Se utilizan principalmente para la *búsqueda de patrones* en cadenas de caracteres u *operaciones de sustituciones*.

Se trata de una herramienta ampliamente utilizada en las ciencias de la computación y necesaria para multitud de aplicaciones que traten con información textual.

Pero... ¿qué pinta tiene una expresión regular?

.. code-block::
    
    >>> regex = '^\d{8}[A-Z]$'

La expresión regular anterior nos permite comprobar que una cadena de texto dada es un DNI válido. Si analizamos parte por parte tendríamos lo siguiente:

- ``^`` comienzo de línea.
- ``\d{8}`` dígito que se repite 8 veces.
- ``[A-Z]`` letra en mayúsculas.
- ``$`` final de línea.

********
Sintaxis
********

Las expresiones regulares pueden contener tanto **caracteres especiales** como caracteres ordinarios. La mayoría de los caracteres ordinarios, como ``'A'``, ``'b'``, o ``'0'`` son las expresiones regulares más sencillas; simplemente se ajustan a sí mismas.

Caracteres especiales
=====================

Existen una serie de caracteres que tienen un significado especial dentro de una expresión regular:

.. csv-table::
    :file: tables/regex-chars.csv
    :widths: 10, 50
    :header-rows: 1
    :class: longtable

Expresiones en crudo
====================

Cuando definimos una expresión regular es conveniente utilizar el :ref:`formato raw <core/datatypes/strings:expresiones literales>` en las cadenas de texto para que los caracteres especiales no pierdan su semántica.

Veamos un ejemplo con el tabulador::

    >>> regex = '\t[abc]$'
    >>> print(regex)
    	[abc]$

    >>> regex = r'\t[abc]$'  # formato crudo
    >>> print(regex)
    \t[abc]$

***********
Operaciones
***********

Buscar
======

La búsqueda de patrones es una de las principales utilidades de las expresiones regulares.

Supongamos que queremos buscar un número de teléfono dentro de un texto. Para ello vamos a utilizar la función `search()`_::

    >>> import re

    >>> text = 'Estaré disponible en el +34755142009 el lunes por la tarde'

    >>> regex = r'\+?\d{2}\d{9}'
    >>> re.search(regex, text)
    <re.Match object; span=(24, 36), match='+34755142009'>

Esta función devuelve un objeto de tipo :ref:`Match <stdlib/text_processing/re:coincidencia>` en cuya representación podemos ver un campo ``span`` que nos indica el alcance de la concidencia::

    >>> text[24:36]
    '+34755142009'

En el ejemplo anterior estamos buscando un solo elemento. Imaginemos un caso en el que queremos buscar todas las cantidades de dinero que aparecen en un determinado texto. Para ello vamos a utilizar la función `findall()`_::

    >>> text = 'El coste ascendió a 36€ más un 12% de impuestos para un total de 40€'

    >>> re.findall(r'\d+€', text)
    ['36€', '40€']

Si utilizamos un **grupo de captura** (paréntesis) la función ``findall()`` sólo nos devolverá aquellas coincidencias del grupo de captura::

    >>> re.findall(r'(\d+)€', text)
    ['36', '40']

En el caso de que queramos agrupar expresiones regulares con ``findall()`` sin que se capturen estos grupos debemos utilizar la sintaxis: ``(?:...)``


.. attention::
    La función ``findall()`` no devuelve un objeto ``Match`` sino que retorna una lista con las cadenas de texto coincidentes.

Coincidencia
------------

El tipo de objeto `Match`_ es el utilizado en este módulo para representar una coincidencia.

Retomando el ejemplo anterior de la búsqueda del teléfono, veamos qué podemos hacer con este tipo de objetos::

    >>> text = 'Estaré disponible en el +34755142009 el lunes por la tarde'

    >>> regex = r'\+?\d{2}\d{9}'
    >>> m = re.search(regex, text)

    >>> m
    <re.Match object; span=(24, 36), match='+34755142009'>

Si queremos acceder al texto completo coincidente, tenemos dos alternativas equivalentes::

    >>> m[0]
    '+34755142009'

    >>> m.group(0)
    '+34755142009'

Podemos conocer dónde empieza y dónde acaba el texto coincidente de la siguiente manera::

    >>> m.span()  # equivale a m.span(0)
    (24, 36)

Incluso hay una manera de acceder a estos índices por separado::

    >>> m.start()
    24

    >>> m.end()
    36

Grupos de captura
^^^^^^^^^^^^^^^^^

Los grupos de captura permiten "marcar" partes de la expresión regular para luego poder acceder a cada una de forma directa e independiente.

Para ejemplificar este comportamiento vamos a modificar ligeramente la expresión regular original del número de teléfono y capturar también el prefijo y el propio número de teléfono::

    >>> m = re.search(r'\+?(\d{2})(\d{9})', text) 

.. tip::
    Nótese cómo hemos tenido que **escapar** el símbolo ``+`` usando la barra invertida para quitarle su significado especial.

Ahora podemos acceder a los grupos capturados de la siguiente manera:

    >>> m[1]  # equivale a m.group(1)
    '34'
    >>> m[2]  # equivale a m.group(2)
    '755142009'

Igualmente podemos acceder a los índices de comienzo y fin de cada grupo capturado::

    >>> m.span(1)  # '34'
    (25, 27)

    >>> m.span(2)  # '755142009'
    (27, 36)

Si queremos una aproximación más "semántica", podemos **añadir nombres** a los **grupos de captura**::

>>> regex = r'\+?(?P<prefix>\d{2})(?P<number>\d{9})'
>>> m = re.search(regex, text)

Con este cambio ahora podemos **acceder a los grupos de captura por su nombre**::

    >>> m['prefix']  # equivale a m.group('prefix')
    '34'

    >>> m['number']  # equivale a m.group('number')
    '755142009'

Y también existe la posibilidad de obtener el diccionario completo con los grupos capturados::

    >>> m.groupdict()
    {'prefix': '34', 'number': '755142009'}

Ignorar mayúsculas y minúsculas
-------------------------------

Supongamos que debemos encontrar todas las vocales que hay en un determinado nombre. La primera aproximación sería la siguiente::

    >>> name = 'Alan Turing'
    >>> regex = r'[aeiou]'

    >>> re.findall(regex, name)
    ['a', 'u', 'i']

Aparentemente está bien pero nos damos cuenta de que la primera ``A`` mayúscula no está entre los resultados.

Este módulo de expresiones regulares establece una serie de "flags" que podemos pasar a las distintas funciones para modificar su comportamiento. Uno de los más importantes es el que nos permite ignorar mayúsculas y minúsculas: ``re.IGNORECASE``.

Veamos su aplicación con el ejemplo anterior::

    >>> re.findall(regex, name, re.IGNORECASE)
    ['A', 'a', 'u', 'i']

Podemos "abreviar" esta constante de la siguiente manera::

    >>> re.findall(regex, name, re.I)
    ['A', 'a', 'u', 'i']

Separar
=======

Otras de las operaciones más usadas con expresiones regulares es la separación o división de una cadena de texto mediante un separador.

En su momento vimos el uso de la función :ref:`split() <core/datastructures/lists:dividir una cadena de texto en lista>` para cadenas de texto, pero era muy limitada al especificar patrones avanzados.  Veamos el uso de la función ``re.split()`` dentro de este módulo de expresiones regulares.

Un ejemplo muy sencillo sería **separar la parte entera de la parte decimal** en un determinado número flotante::

    >>> regex = r'[.,]'

    >>> re.split(regex, '3.14')
    ['3', '14']

    >>> re.split(regex, '3,14')
    ['3', '14']

Vemos que la función devuelve una lista con los distintos elementos separados.

.. caution::
    Aunque parezca muy sencillo, este ejemplo no se puede resolver de manera "directa" usando la función ``split()`` de cadenas de texto.

Python también nos da la posibilidad de "capturar" el separador. Siguiendo el ejemplo anterior:

.. code-block::
    :emphasize-lines: 1

    >>> regex = r'([.,])'  # paréntesis: añadimos grupo de captura

    >>> re.split(regex, '3.14')
    ['3', '.', '14']

    >>> re.split(regex, '3,14')
    ['3', ',', '14']


Reemplazar
==========

Este módulo de expresions regulares también nos ofrece la posibilidad de reemplazar ocurrencias dentro de un texto.

A vueltas con el ejemplo del nombre de una persona, supongamos que recibimos la información en formato ``<nombre> <apellidos>`` y que la necesitamos en formato ``<apellidos>, <nombre>``. Veamos cómo resolver este problema con la operación de reemplazar::

    >>> name = 'Alan Turing'

    >>> regex = r'(\w+) +(\w+)'

    >>> repl = r'\2, \1'

    >>> re.sub(regex, repl, name)
    'Turing, Alan'

Hemos utilizado la función ``re.sub()`` que recibe 3 parámetros:

1. La expresión regular a localizar.
2. La expresión de reemplazo.
3. La cadena de texto sobre la que trabajar.

Dado que hemos utilizado *grupos de captura* podemos hacer referencia a ellos a través de sus índices mediante ``\1``, ``\2`` y así sucesivamente.

Al igual que veíamos previamente, existe la posibilidad de nombrar los grupos de captura, y así facilitar la escritura de las expresiones de reemplazo::

    >>> name = 'Alan Turing'

    >>> regex = r'(?P<name>\w+) +(?P<surname>\w+)'

    >>> repl = r'\g<surname>, \g<name>'

    >>> re.sub(regex, repl, name)
    'Turing, Alan'

Esta función admite un uso más avanzado ya que podemos **pasar una función** en vez de una cadena de texto de reemplazo, lo que nos abre un mayor rango de posibilidades.

Siguiendo con el caso anterior, supongamos que queremos hacer la misma transformación pero convirtiendo el apellido a mayúsculas, y asegurarnos de que el nombre queda como título::

    >>> name = 'Alan Turing'

    >>> regex = r'(\w+) +(\w+)'

    >>> re.sub(regex, lambda m: f'{m[2].upper()}, {m[1].title()}', name)
    'TURING, Alan'

.. seealso::
    Existe una función ``re.subn()`` que devuelve una tupla con la nueva cadena de texto reemplazada y el número de sustituciones realizadas.

Casar
=====

Si lo que estamos buscando es ver si una determinada cadena de texto "casa" (coincide) con un patrón de expresión regular, podemos hacer uso de la función ``re.fullmatch()``.

Veamos un ejemplo en el que comprobamos si un texto dado es un DNI válido::

    >>> regex = r'\d{8}[A-Z]'

    >>> text = '54632178Y'

    >>> re.fullmatch(regex, text)  # devuelve un objeto Match
    <re.Match object; span=(0, 9), match='54632178Y'>

Si el patrón no casa la función devuelve ``None``::

    >>> text = '87896532$'

    >>> re.fullmatch(regex, text)  # devuelve None

    >>> re.fullmatch(regex, text) is None
    True

Todo esto lo podemos poner dentro una sentencia condicional haciendo uso además del :ref:`operador morsa <core/controlflow/conditionals:operador morsa>` para aprovechar la variable creada::

    >>> def check_id_card(text: str) -> None:
    ...     REGEX = r'\d{8}[A-Z]'
    ...     if m := re.fullmatch(REGEX, text):
    ...         print(f'{text} es un DNI válido')
    ...         print(m.span())
    ...     else:
    ...         print(f'{text} no es un DNI válido')
    ...
    
    >>> check_id_card('54632178Y')
    54632178Y es un DNI válido
    (0, 9)
    
    >>> check_id_card('87896532$')
    87896532$ no es un DNI válido

Hay una **variante más "flexible"** para casar que es ``re.match()`` y comprueba la existencia del patrón **sólo desde el comienzo de la cadena**. *Es decir, que si el final de la cadena no coincide sigue casando*.

Continuando con el caso anterior de comprobación de los DNI, podemos ver que añadir caracteres al final del documento de identidad no modifica el comportamiento de ``re.match()``::

    >>> regex = r'\d{8}[A-Z]'
    >>> text = '54632178Y###'

    >>> re.match(regex, text)
    <re.Match object; span=(0, 9), match='54632178Y'>

Sin embargo no sucede lo mismo si añadimos caracteres al principio y al final de la cadena::

    >>> regex = r'\d{8}[A-Z]'
    >>> text = '&&&54632178Y###'

    >>> re.match(regex, text) is None  # No casa!
    True

En cualquier caso podemos hacer que ``re.match()`` se comporte como ``re.fullmatch()`` si especificamos los **indicadores de comienzo y final de línea** en el patrón:

.. code-block::
    :emphasize-lines: 1

    >>> regex = r'^\d{8}[A-Z]$'
    >>> text = '54632178Y'

    >>> re.match(regex, text)
    <re.Match object; span=(0, 9), match='54632178Y'>

.. tip::
    Tanto ``re.fullmatch()`` como ``re.match()`` devuelven un objeto de tipo :ref:`Match <stdlib/text_processing/re:coincidencia>` con lo que podemos hacer uso de todos sus métodos y atributos.

Compilar
========

Si vamos a utilizar una expresión regular una única vez entonces no debemos preocuparnos por cuestiones de rendimiento. Pero si repetimos su aplicación, sería más recomendable `compilar`_ la expresión regular a un patrón para mejorar el rendimiento:

.. code-block::
    :emphasize-lines: 3

    >>> regex = r'\d+'

    >>> pat = re.compile(regex)

    >>> type(pat)
    re.Pattern

    >>> re.search(pat, '1:abc;10:def;100;ghi')
    <re.Match object; span=(0, 1), match='1'>

Aclaraciones sobre corchetes
============================

Los corchetes ``[]`` en una expresión regular tienen varios matices:

Los símbolos incluidos pierden su significado especial:
    .. code-block::

        >>> re.match(r'[.]', 'A')  # No casa!
        
        >>> re.match(r'[.]', '.')
        <re.Match object; span=(0, 1), match='.'>

El guión medio hay que escaparlo en situaciones donde no represente un rango:
    .. code-block::
        :emphasize-lines: 7

        >>> re.match(r'[-\d\s]', '-')  # No hay que escapar
        <re.Match object; span=(0, 1), match='-'>

        >>> re.match(r'[\d\s-]', '-')  # No hay que escapar
        <re.Match object; span=(0, 1), match='-'>

        >>> re.match(r'[\d\-\s]', '-') # Hay que escapar!
        <re.Match object; span=(0, 1), match='-'>


**********
Ejercicios
**********

1. :pypas:`vowel-words!`
2. :pypas:`valid-float!`
3. :pypas:`valid-email!`
4. :pypas:`calc-from-str!`
5. :pypas:`valid-url!`

.. --------------- Footnotes ---------------

.. [#regex-unsplash] Foto original de portada por `Alice Butenko`_ en Unsplash.

.. --------------- Hyperlinks ---------------

.. _Alice Butenko: https://unsplash.com/@alivka?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
.. _re: https://docs.python.org/es/3/library/re.html
.. _expresiones regulares: https://es.wikipedia.org/wiki/Expresi%C3%B3n_regular
.. _findall(): https://docs.python.org/es/3/library/re.html#re.findall
.. _search(): https://docs.python.org/es/3/library/re.html#re.search
.. _Match: https://docs.python.org/es/3/library/re.html#match-objects
.. _compilar: https://docs.python.org/3/library/re.html#re.compile
