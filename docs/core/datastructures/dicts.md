---
icon: material/code-braces
tags:
  - Fundamentos del lenguaje
  - Estructuras de datos
  - Diccionarios
---

# Diccionarios { #dicts }

![Banner](images/dicts/banner.jpg)
///caption
Imagen generada con Inteligencia Artificial
///

Podemos trasladar el concepto de _diccionario_ de la vida real al mundo Python. Al fin y al cabo un diccionario es un objeto que contiene palabras, y cada palabra tiene asociado un significado. Haciendo el paralelismo, diríamos que en Python un diccionario es también un objeto indexado por **claves** (las palabras) que tienen asociados unos **valores** (los significados).

![Dark image](images/dicts/dicts-dark.svg#only-dark)
![Light image](images/dicts/dicts-light.svg#only-light)

Los diccionarios en Python tienen las siguientes **características**:

- Mantienen el **orden** en el que se insertan las claves[^1].
- Son **mutables**, con lo que permiten añadir, borrar y modificar sus elementos.
- Las **claves** deben ser **únicas**. A menudo se utilizan las _cadenas de texto_ como claves, pero en realidad podría ser **cualquier tipo de datos inmutable**: enteros, flotantes, tuplas (entre otros).
- Tienen un **acceso muy rápido** a sus elementos, debido a la forma en la que están implementados internamente[^2].

!!! note "Hashes"

    En otros lenguajes de programación, a los diccionarios se les conoce como _arrays asociativos_, _«hashes»_ o _«hashmaps»_. Básicamente porque al final lo que utilizan es una [función hash](#hashables) para determinar la ubicación de las claves.

## Creando diccionarios { #create }

Para crear un diccionario usamos llaves `{}` rodeando asignaciones `clave: valor` que están separadas por comas.

Veamos algunos <span class="example">ejemplos:material-flash:</span> de diccionarios:

```pycon
>>> rae = {#(1)!
...     'bifronte': 'De dos frentes o dos caras',
...     'anarcoide': 'Que tiende al desorden',
...     'montuvio': 'Campesino de la costa'
... }

>>> population_can = {#(2)!
...     2015: 2_135_209,
...     2016: 2_154_924,
...     2017: 2_177_048,
...     2018: 2_206_901,
...     2019: 2_220_270
... }

>>> empty_dict = {}#(3)!
```
{ .annotate }

1. Un diccionario con claves [cadenas de texto](../datatypes/strings.md) y valores [cadenas de texto](../datatypes/strings.md).
2. Un diccionario con claves [números enteros](../datatypes/numbers.md#integers) y valores [números enteros](../datatypes/numbers.md#integers).
3. El **diccionario vacío** (_0 elementos_).

!!! exercise "Ejercicio"

    Entra en el intérprete interactivo de Python <span class="green">❯❯❯</span> y crea un diccionario con los nombres (como claves) de 5 personas de tu familia y sus edades (como valores).
    
## Conversión { #cast }

Para convertir otros tipos de datos en un diccionario podemos usar la función `#!python dict()`.

Veamos varios <span class="example">ejemplos:material-flash:</span> donde creamos un diccionario a partir de...

=== "... una lista de cadenas de texto"

    ```pycon
    >>> dict(['a1', 'b2'])
    {'a': '1', 'b': '2'}
    ```

=== "... una tupla de cadenas de texto"

    ```pycon
    >>> dict(('a1', 'b2'))
    {'a': '1', 'b': '2'}
    ```
    
=== "... una lista de listas"

    ```pycon
    >>> dict([['a', 1], ['b', 2]])
    {'a': 1, 'b': 2}
    ```

:material-check-all:{ .blue } Si nos fijamos bien, _cualquier iterable que tenga una estructura interna de 2 elementos_ es susceptible de convertirse en un diccionario a través de la función `#!python dict()`.

### Creando con `dict()` { #dict-create }

También es posible utilizar la función `#!python dict()` para crear dicionarios y no tener que utilizar llaves y comillas.

Planteemos un <span class="example">ejemplo:material-flash:</span> donde queremos transformar la siguiente tabla en un diccionario:

| Atributo | Valor |
| --- | --- |
| `name` | Guido |
| `surname` | van Rossum |
| `job` | Python creator |

Utilizando la construcción mediante `#!python dict()` podemos pasar ^^clave y valor^^ como **argumentos** de la función:

```pycon
>>> person = dict(
...     name='Guido',
...     surname='van Rossum',
...     job='Python creator'
... )

>>> person
{'name': 'Guido', 'surname': 'van Rossum', 'job': 'Python creator'}
```

El inconveniente que tiene esta aproximación es que las **claves deben ser identificadores válidos** en Python. Por <span class="example">ejemplo:material-flash:</span> no se permiten espacios:

```pycon hl_lines="7"
>>> person = dict(
...     name='Guido van Rossum',
...     date of birth='31/01/1956'
  Cell In[1], line 1
    person = dict(
                 ^
SyntaxError: '(' was never closed
```

### Creando con relleno { #dict-filled }

Python permite crear un diccionario especificando sus claves y un único valor de «relleno» utilizando la función [`fromkeys()`](https://docs.python.org/3/library/stdtypes.html#dict.fromkeys).

Por <span class="example">ejemplo:material-flash:</span> creemos un diccionario para almacenar el «rating» (valoración) de productos en una tienda de comercio online (inicialmente tendrán 0):

```pycon
>>> dict.fromkeys(['portátil', 'nevera', 'ventilador', 'monitor'], 0)
{'portátil': 0, 'nevera': 0, 'ventilador': 0, 'monitor': 0}
```

!!! note "Sobre cualquier iterable"

    Es posible aplicar `fromkeys()` sobre **cualquier iterable** con referencia a las claves.

## Operaciones con diccionarios { #operations }

Existen multitud de operaciones que se pueden realizar sobre diccionarios. A continuación veremos la mayoría de ellas:

### Obtener un elemento { #get-item }

Para obtener un elemento (valor de una clave) de un diccionario basta con **escribir la clave entre corchetes**.

Veamos un <span class="example">ejemplo:material-flash:</span>:

```pycon hl_lines="7"
>>> rae = {
...     'bifronte': 'De dos frentes o dos caras',
...     'anarcoide': 'Que tiende al desorden',
...     'montuvio': 'Campesino de la costa'
... }

>>> rae['anarcoide']
'Que tiende al desorden'
```

Si intentamos acceder a una clave que no existe, obtendremos un error de tipo [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError):

```pycon hl_lines="5"
>>> rae['acceso']
Traceback (most recent call last):
  Cell In[1], line 1
    rae['acceso']
KeyError: 'acceso'
```

#### Usando `get()` { #get }

Existe una función muy útil para «superar» los posibles errores de acceso por claves inexistentes. Se trata de `#!python get()` y su comportamiento es el siguiente:

1. Si la clave que buscamos existe, nos devuelve su valor.
2. Si la clave que buscamos no existe, nos devuelve `#!python None` salvo que le indiquemos otro valor por defecto, pero en ninguno de los dos casos obtendremos un error.

Veamos un <span class="example">ejemplo:material-flash:</span> de cada uno de los escenarios indicados:

```pycon
>>> rae
{'bifronte': 'De dos frentes o dos caras',
 'anarcoide': 'Que tiende al desorden',
 'montuvio': 'Campesino de la costa'}

>>> rae.get('bifronte')#(1)!
'De dos frentes o dos caras'

>>> rae.get('programación')#(2)!

>>> rae.get('programación', 'No disponible')#(3)!
'No disponible'
```
{ .annotate }

1. La clave existe y se devuelve su valor.
2. La clave no existe y se devuelve `#!python None` (no aparece nada en la salida).
3. La clave no existe pero aportamos un valor por defecto.

### Añadir o modificar un elemento { #add-modify }

Para añadir un elemento a un diccionario sólo es necesario hacer referencia a la _clave_ y asignarle un _valor_:

- Si la clave **ya existía** en el diccionario, **se reemplaza** el valor existente por el nuevo.
- Si la clave **es nueva**, **se añade** al diccionario con su valor. _No vamos a obtener un error a diferencia de las listas_.

Partimos del siguiente diccionario de <span class="example">ejemplo:material-flash:</span> para mostrar ambos escenarios:

```pycon
rae = {
...     'bifronte': 'De dos frentes o dos caras',
...     'anarcoide': 'Que tiende al desorden',
...     'montuvio': 'Campesino de la costa'
... }
```

=== "Añadir elemento :octicons-diff-added-24:"

    ```pycon
    >>> rae['enjuiciar'] = 'Someter una cuestión a examen, discusión y juicio'

    >>> rae
    {'anarcoide': 'Que tiende al desorden',
     'bifronte': 'De dos frentes o dos caras',
     'enjuiciar': 'Someter una cuestión a examen, discusión y juicio',
     'montuvio': 'Campesino de la costa'}
    ```
    
=== "Modificar elemento :fontawesome-solid-down-left-and-up-right-to-center:"

    ```pycon
    >>> rae['enjuiciar'] = 'Instruir, juzgar o sentenciar una causa'

    >>> rae
    {'anarcoide': 'Que tiende al desorden',
     'bifronte': 'De dos frentes o dos caras',
     'enjuiciar': 'Instruir, juzgar o sentenciar una causa',
     'montuvio': 'Campesino de la costa'}
    ```

#### Patrón creación { #create-pattern }

Una forma muy habitual de trabajar con diccionarios es empezar con uno vacío e ir añadiendo elementos poco a poco. Se podría hablar de un **patrón creación**.

A continuación se muestra un <span class="example">ejemplo:material-flash:</span> de creación de un diccionario donde las **claves** son las **letras vocales** y los **valores** son sus [códigos UNICODE](../datatypes/strings.md#unicode):

```pycon
>>> VOWELS = 'aeiou'

>>> cvowels = {}

>>> for vowel in VOWELS:
...     cvowels[vowel] = ord(vowel)
...

>>> cvowels
{'a': 97, 'e': 101, 'i': 105, 'o': 111, 'u': 117}
```

!!! exercise "Ejercicio"

    [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `extract-cities`

### Pertenencia de una clave { #in }

La forma **pitónica** de comprobar la existencia de una ^^clave^^ dentro de un diccionario, es utilizar el operador `#!python in`:

```pycon
>>> 'bifronte' in rae
True

>>> 'almohada' in rae
False

>>> 'montuvio' not in rae
False
```

!!! note "Booleano"

    El operador `#!python in` siempre devuelve un valor _booleano_, es decir, verdadero o falso.

!!! exercise "Ejercicio"

    [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `count-letters`

### Longitud de un diccionario { #length }

Podemos conocer el número de elementos («clave-valor») que tiene un diccionario mediante la función `#!python len()`:

```pycon
>>> rae
{'bifronte': 'De dos frentes o dos caras',
 'anarcoide': 'Que tiende al desorden',
 'montuvio': 'Campesino de la costa',
 'enjuiciar': 'Instruir, juzgar o sentenciar una causa'}

>>> len(rae)
4
```

### Obtener todos los elementos { #get-items }

Python ofrece mecanismos para obtener todos los elementos de un diccionario.

Partimos del siguiente diccionario de <span class="example">ejemplo:material-flash:</span> para ilustrar estos mecanismos:

```pycon
>>> rae
{'anarcoide': 'Que tiende al desorden',
 'bifronte': 'De dos frentes o dos caras',
 'enjuiciar': 'Instruir, juzgar o sentenciar una causa',
 'montuvio': 'Campesino de la costa'}
```

=== "Obtener claves :octicons-key-16:"

    ```pycon
    >>> rae.keys()
    dict_keys(['bifronte', 'anarcoide', 'montuvio', 'enjuiciar'])
    ```

=== "Obtener valores :material-content-save:"

    ```pycon
    >>> rae.values()
    dict_values([
        'De dos frentes o dos caras',
        'Que tiende al desorden',
        'Campesino de la costa',
        'Instruir, juzgar o sentenciar una causa'
    ])
    ```

=== "Obtener claves y valores :octicons-key-16::material-content-save:"

    ```pycon
    >>> rae.items()
    dict_items([
        ('bifronte', 'De dos frentes o dos caras'),
        ('anarcoide', 'Que tiende al desorden'),
        ('montuvio', 'Campesino de la costa'),
        ('enjuiciar', 'Instruir, juzgar o sentenciar una causa')
    ])
    ```

    :material-check-all:{ .blue } Cabe destacar que los «items» se devuelven como una **[lista](./lists.md) de [tuplas](./tuples.md)**, donde cada tupla contiene dos elementos: el primero representa la **clave** y el segundo representa el **valor**.

### Iterar sobre un diccionario { #iterate }    

En función de los [elementos que podemos obtener](#get-items), Python proporciona tres maneras de iterar sobre un diccionario:

=== "Iterar sobre claves :octicons-key-16:"

    ```pycon
    >>> for word in rae.keys():
    ...     print(word)
    ...
    bifronte
    anarcoide
    montuvio
    enjuiciar
    ```

=== "Iterar sobre valores :material-content-save:"

    ```pycon
    >>> for meaning in rae.values():
    ...     print(meaning)
    ...
    De dos frentes o dos caras
    Que tiende al desorden
    Campesino de la costa
    Instruir, juzgar o sentenciar una causa
    ```

=== "Iterar sobre claves y valores :octicons-key-16::material-content-save:"

    ```pycon
    >>> for word, meaning in rae.items():
    ...     print(f'{word}: {meaning}')#(1)!
    ...
    bifronte: De dos frentes o dos caras
    anarcoide: Que tiende al desorden
    montuvio: Campesino de la costa
    enjuiciar: Instruir, juzgar o sentenciar una causa
    ```
    { .annotate }
    
    1. Recuerda el uso de los [«f-strings»](../../core/datatypes/strings.md#fstrings) para formatear cadenas de texto.

!!! exercise "Ejercicio"

    [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `avg-population`

### Borrar elementos { #remove }

Python nos ofrece varios mecanismos para borrar elementos en un diccionario:

=== "Por su clave :octicons-key-16:"

    ```pycon hl_lines="7"
    >>> rae = {
    ...     'bifronte': 'De dos frentes o dos caras',
    ...     'anarcoide': 'Que tiende al desorden',
    ...     'montuvio': 'Campesino de la costa'
    ... }
    
    >>> del rae['bifronte']
    
    >>> rae
    {'anarcoide': 'Que tiende al desorden', 'montuvio': 'Campesino de la costa'}
    ```

=== "Por su clave (con extracción) :material-party-popper:"

    ```pycon hl_lines="7"
    >>> rae = {
    ...     'bifronte': 'De dos frentes o dos caras',
    ...     'anarcoide': 'Que tiende al desorden',
    ...     'montuvio': 'Campesino de la costa'
    ... }
    
    >>> rae.pop('anarcoide')#(1)!
    'Que tiende al desorden'
    
    >>> rae
    {'bifronte': 'De dos frentes o dos caras', 'montuvio': 'Campesino de la costa'}
    
    >>> rae.pop('anarcoide')#(2)!
    Traceback (most recent call last):
      Cell In[1], line 1
        rae.pop('anarcoide')
    KeyError: 'anarcoide'
    ```
    { .annotate }
    
    1. `#!python pop()` extrae la clave (y el valor) indicados.
    2. Si una clave no existe obtenemos un error de tipo [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError).

=== "Borrado completo :material-eraser:"

    ```pycon hl_lines="7"
    >>> rae = {
    ...     'bifronte': 'De dos frentes o dos caras',
    ...     'anarcoide': 'Que tiende al desorden',
    ...     'montuvio': 'Campesino de la costa'
    ... }
    
    >>> rae.clear()#(1)!
    
    >>> rae
    {}
    ```
    { .annotate }
    
    1. Se borra la zona de memoria existente.

=== "Borrado completo (reasignado) :octicons-trash-16:"

    ```pycon hl_lines="7"
    >>> rae = {
    ...     'bifronte': 'De dos frentes o dos caras',
    ...     'anarcoide': 'Que tiende al desorden',
    ...     'montuvio': 'Campesino de la costa'
    ... }
    
    >>> rae = {}#(1)!
    
    >>> rae
    {}
    ```    
    { .annotate }
    
    1. Se busca una nueva zona de memoria vacía.

!!! exercise "Ejercicio"

    [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `merge-dicts`

### Combinar diccionarios { #combine }

Dados dos (o más) diccionarios, es posible «mezclarlos» para obtener una combinación de los mismos. Esta combinación se basa en dos premisas:

- [x] Si la clave no existe, se añade con su valor.
- [x] Si la clave ya existe, se añade con el valor del «último»[^3] diccionario en la mezcla.

Partiendo de los siguientes diccionarios vamos a mostrar <span class="example">ejemplos:material-flash:</span> sobre los mecanismos que ofrece Python para combinar diccionarios:

```pycon
>>> rae1 = {
...     'bifronte': 'De dos frentes o dos caras',
...     'enjuiciar': 'Someter una cuestión a examen, discusión y juicio'
... }

>>> rae2 = {
...     'anarcoide': 'Que tiende al desorden',
...     'montuvio': 'Campesino de la costa',
...     'enjuiciar': 'Instruir, juzgar o sentenciar una causa'
... }
```

=== "Sin modificar los diccionarios originales :material-silverware-clean:"

    ```pycon
    >>> rae1 | rae2#(1)!
    {'bifronte': 'De dos frentes o dos caras',
     'enjuiciar': 'Instruir, juzgar o sentenciar una causa',
     'anarcoide': 'Que tiende al desorden',
     'montuvio': 'Campesino de la costa'}
    ```
    { .annotate }
    
    1. En versiones anteriores a <span class="pyversion"><a href="https://docs.python.org/3.9/">Python <span class="version">:octicons-tag-24: 3.9</span></a></span> habría que utilizar: `#!python {**rae1, **rae2}`

=== "Modificando los diccionarios originales :material-message-arrow-right-outline:"

    ```pycon
    >>> rae1.update(rae2)
    
    >>> rae1
    {'bifronte': 'De dos frentes o dos caras',
     'enjuiciar': 'Instruir, juzgar o sentenciar una causa',
     'anarcoide': 'Que tiende al desorden',
     'montuvio': 'Campesino de la costa'}
    ```

??? tip "Orden de la mezcla"

    Hay que tener en cuenta el orden en el que especificamos los diccionarios a la hora de su combinación (mezcla) ya que es relevante en el resultado final. En este caso _el orden de los factores sí altera el producto_.

## Cuidado con las copias { #copy }

Al igual que [ocurría con las listas](lists.md#copy), si hacemos un cambio en un diccionario, se verá reflejado en todas las variables que hagan referencia al mismo. Esto se deriva de su propiedad de ser _mutable_.

Veamos un <span class="example">ejemplo:material-flash:</span> concreto:

```pycon hl_lines="12 17"
>>> original_rae = {
...     'bifronte': 'De dos frentes o dos caras',
...     'anarcoide': 'Que tiende al desorden',
...     'montuvio': 'Campesino de la costa'
... }

>>> copy_rae = original_rae#(1)!

>>> original_rae['bifronte'] = 'bla bla bla'#(2)!

>>> original_rae
{'bifronte': 'bla bla bla',
 'anarcoide': 'Que tiende al desorden',
 'montuvio': 'Campesino de la costa'}

>>> copy_rae
{'bifronte': 'bla bla bla',
 'anarcoide': 'Que tiende al desorden',
 'montuvio': 'Campesino de la costa'}
```
{ .annotate }

1. Con esta asignación, ambas variables (nombres) quedan apuntando a la misma zona de memoria.
2. Esta modificación se realiza sobre la misma zona de memoria, lo que afecta a ambas variables.

Una **posible solución** a este problema es hacer una «copia dura». Para ello Python proporciona la función `#!python copy()`:

```pycon hl_lines="9 12 17"
>>> original_rae = {
...     'bifronte': 'De dos frentes o dos caras',
...     'anarcoide': 'Que tiende al desorden',
...     'montuvio': 'Campesino de la costa'
... }

>>> copy_rae = original_rae.copy()#(1)!

>>> original_rae['bifronte'] = 'bla bla bla'#(2)!

>>> original_rae
{'bifronte': 'bla bla bla',
'anarcoide': 'Que tiende al desorden',
'montuvio': 'Campesino de la costa'}

>>> copy_rae
{'bifronte': 'De dos frentes o dos caras',
 'anarcoide': 'Que tiende al desorden',
 'montuvio': 'Campesino de la costa'}
```
{ .annotate }

1. La copia se realiza en zonas de memoria distintas.
2. Esta modificación ya no afecta a ambas variables, al estar segmentadas en memoria.

??? warning "Copia profunda"

    En el caso de que estemos trabajando con diccionarios que contienen elementos mutables, debemos hacer uso de la función `#!python deepcopy()` dentro del módulo `copy` de la librería estándar.

## Diccionarios por comprensión { #comprehension }

De forma análoga a cómo se escriben las [listas por comprensión](lists.md#comprehension), podemos aplicar este método a los diccionarios usando llaves `{ }`.

Veamos un <span class="example">ejemplo:material-flash:</span> en el que creamos un **diccionario por comprensión** donde las claves son palabras y los valores son sus longitudes:

```pycon hl_lines="3"
>>> words = ('sun', 'space', 'rocket', 'earth')

>>> words_length = {word: len(word) for word in words}

>>> words_length
{'sun': 3, 'space': 5, 'rocket': 6, 'earth': 5}
```

También podemos aplicar **condiciones** a estas comprensiones. Continuando con el <span class="example">ejemplo:material-flash:</span> anterior, podemos incorporar la restricción de sólo incluir palabras que no empiecen por vocal:

```pycon hl_lines="3"
>>> words = ('sun', 'space', 'rocket', 'earth')

>>> words_length = {w: len(w) for w in words if w[0] not in 'aeiou'}

>>> words_length
{'sun': 3, 'space': 5, 'rocket': 6}
```

??? info "PEP-274"

    Se puede consultar el [PEP-274](https://www.python.org/dev/peps/pep-0274/) para ver más ejemplos sobre diccionarios por comprensión.

!!! exercise "Ejercicio"

    [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `split-marks`

## Objetos «hashables» { #hashables }

La única restricción que deben cumplir las **claves** de un diccionario es ser **«hashables»**. Un objeto es «hashable» si se le puede asignar un valor «hash» que no cambia en ejecución durante toda su vida.

Para encontrar el «hash» de un objeto, Python usa la función `#!python hash()`, que devuelve un número entero y es utilizado para indexar la tabla «hash» que se mantiene internamente:

```pycon
>>> hash(999)
999

>>> hash(3.14)
322818021289917443

>>> hash('hello')#(1)!
-8103770210014465245

>>> hash(('a', 'b', 'c'))
-2157188727417140402
```
{ .annotate }

1. La función «built-in» `hash()` realmente hace una llamada al método mágico `__hash__()` del objeto en cuestión: `#!python 'hello'.__hash__()`

Para que un objeto sea «hashable», debe ser de un **tipo inmutable**:

```pycon hl_lines="5"
>>> hash(['a', 'b', 'c'])
Traceback (most recent call last):
  Cell In[1], line 1
    hash(['a', 'b', 'c'])
TypeError: unhashable type: 'list'
```

!!! success "Claves inmutables"

    De lo anterior se deduce que las claves de los diccionarios, al tener que ser «hashables», sólo pueden ser objetos inmutables.

## Ejercicios

1.  [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `group-words`
2.  [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `same-dict-values`
3.  [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `dict-from-list`
4.  [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `clear-dict-values`
5.  [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `fix-keys`
6.  [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `order-stock`
7.  [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `inventory-updates`
8.  [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `sort-dict`
9.  [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `money-back`
10. [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `money-back-max`
11. [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `first-ntimes`
12. [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `fix-id`
13. [pypas](../../third-party/learning/pypas.md) &nbsp;:fontawesome-solid-hand-holding-heart:{ .acc .slide } `dict-pull`



[^1]: «Los diccionarios preservan el orden de inserción» extraído de la [documentación oficial de Python sobre diccionarios](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict).
[^2]: Artículo de Ramil Suleimanov sobre [«Por qué los diccionarios en Python son tan rápidos»](https://medium.com/@r_suleimanov/why-is-python-dict-so-fast-555e330a8ded).
[^3]: En este contexto «último» significa el que esté más a la derecha en la sentencia de asignación.
