---
icon: material/file-cabinet
tags:
  - Fundamentos del lenguaje
  - Estructuras de datos
  - Ficheros
---

# Ficheros { #files }

![Banner](images/files/banner.jpg)
/// caption
Imagen generada con Inteligencia Artificial
///

Aunque los ficheros encajarían más en un apartado de «entrada/salida» ya que representan un **medio de almacenamiento persistente**, también podrían ser vistos como _estructuras de datos_, puesto que nos permiten guardar información y asignarle un cierto formato.

Un **fichero** es un _conjunto de bytes_ almacenados en algún dispositivo. El [sistema de ficheros](https://bit.ly/405ABbw) es la estructura lógica que alberga los ficheros y está jerarquizado a través de _directorios_ (o carpetas). Cada fichero se **identifica unívocamente a través de una ruta** que nos permite acceder a él.

En esta sección nos centraremos en el manejo de **ficheros de texto plano** (aquellos que son entendibles por humanos). Pero también existen _ficheros binarios_ que Python es capaz de manejar.

Hay tres modos de apertura de un fichero:

- [x] [Lectura](#read).
- [x] [Escritura](#write).
- [x] [Añadido](#append).

## Lectura de un fichero { #read }

Para abrir un fichero en **modo lectura** utilizamos la función `#!python open()` con el modificador `#!python 'r'`.

En el siguiente <span class="example">ejemplo:material-flash:</span> vamos a leer el contenido de un fichero que contiene las **temperaturas mínimas y máximas** de cada día de la última semana en una región determinada:

```text title="store/temps.dat" linenums="1"
23 29
23 31
26 34
23 33
22 29
22 28
22 28
```

Abrir un fichero significa crear un objeto «manejador»[^1] que nos permita realizar operaciones sobre dicho fichero:

```pycon
>>> f = open('store/temps.dat', 'r')#(1)!
```
{ .annotate }

1. Es posible omitir `#!python 'r'` ya que el modo de apertura por defecto es _lectura_.

La función `#!python open()` recibe como primer argumento la **ruta al fichero** que queremos manejar (como un «string») y como segundo argumento el **modo de apertura** (también como un «string»). Nos **devuelve el manejador del fichero**, que en este caso lo estamos asignando a una variable llamada `f` pero le podríamos haber puesto cualquier otro nombre.

!!! note "Rutas relativas vs Rutas absolutas"

    Es importante dominar los conceptos de ruta relativa y ruta absoluta para el trabajo con ficheros (véase [este artículo](https://sanchezcorbalan.es/rutas-relativas-vs-rutas-absolutas/) de _Sánchez Corbalán_).

El **manejador del fichero** se implementa mediante un [flujo de entrada/salida](https://docs.python.org/es/3/library/io.html#io.TextIOWrapper) para las operaciones de lectura/escritura. Este objeto almacena, entre otras cosas, la ruta al fichero, el modo de apertura y la codificación:

```pycon
>>> f
<_io.TextIOWrapper name='store/temps.dat' mode='r' encoding='UTF-8'>
```

!!! tip "Codificaciones"

    Existen muchas [codificaciones de caracteres](https://es.wikipedia.org/wiki/Codificaci%C3%B3n_de_caracteres) para ficheros, pero la más utilizada es [UTF-8](https://es.wikipedia.org/wiki/UTF-8) ya que es capaz de representar cualquier caracter [Unicode](../datatypes/strings.md#unicode) al utilizar una longitud variable de 1 a 4 bytes.

Hay que tener en cuenta que **la ruta al fichero** que abrimos (en modo lectura) **debe existir**, ya que de lo contrario obtendremos un error:

```pycon hl_lines="5"
>>> f = open('foo.txt', 'r')
Traceback (most recent call last):
  Cell In[1], line 1
    f = open('foo.txt', 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'foo.txt'
```

Una vez abierto el fichero ya podemos proceder a leer su contenido. Para ello Python nos ofrece la posibilidad de leer todo el fichero de una vez o bien leerlo línea a línea.

### Lectura completa

Siguiendo nuestro <span class="example">ejemplo:material-flash:</span> de temperaturas, veamos cómo leer todo el contenido del fichero de una sola vez. Para esta operación, Python nos provee de dos funciones:

=== "`read()` :fontawesome-regular-file-text:"

    Devuelve todo el contenido del fichero como una única **cadena de texto**:

    ```pycon
    >>> f = open('store/temps.dat')
    
    >>> f.read()
    '23 29\n23 31\n26 34\n23 33\n22 29\n22 28\n22 28\n'
    ```

=== "`readlines()` :material-account-file-text-outline:"

    Devuelve todo el contenido del fichero como una **lista** donde cada elemento de la lista representa una línea del fichero:

    ```pycon
    >>> f = open('store/temps.dat')
    
    >>> f.readlines()
    ['23 29\n', '23 31\n', '26 34\n', '23 33\n', '22 29\n', '22 28\n', '22 28\n']
    ```

!!! warning "Saltos de línea"

    Nótese que, en ambos casos, los saltos de línea `#!python '\n'` siguen apareciendo en los datos leídos, por lo que habría que [limpiar](../datatypes/strings.md#strip) estos caracteres.

### Lectura línea a línea { #read-line-by-line }

Hay situaciones en las que interesa leer el contenido del fichero **línea a línea**. Imaginemos un fichero de tamaño considerable (varios GB). Si intentamos leer completamente este fichero de sola una vez podríamos ocupar demasiada RAM y reducir el rendimiento de nuestra máquina.

Es por ello que Python nos ofrece varias aproximaciones a la lectura de ficheros línea a línea. La más usada es ^^iterar sobre el propio manejador del fichero^^[^2].

Veamos cómo aplicarlo en el <span class="example">ejemplo:material-flash:</span> de las temperaturas:

```pycon
>>> f = open('store/temps.dat')

>>> for line in f:    # that easy!
...     print(line)#(1)!
...
23 29

23 31

26 34

23 33

22 29

22 28

22 28
```
{ .annotate }

1. Notése que cada línea tiene un «espacio de más» que proviene del propio `#!python print()`.

#### Enumerando líneas { #enumerate }

En ocasiones no sólo necesitamos recorrer cada línea del fichero sino también ir llevando un «índice» que nos indique el número de línea que estamos procesando.

Dado que los manejadores de ficheros también son **objetos iterables** podemos hacer uso de la función [`enumerate()`](lists.md#enumerate).

A continuación mostramos un <span class="example">ejemplo:material-flash:</span> donde aprovechamos esta característica para incluir los días de la semana en el fichero de temperaturas:

```pycon
>>> f = open('store/temps.dat')

>>> for line_no, line in enumerate(f, start=1):
...     print(f'D{line_no}: {line.strip()}')
...
D1: 23 29
D2: 23 31
D3: 26 34
D4: 23 33
D5: 22 29
D6: 22 28
D7: 22 28
```

### Lectura de una línea { #readline }

Es posible que sólo necesitemos leer una línea del fichero. Para ello Python nos ofrece la función `#!python readline()` que devuelve la «siguiente» línea del fichero.

Veamos cómo hacerlo con el <span class="example">ejemplo:material-flash:</span> del fichero de temperaturas:

```pycon
>>> f = open('store/temps.dat')

>>> f.readline()#(1)!
'23 29\n'
```
{ .annotate }

1. Devuelve una única línea, en este caso la primera del fichero.

:material-check-all:{ .blue } Es importante señalar que cuando utilizamos la función `#!python readline()` el ^^puntero de lectura^^ se desplaza hasta la siguiente línea del fichero. Este hecho nos permite seguir leyendo desde donde nos quedamos.

A continuación se muestra un trozo de código sobre el <span class="example">ejemplo:material-flash:</span> de las temperaturas en el que mezclamos ambas técnicas de lectura:

```pycon
>>> f = open('store/temps.dat')#(1)!

>>> for _ in range(3):#(2)!
...     print(f.readline().strip())
...
23 29
23 31
26 34

>>> for line in f:#(3)!
...     print(line.strip())
...
23 33
22 29
22 28
22 28
```
{ .annotate }

1. Puntero de lectura en la posición 0 del fichero.
2. Lectura de las 3 primeras líneas del fichero.
3. Lectura de las restantes líneas del fichero.

La función `#!python readline()` devuelve la **cadena vacía** cuando el _puntero de lectura_ ha llegado al final del fichero. Bajo esta premisa podríamos implementar una forma **poco ortodoxa** de leer un fichero:

```pycon
>>> f = open('store/temps.dat')

>>> while line := f.readline():
...     print(line.strip())
...
23 29
23 31
26 34
23 33
22 29
22 28
22 28
```

### Lectura con posicionamiento { #seek }

Hay que tener en cuenta que, una vez que leemos un fichero, no lo podemos volver a leer «directamente». O dicho de otra manera, el iterable que lleva implícito «se agota».

Analicemos este escenario con el <span class="example">ejemplo:material-flash:</span> anterior:

```pycon
>>> f = open('store/temps.dat')

>>> for line in f:#(1)!
...     print(line.strip(), end=' ')
...
23 29 23 31 26 34 23 33 22 29 22 28 22 28

>>> for line in f:#(2)!
...     print(line.strip(), end=' ')
```
{ .annotate }

1. Recorrido de todo el fichero línea a línea.
2.  - Al intentar recorre de nuevo el fichero no sale nada por pantalla.
    - El puntero de lectura ha llegado al final.

Aunque no es tan usual, existe la posibilidad de **volver a leer el fichero desde el principio** reposicionando el **puntero de lectura** mediante la función [`seek()`](https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects).

A continuación se muestra como <span class="example">ejemplo:material-flash:</span> una «doble» lectura del fichero de temperaturas:

```pycon hl_lines="8"
>>> f = open('store/temps.dat')

>>> for line in f:
...     print(line.strip(), end=' ')
...
23 29 23 31 26 34 23 33 22 29 22 28 22 28

>>> f.seek(0)#(1)!
0

>>> for line in f:
...     print(line.strip(), end=' ')
...
23 29 23 31 26 34 23 33 22 29 22 28 22 28
```
{ .annotate }

1.  - Situamos el puntero de lectura en el _byte_ 0.
    - Devuelve la posición absoluta (en _bytes_) en la que se encuentra el puntero de lectura.

??? tip "Posicionamiento relativo"

    La función [`seek()`](https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects) también permite indicar un **desplazamiento relativo** si se usa el segundo argumento.
    
    | Uso | Mover el puntero de lectura... |
    | --- | --- |
    | `#!python f.seek(10, 0)` | 10 _bytes_ desde el ^^principio del fichero^^ (`0`) `DEFAULT` |
    | `#!python f.seek(7, 1)` | 7 _bytes_ desde la ^^posición actual del puntero de lectura^^ (`1`) |
    | `#!python f.seek(-5, 2)` | 5 _bytes_ desde el ^^final del fichero^^ (`2`) |

## Escritura de un fichero { #write }

Para abrir un fichero en **modo escritura** utilizamos la función `#!python open()` con el modificador `#!python 'w'`.

A continuación vamos a implementar un <span class="example">ejemplo:material-flash:</span> para escribir en un fichero las temperaturas mínimas y máximas de la última semana en una región determinada.

Lo primero será abrir el fichero en modo escritura:

```pycon
>>> f = open('store/temps.dat', 'w')
```

:material-alarm-light:{.acc} La apertura de un fichero en _modo escritura_ ^^borrará todo el contenido^^ que contuviera.

??? failure "Ruta al fichero"

    Las carpetas (o directorios) intermedios hasta llegar al fichero indicado **deben existir** previamente. De lo contrario obtendremos un error:

    ```pycon hl_lines="6"
    >>> f = open('foo/bar/temps.dat', 'w')
    Traceback (most recent call last):
      Cell In[1], line 1
        f = open('foo/bar/temps.dat', 'w')
        return io_open(file, *args, **kwargs)
    FileNotFoundError: [Errno 2] No such file or directory: 'foo/bar/temps.dat'
    ```

Ahora supongamos que disponemos de una estructura de datos (_[tupla](./tuples.md) de tuplas_) con las temperaturas:

```pycon
>>> temps = (
...   (23, 29),
...   (23, 31),
...   (26, 34),
...   (23, 33),
...   (22, 29),
...   (22, 28),
...   (22, 28),
... )
```

Python proporciona la función (método) `#!python write()` para escribir en un fichero:

```pycon hl_lines="2 4"
>>> for min_temp, max_temp in temps:
...     f.write(f'{min_temp} {max_temp}\n')#(1)!
...
>>> f.close()#(2)!
```
{ .annotate }

1.  - Construimos un «f-string» con la cadena a escribir en el fichero.
    - No olvidarse del saltó de línea `#!python '\n'` para incluir cada línea.
2. Es fundamental cerrar el fichero, especialmente en modo escritura, ya que de lo contrario podríamos perder los datos.

Si tratáramos de escribir directamente las temperaturas (como enteros) en el fichero, obtendríamos un error:

```pycon hl_lines="8"
>>> for min_temp, max_temp in temps:
...     f.write(min_temp)#(1)!
...     f.write(max_temp)#(2)!
...
Traceback (most recent call last):
  Cell In[1], line 2
    f.write(min_temp)
TypeError: write() argument must be str, not int
```
{ .annotate }

1. La función `#!python write()` sólo admite _cadenas de texto_.
2. La función `#!python write()` sólo admite _cadenas de texto_.

!!! info "Escribiendo líneas"

    Python proporciona la función [`f.writelines()`](https://docs.python.org/3/library/io.html#io.IOBase.writelines) que nos permite escribir un _iterable_ de líneas al fichero de una sola vez. Los saltos de línea no se añaden automáticamente.

### Usando contextos { #contexts }

Python proporciona [gestores de contexto](../modularity/oop.md#context-manager) como aproximación al manejo de ficheros. En este escenario usaremos la sentencia `#!python with` y el contexto creado se ocupará de abrir y cerrar el fichero automáticamente (**incluso si ha habido cualquier error**).

Veamos cómo aplicarlo con el <span class="example">ejemplo:material-flash:</span> anterior de las temperaturas:

```pycon
>>> with open('store/temps.dat', 'w') as f:#(1)!
...     for min_temp, max_temp in temps:
...         f.write(f'{min_temp} {max_temp}\n')
...
```
{ .annotate }

1.  - Abrimos el fichero en modo escritura.
    - Creamos un objeto `f` como manejador.

!!! tip "Uso de contextos"

    Aunque estos contextos también se pueden utilizar en modo lectura, son ^^realmente importantes cuando escribimos datos en un fichero^^, ya que nos aseguran el cierre del mismo y evitamos pérdidas de datos.

#### Múltiples ficheros { #multiple-files }

Cuando tenemos que abrir varios ficheros utilizando _gestores de contexto_ tenemos dos opciones: **anidamiento** o **misma línea**:

=== "Anidamiento"

    ```python
    >>> with open('file1', 'w') as f1:
    ...     with open('file2', 'w') as f2:
    ...         # file management
    ```

=== "Misma línea"

    ```python
    >>> with open('file1', 'w') as f1, open('file2', 'w') as f2:
    ...     # file management
    ```

Esto vale tanto para apertura de ficheros en _modo lectura_ como en _modo escritura_.

### Añadiendo líneas { #append }

Añadir información a un fichero se podría ver como un _caso especial_ de escribir información; con la diferencia de que no podemos modificar el contenido previo, sino únicamente añadir nuevos datos.

Para abrir un fichero en **modo añadido** utilizamos la función `#!python open()` con el modificador `#!python 'a'`.

## Ejercicios { #exercises }

1. [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `wc`
2. [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `read-csv`
3. [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `txt2md`
4. [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `avg-temps`
5. [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `find-words`
6. [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `sum-matrix`
7. [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `longest-word`
8. [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `word-freq`
9. [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `get-line`
10. [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `replace-chars`
11. [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `histogram-txt`
12. [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `submarine`
13. [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `common-words`
14. [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `split-file`

[^1]: Es muy frecuente encontrar en la documentación el término «handler» para referirse al objeto manejador del fichero.
[^2]: Los manejadores de ficheros son estructuras de datos [iterables](../modularity/oop.md#iterables).
