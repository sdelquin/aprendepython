---
icon: material/text-box
---

# Cadenas de texto { #strings }

![Dices](images/strings/newspaper.jpg)
(1)
{ .annotate }

1. :fontawesome-regular-copyright: [Roman Kraft](https://unsplash.com/@romankraft) (Unsplash)

Las cadenas de texto son **secuencias de caracteres**. También se les conoce como «strings» y nos permiten almacenar información textual de manera muy cómoda.

Es importante señalar que desde <span class="pyversion"><a href="https://docs.python.org/3.0/">Python <span class="version">:octicons-tag-24: 3.0</span></a></span> las cadenas de texto se almacenan en el estándar [Unicode](https://es.wikipedia.org/wiki/Unicode), lo que supone una gran ventaja con respecto a versiones antiguas del lenguaje (que usaban _bytes_ para esto). Además permite representar una cantidad ingente de símbolos incluyendo los famosos emojis 😎.

## Creando «strings» { #create }

Para escribir una cadena de texto en Python basta con rodear los caracteres con comillas simples:

```pycon
>>> 'Mi primera cadena en Python'
'Mi primera cadena en Python'
```

Para incluir _comillas dobles_ dentro de la cadena de texto no hay mayor inconveniente:

```pycon
>>> 'Los llamados "strings" son secuencias de caracteres'
'Los llamados "strings" son secuencias de caracteres'
```

Para incluir _comillas simples_ dentro de la cadena de texto cambiamos las comillas exteriores a comillas dobles(1):
{ .annotate }

1. Otra opción es [escapar](#escape-sequences) las comillas simples: `#!python 'Los llamados \'strings\' son secuencias de caracteres'`.

```pycon
>>> "Los llamados 'strings' son secuencias de caracteres"
"Los llamados 'strings' son secuencias de caracteres"
```

!!! tip "Cuestión de estilo"

    Efectivamente, como se puede ver, las cadenas de texto en Python se pueden escribir con comillas simples o con comillas dobles. Es indiferente. **En mi caso personal prefiero usar comillas simples :fontawesome-solid-single-quote-right:**.

    Hagas lo que hagas... ¡haz siempre lo mismo!

### Comillas triples { #triple-quotes }

Una forma alternativa de crear cadenas de texto es utilizar _comillas triples_. Su aplicación está pensada principalmente para **cadenas multilínea**:

```pycon
>>> poem = """To be, or not to be, that is the question:
... Whether 'tis nobler in the mind to suffer
... The slings and arrows of outrageous fortune,
... Or to take arms against a sea of troubles"""
```

En este caso sí que se debería utilizar **comillas dobles** (triples) siguiendo las [indicaciones de la guía de estilo de Python](https://peps.python.org/pep-0008/#string-quotes):

!!! quote "PEP 257"

    In Python, single-quoted strings and double-quoted strings are the same. This PEP does not make a recommendation for this. Pick a rule and stick to it. When a string contains single or double quote characters, however, use the other one to avoid backslashes in the string. It improves readability.
    
    ^^For triple-quoted strings, always use double quote^^ characters to be consistent with the docstring convention in PEP 257.

### Cadena vacía { #empty-string }

La cadena vacía es aquella que no contiene ningún carácter. Aunque a priori no lo pueda parecer, es un recurso importante en cualquier programa (y lenguaje de programación). Su representación en Python es la siguiente:

```pycon
>>> ''
''
```

## Conversión { #cast }

Podemos crear «strings» a partir de otros tipos de datos mediante la función `#!python str()`:

```pycon
>>> str(True)
'True'
>>> str(10)
'10'
>>> str(21.7)
'21.7'
```

Para el caso contrario de convertir un «string» a un valor numérico, tenemos a disposición las [funciones ya vistas](numbers.md#explicit-typecast):

```pycon
>>> int('10')
10
>>> float('21.7')
21.7
```

En aquellos casos donde la cadena de texto no se pueda convertir, Python nos indicará que hay un error:

```pycon
>>> float('3.1a')
Traceback (most recent call last):
  Cell In[1], line 1
    float('3.1a')
ValueError: could not convert string to float: '3.1a'
```

!!! tip "Otras bases"

    Hay que tener en cuenta un detalle. La función `#!python int()` también admite la **base** en la que se encuentra el número. Eso significa que podemos pasar un número, por ejemplo, en **hexadecimal** (como «string») y lo podríamos convertir a su valor entero:

    ```pycon
    >>> int('FF', 16)
    255
    ```

## Secuencias de escape { #escape-sequences }

Python permite escapar el significado de algunos caracteres para conseguir otros resultados. Si escribimos una barra invertida `\` antes del carácter en cuestión, le otorgamos un significado especial.

Quizás la secuencia de escape más conocida es `\n` que representa un ^^salto de línea^^, pero existen muchas otras:

=== "Salto de línea `#!python '\n'`"

    ```pycon
    >>> msg = 'Primera línea\nSegunda línea\nTercera línea'
    >>> print(msg)
    Primera línea
    Segunda línea
    Tercera línea
    ```    

=== "Tabulador `#!python '\t'`"

    ```pycon
    >>> msg = 'Valor = \t40'
    >>> print(msg)
    Valor =     40
    ```

=== "Comilla simple `#!python '\''`"

    ```pycon
    >>> msg = 'Necesitamos \'escapar\' la comilla simple'
    >>> print(msg)
    Necesitamos 'escapar' la comilla simple
    ```
    
=== "Barra invertida `#!python '\\'`"

    ```pycon
    >>> msg = 'Capítulo \\ Sección \\ Encabezado'
    >>> print(msg)
    Capítulo \ Sección \ Encabezado
    ```

:material-check-all:{ .blue } Los <span class="example">ejemplos:material-flash:</span> anteriores se han mostrado con el [intérprete de Python](data.md#get-value). Aún así hemos utilizado la función `#!python print()` porque nos permite ver realmente el resultado de utilizar los caracteres escapados.

### Cadenas en crudo { #raw }

Hay situaciones en las que nos interesa que los caracteres especiales pierdan ese significado y poder usarlos de otra manera. Existe un modificador de cadena que proporciona Python para tratar el texto en bruto. Es el llamado «raw data» y se aplica anteponiendo una `r` a la cadena de texto.

Veamos algunos ejemplos:

=== "«raw» con salto de línea"

    ```pycon
    >>> text = 'abc\ndef'
    >>> print(text)
    abc
    def

    >>> text = r'abc\ndef'
    >>> print(text)
    abc\ndef
    ```

=== "«raw» con tabulador"

    ```pycon
    >>> text = 'a\tb\tc'
    >>> print(text)
    a    b    c

    >>> text = r'a\tb\tc'
    >>> print(text)
    a\tb\tc
    ```

!!! note "Expresiones regulares"

    El modificador `#!python r''` es muy utilizado para escribir [expresiones regulares](../../stdlib/text-processing/re.md).

## Más sobre `print()` { #more-about-print }

Hemos estado utilizando la función `#!python print()` de manera sencilla, pero admite algunos [parámetros](https://docs.python.org/es/3/library/functions.html#print) interesantes.

Veamos algunos <span class="example">ejemplos:material-flash:</span>:

```pycon
>>> msg1 = '¿Sabes por qué estoy acá?'
>>> msg2 = 'Porque me apasiona'

>>> print(msg1, msg2)#(1)!
¿Sabes por qué estoy acá? Porque me apasiona

>>> print(msg1, msg2, sep='|')#(2)!
¿Sabes por qué estoy acá?|Porque me apasiona

>>> print(msg2, end='!!')#(3)!
Porque me apasiona!!
```
{ .annotate }

1. Podemos imprimir todas las variables que queramos separándolas por comas.
2. El **separador por defecto** entre las variables es un **espacio**. Podemos cambiar el carácter que se utiliza como separador entre cadenas a través de `sep`.
3. El carácter de **final de texto** es un **salto de línea**. Podemos cambiar el carácter que se utiliza como final de texto a través de `end`.

## Leer datos desde teclado { #read-from-keyboard }

Los programas se desarrollan (habitualmente) para tener una cierta interacción con el usuario. Una de las formas de interacción es solicitar la entrada de datos por teclado. Como muchos otros lenguajes de programación, Python también nos ofrece la posibilidad de leer la información introducida por teclado. Para ello se utiliza la función `#!python input()`.

Veamos algunos ejemplos:

```pycon hl_lines="1 8"
>>> name = input('Introduzca su nombre: ')
Introduzca su nombre: Sergio
>>> name
'Sergio'
>>> type(name)
str

>>> age = input('Introduzca su edad: ')#(1)!
Introduzca su edad: 41
>>> age
'41'
>>> type(age)
str
```
{ .annotate }

1. La función `#!python input()` siempre nos **devuelve un objeto de tipo cadena de texto** o `str`. Tenerlo muy en cuenta a la hora de trabajar con números, ya que debemos realizar una [conversión explícita](numbers.md#explicit-typecast).

!!! warning "Advertencia"

    Aunque está permitido, **NUNCA** llames `input` a una variable porque destruirías la función que nos permite leer datos desde teclado. Y tampoco uses nombres derivados como `_input` o `input_` ya que **no son nombres representativos** que [identifiquen el propósito de la variable](data.md#naming-standards).

!!! exercise "Ejercicio"

    [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `calc-basic`    

## Operaciones con «strings» { #operations }

### Combinar cadenas { #merge }

Podemos combinar dos o más cadenas de texto utilizando el operador `+`:

```pycon
>>> proverb1 = 'Cuando el río suena'
>>> proverb2 = 'agua lleva'

>>> proverb1 + proverb2
'Cuando el río suenaagua lleva'

>>> proverb1 + ', ' + proverb2#(1)!
'Cuando el río suena, agua lleva'
```
{ .annotate }

1. Podemos «sumar» todas la cadenas de texto que sean necesarias.

### Repetir cadenas { #repeat }

Podemos repetir dos o más cadenas de texto utilizando el operador `*`:

```pycon
>>> reaction = 'Wow'

>>> reaction * 4
'WowWowWowWow'
```

### Obtener un caracter { #get-char }

Los «strings» están **indexados** y cada carácter tiene su propia posición (numérica).

Veamos el <span class="example">ejemplo:material-flash:</span> de la cadena de texto `#!python 'Hola, Mundo'`:

![Dark image](images/strings/string-indexing-dark.svg#only-dark)
![Light image](images/strings/string-indexing-light.svg#only-light)

Para acceder a cada caracter podemos hacer uso de su **índice** que, en Python, puede ser **tanto positivo como negativo**:

```pycon
>>> sentence[0]
'H'
>>> sentence[-1]
'o'
>>> sentence[4]
','
>>> sentence[-5]
'M'
```

En caso de que intentemos acceder a un índice que no existe, obtendremos un error por _fuera de rango_:

```pycon hl_lines="5"
>>> sentence[50]
Traceback (most recent call last):
  Cell In[1], line 1
    sentence[50]
IndexError: string index out of range
```

Las cadenas de texto son tipos de datos [inmutables](data.md#mutability). Es por ello que no podemos modificar un carácter directamente.

Veamos un <span class="example">ejemplo:material-flash:</span>:

```pycon hl_lines="7"
>>> song = 'Hey Jude'

>>> song[4] = 'D'
Traceback (most recent call last):
  Cell In[2], line 1
    song[4] = 'D'
TypeError: 'str' object does not support item assignment
```

Existen formas de modificar una cadena de texto que veremos más adelante, aunque realmente no estemos transformando el original sino creando un nuevo objeto con las modificaciones.

!!! failure "Sobre las constantes"

    No hay que confundir las [constantes](data.md#constants) con los tipos de datos inmutables. Es por ello que las variables que almacenan cadenas de texto, a pesar de ser inmutables, no se escriben en mayúsculas.

### Trocear una cadena { #slicing }

Es posible extraer «trozos» («rebanadas»)[^1] de una cadena de texto. Tenemos varias aproximaciones para ello:

=== "Comienzo y fin"

    Se indica con la sintaxis `#!python [start:end]`

    ```pycon
    >>> proverb = 'Agua pasada no mueve molino'
    >>> proverb[5:11]
    'pasada'
    ```

    :material-check-all:{ .blue } Se llega hasta `end - 1`

=== "Comienzo y fin (otro paso)"

    El **paso** indica cuánto nos movemos en el troceado (_tamaño del salto_). El paso por defecto es 1, pero este valor se puede modificar. Se indica con la sintaxis `#!python [start:end:step]`

    ```pycon
    >>> proverb = 'Agua pasada no mueve molino'
    >>> proverb[5:11:2]#(1)!
    'psd'
    ```
    { .annotate }
    
    1. paso = `2`

    :material-check-all:{ .blue } Se llega hasta `end - 1`

=== "Comienzo sin fin"

    Si no especificamos hasta dónde llegar, el troceado se extenderá hasta el final de la cadena de texto. Se indica con la sintaxis `#!python [start:]`

    ```pycon
    >>> proverb = 'Agua pasada no mueve molino'
    >>> proverb[12:]
    'no mueve molino'
    ```

=== "Fin sin comienzo"

    Si no especificamos desde dónde empezar, el troceado empezará por el principio de la cadena de texto. Se indica con la sintaxis `#!python [:end]`

    ```pycon
    >>> proverb = 'Agua pasada no mueve molino'
    >>> proverb[:11]
    'Agua pasada'
    ```

    :material-check-all:{ .blue } Se llega hasta `end - 1`

=== "Ni comienzo ni fin"

    Si no especificamos comienzo ni fin, el troceado empezará por el principio de la cadena de texto y se extendrá hasta el final de la misma. Se indica con la sintaxis `#!python [:]`

    ```pycon
    >>> proverb = 'Agua pasada no mueve molino'
    >>> proverb[:]
    'Agua pasada no mueve molino'    
    ```

### Longitud de la cadena { #length }

Para obtener la longitud de una cadena podemos hacer uso de `#!python len()`, una función común a prácticamente todos los tipos y estructuras de datos en Python.

Veamos algunos <span class="example">ejemplos:material-flash:</span>:

```pycon
>>> proverb = 'Lo cortés no quita lo valiente'
>>> len(proverb)
30

>>> empty = ''
>>> len(empty)#(1)!
0
```
{ .annotate }

1. La cadena vacía siempre tiene longitud 0.

### Pertenencia de un elemento { #in }

Si queremos comprobar que una determinada subcadena se encuentra en una cadena de texto utilizamos el operador `#!python in` para ello. Se trata de una expresión que tiene como resultado un valor «booleano» verdadero o falso.

Veamos algunos <span class="example">ejemplos:material-flash:</span>:

```pycon
>>> proverb = 'Más vale malo conocido que bueno por conocer'

>>> 'malo' in proverb
True

>>> 'mal' in proverb#(1)!
True

>>> 'bueno' in proverb
True

>>> 'regular' in proverb
False

>>> '' in proverb#(2)!
True
```
{ .annotate }

1. El operador `#!python in` no busca «palabras», únicamente secuencias de caracteres.
2. La cadena vacía está en todas las cadenas.

Habría que prestar atención al caso en el que intentamos descubrir si una subcadena **no está** en la cadena de texto:

```pycon
>>> dna_sequence = 'ATGAAATTGAAATGGGA'

>>> not('C' in dna_sequence)#(1)!
True

>>> 'C' not in dna_sequence#(2)!
True
```
{ .annotate }

1. Esta podría ser una primera aproximación.
2. Esta es la forma realmente [pitónica](../modularity/functions.md#pythonic).

### Limpiar cadenas { #strip }

Cuando leemos datos del usuario o de cualquier fuente externa de información, es bastante probable que se incluyan en esas cadenas de texto caracteres de relleno[^2] al comienzo y al final. Python nos ofrece la posibilidad de eliminar estos caracteres u otros que no nos interesen.

La función `#!python strip()` se utiliza para eliminar caracteres del principio y del final de un «string». También existen variantes de esta función para aplicarla únicamente al comienzo o únicamente al final de la cadena de texto.

Supongamos que debemos procesar un fichero con números de serie de un determinado artículo. Cada línea contiene el valor que nos interesa pero se han «colado» ciertos caracteres de relleno que debemos limpiar:

```pycon
>>> serial_number = '\n\t   \n 48374983274832    \n\n\t   \t   \n'

>>> serial_number.strip()
'48374983274832'
```

!!! info "Valores por defecto"

    Si no se especifican los caracteres a eliminar, `strip()` usará por defecto cualquier combinación de _espacios en blanco_, _saltos de línea_ `\n` y _tabuladores_ `\t`.

Hay dos variantes de esta función para especificar «por dónde» hacer la limpieza:

=== ":material-hand-pointing-right: «Left» `strip`" 

    ```pycon
    >>> serial_number.lstrip()
    '48374983274832    \n\n\t   \t   \n'
    ```    

=== "«Right» `strip` :material-hand-pointing-left:"

    ```pycon
    >>> serial_number.rstrip()
    '\n\t   \n 48374983274832'
    ```    

También existe la posibilidad de **especificar los caracteres** que queremos borrar:

```pycon
>>> serial_number.strip('\n')
'\t   \n 48374983274832    \n\n\t   \t   '
```

!!! tip "Cadena modificada"

    La función `strip()` no modifica la cadena que estamos usando (_algo obvio porque los «strings» son [inmutables](data.md#mutability)_) sino que ^^devuelve una nueva cadena^^ de texto con las modificaciones pertinentes.

### Realizar búsquedas { #search }

Aunque hemos visto que la forma [pitónica](../modularity/functions.md#pythonic) de saber [si una subcadena se encuentra dentro de otra](#in) es a través del operador `#!python in`, Python nos ofrece distintas alternativas para realizar búsquedas dentro de una cadena de texto.

Vamos a partir de una variable que contiene un trozo de la canción [Mediterráneo](https://open.spotify.com/track/7Bewui7KtaMzROeteRitRz?si=NGwOUmwfRSuapY3JL7s1uQ) de Joan Manuel Serrat para ejemplificar las distintas opciones que tenemos:

```pycon
>>> lyrics = """Quizás porque mi niñez
... Sigue jugando en tu playa
... Y escondido tras las cañas
... Duerme mi primer amor
... Llevo tu luz y tu olor
... Por dondequiera que vaya"""
```

Comprobar si una cadena de texto **empieza o termina por alguna subcadena**:

```pycon
>>> lyrics.startswith('Quizás')
True

>>> lyrics.endswith('Final')
False
```

Encontrar la **primera ocurrencia** de alguna subcadena:

```pycon
>>> lyrics.find('amor')
93

>>> lyrics.index('amor')
93
```

Tanto `find()` como `index()` devuelven el **índice** de la primera ocurrencia de la subcadena que estemos buscando, pero se diferencian en su comportamiento cuando _la subcadena buscada no existe_:

```pycon
>>> lyrics.find('universo')
-1

>>> lyrics.index('universo')
Traceback (most recent call last):
  Cell In[2], line 1
    lyrics.index('universo')
ValueError: substring not found
```

Para contabilizar el **número de veces que aparece** una subcadena utilizamos la función `count()`:

```pycon
>>> lyrics.count('mi')
2

>>> lyrics.count('tu')
3

>>> lyrics.count('él')
0
```

!!! exercise "Ejercicio"

    [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `lost-word`

### Reemplazar texto { #replace }

Podemos usar la función `replace()` indicando la _subcadena a reemplazar_, la _subcadena de reemplazo_ y _cuántas instancias_ se deben reemplazar. Si no se especifica este último argumento, la sustitución se hará en todas las instancias encontradas.

Veamos un <span class="example">ejemplo:material-flash:</span>:

```pycon
>>> proverb = 'Quien mal anda mal acaba'

>>> proverb.replace('mal', 'bien')
'Quien bien anda bien acaba'

>>> proverb.replace('mal', 'bien', 1)#(1)!
'Quien bien anda mal acaba'
```
{ .annotate }

1. Es posible indicar cuántos reemplazos llevar a cabo.

### Mayúsculas y minúsculas { #text-cases }

Python nos permite realizar variaciones en los caracteres de una cadena de texto para pasarlos a mayúsculas y/o minúsculas.

Veamos las distintas opciones disponibles a través del siguiente <span class="example">ejemplo:material-flash:</span>:

```pycon
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
```
    
### Identificando caracteres { #identify-chars }

Hay veces que recibimos información textual de distintas fuentes de las que necesitamos identificar qué tipo de caracteres contienen. Para ello Python nos ofrece un grupo de funciones:

=== "Alfanuméricos :material-numeric-1-circle-outline: :material-format-letter-case:"

    Detectar si todos los caracteres son letras o números:

    ```pycon
    >>> 'R2D2'.isalnum()
    True
    >>> 'C3-PO'.isalnum()
    False
    ```

=== "Alfabéticos :material-format-letter-case:"

    Detectar si todos los caracteres son alfabéticos:    

    ```pycon
    >>> 'abc'.isalpha()
    True
    >>> 'a-b-c'.isalpha()
    False
    ```

=== "Numéricos :material-numeric-1-circle-outline:"

    Detectar si todos los caracteres son números:

    ```pycon
    >>> '314'.isnumeric()
    True
    >>> '3.14'.isnumeric()
    False
    ```

=== "Mayúsculas/Minúsculas :material-format-letter-case-upper:"

    Detectar mayúsculas/minúsculas en la cadena de texto:

    ```pycon
    >>> 'BIG'.isupper()
    True
    >>> 'small'.islower()
    True
    >>> 'First Heading'.istitle()
    True
    ```

## Interpolación de cadenas { #interpolation }

En este apartado veremos cómo **interpolar** valores dentro de cadenas de texto utilizando diferentes formatos. Interpolar (en este contexto) significa **sustituir una variable por su valor** dentro de una cadena de texto.

Veamos los estilos que proporciona Python para este cometido:

| Nombre | Símbolo | Soportado |
| --- | --- | --- |
| Estilo «antiguo» | `#!python %` | :material-code-greater-than-or-equal: <span class="pyversion"><a href="https://docs.python.org/2.0/">Python <span class="version">:octicons-tag-24: 2.0</span></a></span> 
| Estilo «nuevo» | `#!python .format()` | :material-code-greater-than-or-equal: <span class="pyversion"><a href="https://docs.python.org/2.6/">Python <span class="version">:octicons-tag-24: 2.6</span></a></span>
| «f-strings» | `#!python f''` | :material-code-greater-than-or-equal: <span class="pyversion"><a href="https://docs.python.org/3.6/">Python <span class="version">:octicons-tag-24: 3.6</span></a></span>

Aunque aún podemos encontrar código Python con el [estilo antiguo y el estilo nuevo en el formateo de cadenas](https://pyformat.info/), vamos a centrarnos en el análisis de los **«f-strings»** que se están muy extendidos en el desarrollo actual.

### «f-strings» { #fstrings }

Los f-strings [aparecieron en Python 3.6](https://docs.python.org/es/3/whatsnew/3.6.html#new-features) y se suelen usar en código de nueva creación. Es la forma más potente –y en muchas ocasiones más eficiente– de formar cadenas de texto incluyendo valores de otras variables.

La **interpolación** en cadenas de texto es un concepto que existe en la gran mayoría de lenguajes de programación y hace referencia al hecho de sustituir los nombres de variables por sus valores cuando se construye un «string».

Para indicar en Python que una cadena es un «f-string» basta con precederla de una `f` e incluir las variables o expresiones a interpolar entre llaves `{...}`.

Supongamos que disponemos de los datos de una persona y queremos formar una frase de bienvenida con ellos:

```pycon
>>> name = 'Leia Organa'
>>> age = 22
>>> role = 'líder de la Alianza Rebelde'

>>> f'Me llamo {name}, tengo {age} años y soy {role}'#(1)!
'Me llamo Leia Organa, tengo 22 años y soy líder de la Alianza Rebelde'
```
{ .annotate }

1. Si olvidamos poner la `f` delante de la cadena de texto, no obtendremos ningún eror, únicamente no habrá sustitución (interpolación) de variables:

    ```python
    >>> 'Me llamo {name}, tengo {age} años y soy {role}'
    'Me llamo {name}, tengo {age} años y soy {role}'
    ```

Podría surgir la duda de **cómo incluir llaves** dentro de un «f-string», teniendo en cuenta que las llaves son símbolos especiales para la interpolación de variables. La respuesta es duplicar las llaves:

```pycon
>>> x = 10

>>> f'The variable is {{ x = {x} }}'
'The variable is { x = 10 }'
```

#### Formateando cadenas { #formatting }

Los «f-strings» proporcionan una gran variedad de **opciones de formateado**: ancho del texto, número de decimales, tamaño de la cifra, alineación, etc. Muchas de estas facilidades se pueden consultar en el artículo [Best of Python3.6 f-strings](https://medium.com/@NirantK/best-of-python3-6-f-strings-41f9154983e)[^3].

=== "Formateando enteros"

    El **modificador** para formatear enteros es `d` (_entero decimal_):

    ```pycon
    >>> mount_height = 3718
    
    >>> f'{mount_height:10d}'
    '      3718'
    
    >>> f'{mount_height:010d}'
    '0000003718'
    ```

=== "Formateando flotantes"

    El **modificador** para formatear flotantes es `f` (_flotante_):

    ```pycon
    >>> PI = 3.14159265
    
    >>> f'{PI:f}'#(1)!
    '3.141593'
    
    >>> f'{PI:.3f}'
    '3.142'
    
    >>> f'{PI:12f}'
    '    3.141593'
    
    >>> f'{PI:7.2f}'
    '   3.14'
    
    >>> f'{PI:07.2f}'
    '0003.14'
    
    >>> f'{PI:.010f}'
    '3.1415926500'
    
    >>> f'{PI:e}'
    '3.141593e+00'
    ```
    { .annotate }
    
    1. Por defecto se muestran **6 cifras decimales**.

=== "Formateando cadenas"

    El **modificador** para formatear cadenas de texto es `s` (_string_):

    ```pycon
    >>> text1 = 'how'
    >>> text2 = 'are'
    >>> text3 = 'you'
    
    >>> f'{text1:<7s}|{text2:^11s}|{text3:>7s}'
    'how    |    are    |    you'
    
    >>> f'{text1:-<7s}|{text2:·^11s}|{text3:->7s}'
    'how----|····are····|----you'
    ```
    
=== "Formateando en otras bases"

    El **modificador** para binario es `b`, para octal es `o` y para hexadecimal es `x`:

    ```pycon
    >>> value = 65_321
    
    >>> f'{value:b}'
    '1111111100101001'
    
    >>> f'{value:o}'
    '177451'
    
    >>> f'{value:x}'
    'ff29'
    ```
    
    Por supuesto en el caso de otras bases también es posible aplicar los mismos _modificadores de ancho y de relleno_ vistos para números enteros decimales. Por ejemplo:

    ```pycon
    >>> f'{value:07x}'
    '000ff29'
    ```

    Como ^^curiosidad^^, si utilizamos el modificador `X` **en mayúsculas** es como si aplicáramos (automáticamente) un [`upper()`](#text-cases) al resultado del valor _hexadecimal_:

    ```python
    >>> f'{value:07X}'
    '000FF29'
    ```

    !!! note "Cambio de base"
    
        Nótese la diferencia de obtener el cambio de base con este método frente a las [funciones de cambio de base](numbers.md#bases) ya vistas previamente que añaden el prefijo de cada base `#!python 0b`, `#!python 0o` y `#!python 0x`.

#### Modo «debug» { #fstring-debug }

A partir de [Python 3.8](https://docs.python.org/3/whatsnew/3.8.html#f-strings-support-for-self-documenting-expressions-and-debugging), los «f-strings» permiten imprimir el nombre de la variable y su valor, como un atajo para depurar nuestro código. Para ello sólo tendremos que incluir el símbolo igual `=` después del nombre de la variable.

Veamos algunos <span class="example">ejemplos:material-flash:</span>:

```pycon
>>> serie = 'The Simpsons'
>>> imdb_rating = 8.7
>>> num_seasons = 30

>>> f'{serie=}'
"serie='The Simpsons'"

>>> f'{imdb_rating=}'
'imdb_rating=8.7'

>>> f'{serie[4:]=}'#(1)!
"serie[4:]='Simpsons'"

>>> f'{imdb_rating / num_seasons=}'
'imdb_rating / num_seasons=0.29'
```
{ .annotate }

1. También podemos añadir... ¡expresiones!

#### Modo «representación» { #fstring-repr }

Si imprimimos el valor de una variable utilizando un «f-string», obviamente veremos ese valor tal y como esperaríamos:

```pycon
>>> name = 'Steven Spielberg'

>>> print(f'{name}')  # NO HAGAS ESTO! Usa: print(name)
Steven Spielberg
```

Pero si quisiéramos ver la representación del objeto, tal y como se almacena internamente, podríamos utilizar el modificador `!r` en el «f-string»:

```pycon
>>> name = 'Steven Spielberg'

>>> print(f'{name!r}')
'Steven Spielberg'
```

!!! exercise "Ejercicio"

    [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `fstring-format`

## Caracteres Unicode { #unicode }

Los programas de ordenador deben manejar una **amplia variedad de caracteres**. Simplemente por el hecho de la internacionalización hay que mostrar mensajes en distintos idiomas (inglés, francés, japonés, español, etc.). También es posible incluir «emojis» u otros símbolos.

Python utiliza el estándar **Unicode** para representar caracteres. Eso significa que tenemos acceso a una [amplia carta de caracteres](https://unicode-table.com/en/blocks/) que nos ofrece este estándar de codificación.

Unicode asigna a cada carácter (al menos) dos atributos:

1. Un **código numérico** único (habitualmente se muestra en [hexadecimal](numbers.md#hex)).
2. Un **nombre** representativo.

Veamos un <span class="example">ejemplo:material-flash:</span> con el típico «emoji» de un cohete :rocket: (definido en [este cuadro Unicode](https://unicode-table.com/en/1F680/)).

Python nos permite convertir de...

=== "Carácter a código :material-alphabetical-variant::material-arrow-right-thin::octicons-number-24:"

    Mediante la función `#!python ord()`:

    ```pycon
    >>> rocket_char = '🚀'
    
    >>> ord(rocket_char)
    128640
    
    >>> hex(ord(rocket_char))#(1)!
    '0x1f680'    
    ```
    { .annotate }
    
    1. Es habitual trabajar los códigos Unicode en formato **hexadecimal**.

=== "Código a carácter :octicons-number-24::material-arrow-right-thin::material-alphabetical-variant:"

    Mediante la función `#!python chr()`:

    ```pycon
    >>> rocket_code = 0x1f680
    
    >>> chr(rocket_code)
    '🚀'    
    ```

=== "Nombre a carácter :material-label-outline::material-arrow-right-thin::material-alphabetical-variant:"

    Mediante el modificar `#!python '\N'`:

    ```pycon
    >>> '\N{ROCKET}'
    '🚀'
    ```

!!! exercise "Ejercicio"

    [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `find-unicode`

### ASCII { #ascii }

En los albores de la computación los caracteres se representaban utilizando el [código ASCII](https://elcodigoascii.com.ar/). En un primer momento solo incluía letras mayúsculas y números, pero en 1967 se agregaron las letras minúsculas y algunos caracteres de control, formando así lo que se conoce como [US-ASCII](https://www.microfocus.com/documentation/enterprise-developer/ed60/ETS-help/HHSNRHOPTN0P.html), es decir los caracteres del 0 al 127.

Podemos obtener algunos de los _caracteres imprimibles_ del código ASCII mediante Python:

```pycon
>>> chr(48)
'0'
>>> chr(57)
'9'
>>> chr(65)
'A'
>>> chr(90)
'Z'
```

### Comparar cadenas { #compare }

Cuando comparamos dos cadenas de texto lo hacemos en términos **lexicográficos**. Es decir, se van comparando los caracteres de ambas cadenas uno a uno y se va chequeando cuál está «antes».

Podemos afirmar (al menos en Python) que la cadena de texto `#!python 'arca'` es menor que la cadena de texto `#!python 'arpa'`:

```pycon
>>> 'arca' < 'arpa'#(1)!
True
```
{ .annotate }

1. Python analiza cada carácter:

    `#!python ord('a') #97` :material-equal-box: `#!python ord('a') #97`  
    `#!python ord('r') #114` :material-equal-box: `#!python ord('r') #114`  
    `#!python ord('c') #99` :material-code-less-than: `#!python ord('p') #112`

    :material-check-all:{ .blue } El último carácter no se analiza ya que en este punto sabemos positivamente que la primera cadena de texto es menor que la segunda.

Otros ejemplos:

```pycon
>>> 'a' < 'antes'
True
>>> 'antes' < 'después'
True
>>> 'después' < 'ahora'
False
>>> 'ahora' < 'a'
False
```

Ten en cuenta que en ~~Python~~ Unicode la letras mayúsculas van antes que las minúsculas:

```pycon
>>> 'A' < 'a'#(1)!
True
```
{ .annotate }

1. Cuestión de códigos...
```pycon
>>> ord('A')
65
>>> ord('a')
97
```

## Ejercicios { #exercises }

1. [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `format-hexcolor`
2. [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `swap-name`
3. [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `samba-split`
4. [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `nif-digit`
5. [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `n-repeat`
6. [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `str-metric`
7. [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `h2md`
8. [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `count-sheeps`
9. [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `strip1`
10. [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `find-integral`
11. [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `multiply-jack`
12. [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `first-last-digit`



[^1]: El término inglés es «slice» o «slicing».
[^2]: Se suele utilizar el término inglés «padding» para referirse a estos caracteres.
[^3]: Escrito por Nirant Kasliwal en Medium.
