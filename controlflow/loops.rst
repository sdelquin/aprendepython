######
Bucles
######

.. image:: img/gary-lopater-UaUaefoUmZ8-unsplash.jpg

Cuando queremos hacer algo más de una vez, necesitamos recurrir a un **bucle**. En esta sección veremos las distintas sentencias en Python que nos permiten repetir un bloque de código. [#wheel-unsplash]_

**********************
La sentencia ``while``
**********************

El mecanismo más sencillo en Python para repetir instrucciones es mediante la sentencia ``while``. El mensaje que podemos interpretar tras esta sentencia es: "Mientras se cumpla la condición haz algo". Veamos un sencillo bucle que muestra por pantalla los números del 1 al 5::

    >>> count = 1

    >>> while count <= 5:
    ...     print(count)
    ...     count += 1
    ...
    1
    2
    3
    4
    5

Ejecución **paso a paso** a través de *Python Tutor*:

.. only:: latex

    https://cutt.ly/dfeqTCZ

.. only:: html

    .. raw:: html

        <iframe width="800" height="330" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=count%20%3D%201%0A%0Awhile%20count%20%3C%3D%205%3A%0A%20%20%20%20print%28count%29%0A%20%20%20%20count%20%2B%3D%201&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

La condición del bucle se comprueba en cada nueva repetición. En este caso chequeamos que la variable ``count`` sea menor o igual que 5. Dentro del cuerpo del bucle estamos incrementando esa variable en 1 unidad.

Romper un bucle while
=====================

Python ofrece la posibilidad de *romper* o finalizar un bucle *antes de que cumpla la condición de parada*. Supongamos un ejemplo en el que estamos buscando el primer número múltiplo de 3 yendo desde 20 hasta 1::

    >>> num = 20

    >>> while num >= 1:
    ...     if num % 3 == 0:
    ...         print(num)
    ...         break
    ...     num -= 1
    ...
    18

Ejecución **paso a paso** a través de *Python Tutor*:

.. only:: latex

    https://cutt.ly/wfrKnHl

.. only:: html

    .. raw:: html

        <iframe width="800" height="360" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=num%20%3D%2020%0A%0Awhile%20num%20%3E%3D%201%3A%0A%20%20%20%20if%20num%20%25%203%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20print%28num%29%0A%20%20%20%20%20%20%20%20break%0A%20%20%20%20num%20-%3D%201&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

Como hemos visto en este ejemplo, ``break`` nos permite finalizar el bucle una vez que hemos encontrado nuestro objetivo: el primer múltiplo de 3. Pero si no lo hubiéramos encontrado, el bucle habría seguido decrementando la variable ``num`` hasta valer 0, y la condición del bucle ``while`` hubiera resultado falsa.

Bucle infinito
==============

Si no establecemos bien la **condición de parada** o bien el valor de alguna variable está fuera de control, es posible que lleguemos a una situación de bucle infinito, del que nunca podamos salir. Veamos un ejemplo de esto::

    >>> num = 1

    >>> while num != 10:
    ...     num += 2
    ...
    ^C---------------------------------------------------------------------------
    KeyboardInterrupt                         Traceback (most recent call last)
    <ipython-input-59-f6cb5d82e006> in <module>
          1 while num != 10:
    ----> 2     num += 2
          3

    KeyboardInterrupt:

El problema que surje es que la variable ``num`` toma los valores ``1, 3, 5, 7, 9, 11, ...`` por lo que nunca se cumple la condición del bucle. Esto hace que repitamos eternamente la instrucción de incremento.

Ejecución **paso a paso** a través de *Python Tutor*:

.. only:: latex

    https://cutt.ly/AfrZroa

.. only:: html

    .. raw:: html

        <iframe width="800" height="250" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=num%20%3D%201%0A%0Awhile%20num%20!%3D%2010%3A%0A%20%20%20%20num%20%2B%3D%202&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

Una posible solución a este error es reescribir la condición de parada en el bucle:

.. code-block::
    :emphasize-lines: 3

    >>> num = 1

    >>> while num < 10:
    ...     num += 2
    ...
       

.. tip:: Para abortar una situación de *bucle infinito* podemos pulsar en el teclado la combinación :kbd:`CTRL-C`. Se puede ver reflejado en el intérprete de Python por ``KeyboardInterrupt``.

.. _for-sentence:

********************
La sentencia ``for``
********************

Python permite recorrer aquellos tipos de datos que sean **iterables**, es decir, que admitan *iterar* [#iterate]_ sobre ellos. Algunos ejemplos de tipos y estructuras de datos que permiten ser iteradas (*recorridas*) son: cadenas de texto, listas, diccionarios, ficheros, etc. La sentencia ``for`` nos permite realizar esta acción.

A continuación un ejemplo en el que vamos a recorrer (iterar) una cadena de texto:

.. code-block::
    :emphasize-lines: 3

    >>> word = 'Python'

    >>> for letter in word:
    ...     print(letter)
    ...
    P
    y
    t
    h
    o
    n

La clave aquí está en darse cuenta que el bucle va tomando, en cada iteración, cada uno de los elementos de la variable que especifiquemos. En este caso concreto ``letter`` va tomando cada una de las letras que existen en ``word``, porque una cadena de texto está formado por elementos que son caracteres.

Ejecución **paso a paso** a través de *Python Tutor*:

.. only:: latex

    https://cutt.ly/Pft6R2e

.. only:: html

    .. raw:: html

        <iframe width="800" height="300" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=word%20%3D%20'Python'%0A%0Afor%20letter%20in%20word%3A%0A%20%20%20%20print%28letter%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

.. note:: La variable que utilizamos en el bucle ``for`` para ir tomando los valores puede tener cualquier nombre. Al fin y al cabo es una variable que definimos según nuestras necesidades. Tener en cuenta que se suele usar un nombre en singular.

Romper un bucle for
===================

Una sentencia break dentro de un ``for`` rompe el bucle, :ref:`igual que veíamos <controlflow/loops:Romper un bucle while>` para los bucles ``while``. Veamos un ejemplo con el código anterior. En este caso vamos a recorrer una cadena de texto y pararemos el bucle cuando encontremos una letra *t* minúscula:

.. code-block::
    :emphasize-lines: 5

    >>> word = 'Python'

    >>> for letter in word:
    ...     if letter == 't':
    ...         break
    ...     print(letter)
    ...
    P
    y

Ejecución **paso a paso** a través de *Python Tutor*:

.. only:: latex

    https://cutt.ly/zfyqkbJ

.. only:: html

    .. raw:: html

        <iframe width="800" height="300" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=word%20%3D%20'Python'%0A%0Afor%20letter%20in%20word%3A%0A%20%20%20%20if%20letter%20%3D%3D%20't'%3A%0A%20%20%20%20%20%20%20%20break%0A%20%20%20%20print%28letter%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

Generar secuencias de números
=============================

La función ``range()`` devuelve un *flujo de números* en el rango especificado, sin necesidad de crear y almacenar previamente una larga estructura de datos. Esto permite generar rangos enormes sin consumir toda la *memoria* del sistema.

El uso de ``range()`` es similar a los :ref:`"slices" <datatypes/strings:Trocear una cadena>`: ``range(start, stop, step)``. Podemos omitir ``start`` y el rango empezaría en 0. El único valor requerido es ``stop`` y el último valor generado será justo el anterior a este. El valor por defecto de ``step`` es 1, pero se puede ir "hacia detrás" con -1.

``range()`` devuelve un *objeto iterable*, así que necesitamos obtener los valores paso a paso con una sentencia ``for ... in`` [#convert-list]_. Veamos diferentes ejemplos de uso:

**Rango:** :math:`[0, 1, 2]`
    ::

        >>> for i in range(0, 3):
        ...     print(i)
        ...
        0
        1
        2

        >>> for i in range(3):
        ...     print(i)
        ...
        0
        1
        2

**Rango:** :math:`[1, 3, 5]`
    ::

        >>> for i in range(1, 6, 2):
        ...     print(i)
        ...
        1
        3
        5

**Rango:** :math:`[2, 1, 0]`
    ::

        >>> for i in range(2, -1, -1):
        ...     print(i)
        ...
        2
        1
        0

Ejecución **paso a paso** a través de *Python Tutor*:

.. only:: latex

    https://cutt.ly/vfywE45

.. only:: html

    .. raw:: html

        <iframe width="800" height="250" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=for%20i%20in%20range%282,%2010%29%3A%0A%20%20%20%20print%28i%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>
    
.. tip:: Se suelen utilizar nombres de variables `i`, `j`, `k` para lo que se viene a denominar **contadores**. Este tipo de variables toman valores numéricos enteros como en los ejemplos anteriores. No conviene generalizar el uso de estas variables a situaciones en las que, claramente, tenemos la posibilidad de asignar un nombre semánticamente más significativo.

***************
Bucles anidados
***************

Como ya vimos en las sentencias condicionales, el *anidamiento* es una técnica en la que incluimos distintos niveles de encapsulamiento de sentencias, unas dentro de otras, con mayor nivel de profundidad. En el caso de los bucles también es posible hacer anidamiento.

Veamos un ejemplo de 2 bucles anidados en el que generamos todas las tablas de multiplicar::

    >>> for i in range(1, 10):
    ...     for j in range(1, 10):
    ...         result = i * j
    ...         print(f'{i} * {j} = {result}')
    ...
    1 x 1 = 1
    1 x 2 = 2
    1 x 3 = 3
    1 x 4 = 4
    1 x 5 = 5
    1 x 6 = 6
    1 x 7 = 7
    1 x 8 = 8
    1 x 9 = 9
    2 x 1 = 2
    2 x 2 = 4
    2 x 3 = 6
    2 x 4 = 8
    2 x 5 = 10
    2 x 6 = 12
    2 x 7 = 14
    2 x 8 = 16
    2 x 9 = 18
    3 x 1 = 3
    3 x 2 = 6
    3 x 3 = 9
    3 x 4 = 12
    3 x 5 = 15
    3 x 6 = 18
    3 x 7 = 21
    3 x 8 = 24
    3 x 9 = 27
    4 x 1 = 4
    4 x 2 = 8
    4 x 3 = 12
    4 x 4 = 16
    4 x 5 = 20
    4 x 6 = 24
    4 x 7 = 28
    4 x 8 = 32
    4 x 9 = 36
    5 x 1 = 5
    5 x 2 = 10
    5 x 3 = 15
    5 x 4 = 20
    5 x 5 = 25
    5 x 6 = 30
    5 x 7 = 35
    5 x 8 = 40
    5 x 9 = 45
    6 x 1 = 6
    6 x 2 = 12
    6 x 3 = 18
    6 x 4 = 24
    6 x 5 = 30
    6 x 6 = 36
    6 x 7 = 42
    6 x 8 = 48
    6 x 9 = 54
    7 x 1 = 7
    7 x 2 = 14
    7 x 3 = 21
    7 x 4 = 28
    7 x 5 = 35
    7 x 6 = 42
    7 x 7 = 49
    7 x 8 = 56
    7 x 9 = 63
    8 x 1 = 8
    8 x 2 = 16
    8 x 3 = 24
    8 x 4 = 32
    8 x 5 = 40
    8 x 6 = 48
    8 x 7 = 56
    8 x 8 = 64
    8 x 9 = 72
    9 x 1 = 9
    9 x 2 = 18
    9 x 3 = 27
    9 x 4 = 36
    9 x 5 = 45
    9 x 6 = 54
    9 x 7 = 63
    9 x 8 = 72
    9 x 9 = 81

Lo que está ocurriendo en este código es que, para cada valor que toma la variable ``i``, la otra variable ``j`` toma todos sus valores. Como resultado tenemos una combinación completa de los valores en el rango especificado.

Ejecución **paso a paso** a través de *Python Tutor*:

.. only:: latex

    https://cutt.ly/vfyeWvj

.. only:: html

    .. raw:: html

        <iframe width="800" height="300" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=for%20i%20in%20range%281,%2010%29%3A%0A%20%20%20%20for%20j%20in%20range%281,%2010%29%3A%0A%20%20%20%20%20%20%20%20result%20%3D%20i%20*%20j%0A%20%20%20%20%20%20%20%20print%28f'%7Bi%7D%20*%20%7Bj%7D%20%3D%20%7Bresult%7D'%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

.. note::
    * Podemos añadir todos los niveles de anidamiento que queramos. Eso sí, hay que tener en cuenta que cada nuevo nivel de anidamiento supone un importante aumento de la `complejidad ciclomática`_ de nuestro código, lo que se traduce en mayores tiempos de ejecución.
    * Los bucles anidados también se pueden aplicar a la sentencia ``while``.

.. admonition:: Ejercicio
    :class: exercise

    Imprima los 100 primeros números de la `sucesión de Fibonacci`_: :math:`0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, \dots` 

.. rubric:: AMPLIAR CONOCIMIENTOS

* `The Python range() Function <https://realpython.com/courses/python-range-function/>`_
* `How to Write Pythonic Loops <https://realpython.com/courses/how-to-write-pythonic-loops/>`_
* `For Loops in Python (Definite Iteration) <https://realpython.com/courses/python-for-loop/>`_
* `Python "while" Loops (Indefinite Iteration) <https://realpython.com/python-while-loop/>`_



.. --------------- Footnotes ---------------

.. [#wheel-unsplash] Foto original de portada por `Gary Lopater`_ en Unsplash.
.. [#iterate] Realizar cierta acción varias veces. En este caso la acción es tomar cada elemento.
.. [#convert-list] O convertir el objeto a una secuencia como una lista.

.. --------------- Hyperlinks ---------------

.. _Gary Lopater: https://unsplash.com/@glopater?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
.. _complejidad ciclomática: https://es.wikipedia.org/wiki/Complejidad_ciclom%C3%A1tica
.. _sucesión de Fibonacci: https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci
