###########
Excepciones
###########

.. image:: img/sarah-kilian-52jRtc2S_VE-unsplash.jpg

Una **excepción** es el bloque de código que se lanza cuando se produce un **error** en la ejecución de un programa Python. [#icecream-unsplash]_

De hecho ya hemos visto algunas de estas excepciones: accesos fuera de rango a listas o tuplas, accesos a claves inexistentes en diccionarios, etc. Cuando ejecutamos código que podría fallar bajo ciertas circunstancias, necesitamos también manejar, de manera adecuada, las excepciones que se generan.

*****************
Manejando errores
*****************

Si una excepción ocurre en algún lugar de nuestro programa y no es capturada en ese punto, va subiendo (burbujeando) hasta que es capturada en alguna función que ha hecho la llamada. Si en toda la "pila" de llamadas no existe un control de la excepción, Python muestra un mensaje de error con información adicional::

    >>> def intdiv(a: int, b: int) -> int:
    ...     return a // b
    ...

    >>> intdiv(3, 0)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 2, in intdiv
    ZeroDivisionError: integer division or modulo by zero

Para manejar (capturar) las excepciones podemos usar un bloque de código con las palabras reservadas ``try`` and ``except``::

    >>> def intdiv(a: int, b: int) -> int:
    ...     try:
    ...         return a // b
    ...     except:
    ...         print('Please do not divide by zero...')
    ...

    >>> intdiv(3, 0)
    Please do not divide by zero...

Aquel código que se encuentre dentro del bloque ``try`` se ejecutará normalmente siempre y cuando no haya un error. Si se produce una excepción, ésta será capturada por el bloque ``except``, ejecutándose el código que contiene.

.. hint:: No es una buena práctica usar un bloque ``except`` sin indicar el **tipo de excepción** que estamos gestionando, no sólo porque puedan existir varias excepciones que capturar sino porque, como dice el :ref:`Zen de Python <core/introduction/python:Zen de Python>`: "explícito" es mejor que "implícito".

La traza o **pila de llamadas** ("Traceback" en inglés) se muestra cada vez que se produce una excepción en nuestro programa y contiene todas las llamadas que han intervenido en el proceso. Dependiendo de lo anidado que esté el error, tendremos una traza más o menos grande::

    >>> def intdiv(a: int, b: int) -> int:
    ...     return a // b
    ...
    >>> def arithmetics():
    ...     return intdiv(3, 0)
    ...
    >>> def manage():
    ...     return arithmetics()
    ...
    >>> def main():
    ...     return manage()
    ...

    >>> main()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 2, in main
      File "<stdin>", line 2, in manage
      File "<stdin>", line 2, in arithmetics
      File "<stdin>", line 2, in intdiv
    ZeroDivisionError: integer division or modulo by zero

Especificando excepciones
=========================

En el siguiente ejemplo mejoraremos el código anterior, capturando distintos tipos de `excepciones predefinidas`_:

- ``TypeError`` por si los operandos no permiten la división.
- ``ZeroDivisionError`` por si el denominador es cero.
- ``Exception`` para cualquier otro error que se pueda producir.

Veamos su implementación::

    >>> def intdiv(a, b):
    ...     try:
    ...         result = a // b
    ...     except TypeError:
    ...         print('Check operands. Some of them seems strange...')
    ...     except ZeroDivisionError:
    ...         print('Please do not divide by zero...')
    ...     except Exception:
    ...         print('Ups. Something went wrong...')
    ...

    >>> intdiv(3, 0)
    Please do not divide by zero...

    >>> intdiv(3, '0')
    Check operands. Some of them seems strange...

Excepciones predefinidas
------------------------

Las `excepciones predefinidas`_ en Python cubren un amplio rango de posibilidades y *no hace falta importarlas previamente*. Se pueden usar directamente.

Conocerlas es importante ya que nos permitirá gestionar mejor los posibles errores y dar respuesta a situaciones inesperadas. Veamos a continuación algunas de las más relevantes:

.. csv-table::
    :file: tables/exceptions.csv
    :widths: 20, 60, 20
    :header-rows: 1
    :class: longtable

Agrupando excepciones
---------------------

Si nos interesa tratar distintas excepciones con el mismo comportamiento, es posible agruparlas en una única línea:

.. code-block::
    :emphasize-lines: 4

    >>> def intdiv(a, b):
    ...     try:
    ...         result = a // b
    ...     except (TypeError, ZeroDivisionError):
    ...         print('Check operands: Some of them caused errors...')
    ...     except Exception:
    ...         print('Ups. Something went wrong...')
    ...

    >>> intdiv(3, 0)
    Check operands: Some of them caused errors...

Variantes en el tratamiento
===========================

Python proporciona la cláusula ``else`` para saber que todo ha ido bien y que no se ha lanzado ninguna excepción. Esto es relevante a la hora de manejar los errores.

De igual modo, tenemos a nuestra disposición la cláusula ``finally`` que se ejecuta siempre, independientemente de si ha habido o no ha habido error.

Veamos un ejemplo de ambos::

    >>> values = [4, 2, 7]

    >>> try:
    ...     r = values[3]
    ... except IndexError:
    ...     print('Error: Index not in list')
    ... else:
    ...     print(f'Your wishes are my command: {r}')
    ... finally:
    ...     print('Have a good day!')
    ...
    Error: Index not in list
    Have a good day!

    >>> try:
    ...     r = values[2]
    ... except IndexError:
    ...     print('Error: Index not in list')
    ... else:
    ...     print(f'Your wishes are my command: {r}')
    ... finally:
    ...     print('Have a good day!')
    ...
    Your wishes are my command: 7
    Have a good day!

.. admonition:: Ejercicio
    :class: exercise

    Sabiendo que ``ValueError`` es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función ``getint()`` que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto.

    Ejecución a modo de ejemplo::

        Give me an integer number: ten
        Not a valid integer. Try it again!
        Give me an integer number: diez
        Not a valid integer. Try it again!
        Give me an integer number: 10

    Implemente:

    1. Versión iterativa en ``get_integers_iter.py``
    2. Versión recursiva en ``get_integers_recur.py``

Mostrando los errores
=====================

Además de capturar las excepciones podemos mostrar sus mensajes de error asociados. Para ello tendremos que hacer uso de la palabra reservada ``as`` junto a un nombre de variable que contendrá el objeto de la excepción.

Veamos este comportamiento siguiendo con el ejemplo anterior::

    >>> try:
    ...     print(values[3])
    ... except IndexError as err:
    ...     print(err)
    ...
    list index out of range

Una vez con la excepción capturada, ya podemos "elaborar" un poco más el mensaje de salida::

    >>> try:
    ...     print(values[3])
    ... except IndexError as err:
    ...     print(f'Something went wrong: {err}')
    ...
    Something went wrong: list index out of range

.. seealso::
    Este "alias" también es posible aplicarlo cuando :ref:`agrupamos excepciones <core/modularity/exceptions:agrupando excepciones>`.

Elevando excepciones
====================

Es habitual que nuestro programa tenga que lanzar (elevar o levantar) una excepción (predefinida o propia). Para ello tendremos que hacer uso de la sentencia ``raise``.

Supongamos una función que suma dos valores enteros. En el caso de que alguno de los operandos no sea entero, elevaremos una excepción indicando esta circunstancia:

.. code-block::
    :emphasize-lines: 4, 14

    >>> def _sum(a: int, b: int) -> int:
    ...     if isinstance(a, int) and isinstance(b, int):
    ...         return a + b
    ...     raise TypeError('Operands must be integers')
    ...

    >>> _sum(4, 3)  # todo normal
    7

    >>> _sum('x', 'y')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 4, in _sum
    TypeError: Operands must be integers

Jerarquía de excepciones
========================

Todas las excepciones predefinidas en Python heredan de la clase ``Exception`` y de la clase ``BaseException`` (más allá de heredar, obviamente, de ``object``).

Podemos visitar algunas :ref:`excepciones predefinidas <core/modularity/exceptions:excepciones predefinidas>` y comprobar este comportamiento::

    >>> TypeError.mro()
    [TypeError, Exception, BaseException, object]

    >>> ZeroDivisionError.mro()
    [ZeroDivisionError, ArithmeticError, Exception, BaseException, object]

    >>> IndexError.mro()
    [IndexError, LookupError, Exception, BaseException, object]

    >>> FileNotFoundError.mro()
    [FileNotFoundError, OSError, Exception, BaseException, object]

A continuación se detalla la **jerarquía completa de excepciones predefinidas** en Python::

    BaseException
    ├── BaseExceptionGroup
    ├── GeneratorExit
    ├── KeyboardInterrupt
    ├── SystemExit
    └── Exception
        ├── ArithmeticError
        │    ├── FloatingPointError
        │    ├── OverflowError
        │    └── ZeroDivisionError
        ├── AssertionError
        ├── AttributeError
        ├── BufferError
        ├── EOFError
        ├── ExceptionGroup [BaseExceptionGroup]
        ├── ImportError
        │    └── ModuleNotFoundError
        ├── LookupError
        │    ├── IndexError
        │    └── KeyError
        ├── MemoryError
        ├── NameError
        │    └── UnboundLocalError
        ├── OSError
        │    ├── BlockingIOError
        │    ├── ChildProcessError
        │    ├── ConnectionError
        │    │    ├── BrokenPipeError
        │    │    ├── ConnectionAbortedError
        │    │    ├── ConnectionRefusedError
        │    │    └── ConnectionResetError
        │    ├── FileExistsError
        │    ├── FileNotFoundError
        │    ├── InterruptedError
        │    ├── IsADirectoryError
        │    ├── NotADirectoryError
        │    ├── PermissionError
        │    ├── ProcessLookupError
        │    └── TimeoutError
        ├── ReferenceError
        ├── RuntimeError
        │    ├── NotImplementedError
        │    └── RecursionError
        ├── StopAsyncIteration
        ├── StopIteration
        ├── SyntaxError
        │    └── IndentationError
        │         └── TabError
        ├── SystemError
        ├── TypeError
        ├── ValueError
        │    └── UnicodeError
        │         ├── UnicodeDecodeError
        │         ├── UnicodeEncodeError
        │         └── UnicodeTranslateError
        └── Warning
            ├── BytesWarning
            ├── DeprecationWarning
            ├── EncodingWarning
            ├── FutureWarning
            ├── ImportWarning
            ├── PendingDeprecationWarning
            ├── ResourceWarning
            ├── RuntimeWarning
            ├── SyntaxWarning
            ├── UnicodeWarning
            └── UserWarning

.. tip::
    Si capturamos una clase base estaremos capturando todas sus clases derivadas. Esto no es cierto a la inversa.

*******************
Excepciones propias
*******************

Python ofrece una gran cantidad de `excepciones predefinidas`_. Hasta ahora hemos visto cómo gestionar y manejar este tipo de excepciones. Pero hay ocasiones en las que nos puede interesar crear nuestras propias excepciones. Para ello simplemente tendremos que crear una clase :ref:`heredando <core/modularity/oop:Herencia>` de ``Exception``, la clase base para todas las excepciones.

Veamos un ejemplo en el que creamos una excepción propia controlando que el valor sea un número entero:

.. code-block::
    :emphasize-lines: 9, 13

    >>> class NotIntError(Exception):
    ...     pass
    ...

    >>> values = (4, 7, 2.11, 9)

    >>> for value in values:
    ...     if not isinstance(value, int):
    ...         raise NotIntError(value)
    ...
    Traceback (most recent call last):
      File "<stdin>", line 3, in <module>
    NotIntError: 2.11

Hemos usado la sentencia ``raise`` para :ref:`elevar esta excepción <core/modularity/exceptions:elevando excepciones>`, que podría ser controlada en un nivel superior mediante un bloque ``try`` - ``except``.

.. note:: Para crear una excepción propia basta con crear una clase vacía. No es necesario incluir código más allá de un ``pass``.

Mensaje personalizado
=====================

Podemos personalizar la excepción propia añadiendo un mensaje como **valor por defecto**. Siguiendo el ejemplo anterior, veamos cómo introducimos esta información:

.. code-block::
    :emphasize-lines: 6,9

    >>> class NotIntError(Exception):
    ...     def __init__(self, message='This module only works with integers. Sorry!'):
    ...         super().__init__(message)
    ...

    >>> raise NotIntError()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NotIntError: This module only works with integers. Sorry!

Supongamos que queremos ir un paso más allá e **incorporar en el mensaje de la excepción el propio valor** que está generando el error:

.. code-block::
    :emphasize-lines: 14

    >>> class NotIntError(Exception):
    ...     def __init__(self, value, *, message='This module only works with integers. Sorry!'):
    ...         self.value = value
    ...         self.message = message
    ...         super().__init__(self.message)
    ...
    ...     def __str__(self):
    ...         return f'{self.value} -> {self.message}'
    ...

    >>> raise NotIntError(2.11)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NotIntError: 2.11 -> This module only works with integers. Sorry!

Y con esta misma configuración podemos **modificar el mensaje por defecto**:

.. code-block::
    :emphasize-lines: 4

    >>> raise NotIntError(2.11, message='Please use integers!')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NotIntError: 2.11 -> Please use integers!

.. note::
    Una excepción propia no es más que una clase ordinaria y, por tanto, admite cualquier tipo de parámetro en su constructor y resto de métodos. Si se usa con sentido puede ser una poderosa herramienta.

**No siempre es necesario** implementar el método ``__str__()``. Veamos una reescritura del código anterior::

    >>> class NotIntError(Exception):
    ...     def __init__(self, value, *, message='This module only works with integers. Sorry!'):
    ...         err_info = f'{value} -> {message}'
    ...         super().__init__(err_info)
    ...

Nos estamos apoyando en el hecho de que ``NotIntError`` hereda de ``Exception`` y esta clase base ya dispone de un método ``__str__()``. Podemos comprobar que su comportamiento es igual que antes::

    >>> raise NotIntError(2.11)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NotIntError: 2.11 -> This module only works with integers. Sorry!

    >>> raise NotIntError(2.11, message='Please use integers!')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NotIntError: 2.11 -> Please use integers!

**********
Aserciones
**********

Si hablamos de control de errores hay que citar una sentencia en Python denominada ``assert``. Esta sentencia nos permite comprobar si se están cumpliendo las "expectativas" de nuestro programa, y en caso contrario, lanza una excepción informativa.

Su sintaxis es muy simple. Únicamente tendremos que indicar una expresión de comparación después de la sentencia::

    >>> result = 10

    >>> assert result > 0

    >>> print(result)
    10

En el caso de que la condición se cumpla, no sucede nada: el programa continúa con su flujo normal. Esto es indicativo de que las expectativas que teníamos se han satisfecho.

Sin embargo, si la condición que fijamos no se cumpla, la aserción devuelve un error ``AssertionError`` y el programa interrupme su ejecución::

    >>> result = -1

    >>> assert result > 0
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AssertionError

Podemos observar que la excepción que se lanza no contiene ningún mensaje informativo. Es posible personalizar este mensaje añadiendo un segundo elemento en la :ref:`tupla <core/datastructures/tuples:tuplas>` de la aserción::

    >>> assert result > 0, 'El resultado debe ser positivo'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AssertionError: El resultado debe ser positivo

**********
Ejercicios
**********

1. Escriba una clase ``Card`` que represente una carta de poker y una clase ``InvalidCardError`` que represente un error propio indicando que la carta no es válida.

    | Plantilla: :download:`poker.py <files/templates/poker.py>`
    | Glifos de cartas: :download:`cards.dat <files/cards.dat>`
    | Comprobación: ``pytest -xq`` :download:`test_poker.py <files/test_poker.py>`

*********************
Ampliar conocimientos
*********************

- `Python Exceptions: An introduction <https://realpython.com/python-exceptions/>`_
- `Python KeyError Exceptions and How to Handle Them <https://realpython.com/python-keyerror/>`_
- `Understanding the Python Traceback <https://realpython.com/python-traceback/>`_


.. --------------- Footnotes ---------------

.. [#icecream-unsplash] Foto original por `Sarah Kilian`_ en Unsplash.

.. --------------- Hyperlinks ---------------

.. _Sarah Kilian: https://unsplash.com/@rojekilian?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
.. _excepciones predefinidas: https://docs.python.org/es/3/library/exceptions.html#concrete-exceptions
