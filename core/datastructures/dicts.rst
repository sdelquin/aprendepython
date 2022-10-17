############
Diccionarios
############

.. image:: img/aaron-burden-fgmf2Eyrwm4-unsplash.jpg


Podemos trasladar el concepto de *diccionario* de la vida real al de *diccionario* en Python. Al fin y al cabo un diccionario es un objeto que contiene palabras, y cada palabra tiene asociado un significado. Haciendo el paralelismo, diríamos que en Python un diccionario es también un objeto indexado por **claves** (las palabras) que tienen asociados unos **valores** (los significados). [#dict-unsplash]_


.. figure:: img/dicts.jpg
    :align: center

    Analogía de un diccionario en Python

Los diccionarios en Python tienen las siguientes *características*:

* Mantienen el **orden** en el que se insertan las claves. [#keep-order]_
* Son **mutables**, con lo que admiten añadir, borrar y modificar sus elementos.
* Las **claves** deben ser **únicas**. A menudo se utilizan las *cadenas de texto* como claves, pero en realidad podría ser cualquier tipo de datos inmutable: enteros, flotantes, tuplas (entre otros).
* Tienen un **acceso muy rápido** a sus elementos, debido a la forma en la que están implementados internamente. [#time-complexity]_

.. note:: En otros lenguajes de programación, a los diccionarios se les conoce como *arrays asociativos*, *"hashes"* o *"hashmaps"*.

********************
Creando diccionarios
********************

Para crear un diccionario usamos llaves ``{}`` rodeando asignaciones ``clave: valor`` que están separadas por comas. Veamos algunos ejemplos de diccionarios::

    >>> empty_dict = {}

    >>> rae = {
    ...     'bifronte': 'De dos frentes o dos caras',
    ...     'anarcoide': 'Que tiende al desorden',
    ...     'montuvio': 'Campesino de la costa'
    ... }

    >>> population_can = {
    ...     2015: 2_135_209,
    ...     2016: 2_154_924,
    ...     2017: 2_177_048,
    ...     2018: 2_206_901,
    ...     2019: 2_220_270
    ... }

En el código anterior podemos observar la creación de un diccionario vacío, otro donde sus claves y sus valores son cadenas de texto y otro donde las claves y los valores son valores enteros.

Ejecución **paso a paso** a través de *Python Tutor*:

.. only:: latex

    https://cutt.ly/Sfav2Yw


.. only:: html

    .. raw:: html

        <iframe width="800" height="585" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=empty_dict%20%3D%20%7B%7D%0A%0Arae%20%3D%20%7B%0A%20%20%20%20'bifronte'%3A%20'De%20dos%20frentes%20o%20dos%20caras',%0A%20%20%20%20'anarcoide'%3A%20'Que%20tiende%20al%20desorden',%0A%20%20%20%20'montuvio'%3A%20'Campesino%20de%20la%20costa'%0A%7D%0A%0Apopulation_can%20%3D%20%7B%0A%20%20%20%202015%3A%202_135_209,%0A%20%20%20%202016%3A%202_154_924,%0A%20%20%20%202017%3A%202_177_048,%0A%20%20%20%202018%3A%202_206_901,%0A%20%20%20%202019%3A%202_220_270%0A%7D&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

.. admonition:: Ejercicio
    :class: exercise

    Cree un diccionario con los nombres de 5 personas de su familia y sus edades.

    .. only:: html
    
        |solution| :download:`family_dict.py <files/family_dict.py>`

**********
Conversión
**********

Para convertir otros tipos de datos en un diccionario podemos usar la función ``dict()``::

    >>> # Diccionario a partir de una lista de cadenas de texto
    >>> dict(['a1', 'b2'])
    {'a': '1', 'b': '2'}

    >>> # Diccionario a partir de una tupla de cadenas de texto
    >>> dict(('a1', 'b2'))
    {'a': '1', 'b': '2'}

    >>> # Diccionario a partir de una lista de listas
    >>> dict([['a', 1], ['b', 2]])
    {'a': 1, 'b': 2}

.. note:: Si nos fijamos bien, cualquier iterable que tenga una estructura interna de 2 elementos es susceptible de convertirse en un diccionario a través de la función ``dict()``.

Diccionario vacío
=================

Existe una manera particular de usar ``dict()`` y es no pasarle ningún argumento. En este caso estaremos queriendo convertir el "vacío" en un diccionario, con lo que obtendremos un *diccionario vacío*::

    >>> dict()
    {}

.. tip:: Para crear un diccionario vacío, se suele recomendar el uso de ``{}`` frente a ``dict()``, no sólo por ser más *pitónico* sino por tener (en promedio) un mejor rendimiento en tiempos de ejecución.

Creación con ``dict()``
=======================

También es posible utilizar la función ``dict()`` para crear dicionarios y no tener que utilizar llaves y comillas:

Supongamos que queremos transformar la siguiente tabla en un diccionario:

+-------------+----------------+
|  Atributo   |     Valor      |
+=============+================+
|  ``name``   |     Guido      |
+-------------+----------------+
| ``surname`` | Van Rossum     |
+-------------+----------------+
| ``job``     | Python creator |
+-------------+----------------+

Utilizando la construcción mediante ``dict`` podemos pasar clave y valor como **argumentos** de la función::

    >>> person = dict(
    ...     name='Guido',
    ...     surname='Van Rossum',
    ...     job='Python creator'
    ... )

    >>> person
    {'name': 'Guido', 'surname': 'Van Rossum', 'job': 'Python creator'}

El inconveniente que tiene esta aproximación es que las **claves deben ser identificadores válidos** en Python. Por ejemplo, no se permiten espacios::

    >>> person = dict(
    ...     name='Guido van Rossum',
    ...     date of birth='31/01/1956'
      File "<stdin>", line 3
        date of birth='31/01/1956'
              ^
    SyntaxError: invalid syntax

|intlev|

Es posible crear un diccionario especificando sus claves y un único valor de "relleno"::

    >>> dict.fromkeys('aeiou', 0)
    {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

.. note::
    Es válido pasar cualquier "iterable" como referencia a las claves.

****************************
Operaciones con diccionarios
****************************

Obtener un elemento
===================

Para obtener un elemento de un diccionario basta con escribir la **clave** entre corchetes. Veamos un ejemplo:

.. code-block::
    :emphasize-lines: 7

    >>> rae = {
    ...     'bifronte': 'De dos frentes o dos caras',
    ...     'anarcoide': 'Que tiende al desorden',
    ...     'montuvio': 'Campesino de la costa'
    ... }

    >>> rae['anarcoide']
    'Que tiende al desorden'

Si intentamos acceder a una clave que no existe, obtendremos un error::

    >>> rae['acceso']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'acceso'

Usando ``get()``
----------------

Existe una función muy útil para "superar" los posibles errores de acceso por claves inexistentes. Se trata de ``get()`` y su comportamiento es el siguiente:

1. Si la clave que buscamos existe, nos devuelve su valor.
2. Si la clave que buscamos no existe, nos devuelve ``None`` [#none]_ salvo que le indiquemos otro valor por defecto, pero en ninguno de los dos casos obtendremos un error.

.. code-block::
    :linenos:

    >>> rae
    {'bifronte': 'De dos frentes o dos caras',
     'anarcoide': 'Que tiende al desorden',
     'montuvio': 'Campesino de la costa'}

    >>> rae.get('bifronte')
    'De dos frentes o dos caras'

    >>> rae.get('programación')

    >>> rae.get('programación', 'No disponible')
    'No disponible'

**Línea 6**:
    Equivalente a ``rae['bifronte']``.
**Línea 9**:
    La clave buscada no existe y obtenemos ``None``. [#invisible-none]_
**Línea 11**:
    La clave buscada no existe y nos devuelve el valor que hemos aportado por defecto.

Añadir o modificar un elemento
==============================

Para añadir un elemento a un diccionario sólo es necesario hacer referencia a la *clave* y asignarle un *valor*:

* Si la clave **ya existía** en el diccionario, **se reemplaza** el valor existente por el nuevo.
* Si la clave **es nueva**, **se añade** al diccionario con su valor. *No vamos a obtener un error a diferencia de las listas*.

Partimos del siguiente diccionario para ejemplificar estas acciones::

    >>> rae = {
    ...     'bifronte': 'De dos frentes o dos caras',
    ...     'anarcoide': 'Que tiende al desorden',
    ...     'montuvio': 'Campesino de la costa'
    ... }

Vamos a **añadir** la palabra *enjuiciar* a nuestro diccionario de la Real Academia de La Lengua::

    >>> rae['enjuiciar'] = 'Someter una cuestión a examen, discusión y juicio'

    >>> rae
    {'bifronte': 'De dos frentes o dos caras',
     'anarcoide': 'Que tiende al desorden',
     'montuvio': 'Campesino de la costa',
     'enjuiciar': 'Someter una cuestión a examen, discusión y juicio'}

Supongamos ahora que queremos **modificar** el significado de la palabra *enjuiciar* por otra acepción::

    >>> rae['enjuiciar'] = 'Instruir, juzgar o sentenciar una causa'

    >>> rae
    {'bifronte': 'De dos frentes o dos caras',
     'anarcoide': 'Que tiende al desorden',
     'montuvio': 'Campesino de la costa',
     'enjuiciar': 'Instruir, juzgar o sentenciar una causa'}

Creando desde vacío
-------------------

Una forma muy habitual de trabajar con diccionarios es utilizar el **patrón creación** partiendo de uno vacío e ir añadiendo elementos poco a poco.

Supongamos un ejemplo en el que queremos construir un diccionario donde las claves son las letras vocales y los valores son sus posiciones::

    >>> VOWELS = 'aeiou'

    >>> enum_vowels = {}

    >>> for i, vowel in enumerate(VOWELS):
    ...     enum_vowels[vowel] = i + 1
    ...

    >>> enum_vowels
    {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}

.. note:: Hemos utilizando la función ``enumerate()`` que ya vimos para las listas en el apartado: :ref:`core/datastructures/lists:Iterar usando enumeración`.

.. admonition:: Ejercicio
    :class: exercise

    Construya un diccionario partiendo de una cadena de texto con el siguiente formato:

    ``<city>:<population>;<city>:<population>;<city>:<population>;....``

    - Claves: **ciudades**.
    - Valores: **habitantes** (*como enteros*).

    **Ejemplo**

    * Entrada: ``Tokyo:38_140_000;Delhi:26_454_000;Shanghai:24_484_000;Mumbai:21_357_000;São Paulo:21_297_000``
    * Salida: ``{'Tokyo': 38140000, 'Delhi': 26454000, 'Shanghai': 24484000, 'Mumbai': 21357000, 'São Paulo': 21297000}``
    
    .. only:: html
    
        |solution| :download:`cities.py <files/cities.py>`


Pertenencia de una clave
========================

La forma **pitónica** de comprobar la existencia de una clave dentro de un diccionario, es utilizar el operador ``in``::

    >>> 'bifronte' in rae
    True

    >>> 'almohada' in rae
    False

    >>> 'montuvio' not in rae
    False

.. note:: El operador ``in`` siempre devuelve un valor booleano, es decir, verdadero o falso.

.. admonition:: Ejercicio
    :class: exercise

    Usando un diccionario, cuente el número de veces que se repite cada letra en una cadena de texto dada.

    **Ejemplo**
        * Entrada: ``'boom'``
        * Salida: ``{'b': 1, 'o': 2, 'm': 1}`` 

    .. only:: html

        |solution| :download:`counter.py <files/counter.py>`

Obtener todos los elementos
===========================

Python ofrece mecanismos para obtener todos los elementos de un diccionario. Partimos del siguiente diccionario::

    >>> rae
    {'bifronte': 'De dos frentes o dos caras',
     'anarcoide': 'Que tiende al desorden',
     'montuvio': 'Campesino de la costa',
     'enjuiciar': 'Instruir, juzgar o sentenciar una causa'}

**Obtener todas las claves de un diccionario**:
    Mediante la función ``keys()``::

        >>> rae.keys()
        dict_keys(['bifronte', 'anarcoide', 'montuvio', 'enjuiciar'])

**Obtener todos los valores de un diccionario**:
    Mediante la función ``values()``::

        >>> rae.values()
        dict_values([
            'De dos frentes o dos caras',
            'Que tiende al desorden',
            'Campesino de la costa',
            'Instruir, juzgar o sentenciar una causa'
        ])

**Obtener todos los pares "clave-valor" de un diccionario**:
    Mediante la función ``items()``::

        >>> rae.items()
        dict_items([
            ('bifronte', 'De dos frentes o dos caras'),
            ('anarcoide', 'Que tiende al desorden'),
            ('montuvio', 'Campesino de la costa'),
            ('enjuiciar', 'Instruir, juzgar o sentenciar una causa')
        ])

.. note:: Para este último caso cabe destacar que los "items" se devuelven como una lista de *tuplas*, donde cada tupla tiene dos elementos: el primero representa la clave y el segundo representa el valor.

Longitud de un diccionario
==========================

Podemos conocer el número de elementos ("clave-valor") que tiene un diccionario con la función ``len()``::

    >>> rae
    {'bifronte': 'De dos frentes o dos caras',
     'anarcoide': 'Que tiende al desorden',
     'montuvio': 'Campesino de la costa',
     'enjuiciar': 'Instruir, juzgar o sentenciar una causa'}

    >>> len(rae)
    4

Iterar sobre un diccionario
===========================

En base a :ref:`los elementos que podemos obtener <core/datastructures/dicts:Obtener todos los elementos>`, Python nos proporciona tres maneras de iterar sobre un diccionario.

**Iterar sobre claves**::

    >>> for word in rae.keys():
    ...     print(word)
    ...
    bifronte
    anarcoide
    montuvio
    enjuiciar

**Iterar sobre valores**::

    >>> for meaning in rae.values():
    ...     print(meaning)
    ...
    De dos frentes o dos caras
    Que tiende al desorden
    Campesino de la costa
    Instruir, juzgar o sentenciar una causa

**Iterar sobre "clave-valor"**::

    >>> for word, meaning in rae.items():
    ...     print(f'{word}: {meaning}')
    ...
    bifronte: De dos frentes o dos caras
    anarcoide: Que tiende al desorden
    montuvio: Campesino de la costa
    enjuiciar: Instruir, juzgar o sentenciar una causa

.. note:: En este último caso, recuerde el uso de los :ref:`core/datatypes/strings:"f-strings"` para formatear cadenas de texto.

.. admonition:: Ejercicio
    :class: exercise

    Dado el diccionario de ciudades y poblaciones ya visto, y suponiendo que estas ciudades son las únicas que existen en el planeta, calcule el porcentaje de población relativo de cada una de ellas con respecto al total.

    **Ejemplo**

    * Entrada: ``{'Tokyo': 38140000, 'Delhi': 26454000, 'Shanghai': 24484000, 'Mumbai': 21357000, 'São Paulo': 21297000}``
    * Salida: ``{'Tokyo': 28.952722193544467, 'Delhi': 20.081680988673973, 'Shanghai': 18.58622050830474, 'Mumbai': 16.212461664591746, 'São Paulo': 16.16691464488507}``
    
    .. only:: html
    
        |solution| :download:`population.py <files/population.py>`

Combinar diccionarios
=====================

Dados dos (o más) diccionarios, es posible "mezclarlos" para obtener una combinación de los mismos. Esta combinación se basa en dos premisas:

1. Si la clave no existe, se añade con su valor.
2. Si la clave ya existe, se añade con el valor del "último" diccionario en la mezcla. [#last-dict]_

Python ofrece dos mecanismos para realizar esta combinación. Vamos a partir de los siguientes diccionarios para ejemplificar su uso::

    >>> rae1 = {
    ...     'bifronte': 'De dos frentes o dos caras',
    ...     'enjuiciar': 'Someter una cuestión a examen, discusión y juicio'
    ... }

    >>> rae2 = {
    ...     'anarcoide': 'Que tiende al desorden',
    ...     'montuvio': 'Campesino de la costa',
    ...     'enjuiciar': 'Instruir, juzgar o sentenciar una causa'
    ... }

**Sin modificar los diccionarios originales**:
    Mediante el operador ``**``::

        >>> {**rae1, **rae2}
        {'bifronte': 'De dos frentes o dos caras',
         'enjuiciar': 'Instruir, juzgar o sentenciar una causa',
         'anarcoide': 'Que tiende al desorden',
         'montuvio': 'Campesino de la costa'}

    A partir de **Python 3.9** podemos utilizar el operador ``|`` para combinar dos diccionarios::

        >>> rae1 | rae2
        {'bifronte': 'De dos frentes o dos caras',
         'enjuiciar': 'Instruir, juzgar o sentenciar una causa',
         'anarcoide': 'Que tiende al desorden',
         'montuvio': 'Campesino de la costa'}

**Modificando los diccionarios originales**:
    Mediante la función ``update()``::

        >>> rae1.update(rae2)

        >>> rae1
        {'bifronte': 'De dos frentes o dos caras',
         'enjuiciar': 'Instruir, juzgar o sentenciar una causa',
         'anarcoide': 'Que tiende al desorden',
         'montuvio': 'Campesino de la costa'}

.. note:: Tener en cuenta que el orden en el que especificamos los diccionarios a la hora de su combinación (mezcla) es relevante en el resultado final. En este caso *el orden de los factores sí altera el producto*.

Borrar elementos
================

Python nos ofrece, al menos, tres formas para borrar elementos en un diccionario:

**Por su clave**:
    Mediante la sentencia ``del``:

    .. code-block::
        :emphasize-lines: 7
    
        >>> rae = {
        ...     'bifronte': 'De dos frentes o dos caras',
        ...     'anarcoide': 'Que tiende al desorden',
        ...     'montuvio': 'Campesino de la costa'
        ... }

        >>> del(rae['bifronte'])

        >>> rae
        {'anarcoide': 'Que tiende al desorden', 'montuvio': 'Campesino de la costa'}

**Por su clave (con extracción)**:
    Mediante la función ``pop()`` podemos extraer un elemento del diccionario por su clave. Vendría a ser una combinación de ``get()`` + ``del``:

    .. code-block::
        :emphasize-lines: 7

        >>> rae = {
        ...     'bifronte': 'De dos frentes o dos caras',
        ...     'anarcoide': 'Que tiende al desorden',
        ...     'montuvio': 'Campesino de la costa'
        ... }

        >>> rae.pop('anarcoide')
        'Que tiende al desorden'

        >>> rae
        {'bifronte': 'De dos frentes o dos caras', 'montuvio': 'Campesino de la costa'}

        >>> rae.pop('bucle')
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        KeyError: 'bucle'

    .. warning:: Si la clave que pretendemos extraer con ``pop()`` no existe, obtendremos un error.

**Borrado completo del diccionario**:
    1. Utilizando la función ``clear()``::

        >>> rae = {
        ...     'bifronte': 'De dos frentes o dos caras',
        ...     'anarcoide': 'Que tiende al desorden',
        ...     'montuvio': 'Campesino de la costa'
        ... }

        >>> rae.clear()

        >>> rae
        {}

    2. "Reinicializando" el diccionario a vacío con ``{}``::

        >>> rae = {
        ...     'bifronte': 'De dos frentes o dos caras',
        ...     'anarcoide': 'Que tiende al desorden',
        ...     'montuvio': 'Campesino de la costa'
        ... }

        >>> rae = {}

        >>> rae
        {}

    .. note:: La diferencia entre ambos métodos tiene que ver con cuestiones internas de gestión de memoria y de rendimiento.

**********************
Cuidado con las copias
**********************

|intlev|

Al igual que ocurría con :ref:`las listas <core/datastructures/lists:Cuidado con las copias>`, si hacemos un cambio en un diccionario, se verá reflejado en todas las variables que hagan referencia al mismo. Esto se deriva de su propiedad de ser *mutable*. Veamos un ejemplo concreto:

.. code-block::
    :emphasize-lines: 12, 17

    >>> original_rae = {
    ...     'bifronte': 'De dos frentes o dos caras',
    ...     'anarcoide': 'Que tiende al desorden',
    ...     'montuvio': 'Campesino de la costa'
    ... }

    >>> copy_rae = original_rae

    >>> original_rae['bifronte'] = 'bla bla bla'

    >>> original_rae
    {'bifronte': 'bla bla bla',
     'anarcoide': 'Que tiende al desorden',
     'montuvio': 'Campesino de la costa'}

    >>> copy_rae
    {'bifronte': 'bla bla bla',
     'anarcoide': 'Que tiende al desorden',
     'montuvio': 'Campesino de la costa'}

Una **posible solución** a este problema es hacer una "copia dura". Para ello Python proporciona la función ``copy()``:

.. code-block::
    :emphasize-lines: 7, 12, 17

    >>> original_rae = {
    ...     'bifronte': 'De dos frentes o dos caras',
    ...     'anarcoide': 'Que tiende al desorden',
    ...     'montuvio': 'Campesino de la costa'
    ... }

    >>> copy_rae = original_rae.copy()

    >>> original_rae['bifronte'] = 'bla bla bla'

    >>> original_rae
    {'bifronte': 'bla bla bla',
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa'}

    >>> copy_rae
    {'bifronte': 'De dos frentes o dos caras',
     'anarcoide': 'Que tiende al desorden',
     'montuvio': 'Campesino de la costa'}

.. tip:: En el caso de que estemos trabajando con diccionarios que contienen elementos mutables, debemos hacer uso de la función ``deepcopy()`` dentro del módulo ``copy`` de la librería estándar.

****************************
Diccionarios por comprensión
****************************

|intlev|

De forma análoga a cómo se escriben las :ref:`listas por comprensión <core/datastructures/lists:Listas por comprensión>`, podemos aplicar este método a los diccionarios usando llaves ``{`` ``}``.

Veamos un ejemplo en el que creamos un **diccionario por comprensión** donde las claves son palabras y los valores son sus longitudes:

.. code-block::
    :emphasize-lines: 3

    >>> words = ('sun', 'space', 'rocket', 'earth')

    >>> words_length = {word: len(word) for word in words}

    >>> words_length
    {'sun': 3, 'space': 5, 'rocket': 6, 'earth': 5}

También podemos aplicar **condiciones** a estas comprensiones. Continuando con el ejemplo anterior, podemos incorporar la restricción de sólo incluir palabras que no empiecen por vocal::

    >>> words = ('sun', 'space', 'rocket', 'earth')

    >>> words_length = {w: len(w) for w in words if w[0] not in 'aeiou'}

    >>> words_length
    {'sun': 3, 'space': 5, 'rocket': 6}

.. note:: Se puede consultar el `PEP-274`_ para ver más ejemplos sobre diccionarios por comprensión.

*******************
Objetos "hashables"
*******************

|advlev|

La única restricción que deben cumplir las **claves** de un diccionario es ser **"hashables"** [#hashables-terron]_. Un objeto es "hashable" si se le puede asignar un valor "hash" que no cambia en ejecución durante toda su vida.

Para encontrar el "hash" de un objeto, Python usa la función ``hash()``, que devuelve un número entero y es utilizado para indexar la *tabla "hash"* que se mantiene internamente::

    >>> hash(999)
    999

    >>> hash(3.14)
    322818021289917443

    >>> hash('hello')
    -8103770210014465245

    >>> hash(('a', 'b', 'c'))
    -2157188727417140402

Para que un objeto sea "hashable", debe ser **inmutable**::

    >>> hash(['a', 'b', 'c'])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unhashable type: 'list'

.. note:: De lo anterior se deduce que las claves de los diccionarios, al tener que ser "hasheables", sólo pueden ser objetos inmutables.

La función "built-in" ``hash()`` realmente hace una llamada al método mágico ``__hash__()`` del objeto en cuestión::

    >>> hash('spiderman')
    -8105710090476541603

    >>> 'spiderman'.__hash__()
    -8105710090476541603

----

.. rubric:: EJERCICIOS DE REPASO

1. Escriba un programa en Python que acepte una lista de palabras y las agrupe por su letra inicial usando un diccionario (:download:`solución <files/group_words.py>`).

    | Entrada: [ 'mesa', 'móvil', 'barco', 'coche', 'avión', 'bandeja', 'casa', 'monitor', 'carretera', 'arco']
    | Salida: {'m': ['mesa', 'móvil', 'monitor'], 'b': ['barco', 'bandeja'], 'c': ['coche', 'casa', 'carretera'], 'a': ['avión', 'arco']}

2. Escriba un programa en Python que acepte un diccionario y determine si todos los valores son iguales o no (:download:`solución <files/same_values.py>`).

    | Entrada: {'Juan': 5, 'Antonio': 5, 'Inma': 5, 'Ana': 5, 'Esteban': 5}
    | Salida: Same values

3. Escriba un programa en Python que acepte una lista de listas con varios elementos y obtenga un diccionario donde las claves serán los primeros elementos de las sublistas y los valores serán los restantes -- como listas -- (:download:`solución <files/build_super_dict.py>`).

    | Entrada: [['Episode IV - A New Hope', 'May 25', 1977], ['Episode V - The Empire Strikes Back', 'May 21', 1980], ['Episode VI - Return of the Jedi', 'May 25', 1983]]
    | Salida: {'Episode IV - A New Hope': ['May 25', 1977], 'Episode V - The Empire Strikes Back': ['May 21', 1980], 'Episode VI - Return of the Jedi': ['May 25', 1983]}

4. Escriba un programa en Python que acepte un diccionario cuyos valores son listas y borre el contenido de dichas listas (:download:`solución <files/clear_values.py>`).

    | Entrada: {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
    | Salida: {'C1': [], 'C2': [], 'C3': []}

5. Escriba un programa en Python que acepte un diccionario y elimine los espacios de sus claves respetando los valores correspondientes (:download:`solución <files/fix_keys.py>`).

    | Entrada: {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
    | Salida: {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']}

.. rubric:: AMPLIAR CONOCIMIENTOS

* `Using the Python defaultdict Type for Handling Missing Keys <https://realpython.com/python-defaultdict/>`_
* `Python Dictionary Iteration: Advanced Tips & Tricks <https://realpython.com/courses/python-dictionary-iteration/>`_
* `Python KeyError Exceptions and How to Handle Them <https://realpython.com/courses/python-keyerror/>`_
* `Dictionaries in Python <https://realpython.com/courses/dictionaries-python/>`_
* `How to Iterate Through a Dictionary in Python <https://realpython.com/iterate-through-dictionary-python/>`_
* `Shallow vs Deep Copying of Python Objects <https://realpython.com/copying-python-objects/>`_


.. --------------- Footnotes ---------------

.. [#dict-unsplash] Foto original de portada por `Aaron Burden`_ en Unsplash.
.. [#keep-order] Aunque históricamente Python no establecía que las claves de los diccionarios tuvieran que mantener su orden de inserción, a partir de Python 3.7 este comportamiento cambió y se garantizó el orden de inserción de las claves como `parte oficial de la especificación del lenguaje <https://docs.python.org/es/3/whatsnew/3.7.html>`_.
.. [#time-complexity] Véase este `análisis de complejidad y rendimiento`_ de distintas estructuras de datos en CPython.
.. [#none] ``None`` es la palabra reservada en Python para la "nada". Más información en `esta web <https://recursospython.com/guias-y-manuales/el-tipo-de-dato-none/>`_.
.. [#invisible-none] Realmente no estamos viendo nada en la consola de Python porque la representación en cadena de texto es vacía.
.. [#last-dict] En este caso "último" hace referencia al diccionario que se encuentra más a la derecha en la expresión.
.. [#hashables-terron] Se recomienda `esta ponencia <https://www.youtube.com/watch?v=JP3MnEcrdfQ>`_ de Víctor Terrón sobre objetos "hashables".

.. --------------- Hyperlinks ---------------

.. _Aaron Burden: https://unsplash.com/@aaronburden?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
.. _análisis de complejidad y rendimiento: https://wiki.python.org/moin/TimeComplexity
.. _PEP-274: https://www.python.org/dev/peps/pep-0274/
