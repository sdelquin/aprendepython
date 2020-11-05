###########
Excepciones
###########

.. image:: img/sarah-kilian-52jRtc2S_VE-unsplash.jpg

Una **excepción** es el código que se ejecuta cuando se produce un **error** en nuestro programa Python durante la fase de ejecución. [#icecream-unsplash]_

De hecho ya hemos visto algunas de estas excepciones: accesos fuera de rango a listas o tuplas, accesos a claves inexistentes en diccionarios, etc. Cuando ejecutamos código que podría fallar bajo ciertas circunstancias necesitamos también manejar las excepciones de manera adecuada.

*****************
Manejando errores
*****************

Si una excepción ocurre en algún lugar de nuestro programa y no es capturada en ese punto, va subiendo (burbujeando) hasta que es capturada en alguna función que ha hecho la llamada. Si en toda la "pila" de llamadas no existe un control de la excepción, Python muestra un mensaje de error con información adicional::

    >>> short_list = ['a', 'b', 'c']

    >>> short_list[5]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list index out of range

Para manejar (capturar) las excepciones podemos usar un bloque de código con las palabras reservadas ``try`` and ``except``::

    >>> short_list = ['a', 'b', 'c']
    >>> position = 5

    >>> try:
    ...     short_list[position]
    ... except:
    ...     print(f'Need a position between 0 and {len(short_list) - 1} but got {position}')
    ...
    Need a position between 0 and 2 but got 5

El código que está dentro del bloque ``try`` se ejecuta, si hay un error se "levanta" una excepción y se ejecuta el código que está dentro del bloque ``except``. En caso de que no hayan errores no se ejecuta el bloque ``except``.

.. hint:: No es una buena práctica usar un bloque ``except`` sin indicar el **tipo de excepción** que estamos gestionando, no sólo porque puedan existir varias excepciones que capturar sino porque, como dice el :ref:`Zen de Python <introduction/python:Zen de Python>`: "explícito" es mejor que "implícito".

Especificando excepciones
=========================

En el siguiente ejemplo mejoraremos el código anterior capturando, en primer lugar ``IndexError`` y luego capturando cualquier otra excepción que se pueda producir::

    >>> short_list = ['a', 'b', 'c']

    >>> while True:
    ...     value = input('Position [q to quit]? ')
    ...     if value == 'q':
    ...         break
    ...     try:
    ...         position = int(value)
    ...         print(short_list[position])
    ...     except IndexError as err:
    ...         print('Bad index:', position)
    ...     except Exception as other:
    ...         print('Something else broke:', other)
    ...
    Position [q to quit]? 0
    a
    Position [q to quit]? 1
    b
    Position [q to quit]? 2
    c
    Position [q to quit]? 100
    Bad index: 100
    Position [q to quit]? ciao
    Something else broke: invalid literal for int() with base 10: 'ciao'
    Position [q to quit]? q

*******************
Excepciones propias
*******************

|advlev|

Todas las excepciones que hemos visto hasta ahora estaban ya predefinidas en el propio lenguaje o en la librería estándar. Pero es posible crear **excepciones propias** para manejar situaciones especiales que podrían producirse en nuestro código.

Para crear una excepción propia debemos crear una clase que herede de ``Exception``. En principio, valdría con una clase vacía.

Veamos un ejemplo en el que crearemos una excepción propia controlando que una cadena de texto esté escrita en mayúsculas::

    >>> class UppercaseException(Exception):
    ...     pass
    ...

    >>> words = ['chocolate', 'milk', 'TEA', 'water']

    >>> for word in words:
    ...     if word.isupper():
    ...         raise UppercaseException(word)
    ...
    Traceback (most recent call last):
      File "<stdin>", line 3, in <module>
    __main__.UppercaseException: TEA

Hemos usado la sentencia ``raise`` para "elevar" esta excepción, que podría ser controlada en un nivel superior mediante un bloque ``try`` - ``except``.

Mensaje personalizado
=====================

Podemos personalizar la excepción añadiendo un mensaje más informativo. Siguiendo el ejemplo anterior, veamos cómo introducimos esta información::

    >>> class UppercaseException(Exception):
    ...     def __init__(self, message='Uppercase means shout. Please do not use it!'):
    ...         super().__init__(message)
    ...

    >>> raise UppercaseException()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    __main__.UppercaseException: Uppercase means shout. Please do not use it!

Podemos ir un paso más allá e incorporar en el mensaje la propia cadena de texto que está generando el error::

    >>> class UppercaseException(Exception):
    ...     def __init__(self, word, message='Uppercase means shout. Please do not use it!'):
    ...         self.word = word
    ...         self.message = message
    ...         super().__init__(self.message)
    ...
    ...     def __str__(self):
    ...         return f'{self.word} -> {self.message}'
    ...
    >>> raise UppercaseException('TEA')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    __main__.UppercaseException: TEA -> Uppercase means shout. Please do not use it!

.. rubric:: AMPLIAR CONOCIMIENTOS

- `Python Exceptions: An introduction <https://realpython.com/python-exceptions/>`_
- `Python KeyError Exceptions and How to Handle Them <https://realpython.com/python-keyerror/>`_
- `Understanding the Python Traceback <https://realpython.com/python-traceback/>`_



.. --------------- Footnotes ---------------

.. [#icecream-unsplash] Foto original por `Sarah Kilian`_ en Unsplash.

.. --------------- Hyperlinks ---------------

.. _Sarah Kilian: https://unsplash.com/@rojekilian?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
