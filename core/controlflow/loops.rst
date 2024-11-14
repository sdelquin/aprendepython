######
Bucles
######

.. image:: img/gary-lopater-UaUaefoUmZ8-unsplash.jpg

Cuando queremos hacer algo más de una vez, necesitamos recurrir a un **bucle**. En esta sección veremos las distintas sentencias en Python que nos permiten repetir un bloque de código. [#wheel-unsplash]_

**********************
La sentencia ``while``
**********************

El primer mecanismo que existe en Python para repetir instrucciones es usar la sentencia ``while``. La semántica tras esta sentencia es: "Mientras se cumpla la condición haz algo". 

Veamos un sencillo bucle que repite un saludo mientras así se desee::

    >>> want_greet = 'S'  # importante dar un valor inicial

    >>> while want_greet == 'S':
    ...     print('Hola qué tal!')
    ...     want_greet = input('¿Quiere otro saludo? [S/N] ')
    ... print('Que tenga un buen día')
    Hola qué tal!
    ¿Quiere otro saludo? [S/N] S
    Hola qué tal!
    ¿Quiere otro saludo? [S/N] S
    Hola qué tal!
    ¿Quiere otro saludo? [S/N] N
    Que tenga un buen día

Ejecución **paso a paso** a través de *Python Tutor*:

.. raw:: html

    <iframe width="800" height="310" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=want_greet%20%3D%20'S'%20%20%23%20importante%20dar%20un%20valor%20inicial%0A%0Awhile%20want_greet%20%3D%3D%20'S'%3A%0A%20%20%20%20print%28'Hola%20qu%C3%A9%20tal!'%29%0A%20%20%20%20want_greet%20%3D%20input%28'%C2%BFQuiere%20otro%20saludo%3F%20%5BS/N%5D%20'%29%0Aprint%28'Que%20tenga%20un%20buen%20d%C3%ADa'%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>


La condición del bucle se comprueba en cada nueva repetición. En este caso chequeamos que la variable ``want_greet`` sea igual a ``'S'``. Dentro del cuerpo del bucle estamos mostrando un mensaje y pidiendo la opción al usuario.

Romper un bucle while
=====================

Python ofrece la posibilidad de *romper* o finalizar un bucle *antes de que se cumpla la condición de parada*.

Supongamos que en el ejemplo anterior, establecemos un máximo de 4 saludos:

.. code-block::
    :emphasize-lines: 11

    >>> MAX_GREETS = 4

    >>> num_greets = 0
    >>> want_greet = 'S'

    >>> while want_greet == 'S':
    ...     print('Hola qué tal!')
    ...     num_greets += 1
    ...     if num_greets == MAX_GREETS:
    ...         print('Máximo número de saludos alcanzado')
    ...         break
    ...     want_greet = input('¿Quiere otro saludo? [S/N] ')
    ... print('Que tenga un buen día')
    Hola qué tal!
    ¿Quiere otro saludo? [S/N] S
    Hola qué tal!
    ¿Quiere otro saludo? [S/N] S
    Hola qué tal!
    ¿Quiere otro saludo? [S/N] S
    Hola qué tal!
    Máximo número de saludos alcanzado
    Que tenga un buen día

Ejecución **paso a paso** a través de *Python Tutor*:

.. raw:: html

    <iframe width="800" height="460" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=MAX_GREETS%20%3D%204%0A%0Anum_greets%20%3D%200%0Awant_greet%20%3D%20'S'%0A%0Awhile%20want_greet%20%3D%3D%20'S'%3A%0A%20%20%20%20print%28'Hola%20qu%C3%A9%20tal!'%29%0A%20%20%20%20num_greets%20%2B%3D%201%0A%20%20%20%20if%20num_greets%20%3D%3D%20MAX_GREETS%3A%0A%20%20%20%20%20%20%20%20print%28'M%C3%A1ximo%20n%C3%BAmero%20de%20saludos%20alcanzado'%29%0A%20%20%20%20%20%20%20%20break%0A%20%20%20%20want_greet%20%3D%20input%28'%C2%BFQuiere%20otro%20saludo%3F%20%5BS/N%5D%20'%29%0Aprint%28'Que%20tenga%20un%20buen%20d%C3%ADa'%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

Como hemos visto en este ejemplo, ``break`` nos permite finalizar el bucle una vez que hemos llegado al máximo número de saludos. Pero si no hubiéramos llegado a dicho límite, el bucle habría seguido hasta que el usuario indicara que no quiere más saludos.

Otra forma de resolver este ejercicio sería incorporar una condición al bucle::

    while want_greet == 'S' and num_questions < MAX_GREETS:
        ...

Comprobar la rotura
-------------------

Python nos ofrece la posibilidad de **detectar si el bucle ha acabado de forma ordinaria**, esto es, ha finalizado por no cumplirse la condición establecida. Para ello podemos hacer uso de la sentencia ``else`` como parte del propio bucle. Si el bucle while finaliza normalmente (sin llamada a ``break``) el flujo de control pasa a la sentencia opcional ``else``.

Veamos su comportamiento siguiendo con el ejemplo que venimos trabajando:

.. code-block::
    :emphasize-lines: 13-14

    >>> MAX_GREETS = 4

    >>> num_greets = 0
    >>> want_greet = 'S'

    >>> while want_greet == 'S':
    ...     print('Hola qué tal!')
    ...     num_greets += 1
    ...     if num_greets == MAX_GREETS:
    ...         print('Máximo número de saludos alcanzado')
    ...         break
    ...     want_greet = input('¿Quiere otro saludo? [S/N] ')
    ... else:
    ...     print('Usted no quiere más saludos')
    ... print('Que tenga un buen día')
    Hola qué tal!
    ¿Quiere otro saludo? [S/N] S
    Hola qué tal!
    ¿Quiere otro saludo? [S/N] N
    Usted no quiere más saludos
    Que tenga un buen día

.. important::
    Si hubiéramos agotado el número de saludos NO se habría ejecutado la cláusula ``else`` del bucle ya que habríamos roto el flujo con un ``break``.

.. warning::
    La sentencia ``else`` sólo tiene sentido en aquellos bucles que contienen un ``break``.

Ejecución **paso a paso** a través de *Python Tutor*:

.. raw:: html

    <iframe width="800" height="510" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=MAX_GREETS%20%3D%204%0A%0Anum_greets%20%3D%200%0Awant_greet%20%3D%20'S'%0A%0Awhile%20want_greet%20%3D%3D%20'S'%3A%0A%20%20%20%20print%28'Hola%20qu%C3%A9%20tal!'%29%0A%20%20%20%20num_greets%20%2B%3D%201%0A%20%20%20%20if%20num_greets%20%3D%3D%20MAX_GREETS%3A%0A%20%20%20%20%20%20%20%20print%28'M%C3%A1ximo%20n%C3%BAmero%20de%20saludos%20alcanzado'%29%0A%20%20%20%20%20%20%20%20break%0A%20%20%20%20want_greet%20%3D%20input%28'%C2%BFQuiere%20otro%20saludo%3F%20%5BS/N%5D%20'%29%0Aelse%3A%0A%20%20%20%20print%28'Usted%20no%20quiere%20m%C3%A1s%20saludos'%29%0Aprint%28'Que%20tenga%20un%20buen%20d%C3%ADa'%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

Continuar un bucle
==================

Hay situaciones en las que, en vez de romper un bucle, nos interesa **saltar adelante hacia la siguiente repetición**. Para ello Python nos ofrece la sentencia ``continue`` que hace precisamente eso, descartar el resto del código del bucle y saltar a la siguiente iteración.

Continuamos con el ejemplo anterior y vamos a contar el número de respuestas válidas:

.. code-block::
    :emphasize-lines: 10

    >>> want_greet = 'S'
    >>> valid_options = 0

    >>> while want_greet == 'S':
    ...     print('Hola qué tal!')
    ...     want_greet = input('¿Quiere otro saludo? [S/N] ')
    ...     if want_greet not in 'SN':
    ...         print('No le he entendido pero le saludo')
    ...         want_greet = 'S'
    ...         continue
    ...     valid_options += 1
    ... print(f'{valid_options} respuestas válidas')
    ... print('Que tenga un buen día')
    Hola qué tal!
    ¿Quiere otro saludo? [S/N] S
    Hola qué tal!
    ¿Quiere otro saludo? [S/N] A
    No le he entendido pero le saludo
    Hola qué tal!
    ¿Quiere otro saludo? [S/N] B
    No le he entendido pero le saludo
    Hola qué tal!
    ¿Quiere otro saludo? [S/N] N
    2 respuestas válidas
    Que tenga un buen día

Ejecución **paso a paso** a través de *Python Tutor*:

.. raw:: html

    <iframe width="800" height="460" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=want_greet%20%3D%20'S'%0Avalid_options%20%3D%200%0A%0Awhile%20want_greet%20%3D%3D%20'S'%3A%0A%20%20%20%20print%28'Hola%20qu%C3%A9%20tal!'%29%0A%20%20%20%20want_greet%20%3D%20input%28'%C2%BFQuiere%20otro%20saludo%3F%20%5BS/N%5D%20'%29%0A%20%20%20%20if%20want_greet%20not%20in%20'SN'%3A%0A%20%20%20%20%20%20%20%20print%28'No%20le%20he%20entendido%20pero%20le%20saludo'%29%0A%20%20%20%20%20%20%20%20want_greet%20%3D%20'S'%0A%20%20%20%20%20%20%20%20continue%0A%20%20%20%20valid_options%20%2B%3D%201%0Aprint%28f'%7Bvalid_options%7D%20respuestas%20v%C3%A1lidas'%29%0Aprint%28'Que%20tenga%20un%20buen%20d%C3%ADa'%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

Bucle infinito
==============

Si no establecemos correctamente la **condición de parada** o bien el valor de alguna variable está fuera de control, es posible que lleguemos a una situación de bucle infinito, del que nunca podamos salir. Veamos un ejemplo de esto::

    >>> num = 1

    >>> while num != 10:
    ...     num += 2
    ...
    # CTRL-C
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyboardInterrupt

El problema que surje es que la variable ``num`` toma los valores ``1, 3, 5, 7, 9, 11, ...`` por lo que nunca se cumple la condición de parada del bucle. Esto hace que repitamos "eternamente" la instrucción de incremento.

Ejecución **paso a paso** a través de *Python Tutor*:

.. raw:: html

    <iframe width="800" height="260" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=num%20%3D%201%0A%0Awhile%20num%20!%3D%2010%3A%0A%20%20%20%20num%20%2B%3D%202&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

Una posible solución a este error es reescribir la condición de parada en el bucle:

.. code-block::
    :emphasize-lines: 3

    >>> num = 1

    >>> while num < 10:
    ...     num += 2
    ...
       

.. tip:: Para abortar una situación de *bucle infinito* podemos pulsar en el teclado la combinación :kbd:`CTRL-C`. Se puede ver reflejado en el intérprete de Python por ``KeyboardInterrupt``.

Hay veces que un **supuesto bucle "infinito"** puede ayudarnos a resolver un problema. Imaginemos que queremos escribir un programa que ayude al profesorado a introducir las notas de un examen. Si la nota no está en el intervalo :math:`[0, 10]` mostramos un mensaje de error, en otro caso seguimos pidiendo valores::

    >>> while True:
    ...     mark = float(input('Introduzca nueva nota: '))
    ...     if not(0 <= mark <= 10):
    ...         print('Nota fuera de rango')
    ...         break
    ...     print(mark)
    ...
    Introduzca nueva nota: 5
    5.0
    Introduzca nueva nota: 3
    3.0
    Introduzca nueva nota: 11
    Nota fuera de rango

El código anterior se podría enfocar haciendo uso del :ref:`operador morsa <core/controlflow/conditionals:operador morsa>`::

    >>> while 0 <= (mark := float(input('Introduzca una nueva nota: '))) <= 10:
    ...     print(mark)
    ... print('Nota fuera de rango')
    Introduzca una nueva nota: 5
    5.0
    Introduzca una nueva nota: 3
    3.0
    Introduzca una nueva nota: 11
    Nota fuera de rango

.. admonition:: Ejercicio
    
    :pypas:`m5-limited`

.. _for-sentence:

********************
La sentencia ``for``
********************

Python permite recorrer aquellos tipos de datos que sean **iterables**, es decir, que admitan *iterar* [#iterate]_ sobre ellos. Algunos ejemplos de tipos y estructuras de datos que permiten ser iteradas (*recorridas*) son: cadenas de texto, listas, diccionarios, ficheros, etc. La sentencia ``for`` nos permite realizar esta acción.

A continuación se plantea un ejemplo en el que vamos a recorrer (iterar) una cadena de texto:

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

La clave aquí está en darse cuenta que el bucle va tomando, en cada iteración, cada uno de los elementos de la variable que especifiquemos. En este caso concreto ``letter`` va tomando cada una de las letras que existen en ``word``, porque una cadena de texto está formada por elementos que son caracteres.

Ejecución **paso a paso** a través de *Python Tutor*:

.. raw:: html

    <iframe width="800" height="345" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=word%20%3D%20'Python'%0A%0Afor%20letter%20in%20word%3A%0A%20%20%20%20print%28letter%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

.. important:: La variable que utilizamos en el bucle ``for`` para ir tomando los valores puede tener **cualquier nombre**. Al fin y al cabo es una variable que definimos según nuestras necesidades. Tener en cuenta que se suele usar un nombre en singular.

Romper un bucle for
===================

Una sentencia break dentro de un ``for`` rompe el bucle, :ref:`igual que veíamos <core/controlflow/loops:Romper un bucle while>` para los bucles ``while``. Veamos un ejemplo con el código anterior. En este caso vamos a recorrer una cadena de texto y pararemos el bucle cuando encontremos una letra *t* minúscula:

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

.. raw:: html

    <iframe width="800" height="390" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=word%20%3D%20'Python'%0A%0Afor%20letter%20in%20word%3A%0A%20%20%20%20if%20letter%20%3D%3D%20't'%3A%0A%20%20%20%20%20%20%20%20break%0A%20%20%20%20print%28letter%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

.. tip:: Tanto la :ref:`comprobación de rotura de un bucle <core/controlflow/loops:Comprobar la rotura>` como la :ref:`continuación a la siguiente iteración <core/controlflow/loops:Continuar un bucle>` se llevan a cabo del mismo modo que hemos visto con los bucles de tipo ``while``.

.. admonition:: Ejercicio

    :pypas:`count-vowels`

Secuencias de números
=====================

Es muy habitual hacer uso de secuencias de números en bucles. Python no tiene una instrucción específica para ello. Lo que sí aporta es una función ``range()`` que devuelve un *flujo de números* en el rango especificado. Una de las grandes ventajas es que la "lista" generada no se construye explícitamente, sino que cada valor se genera bajo demanda. Esta técnica mejora el consumo de recursos, especialmente en términos de memoria.

La técnica para la generación de secuencias de números es muy similar a la utilizada en los :ref:`"slices" <core/datatypes/strings:Trocear una cadena>` de cadenas de texto. En este caso disponemos de la función ``range(start, stop, step)``:

- **start**: Es *opcional* y tiene valor por defecto **0**.
- **stop**: es *obligatorio* (siempre se llega a 1 menos que este valor).
- **step**: es *opcional* y tiene valor por defecto **1**.

``range()`` devuelve un *objeto iterable*, así que iremos obteniendo los valores paso a paso con una sentencia ``for ... in`` [#convert-list]_. Veamos diferentes ejemplos de uso:

**Rango:** :math:`[0, 1, 2]`
    ::

        >>> for i in range(0, 3):
        ...     print(i)
        ...
        0
        1
        2

        >>> for i in range(3):  # No hace falta indicar el inicio si es 0
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

.. raw:: html

    <iframe width="800" height="300" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=for%20i%20in%20range%282,%2010%29%3A%0A%20%20%20%20print%28i%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>
    
.. tip:: Se suelen utilizar nombres de variables ``i``, ``j``, ``k`` para lo que se denominan **contadores**. Este tipo de variables toman valores numéricos enteros como en los ejemplos anteriores. No conviene generalizar el uso de estas variables a situaciones en las que, claramente, tenemos la posibilidad de asignar un nombre semánticamente más significativo. Esto viene de tiempos antiguos en FORTRAN donde ``i`` era la primera letra que tenía valor entero por defecto.

.. admonition:: Ejercicio

    :pypas:`prime`

Usando el guión bajo
--------------------

Hay situaciones en las que **no necesitamos usar la variable** que toma valores en el rango, sino que únicamente queremos repetir una acción un número determinado de veces.

Para estos casos se suele recomendar usar el **guión bajo** ``_`` como **nombre de variable**, que da a entender que no estamos usando esta variable de forma explícita::

    >>> for _ in range(10):
    ...     print('Repeat me 10 times!')
    ...
    Repeat me 10 times!
    Repeat me 10 times!
    Repeat me 10 times!
    Repeat me 10 times!
    Repeat me 10 times!
    Repeat me 10 times!
    Repeat me 10 times!
    Repeat me 10 times!
    Repeat me 10 times!
    Repeat me 10 times!

.. admonition:: Ejercicio

    :pypas:`pow`

***************
Bucles anidados
***************

Como ya vimos en las :ref:`sentencias condicionales <if-sentence>`, el *anidamiento* es una técnica por la que incluimos distintos niveles de encapsulamiento de sentencias, unas dentro de otras, con mayor nivel de profundidad. En el caso de los bucles también es posible hacer anidamiento.

.. figure:: img/matrioskas.jpg
    :align: center

    Muñecas rusas Matrioskas para ejemplificar el anidamiento [#matrioskas]_

Veamos un ejemplo de 2 bucles anidados en el que generamos todas las tablas de multiplicar::

    >>> for num_table in range(1, 10):
    ...     for mul_factor in range(1, 10):
    ...         result = num_table * mul_factor 
    ...         print(f'{num_table} * {mul_factor} = {result}')
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

.. raw:: html

    <iframe width="800" height="260" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=for%20num_table%20in%20range%281,%2010%29%3A%0A%20%20%20%20for%20mul_factor%20in%20range%281,%2010%29%3A%0A%20%20%20%20%20%20%20%20result%20%3D%20num_table%20*%20mul_factor%0A%20%20%20%20%20%20%20%20print%28f'%7Bnum_table%7D%20*%20%7Bmul_factor%7D%20%3D%20%7Bresult%7D'%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

.. note::
    * Podemos añadir todos los niveles de anidamiento que queramos. Eso sí, hay que tener en cuenta que cada nuevo nivel de anidamiento supone un importante aumento de la `complejidad ciclomática`_ de nuestro código, lo que se traduce en mayores tiempos de ejecución.
    * Los bucles anidados también se pueden aplicar en la sentencia ``while``.

.. admonition:: Ejercicio
    
    :pypas:`mosaic`

**********
Ejercicios
**********

1. :pypas:`letdig!`
2. :pypas:`m3-sum-limited!`
3. :pypas:`repeat-please!`
4. :pypas:`one-tree!`
5. :pypas:`chess-horse!`
6. :pypas:`domino!`
7. :pypas:`fmin!`
8. :pypas:`ascii-table!`
9. :pypas:`guess-number!`
10. :pypas:`gcd!`
11. :pypas:`hamming!`
12. :pypas:`cartesian!`
13. :pypas:`cumprod-sq!`
14. :pypas:`isalpha!`
15. :pypas:`kpower!`
16. :pypas:`fibonacci!`

----

1. `Summation <https://www.codewars.com/kata/55d24f55d7dd296eb9000030>`_
2. `Find nearest square number <https://www.codewars.com/kata/5a805d8cafa10f8b930005ba>`_
3. `Bin to decimal <https://www.codewars.com/kata/57a5c31ce298a7e6b7000334>`_
4. `altERnaTIng cAsE <https://www.codewars.com/kata/56efc695740d30f963000557>`_
5. `Fake binary <https://www.codewars.com/kata/57eae65a4321032ce000002d>`_
6. `Correct the mistakes of the character recognition software <https://www.codewars.com/kata/577bd026df78c19bca0002c0>`_
7. `String cleaning <https://www.codewars.com/kata/57e1e61ba396b3727c000251>`_
8. `Sum of multiples <https://www.codewars.com/kata/57241e0f440cd279b5000829>`_
9. `ASCII Total <https://www.codewars.com/kata/572b6b2772a38bc1e700007a>`_
10. `Collatz Conjecture (3n+1) <https://www.codewars.com/kata/577a6e90d48e51c55e000217>`_

*********************
Ampliar conocimientos
*********************

* `The Python range() Function <https://realpython.com/courses/python-range-function/>`_
* `How to Write Pythonic Loops <https://realpython.com/courses/how-to-write-pythonic-loops/>`_
* `For Loops in Python (Definite Iteration) <https://realpython.com/courses/python-for-loop/>`_
* `Python "while" Loops (Indefinite Iteration) <https://realpython.com/python-while-loop/>`_



.. --------------- Footnotes ---------------

.. [#wheel-unsplash] Foto original de portada por `Gary Lopater`_ en Unsplash.
.. [#iterate] Realizar cierta acción varias veces. En este caso la acción es tomar cada elemento.
.. [#convert-list] O convertir el objeto a una secuencia como una lista.
.. [#matrioskas] Foto de Matrioskas por `Marina Yufereva`_`` en Escáner Cultural.

.. --------------- Hyperlinks ---------------

.. _Gary Lopater: https://unsplash.com/@glopater?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
.. _complejidad ciclomática: https://es.wikipedia.org/wiki/Complejidad_ciclom%C3%A1tica
.. _sucesión de Fibonacci: https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci
.. _número primo: https://es.wikipedia.org/wiki/N%C3%BAmero_primo
.. _distancia hamming: https://es.wikipedia.org/wiki/Distancia_de_Hamming
.. _producto cartesiano: https://es.wikipedia.org/wiki/Producto_cartesiano
.. _Tabla ASCII: https://www.asciitable.com/
.. _Marina Yufereva: https://www.revista.escaner.cl/node/7197
