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

Una **expresión regular** (también conocida como **regex** o **regexp** por su contracción anglosajona **reg**-ular **exp**-ression) es una cadena de texto que conforma un patrón de búsqueda. Se utilizan principalmente para la *búsqueda de patrones* de cadenas de caracteres u *operaciones de sustituciones*.

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

Cuando definimos una expresión regular es conveniente utilizar el :ref:`formato raw <core/datatypes/strings:expresiones literales>` para que los caracteres especiales no pierdan su semántica.

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

Búsqueda
========

La búsqueda de patrones es una de las principales utilidades de las expresiones regulares.

Supongamos que queremos buscar un número de teléfono dentro de un texto. Para ello vamos a utilizar la función `search()`_::

    >>> import re

    >>> text = 'Estaré disponible en el +34755142009 el lunes por la tarde'

    >>> re.search(r'\+?\d{2}\d{9}', text)
    <re.Match object; span=(24, 36), match='+34755142009'>

Esta función devuelve un objeto de tipo ``Match`` en cuya representación podemos ver un campo ``span`` que nos indica el alcance de la concidencia::

    >>> text[24:36]
    '+34755142009'

En el ejemplo anterior estamos buscando un solo elemento. Imaginemos un caso en el que queremos buscar todas las cantidades de dinero que aparecen en un determinado texto. Para ello vamos a utilizar la función `findall()`_::

    >>> text = 'El coste ascendió a 36€ más un 12% de impuestos para un total de 40€'

    >>> re.findall(r'\d+€', text)
    ['36€', '40€']

    >>> re.findall(r'(\d+)€', text)
    ['36', '40']

.. attention::
    La función ``findall()`` no devuelve un objeto ``Match`` sino que retorna una lista con las cadenas de texto coincidentes.

Concidencia
===========

El tipo de objeto `Match`_ es el utilizado en este módulo para representar una coincidencia.

Retomando el ejemplo anterior de la búsqueda del teléfono, veamos qué podemos hacer con este tipo de objetos::

    >>> text = 'Estaré disponible en el +34755142009 el lunes por la tarde'

    >>> m = re.search(r'\+?\d{2}\d{9}', text)

    >>> m
    <re.Match object; span=(24, 36), match='+34755142009'>



.. --------------- Footnotes ---------------

.. [#regex-unsplash] Foto original de portada por `Alice Butenko`_ en Unsplash.

.. --------------- Hyperlinks ---------------

.. _Alice Butenko: https://unsplash.com/@alivka?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
.. _re: https://docs.python.org/es/3/library/re.html
.. _expresiones regulares: https://es.wikipedia.org/wiki/Expresi%C3%B3n_regular
.. _findall(): https://docs.python.org/es/3/library/re.html#re.findall
.. _search(): https://docs.python.org/es/3/library/re.html#re.search
.. _Match: https://docs.python.org/es/3/library/re.html#match-objects
