*********
Funciones
*********

.. image:: img/nathan-dumlao-6Lh0bRb9LOA-unsplash.jpg

Hasta ahora todo lo que hemos hecho han sido breves fragmentos de código Python. Esto puede ser razonable para pequeñas tareas, pero nadie quiere reescribir los fragmentos de código cada vez. Necesitamos una manera de organizar nuestro código en piezas manejables. [#brewery-unsplash]_ 

El primer paso para la **reutilización de código** es la **función**. Se trata de un trozo de código con nombre y separado del resto. Puede tomar cualquier número y tipo de *parámetros* y devolver cualquier número y tipo de *resultados*. 

Básicamente podemos hacer dos cosas con una función:

- Definirla (con cero o más parámetros).
- Invocarla (y obtener cero o más resultados).

Definir una función
===================

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
~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~

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

Parámetros y argumentos
=======================

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
~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~

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

Documentación
=============

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

Explicación de parámetros
~~~~~~~~~~~~~~~~~~~~~~~~~

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

Espacios de nombres
===================

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

.. admonition:: Ejercicio
    :class: exercise

    .. rubric:: Primera parte

    Escriba una función ``factorial`` que reciba un único parámetro ``n`` y devuelva su factorial.

    *El factorial de un número n se define como*:
    
    .. math:: 
        n! = n \cdot (n - 1) \cdot (n - 2) \cdot \ldots \cdot 1
    
    **Ejemplo**
        * Entrada: ``5``
        * Salida: ``120``



.. rubric:: AMPLIAR CONOCIMIENTOS

- `Defining Your Own Python Function <https://realpython.com/defining-your-own-python-function/>`_
- `Python args and kwargs: Demystified <https://realpython.com/courses/python-kwargs-and-args/>`_
- `Documenting Python Code: A Complete Guide <https://realpython.com/courses/documenting-python-code/>`_
- `Thinking Recursively in Python <https://realpython.com/courses/thinking-recursively-python/>`_
- `Writing Comments in Python <https://realpython.com/courses/writing-comments-python/>`_



.. --------------- Footnotes ---------------

.. [#brewery-unsplash] Foto original por `Nathan Dumlao`_ en Unsplash.
.. [#blogic] Término para identificar el "algoritmo" o secuencia de instrucciones derivadas del procesamiento que corresponda.
.. [#docstring-formats] Véase `Docstring Formats`_.

.. --------------- Hyperlinks ---------------

.. _Nathan Dumlao: https://unsplash.com/@nate_dumlao?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
.. _DocString Formats: https://realpython.com/documenting-python-code/#docstring-formats
