######
Tuplas
######

.. image:: img/engin-akyurt-hdJYDQ9CUtQ-unsplash.jpg


El concepto de **tupla** es muy similar al de :ref:`lista <core/datastructures/lists:Listas>`. Aunque hay algunas diferencias menores, lo fundamental es que, mientras una *lista* es mutable y se puede modificar, una *tupla* no admite cambios y por lo tanto, es **inmutable**. [#chain-unsplash]_

**************
Creando tuplas
**************

Podemos pensar en crear tuplas tal y como :ref:`lo hacíamos con listas <core/datastructures/lists:Creando listas>`, pero usando **paréntesis** en lugar de *corchetes*::

    >>> empty_tuple = ()

    >>> tenerife_geoloc = (28.46824, -16.25462)

    >>> three_wise_men = ('Melchor', 'Gaspar', 'Baltasar')

.. tip::
    Al igual que con las listas, las tuplas admiten diferentes tipos de datos: ``('a', 1, True)``

Tuplas de un elemento
=====================

Hay que prestar especial atención cuando vamos a crear una **tupla de un único elemento**. La intención primera sería hacerlo de la siguiente manera::

    >>> one_item_tuple = ('Papá Noel')

    >>> one_item_tuple
    'Papá Noel'

    >>> type(one_item_tuple)
    str

Realmente, hemos creado una variable de tipo ``str`` (cadena de texto). Para crear una tupla de un elemento debemos añadir una **coma** al final::

    >>> one_item_tuple = ('Papá Noel',)

    >>> one_item_tuple
    ('Papá Noel',)

    >>> type(one_item_tuple)
    tuple

Tuplas sin paréntesis
=====================

Según el caso, hay veces que nos podemos encontrar con tuplas que no llevan paréntesis. Quizás no está tan extendido, pero a efectos prácticos tiene el mismo resultado. Veamos algunos ejemplos de ello::

    >>> one_item_tuple = 'Papá Noel',

    >>> three_wise_men = 'Melchor', 'Gaspar', 'Baltasar'

    >>> tenerife_geoloc = 28.46824, -16.25462

.. warning::
    Aunque está permitido, **NUNCA** llames ``tuple`` a una variable porque destruirías la función que nos permite crear tuplas. Y tampoco uses nombres derivados como ``_tuple`` o ``tuple_`` ya que no son nombres representativos que :ref:`identifiquen el propósito de la variable <core/datatypes/data:convenciones para nombres>`.

*******************
Modificar una tupla
*******************

Como ya hemos comentado previamente, las tuplas con estructuras de datos **inmutables**. Una vez que las creamos con un valor, no podemos modificarlas. Veamos qué ocurre si lo intentamos::

    >>> three_wise_men = 'Melchor', 'Gaspar', 'Baltasar'

    >>> three_wise_men[0] = 'Tom Hanks'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'tuple' object does not support item assignment

**********
Conversión
**********

Para convertir otros tipos de datos en una tupla podemos usar la función ``tuple()``::

    >>> shopping = ['Agua', 'Aceite', 'Arroz']

    >>> tuple(shopping)
    ('Agua', 'Aceite', 'Arroz')

Esta conversión es válida para aquellos tipos de datos que sean *iterables*: cadenas de caracteres, listas, diccionarios, conjuntos, etc. Un ejemplo que no funciona es intentar convertir un número en una tupla::

    >>> tuple(5)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'int' object is not iterable

El uso de la función ``tuple()`` sin argumentos equivale a crear una tupla vacía::

    >>> tuple()
    ()

.. tip:: Para crear una tupla vacía, se suele recomendar el uso de ``()`` frente a ``tuple()``, no sólo por ser más *pitónico* sino por tener (en promedio) un mejor rendimiento en tiempos de ejecución.

**********************
Operaciones con tuplas
**********************

Con las tuplas podemos realizar :ref:`todas las operaciones que vimos con listas <core/datastructures/lists:Operaciones con listas>` **salvo las que conlleven una modificación** "in-situ" de la misma:

* ``reverse()``
* ``append()``
* ``extend()``
* ``remove()``
* ``clear()``
* ``sort()``

.. tip::
    Sí es posible aplicar ``sorted()`` o ``reversed()`` sobre una tupla ya que no estamos modificando su valor sino creando un nuevo objeto.

.. seealso::
    La comparación de tuplas funciona exactamente igual que la :ref:`comparación de listas <core/datastructures/lists:comparar listas>`.

************************
Desempaquetado de tuplas
************************

El **desempaquetado** es una característica de las tuplas que nos permite *asignar una tupla a variables independientes*:

.. figure:: img/tuple-unpacking.jpg
    :align: center

    Desempaquetado de tuplas

Veamos un ejemplo con código::

    >>> three_wise_men = ('Melchor', 'Gaspar', 'Baltasar') 

    >>> king1, king2, king3 = three_wise_men

    >>> king1
    'Melchor'
    >>> king2
    'Gaspar'
    >>> king3
    'Baltasar'

Python proporciona la función "built-in" ``divmod()`` que devuelve el cociente y el resto de una división usando una única llamada. Lo interesante (para el caso que nos ocupa) es que se suele utilizar el desempaquetado de tuplas para obtener los valores::

    >>> quotient, remainder = divmod(7, 3)

    >>> quotient
    2
    >>> remainder
    1


Intercambio de valores
======================

A través del desempaquetado de tuplas podemos llevar a cabo *el intercambio de los valores de dos variables* de manera directa:

.. code-block::
    :emphasize-lines: 4

    >>> value1 = 40
    >>> value2 = 20

    >>> value1, value2 = value2, value1

    >>> value1
    20
    >>> value2
    40

.. note:: A priori puede parecer que esto es algo "natural", pero en la gran mayoría de lenguajes de programación no es posible hacer este intercambio de forma "directa" ya que necesitamos recurrir a una tercera variable "auxiliar" como almacén temporal en el paso intermedio de traspaso de valores.

Desempaquetado extendido
========================

No tenemos que ceñirnos a realizar desempaquetado uno a uno. También podemos extenderlo e indicar ciertos "grupos" de elementos mediante el operador ``*``.

Veamos un ejemplo:

.. code-block::
    :emphasize-lines: 3

    >>> ranking = ('G', 'A', 'R', 'Y', 'W')

    >>> head, *body, tail = ranking

    >>> head
    'G'

    >>> body
    ['A', 'R', 'Y']

    >>> tail
    'W'

Desempaquetado genérico
=======================

El desempaquetado de tuplas es extensible a cualquier tipo de datos que sea **iterable**. Veamos algunos ejemplos de ello.

Sobre cadenas de texto::

    >>> oxygen = 'O2'
    >>> first, last = oxygen
    >>> first, last
    ('O', '2')

    >>> text = 'Hello, World!'
    >>> head, *body, tail = text
    >>> head, body, tail
    ('H', ['e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd'], '!')

Sobre listas::

    >>> writer1, writer2, writer3 = ['Virginia Woolf', 'Jane Austen', 'Mary Shelley']
    >>> writer1, writer2, writer3
    ('Virginia Woolf', 'Jane Austen', 'Mary Shelley')

    >>> text = 'Hello, World!'    
    >>> word1, word2 = text.split()
    >>> word1, word2
    ('Hello,', 'World!')

************************
¿Tuplas por comprensión?
************************

Los tipos de datos mutables (*listas, diccionarios y conjuntos*) sí permiten comprensiones pero no así los tipos de datos inmutables como *cadenas de texto* y *tuplas*.

Si intentamos crear una **tupla por comprensión** utilizando paréntesis alrededor de la expresión, vemos que no obtenemos ningún error al ejecutarlo::

    >>> myrange = (number for number in range(1, 6))

Sin embargo no hemos conseguido una tupla por comprensión sino un generador::

    >>> myrange
    <generator object <genexpr> at 0x10b3732e0>

****************
Tuplas vs Listas
****************

Aunque puedan parecer estructuras de datos muy similares, sabemos que las tuplas carecen de ciertas operaciones, especialmente las que tienen que ver con la modificación de sus valores, ya que no son inmutables. Si las listas son más flexibles y potentes, ¿por qué íbamos a necesitar tuplas? Veamos 4 potenciales ventajas del uso de tuplas frente a las listas:

1. Las tuplas ocupan **menos espacio** en memoria.
2. En las tuplas existe **protección** frente a cambios indeseados.
3. Las tuplas se pueden usar como **claves de diccionarios** (son :ref:`"hashables" <core/datastructures/dicts:Objetos "hashables">`).
4. Las `namedtuples`_ son una alternativa sencilla a los objetos.



.. --------------- Footnotes ---------------

.. [#chain-unsplash] Foto original de portada por `engin akyurt`_ en Unsplash.

.. --------------- Hyperlinks ---------------

.. _engin akyurt: https://unsplash.com/@enginakyurt?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
.. _namedtuples: https://docs.python.org/es/3/library/collections.html#collections.namedtuple
