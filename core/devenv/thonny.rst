######
Thonny
######

.. image:: img/freddie-marriage-vSchPA-YA_A-unsplash.jpg

`Thonny <https://thonny.org/>`__ es un programa muy interesante para empezar a aprender Python, ya que engloba tres de las herramientas fundamentales para trabajar con el lenguaje: **intérprete**, **editor** y **depurador**. [#thonny-unsplash]_

Cuando vamos a trabajar con Python debemos tener instalado, como mínimo, un :ref:`intérprete <core/introduction/machine:Compiladores>` del lenguaje (para otros lenguajes sería un *compilador*). El **intérprete** nos permitirá *ejecutar* nuestro código para obtener los resultados deseados. La idea del intéprete es lanzar instrucciones "sueltas" para probar determinados aspectos.

Pero normalmente queremos ir un poco más allá y poder escribir programas algo más largos, por lo que también necesitaremos un **editor**. Un editor es un programa que nos permite crear ficheros de código (en nuestro caso con extensión ``*.py``), que luego son ejecutados por el intérprete.

Hay otra herramienta interesante dentro del entorno de desarrollo que sería el **depurador**. Lo podemos encontrar habitualmente en la bibliografía por su nombre inglés *debugger*. Es el módulo que nos permite ejecutar paso a paso nuestro código y visualizar qué está ocurriendo en cada momento. Se suele usar normalmente para encontrar fallos (*bugs*) en nuestros programas y poder solucionarlos (*debug*/*fix*).

Cuando nos encontramos con un programa que proporciona estas funciones (e incluso otras adicionales) para el trabajo de programación, nos referimos a él como un *Entorno Integrado de Desarrollo*, conocido popularmente por sus siglas en inglés **IDE** (por Integrated Development Environment). Thonny es un IDE gratuito, sencillo y apto para principiantes.

***********
Instalación
***********

Para instalar Thonny debemos acceder a su `web <https://thonny.org>`_ y descargar la aplicación para nuestro sistema operativo. La ventaja es que está disponible tanto para **Windows**, **Mac** y **Linux**. Una vez descargado el fichero lo ejecutamos y seguimos su instalación paso por paso.

Una vez terminada la instalación ya podemos lanzar la aplicación que se verá parecida a la siguiente imagen:

.. figure:: img/thonny-empty.png
    :align: center

    Aspecto de Thonny al arrancarlo

.. note:: Es posible que el aspecto del programa varíe ligeramente según el sistema operativo, configuración de escritorio, versión utilizada o idioma (*en mi caso está en inglés*), pero a efectos de funcionamiento no hay diferencia.

Podemos observar que la pantalla está dividida en 3 paneles:

* *Panel principal* que contiene el **editor** e incluye la etiqueta ``<untitled>`` donde escribiremos nuestro *código fuente* Python.
* *Panel inferior* con la etiqueta *Shell* que contiene el **intérprete** de Python. En el momento de la escritura del presente documento, Thonny incluye la versión de Python 3.7.7.
* *Panel derecho* que contiene el **depurador**. Más concretamente se trata de la ventana de variables donde podemos *inspeccionar* el valor de las mismas.

Versiones de Python
===================

Existen múltiples versiones de Python. Desde el lanzamiento de la versión 1.0 en 1994 se han ido liberando versiones, cada vez, con nuevas características que aportan riqueza al lenguaje:

.. csv-table::
    :file: ../introduction/tables/python_versions.csv
    :widths: 15, 30
    :header-rows: 1
    :class: longtable

.. note:: Para ser exactos, esta tabla (y en general todo este manual) versa sobre una implementación concreta de Python denominada ``CPython``, pero existen `otras implementaciones alternativas de Python <https://www.python.org/download/alternatives/>`_. A los efectos de aprendizaje del lenguaje podemos referirnos a *Python* (aunque realmente estaríamos hablando de *CPython*).

**********************
Probando el intérprete
**********************

El intérprete de Python (por lo general) se identifica claramente porque posee un **prompt** [#prompt]_ con tres angulos hacia la derecha ``>>>``. En Thonny lo podemos encontrar en el panel inferior, pero se debe tener en cuenta que el intérprete de Python es una herramienta autocontenida y que la podemos ejecutar desde el símbolo del sistema o la terminal:

.. code-block::
    :caption: Invocando el intérprete de Python 3.7 desde una terminal en MacOS

    $ python3.7
    Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52)
    [Clang 6.0 (clang-600.0.57)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Para hacer una prueba inicial del intérprete vamos a retomar el primer programa que se suele hacer. Es el llamado :ref:`"Hello, World" <core/introduction/machine:Ensamblador>`. Para ello escribimos lo siguiente en el intérprete y pulsamos la tecla :kbd:`ENTER`::

    >>> print('Hello, World')
    Hello, World

Lo que hemos hecho es indicarle a Python que ejecute como **entrada** la instrucción ``print('Hello, World')``. La **salida** es el texto ``Hello, World`` que lo vemos en la siguiente línea (*ya sin el prompt* ``>>>``).

******************
Probando el editor
******************

Ahora vamos a realizar la misma operación, pero en vez de ejecutar la instrucción directamente en el intérprete, vamos a crear un fichero y guardarlo con la sentencia que nos interesa. Para ello escribimos ``print('Hello, World')`` en el panel de edición (*superior*) y luego guardamos el archivo con el nombre ``helloworld.py`` [#save-file]_:

.. figure:: img/thonny-save.png
    :align: center

    Guardando nuestro primer programa en Python

.. important:: Los ficheros que contienen programas hechos en Python siempre deben tener la extensión ``.py``

Ahora ya podemos *ejecutar* nuestro fichero ``helloworld.py``. Para ello pulsamos el botón verde con triángulo blanco (en la barra de herramientas) o bien damos a la tecla :kbd:`F5`. Veremos que en el panel de *Shell* nos aparece la salida esperada. Lo que está pasando "entre bambalinas" es que el intérprete de Python está recibiendo como entrada el fichero que hemos creado; lo ejecuta y devuelve la salida para que Thonny nos lo muestre en el panel correspondiente.

*********************
Probando el depurador
*********************

Nos falta por probar el depurador o "debugger". Aunque su funcionamiento va mucho más allá, de momento nos vamos a quedar en la posibilidad de inspeccionar las variables de nuestro programa. Desafortunadamente ``helloworld.py`` es muy simple y ni siquiera contiene variables, pero podemos hacer una pequeña modificación al programa para poder incorporarlas:

.. code-block:: python
    :linenos:
    :emphasize-lines: 1

    msg = 'Hello, World'
    print(msg)

Aunque ya lo veremos en profundidad, lo que hemos hecho es añadir una variable ``msg`` en la *línea 1* para luego utilizarla al mostrar por pantalla su contenido. Si ahora volvemos a ejecutar nuestro programa veremos que en el panel de variables nos aparece la siguiente información:

+---------+--------------------+
|  Name   |       Value        |
+=========+====================+
| ``msg`` | ``'Hello, World'`` |
+---------+--------------------+

También existe la posibilidad, a través del depurador, de ir ejecutando nuestro programa **paso a paso**. Para ello basta con pulsar en el botón que tiene un *insecto*. Ahí comienza la sesión de depuración y podemos avanzar instrucción por instrucción usando la tecla :kbd:`F7`:

.. figure:: img/thonny-debug.png
    :align: center

    Depurando nuestro primer programa en Python



.. --------------- Footnotes ---------------

.. [#thonny-unsplash] Foto original de portada por `freddie marriage`_ en Unsplash.
.. [#prompt] Término inglés que se refiere al símbolo que precede la línea de comandos.
.. [#save-file] La carpeta donde se guarden los archivos de código no es crítico para su ejecución, pero sí es importante mantener un orden y una organización para tener localizados nuestros ficheros y proyectos.

.. --------------- Hyperlinks ---------------

.. _freddie marriage: https://unsplash.com/@fredmarriage?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
