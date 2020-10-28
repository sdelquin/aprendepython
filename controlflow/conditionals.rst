#############
Condicionales
#############

.. image:: img/ali-nafezarefi-62H_swdrc4A-unsplash.jpg

En esta sección veremos la sentencia condicional ``if`` y las distintas variantes que puede asumir, pero antes de eso introduciremos algunas cuestiones generales de *escritura de código*. [#fork-unsplash]_

*********************
Definición de bloques
*********************

A diferencia de otros lenguajes que utilizan llaves para definir los bloques de código, cuando Guido Van Rossum :ref:`creó el lenguaje <introduction/python:Python>` quiso evitar estos caracteres por considerarlos innecesarios. Es por ello que en Python los bloques de código se definen a través de **espacios en blanco, preferiblemente 4**. [#pep8]_ En términos técnicos se habla del **tamaño de indentación**.

.. figure:: img/four-spaces.png

   Python recomienda 4 espacios en blanco para indentar

.. hint:: Esto puede resultar extraño e incómodo a personas que vienen de otros lenguajes de programación pero desaparece rápido y se siente natural a medida que se escribe código.

***********
Comentarios
***********

Un *comentario* es un trozo de texto en tu programa que es ignorado por el intérprete de Python. Se pueden usar para aclarar líneas de código adyacentes, para dejar notas recordatorias o cualquier otro propósito.

Los comentarios se inician con el símbolo almohadilla ``#`` y desde ese punto hasta el final de la línea es parte del comentario:

.. code-block::
    :caption: Comentario de bloque

    # 60 sec/min * 60 min/hr * 24 hr/day
    seconds_per_day = 86400

Los comentarios también pueden aparecer en la misma línea de código, aunque `la guía de estilo de Python <https://www.python.org/dev/peps/pep-0008/#inline-comments>`__ no aconseja usarlos en demasía:

.. code-block::
    :caption: Comentario en línea

    stock = 0   # Liberar productos adicionales

****************
Ancho del código
****************

Los programas suelen ser más legibles cuando las líneas no son excesivamente largas. La longitud máxima de línea recomendada por `la guía de estilo de Python <https://www.python.org/dev/peps/pep-0008/#maximum-line-length>`__ es de **80 caracteres**.

Sin embargo, esto genera una cierta polémica hoy en día, ya que los tamaños de pantalla han aumentado y las resoluciones son mucho mayores que hace años. Así las líneas de más de 80 caracteres se siguen visualizando correctamente. Hay personas que son más estrictas en este límite y otras más flexibles.

En caso de que queramos **romper una línea de código** demasiado larga, tenemos dos opciones: usar la *barra invertida* ``\`` o usar los *paréntesis* ``(...)``. Veamos un ejemplo::


    >>> factorial = 4 * 3 * 2 * 1

    >>> factorial = 4 * \
    ...             3 * \
    ...             2 * \
    ...             1

    >>> factorial = (4 *
    ...              3 *
    ...              2 *
    ...              1)

*******************
La sentencia ``if``
*******************

Las sentencia condicional en Python (al igual que en muchos otros lenguajes de programación) es ``if``. En su escritura debemos añadir una **expresión de comparación** terminando con dos puntos al final de la línea. Veamos un ejemplo::

    >>> temperature = 40

    >>> if temperature > 35:
    ...     print('Aviso por alta temperatura')
    ...
    Aviso por alta temperatura

.. note:: Nótese que en Python no es necesario incluir paréntesis ``(`` y ``)`` al escribir condiciones. Hay veces que es recomendable por claridad o por establecer prioridad.

En el caso anterior se puede ver claramente que la condición se cumple y por tanto se ejecuta la instrucción que tenemos dentro del cuerpo de la condición. Pero podría no ser así. Para controlar ese caso existe la sentencia ``else``. Veamos el mismo ejemplo anterior pero añadiendo esta variante::

    >>> temperature = 20

    >>> if temperature > 35:
    ...     print('Aviso por alta temperatura')
    ... else:
    ...     print('Parámetros normales')
    ...
    Parámetros normales    

Podríamos tener incluso condiciones dentro de condiciones, lo que se viene a llamar técnicamente **condiciones anidadas** [#nesting]_. Veamos un ejemplo ampliando el caso anterior::

    >>> temperature = 28

    >>> if temperature < 20:
    ...     if temperature < 10:
    ...         print('Nivel azul')
    ...     else:
    ...         print('Nivel verde')
    ... else:
    ...     if temperature < 30:
    ...         print('Nivel naranja')
    ...     else:
    ...         print('Nivel rojo')
    ...
    Nivel naranja

Python nos ofrece una mejora en la escritura de condiciones anidadas cuando nos aparecen juntos un ``else`` y un ``if``. Podemos sustituirlos por la sentencia ``elif``:

.. figure:: img/elif.png

   Construcción de la sentencia ``elif``

Apliquemos esta mejora al código del ejemplo anterior:

.. code-block::
    :emphasize-lines: 8

    >>> temperature = 28

    >>> if temperature < 20:
    ...     if temperature < 10:
    ...         print('Nivel azul')
    ...     else:
    ...         print('Nivel verde')
    ... elif temperature < 30:
    ...     print('Nivel naranja')
    ... else:
    ...     print('Nivel rojo')
    ...
    Nivel naranja

Ejecución **paso a paso** a través de *Python Tutor*:

.. only:: latex

    https://cutt.ly/wd58B4t

.. only:: html

    .. raw:: html

        <iframe width="800" height="440" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=temperature%20%3D%2028%0A%0Aif%20temperature%20%3C%2020%3A%0A%20%20%20%20if%20temperature%20%3C%2010%3A%0A%20%20%20%20%20%20%20%20print%28'Nivel%20azul'%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28'Nivel%20verde'%29%0Aelif%20temperature%20%3C%2030%3A%0A%20%20%20%20print%28'Nivel%20naranja'%29%0Aelse%3A%0A%20%20%20%20print%28'Nivel%20rojo'%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

*************************
Operadores de comparación
*************************

Cuando escribimos condiciones debemos incluir alguna expresión de comparación. Para usar estas expresiones es fundamental conocer los operadores que nos ofrece Python:

+-------------------+---------+
|     Operador      | Símbolo |
+===================+=========+
| Igualdad          | ``==``  |
+-------------------+---------+
| Desigualdad       | ``!=``  |
+-------------------+---------+
| Menor que         | ``<``   |
+-------------------+---------+
| Menor o igual que | ``<=``  |
+-------------------+---------+
| Mayor que         | ``>``   |
+-------------------+---------+
| Mayor o igual que | ``>=``  |
+-------------------+---------+

A continuación vamos a ver una serie de ejemplos con expresiones de comparación. Téngase en cuenta que estas expresiones habría que incluirlas dentro de la sentencia condicional en el caso de que quisiéramos tomar una acción concreta::

    >>> value = 7

    >>> value == 5
    False

    >>> value == 7
    True

    >>> 5 < value
    True

    >>> value < 10
    True

Podemos escribir condiciones más complejas usando los **operadores lógicos**:

.. hlist::
    :columns: 3

    * ``and``
    * ``or``
    * ``not``

.. code-block::

    >>> (5 < value) or (value > 10)
    True

    >>> (5 < value) and (not (value > 10))
    True

    >>> (5 > value) and (value < 10)
    True

Python ofrece la posibilidad de ver si un valor está entre dos límites de manera directa. Así, por ejemplo, para descubrir si ``value`` está entre *5* y *10* haríamos::

    >>> 5 < value < 10
    True

.. note::
    1. Una expresión de comparación siempre devuelve un valor *booleano*, es decir ``True`` o ``False``.
    2. El uso de paréntesis, en función del caso, puede aclarar la expresión de comparación.

.. admonition:: Ejercicio
    :class: exercise

    Dada una variable ``year`` con un valor entero, compruebe si dicho año es **bisiesto** o no lo es.

    ℹ️ Un año es bisiesto en el calendario Gregoriano, si es divisible entre 4 y no divisible entre 100, o bien si es divisible entre 400. Puedes hacer la comprobación en `esta lista de años bisiestos <https://kalender-365.de/leap-years.php>`_.

    **Ejemplo**
        * Entrada: ``2008``
        * Salida: ``Es un año bisiesto``

"Booleanos" en condiciones
==========================

Cuando queremos preguntar por la *veracidad* de determinada variable "booleana" en una condición, la primera aproximación que parece razonable es la siguiente:

.. code-block::
    :emphasize-lines: 3

    >>> is_cold = True

    >>> if is_cold == True:
    ...     print('Coge chaqueta')
    ... else:
    ...     print('Usa camiseta')
    ...
    Coge chaqueta

Pero podemos *simplificar* esta condición tal que así:

.. code-block::
    :emphasize-lines: 1

    >>> if is_cold:
    ...     print('Coge chaqueta')
    ... else:
    ...     print('Usa camiseta')
    ...
    Coge chaqueta

Hemos visto una comparación para un valor "booleano" verdadero (``True``). En el caso de que la comparación fuera para un valor falso lo haríamos así:

.. code-block::
    :emphasize-lines: 3

    >>> is_cold = False

    >>> if not is_cold:
    ...     print('Usa camiseta')
    ... else:
    ...     print('Coge chaqueta')
    ...
    Usa camiseta

De hecho, si lo pensamos, estamos reproduciendo bastante bien el *lenguaje natural*:

* Si hace frío, coge chaqueta.
* Si no hace frío, usa camiseta. 

.. admonition:: Ejercicio
    :class: exercise

    Escriba un programa que permita adivinar un personaje de `Marvel`_ en base a las tres preguntas siguientes:

    1. ¿Puede volar?
    2. ¿Es humano?
    3. ¿Tiene máscara?

    .. image:: img/marvel-flowchart.png

    **Ejemplo**
        * Entrada: ``can_fly = True``, ``is_human = True`` y ``has_mask = True``
        * Salida: ``Ironman``
    
    🤔 Es una especie de `Akinator`_ para personajes de Marvel...
       

``None`` es útil
================

|intlev|

``None`` es un valor especial de Python que almacena el **valor nulo** [#none]_. No es lo mismo que ``False``, aunque lo parezca cuando lo evaluamos como booleano::

    >>> thing = None

    >>> if thing:
    ...     print("It's some thing")
    ... else:
    ...     print("It's no thing")
    ...
    It's no thing

Para distinguir ``None`` del valor booleano ``False`` se recomienda el uso del operador ``is``::

    >>> thing = None

    >>> if thing is None:
    ...     print("It's nothing")
    ... else:
    ...     print("It's something")
    ...
    It's nothing

La forma "pitónica" de preguntar si algo **no es nulo** es la siguiente:

.. code-block::
    :emphasize-lines: 3

    >>> value = 99

    >>> if value is not None:
    ...     print(f'{value=}')
    ...
    value=99

**************
Operador morsa
**************

|advlev|

A partir de Python 3.8 se incorpora el `operador morsa`_ [#walrus-operator]_, que usa la siguiente sentencia de asignación: ``name := expression``.

Supongamos un ejemplo en el que computamos el perímetro de una circunferencia, indicando al usuario que debe incrementarlo siempre y cuando no llegue a un mínimo establecido.

**Versión tradicional**

.. code-block::

    >>> radius = 4.25
    ... perimeter = 2 * 3.14 * radius
    ... if perimeter < 100:
    ...     print('Increase radius to reach minimum perimeter')
    ...     print('Actual perimeter: ', perimeter)
    ...
    Increase radius to reach minimum perimeter
    Actual perimeter:  26.69

**Versión con operador morsa**

.. code-block::
    :emphasize-lines: 2

    >>> radius = 4.25
    ... if (perimeter := 2 * 3.14 * radius) < 100:
    ...     print('Increase radius to reach minimum perimeter')
    ...     print('Actual perimeter: ', perimeter)
    ...
    Increase radius to reach minimum perimeter
    Actual perimeter:  26.69

Como hemos comprobado, el operador morsa permite realizar asignaciones dentro de expresiones, lo que, en muchas ocasiones permite tener un código más compacto.


.. rubric:: AMPLIAR CONOCIMIENTOS

* `How to Use the Python or Operator <https://realpython.com/python-or-operator/>`_
* `Conditional Statements in Python (if/elif/else) <https://realpython.com/courses/python-conditional-statements/>`_



.. --------------- Footnotes ---------------

.. [#fork-unsplash] Foto original de portada por `ali nafezarefi`_ en Unsplash.
.. [#pep8] Reglas de indentación definidas en `PEP 8`_
.. [#nesting] El anidamiento (o "nesting") hace referencia a incorporar sentencias unas dentro de otras mediante la inclusión de diversos niveles de profunidad (indentación).
.. [#none] Lo que en otros lenguajes se conoce como ``nil``, ``null``, ``nothing``.
.. [#walrus-operator] Se denomina así porque el operador ``:=`` tiene similitud con los colmillos de una morsa.

.. --------------- Hyperlinks ---------------

.. _ali nafezarefi: https://unsplash.com/@beautyisblinding?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
.. _PEP 8: https://www.python.org/dev/peps/pep-0008/#indentation
.. _operador morsa: https://www.python.org/dev/peps/pep-0572/
.. _Marvel: https://www.marvel.com/
.. _Akinator: https://es.akinator.com/
