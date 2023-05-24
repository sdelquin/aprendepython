######
sqlite
######

.. image:: img/jandira-sonnendeck-AcW1ZwD-qC0-unsplash.jpg

El módulo `sqlite3`_ permite trabajar con bases de datos de tipo **SQLite** [#sqlite-unsplash]_. 

***************
¿Qué es SQLite?
***************

`SQLite`_ es un sistema gestor de bases de datos relacional contenido en una pequeña librería escrita en C (~275kB).

A continuación se muestran algunas de sus **principales características**:

- Tablas, índices, "triggers" y vistas ilimitadas.
- Hasta 32K columnas en una tabla y filas ilimitadas.
- Índices multi-columna.
- Restricciones de tipo ``CHECK``, ``UNIQUE``, ``NOT NULL`` y ``FOREIGN KEY``.
- Transacciones planas usando ``BEGIN``, ``COMMIT`` y ``ROLLBACK``
- Transacciones anidadas usando ``SAVEPOINT``, ``RELEASE`` y ``ROLLBACK TO``.
- Subconsultas.
- "Joins" de hasta 64 relaciones.
- "Joins" de tipo "left", "right" y "full outer".
- Uso de ``DISTINCT``, ``ORDER BY``, ``GROUP BY``, ``HAVING``, ``LIMIT`` y ``OFFSET``.
- Uso de ``UNION``, ``UNION ALL``, ``INTERSECT`` y ``EXCEPT``.
- Una amplia librería de `funciones SQL estándar`_.
- `Funciones de agregación`_.
- `Funciones de ventana`_.
- Por supuesto el uso de ``UPDATE``, ``DELETE`` e ``INSERT``.
- Cláusula `UPSERT`_.
- Soporte para `valores JSON`_.

Y muchas otras que se pueden consultar en la `página del proyecto <https://sqlite.org/fullsql.html>`_.

****************************
Conexión a la base de datos
****************************

Una base de datos SQLite no es más que un fichero binario, habitualmente con extensión ``.db`` o ``.sqlite``.

La **conexión a la base de datos** se realiza a través de la función `connect()`_ que espera recibir la ruta al fichero de base de datos y devuelve un objeto de tipo `Connection`_::

    >>> import sqlite3
    
    >>> con = sqlite3.connect('python.db')
    
    >>> con
    <sqlite3.Connection at 0x106ea8210>

.. warning::
    El módulo se llama **sqlite3** (no olvidarse del 3 al final).

La función ``connect()`` creará el fichero ``python.db`` si es que no existe. De momento se ha creado pero sin contenido::

    >>> !file python.db
    python.db: empty

Una vez que disponemos de la conexión ya podemos obtener un `Cursor`_ mediante la función `cursor()`_. Un **cursor** se podría ver como un manejador para realizar operaciones sobre la base de datos::

    >>> cur = con.cursor()
    
    >>> cur
    <sqlite3.Cursor at 0x106a63960>

******************
Creación de tablas
******************

Durante toda esta sección vamos a trabajar con una tabla de ejemplo que represente las `distintas versiones de Python`_ que han sido liberadas.

Lo primero de todo será crear la tabla ``pyversions`` -- teniendo en cuenta los `tipos de datos SQLite`_ -- con un código similar al siguiente:

.. code-block:: sql

    CREATE TABLE pyversions (
        branch CHAR PRIMARY KEY,
        released_at_year INTEGER,
        released_at_month INTEGER,
        release_manager CHAR
    )

Haremos uso del cursor creado para **ejecutar** estas instrucciones::

    >>> sql = '''CREATE TABLE pyversions (
    ...     branch CHAR PRIMARY KEY,
    ...     released_at_year INTEGER,
    ...     released_at_month INTEGER,
    ...     release_manager CHAR
    ... )'''

    >>> cur.execute(sql)
    <sqlite3.Cursor at 0x106a63960>

.. hint::
    Las :ref:`cadenas multilínea <core/datatypes/strings:comillas triples>` son grandes aliadas a la hora de escribir sentencias SQL.

En teoría, ya hemos creado la tabla ``pyversions`` de manera satisfactoria. Si comprobamos el tipo del fichero ``python.db`` podemos observar que concuerda con lo esperado::

    >>> !file python.db
    python.db: SQLite 3.x database, last written using SQLite version 3032003

***************
Añadiendo datos
***************

Para poder tener contenido sobre el que trabajar, vamos primeramente a añadir ciertos datos a la tabla. Como básicamente seguimos ejecutando sentencias SQL (en este caso de inserción) podemos volver a hacer uso de la función `execute()`_::

    >>> sql = 'INSERT INTO pyversions VALUES("2.6", 2008, 10, "Barry Warsaw")'
    
    >>> cur.execute(sql)
    <sqlite3.Cursor at 0x106a63960>

Aparentemente todo ha ido bien. Vamos a usar -- temporalmente -- la herramienta cliente ``sqlite3`` [#sqlite-cli]_ para ver el contenido de la tabla:

.. code-block:: console

    $ sqlite3 python.db "select * from pyversions"
    $ # Vacío

Resulta que no obtenemos ningún registro. ¿Por qué ocurre esto? Se debe a que la transacción está aún pendiente de confirmar. Para consolidarla tendremos que hacer uso de la función `commit()`_::

    >>> con.commit()

.. note::
    La función ``commit()`` pertenece al objeto conexión, no al objeto cursor.

Ahora podemos comprobar que sí se han guardado los datos correctamente:

.. code-block:: console

    $ sqlite3 python.db "select * from pyversions"
    2.6|2008|10|Barry Warsaw

Inserciones parametrizadas
==========================

Supongamos que no sabemos, a priori, los datos que vamos a insertar en la tabla puesto que provienen del usuario o de otra fuente externa. En este caso cabría plantearse cuál es la mejor opción para parametrizar la consulta.

Una primera aproximación podrían ser los :ref:`f-strings <core/datatypes/strings:"f-strings">`::

    >>> branch = 3.9
    >>> released_at_year = 2020
    >>> released_at_month = 10
    >>> release_manager = 'Łukasz Langa'

    >>> sql = f'INSERT INTO pyversions VALUES({branch}, {released_at_year}, {released_at_month}, {release_manager})'
    >>> sql
    'INSERT INTO pyversions VALUES(3.9, 2020, 10, Łukasz Langa)'

    >>> cur.execute(sql)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    OperationalError: near "Langa": syntax error

Obtenemos un error porque el contenido de "release manager" **es una cadena de texto y no puede contener espacios**. Una solución a este problema sería detectar qué campos necesitan comillas e incorporarlas de forma manual.

Pero existe otra aproximación y es **usar los "placeholders" que ofrece SQLite** al ejecutar sentencias. Estos "placeholders" se representan por el **símbolo de interrogación** ``?`` y se sustituyen por el **valor correspondiente en una tupla** que pasamos a posteriori.

Veamos cómo sería esta reimplementación::

    >>> sql = 'INSERT INTO pyversions VALUES(?, ?, ?, ?)'

    >>> cur.execute(sql, (branch, released_at_year, released_at_month, release_manager))
    <sqlite3.Cursor at 0x107426c40>

Ahora sí que todo ha ido bien y **no nos hemos tenido que preocupar del tipo de los campos**. Ya sólo por esto valdría la pena utilizar esta aproximación pero también sirve para evitar ataques por inyección SQL [#inyeccion-sql]_.

Este módulo también nos ofrece la posibilidad de usar **parámetros nominales a través de un diccionario** especificando los campos con dos puntos ``:field``. Veamos cómo sería esta aproximación::

    >>> sql = 'INSERT INTO pyversions VALUES(:branch, :year, :month, :manager)'

    >>> cur.execute(sql, dict(year=2020, month=10, branch=3.9, manager='Łukasz Langa'))
    <sqlite3.Cursor at 0x107426c40>

.. tip::
    Nótese que no es necesario usar el mismo orden de los parámetros cuando utilizamos esta aproximación nominal ya que el diccionario incluye las claves.

Inserciones en lote
===================

Vamos a pensar en un escenario algo más real, en el que necesitamos **insertar en la tabla más de un registro**. Obviamente la solución programática no puede ser ir de uno en uno.

Supongamos que disponemos del siguiente fichero ``pyversions.csv``:

.. literalinclude:: files/pyversions.csv
   :linenos:

Queremos procesar cada línea e insertarla en la tabla como un nuevo registro. Veamos una primera aproximación::

    >>> with open('pyversions.csv') as f:
    ...     f.readline()  # ignore headers
    ...     for line in f:
    ...         branch, year, month, manager = line.strip().split(',')
    ...         sql = f'INSERT INTO pyversions VALUES ("{branch}", {year}, {month}, "{manager}")'
    ...         cur.execute(sql)
    ...     con.commit()
    ...

Otra forma de hacer esto mismo sería utilizar la función `executemany()`_ en la que podemos indicar los parámetros a utilizar si partimos de un **iterable** de iterables (con el mismo número de campos que la tabla):

.. code-block::
    :emphasize-lines: 20

    >>> f = open('pyversions.csv')
    >>> data = [line.strip().split(',') for line in f.readlines()[1:]]
    >>> data
    [['2.6', '2008', '10', 'Barry Warsaw'],
     ['2.7', '2010', '7', 'Benjamin Peterson'],
     ['3.0', '2008', '12', 'Barry Warsaw'],
     ['3.1', '2009', '6', 'Benjamin Peterson'],
     ['3.2', '2011', '2', 'Georg Brandl'],
     ['3.3', '2012', '9', 'Georg Brandl'],
     ['3.4', '2014', '3', 'Larry Hastings'],
     ['3.5', '2015', '9', 'Larry Hastings'],
     ['3.6', '2016', '12', 'Ned Deily'],
     ['3.7', '2018', '6', 'Ned Deily'],
     ['3.8', '2019', '10', 'Łukasz Langa'],
     ['3.9', '2020', '10', 'Łukasz Langa'],
     ['3.10', '2021', '10', 'Pablo Galindo Salgado'],
     ['3.11', '2022', '10', 'Pablo Galindo Salgado'],
     ['3.12', '2023', '10', 'Thomas Wouters']]
    
    >>> cur.executemany('INSERT INTO pyversions VALUES (?, ?, ?, ?)', data)
    <sqlite3.Cursor at 0x104f3fb20>
    
    >>> con.commit()

Si dispusiéramos de un **diccionario** podríamos indicar incluso el nombre de los campos:

.. code-block::
    :emphasize-lines: 22

    >>> f = open('pyversions.csv')
    >>> fields = f.readline().strip().split(',')
    >>> data = [{f: v for f, v in zip(fields, line.strip().split(','))} for line in f]

    >>> data
    [{'branch': '2.6', 'year': '2008', 'month': '10', 'manager': 'Barry Warsaw'},
     {'branch': '2.7', 'year': '2010', 'month': '7', 'manager': 'Benjamin Peterson'},
     {'branch': '3.0', 'year': '2008', 'month': '12', 'manager': 'Barry Warsaw'},
     {'branch': '3.1', 'year': '2009', 'month': '6', 'manager': 'Benjamin Peterson'},
     {'branch': '3.2', 'year': '2011', 'month': '2', 'manager': 'Georg Brandl'},
     {'branch': '3.3', 'year': '2012', 'month': '9', 'manager': 'Georg Brandl'},
     {'branch': '3.4', 'year': '2014', 'month': '3', 'manager': 'Larry Hastings'},
     {'branch': '3.5', 'year': '2015', 'month': '9', 'manager': 'Larry Hastings'},
     {'branch': '3.6', 'year': '2016', 'month': '12', 'manager': 'Ned Deily'},
     {'branch': '3.7', 'year': '2018', 'month': '6', 'manager': 'Ned Deily'},
     {'branch': '3.8', 'year': '2019', 'month': '10', 'manager': 'Łukasz Langa'},
     {'branch': '3.9', 'year': '2020', 'month': '10', 'manager': 'Łukasz Langa'},
     {'branch': '3.10', 'year': '2021', 'month': '10', 'manager': 'Pablo Galindo Salgado'},
     {'branch': '3.11', 'year': '2022', 'month': '10', 'manager': 'Pablo Galindo Salgado'},
     {'branch': '3.12', 'year': '2023', 'month': '10', 'manager': 'Thomas Wouters'}]

    >>> cur.executemany('INSERT INTO pyversions VALUES (:branch, :year, :month, :manager)', data)
    <sqlite3.Cursor at 0x106e96030>

    >>> con.commit()

En cualquiera de los tres casos anteriores el resultado es el mismo y los registros quedan correctamente insertados en la base de datos:

.. code-block:: console

    $ sqlite3 python.db "select * from pyversions"
    2.6|2008|10|Barry Warsaw
    2.7|2010|7|Benjamin Peterson
    3.0|2008|12|Barry Warsaw
    3.1|2009|6|Benjamin Peterson
    3.2|2011|2|Georg Brandl
    3.3|2012|9|Georg Brandl
    3.4|2014|3|Larry Hastings
    3.5|2015|9|Larry Hastings
    3.6|2016|12|Ned Deily
    3.7|2018|6|Ned Deily
    3.8|2019|10|Łukasz Langa
    3.9|2020|10|Łukasz Langa
    3.10|2021|10|Pablo Galindo Salgado
    3.11|2022|10|Pablo Galindo Salgado
    3.12|2023|10|Thomas Wouters

Cerrando la conexión
====================

Al igual que ocurre con un fichero de texto, es necesario **cerrar la conexión abierta** para que se liberen los recursos asociados y se debloquee la base de datos.

La forma más directa de hacer esto sería::

    >>> con.close()

.. attention::
    Si hay alguna transacción pendiente, esta no será guardada al cerrar la conexión con la base de datos, si no se consolidan los cambios previamente.

Confirmar cambios
=================

En SQLite también es posible utilizar un :ref:`gestor de contexto <core/modularity/oop:gestores de contexto>` sobre la conexión que funciona de la siguiente manera:

- Si todo ha ido bien ejecutará un "commit" al final del bloque.
- Si ha habido alguna excepción ejecutará un "rollback" para que todo quede como al principio y deshacer los posibles cambios efectuados.

Ejemplo en el que todo va bien::

    >>> try:
    ...     with con:
    ...         cur.execute('INSERT INTO pyversions VALUES ("3.13", 2024, 10, "Thomas Wouters")')
    ... except sqlite3.IntegrityError:
    ...     print('Error: Duplicated Python version')
    ...

    >>> con.close()

Ejemplo donde se produce un error::

    >>> try:
    ...     with con:
    ...         cur.execute('INSERT INTO pyversions VALUES ("3.12", 2023, 10, "Thomas Wouters")')
    ... except sqlite3.IntegrityError:
    ...     print('Error: Duplicated Python version')
    ...
    Error: Duplicated Python version

    >>> con.close()

Nótese que en ambos casos **debemos cerrar la conexión**. Esto no se realiza de forma automática.

.. seealso::
    Existe la función `rollback()`_ que restaura a su comienzo cualquier transacción pendiente.

Es interesante conocer las distintas `excepciones`_ que pueden producirse al trabajar con este módulo a la hora del control de errores y de plantear posibles escenarios de mejora.

*********
Consultas
*********

La manera más sencilla de hacer una consulta es utilizar un cursor. Existen dos aproximaciones en el tratamiento de los resultados de la consulta:

1. Registros como tuplas.
2. Registros como diccionarios.

Registros como tuplas
=====================

Cuando ejecutamos una consulta **el resultado es un objeto iterable** que podemos recorrer de la misma manera que hemos hecho hasta ahora. Los datos nos vienen en forma de **tuplas**::

    >>> for row in cur.execute('SELECT * FROM pyversions'):
    ...     print(row)
    ...
    ('2.6', 2008, 10, 'Barry Warsaw')
    ('2.7', 2010, 7, 'Benjamin Peterson')
    ('3.0', 2008, 12, 'Barry Warsaw')
    ('3.1', 2009, 6, 'Benjamin Peterson')
    ('3.2', 2011, 2, 'Georg Brandl')
    ('3.3', 2012, 9, 'Georg Brandl')
    ('3.4', 2014, 3, 'Larry Hastings')
    ('3.5', 2015, 9, 'Larry Hastings')
    ('3.6', 2016, 12, 'Ned Deily')
    ('3.7', 2018, 6, 'Ned Deily')
    ('3.8', 2019, 10, 'Łukasz Langa')
    ('3.9', 2020, 10, 'Łukasz Langa')
    ('3.10', 2021, 10, 'Pablo Galindo Salgado')
    ('3.11', 2022, 10, 'Pablo Galindo Salgado')
    ('3.12', 2023, 10, 'Thomas Wouters')
    ('3.13', 2024, 10, 'Thomas Wouters')

También tenemos la opción de utilizar las funciones `fetchone()`_ y `fetchall()`_ para obtener una o todas las filas de la consulta::

    >>> res = cur.execute('SELECT * FROM pyversions')
    
    >>> res.fetchone()
    ('2.6', 2008, 10, 'Barry Warsaw')
    
    >>> res.fetchall()
    [('2.7', 2010, 7, 'Benjamin Peterson'),
     ('3.0', 2008, 12, 'Barry Warsaw'),
     ('3.1', 2009, 6, 'Benjamin Peterson'),
     ('3.2', 2011, 2, 'Georg Brandl'),
     ('3.3', 2012, 9, 'Georg Brandl'),
     ('3.4', 2014, 3, 'Larry Hastings'),
     ('3.5', 2015, 9, 'Larry Hastings'),
     ('3.6', 2016, 12, 'Ned Deily'),
     ('3.7', 2018, 6, 'Ned Deily'),
     ('3.8', 2019, 10, 'Łukasz Langa'),
     ('3.9', 2020, 10, 'Łukasz Langa'),
     ('3.10', 2021, 10, 'Pablo Galindo Salgado'),
     ('3.11', 2022, 10, 'Pablo Galindo Salgado'),
     ('3.12', 2023, 10, 'Thomas Wouters'),
     ('3.13', 2024, 10, 'Thomas Wouters')]

.. caution::
    Nótese que la llamada a ``fetchone()`` hace que quede "una fila menos" que recorrer. Es un comportamiento totalmente análogo a la :ref:`lectura de una línea <core/datastructures/files:lectura de una línea>` en un fichero. 

Registros como diccionarios
===========================

Este módulo también nos permite obtener los resultados de una consulta como un **iterable de diccionarios**. Esto ayuda a **acceder a los valores de cada registro por el nombre de la columna**.

Lo primero será indicar en la conexión que queremos obtener los resultados **también** como diccionarios:

.. code-block::
    :emphasize-lines: 2

    >>> con = sqlite3.connect('python.db')
    >>> con.row_factory = sqlite3.Row

Ahora ejecutamos una consulta y accedemos a la primera fila del resultado::

    >>> cur = con.cursor()
    >>> res = cur.execute('SELECT * FROM pyversions')

    >>> row = res.fetchone()
    >>> row
    <sqlite3.Row at 0x107b76190>

    >>> row.keys()
    ['branch', 'released_at_year', 'released_at_month', 'release_manager']

    >>> row['branch']
    '2.6'
    >>> row['released_at_year']
    2008
    >>> row['released_at_month']
    10
    >>> row['release_manager']
    'Barry Warsaw'

Vemos que esta aproximación nos permite usar nombres de columnas pero también es posible seguir accediendo a la información **a través del índice**::

    >>> row[0]
    '2.6'
    >>> row[1]
    2008
    >>> row[2]
    10
    >>> row[3]
    'Barry Warsaw'

Número de filas
===============

Hay ocasiones en las que lo que necesitamos obtener no es el dato en sí mismo, sino el **número de filas vinculadas a una determinada consulta**. En este sentido hay varias alternativas.

La primera aproximación es **mediante la sentencia SQL para contar**: ``COUNT()`` y obtener su resultado::

    >>> result = cur.execute('SELECT COUNT(*) FROM pyversions')

    >>> rows = result.fetchone()

    >>> rows[0]
    15

La segunda aproximación es **utilizar herramientas Python** para obtener la longitud del resultado de la consulta::

    >>> result = cur.execute('SELECT * FROM pyversions')

    >>> rows = result.fetchall()

    >>> len(rows)
    15

*********************
Otras funcionalidades
*********************

Tablas en memoria
=================

Existe la posibilidad de trabajar con tablas en memoria sin necesidad de tener un fichero en disco.

Veamos un ejemplo muy sencillo:

.. code-block::
    :emphasize-lines: 1

    >>> con = sqlite3.connect(':memory:')

    >>> cur = con.cursor()

    >>> cur.execute('CREATE TABLE temp (id INTEGER PRIMARY KEY, value CHAR)')
    <sqlite3.Cursor at 0x107884ea0>

    >>> cur.execute('INSERT INTO temp VALUES (1, "X")')
    <sqlite3.Cursor at 0x107884ea0>

    >>> for row in cur.execute('SELECT * FROM temp'):
    ...     print(row)
    ...
    (1, 'X')

.. caution::
    Obviamente si no guardamos estos datos los perderemos al no disponer de persistencia.


Claves autoincrementales
========================

Es muy habitual encontrar en la definición de una tabla un **campo identificador numérico entero** con el modificador ``AUTOINCREMENT`` de tal forma que actúe como clave primaria.

Existe una `forma sencilla de aplicar este escenario en SQLite <https://www.sqlite.org/autoinc.html>`_:

1. Definimos una columna de tipo ``INTEGER PRIMARY KEY``.
2. En cualquier operación de inserción, si no especificamos un valor explícito para dicha columna, se rellenará automáticamente con un entero sin usar, típicamente uno más que el último valor generado.

Veamos un ejemplo de aplicación con una tabla en memoria que almacena **ciudades y sus geolocalizaciones**:

.. code-block::
    :emphasize-lines: 5, 12, 18, 21, 27

    >>> con = sqlite3.connect(':memory:')
    >>> cur = con.cursor()

    >>> cur.execute('''CREATE TABLE cities (
    ... id INTEGER PRIMARY KEY,
    ... city CHAR UNIQUE,
    ... latitude REAL,
    ... longitude REAL)''')
    <sqlite3.Cursor at 0x107139bc0>

    >>> cur.execute('''INSERT INTO
    ... cities(city, latitude, longitude)  # Obviamos "id"
    ... VALUES("Tokyo", 35.652832, 139.839478)''')
    <sqlite3.Cursor at 0x107139bc0>

    >>> result = cur.execute('SELECT * FROM cities')
    >>> result.fetchall()
    [(1, 'Tokyo', 35.652832, 139.839478)]

    >>> cur.execute('''INSERT INTO
    ... cities(city, latitude, longitude)  # Obviamos "id"
    ... VALUES("Barcelona", 41.390205, 2.154007)''')
    <sqlite3.Cursor at 0x107139bc0>

    >>> result = cur.execute('SELECT * FROM cities')
    >>> result.fetchall()
    [(1, 'Tokyo', 35.652832, 139.839478), (2, 'Barcelona', 41.390205, 2.154007)]

Copias de seguridad
===================

Es posible realizar copias de seguridad de manera programática [#backup-example]_:

.. code-block::
    :emphasize-lines: 9

    >>> def progress(status, remaining, total):
    ...     print(f'Copied {total-remaining} of {total} pages...')
    ...

    >>> src = sqlite3.connect('python.db')
    >>> dst = sqlite3.connect('backup.db')

    >>> with dst:
    ...     src.backup(dst, pages=1, progress=progress)
    ...
    Copied 1 of 3 pages...
    Copied 2 of 3 pages...
    Copied 3 of 3 pages...

    >>> dst.close()
    >>> src.close()

Podemos comprobar que ambas bases de datos tienen el mismo contenido::

    >>> src = sqlite3.connect('python.db')
    >>> dst = sqlite3.connect('backup.db')

    >>> with src, dst:
    ...     src_cur = src.cursor()
    ...     dst_cur = dst.cursor()
    ...     sql = 'SELECT * FROM pyversions'
    ...     src_data = src_cur.execute(sql).fetchall()
    ...     dst_data = dst_cur.execute(sql).fetchall()
    ...     if src_data == dst_data:
    ...         print('Contents from both DBs are the same!')
    ...
    Contents from both DBs are the same!

Información de filas
====================

Cuando ejecutamos una sentencia de modificación sobre la base de datos podemos obtener el **número de filas modificadas**:

.. code-block::
    :emphasize-lines: 25

    >>> con = sqlite3.connect('python.db')
    >>> cur = con.cursor()

    >>> cur.execute('SELECT * FROM pyversions').fetchall()
    [('2.6', 2008, 10, 'Barry Warsaw'),
     ('2.7', 2010, 7, 'Benjamin Peterson'),
     ('3.0', 2008, 12, 'Barry Warsaw'),
     ('3.1', 2009, 6, 'Benjamin Peterson'),
     ('3.2', 2011, 2, 'Georg Brandl'),
     ('3.3', 2012, 9, 'Georg Brandl'),
     ('3.4', 2014, 3, 'Larry Hastings'),
     ('3.5', 2015, 9, 'Larry Hastings'),
     ('3.6', 2016, 12, 'Ned Deily'),
     ('3.7', 2018, 6, 'Ned Deily'),
     ('3.8', 2019, 10, 'Łukasz Langa'),
     ('3.9', 2020, 10, 'Łukasz Langa'),
     ('3.10', 2021, 10, 'Pablo Galindo Salgado'),
     ('3.11', 2022, 10, 'Pablo Galindo Salgado'),
     ('3.12', 2023, 10, 'Thomas Wouters'),
     ('3.13', 2024, 10, 'Thomas Wouters')]

    >>> cur.execute('UPDATE pyversions SET released_at_year=2000')
    <sqlite3.Cursor at 0x105593dc0>

    >>> cur.rowcount
    16  # filas modificadas

Cuando insertamos un registro en la base de datos podemos obtener cuál es el **identificador de la últila fila insertada**:

.. code-block::
    :emphasize-lines: 4

    >>> cur.execute('INSERT INTO pyversions VALUES ("3.14", 2025, 10, "Guido Van Rossum")')
    <sqlite3.Cursor at 0x105593dc0>

    >>> cur.lastrowid
    17

.. rubric:: EJERCICIOS DE REPASO

1. Escriba una clase ``ToDo`` y una clase ``Task`` que permita implementar una aplicación de gestión de tareas.

.. only:: html

    | Plantilla: :download:`todo.py <files/templates/todo.py>`
    | Tests: :download:`test_todo.py <files/test_todo.py>`
    | Lanzar tests: ``pytest -xq test_todo.py``

.. --------------- Footnotes ---------------

.. [#sqlite-unsplash] Foto original de portada por `Jandira Sonnendeck`_ en Unsplash.
.. [#sqlite-cli] `Herramienta cliente de sqlite`_ para terminal.
.. [#backup-example] Ejemplo tomado de la documentación oficial de Python.
.. [#inyeccion-sql] `Inyección SQL`_ es un método de infiltración de código intruso que se vale de una vulnerabilidad informática presente en una aplicación en el nivel de validación de las entradas para realizar operaciones sobre una base de datos.

.. --------------- Hyperlinks ---------------

.. _Jandira Sonnendeck: https://unsplash.com/@jandira_sonnendeck?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
.. _sqlite3: https://docs.python.org/es/3/library/sqlite3.html
.. _SQLite: https://sqlite.org/index.html
.. _funciones SQL estándar: https://sqlite.org/lang_corefunc.html
.. _Funciones de agregación: https://sqlite.org/lang_aggfunc.html
.. _Funciones de ventana: https://sqlite.org/windowfunctions.html
.. _UPSERT: https://sqlite.org/lang_upsert.html
.. _valores JSON: https://sqlite.org/json1.html
.. _distintas versiones de Python: https://devguide.python.org/versions/
.. _tipos de datos SQLite: https://www.sqlite.org/datatype3.html
.. _connect(): https://docs.python.org/es/3/library/sqlite3.html#sqlite3.connect
.. _Connection: https://docs.python.org/es/3/library/sqlite3.html#sqlite3.Connection
.. _cursor(): https://docs.python.org/es/3/library/sqlite3.html#sqlite3.Connection.cursor
.. _Cursor: https://docs.python.org/es/3/library/sqlite3.html#sqlite3.Cursor
.. _execute(): https://docs.python.org/es/3/library/sqlite3.html#sqlite3.Cursor.execute
.. _commit(): https://docs.python.org/es/3/library/sqlite3.html#sqlite3.Connection.commit
.. _Herramienta cliente de sqlite: https://www.sqlite.org/cli.html
.. _executemany(): https://docs.python.org/es/3/library/sqlite3.html#sqlite3.Cursor.executemany
.. _fetchone(): https://docs.python.org/es/3/library/sqlite3.html#sqlite3.Cursor.fetchone
.. _fetchall(): https://docs.python.org/es/3/library/sqlite3.html#sqlite3.Cursor.fetchall
.. _rollback(): https://docs.python.org/es/3/library/sqlite3.html#sqlite3.Connection.rollback
.. _excepciones: https://docs.python.org/es/3/library/sqlite3.html#exceptions
.. _Inyección SQL: https://es.wikipedia.org/wiki/Inyecci%C3%B3n_SQL
