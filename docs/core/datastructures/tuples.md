---
icon: octicons/link-16
tags:
  - Fundamentos del lenguaje
  - Estructuras de datos
  - Tuplas
---

# Tuplas { #tuples }

![Banner](images/tuples/banner.jpg)
/// caption
Imagen generada con Inteligencia Artificial
///

El concepto de **tupla** es muy similar al de [lista](lists.md). Aunque hay algunas diferencias menores, lo fundamental es que, mientras una _lista_ es mutable y se puede modificar, una _tupla_ no admite cambios y por lo tanto, es **inmutable**.

## Creando tuplas { #create }

Podemos pensar en crear tuplas tal y como [lo hacíamos con listas](lists.md#create), pero usando **paréntesis** en lugar de _corchetes_:

```pycon
>>> tenerife_geoloc = (28.46824, -16.25462)#(1)!

>>> three_wise_men = ('Melchor', 'Gaspar', 'Baltasar')#(2)!

>>> empty_tuple = ()#(3)!

>>> data = ('Welcome', 17, [0.1, 0.2], True)#(4)!
```
{ .annotate }

1. Una tupla de 2 [números flotantes](../datatypes/numbers.md#floats) representando _latitud_ y _longitud_.
2. Una tupla de 3 [cadenas de texto](../datatypes/strings.md).
3. La **tupla vacía** (_0 elementos_).
4. Una tupla **heterogénea** de 4 elementos de distinta naturaleza.

### Tuplas de un elemento

Hay que prestar especial atención cuando vamos a crear una **tupla de un único elemento**:

=== "Forma incorrecta :material-thumb-down:"

    La intención primera sería hacerlo de la siguiente manera:

    ```pycon
    >>> one_item_tuple = ('Papá Noel')#(1)!

    >>> one_item_tuple
    'Papá Noel'

    >>> type(one_item_tuple)#(2)!
    str
    ```
    { .annotate }

    1. Los paréntesis se ignoran en este contexto.
    2. Lo que hemos creado realmente es una _cadena de texto_.

=== "Forma correcta :material-thumb-up:"

    Para crear una tupla de un elemento debemos **añadir una coma al final**:

    ```pycon hl_lines="1"
    >>> one_item_tuple = ('Papá Noel',)

    >>> one_item_tuple
    ('Papá Noel',)

    >>> type(one_item_tuple)
    tuple
    ```

### Tuplas sin paréntesis

Según el caso, hay veces que nos podemos encontrar con tuplas que no llevan paréntesis. Quizás no está tan extendido, pero a efectos prácticos tiene el mismo resultado.

Veamos algunos <span class="example">ejemplos:material-flash:</span> de ello:

```pycon
>>> one_item_tuple = 'Papá Noel',

>>> three_wise_men = 'Melchor', 'Gaspar', 'Baltasar'

>>> tenerife_geoloc = 28.46824, -16.25462
```

## Conversión

Para convertir otros tipos de datos en una tupla podemos usar la función `tuple()`. Por <span class="example">ejemplo:material-flash:</span> podemos convertir una _lista_ en una tupla:

```pycon
>>> shopping = ['Agua', 'Aceite', 'Arroz']

>>> tuple(shopping)
('Agua', 'Aceite', 'Arroz')
```

Esta conversión es válida para aquellos tipos de datos que sean **iterables**: cadenas de caracteres, listas, diccionarios, conjuntos, etc.

Un <span class="example">ejemplo:material-flash:</span> que no funciona es intentar _convertir un número en una tupla_:

```pycon hl_lines="5"
>>> tuple(5)
Traceback (most recent call last):
  Cell In[1], line 1
    tuple(5)
TypeError: 'int' object is not iterable
```

??? warning "Nombre de variable"

    Aunque está permitido, no suele ser una buena práctica llamar `tuple` a una variable ya que destruirías la función que nos permite trabajar con tuplas. Tampoco parece muy razonable utilizar nombres como `<algo>_tuple` o `tuple_<algo>` ya que no es necesario incluir en el nombre de una variable su propia naturaleza.

## Modificar una tupla { #modify }

Como se ha comentado al principio de este capítulo, las tuplas son **estructuras de datos inmutables**. Una vez que las creamos con un valor, no podemos modificarlas.

Veamos qué ocurre en el siguiente <span class="example">ejemplo:material-flash:</span> donde queremos suplantar al Rey Mago _Melchor_:

```pycon hl_lines="7"
>>> three_wise_men = 'Melchor', 'Gaspar', 'Baltasar'

>>> three_wise_men[0] = 'Tom Hanks'
Traceback (most recent call last):
  Cell In[2], line 1
    three_wise_men[0] = 'Tom Hanks'
TypeError: 'tuple' object does not support item assignment
```
    
## Operaciones con tuplas { #operations }

Con las tuplas podemos realizar [todas las operaciones que vimos con listas](lists.md#operations) **salvo las que conlleven una modificación** «in-situ» de la misma:

- `reverse()`
- `append()`
- `extend()`
- `remove()`
- `clear()`
- `sort()`

Un par de detalles:

<div class="annotate" markdown>
- Sí es posible aplicar `sorted()` o `reversed()` sobre una tupla ya que no estamos modificando su valor sino creando un nuevo objeto.(1)
- La comparación de tuplas funciona exactamente igual que la [comparación de listas](lists.md#compare).
</div>
1. Estas funciones devuelven **una lista** en vez de una tupla.

## Desempaquetado de tuplas { #unpack }

El **desempaquetado** es una característica de las tuplas que nos permite **asignar una tupla a variables independientes**:

![Dark image](images/tuples/tuple-unpacking-dark.svg#only-dark)
![Light image](images/tuples/tuple-unpacking-light.svg#only-light)

Veamos un <span class="example">ejemplo:material-flash:</span> desempaquetando a los tres Reyes Magos:

```pycon hl_lines="3"
>>> three_wise_men = ('Melchor', 'Gaspar', 'Baltasar')

>>> king1, king2, king3 = three_wise_men

>>> king1
'Melchor'
>>> king2
'Gaspar'
>>> king3
'Baltasar'
```

Veamos otro <span class="example">ejemplo:material-flash:</span> en el que utilizamos la función «built-in» [`divmod()`](https://docs.python.org/3/library/functions.html#divmod) que devuelve el cociente y el resto de una división usando una única llamada. Lo interesante (para el caso que nos ocupa) es que se suele utilizar el desempaquetado de tuplas para obtener los valores por separado:

```pycon
>>> quotient, remainder = divmod(7, 3)#(1)!

>>> quotient
2
>>> remainder
1
```
{ .annotate }

1.  
    ```
    7 │ 3
      └————
    1   2
    ```

### Intercambio de valores { #swap-values }

Veamos cómo implementar el intercambio de los valores de dos variables:

=== "Forma «tradicional» :material-town-hall:"

    Necesitamos usar una variable intermedia $z$ para no perder valores:

    ```pycon hl_lines="4"
    >>> a = 1
    >>> b = 2

    >>> z = a

    >>> a = b
    >>> b = z

    >>> a
    2
    >>> b
    1
    ```

=== "Forma directa :material-sign-direction:"

    Usando desempaquetado podemos hacerlo de forma directa:

    ```pycon hl_lines="4"
    >>> a = 1
    >>> b = 2

    >>> a, b = b, a

    >>> a
    2
    >>> b
    1
    ```
    
### Desempaquetado extendido { #extended-unpacking }

No tenemos que ceñirnos a realizar desempaquetado uno a uno. También podemos extenderlo e indicar ciertos **«grupos» de elementos** mediante el operador `*`.

Veamos posibles implementaciones del _desempaquetado extendido_ en un <span class="example">ejemplo:material-flash:</span> de «ranking» de lenguajes de programación:

=== "Primero, otros y último"

    ```pycon hl_lines="3"
    >>> ranking = ('Python', 'Java', 'C', 'TypeScript', 'Rust')

    >>> first, *others, last = ranking

    >>> first
    'Python'
    >>> others
    ['Java', 'C', 'TypeScript']
    >>> last
    'Rust'
    ```
    
=== "Primero y otros"

    ```pycon hl_lines="3"
    >>> ranking = ('Python', 'Java', 'C', 'TypeScript', 'Rust')

    >>> first, *others = ranking

    >>> first
    'Python'
    >>> others
    ['Java', 'C', 'TypeScript', 'Rust']
    ```

=== "Primero, segundo y otros"

    ```pycon hl_lines="3"
    >>> ranking = ('Python', 'Java', 'C', 'TypeScript', 'Rust')

    >>> first, second, *others = ranking

    >>> first
    'Python'
    >>> second
    'Java'
    >>> others
    ['C', 'TypeScript', 'Rust']
    ```

=== "Otros, penúltimo y último"

    ```pycon hl_lines="3"
    >>> ranking = ('Python', 'Java', 'C', 'TypeScript', 'Rust')

    >>> *others, next_to_last, last = ranking

    >>> others
    ['Python', 'Java', 'C']
    >>> next_to_last
    'TypeScript'
    >>> last
    'Rust'
    ```

=== "Otros y último"

    ```pycon hl_lines="3"
    >>> ranking = ('Python', 'Java', 'C', 'TypeScript', 'Rust')

    >>> *others, last = ranking

    >>> others
    ['Python', 'Java', 'C', 'TypeScript']
    >>> last
    'Rust'
    ```

??? note "Limitación al desempaquetado extendido"

    La condición necesaria para realizar desempaquetado extendido es que el número de elementos de destino debe ser **menor o igual** al número de elementos de origen.

### Desempaquetado genérico { #generic-unpacking }

El desempaquetado de tuplas es **extensible a cualquier otro tipo de datos que sea iterable**.

Veamos algunos <span class="example">ejemplos:material-flash:</span>:

=== "Sobre cadenas de texto :material-format-quote-open:"

    ```pycon
    >>> oxygen = 'O2'
    >>> first, last = oxygen
    >>> first, last
    ('O', '2')
    
    >>> text = 'Hello, World!'
    >>> head, *body, tail = text
    >>> head, body, tail
    ('H', ['e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd'], '!')
    ```

=== "Sobre listas :material-code-brackets:"

    ```pycon
    >>> writer1, writer2, writer3 = ['Virginia Woolf', 'Jane Austen', 'Mary Shelley']
    >>> writer1, writer2, writer3
    ('Virginia Woolf', 'Jane Austen', 'Mary Shelley')
    
    >>> text = 'Hello, World!'
    >>> word1, word2 = text.split()
    >>> word1, word2
    ('Hello,', 'World!')
    ```

## ¿Tuplas por comprensión? { #tuple-comprehension }

Los tipos de datos mutables (_listas, diccionarios y conjuntos_) sí permiten comprensiones pero **no así los tipos de datos inmutables** como cadenas de texto y tuplas.

Si intentamos crear una **tupla por comprensión** utilizando paréntesis alrededor de la expresión, vemos que no aparece ningún error al ejecutarlo:

```pycon
>>> myrange = (number for number in range(1, 6))
```

Sin embargo lo que obtendremos **no es una tupla** sino un [generador](../modularity/functions.md#generators):

```pycon
>>> myrange
<generator object <genexpr> at 0x10b3732e0>
```

## Tuplas vs Listas { #tuples-vs-lists }

Aunque las tuplas y las listas puedan parecer estructuras de datos muy similares, sabemos que las tuplas carecen de ciertas operaciones, especialmente las que tienen que ver con la modificación de sus valores, ya que no son inmutables.

Si las listas son más flexibles y potentes, **¿por qué íbamos a necesitar tuplas?** Veamos 4 potenciales ^^ventajas^^ del uso de tuplas frente a las listas:

1. Las tuplas ocupan **menos espacio** en memoria.
2. En las tuplas existe **protección** frente a cambios indeseados.
3. Las tuplas se pueden usar como **claves de diccionarios** (son [«hashables»](dicts.md#hashables)).
4. Las [`namedtuples`](https://docs.python.org/es/3/library/collections.html#collections.namedtuple) son una alternativa sencilla a los objetos.
