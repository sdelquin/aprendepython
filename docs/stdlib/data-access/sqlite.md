---
icon: simple/sqlite
---

# sqlite { #sqlite }

![Hard disk](images/sqlite/hdd.jpg)
(1)
{ .annotate }

1. :fontawesome-regular-copyright: [Jandira Sonnendeck](https://unsplash.com/@jandira_sonnendeck) :material-at: [Unsplash](https://unsplash.com) 

## ¿Qué es SQLite? { #what-is-sqlite }

[SQLite](https://sqlite.org/index.html) es un **sistema gestor de bases de datos relacional** contenido en una pequeña librería escrita en C (~275kB) y que usa **un único fichero** para almacenar la base de datos.

A continuación se muestran algunas de sus **principales características**:

- [x] Tablas, índices, «triggers» y vistas ilimitadas.
- [x] Hasta 32K columnas en una tabla y filas ilimitadas.
- [x] Índices multi-columna.
- [x] Restricciones de tipo `CHECK`, `UNIQUE`, `NOT NULL` y `FOREIGN KEY`.
- [x] Transacciones planas usando `BEGIN`, `COMMIT` y `ROLLBACK`.
- [x] Transacciones anidadas usando `SAVEPOINT`, `RELEASE` y `ROLLBACK TO`.
- [x] Subconsultas.
- [x] «Joins» de hasta 64 relaciones.
- [x] «Joins» de tipo «left», «right» y «full outer».
- [x] Uso de `DISTINCT`, `ORDER BY`, `GROUP BY`, `HAVING`, `LIMIT` y `OFFSET`.
- [x] Uso de `UNION`, `UNION ALL`, `INTERSECT` y `EXCEPT`.
- [x] Una amplia librería de [funciones SQL estándar](https://sqlite.org/lang_corefunc.html).
- [x] [Funciones de agregación](https://sqlite.org/lang_aggfunc.html).
- [x] [Funciones de ventana](https://sqlite.org/windowfunctions.html).
- [x] Por supuesto el uso de `UPDATE`, `DELETE` e `INSERT`.
- [x] Cláusula [`UPSERT`](https://sqlite.org/lang_upsert.html).
- [x] Soporte para [valores JSON](https://sqlite.org/json1.html).

Y muchas otras que se pueden consultar en la [página del proyecto](https://sqlite.org/fullsql.html).

## Conexión a la base de datos { #db-connect }

Una base de datos SQLite no es más que un **fichero binario**, habitualmente con extensión `.db` o `.sqlite`. Antes de realizar cualquier operación es necesario «conectar» con este fichero.

La **conexión a la base de datos** se realiza a través de la función [`connect()`](https://docs.python.org/es/3/library/sqlite3.html#sqlite3.connect) que espera recibir la ruta al fichero de base de datos y devuelve un objeto de tipo [`Connection`](https://docs.python.org/es/3/library/sqlite3.html#sqlite3.Connection).

```pycon
>>> import sqlite3#(1)!

>>> con = sqlite3.connect('python.db')#(2)!
>>> con#(3)!
<sqlite3.Connection at 0x105953c40>
```
{ .annotate }

1. Importamos el módulo.  
    :fontawesome-solid-triangle-exclamation:{.acc} Se llama **sqlite3** (no olvidarse del 3 al final).
2. Especificamos una ruta (relativa o absoluta) al fichero de base de datos.
3. Comprobamos que el objeto devuelto es una instancia de la clase `Connection`.

La primera vez que conectamos a una base de datos (fichero) inexistente, Python lo creará sin contenido alguno:

```pycon
>>> !file python.db
python.db: empty
```

Una vez que disponemos de la conexión ya podemos obtener un [`Cursor`](https://docs.python.org/es/3/library/sqlite3.html#sqlite3.Cursor) mediante la función [`cursor()`](https://docs.python.org/es/3/library/sqlite3.html#sqlite3.Connection.cursor). Un cursor se podría ver como **un manejador para realizar operaciones** sobre la base de datos:

```pycon
>>> cur = con.cursor()
>>> cur
<sqlite3.Cursor object at 0x1057d4240>
```

## Creación de tablas { #create-table }

Para poder crear una tabla primero debemos manejar los [tipos de datos SQLite](https://www.sqlite.org/datatype3.html) disponibles. Aunque hay alguno más, con los siguientes nos será suficiente para la inmensa mayoría de diseños de bases de datos que podamos necesitar:

- [x] `INTEGER` :material-arrow-right-bold: para valores **enteros**.
- [x] `REAL` :material-arrow-right-bold: para valores **flotantes**.
- [x] `TEXT` :material-arrow-right-bold: para **cadenas de texto**.

!!! warning "INT"

    Aunque `INT` también está permitido, se desaconseja su uso en favor de `INTEGER` especialmente cuando trabajamos con la librería Python `sqlite3` y no queremos obtener resultados inesperados.

Durante toda esta sección vamos a trabajar con una tabla de <span class="example">ejemplo:material-flash:</span> que representa las [distintas versiones de Python](https://devguide.python.org/versions/) que han sido liberadas.

Empecemos creando la tabla `pyversions` a través de un código SQL similar al siguiente:

```sql
CREATE TABLE pyversions (
    branch TEXT PRIMARY KEY,
    released_at_year INTEGER,
    released_at_month INTEGER,
    release_manager TEXT
)
```

Haremos uso del cursor creado para **ejecutar** estas instrucciones:

```pycon
>>> sql = """CREATE TABLE pyversions (
...     branch TEXT PRIMARY KEY,
...     released_at_year INTEGER,
...     released_at_month INTEGER,
...     release_manager TEXT
... )"""#(1)!

>>> cur.execute(sql)#(2)!
<sqlite3.Cursor object at 0x1057d4240>
```
{ .annotate }

1.  - Es habitual usar [comillas triples](../../core/datatypes/strings.md#triple-quotes) para definir sentencias SQL dentro de código Python.
    - No es necesario añadir punto y coma `;` al final de la sentencia SQL cuando usamos el módulo `sqlite3` salvo que se trate de [scripts](#run-scripts).
2. Un _cursor_ tiene un método `execute()` que permite ejecutar sentencias SQL.

Ya hemos creado la tabla `pyversions` de manera satisfactoria.

Si comprobamos ahora el contenido del fichero `python.db` podemos observar que nos indica la versión de SQLite y la última escritura:

```pycon
>>> !file python.db
python.db: SQLite 3.x database, last written using SQLite version 3047001, file counter 1, database pages 3, cookie 0x1, schema 4, UTF-8, version-valid-for 1
```

## Añadiendo datos { #add-data }

Para tener contenido sobre el que trabajar, vamos primeramente a añadir ciertos datos a la tabla. Como básicamente seguimos ejecutando sentencias SQL (en este caso de inserción) podemos volver a hacer uso de la función [`execute()`](https://docs.python.org/es/3/library/sqlite3.html#sqlite3.Cursor.execute):

```pycon
>>> sql = 'INSERT INTO pyversions VALUES ("2.6", 2008, 10, "Barry Warsaw")'

>>> cur.execute(sql)
<sqlite3.Cursor object at 0x1057d4240>
```

Aparentemente todo ha ido bien. Vamos a usar —temporalmente— la herramienta cliente sqlite3[^1] para ver el contenido de la tabla:

```console
$ sqlite3 python.db "select * from pyversions"
```

Resulta que tenemos una salida vacía. ¿No hay ningún registro? Esto se debe a que la transacción está aún pendiente de confirmar. Para consolidarla tendremos que hacer uso de la función [`commit()`](https://docs.python.org/es/3/library/sqlite3.html#sqlite3.Connection.commit):

```pycon
>>> con.commit()#(1)!
```
{ .annotate }

1.  - Nótese que el método `commit()` pertenece a la **conexión** y no a al _cursor_.
    - Las transacciones pueden consolidarse con `commit()` o deshacerse con `rollback()`.

Ahora podemos comprobar que sí se han guardado los datos correctamente:

```console
$ sqlite3 python.db "select * from pyversions"
2.6|2008|10|Barry Warsaw
```

### Autocommit { #autocommit }

Cuando creamos [la conexión a la base de datos](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect) podemos pasar como argumento `autocommit=True` de tal forma que no sea necesario invocar explícitamente a `commit()`:

```pycon
>>> con = sqlite3.connect('python.db', autocommit=True)
```

Así, cada vez que ejecutemos operaciones de modificación sobre la base de datos se lanzará automáticamente el método `commit()` confirmando los cambios indicados.

### Inserción parametrizada { #param-insert }

Supongamos que no sabemos, a priori, los datos que vamos a insertar en la tabla puesto que provienen del usuario o de otra fuente externa. En este caso cabría plantearse cuál es la mejor opción para **parametrizar la consulta**.

En una primera aproximación podríamos pensar en utilizar un [f-string](../../core/datatypes/strings.md#fstrings).

Por <span class="example">ejemplo:material-flash:</span> vamos a insertar un nuevo registro a partir de ciertas variables:

```pycon
>>> branch = 3.11
>>> released_at_year = 2022
>>> released_at_month = 10
>>> release_manager = 'Pablo Galindo Salgado'

>>> sql = f'INSERT INTO pyversions VALUES ({branch}, {released_at_year}, {released_at_month}, {release_manager})'
>>> sql
'INSERT INTO pyversions VALUES (3.11, 2022, 10, Pablo Galindo Salgado)'

>>> cur.execute(sql)
Traceback (most recent call last):
  Cell In[7], line 1
    cur.execute(sql)
OperationalError: near "Galindo": syntax error
```

¿Qué ha ocurrido? Obtenemos un error porque el contenido de «release manager» `#!python 'Pablo Galindo Salgado'` es una cadena de texto y no puede contener espacios (en SQL).

Una solución a este problema sería detectar qué campos necesitan comillas e incorporarlas de forma manual. Pero una solución más robusta y efectiva es utilizar los «placeholders» de SQLite.

Un «placeholder»[^2] se introduce en la sentencia SQL y se sustituye a posteriori por el correspondiente valor indicado al ejecutar. La gran ventaja de este enfoque es que **no hay que preocuparse del tipo de dato** ya que el módulo `sqlite3` se encarga de introducir comillas o formatear según corresponda.

Veamos cómo sería la inserción anterior utilizando esta técnica, usando...

=== "«Placeholder» posicional"

    ```pycon hl_lines="6"
    >>> branch = 3.11
    >>> released_at_year = 2022
    >>> released_at_month = 10
    >>> release_manager = 'Pablo Galindo Salgado'

    >>> sql = 'INSERT INTO pyversions VALUES (?, ?, ?, ?)'#(1)!
    >>> cur.execute(sql, [
    ...    branch,
    ...    released_at_year,
    ...    released_at_month,
    ...    release_manager
    ... ])#(2)!
    <sqlite3.Cursor object at 0x1057d4240>
    ```
    { .annotate }
    
    1. Los «placeholders» se indican mediante **signos de interrogación** `?`.
    2. Los valores a sustituir (interpolar) se pasan mediante un **iterable**.

=== "«Placeholder» nominal"

    ```pycon hl_lines="6"
    >>> branch = 3.11
    >>> released_at_year = 2022
    >>> released_at_month = 10
    >>> release_manager = 'Pablo Galindo Salgado'

    >>> sql = 'INSERT INTO pyversions VALUES (:branch, :year, :month, :manager)'#(1)!
    >>> cur.execute(sql, {
    ...    'branch': branch,
    ...    'year': released_at_year,
    ...    'month': released_at_month,
    ...    'manager': release_manager
    ... })#(2)!
    <sqlite3.Cursor object at 0x1057d4240>
    ```
    { .annotate }
    
    1. Los «placeholders» se indican mediante **dos puntos y nombre**.
    2. Los valores a sustituir (interpolar) se pasan mediante un **diccionario**.
    
### Inserciones en lote { #batch-insert }

Quizás en un escenario más realista tendríamos datos en un formato tabular para cargarlos directamente en una tabla de SQLite.

Supongamos por <span class="example">ejemplo:material-flash:</span> que disponemos del siguiente fichero:

```csv title="pyversions.csv"
branch,year,month,manager
2.6,2008,10,Barry Warsaw
2.7,2010,7,Benjamin Peterson
3.0,2008,12,Barry Warsaw
3.1,2009,6,Benjamin Peterson
3.2,2011,2,Georg Brandl
3.3,2012,9,Georg Brandl
3.4,2014,3,Larry Hastings
3.5,2015,9,Larry Hastings
3.6,2016,12,Ned Deily
3.7,2018,6,Ned Deily
3.8,2019,10,Łukasz Langa
3.9,2020,10,Łukasz Langa
3.10,2021,10,Pablo Galindo Salgado
3.11,2022,10,Pablo Galindo Salgado
3.12,2023,10,Thomas Wouters
3.13,2024,10,Thomas Wouters
```

La primera aproximación que se nos podría venir a la cabeza es utilizar una [inserción parametrizada](#param-insert) por cada línea del fichero de entrada:

```pycon
>>> sql = 'INSERT INTO pyversions VALUES (?, ?, ?, ?)'

>>> with open('pyversions.csv') as f:
...     f.readline()#(1)!
...     for line in f:
...         pyversion = line.strip().split(',')
...         cur.execute(sql, pyversion)
...     con.commit()
...
```
{ .annotate }

1. Saltamos la cabecera.

Pero este módulo permite atacar el problema desde otro enfoque utilizando la función [`executemany()`](https://docs.python.org/es/3/library/sqlite3.html#sqlite3.Cursor.executemany).

Veamos una reimplementación del <span class="example">ejemplo:material-flash:</span> anterior, usando un...

=== "Iterable de listas"

    ```pycon hl_lines="25"
    >>> with open('pyversions.csv') as f:
    ...     f.readline()#(1)!
    ...     pyversions = [line.strip().split(',') for line in f]
    ...

    >>> pyversions#(2)!
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
     ['3.12', '2023', '10', 'Thomas Wouters'],
     ['3.13', '2024', '10', 'Thomas Wouters']]    
    
    >>> sql = 'INSERT INTO pyversions VALUES (?, ?, ?, ?)'#(3)!
    >>> cur.executemany(sql, pyversions)
    <sqlite3.Cursor object at 0x103432bc0>

    >>> con.commit()
    ```
    { .annotate }
    
    1. Saltamos la cabecera.
    2.  - Hemos conseguido generar una **lista de listas**.
        - Es posible que no veas la salida exactamente así. Si es el caso, puedes hacer lo siguiente:
            ```pycon
            >>> from pprint import pprint
            >>> pprint(pyversions)
            ```
    3. Utilizamos una [inserción parametrizada](#param-insert) usando «placeholders» posicionales.

=== "Iterable de diccionarios"

    ```pycon hl_lines="25"
    >>> with open('pyversions.csv') as f:
    ...     fields = f.readline().strip().split(',')#(1)!
    ...     pyversions = [{f: v for f, v in zip(fields, line.strip().split(','))} for line in f]
    ...

    >>> pyversions#(2)!
    [{'branch': '2.6', 'manager': 'Barry Warsaw', 'month': '10', 'year': '2008'},
     {'branch': '2.7', 'manager': 'Benjamin Peterson', 'month': '7', 'year': '2010'},
     {'branch': '3.0', 'manager': 'Barry Warsaw', 'month': '12', 'year': '2008'},
     {'branch': '3.1', 'manager': 'Benjamin Peterson', 'month': '6', 'year': '2009'},
     {'branch': '3.2', 'manager': 'Georg Brandl', 'month': '2', 'year': '2011'},
     {'branch': '3.3', 'manager': 'Georg Brandl', 'month': '9', 'year': '2012'},
     {'branch': '3.4', 'manager': 'Larry Hastings', 'month': '3', 'year': '2014'},
     {'branch': '3.5', 'manager': 'Larry Hastings', 'month': '9', 'year': '2015'},
     {'branch': '3.6', 'manager': 'Ned Deily', 'month': '12', 'year': '2016'},
     {'branch': '3.7', 'manager': 'Ned Deily', 'month': '6', 'year': '2018'},
     {'branch': '3.8', 'manager': 'Łukasz Langa', 'month': '10', 'year': '2019'},
     {'branch': '3.9', 'manager': 'Łukasz Langa', 'month': '10', 'year': '2020'},
     {'branch': '3.10', 'manager': 'Pablo Galindo Salgado', 'month': '10', 'year': '2021'},
     {'branch': '3.11', 'manager': 'Pablo Galindo Salgado', 'month': '10', 'year': '2022'},
     {'branch': '3.12', 'manager': 'Thomas Wouters', 'month': '10', 'year': '2023'},
     {'branch': '3.13', 'manager': 'Thomas Wouters', 'month': '10', 'year': '2024'}]
    
    >>> sql = 'INSERT INTO pyversions VALUES (:branch, :year, :month, :manager)'#(3)!
    >>> cur.executemany(sql, pyversions)
    <sqlite3.Cursor object at 0x103432bc0>

    >>> con.commit()
    ```
    { .annotate }
    
    1. Leemos los nombres de los campos desde la primera línea del fichero.
    2.  - Hemos conseguido generar una **lista de diccionarios**.
        - Es posible que no veas la salida exactamente así. Si es el caso, puedes hacer lo siguiente:
            ```pycon
            >>> from pprint import pprint
            >>> pprint(pyversions)
            ```
    3. Utilizamos una [inserción parametrizada](#param-insert) usando «placeholders» nominales.

En cualquiera de los casos anteriores el resultado sería el mismo y los registros quedan correctamente insertados en la base de datos:

```console
$ sqlite3 python.db "SELECT * FROM pyversions"
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
3.13|2024|10|Thomas Wouters
```

### Identificador de fila { #rowid }

En el comportamiento por defecto de una base de datos SQLite **todas las tablas disponen de una columna «oculta» denominada «rowid»** o _identificador de fila_.

Esta columna se va rellenando **de forma automática con valores enteros únicos** y puede utilizarse como ^^clave primaria^^ de los registros.

Para poder visualizar (o utilizar) esta columna es necesario indicarlo explícitamente en la consulta:

```console
$ sqlite3 python.db "SELECT rowid, * FROM pyversions"
1|2.6|2008|10|Barry Warsaw
2|2.7|2010|7|Benjamin Peterson
3|3.0|2008|12|Barry Warsaw
4|3.1|2009|6|Benjamin Peterson
5|3.2|2011|2|Georg Brandl
6|3.3|2012|9|Georg Brandl
7|3.4|2014|3|Larry Hastings
8|3.5|2015|9|Larry Hastings
9|3.6|2016|12|Ned Deily
10|3.7|2018|6|Ned Deily
11|3.8|2019|10|Łukasz Langa
12|3.9|2020|10|Łukasz Langa
13|3.10|2021|10|Pablo Galindo Salgado
14|3.11|2022|10|Pablo Galindo Salgado
15|3.12|2023|10|Thomas Wouters
16|3.13|2024|10|Thomas Wouters
```

### Cerrando la conexión { #con-close }

Al igual que ocurre con un fichero de texto, es necesario cerrar la conexión abierta para que se liberen los recursos asociados y se debloquee la base de datos.

La forma más directa de hacer esto sería:

```pycon
>>> con.close()
```

!!! warning "Transacciones pendientes"

    Si hay alguna transacción pendiente, esta no será guardada al cerrar la conexión con la base de datos, si previamente no se consolidan los cambios.

### Gestor de contexto { #context-manager }

En SQLite también es posible utilizar un [gestor de contexto](../../core/modularity/oop.md#context-manager) sobre la conexión, que funciona de la siguiente manera:

- :material-table-check:{.green} Si todo ha ido bien ejecutará un «commit» al final del bloque.
- :material-table-remove:{.red} Si ha habido alguna excepción ejecutará un «rollback»[^3] para que todo quede como al principio y deshacer los posibles cambios efectuados.

Analicemos el siguiente <span class="example">ejemplo:material-flash:</span>:

```pycon
>>> with con:
...     cur.execute('INSERT INTO pyversions VALUES ("3.12", 2023, 10, "Thomas Wouters")')
...     cur.execute('INSERT INTO pyversions VALUES ("3.12", 2024, 10, "Thomas Wouters")')
...
Traceback (most recent call last):
  Cell In[1], line 3
    cur.execute('INSERT INTO pyversions VALUES ("3.12", 2024, 10, "Thomas Wouters")')
IntegrityError: UNIQUE constraint failed: pyversions.branch
```

Se ha elevado una excepción de tipo `IntegrityError` indicando que hay valores duplicados en el campo `branch` ya que se trata de clave primaria y sus valores deben ser únicos. Pero dado que estamos en un gestor de contexto, se realiza un «rollback» de las acciones previas y la base de datos queda en el mismo estado anterior.

!!! tip "Excepciones"

    Es interesante conocer las distintas [excepciones](https://docs.python.org/es/3/library/sqlite3.html#exceptions) que pueden producirse al trabajar con este módulo a la hora del control de errores y de plantear posibles escenarios de mejora.

## Consultas { #queries }

A la hora de realizar consulas en `sqlite3` debemos tener en cuenta qué salida estamos buscando:

- Registros como tuplas.
- Registros como filas.

### Registros como tuplas { #tuple-records }

La ejecución de una consulta —desde un cursor— retorna un [objeto iterable](../../core/modularity/oop.md#iterables). Por defecto el contenido de dicho iterable son **tuplas** donde cada _tupla_ representa una fila de la tabla consultada.

Veamos un <span class="example">ejemplo:material-flash:</span> consultando toda la tabla `pyversions`:

```pycon
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
```

También tenemos la opción de utilizar las funciones [`fetchone()`](https://docs.python.org/es/3/library/sqlite3.html#sqlite3.Cursor.fetchone) y [`fetchall()`](https://docs.python.org/es/3/library/sqlite3.html#sqlite3.Cursor.fetchall) para obtener una o todas las filas de la consulta:

```pycon
>>> query = cur.execute('SELECT * FROM pyversions')

>>> query.fetchone()#(1)!
('2.6', 2008, 10, 'Barry Warsaw')

>>> query.fetchall()
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
```
{ .annotate }

1. Nótese que la llamada a `fetchone()` hace que quede «una fila menos» que recorrer. Es un comportamiento totalmente análogo al de la [lectura de una línea](../../core/datastructures/files.md#readline) en un fichero.

### Registros como filas { #row-records }

El módulo `sqlite3` también nos permite obtener los resultados de una consulta como objetos de tipo [`Row`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Row) lo que facilita **acceder a los valores** de cada registro tanto **por el índice como por el nombre** de la columna.

Para «activar» este modo tendremos que fijar el valor de la factoría de filas en la conexión:

```pycon hl_lines="2"
>>> con = sqlite3.connect('python.db')
>>> con.row_factory = sqlite3.Row
```

!!! info "Antes de consultar"

    Para que las consultas usen esta factoría hay que fijar el atributo `row_factory` **antes de crear el cursor** correspondiente. 

Veamos un <span class="example">ejemplo:material-flash:</span> consultando toda la tabla `pyversions`:

```pycon
>>> for row in cur.execute('SELECT * FROM pyversions'):
...     print(row)
...
<sqlite3.Row object at 0x10345c8e0>
<sqlite3.Row object at 0x103cc0940>
<sqlite3.Row object at 0x103bcbf10>
<sqlite3.Row object at 0x103cc0940>
<sqlite3.Row object at 0x10345c8e0>
<sqlite3.Row object at 0x103cc0940>
<sqlite3.Row object at 0x103bcbf10>
<sqlite3.Row object at 0x103cc0940>
<sqlite3.Row object at 0x10345c8e0>
<sqlite3.Row object at 0x103cc0940>
<sqlite3.Row object at 0x103bcbf10>
<sqlite3.Row object at 0x103cc0940>
<sqlite3.Row object at 0x10345c8e0>
<sqlite3.Row object at 0x103cc0940>
<sqlite3.Row object at 0x103bcbf10>
<sqlite3.Row object at 0x103cc0940>
```

Vemos que los objetos devueltos son de tipo `sqlite3.Row` pero no obtenemos gran información sobre su contenido.

A continuación se muestra el acceso a los valores del último objeto `sqlite3.Row` mediante...

=== "Nombre de columnas"

    ```pycon
    >>> row
    <sqlite3.Row object at 0x103cc0940>

    >>> row['branch']
    '3.13'
    >>> row['released_at_year']
    2024
    >>> row['released_at_month']
    10
    >>> row['release_manager']
    'Thomas Wouters'

    >>> row.keys()#(1)!
    ['branch', 'released_at_year', 'released_at_month', 'release_manager']
    ```
    { .annotate }
    
    1. Acceso a los nombres de los campos.

    Es posible desempaquetar la fila:

    ```pycon
    >>> branch, year, month, manager = row
    >>> branch, year, month, manager
    ('3.13', 2024, 10, 'Thomas Wouters') 
    ```

=== "Índice de columnas"

    ```pycon
    >>> row
    <sqlite3.Row object at 0x103cc0940>

    >>> row[0]
    '3.13'
    >>> row[1]
    2024
    >>> row[2]
    10
    >>> row[3]
    'Thomas Wouters'
    ```

    Es posible desempaquetar la fila:

    ```pycon
    >>> branch, year, month, manager = row
    >>> branch, year, month, manager
    ('3.13', 2024, 10, 'Thomas Wouters') 
    ```

!!! note "Funciones auxiliares"

    El modo `sqlite3.Row` también permite utilizar las funciones `fetchone()` y `fetchall()`.

### Números de filas { #num-rows }

Hay ocasiones en las que lo que necesitamos obtener no es el dato en sí mismo, sino el **número de filas vinculadas a una determinada consulta**. En este sentido hay varias alternativas:

=== "Utilizar herramientas Python"

    ```pycon
    >>> query = cur.execute('SELECT * FROM pyversions')
    >>> len(query.fetchall())
    16
    ```    

=== "Utilizar sentencias SQL"

    ```pycon
    >>> query = cur.execute('SELECT COUNT(*) FROM pyversions')
    >>> query.fetchone()[0]#(1)!
    16
    ```
    { .annotate }
    
    1. Sólo hay una columna (con el resultado de la «cuenta»).

    :material-check-all:{ .blue } Esta opción es deseable si lo único que necesitamos es obtener el número de filas afectadas, ya que así estaremos rebajando la carga de datos en la consulta.

### Comprobando si hay resultados { #check-results }

La aplicación del [operador morsa](../../core/controlflow/conditionals.md#walrus) en las consultas mediante `sqlite3` es muy habitual ya que facilita la comprobación de resultados.

Veamos una posible implementación en el siguiente <span class="example">ejemplo:material-flash:</span>...

=== "Consulta vacía"

    ```pycon hl_lines="6"
    >>> con = sqlite3.connect('python.db')
    >>> cur = con.cursor()
    
    >>> res = cur.execute('SELECT * FROM pyversions WHERE branch=4.0')
    
    >>> if row := res.fetchone():
    ...     print(row)
    ... else:
    ...     print('Empty query')
    ...
    Empty query
    ```

=== "Consulta con datos"

    ```pycon hl_lines="6"
    >>> con = sqlite3.connect('python.db')
    >>> cur = con.cursor()
    
    >>> res = cur.execute('SELECT * FROM pyversions WHERE branch=3.0')
    
    >>> if row := res.fetchone():
    ...     print(row)
    ... else:
    ...     print('Empty query')
    ...
    ('3.0', 2008, 12, 'Barry Warsaw')
    ```

## Otras funcionalidades { #features }

El módulo `sqlite3` dispone de otras funcionalidades realmente interesantes que serán analizadas en este apartado.

### Tablas en memoria { #memory }

Existe la posibilidad de trabajar con tablas en memoria sin necesidad de tener un fichero en disco.

Veamos un <span class="example">ejemplo:material-flash:</span> muy sencillo:

```pycon
>>> con = sqlite3.connect(':memory:')
>>> cur = con.cursor()

>>> sql = 'CREATE TABLE temp (id INTEGER PRIMARY KEY, value TEXT)'
>>> cur.execute(sql)
<sqlite3.Cursor object at 0x103b878c0>

>>> sql = 'INSERT INTO temp VALUES (1, "X")'
>>> cur.execute(sql)#(1)!
<sqlite3.Cursor object at 0x103b878c0>

>>> for row in cur.execute('SELECT * FROM temp'):
...     print(row)
...
(1, 'X')
```
{ .annotate }

1. Al utilizar tablas en memoria existe un «autocommit» por defecto.

Esta aproximación puede ser interesante para escenarios donde no nos importe la **persistencia**, ya que los datos no serán volcados a disco.

### Claves autoincrementales { #autoinc }

Es muy habitual encontrar en la definición de una tabla un **campo identificador numérico entero** que actúe como **clave primaria** y se le asignen valores automáticamente.

Para [implementar este esquema](https://www.sqlite.org/autoinc.html) en SQLite **debemos simplemente definir una columna de tipo** `INTEGER PRIMARY KEY`. A partir de ahí, en cualquier operación de inserción, si no especificamos un valor explícito para dicha columna, se rellenará automáticamente con un entero sin usar, típicamente uno más que el último valor generado.

A continuación se muestra un <span class="example">ejemplo:material-flash:</span> de aplicación de claves autoincrementales mediante una tabla en memoria que almacena **ciudades y sus geolocalizaciones**:

```pycon hl_lines="5"
>>> con = sqlite3.connect(':memory:')
>>> cur = con.cursor()

>>> cur.execute('''CREATE TABLE cities (
... id INTEGER PRIMARY KEY,
... city TEXT UNIQUE,
... latitude REAL,
... longitude REAL)''')
<sqlite3.Cursor at 0x107139bc0>

>>> cur.execute('''INSERT INTO
... cities (city, latitude, longitude)
... VALUES ("Tokyo", 35.652832, 139.839478)''')#(1)!
<sqlite3.Cursor at 0x107139bc0>

>>> result = cur.execute('SELECT * FROM cities')
>>> result.fetchall()
[(1, 'Tokyo', 35.652832, 139.839478)]

>>> cur.execute('''INSERT INTO
... cities (city, latitude, longitude)
... VALUES ("Barcelona", 41.390205, 2.154007)''')#(2)!
<sqlite3.Cursor at 0x107139bc0>

>>> result = cur.execute('SELECT * FROM cities')
>>> result.fetchall()
[(1, 'Tokyo', 35.652832, 139.839478),
 (2, 'Barcelona', 41.390205, 2.154007)]
```
{ .annotate }

1. Obviamos el campo `id`.
2. Obviamos el campo `id`.

### Copia de seguridad { #backup }

Es posible realizar copias de seguridad de manera programática. Veamos un <span class="example">ejemplo:material-flash:</span>[^4] donde copiamos dos bases de datos (ficheros):

```pycon hl_lines="8-9"
>>> def progress(status, remaining, total):
...     print(f'Copied {total-remaining} of {total} pages...')
...

>>> src = sqlite3.connect('python.db')
>>> dst = sqlite3.connect('backup.db')

>>> with dst:#(1)!
...     src.backup(dst, pages=1, progress=progress)#(2)!
...
Copied 1 of 3 pages...
Copied 2 of 3 pages...
Copied 3 of 3 pages...

>>> dst.close()
>>> src.close()
```
{ .annotate }

1. Se utiliza un [gestor de contexto](#context-manager).
2.  - El parámetro `pages` indica el número de páginas a copiar «de cada vez». Si este valor es menor o igual que 0, la base de datos se copia en un único paso. El valor por defecto es -1
    - El parámetro `progress` permite definir una función para mostrar algún tipo de indicación del progreso de la copia.

Tras la copia, podemos comprobar que ambas bases de datos tienen el mismo contenido:

```pycon
>>> src = sqlite3.connect('python.db')
>>> dst = sqlite3.connect('backup.db')

>>> with src, dst:#(1)!
...     src_cur = src.cursor()
...     dst_cur = dst.cursor()
...     sql = 'SELECT * FROM pyversions'
...     src_data = src_cur.execute(sql).fetchall()
...     dst_data = dst_cur.execute(sql).fetchall()
...     if src_data == dst_data:
...         print('Contents from both DBs are the same!')
...
Contents from both DBs are the same!
```
{ .annotate }

1. Es posible aplicar [gestores de contexto](#context-manager) sobre dos conexiones a la vez.

Este mecanismo de copia de seguridad funciona incluso...

- [x] Si la base de datos está siendo accedida por otros clientes o concurrentemente por la misma conexión.
- [x] Entre bases de datos `:memory:` y bases de datos en disco.

:material-check-all:{ .blue } Hacer directamente una copia del fichero `file.db` (desde el propio sistema operativo) también es una opción rápida para disponer de copias de seguridad.

### Información de filas { #rowinfo }

Cuando ejecutamos una **sentencia de modificación** sobre la base de datos podemos **obtener el número de filas afectadas**. Este dato lo sacamos del atributo `rowcount` del _cursor_ correspondiente.

Podemos comprobarlo en el siguiente <span class="example">ejemplo:material-flash:</span> de versiones de Python:

```pycon hl_lines="25-26"
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

>>> cur.rowcount#(1)!
16
```
{ .annotate }

1. 16 filas afectadas por la sentencia `UPDATE` de actualización de registros.

Igualmente al **insertar un registro** en la base de datos podemos **obtener cuál es el identificador de la últila fila insertada**:

```pycon hl_lines="4-5"
>>> cur.execute('INSERT INTO pyversions VALUES ("3.20", 2031, 10, "Guido van Rossum")')
<sqlite3.Cursor at 0x105593dc0>

>>> cur.lastrowid#(1)!
17
```
{ .annotate }

1.  - El identificador de la última fila insertada es 17.
    - También funciona si utilizamos una **clave primaria `INTEGER` personalizada** e insertamos un valor «manualmente» en dicha columna.

### Ejecución de scripts { #run-scripts }

¿Qué pasaría si intentamos **ejecutar varias sentencias SQL a la vez** con las herramientas que hemos visto hasta ahora?

A vueltas con el <span class="example">ejemplo:material-flash:</span> de las versiones de Python tendríamos lo siguiente:

```pycon hl_lines="18-22"
>>> con = sqlite3.connect(':memory:')
>>> cur = con.cursor()

>>> sql = """
... CREATE TABLE pyversions (
...     branch TEXT PRIMARY KEY,
...     released_at_year INTEGER,
...     released_at_month INTEGER,
...     release_manager TEXT
... );
...
... INSERT INTO pyversions VALUES("3.10", 2021, 10, "Pablo Galindo Salgado");
... INSERT INTO pyversions VALUES("3.11", 2022, 10, "Pablo Galindo Salgado");
... INSERT INTO pyversions VALUES("3.12", 2023, 10, "Thomas Wouters");
... INSERT INTO pyversions VALUES("3.13", 2024, 10, "Thomas Wouters");
... """

>>> cur.execute(sql)#(1)!
Traceback (most recent call last):
  Cell In[4], line 1
    cur.execute(sql)
ProgrammingError: You can only execute one statement at a time.
```
{ .annotate }

1. Lo que ocurre es que **obtenemos un error** indicando que sólo se puede ejecutar una sentencia cada vez.

Para resolver este problema disponemos de la función [`executescript()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executescript) que **permite ejecutar varias sentencias SQL de una sola vez**:

Volvemos a lanzar la misma sentencia SQL pero ahora utilizando este nuevo mecanismo:

```pycon hl_lines="1"
>>> cur.executescript(sql)#(1)!
<sqlite3.Cursor object at 0x1034a95c0>

>>> cur.execute('SELECT * FROM pyversions').fetchall()#(2)!
[('3.10', 2021, 10, 'Pablo Galindo Salgado'),
 ('3.11', 2022, 10, 'Pablo Galindo Salgado'),
 ('3.12', 2023, 10, 'Thomas Wouters'),
 ('3.13', 2024, 10, 'Thomas Wouters')]
```
{ .annotate }

1. Ejecutamos el script «de una sola vez».
2. Comprobamos que los datos se han insertado correctamente.

## Ejercicios { #exercises }

1. [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `todo`
2. [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `twitter`


[^1]: [Herramienta cliente de sqlite](https://www.sqlite.org/cli.html) para terminal.
[^2]: En programación, un «placeholder» es un valor temporal o marcador que se utiliza como sustituto de datos reales que se asignarán más adelante.
[^3]: En tecnologías de base de datos, un «rollback» o reversión es una operación que devuelve a la base de datos a algún estado previo.
[^4]: Ejemplo tomado de la documentación oficial de Python.
