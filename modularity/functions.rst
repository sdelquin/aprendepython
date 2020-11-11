#########
Funciones
#########

.. image:: img/nathan-dumlao-6Lh0bRb9LOA-unsplash.jpg

Hasta ahora todo lo que hemos hecho han sido breves fragmentos de código Python. Esto puede ser razonable para pequeñas tareas, pero nadie quiere reescribir los fragmentos de código cada vez. Necesitamos una manera de organizar nuestro código en piezas manejables. [#brewery-unsplash]_ 

El primer paso para la **reutilización de código** es la **función**. Se trata de un trozo de código con nombre y separado del resto. Puede tomar cualquier número y tipo de *parámetros* y devolver cualquier número y tipo de *resultados*. 

Básicamente podemos hacer dos cosas con una función:

- Definirla (con cero o más parámetros).
- Invocarla (y obtener cero o más resultados).

*******************
Definir una función
*******************

Para definir una función en Python debemos usar la palabra reservada ``def`` seguida del nombre de la función con paréntesis rodeando a los parámetros de entrada y finalmente dos puntos ``:``

.. figure:: img/function-definition.png

    Definición de una función en Python
   
.. warning:: Prestar especial atención a los dos puntos ``:`` porque suelen olvidarse en la *definición de la función*.

Hagamos una primera función sencilla que no recibe parámetros::

    def say_hello():
        print('Hello!')

- Nótese la :ref:`indentación <controlflow/conditionals:Definición de bloques>` (sangrado) del *cuerpo* de la función.
- Los *nombres de las funciones* siguen :ref:`las mismas reglas que las variables <datatypes/data:Variables>`.

Invocar una función
===================

Para invocar (o "llamar") a una función basta con escribir su nombre y utilizar paréntesis. En el caso de la función sencilla (vista anteriormente) se haría así:

.. code-block::
    :emphasize-lines: 5

    >>> def say_hello():
    ...     print('Hello!')
    ...

    >>> say_hello()
    Hello!

Como era de esperar, al invocar a la función obtenemos un mensaje por pantalla, fruto de la ejecución del cuerpo de la función.

Retornar un valor
=================

Las funciones pueden retornar (o "devolver") un valor. Veamos un ejemplo muy sencillo::

    >>> def agree():
    ...     return True
    ...

    >>> agree()
    True

Pero no sólo podemos invocar a la función directamente, también la podemos integrar en otras expresiones. Por ejemplo en condicionales::

    >>> if agree():
    ...     print('Trato hecho')
    ... else:
    ...     print('Hasta la próxima')
    ...
    Trato hecho

.. note:: En la sentencia ``return`` podemos incluir variables y expresiones, no únicamente literales.

En aquellos casos en los que una función no tenga un ``return`` explícito, siempre devolverá ``None``.

.. code-block::

    >>> def foo():
    ...     x = 'foo'
    ...

    >>> print(foo())
    None

Si una función no incluye un ``return`` de forma explícita, devolverá ``None`` de forma implícita::

    >>> def empty():
    ...     x = 0
    ...

    >>> print(empty())
    None

.. admonition:: Ejercicio
    :class: exercise

    Escriba una función en Python que reproduzca lo siguiente:

    :math:`f(x, y) = x^2 + y^2`

    **Ejemplo**
        * Entrada: ``3`` y ``4``
        * Salida: ``25``

*********
Veracidad
*********

|intlev|

Ya hemos hablado ligeramente sobre la :ref:`comprobación de veracidad <controlflow/conditionals:"Booleanos" en condiciones>` en Python.

Vamos a crear una función propia para comprobar la veracidad de distintos objetos del lenguaje, y así hacernos una mejor idea de qué cosas **son evaluadas** a *verdadero* y cuáles a *falso*::

    >>> def truthiness(thing):
    ...     if thing:
    ...         print(f'{thing} is True')
    ...     else:
    ...         print(f'{thing} is False')
    ...

Evaluando a ``False``
=====================

Veamos qué "cosas" son evaluadas a ``False`` en Python::

    >>> truthiness(False)
    False is False

    >>> truthiness(None)
    None is False

    >>> truthiness(0)
    0 is False

    >>> truthiness(0.0)
    0.0 is False

    >>> truthiness('')
     is False

    >>> truthiness([])
    [] is False

    >>> truthiness(())
    () is False

    >>> truthiness({})
    {} is False

    >>> truthiness(set())
    set() is False

.. important:: El resto de objetos son evaluados a ``True`` en Python.

Evaluando a ``True``
====================

Veamos ciertos ejemplos que son evaluados a ``True`` en Python::

    >>> truthiness(True)
    True is True

    >>> truthiness(1e-10)
    1e-10 is True

    >>> truthiness([0])
    [0] is True

    >>> truthiness(('',))
    ('',) is True

    >>> truthiness(' ')
      is True
    
    >>> truthiness('🦆')
    🦆 is True

***********************
Parámetros y argumentos
***********************

Vamos a empezar a crear funciones que reciben **parámetros**. En este caso escribiremos una función ``echo()`` que recibe el parámetro ``anything`` y muestra esa variable dos veces separada por un espacio::

    >>> def echo(anything):
    ...     return anything + ' ' + anything
    ...

    >>> echo('Is anybody out there?')
    'Is anybody out there? Is anybody out there?'

.. note:: En este caso, ``'Is anybody out there?'`` es un **argumento** de la función.

Cuando llamamos a una función con *argumentos*, los valores de estos argumentos se copian en los correspondientes *parámetros* dentro de la función:

.. figure:: img/args-params.png

   Parámetros y argumentos de una función

.. tip:: La sentencia ``pass`` permite "no hacer nada". Es una especie de "*placeholder*".

Veamos otra función con algo más de lógica de negocio: [#blogic]_

.. code-block::

    >>> def fruit_detection(color):
    ...     if color == 'red':
    ...         return "It's an apple"
    ...     elif color == 'yellow':
    ...         return "It's a banana"
    ...     elif color == 'green':
    ...         return "It's a kiwi"
    ...     else:
    ...         return f"I don't know about the color {color}"
    ...

    >>> fruit = fruit_detection('green')

    >>> fruit
    "It's a kiwi"

Argumentos posicionales
=======================

Los **argumentos posicionales** son aquellos argumentos que se copian en sus correspondientes parámetros **en orden**. Vamos a mostrar un ejemplo definiendo una función que construye y devuelve un diccionario a partir de los argumentos recibidos::

    >>> def menu(wine, entree, dessert):
    ...     return {'wine': wine, 'entree': entree, 'dessert': dessert}
    ...

Una posible llamada a la función con argumentos posicionales sería la siguiente::

    >>> menu('Flor de Chasna', 'Garbanzas', 'Quesillo')
    {'wine': 'Flor de Chasna', 'entree': 'Garbanzas', 'dessert': 'Quesillo'}

Lo que ha sucedido es un **mapeo** directo entre argumentos y parámetros en el mismo orden que estaban definidos:

+--------------------+-------------+
|     Argumento      |  Parámetro  |
+====================+=============+
| ``Flor de chasna`` | ``wine``    |
+--------------------+-------------+
| ``Garbanzas``      | ``entree``  |
+--------------------+-------------+
| ``Quesillo``       | ``dessert`` |
+--------------------+-------------+

.. note:: Una clara desventaja del uso de argumentos posicionales es que se necesita recordar el significado de cada posición.

Argumentos por nombre
=====================

Para evitar la confusión que pueden producir los argumentos posicionales, es posible especificar argumentos **usando el nombre de los correspondientes parámetros**, incluso en un orden distinto a cómo están definidos en la función::

    >>> menu(entree='Queso asado', dessert='Postre de café', wine='Arautava')
    {'wine': 'Arautava', 'entree': 'Queso asado', 'dessert': 'Postre de café'}

Incluso podemos *mezclar* argumentos posicionales y argumentos por nombre::

    >>> menu('Marba', dessert='Frangollo', entree='Croquetas')
    {'wine': 'Marba', 'entree': 'Croquetas', 'dessert': 'Frangollo'}

.. note:: Si se llama a una función mezclando argumentos posicionales y por nombre, los argumentos posicionales deben ir primero.

.. code-block::

    >>> menu(dessert='Frangollo', entree='Croquetas', 'Marba')
      File "<stdin>", line 1
    SyntaxError: positional argument follows keyword argument

Parámetros por defecto
======================

Es posible especificar **valores por defecto** en los parámetros de una función. El valor por defecto se usará cuando en la llamada a la función no se haya proporcionado el correspondiente argumento.

Supongamos que nos gusta mucho el *Tiramisú*. Podemos especificar en la definición de la función que si no se especifica el postre, éste sea siempre *Tiramisú*::

    >>> def menu(wine, entree, dessert='Tiramisú'):
    ...     return {'wine': wine, 'entree': entree, 'dessert': dessert}
    ...

Llamada a la función sin especificar postre::

    >>> menu('Ignios', 'Ensalada')
    {'wine': 'Ignios', 'entree': 'Ensalada', 'dessert': 'Tiramisú'}

Llamada a la función indicando un postre concreto::

    >>> menu('Tajinaste', 'Revuelto de setas', 'Helado')
    {'wine': 'Tajinaste', 'entree': 'Revuelto de setas', 'dessert': 'Helado'}

.. important:: Los valores por defecto en los parámetros se calculan cuando se **define** la función, no cuando se **ejecuta**.

.. admonition:: Ejercicio
    :class: exercise

    Escriba una función ``factorial`` que reciba un único parámetro ``n`` y devuelva su factorial.

    *El factorial de un número n se define como*:
    
    .. math:: 
        n! = n \cdot (n - 1) \cdot (n - 2) \cdot \ldots \cdot 1
    
    **Ejemplo**
        * Entrada: ``5``
        * Salida: ``120``

Modificando parámetros mutables
-------------------------------

|advlev|

En la siguiente función, uno esperaría que ``result`` tuviera una lista vacía en cada ejecución, pero como estamos modificando ese parámetro dentro de la función, este cambio perdura en el tiempo::

    >>> def buggy(arg, result=[]):
    ...     result.append(arg)
    ...     print(result)
    ...

    >>> buggy('a')
    ['a']

    >>> buggy('b')  # Se esperaría ['b']
    ['a', 'b']

Ejecución **paso a paso** a través de *Python Tutor*:

.. only:: latex

    https://cutt.ly/MgoQGU3

.. only:: html

    .. raw:: html

        <iframe width="800" height="360" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20buggy%28arg,%20result%3D%5B%5D%29%3A%0A%20%20%20%20result.append%28arg%29%0A%20%20%20%20print%28result%29%0A%0Aprint%28buggy%28'a'%29%29%0A%0Aprint%28buggy%28'b'%29%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>


A riesgo de perder el *parámetro por defecto*, una posible solución sería la siguiente::

    >>> def works(arg):
    ...     result = []
    ...     result.append(arg)
    ...     return result
    ...

    >>> works('a')
    ['a']

    >>> works('b')
    ['b']

La forma de arreglar el código anterior utilizando un parámetro con valor por defecto sería tener en cuenta cuál es la primera llamada::

    >>> def nonbuggy(arg, result=None):
    ...     if result is None:
    ...         result = []
    ...     result.append(arg)
    ...     print(result)
    ...

    >>> nonbuggy('a')
    ['a']

    >>> nonbuggy('b')
    ['b']

Empaquetar/Desempaquetar argumentos
===================================

|advlev|

Python nos ofrece la posibilidad de empaquetar y desempaquetar argumentos cuando estamos invocando a una función, tanto para **argumentos posicionales** como para **argumentos por nombre**.

Empaquetar/Desempaquetar argumentos posicionales
------------------------------------------------

Si utilizamos el operador ``*`` delante del nombre de un parámetro posicional, estaremos indicando que los argumentos pasados a la función se empaqueten en una **tupla**::

    >>> def print_args(*args):
    ...     print(f'Positional tuple: {args}')
    ...

    >>> print_args()
    Positional tuple: ()

    >>> print_args(1, 2, 3, 'pescado', 'salado', 'es')
    Positional tuple: (1, 2, 3, 'pescado', 'salado', 'es')

.. note:: El hecho de llamar ``args`` al parámetro es una convención.

También podemos utilizar esta estrategia para establecer en una función una serie de parámetros como *requeridos* y recibir el resto de argumentos como *opcionales y empaquetados*::

    >>> def sum_all(v1, v2, *args):
    ...     total = 0
    ...     for value in (v1, v2) + args:
    ...         total += value
    ...     return total
    ...

    >>> sum_all()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: sum_all() missing 2 required positional arguments: 'v1' and 'v2'

    >>> sum_all(1, 2)
    3

    >>> sum_all(5, 9, 3, 8, 11, 21)
    57

Existe la posibilidad de usar el asterisco ``*`` en la llamada a la función para **desempaquetar** los argumentos posicionales::

    >>> def print_args(*args):
    ...     print(f'Positional tuple: {args}')
    ...

    >>> print_args(4, 3, 7, 9)
    Positional tuple: (4, 3, 7, 9)

    >>> args = (4, 3, 7, 9)

    >>> print_args(args)  # No existe desempaquetado!
    Positional tuple: ((4, 3, 7, 9),)

    >>> print_args(*args)  # Sí existe desempaquetado!
    Positional tuple: (4, 3, 7, 9)

Empaquetar/Desempaquetar argumentos por nombre
----------------------------------------------

Si utilizamos el operador ``**`` delante del nombre de un parámetro por nombre, estaremos indicando que los argumentos pasados a la función se empaqueten en un **diccionario**::

    >>> def print_kwargs(**kwargs):
    ...     print(f'Keyword arguments: {kwargs}')
    ...

    >>> print_kwargs()
    Keyword arguments: {}

    >>> print_kwargs(ram=4, os='ubuntu', cpu=3.4)
    Keyword arguments: {'ram': 4, 'os': 'ubuntu', 'cpu': 3.4}

.. note:: El hecho de llamar ``kwargs`` al parámetro es una convención.

Al igual que veíamos previamente, existe la posibilidad de usar doble asterisco ``**`` en la llamada a la función para **desempaquetar** los argumentos por nombre::

    >>> def print_kwargs(**kwargs):
    ...     print(f'Keyword arguments: {kwargs}')
    ...

    >>> print_kwargs(ram=8, os='debian', cpu=2.7)
    Keyword arguments: {'ram': 8, 'os': 'debian', 'cpu': 2.7}

    >>> kwargs = {'ram': 8, 'os': 'debian', 'cpu': 2.7}

    >>> print_kwargs(kwargs)  # No existe desempaquetado!
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: print_kwargs() takes 0 positional arguments but 1 was given

    >>> print_kwargs(**kwargs)  # Sí existe desempaquetado!
    Keyword arguments: {'ram': 8, 'os': 'debian', 'cpu': 2.7}

Argumentos sólo por nombre
==========================

|advlev|

A partir de Python 3 se ofrece la posibilidad de marcar determinados parámetros de la función como argumentos sólo por nombre. Para ello usaremos el asterisco ``*`` como "separador"::

    >>> def print_data(data, *, start=0, end=100, sep=''):
    ...     ''' "start", "end" y "sep" deben ser pasados por nombre '''
    ...     print(sep.join(data[start:end]))
    ...

    >>> print_data('abcdef')
    abcdef

    >>> print_data('abcdef', sep=':')
    a:b:c:d:e:f

    >>> print_data('abcdef', start=2, sep='*')
    c*d*e*f

    >>> print_data('abcdef', end=4, sep='-')
    a-b-c-d

Hasta aquí no hay nada especialmente diferente, pero si intentamos llamar a la función ``print_data()`` pasando el comienzo y el final como *argumentos posicionales* obtendremos un error::

    >>> print_data('abcdef', 2, 4)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: print_data() takes 1 positional argument but 3 were given

Argumentos mutables e inmutables
================================

|intlev|

Igual que veíamos en la incidencia de :ref:`parámetros por defecto con valores mutables <modularity/functions:Modificando parámetros mutables>`, cuando realizamos modificaciones a los argumentos de una función es importante tener en cuenta si son **mutables** (listas, diccionarios, conjuntos, ...) o **inmutables** (tuplas, enteros, flotantes, cadenas de texto, ...) ya que podríamos obtener efectos colaterales no deseados::

    >>> outside = ['one', 'fine', 'day']

    >>> def mangle(arg):
    ...     arg[1] = 'terrible!'
    ...

    >>> outside
    ['one', 'fine', 'day']

    >>> mangle(outside)

    >>> outside
    ['one', 'terrible!', 'day']

.. warning:: Esto **no es una buena práctica**. O bien documentar que el argumento puede modificarse o bien retornar un nuevo valor.

Funciones como parámetros
=========================

|advlev|

Como ya se ha comentado, en Python "todo es un objeto", y también ocurre con las funciones. Podemos asignar una función a una variable, podemos usarlas como argumentos de otras funciones y como valor de retorno. Esto permite una gran flexibilidad y aporta nuevas posibilidades al lenguaje.

Veamos un primer ejemplo en el que pasamos una función como argumento::

    >>> def answer():
    ...     print(42)
    ...

    >>> answer()
    42

    >>> def run_something(func):
    ...     func()
    ...

    >>> type(answer)
    function

    >>> run_something(answer)  # función "answer" como parámetro
    42

Veamos un segundo ejemplo en el que pasamos, no sólo una función como argumento, sino los valores con los que debe operar::

    >>> def add_args(arg1, arg2):
    ...     print(arg1 + arg2)
    ...

    >>> def run_something_with_args(func, arg1, arg2):
    ...     func(arg1, arg2)
    ...

    >>> type(add_args)
    function

    >>> run_something_with_args(add_args, 5, 9)
    14

*************
Documentación
*************

Ya hemos visto que en Python podemos incluir :ref:`comentarios <controlflow/conditionals:Comentarios>` para explicar mejor determinadas zonas de nuestro código.

Del mismo modo podemos (y en muchos casos **debemos**) adjuntar **documentación** a la definición de una función incluyendo una cadena de texto (**docstring**) al comienzo de su cuerpo::

    >>> def echo(anything):
    ...     'echo returns its input argument'
    ...     return anything
    ...

La forma más ortodoxa de escribir un ``docstring`` es utilizando *triples comillas*::

    >>> def print_if_true(thing, check):
    ...     '''
    ...     Prints the first argument if a second argument is true.
    ...     The operation is:
    ...         1. Check whether the *second* argument is true.
    ...         2. If it is, print the *first* argument.
    ...     '''
    ...     if check:
    ...         print(thing)

Para ver el ``docstring`` de una función, basta con utilizar ``help``::

    >>> help(print_if_true)

    Help on function print_if_true in module __main__:

    print_if_true(thing, check)
        Prints the first argument if a second argument is true.
        The operation is:
            1. Check whether the *second* argument is true.
            2. If it is, print the *first* argument.

.. note:: Si queremos ver el ``docstring`` de una función en "crudo" (sin formatear), podemos usar ``print_if_true.__doc__``.

Explicación de parámetros
=========================

Como ya se ha visto es posible documentar una función utilizando un ``docstring``. Pero la redacción y el formato de esta cadena de texto puede ser muy variada. Existen distintas distintas formas de documentar una función (u otros objetos) [#docstring-formats]_ pero vamos a centrarnos en el modelo **NumPy/SciPy**. 

Este modelo se basa en:

* Una primera línea de **descripción de la función**.
* A continuación especificamos las características de los **parámetros** (incluyendo sus tipos) usando el encabezado ``Parameters``.
* Por último, si la función **retorna un valor**, lo indicamos con el encabezado ``Returns``.

Veamos un ejemplo::

    >>> def substract(value1, value2, vabs=False):
    ...     '''Substract two values with choice of absolute value
    ...
    ...     Parameters
    ...     ----------
    ...     value1 : int
    ...         First value in substraction
    ...     value2 : int
    ...         Second value in substraction
    ...     vabs : bool
    ...         Indicates if absolute value is performed over the substraction
    ...
    ...     Returns
    ...     -------
    ...     int
    ...         Substraction of input values
    ...     '''
    ...     result = value1 - value2
    ...     if vabs:
    ...         result = abs(result)
    ...     return result
    ...

    >>> substract(3, 5)
    -2

    >>> substract(3, 5, True)
    2

Anotación de tipos
==================

|intlev|

Las anotaciones de tipos [#type-hints]_ se introdujeron en Python 3.5 y permiten indicar tipos para los parámetros de una función así como su valor de retorno (aunque también funcionan en creación de variables).

Veamos un ejemplo en el que creamos una función para dividir una cadena de texto por la posición especificada en el parámetro::

    >>> def ssplit(text: str, split_pos: int) -> tuple:
    ...     return text[:split_pos], text[split_pos:]
    ...

    >>> ssplit('Always remember us this way', 15)
    ('Always remember', ' us this way')

Como se puede observar, vamos añadiendo los tipos después de cada parámetro utilizando ``:`` como separador. En el caso del valor de retorno usamos ``->``

Quizás la siguiente ejecución pueda sorprender::

    >>> ssplit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
    ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])

Efectivamente como habrás visto, **no hemos obtenido ningún error**, a pesar de que estamos pasando como primer argumento una lista en vez de una cadena de texto. Esto ocurre porque lo que hemos definido es una anotación de tipo, no una declaración de tipo. Existen herramientas como `mypy`_ que sí se encargan de chequear estas situaciones.

Valores por defecto
-------------------

Al igual que ocurre en la definición ordinaria de funciones, cuando usamos anotaciones de tipos también podemos indicar un valor por defecto para los parámetros.

Veamos la forma de hacerlo continuando con el ejemplo anterior::

    >>> def ssplit(text: str, split_pos: int = -1) -> tuple:
    ...     if split_pos == -1:
    ...         split_pos = len(text) // 2
    ...     return text[:split_pos], text[split_pos:]
    ...

    >>> ssplit('Always remember us this way')
    ('Always rememb', 'er us this way')

Simplemente añadimos el valor por defecto después de indicar el tipo.

.. note:: Las **anotaciones de tipos** son una herramienta muy potente y que, usada de forma adecuada, permite complementar la documentación de nuestro código y aclarar ciertos aspectos, que a priori, pudieran parecer confusos. Su aplicación estará en función de la necesidad detectada por parte del equipo de desarrollo.

******************
Tipos de funciones
******************

|advlev|

Funciones interiores
====================

Está permitido definir una función dentro de otra función::

    >>> def outer(a, b):
    ...     def inner(c, d):
    ...         return c + d
    ...     return inner(a, b)
    ...

    >>> outer(4, 7)
    11

Clausuras
=========

Una **clausura** (del término inglés "*closure*") establece el uso de una :ref:`función interior <modularity/functions:Funciones interiores>` que se genera dinámicamente y recuerda los valores de las variables que fueron creadas fuera de la función::

    >>> def make_multiplier_of(n):
    ...     def multiplier(x):
    ...         return x * n
    ...     return multiplier
    ...

    >>> m3 = make_multiplier_of(3)

    >>> m5 = make_multiplier_of(5)

    >>> type(m3)
    function

    >>> m3(7)  # 7 * 3
    21

    >>> type(m5)
    function

    >>> m5(8)  # 8 * 5
    40

.. note:: En una clausura retornamos una función, no una llamada a la función.

Funciones anónimas "lambda"
===========================

Una **función "lambda"** es una función **anómina** que se expresa en **una única sentencia**. Se puede ver como alternativa a pequeñas funciones ordinarias.

Veamos un ejemplo. En primer lugar crearemos dos funciones auxiliares que nos permitirán luego refactorizar a una función "lambda"::

    >>> def edit_story(words, func):
    ...     ''' Apply "func" to every word in "words" '''
    ...     for word in words:
    ...         print(func(word))
    ...

    >>> def emphasize(word):
    ...     return word.capitalize() + '!'
    ...

    >>> words = ['look', 'jump', 'run', 'shout']

    >>> edit_story(words, emphasize)
    Look!
    Jump!
    Run!
    Shout!

Podemos observar que la función ``emphasize()`` es muy breve. Se trata de una buena candidata para ser *anonimizada* mediante una *función "lambda"*::

    >>> edit_story(words, lambda word: word.capitalize() + '!')
    Look!
    Jump!
    Run!
    Shout!

.. note:: Una función "lambda" tiene cero o más argumentos separados por comas, seguido de dos puntos ``:`` y luego el cuerpo de la función. No se usan paréntesis ni se usa la palabra reservada ``def``.

Veamos otro ejemplo en el que mostramos una tabla con el resultado de aplicar el "and" lógico mediante una función "lambda" que ahora recibe dos parámetros::

    >>> logic_and = lambda x, y: x & y

    >>> for i in range(2):
    ...     for j in range(2):
    ...         print(f'{i} & {j} = {logic_and(i, j)}')
    ...
    0 & 0 = 0
    0 & 1 = 0
    1 & 0 = 0
    1 & 1 = 1

Enfoque funcional
=================

Como se comentó en la :ref:`introducción <introduction/python:Características del lenguaje>`, Python es un lenguaje de programación multiparadigma. Uno de los paradigmas menos explotados en este lenguaje es la **programación funcional** [#functional-programming]_.

Python nos ofrece 3 funciones que encajan verdaderamente bien en este enfoque: ``map()``, ``filter()`` y ``reduce()``.

.. figure:: img/map-filter-reduce.png

    Rutinas muy enfocadas a programación funcional

``map()``
---------

Esta función **aplica otra función** sobre cada elemento de un iterable. Supongamos que queremos aplicar la siguiente función:

.. math::

    f(x) = \frac{x^2}{2} \hspace{20px} \forall x \in [1, 10]

.. code-block::

    >>> def f(x):
    ...     return x**2 / 2
    ...

    >>> data = range(1, 11)

    >>> map_gen = map(f, data)

    >>> type(map_gen)
    map

    >>> list(map_gen)
    [0.5, 2.0, 4.5, 8.0, 12.5, 18.0, 24.5, 32.0, 40.5, 50.0]

Aplicando una :ref:`función anónima "lambda" <modularity/functions:Funciones anónimas "lambda">`...

    >>> list(map(lambda x: x**2 / 2, data))
    [0.5, 2.0, 4.5, 8.0, 12.5, 18.0, 24.5, 32.0, 40.5, 50.0]

.. important:: ``map()`` devuelve un **generador**, no directamente una lista.

``filter()``
------------

Esta función **selecciona** aquellos elementos de un iterable que cumplan una determinada condición. Supongamos que queremos seleccionar sólo aquellos números impares dentro de un rango::

    >>> def odd_number(x):
    ...     return x % 2 == 1
    ...

    >>> data = range(1, 21)

    >>> filter_gen = filter(odd_number, data)

    >>> type(filter_gen)
    filter

    >>> list(filter_gen)
    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

Aplicando una :ref:`función anónima "lambda" <modularity/functions:Funciones anónimas "lambda">`...

    >>> list(filter(lambda x: x % 2 == 1, data))
    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

.. important:: ``filter()`` devuelve un **generador**, no directamente una lista.

``reduce()``
------------

Para poder usar esta función debemos usar el módulo ``functools``. Nos permite aplicar una función dada sobre todos los elementos de un iterable de manera acumulativa. O dicho en otras palabras, nos permite **reducir** una función sobre un conjunto de valores. Supongamos que queremos realizar el producto de una serie de valores aplicando este enfoque::

    >>> from functools import reduce

    >>> def mult_values(a, b):
    ...     return a * b
    ...

    >>> data = range(1, 6)

    >>> reduce(mult_values, data)  # ((((1 * 2) * 3) * 4) * 5)
    120

Aplicando una :ref:`función anónima "lambda" <modularity/functions:Funciones anónimas "lambda">`...

    >>> reduce(lambda x, y: x * y, data)
    120

.. hint:: Por cuestiones de legibilidad del código, se suelen preferir las **listas por comprensión** a funciones como ``map()`` o ``filter()``, aunque cada problema tiene sus propias características y sus soluciones más adecuadas.

Generadores
===========

Un **generador** es un objeto que premite crear secuencias. La gran ventaja de usar generadores es que podemos iterar sobre enormes secuencias sin necesidad de crearlas ni de almacenarlas completamente en memoria de una sola vez.

Los generadores suelen ser la fuente de datos de los **iteradores**. De hecho ya hemos usado uno de ellos, ``range()``, para generar secuencias de valores enteros::

    >>> sum(range(1, 101))
    5050

.. note:: Cada vez que iteramos a través de un generador se lleva un seguimiento del último valor generado para poder generar el siguiente (si procede). Esto es diferente de una función ordinaria, que no tiene "memoria" de sus llamadas anteriores y siempre empieza desde la primera línea con el mismo estado.

Funciones generadoras
---------------------

Si necesitamos crear una secuencia *potencialmente larga* podemos escribir una **función generadora**. Se trata de una función ordinaria pero que retorna su valor con ``yield`` en vez de con ``return``.

Veamos un ejemplo en el que escribimos nuestra propia versión de ``range()``::

    >>> def my_range(first=0, last=10, step=1):
    ...     number = first
    ...     while number < last:
    ...         yield number
    ...         number += step
    ...

    >>> type(my_range)
    function

    >>> ranger = my_range(1, 5)  # devuelve un generador

    >>> type(ranger)
    generator

Una vez creado el generador, ya podemos iterar sobre él::

    >>> for i in ranger:
    ...     print(i)
    ...
    1
    2
    3
    4

.. important:: Un detalle muy importante sobre los generadores es que "se agotan". Es decir, una vez que ya hemos consumido todos sus elementos ya no obtendremos nuevos valores.

Expresiones generadoras
-----------------------

Una **expresión generadora** es sintácticamente muy similar a una *lista por comprensión*, pero utilizamos **paréntesis** en vez de corchetes. Se podría ver como una versión acortada de una función generadora.

Veamos un ejemplo en el que crearemos una expresión generadora para producir los números pares entre el 0 y el 10::

    >>> even_gen = (i for i in range(11) if i % 2 == 0)

    >>> type(even_gen)
    generator

    >>> for even_number in even_gen:
    ...     print(even_number)
    ...
    0
    2
    4
    6
    8
    10

.. admonition:: Ejercicio
    :class: exercise

    Escriba una **función generadora** que devuelva los 100 primeros números enteros elevados al cuadrado.

Decoradores
===========

Hay veces que necesitamos modificar una función existente sin cambiar su código fuente. Un ejemplo muy común es añadir algunas sentencias de depuración para ver qué argumentos estamos pasando.

Un **decorador** es una *función* que toma como entrada una función y devuelve otra función. Se podría ver como un caso particular de :ref:`clausura <modularity/functions:Clausuras>`.

Veamos un ejemplo en el que documentamos la ejecución de una función::

    >>> def document_it(func):
    ...     def new_function(*args, **kwargs):
    ...         print('Running function:', func.__name__)
    ...         print('Positional arguments:', args)
    ...         print('Keyword arguments:', kwargs)
    ...         result = func(*args, **kwargs)
    ...         print('Result', result)
    ...         return result
    ...     return new_function
    ...

Ahora vamos a definir una función ordinaria (que usaremos más adelante)::

    >>> def add_ints(a, b):
    ...     return a + b
    ...

    >>> add_ints(3, 5)
    8

Ahora aplicaremos el decorador definido previamente ``document_it()`` sobre la función ordinaria ``add_ints()``. Se dice que que ``document_it()`` es la **función decoradora** y que ``add_ints()`` es la **función decorada**. De esta forma obtendremos información extra sobre la ejecución, y que además es aplicable a cualquier otra función ordinaria::

    >>> documented_add_ints = document_it(add_ints)

    >>> type(documented_add_ints)
    function

    >>> documented_add_ints(3, 5)
    Running function: add_ints
    Positional arguments: (3, 5)
    Keyword arguments: {}
    Result 8
    8

    >>> documented_add_ints(a=7, b=2)
    Running function: add_ints
    Positional arguments: ()
    Keyword arguments: {'a': 7, 'b': 2}
    Result 9
    9

Usando ``@`` para decorar
-------------------------

Como una alternativa a la aplicación manual de un decorador podemos usar el operador ``@`` (seguido del nombre del decorador) antes de la definición de la función que queremos decorar::

    >>> @document_it
    ... def add_ints(a, b):
    ...     return a + b
    ...

    >>> add_ints(8, 15)
    Running function: add_ints
    Positional arguments: (8, 15)
    Keyword arguments: {}
    Result 23
    23

    >>> add_ints(a=3, b=6)
    Running function: add_ints
    Positional arguments: ()
    Keyword arguments: {'a': 3, 'b': 6}
    Result 9
    9

Podemos aplicar más de un decorador a cada función. Para ejemplificarlo vamos primero a definir un nuevo decorador que eleva al cuadrado el resultado de la función decorada::

    >>> def square_it(func):
    ...     def new_function(*args, **kwargs):
    ...         result = func(*args, **kwargs)
    ...         return result * result
    ...     return new_function
    ...

Ahora aplicaremos los dos decoradores que hemos escrito::

    >>> @document_it
    ... @square_it
    ... def add_ints(a, b):
    ...     return a + b
    ...

    >>> add_ints(3, 5)
    Running function: new_function
    Positional arguments: (3, 5)
    Keyword arguments: {}
    Result 64
    64

.. important:: Cuando tenemos varios decoradores aplicados a una función, el orden de ejecución empieza por aquel decorador más "cercano" a la definición de la función.

.. admonition:: Ejercicio
    :class: exercise

    Escriba un decorador que convierta a su valor absoluto los dos primeros parámetros de la función que decora y devuelva el resultado de aplicar dicha función a sus dos argumentos.

    A continuación probar el decorador con una función que devuelva el producto de dos valores, jugando con números negativos y positivos.

    **Ejemplo**
        * Entrada: ``-3`` y ``7``
        * Salida: ``21``

Funciones recursivas
====================

La **recursividad** es el mecanismo por el cual una función se llama a sí misma::

    >>> def call_me():
    ...     return call_me()
    ...

    >>> call_me()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 2, in call_me
      File "<stdin>", line 2, in call_me
      File "<stdin>", line 2, in call_me
      [Previous line repeated 996 more times]
    RecursionError: maximum recursion depth exceeded

.. warning:: Podemos osbservar que existe un número máximo de llamadas recursivas. Python controla esta situación por nosotros, ya que, de no ser así, podríamos llegar a consumir los recursos del sistema.

Veamos ahora un ejemplo más real en el que computar el enésimo término de la `Sucesión de Fibonacci`_ utilizando una función recursiva::

    >>> def fibonacci(n):
    ...     if n == 0:
    ...         return 0
    ...     if n == 1:
    ...         return 1
    ...     return fibonacci(n - 1) + fibonacci(n - 2)
    ...

    >>> fibonacci(10)
    55

    >>> fibonacci(20)
    6765

Función generadora recursiva
----------------------------

Si tratamos de extender el ejemplo anterior de Fibonacci para obtener todos los términos de la sucesión hasta un límite, pero con la filosofía recursiva, podríamos plantear el uso de una :ref:`función generadora <modularity/functions:Funciones generadoras>`::

    >>> def fibonacci():
    ...     def _fibonacci(n):
    ...         if n == 0:
    ...             return 0
    ...         if n == 1:
    ...             return 1
    ...         return _fibonacci(n - 1) + _fibonacci(n - 2)
    ...
    ...     n = 0
    ...     while True:
    ...         yield _fibonacci(n)
    ...         n += 1
    ...

    >>> fib = fibonacci()

    >>> type(fib)
    generator

    >>> for _ in range(10):
    ...     print(next(fib))
    ...
    0
    1
    1
    2
    3
    5
    8
    13
    21
    34

.. admonition:: Ejercicio
    :class: exercise

    Escriba una función recursiva que calcule el factorial de un número:

    .. math::

        n! = n \cdot (n - 1) \cdot (n - 2) \cdot \ldots \cdot 1
    
    **Ejemplo**
        * Entrada: ``5``
        * Salida: ``120``

*******************
Espacios de nombres
*******************

Un nombre puede hacer referencia a múltiples cosas, dependiendo de dónde lo estemos usando. Los programas en Python tienen diferentes **espacios de nombres**, secciones donde un nombre particular es único e independiente del mismo nombre en otros espacios de nombres.

Cada función define su propio espacio de nombres. Si se define una variable ``x`` en el programa principal y otra variable ``x`` dentro de una función, hacen referencia a cosas diferentes. Dicho esto, también es posible (*aunque desaconsejado*) acceder al espacio de nombres global dentro de las funciones.

En el siguiente ejemplo se define una variable global (*primer nivel*) y luego mostramos su valor directamente y mediante una función::

    >>> animal = 'tiger'

    >>> def print_global():
    ...     print('inside print_global:', animal)
    ...

    >>> print('at the top level:', animal)
    at the top level: tiger

    >>> print_global()
    inside print_global: tiger

Ejecución **paso a paso** a través de *Python Tutor*:

.. only:: latex

    https://cutt.ly/3fMI8de

.. only:: html

    .. raw:: html

        <iframe width="800" height="420" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=animal%20%3D%20'tiger'%0A%0Adef%20print_global%28%29%3A%0A%20%20%20%20print%28'inside%20print_global%3A',%20animal%29%0A%0A%0Aprint%28'at%20the%20top%20level%3A',%20animal%29%0A%0A%0Aprint_global%28%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

Sin embargo, si creamos una variable dentro de la función que también tenga el nombre ``animal``, realmente estaremos creando una nueva variable distinta de la global::

    >>> animal = 'tiger'

    >>> def change_local():
    ...     animal = 'panther'
    ...     print('inside change_local:', animal)
    ...

    >>> print('at the top level:', animal)
    at the top level: tiger

    >>> change_local()
    inside change_local: panther

Ejecución **paso a paso** a través de *Python Tutor*:

.. only:: latex

    https://cutt.ly/ifMOeYf

.. only:: html

    .. raw:: html

        <iframe width="800" height="440" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=animal%20%3D%20'tiger'%0A%0Adef%20change_local%28%29%3A%0A%20%20%20%20animal%20%3D%20'panther'%0A%20%20%20%20print%28'inside%20change_local%3A',%20animal%29%0A%0A%0Aprint%28'at%20the%20top%20level%3A',%20animal%29%0A%0A%0Achange_local%28%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

Modificación local de variables globales
========================================

|intlev|

Si dentro de una función, accedemos al valor de la variable global y luego la modificamos, obtendremos un **error**:

.. code-block::
    :emphasize-lines: 4, 5
    :linenos:

    >>> animal = 'tiger'

    >>> def change_and_print_global():
    ...     print('inside change_and_print_global:', animal)
    ...     animal = 'panther'
    ...     print('after the change:', animal)
    ...

    >>> print('at the top level:', animal)
    at the top level: tiger

    >>> change_and_print_global()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 2, in change_and_print_global
    UnboundLocalError: local variable 'animal' referenced before assignment

**Línea 5**
    Aquí la variable ``animal`` ya no es global, porque se ha definido una variable **local** en la siguiente línea. Es por ello que se genera un error por acceder a una variable aún no definida.
**Línea 6**
    Creación de la variable **local** ``animal``.

Acceso con ``global``
=====================

|intlev|

Python nos ofrece la posibilidad de acceder (y modificar) las variables globales dentro de una función. Para ello necesitamos ser **explícitos** y usar la palabra clave ``global`` antes de la variable:

.. code-block::
    :emphasize-lines: 4, 5
    :linenos:

    >>> animal = 'tiger'

    >>> def change_and_print_global():
    ...     global animal
    ...     animal = 'panther'
    ...     print('inside change_and_print_global:', animal)
    ...

    >>> print('at the top level:', animal)
    at the top level: tiger

    >>> change_and_print_global()
    inside change_and_print_global: panther

    >>> print('at the top level:', animal)
    at the top level: panther

**Línea 4**
    Especificamos que el acceso es a la variable global ``animal``.
**Línea 5**
    Modificación de la variable global ``animal``.
**Línea 16**
    Vemos que la variable global ``animal`` ha cambiado realmente su valor.

.. warning:: No se recomienda el uso de variables globales ya que puede dar lugar a confusiones en los accesos.

Introspección de funciones
==========================

|advlev|

Contenido de los espacios de nombres
------------------------------------

Python proporciona dos funciones para acceder al contenido de los espacios de nombres:

``locals()``
    Devuelve un diccionario con los contenidos del **espacio de nombres local**.
``globals()``
    Devuelve un diccionario con los contenidos del **espacio de nombres global**.

.. code-block::
    :emphasize-lines: 5, 14

    >>> animal = 'tiger'

    >>> def change_local():
    ...     animal = 'panther'
    ...     print(f'locals: {locals()}')
    ...

    >>> animal
    'tiger'

    >>> change_local()
    locals: {'animal': 'panther'}

    >>> globals()
    {'__name__': '__main__',
     '__doc__': 'Automatically created module for IPython interactive environment',
     '__package__': None,
     '__loader__': None,
     '__spec__': None,
     '__builtin__': <module 'builtins' (built-in)>,
     '__builtins__': <module 'builtins' (built-in)>,
     '_ih': ['',
      "animal = 'tiger'",
      "def change_local():\n    animal = 'panther'\n    print(f'locals: {locals()}')\n    ",
      'animal',
      'change_local()',
      'globals()'],
     '_oh': {3: 'tiger'},
     '_dh': ['/Users/sdelquin'],
     'In': ['',
      "animal = 'tiger'",
      "def change_local():\n    animal = 'panther'\n    print(f'locals: {locals()}')\n    ",
      'animal',
      'change_local()',
      'globals()'],
     'Out': {3: 'tiger'},
     'get_ipython': <bound method InteractiveShell.get_ipython of <IPython.terminal.interactiveshell.TerminalInteractiveShell object at 0x106a6c2e0>>,
     'exit': <IPython.core.autocall.ExitAutocall at 0x106ac1100>,
     'quit': <IPython.core.autocall.ExitAutocall at 0x106ac1100>,
     '_': 'tiger',
     '__': '',
     '___': '',
     'Prompts': IPython.terminal.prompts.Prompts,
     'Token': Token,
     'MyPrompt': __main__.MyPrompt,
     'ip': <IPython.terminal.interactiveshell.TerminalInteractiveShell at 0x106a6c2e0>,
     '_i': 'change_local()',
     '_ii': 'animal',
     '_iii': "def change_local():\n    animal = 'panther'\n    print(f'locals: {locals()}')\n    ",
     '_i1': "animal = 'tiger'",
     'animal': 'tiger',
     '_i2': "def change_local():\n    animal = 'panther'\n    print(f'locals: {locals()}')\n    ",
     'change_local': <function __main__.change_local()>,
     '_i3': 'animal',
     '_3': 'tiger',
     '_i4': 'change_local()',
     '_i5': 'globals()'}

Usos de doble subguión ``__``
-----------------------------

Los nombres que comienzan y terminan con dos subguiones ``__`` están reservados para uso interno de Python, así que no se deberían utilizar en código propio. Estos nombres se conocen como **"dunder"** que proviene de "double-underscore".

Veamos un ejemplo en el que se muestra el nombre de una función y su documentación::

    >>> def amazing():
    ...     '''This is the amazing function.
    ...     Want to see it again?'''
    ...     print('This function is named:', amazing.__name__)
    ...     print('And its docstring is:', amazing.__doc__)
    ...

    >>> amazing()
    This function is named: amazing
    And its docstring is: This is the amazing function.
        Want to see it again?

.. note:: Existen multitud de variables/funciones "dunder" que se pueden consultar en la sección `Modelo de datos`_ de la documentación oficial de Python.

.. rubric:: AMPLIAR CONOCIMIENTOS

- `Comparing Python Objects the Right Way: "is" vs "==" <https://realpython.com/courses/python-is-identity-vs-equality/>`_
- `Python Scope & the LEGB Rule: Resolving Names in Your Code <https://realpython.com/python-scope-legb-rule/>`_
- `Defining Your Own Python Function <https://realpython.com/defining-your-own-python-function/>`_
- `Null in Python: Understanding Python's NoneType Object <https://realpython.com/null-in-python/>`_
- `Python '!=' Is Not 'is not': Comparing Objects in Python <https://realpython.com/python-is-identity-vs-equality/>`_
- `Python args and kwargs: Demystified <https://realpython.com/courses/python-kwargs-and-args/>`_
- `Documenting Python Code: A Complete Guide <https://realpython.com/courses/documenting-python-code/>`_
- `Thinking Recursively in Python <https://realpython.com/courses/thinking-recursively-python/>`_
- `How to Use Generators and yield in Python <https://realpython.com/introduction-to-python-generators/>`_
- `How to Use Python Lambda Functions <https://realpython.com/courses/python-lambda-functions/>`_
- `Python Decorators 101 <https://realpython.com/courses/python-decorators-101/>`_
- `Writing Comments in Python <https://realpython.com/courses/writing-comments-python/>`_
- `Introduction to Python Exceptions <https://realpython.com/courses/introduction-python-exceptions/>`_
- `Primer on Python Decorators <https://realpython.com/primer-on-python-decorators/>`_



.. --------------- Footnotes ---------------

.. [#brewery-unsplash] Foto original por `Nathan Dumlao`_ en Unsplash.
.. [#blogic] Término para identificar el "algoritmo" o secuencia de instrucciones derivadas del procesamiento que corresponda.
.. [#docstring-formats] Véase `Docstring Formats`_.
.. [#functional-programming] Definición de `Programación funcional` en Wikipedia.
.. [#type-hints] Conocidos como "type hints" en terminología inglesa.

.. --------------- Hyperlinks ---------------

.. _Nathan Dumlao: https://unsplash.com/@nate_dumlao?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
.. _DocString Formats: https://realpython.com/documenting-python-code/#docstring-formats
.. _Programación funcional: https://es.wikipedia.org/wiki/Programaci%C3%B3n_funcional
.. _Modelo de datos: https://docs.python.org/es/3/reference/datamodel.html
.. _Sucesión de Fibonacci: https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci
.. _mypy: http://mypy-lang.org/
