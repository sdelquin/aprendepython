#########
Funciones
#########

.. image:: img/nathan-dumlao-6Lh0bRb9LOA-unsplash.jpg

El concepto de **función** es básico en prácticamente cualquier lenguaje de programación. Se trata de una estructura que nos permite agrupar código. Persigue dos objetivos claros:

1. **No repetir** fragmentos de código en un programa.
2. **Reutilizar** el código en distintos escenarios.

Una función viene *definida* por su *nombre*, sus *parámetros* y su *valor de retorno*. Esta parametrización de las funciones las convierten en una poderosa herramienta ajustable a las circunstancias que tengamos. Al *invocarla* estaremos solicitando su ejecución y obtendremos unos resultados. [#brewery-unsplash]_

*******************
Definir una función
*******************

Para definir una función utilizamos la palabra reservada ``def`` seguida del **nombre** [#naming-functions]_ de la función. A continuación aparecerán 0 o más **parámetros** separados por comas (entre paréntesis), finalizando la línea con **dos puntos** ``:`` En la siguiente línea empezaría el **cuerpo** de la función que puede contener 1 o más **sentencias**, incluyendo (o no) una **sentencia de retorno** con el resultado mediante ``return``.

.. figure:: img/function-definition.jpg
    :align: center

    Definición de una función en Python
   
.. warning:: Prestar especial atención a los dos puntos ``:`` porque suelen olvidarse en la *definición de la función*.

Hagamos una primera función sencilla que no recibe parámetros::

    def say_hello():
        print('Hello!')

.. note::
    Nótese la :ref:`indentación <core/controlflow/conditionals:Definición de bloques>` (sangrado) del *cuerpo* de la función.

Los **nombres de las funciones** siguen :ref:`las mismas reglas que las variables <core/datatypes/data:Variables>` y, como norma general, se suelen utilizar **verbos en infinitivo** para su definición: ``load_data``, ``store_values``, ``reset_cart``, ``filter_results``, ``block_request``, ...

Invocar una función
===================

Para invocar (o "llamar") a una función sólo tendremos que escribir su nombre seguido de paréntesis. En el caso de la función sencilla (vista anteriormente) se haría así:

.. code-block::
    :emphasize-lines: 5

    >>> def say_hello():
    ...     print('Hello!')
    ...

    >>> say_hello()
    Hello!

.. note::
    Como era de esperar, al invocar a esta función obtenemos un mensaje por pantalla, fruto de la ejecución del cuerpo de la función.

Cuando queremos **invocar a una función dentro de un fichero** ``*.py`` lo haremos del mismo modo que hemos visto en el intérprete interactivo:

.. code-block::
    :linenos:

    def say_hello():
        print('Hello!')
    
    # Llamada a la función (primer nivel de indentación)
    say_hello()

Retornar un valor
=================

Las funciones pueden retornar (o "devolver") un valor. Veamos un ejemplo muy sencillo::

    >>> def one():
    ...     return 1
    ...

    >>> one()
    1

.. important:: No confundir ``return`` con ``print()``. El valor de retorno de una función nos permite usarlo fuera de su contexto. El hecho de añadir ``print()`` al cuerpo de una función es algo "coyuntural" y no modifica el resultado de la lógica interna.

.. note:: En la sentencia ``return`` podemos incluir variables y expresiones, no únicamente literales.

Pero no sólo podemos invocar a la función directamente, también la podemos integrar en otras expresiones. Por ejemplo en condicionales::

    >>> if one() == 1:
    ...     print('It works!')
    ... else:
    ...     print('Something is broken')
    ...
    It works!

Si una función no incluye un ``return`` de forma explícita, devolverá :ref:`None <core/controlflow/conditionals:Valor nulo>` de forma implícita::

    >>> def empty():
    ...     x = 0
    ...

    >>> print(empty())
    None

Existe la posibilidad de usar la sentencia ``return`` "a secas" (que también devuelve ``None``) y hace que "salgamos" inmediatamente de la función::

    >>> def quick():
    ...     return
    ...

    >>> print(quick())
    None

.. warning::
    En general, esto **no se considera una buena práctica** salvo que sepamos lo que estamos haciendo. Si la función debe devolver ``None`` es preferible ser **explícito** y utilizar ``return None``. Aunque es posible que en ciertos escenarios nos interese dicha aproximación.

Retornando múltiples valores
----------------------------

Una función puede retornar más de un valor. El "secreto" es hacerlo **mediante una tupla**::

    >>> def multiple():
    ...     return 0, 1  # es una tupla!
    ...

Veamos qué ocurre si invocamos a esta función::

    >>> result = multiple()

    >>> result
    (0, 1)

    >>> type(result)
    tuple

Por lo tanto, podremos aplicar el :ref:`desempaquetado de tuplas <core/datastructures/tuples:desempaquetado de tuplas>` sobre el valor retornado por la función::

    >>> a, b = multiple()
    
    >>> a
    0
    
    >>> b
    1

***********************
Parámetros y argumentos
***********************

Si una función no dispusiera de valores de entrada estaría muy limitada en su actuación. Es por ello que los **parámetros** nos permiten variar los datos que consume una función para obtener distintos resultados. Vamos a empezar a crear funciones que reciben **parámetros**.

En este caso escribiremos una función que recibe un valor numérico y devuelve su raíz cuadrada::

    >>> def sqrt(value):
    ...     return value ** (1/2)
    ...

    >>> sqrt(4)
    2.0

.. note:: En este caso, el valor ``4`` es un **argumento** de la función.

Cuando llamamos a una función con *argumentos*, los valores de estos argumentos se copian en los correspondientes *parámetros* dentro de la función:

.. figure:: img/args-params.jpg
    :align: center

    Parámetros y argumentos de una función

.. tip:: La sentencia ``pass`` permite "no hacer nada". Es una especie de "*placeholder*".

Veamos otra función con dos parámetros y algo más de lógica de negocio: [#blogic]_

.. code-block::

    >>> def _min(a, b):
    ...     if a < b:
    ...         return a
    ...     else:
    ...         return b
    ...

    >>> _min(7, 9)
    7

Nótese que la sentencia ``return`` puede escribirse en **múltiples ocasiones** y puede encontrarse en **cualquier lugar** de la función, no necesariamente al final del cuerpo. Esta técnica puede ser beneficiosa en múltiples escenarios.

Uno de esos escenarios se relaciona con el concepto de **cláusula guarda**: una pieza de código que normalmente está al comienzo de la función y comprueba una serie de condiciones para continuar con la ejecución o cortarla [#guarda]_.

.. admonition:: Ejercicio

    pycheck_: **squared_sum**

Argumentos posicionales
=======================

Los **argumentos posicionales** son aquellos argumentos que se copian en sus correspondientes parámetros **en orden**. 

Vamos a mostrar un ejemplo definiendo una función que construye una "cpu" a partir de 3 parámetros::

    >>> def build_cpu(vendor, num_cores, freq):
    ...     return dict(
    ...         vendor=vendor,
    ...         num_cores=num_cores,
    ...         freq=freq
    ...     )
    ...

Una posible llamada a la función con argumentos posicionales sería la siguiente::

    >>> build_cpu('AMD', 8, 2.7)
    {'vendor': 'AMD', 'num_cores': 8, 'freq': 2.7}

Lo que ha sucedido es un **mapeo** directo entre argumentos y parámetros en el mismo orden que estaban definidos:

+---------------+-----------+
|   Parámetro   | Argumento |
+===============+===========+
| ``vendor``    | ``AMD``   |
+---------------+-----------+
| ``num_cores`` | ``8``     |
+---------------+-----------+
| ``freq``      | ``2.7``   |
+---------------+-----------+

Pero es evidente que una clara desventaja del uso de argumentos posicionales es que se necesita **recordar el orden** de los argumentos. Un error en la posición de los argumentos puede generar resultados indeseados::

    >>> build_cpu(8, 2.7, 'AMD')
    {'vendor': 8, 'num_cores': 2.7, 'freq': 'AMD'}

Argumentos nominales 
====================

En esta aproximación los argumentos no son copiados en un orden específico sino que **se asignan por nombre a cada parámetro**. Ello nos permite evitar el problema de conocer cuál es el orden de los parámetros en la definición de la función. Para utilizarlo, basta con realizar una asignación de cada argumento en la propia llamada a la función.

Veamos la misma llamada que hemos hecho en el ejemplo de construcción de la "cpu" pero ahora utilizando paso de argumentos nominales::

    >>> build_cpu(vendor='AMD', num_cores=8, freq=2.7)
    {'vendor': 'AMD', 'num_cores': 8, 'freq': 2.7}

Se puede ver claramente que el orden de los argumentos no influye en el resultado final::

    >>> build_cpu(num_cores=8, freq=2.7, vendor='AMD')
    {'vendor': 'AMD', 'num_cores': 8, 'freq': 2.7}

Argumentos posicionales y nominales
===================================

Python permite **mezclar argumentos posicionales y nominales** en la llamada a una función::

    >>> build_cpu('INTEL', num_cores=4, freq=3.1)
    {'vendor': 'INTEL', 'num_cores': 4, 'freq': 3.1}

Pero hay que tener en cuenta que, en este escenario, **los argumentos posicionales siempre deben ir antes** que los argumentos nominales. Esto tiene mucho sentido ya que, de no hacerlo así, Python no tendría forma de discernir a qué parámetro corresponde cada argumento::

    >>> build_cpu(num_cores=4, 'INTEL', freq=3.1)
      File "<stdin>", line 1
    SyntaxError: positional argument follows keyword argument

Argumentos mutables e inmutables
================================

|intlev|

Cuando realizamos modificaciones a los argumentos de una función es importante tener en cuenta si son **mutables** (listas, diccionarios, conjuntos, ...) o **inmutables** (tuplas, enteros, flotantes, cadenas de texto, ...) ya que podríamos obtener efectos colaterales no deseados.

Supongamos que nos piden escribir una función que reciba una lista y que devuelva sus valores elevados al cuadrado. Pero lo hacemos "malamente"::

    >>> values = [2, 3, 4]

    >>> def square_it(values):
    ...     # NO HAGAS ESTO
    ...     for i in range(len(values)):
    ...         values[i] **= 2
    ...     return values

    >>> square_it(values)
    [4, 9, 16]

    >>> values  # ???
    [4, 9, 16]

.. warning:: Esto **no es una buena práctica**. O bien documentar que el argumento puede modificarse o bien retornar un nuevo valor. Por regla general, no se recomienda que las funciones modifiquen argumentos de entrada, salvo que sea específicamente lo que estamos buscando.

Parámetros por defecto
======================

Es posible especificar **valores por defecto** en los parámetros de una función. En el caso de que no se proporcione un valor al argumento en la llamada a la función, el parámetro correspondiente tomará el valor definido por defecto.

Siguiendo con el ejemplo de la "cpu", podemos asignar *2.0GHz* como frecuencia por defecto. La definición de la función cambiaría ligeramente::

    >>> def build_cpu(vendor, num_cores, freq=2.0):
    ...     return dict(
    ...         vendor=vendor,
    ...         num_cores=num_cores,
    ...         freq=freq
    ...     )
    ...

Llamada a la función sin especificar frecuencia de "cpu"::

    >>> build_cpu('INTEL', 2)
    {'vendor': 'INTEL', 'num_cores': 2, 'freq': 2.0}

Llamada a la función indicando una frecuencia concreta de "cpu"::

    >>> build_cpu('INTEL', 2, 3.4)
    {'vendor': 'INTEL', 'num_cores': 2, 'freq': 3.4}

|intlev|

Es importante tener presente que los valores por defecto en los parámetros se calculan cuando se **define** la función, no cuando se **ejecuta**. Veamos un ejemplo siguiendo con el caso anterior::

    >>> DEFAULT_FREQ = 2.0
    
    >>> def build_cpu(vendor, num_cores, freq=DEFAULT_FREQ):
    ...     return dict(
    ...         vendor=vendor,
    ...         num_cores=num_cores,
    ...         freq=freq
    ...     )
    ...
    
    >>> build_cpu('AMD', 4)
    {'vendor': 'AMD', 'num_cores': 4, 'freq': 2.0}
    
    >>> DEFAULT_FREQ = 3.5
    
    >>> build_cpu('AMD', 4)
    {'vendor': 'AMD', 'num_cores': 4, 'freq': 2.0}

.. admonition:: Ejercicio

    pycheck_: **factorial**

Modificando parámetros mutables
-------------------------------

|advlev|

Hay que tener cuidado a la hora de manejar los parámetros que pasamos a una función ya que :ref:`podemos obtener resultados indeseados <core/modularity/functions:argumentos mutables e inmutables>`, especialmente cuando trabajamos con *tipos de datos mutables*.

Supongamos una función que añade elementos a una lista que pasamos por parámetro. La idea es que si no pasamos la lista, ésta siempre empiece siendo vacía. Hagamos una serie de pruebas pasando alguna lista como segundo argumento::

    >>> def buggy(arg, result=[]):
    ...     result.append(arg)
    ...     print(result)
    ...

    >>> buggy('a', [])
    ['a']

    >>> buggy('b', [])
    ['b']

    >>> buggy('a', ['x', 'y', 'z'])
    ['x', 'y', 'z', 'a']

    >>> buggy('b', ['x', 'y', 'z'])
    ['x', 'y', 'z', 'b']

Aparentemente todo está funcionando de manera correcta, pero veamos qué ocurre en las siguientes llamadas:

.. code-block::

    >>> def buggy(arg, result=[]):
    ...     result.append(arg)
    ...     print(result)
    ...

    >>> buggy('a')
    ['a']

    >>> buggy('b')  # Se esperaría ['b']
    ['a', 'b']

Obviamente algo no ha funcionado correctamente. Se esperaría que ``result`` tuviera una lista vacía en cada ejecución. Sin embargo esto no sucede por estas dos razones:

1. El valor por defecto se establece cuando se define la función.
2. La variable ``result`` apunta a una zona de memoria en la que se modifican sus valores.

Ejecución **paso a paso** a través de *Python Tutor*:

.. only:: latex

    https://cutt.ly/sBNpVT2

.. only:: html

    .. raw:: html

        <iframe width="800" height="410" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20buggy%28arg,%20result%3D%5B%5D%29%3A%0A%20%20%20%20result.append%28arg%29%0A%20%20%20%20print%28result%29%0A%0Abuggy%28'a'%29%0A%0Abuggy%28'b'%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>


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

La forma de arreglar el código anterior utilizando un parámetro con valor por defecto sería utilizar un **tipo de dato inmutable** y tener en cuenta cuál es la primera llamada::

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

    >>> nonbuggy('a', ['x', 'y', 'z'])
    ['x', 'y', 'z', 'a']

    >>> nonbuggy('b', ['x', 'y', 'z'])
    ['x', 'y', 'z', 'b']

Empaquetar/Desempaquetar argumentos
===================================

|intlev|

Python nos ofrece la posibilidad de empaquetar y desempaquetar argumentos cuando estamos invocando a una función, tanto para **argumentos posicionales** como para **argumentos nominales**.

Y de esto se deriva el hecho de que podamos utilizar un **número variable de argumentos** en una función, algo que puede ser muy interesante según el caso de uso que tengamos.

Empaquetar/Desempaquetar argumentos posicionales
------------------------------------------------

Si utilizamos el operador ``*`` delante del nombre de un parámetro posicional, estaremos indicando que los argumentos pasados a la función se empaqueten en una **tupla**.

Veamos un ejemplo en el que vamos a **implementar una función para sumar un número variable de valores**. La función que tenemos disponible en Python no cubre este caso::

    >>> sum(4, 3, 2, 1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: sum() takes at most 2 arguments (4 given)

Para superar esta "limitación" vamos a hacer uso del ``*`` para empaquetar los argumentos posicionales::

    >>> def _sum(*values):
    ...     result = 0
    ...     for value in values:  # values es una tupla
    ...         result += value
    ...     return result
    ...

    >>> _sum(4, 3, 2, 1)
    10

Existe la posibilidad de usar el asterisco ``*`` en la llamada a la función para **desempaquetar** los argumentos posicionales::

    >>> values = (4, 3, 2, 1)
    
    >>> _sum(values)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 4, in _sum
    TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
    
    >>> _sum(*values)  # Desempaquetado
    10

Empaquetar/Desempaquetar argumentos nominales
---------------------------------------------

Si utilizamos el operador ``**`` delante del nombre de un parámetro nominal, estaremos indicando que los argumentos pasados a la función se empaqueten en un **diccionario**.

Supongamos un ejemplo en el que queremos **encontrar la persona con mayor calificación de un examen**. Haremos uso del ``**`` para empaquetar los argumentos nominales::

    >>> def best_student(**marks):
    ...     max_mark = -1
    ...     for student, mark in marks.items():  # marks es un diccionario
    ...         if mark > max_mark:
    ...             max_mark = mark
    ...             best_student = student
    ...     return best_student
    ...

    >>> best_student(ana=8, antonio=6, inma=9, javier=7)
    'inma'

Al igual que veíamos previamente, existe la posibilidad de usar doble asterisco ``**`` en la llamada a la función para **desempaquetar** los argumentos nominales::

    >>> marks = dict(ana=8, antonio=6, inma=9, javier=7)

    >>> best_student(marks)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: best_student() takes 0 positional arguments but 1 was given

    >>> best_student(**marks)  # Desempaquetado
    'inma'

Convenciones
------------

En muchas ocasiones se utiliza ``args`` como nombre de parámetro para argumentos posicionales y ``kwargs`` como nombre de parámetro para argumentos nominales. Esto son únicamente **convenciones**, no hay obligación de utilizar estos nombres. Así, podemos encontrar funciones definidas de la siguiente manera:

    >>> def func(*args, **kwargs):
    ...     # TODO
    ...     pass
    ...

Forzando modo de paso de argumentos
===================================

Si bien Python nos da flexibilidad para pasar argumentos a nuestras funciones en modo nominal o posicional, existen opciones para forzar que dicho paso sea obligatorio para una determinada modalidad.

Argumentos sólo nominales
-------------------------

|advlev|

A partir de `Python 3.0 <https://www.python.org/dev/peps/pep-3102/>`_ se ofrece la posibilidad de obligar a que determinados parámetros de la función sean pasados sólo por nombre.

Para ello, en la definición de los parámetros de la función, tendremos que incluir un parámetro especial ``*`` que delimitará el tipo de parámetros. Así, todos los parámetros a la derecha del separador estarán **obligados** a ser nominales:

.. figure:: img/keyword-only-params.png
    :align: center

    Separador para especificar parámetros sólo nominales

Ejemplo::

    >>> def sum_power(a, b, *, power=False):
    ...     if power:
    ...         a **= 2
    ...         b **= 2
    ...     return a + b
    ...

    >>> sum_power(3, 4)
    7

    >>> sum_power(a=3, b=4)
    7

    >>> sum_power(3, 4, power=True)
    25

    >>> sum_power(3, 4, True)
    ---------------------------------------------------------------------------
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: sum_power() takes 2 positional arguments but 3 were given

Argumentos sólo posicionales
----------------------------

|advlev|

A partir de `Python 3.8 <https://www.python.org/dev/peps/pep-0570/>`_ se ofrece la posibilidad de obligar a que determinados parámetros de la función sean pasados sólo por posición.

Para ello, en la definición de los parámetros de la función, tendremos que incluir un parámetro especial ``/`` que delimitará el tipo de parámetros. Así, todos los parámetros a la izquierda del delimitador estarán **obligados** a ser posicionales:

.. figure:: img/position-only-params.png
    :align: center

    Separador para especificar parámetros sólo posicionales

Ejemplo::

    >>> def sum_power(a, b, /, power=False):
    ...     if power:
    ...         a **= 2
    ...         b **= 2
    ...     return a + b
    ...

    >>> sum_power(3, 4)
    7

    >>> sum_power(3, 4, True)
    25

    >>> sum_power(3, 4, power=True)
    25

    >>> sum_power(a=3, b=4)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: sum_power() got some positional-only arguments passed as keyword arguments: 'a, b'

Fijando argumentos posicionales y nominales
-------------------------------------------

Si mezclamos las dos estrategias anteriores podemos forzar a que una función reciba argumentos de un modo concreto.

Continuando con el ejemplo anterior, podríamos hacer lo siguiente::

    >>> def sum_power(a, b, /, *, power=False):
    ...     if power:
    ...         a **= 2
    ...         b **= 2
    ...     return a + b
    ...

    >>> sum_power(3, 4, power=True)  # Único modo posible de llamada
    25

.. admonition:: Ejercicio

    pycheck_: **consecutive_freqs**
    

Funciones como parámetros
=========================

|advlev|

Las funciones se pueden utilizar en cualquier contexto de nuestro programa. Son objetos que pueden ser asignados a variables, usados en expresiones, devueltos como valores de retorno o pasados como argumentos a otras funciones.

Veamos un primer ejemplo en el que pasamos una función como argumento::

    >>> def success():
    ...     print('Yeah!')
    ...

    >>> type(success)
    function

    >>> def doit(f):
    ...     f()
    ...

    >>> doit(success)
    Yeah!

Veamos un segundo ejemplo en el que pasamos, no sólo una función como argumento, sino los valores con los que debe operar::

    >>> def repeat_please(text, times=1):
    ...     return text * times
    ...

    >>> type(repeat_please)
    function

    >>> def doit(f, arg1, arg2):
    ...     return f(arg1, arg2)
    ...

    >>> doit(repeat_please, 'Functions as params', 2)
    'Functions as paramsFunctions as params'

*************
Documentación
*************

Ya hemos visto que en Python podemos incluir :ref:`comentarios <core/controlflow/conditionals:Comentarios>` para explicar mejor determinadas zonas de nuestro código.

Del mismo modo podemos (y en muchos casos **debemos**) adjuntar **documentación** a la definición de una función incluyendo una cadena de texto (**docstring**) al comienzo de su cuerpo::

    >>> def sqrt(value):
    ...     'Returns the square root of the value'
    ...     return value ** (1/2)
    ...

La forma más ortodoxa de escribir un ``docstring`` es utilizando *triples comillas*::

    >>> def closest_int(value):
    ...     '''Returns the closest integer to the given value.
    ...     The operation is:
    ...         1. Compute distance to floor.
    ...         2. If distance less than a half, return floor.
    ...            Otherwise, return ceil.
    ...     '''
    ...     floor = int(value)
    ...     if value - floor < 0.5:
    ...         return floor
    ...     else:
    ...         return floor + 1
    ...

Para ver el ``docstring`` de una función, basta con utilizar ``help``::

    >>> help(closest_int)

    Help on function closest_int in module __main__:

    closest_int(value)
        Returns the closest integer to the given value.
        The operation is:
            1. Compute distance to floor.
            2. If distance less than a half, return floor.
               Otherwise, return ceil.

También es posible extraer información usando el símbolo de interrogación::

    >>> closest_int?
    Signature: closest_int(value)
    Docstring:
    Returns the closest integer to the given value.
    The operation is:
        1. Compute distance to floor.
        2. If distance less than a half, return floor.
        Otherwise, return ceil.
    File:      ~/aprendepython/<ipython-input-75-5dc166360da1>
    Type:      function


.. important:: Esto no sólo se aplica a funciones propias, sino a cualquier otra función definida en el lenguaje.

.. note:: Si queremos ver el ``docstring`` de una función en "crudo" (sin formatear), podemos usar ``<function>.__doc__``.


Explicación de parámetros
=========================

Como ya se ha visto, es posible documentar una función utilizando un ``docstring``. Pero la redacción y el formato de esta cadena de texto puede ser muy variada. Existen distintas formas de documentar una función (u otros objetos) [#docstring-formats]_:

`reStructuredText docstrings`_
    Formato de documentación recomendado por Python.
`Google docstrings`_
    Formato de documentación recomendado por Google.
`NumPy-SciPy docstrings`_
    Combinación de formatos reStructuredText y Google (usados por el proyecto `NumPy`_).
`Epytext docstrings`_
    Formato utilizado por Epydoc_ (una adaptación de Javadoc).

Aunque cada uno tienes sus particularidades, todos comparten una misma estructura:

* Una primera línea de **descripción de la función**.
* A continuación especificamos las características de los **parámetros** (incluyendo sus tipos).
* Por último, indicamos si la función **retorna un valor** y sus características.

Aunque todos los formatos son válidos, nos centraremos en **reStructuredText** por ser el estándar propuesto por Python para la documentación.

.. seealso::
    *Google docstrings* y *Numpy docstrings* también son ampliamente utilizados, lo único es que necesitan de un módulo externo denominado `Napoleon`_ para que se puedan incluir en la documentación *Sphinx*.

Sphinx
------

`Sphinx`_ es una herramienta para generar documentación usando el lenguaje reStructuredText_ o RST. Incluye un módulo "built-in" denominado `autodoc`_ el cual permite la autogeneración de documentación a partir de los "docstrings" definidos en el código.

Veamos el uso de este formato en la documentación de la siguiente función::

    >>> def my_power(x, n):
    ...     '''Calculate x raised to the power of n.
    ...
    ...     :param x: number representing the base of the operation
    ...     :type x: int
    ...     :param n: number representing the exponent of the operation
    ...     :type n: int
    ...
    ...     :return: :math:`x^n`
    ...     :rtype: int
    ...     '''
    ...     result = 1
    ...     for _ in range(n):
    ...         result *= x
    ...     return result
    ...
    
Dentro del "docstring" podemos escribir con sintaxis `reStructuredText`_ -- véase por ejemplo la expresión matemática en el tag ``:return:`` -- lo que nos proporciona una gran flexibilidad.

.. note:: La plataforma `Read the Docs`_ aloja la documentación de gran cantidad de proyectos. En muchos de los casos se han usado "docstrings" con el formato Sphinx visto anteriormente. Un ejemplo de ello es la popular librería de Python requests_.

Anotación de tipos
==================

|intlev|

Las anotaciones de tipos o **type-hints** [#type-hints]_ se introdujeron en `Python 3.5 <https://www.python.org/dev/peps/pep-0484/>`_ y permiten indicar tipos para los parámetros de una función y/o para su valor de retorno (*aunque también funcionan en creación de variables*).

Veamos un ejemplo en el que creamos una función para dividir una cadena de texto por la posición especificada en el parámetro::

    >>> def ssplit(text: str, split_pos: int) -> tuple:
    ...     return text[:split_pos], text[split_pos:]
    ...

    >>> ssplit('Always remember us this way', 15)
    ('Always remember', ' us this way')

Como se puede observar, vamos añadiendo los tipos después de cada parámetro utilizando ``:`` como separador. En el caso del valor de retorno usamos la flecha ``->``

Quizás la siguiente ejecución pueda sorprender::

    >>> ssplit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
    ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])

Efectivamente como habrás visto, **no hemos obtenido ningún error**, a pesar de que estamos pasando como primer argumento una lista en vez de una cadena de texto. Esto ocurre porque lo que hemos definido es simplemente una anotación de tipo, no una declaración de tipo. Existen herramientas como `mypy`_ que sí se encarga de comprobar este escenario.

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

Las **anotaciones de tipos** son una herramienta muy potente y que, usada de forma adecuada, permite complementar la documentación de nuestro código y aclarar ciertos aspectos, que a priori, pueden parecer confusos. Su aplicación estará en función de la necesidad detectada por parte del equipo de desarrollo.

Tipos compuestos
----------------

Hay escenarios en los que necesitamos más expresividad de cara a la anotación de tipos. ¿Qué ocurre si queremos indicar una *lista de cadenas de texto* o un *conjunto de enteros*.

Veamos algunos ejemplos válidos:

+----------------------+-------------------------------------------------------------------------------+
|      Anotación       |                                  Significado                                  |
+======================+===============================================================================+
| ``list[str]``        | Lista de cadenas de texto                                                     |
+----------------------+-------------------------------------------------------------------------------+
| ``set[int]``         | Conjunto de enteros                                                           |
+----------------------+-------------------------------------------------------------------------------+
| ``dict[str, float]`` | Diccionario donde las claves son cadenas de texto y los valores son flotantes |
+----------------------+-------------------------------------------------------------------------------+

Múltiples tipos
---------------

En el caso de que queramos indicar que un determinado parámetro puede ser de un tipo o de otro hay que especificarlo utilizando el operador [#or-types]_ ``|``.

Veamos algunos ejemplos válidos:

+--------------------+---------------------------------------+
|     Anotación      |              Significado              |
+====================+=======================================+
+--------------------+---------------------------------------+
| ``tuple❘dict``     | Tupla o diccionario                   |
+--------------------+---------------------------------------+
| ``list[str❘int]``  | Lista de cadenas de texto y/o enteros |
+--------------------+---------------------------------------+
| ``set[int❘float]`` | Conjunto de enteros y/o flotantes     |
+--------------------+---------------------------------------+

.. seealso::
    `Guía rápida para de anotación de tipos (mypy) <https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html>`_

.. admonition:: Ejercicio

    pycheck_: **mcount**

******************
Tipos de funciones
******************

|advlev|

Funciones interiores
====================

Está permitido definir una función dentro de otra función::

    >>> VALID_CHARS = 'xyz'

    >>> def validation_rate(text: str) -> float:
    ...     '''Rate of valid chars in text.'''
    ...     def is_valid_char(char: str) -> bool:
    ...         return char in VALID_CHARS
    ...
    ...     checklist = [is_valid_char(c) for c in text]
    ...     return sum(checklist) / len(text)
    ...

    >>> validation_rate('zxyzxxyz')
    1.0

    >>> validation_rate('abzxyabcdz')
    0.4

    >>> validation_rate('abc')
    0.0

.. tip::
    Estas funciones pueden tener sentido cuando su ámbito de aplicación es muy concreto y no se pueden reutilizar fácilmente.

Clausuras
=========

Una **clausura** (del término inglés "*closure*") establece el uso de una :ref:`función interior <core/modularity/functions:Funciones interiores>` que se genera dinámicamente y recuerda los valores de los argumentos con los que fue creada::

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

    >>> make_multiplier_of(5)(8)  # Llamada directa!
    40

.. important:: En una clausura retornamos una función, no una llamada a una función.

Funciones anónimas "lambda"
===========================

Una **función lambda** tiene las siguientes propiedades:
    1. Se escribe en una única sentencia (línea).
    2. No tiene nombre (anónima).
    3. Su cuerpo conlleva un ``return`` implícito.
    4. Puede recibir cualquier número de parámetros.

Veamos un primer ejemplo de función "lambda" que nos permite contar el número de palabras de una cadena de texto::

    >>> num_words = lambda t: len(t.split())

    >>> type(num_words)
    function

    >>> num_words
    <function __main__.<lambda>(t)>

    >>> num_words('hola socio vamos a ver')
    5

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

Las funciones "lambda" son bastante utilizadas **como argumentos a otras funciones**. Un ejemplo claro de ello es la función ``sorted`` que recibe un parámetro opcional ``key`` donde se define la clave de ordenación.

Veamos cómo usar una función anónima "lambda" para ordenar una tupla de pares *longitud-latitud*::

    >>> geoloc = (
    ... (15.623037, 13.258358),
    ... (55.147488, -2.667338),
    ... (54.572062, -73.285171),
    ... (3.152857, 115.327724),
    ... (-40.454262, 172.318877)
    )

    >>> # Ordenación por longitud (primer elemento de la tupla)
    >>> sorted(geoloc)
    [(-40.454262, 172.318877),
     (3.152857, 115.327724),
     (15.623037, 13.258358),
     (54.572062, -73.285171),
     (55.147488, -2.667338)]

    >>> # Ordenación por latitud (segundo elemento de la tupla)
    >>> sorted(geoloc, key=lambda t: t[1])
    [(54.572062, -73.285171),
     (55.147488, -2.667338),
     (15.623037, 13.258358),
     (3.152857, 115.327724),
     (-40.454262, 172.318877)]

.. admonition:: Ejercicio

    pycheck_: **sort_ages**

Enfoque funcional
=================

Como se comentó en la :ref:`introducción <core/introduction/python:Características del lenguaje>`, Python es un lenguaje de programación multiparadigma. Uno de los `paradigmas <https://es.wikipedia.org/wiki/Paradigma_de_programaci%C3%B3n>`_ menos explotados en este lenguaje es la **programación funcional** [#functional-programming]_.

Python nos ofrece 3 funciones que encajan verdaderamente bien en este enfoque: ``map()``, ``filter()`` y ``reduce()``.

.. figure:: img/map-filter-reduce.png
    :align: center

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

.. tip::
    Hay que tener en cuenta que ``map()`` devuelve un :ref:`generador <core/modularity/functions:generadores>`, no directamente una lista.

Podemos obtener el mismo resultado aplicando una :ref:`función anónima "lambda" <core/modularity/functions:Funciones anónimas "lambda">`::

    >>> list(map(lambda x: x**2 / 2, data))
    [0.5, 2.0, 4.5, 8.0, 12.5, 18.0, 24.5, 32.0, 40.5, 50.0]

En Python es posible "simular" un ``map()`` a través de una :ref:`lista por comprensión <core/datastructures/lists:listas por comprensión>`::

    >>> [x**2 / 2 for x in data]
    [0.5, 2.0, 4.5, 8.0, 12.5, 18.0, 24.5, 32.0, 40.5, 50.0]

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

.. tip::
    Hay que tener en cuenta que ``filter()`` devuelve un :ref:`generador <core/modularity/functions:generadores>`, no directamente una lista.

Podemos obtener el mismo resultado aplicando una :ref:`función anónima "lambda" <core/modularity/functions:Funciones anónimas "lambda">`::

    >>> list(filter(lambda x: x % 2 == 1, data))
    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

En Python es posible "simular" un ``filter()`` a través de una :ref:`lista por comprensión <core/datastructures/lists:listas por comprensión>`::

    >>> [x for x in data if x % 2 == 1]
    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

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

Aplicando una :ref:`función anónima "lambda" <core/modularity/functions:Funciones anónimas "lambda">`...

    >>> reduce(lambda x, y: x * y, data)
    120

.. hint:: Por cuestiones de legibilidad del código, se suelen preferir las **listas por comprensión** a funciones como ``map()`` o ``filter()``, aunque cada problema tiene sus propias características y sus soluciones más adecuadas. Es un **enfoque "más pitónico"**.

Hazlo pitónico
--------------

`Trey Hunner <https://treyhunner.com/>`_ explica en una de sus "newsletters" lo que él entiende por **código pitónico**:

"Pitónico es un término extraño que significa diferentes cosas para diferentes personas. Algunas personas piensan que código pitónico va sobre legibilidad. Otras personas piensan que va sobre adoptar características particulares de Python. Mucha gente tiene una definición difusa que no va sobre legibilidad ni sobre características del lenguaje.

Yo normalmente uso el término código pitónico como un sinónimo de código idiomático o la forma en la que la comunidad de Python tiende a hacer las cosas cuando escribe Python. Eso deja mucho espacio a la interpretación, ya que lo que hace algo idiomático en Python no está particularmente bien definido.

Yo argumento que código pitónico implica adoptar el :ref:`desempaquetado de tuplas <core/datastructures/tuples:desempaquetado de tuplas>`, usar :ref:`listas por comprensión <core/datastructures/lists:listas por comprensión>` cuando sea apropiado, usar :ref:`argumentos nominales <core/modularity/functions:argumentos nominales>` cuando tenga sentido, evitar el :ref:`uso excesivo de clases <core/modularity/oop:objetos y clases>`, usar las :ref:`estructuras de iteración <core/controlflow/loops:bucles>` adecuadas o evitar :ref:`recorrer mediante índices <core/datastructures/lists:iterar sobre una lista>`.

Para mí, código pitónico significa intentar ver el código desde la perspectiva de las herramientas específicas que Python nos proporciona, en oposición a la forma en la que resolveríamos el mismo problema usando las herramientas que nos proporciona JavaScript, Java, C, ..."

Generadores
===========

Un **generador**, como su propio nombre indica, se encarga de generar "valores" sobre los que podemos iterar. Es decir, no construye una secuencia de forma explícita, sino que nos permite ir "consumiendo" un valor de cada vez. Esta propiedad los hace idóneos para situaciones en las que el tamaño de las secuencias podría tener un impacto negativo en el consumo de memoria.

De hecho ya hemos visto algunos generadores y los hemos usado sin ser del todo conscientes. Algo muy parecido [#range]_ a un generador es ``range()`` que ofrece la posibilidad de crear :ref:`secuencias de números <core/controlflow/loops:Secuencias de números>`.

Básicamente existen dos implementaciones de generadores:

- Funciones generadoras.
- Expresiones generadoras.

.. important:: A diferencia de las funciones ordinarias, los generadores tienen la capacidad de **"recordar" su estado** para recuperarlo en la siguiente iteración y continuar devolviendo nuevos valores.

Funciones generadoras
---------------------

Las funciones generadoras [#yield]_ (o factorías de generadores) se escriben como funciones ordinarias con el matiz de incorporar la sentencia ``yield`` que sustituye, de alguna manera, a ``return``. Esta sentencia devuelve el valor indicado y, a la vez, "congela" el estado de la función hasta la siguiente llamada.

Veamos un ejemplo en el que escribimos una **función generadora de números pares**::

    >>> def evens(lim):
    ...     for i in range(0, lim + 1, 2):
    ...         yield i
    ...

    >>> type(evens)
    function

    >>> evens_gen = evens(20)  # retorna un generador

    >>> type(evens_gen)
    generator

Una vez creado el generador, ya podemos iterar sobre él::

    >>> for even in evens_gen:
    ...     print(even, end=' ')
    ...
    0 2 4 6 8 10 12 14 16 18 20

De forma más "directa", podemos iterar sobre la propia llamada a la función generadora::

    >>> for even in evens(20):
    ...     print(even, end=' ')
    ...
    0 2 4 6 8 10 12 14 16 18 20

Si queremos "explicitar" la lista de valores que contiene un generador, podemos hacerlo convirtiendo a lista::

    >>> list(evens(20))
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

Un detalle muy importante es que **los generadores "se agotan"**. Es decir, una vez que ya hemos consumido todos sus elementos, no obtendremos nuevos valores::

    >>> evens_gen = evens(10)
    
    >>> for even in evens_gen:
    ...     print(even, end=' ')
    ...
    0 2 4 6 8 10

    >>> for even in evens_gen:
    ...     print(even, end=' ')
    ... # No sale nada... ¡Agotado!

Expresiones generadoras
-----------------------

Una **expresión generadora** es sintácticamente muy similar a una *lista por comprensión*, pero utilizamos **paréntesis** en vez de corchetes. Se podría ver como una versión acortada de una función generadora.

Podemos tratar de reproducir el ejemplo visto en :ref:`funciones generadoras <core/modularity/functions:Funciones generadoras>` en el que creamos números pares hasta el 20::

    >>> evens_gen = (i for i in range(0, 20, 2))

    >>> type(evens_gen)
    generator

    >>> for i in evens_gen:
    ...     print(i, end=' ')
    ...
    0 2 4 6 8 10 12 14 16 18

.. seealso:: Las expresiones generadoras admiten *condiciones* y *anidamiento de bucles*, tal y como se vio con las :ref:`listas por comprensión <core/datastructures/lists:listas por comprensión>`.

Una expresión generadora se puede explicitar, sumar, buscar su máximo o su mínimo, o lo que queramos, tal y como lo haríamos con un iterable cualquiera::

    >>> list(i for i in range(0, 20, 2))
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

    >>> sum(i for i in range(0, 20, 2))
    90

    >>> min(i for i in range(0, 20, 2))
    0

    >>> max(i for i in range(0, 20, 2))
    18

.. admonition:: Ejercicio

    pycheck_: **gen_squared**

Decoradores
===========

Hay situaciones en las que necesitamos modificar el comportamiento de funciones existentes pero sin alterar su código. Para estos casos es muy útil usar decoradores.

Un **decorador** es una *función* que recibe como parámetro una función y devuelve otra función. Se podría ver como un caso particular de :ref:`clausura <core/modularity/functions:Clausuras>`.

.. figure:: img/decorator-candy.png
    :align: center

    Esqueleto básico de un decorador

El *esqueleto básico* de un decorador es el siguiente::

    >>> def my_decorator(func):
    ...     def wrapper(*args, **kwargs):
    ...         # some code before calling func
    ...         return func(*args, **kwargs)
    ...         # some code after calling func
    ...     return wrapper
    ...

+------------------+------------------------------------------------+
|     Elemento     |                  Descripción                   |
+==================+================================================+
| ``my_decorator`` | Nombre del decorador                           |
+------------------+------------------------------------------------+
| ``wrapper``      | Función interior (convención de nombre)        |
+------------------+------------------------------------------------+
| ``func``         | Función a decorar (convención de nombre)       |
+------------------+------------------------------------------------+
| ``*args``        | Argumentos posicionales (convención de nombre) |
+------------------+------------------------------------------------+
| ``**kwargs``     | Argumentos nominales (convención de nombre)    |
+------------------+------------------------------------------------+


Veamos un ejemplo de **decorador que convierte el resultado numérico de una función a su representación binaria**::

    >>> def res2bin(func):
    ...     def wrapper(*args, **kwargs):
    ...         result = func(*args, **kwargs)
    ...         return bin(result)
    ...     return wrapper
    ...

Ahora definimos una función ordinaria (que usaremos más adelante) y que computa :math:`x^n`::

    >>> def power(x: int, n: int) -> int:
    ...     return x ** n
    ...

    >>> power(2, 3)
    8
    >>> power(4, 5)
    1024

Ahora aplicaremos el decorador definido previamente ``res2bin()`` sobre la función ordinaria ``power()``. Se dice que ``res2bin()`` es la **función decoradora** y que ``power()`` es la **función decorada**::

    >>> decorated_power = res2bin(power)

    >>> decorated_power(2, 3)  # 8
    '0b1000'
    >>> decorated_power(4, 5)  # 1024
    '0b10000000000'

Usando ``@`` para decorar
-------------------------

Python nos ofrece un "`syntactic sugar`_" para simplificar la aplicación de los decoradores a través del operador ``@`` justo antes de la definición de la función que queremos decorar::

    >>> @res2bin
    ... def power(x: int, n: int):
    ...     return x ** n
    ...
    
    >>> power(2, 3)
    '0b1000'
    >>> power(4, 5)
    '0b10000000000'

.. admonition:: Ejercicio

    pycheck_: **abs_decorator**

Manipulando argumentos
----------------------

Hemos visto un ejemplo de decorador que trabaja sobre el resultado de la función decorada, pero nada impide que trabajemos sobre los argumentos que se le pasa a la función decorada.

Supongamos un escenario en el que implementamos **funciones que trabajan con dos operandos** y queremos asegurarnos de que **esos operados son números enteros**. Lo primero será definir el decorador::

    >>> def assert_int(func):
    ...     def wrapper(value1: int, value2: int, /) -> int | float | None:
    ...         if isinstance(value1, int) and isinstance(value2, int):
    ...             return func(value1, value2)
    ...         return None
    ...     return wrapper
    ...

.. tip::
    Dado que sabemos positivamente que las funciones a decorar trabajan con dos operados (dos parámetros) podemos definir la función interior ``wrapper(value1, value2)`` con dos parámetros, en vez de con un número indeterminado de parámetros.

Ahora creamos una función sencilla que suma dos números y le aplicamos el decorador::

    >>> @assert_int
    ... def _sum(a, b):
    ...     return a + b
    ...

Veamos el comportamiento para diferentes casos de uso::

    >>> result = _sum(3, 4)
    >>> print(result)
    7

    >>> result = _sum(5, 'a')
    >>> print(result)
    None

    >>> result = _sum('a', 'b')
    >>> print(result)
    None

Múltiples decoradores
---------------------

Podemos aplicar más de un decorador a cada función. Para ejemplificarlo vamos a crear dos decoradores muy sencillos::

    >>> def plus5(func):
    ...     def wrapper(*args, **kwargs):
    ...         result = func(*args, **kwargs)
    ...         return result + 5
    ...     return wrapper
    ...

    >>> def div2(func):
    ...     def wrapper(*args, **kwargs):
    ...         result = func(*args, **kwargs)
    ...         return result // 2
    ...     return wrapper
    ...

Ahora aplicaremos ambos decoradores sobre una función que realiza el producto de dos números::

    >>> @plus5
    ... @div2
    ... def prod(a, b):
    ...     return a * b
    ...

    >>> prod(4, 3)
    11

    >>> ((4 * 3) // 2) + 5
    11

Cuando tenemos varios decoradores, **se aplican desde afuera hacia adentro** (modelo capa de cebolla). Eso sí, hay que tener en cuenta que la ejecución de un decorador puede depender de otro decorador.

Si anotamos los decoradores podemos ver exactamente cuál es el orden de ejecución::

    >>> def plus5(func):
    ...     def wrapper(*args, **kwargs):
    ...         result = func(*args, **kwargs)  # ——————┐
    ...         print(f'{result=}')             #       |
    ...         print('plus5')                  #       |
    ...         return result + 5               #       |
    ...     return wrapper                      #       |
    ...                                         #       |
    ...                                         #       |
    ... def div2(func):                         #       |
    ...     def wrapper(*args, **kwargs):       #       |
    ...         result = func(*args, **kwargs)  # ◄—————┘
    ...         print(f'{result=}')
    ...         print('div2')
    ...         return result // 2
    ...     return wrapper

Ahora ejecutamos la función decorada::

    >>> prod(4, 3)
    result=12     # función prod "tal cual" (4*3)
    div2          # decorador div2
    result=6      # aplicación decorador div2 (12/2)
    plus5         # decorador plus5
    11            # aplicación decorador plus5 (6+5)

Decoradores con parámetros
--------------------------

El último "salto mortal" sería definir decoradores con parámetros. El *esqueleto básico* de un decorador con parámetros es el siguiente::

    >>> def my_decorator_with_params(*args, **kwargs):
    ...     def decorator(func):
    ...         def wrapper(*args, **kwargs):
    ...             return func(*args, **kwargs)
    ...         return wrapper
    ...     return decorator
    ...

.. attention::
    Nótese que ``my_decorator_with_params()`` no es exactamente un decorador sino que es una factoría de decoradores (:ref:`clausura <core/modularity/functions:clausuras>`) que devuelve un decorador según los argumentos pasados.    

Lo más sencillo es verlo con un ejemplo. Supongamos que queremos forzar a que los parámetros de entrada a la función sean de un tipo concreto (pero parametrizable). Podríamos definir el decorador de la siguiente manera::

    >>> def assert_type(atype):
    ...     def decorator(func):
    ...         def wrapper(*args, **kwargs):
    ...             all_args_with_atype = all(isinstance(a, atype) for a in args)
    ...             all_kwargs_with_atype = all(isinstance(a, atype) for a in kwargs.values())
    ...             if all_args_with_atype and all_kwargs_with_atype:
    ...                 return func(*args, **kwargs)
    ...             return None
    ...         return wrapper
    ...     return decorator
    ...

Ahora creamos una función sencilla que suma dos números y le aplicamos el decorador::

    >>> @assert_type(float)
    ... def _sum(a, b):
    ...     return a + b
    ...

Veamos el comportamiento para diferentes casos de uso::

    >>> result = _sum(3, 4)
    >>> print(result)
    None

    >>> result = _sum(3.0, 4.0)
    >>> print(result)
    7.0

    >>> result = _sum(a=3.0, b=4.0)  # Funciona con kwargs!
    >>> print(result)
    7.0

La ventaja que tiene este enfoque es que podemos aplicar "distintos" decoradores modificando sus parámetros. Por ejemplo, supongamos que ahora queremos **asegurar que una función trabaja únicamente con cadenas de texto**::

    >>> @assert_type(str)
    ... def split(text):
    ...     half_size = len(text) // 2
    ...     return text[:half_size], text[half_size:]
    ...

Veamos su aplicación con distintos tipos de datos::

    >>> result = split('bienvenida')
    >>> print(result)
    ('bienv', 'enida')

    >>> result = split(256)
    >>> print(result)
    None

    >>> result = split([10, 20, 30, 40])
    >>> print(result)
    None

.. admonition:: Ejercicio

    ¿Sabría implementar un decorador para ordenar el resultado de cualquier función tomando un parámetro opcional que indique si la ordenación es ascendente o descendente?

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

.. warning:: Podemos observar que existe un número máximo de llamadas recursivas. Python controla esta situación por nosotros, ya que, de no ser así, podríamos llegar a consumir todos los recursos del sistema.

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

.. admonition:: Ejercicio

    pycheck_: **factorial_recursive**

Otra aproximación a la recursividad se da en problemas donde tenemos que procesar una secuencia de elementos. Supongamos que nos piden **calcular la suma de las longitudes de una serie de palabras** definidas en una lista::

    >>> def get_size(words: list[str]) -> int:
    ...     if len(words) == 0:
    ...         return 0
    ...     return len(words[0]) + get_size(words[1:])
    ...

    >>> words = ['this', 'is', 'recursive']
    >>> get_size(words)
    15

Funcionitis
===========

La "funcionitis" es una "inflamación en la zona funcional" por querer aplicar funciones donde no es necesario. Un ejemplo vale más que mil explicaciones::

    >>> def in_list(item: int, items: list[int]) -> bool:
    ...     return item in items
    ...

    >>> in_list(1, [1, 2, 3])
    True

    >>> 1 in [1, 2, 3]  # That easy!
    True

.. tip::
    La "funcionitis" es uno de los síntomas de la llamada "sobre-ingeniería" a la que tendemos muchas de las personas que hacemos programación. Hay que intentar evitarla en la medida de lo posible.

*******************
Espacios de nombres
*******************

Como bien indica el :ref:`Zen de Python <core/introduction/python:Zen de Python>`:

    *Namespaces are one honking great idea -- let's do more of those!*

Que vendría a traducirse como: "Los espacios de nombres son una gran idea -- hagamos más de eso". Los **espacios de nombres** permiten definir **ámbitos** o **contextos** en los que agrupar nombres de objetos.

Los espacios de nombres proporcionan un mecanismo de empaquetado, de tal forma que podamos tener incluso nombres iguales que no hacen referencia al mismo objeto (siempre y cuando estén en ámbitos distintos).

Cada *función* define su propio espacio de nombres y es diferente del espacio de nombres global aplicable a todo nuestro programa.

.. figure:: img/namespaces.png
    :align: center

    Espacio de nombres global vs espacios de nombres de funciones

Acceso a variables globales
===========================

Cuando una variable se define en el *espacio de nombres global* podemos hacer uso de ella con total transparencia dentro del ámbito de las funciones del programa::

    >>> language = 'castellano'

    >>> def catalonia():
    ...     print(f'{language=}')
    ...

    >>> language
    'castellano'

    >>> catalonia()
    language='castellano'

Creando variables locales
=========================

En el caso de que asignemos un valor a una variable global dentro de una función, no estaremos modificando ese valor. Por el contrario, estaremos creando una *variable en el espacio de nombres local*::

    >>> language = 'castellano'

    >>> def catalonia():
    ...     language = 'catalan'
    ...     print(f'{language=}')
    ...

    >>> language
    'castellano'

    >>> catalonia()
    language='catalan'

    >>> language
    'castellano'

Forzando modificación global
============================

Python nos permite modificar una variable definida en un espacio de nombres global dentro de una función. Para ello debemos usar el modificador ``global``::

    >>> language = 'castellano'

    >>> def catalonia():
    ...     global language
    ...     language  = 'catalan'
    ...     print(f'{language=}')
    ...

    >>> language
    'castellano'

    >>> catalonia()
    language='catalan'

    >>> language
    'catalan'

.. warning:: El uso de ``global`` no se considera una buena práctica ya que puede inducir a confusión y tener efectos colaterales indeseados.

Contenido de los espacios de nombres
====================================

Python proporciona dos funciones para acceder al contenido de los espacios de nombres:

``locals()``
    Devuelve un diccionario con los contenidos del **espacio de nombres local**::

        >>> language = 'castellano'

        >>> def catalonia():
        ...     language  = 'catalan'
        ...     print(f'{locals()=}')
        ...

        >>> catalonia()
        locals()={'language': 'catalan'}

``globals()``
    Devuelve un diccionario con los contenidos del **espacio de nombres global**::

        >>> globals()
        {'__name__': '__main__',
        '__doc__': 'Automatically created module for IPython interactive environment',
        '__package__': None,
        '__loader__': None,
        '__spec__': None,
        '__builtin__': <module 'builtins' (built-in)>,
        '__builtins__': <module 'builtins' (built-in)>,
        '_ih': ['',
        "language = 'castellano'",
        "def catalonia():\n    language  = 'catalan'\n    print(f'{locals()=}')\n    ",
        'language',
        'catalonia()',
        'globals()'],
        '_oh': {3: 'castellano'},
        '_dh': ['/Users/sdelquin'],
        'In': ['',
        "language = 'castellano'",
        "def catalonia():\n    language  = 'catalan'\n    print(f'{locals()=}')\n    ",
        'language',
        'catalonia()',
        'globals()'],
        'Out': {3: 'castellano'},
        'get_ipython': <bound method InteractiveShell.get_ipython of <IPython.terminal.interactiveshell.TerminalInteractiveShell object at 0x10e70c2e0>>,
        'exit': <IPython.core.autocall.ExitAutocall at 0x10e761070>,
        'quit': <IPython.core.autocall.ExitAutocall at 0x10e761070>,
        '_': 'castellano',
        '__': '',
        '___': '',
        'Prompts': IPython.terminal.prompts.Prompts,
        'Token': Token,
        'MyPrompt': __main__.MyPrompt,
        'ip': <IPython.terminal.interactiveshell.TerminalInteractiveShell at 0x10e70c2e0>,
        '_i': 'catalonia()',
        '_ii': 'language',
        '_iii': "def catalonia():\n    language  = 'catalan'\n    print(f'{locals()=}')\n    ",
        '_i1': "language = 'castellano'",
        'language': 'castellano',
        '_i2': "def catalonia():\n    language  = 'catalan'\n    print(f'{locals()=}')\n    ",
        'catalonia': <function __main__.catalonia()>,
        '_i3': 'language',
        '_3': 'castellano',
        '_i4': 'catalonia()',
        '_i5': 'globals()'}

***********************
Consejos para programar
***********************

**Chris Staudinger** comparte `estos 7 consejos <https://twitter.com/chrisstaud/status/1631919411236831235>`_ para mejorar tu código:

1. Las funciones deberían hacer una única cosa.
    *Por ejemplo, un mal diseño sería tener una única función que calcule el total de una cesta de la compra, los impuestos y los gastos de envío. Sin embargo esto se debería hacer con tres funciones separadas. Así conseguimos que el código sea más fácil de matener, reutilizar y depurar.*
2. Utiliza nombres descriptivos y con significado.
    *Los nombres autoexplicativos de variables y funciones mejoran la legibilidad del código. Por ejemplo -- deberíamos llamar "total_cost" a una variable que se usa para almacenar el total de un carrito de la compra en vez de "x" ya que claramente explica su propósito.*
3. No uses variables globales.
    *Las variables globales pueden introducir muchos problemas, incluyendo efectos colaterales inesperados y errores de programación difíciles de trazar. Supongamos que tenemos dos funciones que comparten una variable global. Si una función cambia su valor la otra función podría no funcionar como se espera.*
4. Refactorizar regularmente.
    *El código inevitablemente cambia con el tiempo, lo que puede derivar en partes obsoletas, redundantes o desorganizadas. Trata de mantener la calidad del código revisando y refactorizando aquellas zonas que se editan.*
5. No utilices "números mágicos" o valores "hard-codeados".
    *No es lo mismo escribir "99 * 3" que "price * quantity". Esto último es más fácil de entender y usa variables con nombres descriptivos haciéndolo autoexplicativo. Trata de usar constantes o variables en vez de valores "hard-codeados".*
6. Escribe lo que necesites ahora, no lo que pienses que podrías necesitar en el futuro.
    *Los programas simples y centrados en el problema son más flexibles y menos complejos.*
7. Usa comentarios para explicar el "por qué" y no el "qué".
    *El código limpio es autoexplicativo y por lo tanto los comentarios no deberían usarse para explicar lo que hace el código. En cambio, los comentarios debería usarse para proporcionar contexto adicional, como por qué el código está diseñado de una cierta manera.*

----

.. rubric:: EJERCICIOS DE REPASO

1. pycheck_: **num_in_interval**
2. pycheck_: **extract_evens**
3. pycheck_: **split_case**
4. pycheck_: **perfect**
5. pycheck_: **palindrome**
6. pycheck_: **count_vowels**
7. pycheck_: **pangram**
8. pycheck_: **cycle_alphabet**
9. pycheck_: **bubble_sort**
10. pycheck_: **consecutive_seq**
11. pycheck_: **magic_square**
12. pycheck_: **sum_nested**
13. pycheck_: **power_recursive**
14. pycheck_: **hyperfactorial**

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
.. [#naming-functions] Las :ref:`reglas aplicadas a nombres de variables <core/datatypes/data:Reglas para nombrar variables>` también se aplican a nombres de funciones.
.. [#or-types] Disponible a partir de Python 3.10.
.. [#range] La función ``range()`` es un tanto especial. Véase `este artículo de Trey Hunner <https://treyhunner.com/2018/02/python-range-is-not-an-iterator/>`_.
.. [#yield] Para una explicación detallada sobre generadores e iteradores se recomienda la ponencia `Yield el amigo que no sabías que tenías`_ de Jacobo de Vera.
.. [#guarda] Para más información sobre las cláusulas guarda, véase `este artículo de Miguel G. Flores <https://www.miguelg.com/2019/05/clausulas-guarda-en-python.html>`_

.. --------------- Hyperlinks ---------------

.. _Nathan Dumlao: https://unsplash.com/@nate_dumlao?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
.. _DocString Formats: https://realpython.com/documenting-python-code/#docstring-formats
.. _Programación funcional: https://es.wikipedia.org/wiki/Programaci%C3%B3n_funcional
.. _Modelo de datos: https://docs.python.org/es/3/reference/datamodel.html
.. _Sucesión de Fibonacci: https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci
.. _mypy: http://mypy-lang.org/
.. _syntactic sugar: https://es.wikipedia.org/wiki/Az%C3%BAcar_sint%C3%A1ctico
.. _reStructuredText docstrings: https://peps.python.org/pep-0287/
.. _Google docstrings: https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings
.. _reStructuredText: https://www.sphinx-doc.org/es/master/usage/restructuredtext/index.html
.. _NumPy-SciPy docstrings: https://numpydoc.readthedocs.io/en/latest/format.html
.. _Epytext docstrings: http://epydoc.sourceforge.net/epytext.html
.. _NumPy: https://numpy.org/
.. _Sphinx: https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html
.. _autodoc: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
.. _Read the Docs: https://readthedocs.org/
.. _Napoleon: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
.. _perfecto: https://es.wikipedia.org/wiki/N%C3%BAmero_perfecto
.. _palíndromo: https://es.wikipedia.org/wiki/Pal%C3%ADndromo
.. _pangrama: https://es.wikipedia.org/wiki/Pangrama
.. _pycheck: https://pycheck.es
.. _requests: https://requests.readthedocs.io/en/latest/api/
.. _Epydoc: https://epydoc.sourceforge.net/
.. _Yield el amigo que no sabías que tenías: https://www.youtube.com/watch?v=W-3wHM549gA
