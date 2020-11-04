################
Cadenas de texto
################

.. image:: img/roman-kraft-_Zua2hyvTBk-unsplash.jpg

Los "strings" o cadenas de texto son el primer ejemplo de *secuencia* en Python. En concreto se trata de una **secuencia de caracteres**. Un carácter es la mínima unidad en un sistema de escritura e incluye letras, dígitos, símbolos, signos de puntuación e incluso espacios en blanco o directivas. [#newspaper-unsplash]_

*****************
Creando "strings"
*****************

Para escribir una cadena de texto en Python basta con rodear los caracteres con comillas simples::

    >>> 'Mi primera cadena en Python'
    'Mi primera cadena en Python'

Para incluir *comillas dobles* dentro de la cadena de texto no hay mayor inconveniente:

    >>> 'Los llamados "strings" son secuencias de caracteres'
    'Los llamados "strings" son secuencias de caracteres'

Puede surgir la duda de cómo incluimos *comillas simples* dentro de la propia cadena de texto. Veamos soluciones para ello:

.. code-block::
    :emphasize-lines: 1, 3

    >>> 'Los llamados \'strings\' son secuencias de caracteres'
    "Los llamados 'strings' son secuencias de caracteres"
    >>> "Los llamados 'strings' son secuencias de caracteres"
    "Los llamados 'strings' son secuencias de caracteres"

En la primera opción estamos **escapando** las comillas simples para que no sean tratadas como caracteres especiales. En la segunda opción estamos creando el "string" con comillas dobles (por fuera) para poder incluir directamente las comillas simples (por dentro). Python también nos ofrece esta posibilidad.

Comillas triples
================

Hay una forma alternativa de crear cadenas de texto utilizando *comillas triples*. Su uso está pensado principalmente para **cadenas multilínea**::

    >>> poem = '''To be, or not to be, that is the question:
    ... Whether 'tis nobler in the mind to suffer
    ... The slings and arrows of outrageous fortune,
    ... Or to take arms against a sea of troubles'''

.. important:: Los tres puntos ``...`` que aparecen a la izquierda de las líneas no están incluidos en la cadena de texto. Es el símbolo que ofrece el intérprete de Python cuando saltamos de línea.

Cadena vacía
============

La cadena vacía es aquella que no tiene caracteres pero es perfectamente válida. Aunque a priori no lo pueda parecer, es un recurso importante en cualquier código. Su representación en Python es la siguiente:

    >>> ''
    ''

**********
Conversión
**********

Podemos crear "strings" a partir de otros tipos de datos usando la función ``str()``::

    >>> str(True)
    'True'
    >>> str(10)
    '10'
    >>> str(21.7)
    '21.7'

********************
Secuencias de escape
********************

Python permite **escapar** el significado de algunos caracteres para conseguir otros resultados. Si escribimos una barra invertida ``\`` antes del caracter en cuestión, le otorgamos un significado especial.

Quizás la *secuencia de escape* más conocida es ``\n`` que representa un *salto de línea*, pero existen muchas otras::

    # Salto de línea
    >>> msg = 'Primera línea\nSegunda línea\nTercera línea'
    >>> print(msg)
    Primera línea
    Segunda línea
    Tercera línea

    # Tabulador
    >>> msg = 'Valor = \t40'
    >>> print(msg)
    Valor = 	40

    # Comilla simple
    >>> msg = 'Necesitamos \'escapar\' la comilla simple'
    >>> print(msg)
    Necesitamos 'escapar' la comilla simple

    # Barra invertida
    >>> msg = 'Capítulo \\ Sección \\ Encabezado'
    >>> print(msg)
    Capítulo \ Sección \ Encabezado

.. note:: Es cuando utilizamos la función ``print()`` que vemos el resultado de utilizar los caracteres escapados.
    
Expresiones literales
=====================

|intlev|

Hay situaciones en las que nos interesa que los caracteres especiales pierdan ese significado y poder usarlos de otra manera. Existe un modificar de cadena que proporciona Python para tratar el texto *en bruto*. Es el llamado "raw data" y se aplica anteponiendo una ``r`` a la cadena de texto.

Veamos algunos ejemplos::

    >>> text = 'abc\ndef'
    >>> print(text)
    abc
    def

    >>> text = r'abc\ndef'
    >>> print(text)
    abc\ndef

    >>> text = 'a\tb\tc'
    >>> print(text)
    a    b    c

    >>> text = r'a\tb\tc'
    >>> print(text)
    a\tb\tc

.. hint:: El modificador ``r''`` es muy utilizado para la escritura de **expresiones regulares**.

*********************
Más sobre ``print()``
*********************

Hemos estado utilizando la función ``print()`` de forma sencilla, pero admite `algunos parámetros <https://docs.python.org/es/3/library/functions.html#print>`_ interesantes:

.. code-block::
    :emphasize-lines: 4, 7, 10
    :linenos:

    >>> msg1 = '¿Sabes por qué estoy acá?'
    >>> msg2 = 'Porque me apasiona'

    >>> print(msg1, msg2)
    ¿Sabes por qué estoy acá? Porque me apasiona

    >>> print(msg1, msg2, sep='|')
    ¿Sabes por qué estoy acá?|Porque me apasiona

    >>> print(msg2, end='!!')
    Porque me apasiona!!

*Línea 4:*
    Podemos imprimir todas las variables que queramos separándolas por comas.
*Línea 7:*
    El *separador por defecto* entre las variables es un *espacio*, podemos cambiar el caracter que se utiliza como separador entre cadenas.
*Línea 10:*
    El *carácter de final de texto* es un *salto de línea*, podemos cambiar el caracter que se utiliza como final de texto.

************************
Leer datos desde teclado
************************

Los programas se hacen para tener interacción con el usuario. Una de las formas de interacción es solicitar la entrada de datos por teclado. Como muchos otros lenguajes de programación, Python también nos ofrece la posibilidad de leer la información introducida por teclado. Para ello se utiliza la función ``input()``:

    >>> name = input('Introduzca su nombre: ')
    Introduzca su nombre: Sergio
    >>> name
    'Sergio'
    >>> age = input('Introduzca su edad: ')
    Introduzca su edad: 41
    >>> age
    '41'
    >>> type(age)
    <class 'str'>

.. note:: La función ``input()`` siempre nos devuelve un objeto de tipo cadena de texto o ``str``. Tenerlo muy en cuenta a la hora de trabajar con números, ya que debemos realizar una :ref:`conversión explícita <datatypes/numbers:Conversión explícita>`.

*************************
Operaciones con "strings"
*************************

Combinar cadenas
================

Podemos combinar dos o más cadenas de texto utilizando el operador ``+``::

    >>> proverb1 = 'Cuando el río suena'
    >>> proverb2 = 'agua lleva'
    >>> proverb1 + proverb2
    'Cuando el río suenaagua lleva'

    >>> proverb1 + ', ' + proverb2  # incluimos una coma
    'Cuando el río suena, agua lleva'

Repetir cadenas
===============

Podemos repetir dos o más cadenas de texto utilizando el operador ``*``::

    >>> reaction = 'Wow'
    >>> reaction * 4
    'WowWowWowWow'

Obtener un caracter
===================

Los "strings" están **indexados** y cada caracter tiene su posición propia. Para obtener un único caracter dentro de una cadena de texto es necesario especificar su **índice** dentro de corchetes ``[...]``.

.. figure:: img/string-indexing.png

   Indexado de una cadena de texto

Veamos algunos ejemplos de acceso a caracteres:

    >>> sentence = 'Hola, Mundo'

    >>> sentence[0]
    'H'
    >>> sentence[-1]
    'o'
    >>> sentence[4]
    ','
    >>> sentence[-5]
    'M'

.. note:: Nótese que existen tanto **índices positivos** como **índices negativos** para acceder a cada caracter de la cadena de texto. A priori puede parecer redundante, pero es muy útil para determinados casos.

En caso de que intentemos acceder a un índice que no existe, obtendremos un error por *fuera de rango*:

    >>> sentence[100]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: string index out of range

.. warning:: Téngase en cuenta que el indexado de una cadena de texto siempre empieza en **0** y termina en **una unidad menos de la longitud** de la cadena.

Las cadenas de texto son tipos de datos **inmutables**. Es por ello que no podemos modificar un caracter directamente::

    >>> song = 'Hey Jude'

    >>> song[4] = 'D'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'str' object does not support item assignment

.. tip:: Existen formas de modificar una cadena de texto que veremos más adelante, aunque realmente no estemos transformando el original sino que se crea un nuevo objeto con las modificaciones.

Trocear una cadena
==================

Es posible extraer "trozos" ("rebanadas") de una cadena de texto [#slice]_. Tenemos varias aproximaciones a ello:

``[:]``
    Extrae la secuencia entera desde el comienzo hasta el final. Es una especia de **copia** de toda la cadena de texto.
``[start:]``
    Extrae desde ``start`` hasta el final de la cadena.
``[:end]``
    Extrae desde el comienzo de la cadena hasta ``end`` *menos 1*.
``[start:end]``
    Extrae desde ``start`` hasta ``end`` *menos 1*.
``[start:end:step]``
    Extrae desde ``start`` hasta ``end`` *menos 1* haciendo saltos de tamaño ``step``.

Veamos la aplicación de cada uno de estos accesos a través de un ejemplo::

    >>> proverb = 'Agua pasada no mueve molino'

    >>> proverb[:]
    'Agua pasada no mueve molino'
    >>> proverb[12:]
    'no mueve molino'
    >>> proverb[:11]
    'Agua pasada'
    >>> proverb[5:11]
    'pasada'
    >>> proverb[5:11:2]
    'psd'

.. important:: El troceado siempre llega a una unidad menos del índice final que hayamos especificado. Sin embargo el comienzo sí coincide con el que hemos puesto.

Longitud de una cadena
======================

Para obtener la longitud de una cadena podemos hacer uso de ``len()`` que es una de las funciones "built-in" [#built-in]_ que ofrece Python::

    >>> proberb = 'Lo cortés no quita lo valiente'
    >>> len(proverb)
    27
    >>> empty = ''
    >>> len(empty)
    0

Dividir una cadena
==================

A contrario que ``len()`` algunas funciones son específicas de "strings". Para usar una función de cadena es necesario escribir el nombre del "string", un punto y el nombre de la función, pasando cualquier *argumento* necesario::

    >>> proverb = 'No hay mal que por bien no venga'
    >>> proverb.split()
    ['No', 'hay', 'mal', 'que', 'por', 'bien', 'no', 'venga']
    >>> tools = 'Martillo,Sierra,Destornillador'
    >>> tools.split(',')
    ['Martillo', 'Sierra', 'Destornillador']

.. note:: Si no se especifica un separador, ``split()`` usa por defecto cualquier secuencia de espacios en blanco, tabuladores y saltos de línea.

Aunque aún no lo hemos visto, lo que devuelve ``split()`` es una **lista** (otro tipo de datos en Python) donde cada elemento es una parte de la cadena de texto original.

.. admonition:: Ejercicio
    :class: exercise

    Obtenga el número de palabras que contiene la siguiente cadena de texto::

        quote = 'Before software can be reusable, it first has to be usable'
    
    .. only:: html
    
        |solution| :download:`num_words.py <files/num_words.py>`

Limpiar cadenas
===============

Cuando leemos datos del usuario o de cualquier fuente externa de información, es bastante probable que se incluyan en esas cadenas de texto, *caracteres de relleno* [#padding]_ al comienzo y al final. Python nos ofrece la posibilidad de eliminar estos caracteres u otros que no nos interesen.

La función ``strip()`` se utiliza para eliminar caracteres del principio y final del "string". También existen variantes de esta función para aplicarla únicamente al comienzo o al final de la cadena de texto:

Supongamos que debemos procesar un fichero con números de serie de un determinado artículo. Cada línea contiene el valor que nos interesa pero se han "colado" ciertos caracteres de relleno que debemos limpiar::

    >>> serial_number = '\n\t   \n 48374983274832    \n\n\t   \t   \n'
    >>> serial_number.strip()
    '48374983274832'

.. note:: Si no se especifican los caracteres a eliminar, ``strip()`` usa por defecto cualquier combinación de *espacios en blanco*, *saltos de línea* ``\n`` y *tabuladores* ``\t``.

A continuación vamos a hacer "limpieza" por la izquierda (*comienzo*) y por la derecha (*final*) utilizando la función ``lstrip()`` y ``rstrip()`` respectivamente::

    >>> serial_number.lstrip()  # left strip
    '48374983274832    \n\n\t   \t   \n'
    >>> serial_number.rstrip()  # right strip
    '\n\t   \n 48374983274832'

Como habíamos comentado, también existe la posibilidad de especificar los caracteres que queremos borrar::

    >>> serial_number.strip('\n')
    '\t   \n 48374983274832    \n\n\t   \t   '

.. important:: La función ``strip()`` no modifica la cadena que estamos usando (*algo obvio porque los "strings" son inmutables*) sino que devuelve una nueva cadena de texto con las modificaciones pertinentes.

Realizar búsquedas
==================

Veamos aquellas funciones que proporciona Python para la búsqueda en cadenas de texto. Vamos a partir de una variable que contiene un trozo de la canción `Mediterráneo`_ de *Joan Manuel Serrat*::

    >>> lyrics = '''Quizás porque mi niñez
    ... Sigue jugando en tu playa
    ... Y escondido tras las cañas
    ... Duerme mi primer amor
    ... Llevo tu luz y tu olor
    ... Por dondequiera que vaya'''

Comprobar si una cadena de texto **empieza o termina por alguna subcadena**::

    >>> lyrics.startswith('Quizás')
    True
    >>> lyrics.endswith('Final')
    False

Encontrar la **primera ocurrencia** de alguna subcadena::

    >>> lyrics.find('amor')
    93
    >>> lyrics.index('amor')
    93

Tanto ``find()`` como ``index()`` devuelven el **índice** de la primera ocurrencia de la subcadena que estemos buscando, pero se diferencian en su comportamiento cuando la subcadena buscada no existe::

    >>> lyrics.find('universo')
    -1
    >>> lyrics.index('universo')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: substring not found
    >>>

Contabilizar el **número de veces que aparece** una subcadena::

    >>> lyrics.count('mi')
    2
    >>> lyrics.count('tu')
    3
    >>> lyrics.count('él')
    0

.. admonition:: Ejercicio
    :class: exercise

    Dada la siguiente letra [#tenerife-sea]_, obtenga la misma pero sustituyendo la palabra ``voices`` por ``sounds``:

        >>> song = '''You look so beautiful in this light
        ... Your silhouette over me
        ... The way it brings out the blue in your eyes
        ... Is the Tenerife sea
        ... And all of the voices surrounding us here
        ... They just fade out when you take a breath
        ... Just say the word and I will disappear
        ... Into the wilderness'''

    Utilice para ello únicamente búsqueda, concatenación y troceado de cadenas de texto.

    .. only:: html
    
        |solution| :download:`replace.py <files/replace.py>`

Reemplazar elementos
====================

Podemos usar la función ``replace()`` indicando la *subcadena a reemplazar*, la *subcadena de reemplazo* y *cuántas instancias* se deben reemplazar. Si no se especifica este último argumento, la sustitución se hará en todas las instancias encontradas::

    >>> proverb = 'Quien mal anda mal acaba'

    >>> proverb.replace('mal', 'bien')
    'Quien bien anda bien acaba'

    >>> proverb.replace('mal', 'bien', 1)  # sólo 1 reemplazo
    'Quien bien anda mal acaba'

Mayúsculas y minúsculas
=======================

Python nos permite realizar variaciones en los caracteres de una cadena de texto para pasarlos a mayúsculas y/o minúsculas. Veamos las distintas opciones disponibles::

    >>> proverb = 'quien a buen árbol se arrima Buena Sombra le cobija'

    >>> proverb
    'quien a buen árbol se arrima Buena Sombra le cobija'

    >>> proverb.capitalize()
    'Quien a buen árbol se arrima buena sombra le cobija'
    
    >>> proverb.title()
    'Quien A Buen Árbol Se Arrima Buena Sombra Le Cobija'
    
    >>> proverb.upper()
    'QUIEN A BUEN ÁRBOL SE ARRIMA BUENA SOMBRA LE COBIJA'
    
    >>> proverb.lower()
    'quien a buen árbol se arrima buena sombra le cobija'
    
    >>> proverb.swapcase()
    'QUIEN A BUEN ÁRBOL SE ARRIMA bUENA sOMBRA LE COBIJA'

************************
Interpolación de cadenas
************************

En este apartado veremos cómo **interpolar** valores dentro de cadenas utilizando diferentes formatos. Interpolar (en este contexto) significa sustituir una variable por su valor dentro de una cadena de texto.

Veamos los estilos que proporciona Python para este cometido:

+----------------+-------------+--------------+
|     Nombre     |   Símbolo   |   Soportado  |
+================+=============+==============+
| Estilo antiguo | ``%``       | >= Python2   |
+----------------+-------------+--------------+
| Estilo "nuevo" | ``.format`` | >= Python2.6 |
+----------------+-------------+--------------+
| "f-strings"    | ``f''``     | >= Python3.6 |
+----------------+-------------+--------------+

Aunque aún podemos encontrar código con el `estilo antiguo y el estilo nuevo en el formateo de cadenas <https://pyformat.info/>`_, vamos a centrarnos en el análisis de los **"f-strings"** que se están utilizando bastante en la actualidad.

"f-strings"
===========

Los **f-strings** `aparecieron en Python 3.6 <https://docs.python.org/3/whatsnew/3.6.html#new-features>`_ y se suelen usar en código de nueva creación. Es la forma más potente -- y en muchas ocasiones más eficiente -- de formar cadenas de texto incluyendo valores de otras variables.

La **interpolación** en cadenas de texto es un concepto que existe en la gran mayoría de lenguajes de programación y hace referencia al hecho de sustituir los nombres de variables por sus valores a la hora de construir un "string".

Para indicar en Python que una cadena es un "f-string" basta con precederla con una ``f`` e incluir las variables o expresiones a interpolar entre llaves ``{...}``.

Supongamos que disponemos de los datos de una persona y queremos formar una frase de bienvenida con ellos::

    >>> name = 'Elon Musk'
    >>> age = 49
    >>> fortune = 43_300

    >>> f'Me llamo {name}, tengo {age} años y una fortuna de {fortune} millones'
    'Me llamo Elon Musk, tengo 49 años y una fortuna de 43300 millones'

.. warning:: Si olvidamos poner la **f** delante del "string" no conseguiremos sustitución de variables.

Podría surgir la duda de cómo incluir llaves dentro de la cadena de texto, teniendo en cuenta que las llaves son símbolos especiales para la interpolación de variables. La respuesta es duplicar las llaves::

    >>> x = 10

    >>> f'The variable is {{ x = {x} }}'
    'The variable is { x = 10 }'

Formateando cadenas
-------------------

|intlev|

Los "f-strings" proporcionan una gran variedad de **opciones de formateado**: ancho del texto, número de decimales, tamaño de la cifra, alineación, etc. Muchas de estas facilidades se pueden consultar en el artículo `Best of Python3.6 f-strings`_ [#best-fstrings]_

**Dando formato a valores enteros:**

.. code-block::

    >>> mount_height = 3718

    >>> f'{mount_height:10d}'
    '      3718'

    >>> f'{mount_height:010d}'
    '0000003718'

**Dando formato a otras bases:**

.. code-block::

    >>> value = 0b10010011
    >>> f'{value}'
    '147'
    >>> f'{value:b}'
    '10010011'

    >>> value = 0o47622
    >>> f'{value}'
    '20370'
    >>> f'{value:o}'
    '47622'

    >>> value = 0xab217
    >>> f'{value}'
    '700951'
    >>> f'{value:x}'
    'ab217'

**Dando formato a valores flotantes:**

.. code-block::

    >>> pi = 3.14159265

    >>> f'{pi:f}'
    '3.141593'

    >>> f'{pi:.3f}'
    '3.142'

    >>> f'{pi:12f}'
    '    3.141593'

    >>> f'{pi:7.2f}'
    '   3.14'

    >>> f'{pi:07.2f}'
    '0003.14'

    >>> f'{pi:.010f}'
    '3.1415926500'

    >>> f'{pi:e}'
    '3.141593e+00'

**Alineando valores:**

.. code-block::

    >>> text1 = 'how'
    >>> text2 = 'are'
    >>> text3 = 'you'

    >>> f'{text1:<7s}|{text2:^11s}|{text3:>7s}'
    'how    |    are    |    you'

    >>> f'{text1:-<7s}|{text2:·^11s}|{text3:->7s}'
    'how----|····are····|----you'

Modo "debug"
------------

A partir de Python 3.8, los "f-strings" permiten imprimir el nombre de la variable y su valor, como un atajo para depurar nuestro código. Para ello sólo tenemos que incluir un símbolo ``=`` después del nombre de la variable::

    >>> serie = 'The Simpsons'
    >>> imdb_rating = 8.7
    >>> num_seasons = 30

    >>> f'{serie=}'
    "serie='The Simpsons'"

    >>> f'{imdb_rating=}'
    'imdb_rating=8.7'

    >>> f'{serie[4:]=}'  # incluso podemos añadir expresiones!
    "serie[4:]='Simpsons'"

    >>> f'{imdb_rating / num_seasons=}'
    'imdb_rating / num_seasons=0.29'

.. admonition:: Ejercicio
    :class: exercise

    Dada la variable::

        e = 2.71828
    
    , obtenga los siguientes resultados utilizando "f-strings"::

        '2.718'
        '    2.72'
        '2.718280e+00'
        '00002.7183'
        '            2.71828'

    .. only:: html
    
        |solution| :download:`fstrings.py <files/fstrings.py>`

.. rubric:: AMPLIAR CONOCIMIENTOS

* `A Guide to the Newer Python String Format Techniques <https://realpython.com/python-formatted-output/>`_
* `Strings and Character Data in Python <https://realpython.com/courses/python-strings/>`_
* `How to Convert a Python String to int <https://realpython.com/convert-python-string-to-int/>`_
* `Your Guide to the Python print<> Function <https://realpython.com/python-print/>`_
* `Basic Input, Output, and String Formatting in Python <https://realpython.com/python-input-output/>`_
* `Unicode & Character Encodings in Python: A Painless Guide <https://realpython.com/python-encodings-guide/>`_
* `Python String Formatting Tips & Best Practices <https://realpython.com/courses/python-string-formatting-tips-best-practices/>`_
* `Python 3's f-Strings: An Improved String Formatting Syntax <https://realpython.com/courses/python-3-f-strings-improved-string-formatting-syntax/>`_
* `Splitting, Concatenating, and Joining Strings in Python <https://realpython.com/courses/splitting-concatenating-and-joining-strings-python/>`_
* `Conditional Statements in Python <https://realpython.com/python-conditional-statements/>`_
* `Python String Formatting Best Practices <https://realpython.com/python-string-formatting/>`_



.. --------------- Footnotes ---------------

.. [#newspaper-unsplash] Foto original de portada por `Roman Kraft`_ en Unsplash.
.. [#slice] El término usado en inglés es *slice*.
.. [#built-in] Término inglés para referirse a algo que ya está incorporado por defecto con el lenguaje de programación.
.. [#padding] Se suele utilizar el término inglés "padding" para referirse a estos caracteres.
.. [#best-fstrings] Escrito por Nirant Kasliwal en Medium.
.. [#tenerife-sea] "Tenerife Sea" por Ed Sheeran.

.. --------------- Hyperlinks ---------------

.. _Roman Kraft: https://unsplash.com/@romankraft?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
.. _Mediterráneo: https://open.spotify.com/track/7Bewui7KtaMzROeteRitRz?si=NGwOUmwfRSuapY3JL7s1uQ
.. _Best of Python3.6 f-strings: https://medium.com/@NirantK/best-of-python3-6-f-strings-41f9154983e
