*********
Conjuntos
*********

.. image:: img/duy-pham-Cecb0_8Hx-o-unsplash.jpg

Un **conjunto** en Python se representa por una serie de **valores únicos** y **sin orden establecido**. Lo podríamos ver como un diccionario al que le hemos quitado los valores y nos hemos quedado sólo con las claves. Mantiene muchas similitudes con el `concepto matemático de conjunto`_ [#friends-unsplash]_

Creando conjuntos
=================

Para crear un conjunto basta con separar sus valores por *comas* y rodearlos de llaves ``{}``::

    >>> lottery = {21, 10, 46, 29, 31, 94}

    >>> lottery
    {10, 21, 29, 31, 46, 94}

La excepción la tenemos a la hora de crear un **conjunto vacío**, ya que, siguiendo la lógica de apartados anteriores, deberíamos hacerlo a través de llaves::

    >>> wrong_empty_set = {}

    >>> type(wrong_empty_set)
    dict

.. warning:: Si hacemos esto, lo que obtenemos es un *diccionario vacío*.

La única opción que tenemos es utilizar la función ``set()``::

    >>> empty_set = set()

    >>> empty_set
    set()

    >>> type(empty_set)
    set

Conversión
==========

Para convertir otros tipos de datos en un conjunto podemos usar la función ``set()``::

    >>> set('aplatanada')
    {'a', 'd', 'l', 'n', 'p', 't'}

    >>> set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5])
    {1, 2, 3, 4, 5}

    >>> set(('ADENINA', 'TIMINA', 'TIMINA', 'GUANINA', 'ADENINA', 'CITOSINA'))
    {'ADENINA', 'CITOSINA', 'GUANINA', 'TIMINA'}

    >>> set({'manzana': 'rojo', 'plátano': 'amarillo', 'kiwi': 'verde'})
    {'kiwi', 'manzana', 'plátano'}

.. important:: Como se ha visto en los ejemplos anteriores, ``set()`` se suele utilizar en muchas ocasiones como una forma de **extraer los valores únicos** de otros tipos de datos. En el caso de los diccionarios se extraen las claves, que, por definición, son únicas.

.. note:: El hecho de que en los ejemplos anteriores los elementos de los conjuntos estén ordenados es únicamente un "detalle de implementación" en el que no se puede confiar.

Operaciones con conjuntos
=========================

Obtener un elemento
~~~~~~~~~~~~~~~~~~~

En un conjunto no existe un orden establecido para sus elementos, por lo cual **no podemos acceder a un elemento en concreto**. 

De este hecho se deriva igualmente que *no podemos modificar un elemento existente*, ya que no podemos acceder a él. Python sí nos permite añadir o borrar elementos de un conjunto.

Añadir un elemento
~~~~~~~~~~~~~~~~~~

Para añadir un elemento a un conjunto debemos utilizar la función ``add()``. Como ya hemos indicado, al no importar el orden dentro del conjunto, la inserción no establece a priori la posición dónde se realizará.

A modo de ejemplo, vamos a partir de un conjunto que representa a los cuatro integrantes originales de *The Beatles*. Luego añadiremos a un nuevo componente:  

.. code-block::
    :emphasize-lines: 3

    >>> beatles = set(['Lennon', 'McCartney', 'Harrison', 'Starr'])

    >>> beatles.add('Best')  # Pete Best

    >>> beatles
    {'Best', 'Harrison', 'Lennon', 'McCartney', 'Starr'}

Ejecución **paso a paso** a través de *Python Tutor*:

.. only:: latex

    https://tinyurl.com/9folv2v

.. only:: html

    .. raw:: html

        <iframe width="800" height="320" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=beatles%20%3D%20set%28%5B'Lennon',%20'McCartney',%20'Harrison',%20'Starr'%5D%29%0A%0Abeatles.add%28'Best'%29%20%20%23%20Pete%20Best%0A%0Aprint%28beatles%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

Borrar elementos
~~~~~~~~~~~~~~~~

Para borrar un elemento de un conjunto podemos utilizar la función ``remove()``. Siguiendo con el ejemplo anterior vamos a borrar al último "beatle" añadido::

    >>> beatles
    {'Best', 'Harrison', 'Lennon', 'McCartney', 'Starr'}

    >>> beatles.remove('Best')

    >>> beatles
    {'Harrison', 'Lennon', 'McCartney', 'Starr'}

Longitud de un conjunto
~~~~~~~~~~~~~~~~~~~~~~~

Podemos conocer el número de elementos que tiene un conjunto con la función ``len()``::

    >>> beatles
    {'Harrison', 'Lennon', 'McCartney', 'Starr'}

    >>> len(beatles)
    4

Iterar sobre un conjunto
~~~~~~~~~~~~~~~~~~~~~~~~

Tal y como hemos visto para otros tipos de datos *iterables*, la forma de recorrer los elementos de un conjunto es utilizar la sentencia ``for``::

    >>> for beatle in beatles:
    ...     print(beatle)
    ...
    Harrison
    McCartney
    Starr
    Lennon

.. hint:: Como en el ejemplo anterior, es muy común utilizar una *variable en singular* para recorrer un iterable (en plural). No es una regla fija ni sirve para todos los casos, pero sí suele ser una *buena práctica*.

Pertenencia de elemento
~~~~~~~~~~~~~~~~~~~~~~~

Al igual que con otros tipos de datos, Python nos ofrece el operador ``in`` para determinar si un elemento pertenece a un conjunto::

    >>> beatles
    {'Harrison', 'Lennon', 'McCartney', 'Starr'}

    >>> 'Lennon' in beatles
    True

    >>> 'Fari' in beatles
    False

Teoría de conjuntos
===================

Vamos a partir de dos conjuntos :math:`A=\{1,2\}` y :math:`B=\{2,3\}` para ejemplificar las distintas operaciones que se pueden hacer entre ellos basadas en los `Diagramas de Venn`_ y la `Teoría de Conjuntos <https://es.wikipedia.org/wiki/Teor%C3%ADa_de_conjuntos>`__::

    >>> A = {1, 2}

    >>> B = {2, 3}

.. figure:: img/venn-diagrams.png

   Diagramas de Venn

Intersección
~~~~~~~~~~~~

:math:`A \cap B` -- Elementos que están a la vez en :math:`A` y en :math:`B`::

    >>> A & B
    {2}

    >>> A.intersection(B)
    {2}

Unión
~~~~~

:math:`A \cup B` -- Elementos que están tanto en :math:`A` como en :math:`B`::

    >>> A | B
    {1, 2, 3}

    >>> A.union(B)
    {1, 2, 3}

Diferencia
~~~~~~~~~~

:math:`A - B` -- Elementos que están en :math:`A` y no están en :math:`B`::

    >>> A - B
    {1}

    >>> A.difference(B)
    {1}

Diferencia simétrica
~~~~~~~~~~~~~~~~~~~~

:math:`\overline{A \cap B}` -- Elementos que están en :math:`A` o en :math:`B` pero no en ambos conjuntos::

    >>> A ^ B
    {1, 3}

    >>> A.symmetric_difference(B)
    {1, 3}

.. rubric:: AMPLIAR CONOCIMIENTOS

* `Sets in Python <https://realpython.com/courses/sets-python/>`_



.. --------------- Footnotes ---------------

.. [#friends-unsplash] Foto original de portada por `Duy Pham`_ en Unsplash.

.. --------------- Hyperlinks ---------------

.. _Duy Pham: https://unsplash.com/@miinyuii?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
.. _concepto matemático de conjunto: https://es.wikipedia.org/wiki/Conjunto
.. _Diagramas de Venn: https://es.wikipedia.org/wiki/Diagrama_de_Venn
