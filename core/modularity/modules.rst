#######
Módulos
#######

.. image:: img/xavi-cabrera-kn-UmDZQDjM-unsplash.jpg

Escribir pequeños trozos de código puede resultar interesante para realizar determinadas pruebas. Pero a la larga, nuestros programas tenderán a crecer y será necesario agrupar el código en unidades manejables.

Los **módulos** son simplemente ficheros de texto que contienen código Python y representan unidades con las que *evitar la repetición* y *favorecer la reutilización*. [#lego-unsplash]_

******************
Importar un módulo
******************

Para hacer uso del código de otros módulos usaremos la sentencia ``import``. Esto permite importar el código y las variables de dicho módulo para que estén disponibles en nuestro programa.

La forma más sencilla de importar un módulo es ``import <module>`` donde ``module`` es el nombre de otro fichero Python, sin la extensión ``.py``.

Supongamos que partimos del siguiente fichero (*módulo*):

:download:`arith.py <files/mymath/arith.py>`

.. literalinclude:: files/mymath/arith.py
    :linenos:

Desde otro fichero - en principio en la misma carpeta - podríamos hacer uso de las funciones definidas en ``arith.py``. 

Importar módulo completo
========================

Desde otro fichero haríamos lo siguiente para importar todo el contenido del módulo ``arith.py``:

.. code-block::
    :emphasize-lines: 1
    :linenos:

    >>> import arith

    >>> arith.addere(3, 7)
    10

.. note:: Nótese que en la **línea 3** debemos anteponer a la función ``addere()`` el :ref:`espacio de nombres <core/modularity/functions:Espacios de nombres>` que define el módulo ``arith``.

Ruta de búsqueda de módulos
---------------------------

Python tiene 2 formas de encontrar un módulo:

1. En la carpeta actual de trabajo.
2. En las rutas definidas en la variable de entorno ``PYTHONPATH``.

Para ver las rutas de búsqueda establecidas, podemos ejecutar lo siguiente en un intérprete de Python::

    >>> import sys

    >>> sys.path
    ['/path/to/.pyenv/versions/3.9.1/envs/aprendepython/bin',
    '/path/to/.pyenv/versions/3.9.1/lib/python3.9',
    '/path/to/.pyenv/versions/3.9.1/envs/aprendepython/lib/python3.9/site-packages',
    '']

La cadena vacía que existe al final de la lista hace referencia a la **carpeta actual**.

Modificando la ruta de búsqueda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si queremos modificar la ruta de búsqueda, existen dos opciones:

Modificando directamente la variable ``PYTHONPATH``
    Para ello exportamos dicha variable de entorno desde una terminal:

    .. code-block:: console

        $ export PYTHONPATH=/tmp
    
    Y comprobamos que se ha modificado en ``sys.path``:

    .. code-block::
        :emphasize-lines: 3
    
        >>> sys.path
        ['/path/to/.pyenv/versions/3.9.1/envs/aprendepython/bin',
         '/tmp',
        '/path/to/.pyenv/versions/3.9.1/lib/python3.9',
        '/path/to/.pyenv/versions/3.9.1/envs/aprendepython/lib/python3.9/site-packages',
        '']

Modificando directamente la lista ``sys.path``
    Para ello accedemos a lista que está en el módulo ``sys`` de la librería estandar:

    .. code-block::
        :emphasize-lines: 8
    
        >>> sys.path.append('/tmp')  # añadimos al final

        >>> sys.path
        ['/path/to/.pyenv/versions/3.9.1/envs/aprendepython/bin',
        '/path/to/.pyenv/versions/3.9.1/lib/python3.9',
        '/path/to/.pyenv/versions/3.9.1/envs/aprendepython/lib/python3.9/site-packages',
        '',
        '/tmp']

    .. code-block::
        :emphasize-lines: 4
    
        >>> sys.path.insert(0, '/tmp')  # insertamos por el principio

        >>> sys.path
        ['/tmp',
        '/path/to/.pyenv/versions/3.9.1/envs/aprendepython/bin',
        '/path/to/.pyenv/versions/3.9.1/lib/python3.9',
        '/path/to/.pyenv/versions/3.9.1/envs/aprendepython/lib/python3.9/site-packages',
        '']
    
    .. tip:: El hecho de poner nuestra ruta al principio o al final de ``sys.path`` influye en la búsqueda, ya que si existen dos (o más módulos) que se llaman igual en nuestra ruta de búsqueda, Python usará el primero que encuentre.
    

Importar partes de un módulo
============================

Es posible que no necesitemos todo aquello que está definido en ``arith.py``. Supongamos que sólo vamos a realizar divisiones. Para ello haremos lo siguiente:

.. code-block::
    :emphasize-lines: 1
    :linenos:

    >>> from arith import partitus

    >>> partitus(5, 2)
    2.5

.. note:: Nótese que en la **línea 3** ya podemos hacer uso directamente de la función ``partitus()`` porque la hemos importado directamente. Este esquema tiene el inconveniente de la posible **colisión de nombres**, en aquellos casos en los que tuviéramos algún objeto con el mismo nombre que el objeto que estamos importando.

Importar usando un alias
========================

Hay ocasiones en las que interesa, por colisión de otros nombres o por mejorar la legibilidad, usar un nombre diferente del módulo (u objeto) que estamos importando. Python nos ofrece esta posibilidad a través de la sentencia ``as``.

Supongamos que queremos importar la función del ejemplo anterior pero con otro nombre:

.. code-block::
    :emphasize-lines: 1

    >>> from arith import partitus as mydivision

    >>> mydivision(5, 2)
    2.5

********
Paquetes
********

Un **paquete** es simplemente una **carpeta** que contiene ficheros ``.py``. Además permite tener una jerarquía con más de un nivel de subcarpetas anidadas.

Para ejemplificar este modelo vamos a crear un paquete llamado ``mymath`` que contendrá 2 módulos:

* :download:`arith.py <files/mymath/arith.py>` para operaciones aritméticas (ya visto :ref:`anteriormente <core/modularity/modules:Importar un módulo>`).
* :download:`logic.py <files/mymath/logic.py>` para operaciones lógicas.

El código del módulo de operaciones lógicas es el siguiente:

:download:`logic.py <files/mymath/logic.py>`

.. literalinclude:: files/mymath/logic.py
    :linenos:

Si nuestro código principal va a estar en un fichero ``main.py`` (*a primer nivel*), la estructura de ficheros nos quedaría tal que así:

.. code-block::
    :emphasize-lines: 3
    :linenos:

    .
    ├── main.py
    └── mymath
        ├── arith.py
        └── logic.py

    1 directory, 3 files

**Línea 2**
    Punto de entrada de nuestro programa a partir del fichero ``main.py``
**Línea 3**
    Carpeta que define el paquete ``mymath``.
**Línea 4**
    Módulo para operaciones aritméticas.
**Línea 5**
    Módulo para operaciones lógicas.

Importar desde un paquete
=========================

Si ya estamos en el fichero ``main.py`` (o a ese nivel) podremos hacer uso de nuestro paquete de la siguiente forma:

.. code-block::
    :emphasize-lines: 1
    :linenos:

    >>> from mymath import arith, logic

    >>> arith.pullulate(4, 7)
    28

    >>> logic.et(1, 0)
    0

**Línea 1**
    Importar los módulos ``arith`` y ``logic`` del paquete ``mymath``
**Línea 3**
    Uso de la función ``pullulate`` que está definida en el módulo ``arith``
**Línea 5**
    Uso de la función ``et`` que está definida en el módulo ``logic``

******************
Programa principal
******************

Cuando decidimos desarrollar una pieza de software en Python, normalmente usamos distintos ficheros para ello. Algunos de esos ficheros se convertirán en *módulos*, otros se englobarán en *paquetes* y existirá uno en concreto que será nuestro **punto de entrada**, también llamado **programa principal**.

.. hint:: Suele ser una buena práctica llamar ``main.py`` al fichero que contiene nuestro programa principal.

La estructura que suele tener este *programa principal* es la siguiente::

    # imports de la librería estándar
    # imports de librerías de terceros
    # imports de módulos propios

    # CÓDIGO PROPIO
    # ...
    # CÓDIGO PROPIO

    if __name__ == '__main__':
        # punto de entrada real

.. important:: Si queremos ejecutar este fichero ``main.py`` desde línea de comandos, tendríamos que hacer::

        $ python3 main.py

``if __name__ == '__main__'``
=============================

Esta condición permite, en el programa principal, diferenciar qué codigo se lanzará cuando el fichero se ejecuta directamente o cuando el fichero se importa desde otro lugar.

.. figure:: img/if-name-main.jpg
    :align: center

    Comportamiento de un programa principal al importarlo o ejecutarlo

:download:`hello.py <files/hello.py>`

.. literalinclude:: files/hello.py
    :linenos:

``import hello``
    El código se ejecuta siempre desde la primera instrucción a la última:

    * **Línea 1**: se importa el módulo ``blabla``.
    * **Línea 4**: se define la función ``myfunc()`` y estará disponible para usarse.
    * **Línea 9**: esta condición **no** se cumple, ya que estamos importando y la variable especial ``__name__`` no toma ese valor. Con lo cual finaliza la ejecución.
    * *No hay salida por pantalla*.

``$ python3 hello.py``
    El código se ejecuta siempre desde la primera instrucción a la última:

    * **Línea 1**: se importa el módulo ``blabla``.
    * **Línea 4**: se define la función ``myfunc()`` y estará disponible para usarse.
    * **Línea 9**: esta condición **sí** se cumple, ya que estamos ejecutando directamente el fichero (*como programa principal*) y la variable especial ``__name__`` toma el valor ``__main__``.
    * **Línea 10**: salida por pantalla de la cadena de texto ``Entry point``.
    * **Línea 11**: llamada a la función ``myfunc()`` que muestra por pantalla ``Inside myfunc``, además de invocar a la función ``hi()`` del módulo ``blabla``.

.. rubric:: AMPLIAR CONOCIMIENTOS

- `Defining Main Functions in Python <https://realpython.com/courses/python-main-function/>`_
- `Python Modules and Packages: An Introduction <https://realpython.com/courses/python-modules-packages/>`_
- `Absolute vs Relative Imports in Python <https://realpython.com/courses/absolute-vs-relative-imports-python/>`_
- `Running Python Scripts <https://realpython.com/courses/running-python-scripts/>`_
- `Writing Beautiful Pythonic Code With PEP 8 <https://realpython.com/courses/writing-beautiful-python-code-pep-8/>`_
- `Python Imports 101 <https://realpython.com/courses/python-imports-101/>`_
- `Clean Code in Python <https://testdriven.io/blog/clean-code-python/>`_



.. --------------- Footnotes ---------------

.. [#lego-unsplash] Foto original por `Xavi Cabrera`_ en Unsplash.

.. --------------- Hyperlinks ---------------

.. _Xavi Cabrera: https://unsplash.com/@xavi_cabrera?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
