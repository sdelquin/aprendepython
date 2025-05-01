---
icon: material/regex
---

# re { #re }

![Fork](images/re/floor.jpg)
(1)
{ .annotate }

1. :fontawesome-regular-copyright: [Alice Butenko](https://unsplash.com/@alivka) :material-at: [Unsplash](https://unsplash.com) 

!!! quote "Paradoja"

    Si tienes un problema y lo intentas resolver con expresiones regulares, entonces tienes dos problemas.

El módulo [`re`](https://docs.python.org/es/3/library/re.html) permite trabajar con [expresiones regulares](https://es.wikipedia.org/wiki/Expresi%C3%B3n_regular).

## Expresión regular { #regex }

Una **expresión regular** (también conocida como «regex» o «regexp» por su contracción anglosajona «reg-ular exp-ression») es una cadena de texto que conforma un **patrón de búsqueda**. Se utiliza principalmente para la _búsqueda de patrones_ en cadenas de caracteres u _operaciones de sustitución_.

Se trata de una **herramienta ampliamente utilizada en las ciencias de la computación** y necesaria para multitud de aplicaciones que traten con información textual.

Pero... ¿qué pinta tiene una expresión regular? Veamos un primer <span class="example">ejemplo:material-flash:</span> de expresión regular:

```pycon
>>> regex = '^\d{8}[A-Z]$'
```

La expresión regular anterior nos permite **comprobar que una cadena de texto dada es un DNI válido**. Si analizamos parte por parte tendríamos lo siguiente:

- `^` :material-arrow-right-bold: comienzo de línea.
- `\d{8}` :material-arrow-right-bold: dígito que se repite 8 veces.
- `[A-Z]` :material-arrow-right-bold: letra en mayúsculas.
- `$` :material-arrow-right-bold: final de línea.

## Sintaxis { #syntax }

Las expresiones regulares pueden contener tanto **caracteres especiales** como **caracteres ordinarios**. La mayoría de los caracteres ordinarios, como `#!python 'A'`, `#!python 'b'` o `#!python '0'` son las expresiones regulares más sencillas; simplemente se ajustan a sí mismas.

Existen una serie de caracteres que tienen un **significado especial** dentro de una expresión regular:

| Caracter | Descripción | Ejemplo | :material-check:{.green} | :material-cancel:{.red} |
| --- | --- | --- | --- | --- |
| <span class="hl mono bold">.<span> | Coincide con cualquier carácter excepto con una nueva línea. | `#!python 'a.b'` | `acb`, `a b`, `aab`, `abb`, ... | `bxa`, `a\nb`, `ab`, `abc`, ... |
| <span class="hl mono bold">^<span> | Coincide con el comienzo de la línea o cadena | `#!python '^ab'` | `ab`, `abc`, `abab`, `abcd`, ... | `ba`, `aa`, `bb`, `axb`, ... |
| <span class="hl mono bold">$<span> | Coincide con el final de la línea o cadena. | `#!python 'ab$'` | `ab`, `aab`, `bab`, ` ab` ... | `b`, `bb`, `ba`, `aa`, ... |
| <span class="hl mono bold">*<span> | Coincide con 0 o más repeticiones de la expresión regular precedente. | `#!python 'a*b'` | `b`, `ab`, `aab`, `aaab`, ... | `ba`, `a`, `aa`, `acb`, ... |
| <span class="hl mono bold">+<span> | Coincide con 1 o más repeticiones de la expresión regular precedente. | `#!python 'a+b'` | `ab`, `aab`, `aaab`, ... | `b`, `cb`, `ba`, `bb`, ... |
| <span class="hl mono bold">?<span> | Coincide con 0 o 1 repetición de la expresión regular precedente. | `#!python 'a?b'` | `b`, `ab` | `aab`, `ba`, `aaab`, `cb`, ... |
| <span class="hl mono bold">{m}<span> | Coincide con exactamente `m` repeticiones de la expresión regular precedente. | `#!python 'a{3}'` | `aaa` | `a`, `aa`, `aaaa`, ... |
| <span class="hl mono bold">{m,n}<span> | Coincide de `m` a `n` repeticiones de la expresión regular precedente, tratando de coincidir con el mayor número de repeticiones posibles. | `#!python 'a{2,4}'` | `aa`, `aaa`, `aaaa` | `a`, `aaaaa`, ... |
| <span class="hl mono bold">{m,}<span> | Coincide como mínimo con `m` repeticiones de la expresión regular precedente. | `#!python 'a{2,}'` | `aa`, `aaa`, `aaaa`, ... | `''`, `a`, ... |
| <span class="hl mono bold">{,n}<span> | Coincide como máximo con `n` repeticiones de la expresión regular precedente. | `#!python 'a{,2}'` | `''`, `a`, `aa`, | `aaa`, `aaaa`, ... |
| <span class="hl mono bold">[]<span> | Coincide con el conjunto de caracteres indicados dentro de los corchetes. | `#!python '[abc]'` | `a`, `b`, `c` | `aa`, `d`, `ab`, ... |
| <span class="hl mono bold">[^]<span> | Coincide con cualquier caracter fuera de los caracteres indicados dentro de los corchetes. | `#!python '[^abc]'` | `d`, `e`, `f`, ... | `a`, `b`, `c` |
| <span class="hl mono bold">[m-n]<span> | Coincide con el conjunto de caracteres indicados dentro de los corchetes. | `#!python '[a-d]'` | `a`, `b`, `c`, `d` | `aa`, `f`, `ab`, ... |
| <span class="hl mono bold">[^m-n]<span> | Coincide con cualquier caracter fuera de los caracteres indicados dentro de los corchetes. | `#!python '[^a-d]'` | `e`, `f`, `g`, ... | `a`, `b`, `c`, `d` |
| <span class="hl mono bold">\|<span> | Coincide con una expresión regular u otra, separadas por este símbolo. | `#!python 'a+|b+'` | `a`, `aa`, `b`, `bb`, ... | `ab`, `aabb`, `abab`, ... |
| <span class="hl mono bold">()<span> | Coincide con cualquier expresión regular que esté dentro de los paréntesis, e indica el comienzo y el final de un grupo de captura; el contenido de un grupo puede ser recuperado después de que se haya realizado una coincidencia. | `#!python '(ab)'` | `ab` | `a`, `b`, `abc`, ... |
| <span class="hl mono bold">(?P<name\>)<span> | Coincide con cualquier expresión regular que esté dentro de los paréntesis; el contenido del grupo de captura es accesible por `name`. | `#!python '(?P<test>ab)'` | `ab` | `a`, `b`, `abc`, ... |
| <span class="hl mono bold">(?:)<span> | Coincide con cualquier expresión regular que esté dentro de los paréntesis pero no crea un grupo de captura. | `#!python '(?:ab)'` | `ab` | `a`, `b`, `abc`, ... |
| <span class="hl mono bold">\number<span> | Coincide con el contenido del grupo de captura del mismo número. Se usa en conjunción con `#!python ()`. | `#!python r'(.):\1'` | `a:a`, `b:b`, `c:c`, ... | `a:b`, `b:c`, `c:d`, ... |
| <span class="hl mono bold">(?P=name)<span> | Coincide con el contenido del grupo de captura del mismo nombre. Se usa en conjunción con `#!python ()`. | `#!python '(?P<c1>.):(?P=c1)'` | `a:a`, `b:b`, `c:c`, ... | `a:b`, `b:c`, `c:d`, ... |
| <span class="hl mono bold">\b<span> | Coincide con el comienzo o el final de una palabra. | `#!python r'\ba\b'` | `a;b`, `a b`, `a%b`, ... | `ab`, `ba`, `aa`, ... |
| <span class="hl mono bold">\B<span> | Coincide con cualquier caracter que no sea comienzo o final de una palabra. | `#!python r'a\Bb'` | `ab` | `a b`, `a;b`, `a!b`, ... |
| <span class="hl mono bold">\d<span> | Coincide con cualquier dígito decimal. Equivalente a `[0-9]`. | `#!python r'a\db'` | `a0b`, `a3b`, `a9b`, ... | `ab`, `1ab`, `ab2`, ... |
| <span class="hl mono bold">\D<span> | Coincide con cualquier carácter que no sea un dígito decimal. Equivalente a `[^0-9]`. | `#!python r'a\Db'` | `acb`, `aab`, `a;b`, ... | `a0b`, `a3b`, `a9b`, ... |
| <span class="hl mono bold">\s<span> | Coincide con cualquier espacio en blanco. Equivalente a `[ \t\n\r\f\v]`. | `#!python r'a\sb'` | `a b`, `a\tb`, `a\nb`, ... | `acb`, `abb`, `aab`, ... |
| <span class="hl mono bold">\S<span> | Coincide con cualquier carácter que no sea un espacio en blanco. Equivalente a `[^ \t\n\r\f\v]`. | `#!python r'a\Sb'` | `a.b`, `abb`, `aab`, ... | `a b`, `a\tb`, `a\nb`, ... |
| <span class="hl mono bold">\w<span> | Coincide con cualquier carácter alfanumérico. Equivalente a `[a-zA-Z0-9_]`. | `#!python r'a\wb'` | `aab`, `aAb`, `acb`, ... | `a;b`, `a!b`, `a.b`, ... |
| <span class="hl mono bold">\w<span> | Coincide con cualquier carácter que no sea un carácter alfanumérico. Equivalente a `[^a-zA-Z0-9_]`. | `#!python r'a\Wb'` | `a;b`, `a!b`, `a.b`, ... | `aab`, `aAb`, `acb`, ... |
| <span class="hl mono bold">\<span> | Permite «escapar» el caracter que le sigue, es decir, quitarle el significado especial que tiene. | `#!python r'a\.b'` | `a.b` | `acb`, `aab`, `abb`, ... |

!!! tip "Cadenas en crudo"

    Cuando hay barras invertidas en la expresión regular (`\d`, `\s`, `\w`, `\b`, `\1`, ...) es recomendable el uso de [cadenas en crudo](../../core/datatypes/strings.md#raw) o «raw strings» ya que de no hacerlo podríamos obtener errores del estilo: `#!python SyntaxWarning: invalid escape sequence '\d'`.

    En general, siempre que uses expresiones regulares en Python, lo mejor es usar `#!python r''` para evitar confusiones y errores. Por <span class="example">ejemplo:material-flash:</span> `#!python r'\d+'` en vez de `#!python '\d+'`.

!!! exercise "Ejercicio"

    Coge papel y lápiz e intenta escribir una expresión regular para los siguientes escenarios:

    1. [Documento nacional de identidad en España](https://es.wikipedia.org/wiki/Documento_nacional_de_identidad_(Espa%C3%B1a)).
    2. [Número de identidad de extranjero en España](https://es.wikipedia.org/wiki/N%C3%BAmero_de_identidad_de_extranjero).
    3. [Matrículas automovilísticas en España](https://es.wikipedia.org/wiki/Matr%C3%ADculas_automovil%C3%ADsticas_de_Espa%C3%B1a).
    4. [Código de aeropuertos de IATA](https://es.wikipedia.org/wiki/C%C3%B3digo_de_aeropuertos_de_IATA).
    5. [Prefijos telefónicos mundiales](https://es.wikipedia.org/wiki/Anexo:Prefijos_telef%C3%B3nicos_mundiales).
    6. [Tamaños de papel ISO-DIN](https://es.wikipedia.org/wiki/Formato_de_papel#Norma_ISO_216_/_DIN_476).

## Operaciones { #operations }

Una vez encontrada la expresión regular correspondiente, Python nos ofrece distintas operaciones que podemos realizar.

### Buscar { #re-search }

La búsqueda de patrones es una de las principales utilidades de las expresiones regulares.

#### Búsqueda simple { #search }

Supongamos un <span class="example">ejemplo:material-flash:</span> en el que queremos buscar un número de teléfono dentro de un texto. Para ello vamos a utilizar la función [`search()`](https://docs.python.org/es/3/library/re.html#re.search):

```pycon
>>> import re#(1)!

>>> text = 'Estaré disponible en el +34755142009 el lunes por la tarde'#(2)!

>>> regex = r'\+?\d{2}\d{9}'#(3)!

>>> m = re.search(regex, text)

>>> m#(4)!
<re.Match object; span=(24, 36), match='+34755142009'>
```
{ .annotate }

1. Para poder trabajar con expresiones regular debemos importar el paquete `re` de la librería estándar.
2. Texto de entrada.
3. Definición de la expresión regular:
    - `\+?` :material-arrow-right-bold: Puede aparecer el signo `+` como prefijo del teléfono (lo escapamos ya que el punto `.` es un caracter especial en sí mismo).
    - `\d{2}` :material-arrow-right-bold: Dos repeticiones de un dígito (prefijo).
    - `\d{9}` :material-arrow-right-bold: Nueve repeticiones de un dígito (número telefónico en sí mismo).
4. La función `search()` nos devuelve un objeto tipo `Match` donde `span` indica la «ventana» de coincidencia: `text[24:36]` :material-arrow-right-bold: `#!python '+34755142009'`

Podemos acceder a la coincidencia encontrada de varias formas:

```pycon
>>> m[0]#(1)!
'+34755142009'

>>> m.span(0)#(2)!
(24, 36)
```
{ .annotate }

1.  - El acceso por índice nos devuelve las coindicencias encontradas.
    - Equivalente a usar `#!python m.group(0)`.
2.  - El método `span()` nos devuelve una _tupla_ con los índices de comienzo y finalización de la coincidencia.
    - Equivalente a usar `#!python m.start()` y `#!python m.end()`.

Podemos aplicar **grupos de captura** para separar el prefijo y el teléfono siguiendo con el  <span class="example">ejemplo:material-flash:</span> anterior:

=== "Captura posicional"

    ```pycon hl_lines="5 12-13 15-16"
    >>> import re

    >>> text = 'Estaré disponible en el +34755142009 el lunes por la tarde'#(2)!

    >>> regex = r'\+?(\d{2})(\d{9})'
    
    >>> m = re.search(regex, text)
    
    >>> m[0]
    '+34755142009'
    
    >>> m[1]
    '34'
    
    >>> m[2]
    '755142009'
    ```

=== "Captura nominal"

    ```pycon hl_lines="5 12-13 15-16"
    >>> import re

    >>> text = 'Estaré disponible en el +34755142009 el lunes por la tarde'#(2)!

    >>> regex = r'\+?(?P<prefix>\d{2})(?P<number>\d{9})'
    
    >>> m = re.search(regex, text)
    
    >>> m[0]
    '+34755142009'
    
    >>> m['prefix']
    '34'
    
    >>> m['number']
    '755142009'
    ```

!!! tip "Ignorando mayúsculas y minúsculas"

    Si queremos ignorar mayúsculas y minúsculas a la hora de hacer una búsqueda, sólo tendremos que usar un tercer parámetro indicándolo:

    ```python
    import re

    re.search(regex, text, re.IGNORECASE)#(1)!
    ```
    { .annotate }
    
    1. También se puede abreviar como `re.I`

#### Búsqueda múltiple { #findall }

En el ejemplo anterior hemos estado buscando una única coincidencia. Imaginemos ahora que queremos encontrar todos los teléfonos. Para ello vamos a utilizar la función [`findall()`](https://docs.python.org/es/3/library/re.html#re.findall):

```pycon
>>> import re

>>> text = '''
... Datos de contacto:
...   - Marketing: Rubén López (+49677543181)
...   - Ventas: Sara Mondragón (+34681788902)
...   - Desarrollo: Eva Blasco (+51682131262)
... © Saturno Desarrollos de Software
... '''

>>> regex = r'\+?\d{2}\d{9}'

>>> re.findall(regex, text)#(1)!
['+49677543181', '+34681788902', '+51682131262']
```
{ .annotate }

1. La función `findall()` devuelve una **lista** con las coincidencias encontradas.

Es posible utilizar **grupos de captura** con la función `findall()`. Imaginemos que sólo nos interesan los **prefijos telefónicos** del <span class="example">ejemplo:material-flash:</span> anterior:

```pycon
>>> import re

>>> text = '''
... Datos de contacto:
...   - Marketing: Rubén López (+49677543181)
...   - Ventas: Sara Mondragón (+34681788902)
...   - Desarrollo: Eva Blasco (+51682131262)
... © Saturno Desarrollos de Software
... '''

>>> regex = r'\+?(\d{2})\d{9}'#(1)!

>>> re.findall(regex, text)
['49', '34', '51']
```
{ .annotate }

1. Mediante los paréntesis `()` definimos el grupo de captura sobre el prefijo.

### Separar { #split }

Otras de las operaciones ampliamente usadas con expresiones regulares es la separación o división de una cadena de texto mediante un separador.

En su momento vimos el uso de la función [`split()`](../../core/datastructures/lists.md#split) para cadenas de texto, pero era muy limitada para patrones avanzados. Veamos el uso de la función `re.split()` dentro de este módulo de expresiones regulares.

Un <span class="example">ejemplo:material-flash:</span> muy sencillo sería **separar la parte entera de la parte decimal** en un determinado número flotante:

```pycon
>>> regex = r'[.,]'

>>> re.split(regex, '3.14')
['3', '14']

>>> re.split(regex, '3,14')
['3', '14']
```

Python también nos da la posibilidad de «capturar» el separador. Siguiendo el <span class="example">ejemplo:material-flash:</span> anterior:

```pycon
>>> regex = r'([.,])'#(1)!

>>> re.split(regex, '3.14')
['3', '.', '14']

>>> re.split(regex, '3,14')
['3', ',', '14']
```
{ .annotate }

1. Usamos paréntesis para añadir un grupo de captura.

### Reemplazar { #sub }

El paquete de expresiones regulares `re` también nos ofrece la posibilidad de reemplazar ocurrencias dentro de un texto. Para ello disponemos de la función [`sub`](https://docs.python.org/3/library/re.html#re.sub) (regla mnemotécnica viene del inglés «substitute»).

Veamos a continuación un <span class="example">ejemplo:material-flash:</span> de uso en el que recibimos el nombre de una persona en formato `<nombre> <apellidos>` y queremos convertirlo a formato `<apellidos>, <nombre>`.

Veamos dos soluciones a este problema utilizando la función `re.sub()` mediante:

=== "Grupos de captura posicionales"

    ```pycon
    >>> import re

    >>> name = 'Alan Turing'

    >>> regex = r'(\w+) +(\w+)'#(1)!
    >>> repl = r'\2, \1'#(2)!

    >>> re.sub(regex, repl, name)#(3)!
    'Turing, Alan'
    ```
    { .annotate }

    1. Utilizamos grupos de captura **posicionales** para nombre y apellidos.
    2. Hacemos referencia a los _grupos de captura_ en orden «inverso».
    3. La función `re.sub()` recibe la expresión de búsqueda, la expresión de reemplazo y la cadena de texto sobre la que operar.

=== "Grupos de captura nominales"

    ```pycon
    >>> import re

    >>> name = 'Alan Turing'

    >>> regex = r'(?P<name>\w+) +(?P<surname>\w+)'#(1)!
    >>> repl = r'\g<surname>, \g<name>'#(2)!

    >>> re.sub(regex, repl, name)#(3)!
    'Turing, Alan'    
    ```
    { .annotate }
    
    1. Utilizamos grupos de captura **nominales** para nombre y apellidos.
    2. Hacemos referencia a los _grupos de captura_ en orden «inverso».
    3. La función `re.sub()` recibe la expresión de búsqueda, la expresión de reemplazo y la cadena de texto sobre la que operar.

La función `re.sub()` admite un uso más avanzado ya que podemos **pasar una función** en vez de una cadena de texto de reemplazo, lo que nos abre un abanico de posibilidades.

Siguiendo con el <span class="example">ejemplo:material-flash:</span> anterior, supongamos ahora que queremos hacer la misma transformación pero **convirtiendo el apellido a mayúsculas**, y asegurarnos de que **el nombre queda como título**:

```pycon
>>> import re

>>> name = 'Alan Turing'

>>> regex = r'(\w+) +(\w+)'

>>> re.sub(regex, lambda m: f'{m[2].upper()}, {m[1].title()}', name)#(1)!
'TURING, Alan'
```
{ .annotate }

1. La [función «lambda»](../../core/modularity/functions.md#lambda) recibe el objeto «matcheado» y realiza su modificación mediante los grupos de captura.

!!! tip "Contando reemplazos"

    Existe una función `re.subn()` que devuelve una tupla con la nueva cadena de texto reemplazada y el número de sustituciones realizadas.

### Casar { #match }

Si lo que estamos buscando es comprobar si una determinada cadena de texto «casa» (coincide) con un patrón de expresión regular, podemos hacer uso de la función `re.fullmatch()`.

A continuación se presenta un primer <span class="example">ejemplo:material-flash:</span> que comprueba **si un texto dado es un DNI válido**:

```pycon
>>> import re

>>> regex = r'\d{8}[A-Z]'#(1)!

>>> text = '54632178Y'
>>> re.fullmatch(regex, text)#(2)!
<re.Match object; span=(0, 9), match='54632178Y'>

>>> text = '87896532$'#(3)!
>>> re.fullmatch(regex, text)
```
{ .annotate }

1. Esta expresión regular es una «simplificación» ya que la letra del DNI (_dígito de control_) habría que calcularla utilizando un [algoritmo definido](https://www.interior.gob.es/opencms/es/servicios-al-ciudadano/tramites-y-gestiones/dni/calculo-del-digito-de-control-del-nif-nie/).
2. Cuando la cadena de texto «casa» con la expresión regular se devuelve un objeto de tipo [`Match`](https://docs.python.org/3/library/re.html#match-objects).
3. Cuando la cadena de texto no «casa» con la expresión regular se devuelve `#!python None`.

En este tipo de escenarios es habitual utilizar el [operador morsa](../../core/controlflow/conditionals.md#walrus) para discernir los casos a la vez que creamos una variable:

```pycon
>>> import re

>>> def check_id_card(text: str) -> None:
...     REGEX = r'(\d{8})([A-Z])'
...     if m := re.fullmatch(REGEX, text):#(1)!
...         print(f'{text} es un DNI válido')
...         print(f'N: {m[1]}  CC: {m[2]}')#(2)!
...     else:
...         print(f'{text} no es un DNI válido')

>>> check_id_card('54632178Y')
54632178Y es un DNI válido
N: 54632178  CC: Y

>>> check_id_card('87896532$')
87896532$ no es un DNI válido
```
{ .annotate }

1. En la variable `m` tendremos el objeto `Match` en el caso de que la cadena de texto haya casado.
2. Acceso a los grupos de captura.

!!! warning "Cuidado con `re.match()`"

    Hay una variante más «flexible» para casar que es re.match() y comprueba la existencia del patrón **sólo desde el comienzo de la cadena**. Es decir, que si el final de la cadena no coincide sigue casando.

    === "Caracteres al final"

        :material-check:{.green} Casa...
    
        ```pycon
        >>> regex = r'\d{8}[A-Z]'
        >>> text = '54632178Y###'
        
        >>> re.match(regex, text)
        <re.Match object; span=(0, 9), match='54632178Y'>
        ```
    
    === "Caracteres al principio"

        :material-cancel:{.red} No casa...
    
        ```pycon
        >>> regex = r'\d{8}[A-Z]'
        >>> text = '###54632178Y'
        
        >>> re.match(regex, text)
        ```

En cualquier caso podemos hacer que `re.match()` se comporte como `re.fullmatch()` si especificamos los **indicadores de comienzo y final de línea** en el patrón:

```pycon
>>> regex = r'^\d{8}[A-Z]$'#(1)!
>>> text = '54632178Y'

>>> re.match(regex, text)
<re.Match object; span=(0, 9), match='54632178Y'>
```
{ .annotate }

1.  - `^` indica comienzo de línea.
    - `$` indica final de línea.

#### Aclaraciones sobre corchetes { #squarebrackets }

Hay que tener en cuenta ciertos matices al utilizar corchetes `#!python []` en una expresión regular:

1. Los símbolos incluidos en los corchetes pierden su significado especial:

    ```pycon
    >>> re.match(r'[.]', 'A')#(1)!

    >>> re.match(r'[.]', '.')#(2)!
    <re.Match object; span=(0, 1), match='.'>
    ```
    { .annotate }
    
    1. No casa...
    2. Sí casa...
    
2. El guión medio hay que escaparlo en situaciones donde no represente un rango:

    ```pycon
    >>> re.match(r'[-\d\s]', '-')#(1)!
    <re.Match object; span=(0, 1), match='-'>
    
    >>> re.match(r'[\d\s-]', '-')#(2)!
    <re.Match object; span=(0, 1), match='-'>
    
    >>> re.match(r'[\d\-\s]', '-')#(3)!
    <re.Match object; span=(0, 1), match='-'>
    ```
    { .annotate }
    
    1. No hay que escapar ya que no representa un rango.
    2. No hay que escapar ya que no representa un rango.
    3. Hay que escapar porque «parece» que representa un rango.
    
## Ejercicios { #exercises }

1. [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `vowel-words`
2. [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `valid-float`
3. [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `valid-email`
4. [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `calc-from-str`
5. [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `valid-url`
