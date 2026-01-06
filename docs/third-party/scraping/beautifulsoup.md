---
icon: material/code-block-tags
tags:
  - Paquetes de terceros
  - Scraping
  - Beautiful Soup
---

# Beautiful Soup { #beautifulsoup }

![Banner](images/beautifulsoup/banner.jpg)
///caption
Imagen generada con Inteligencia Artificial
///

[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) es un paquete ampliamente utilizado en técnicas de «scraping»[^1] sobre contenido HTML y similares.

## Instalación { #install }

```console
pip install beautifulsoup4
```

## Modo de uso { #usage }

Es importante reseñar que la importación de este módulo es algo «particular» ya que se utiliza el nombre `bs4`:

```pycon
>>> import bs4
```

## Preparar la sopa { #soup }

Para ilustrar todos los <span class="example">ejemplos:material-flash:</span> vamos a partir del siguiente código HTML:

```html
<html lang="en">
<head>
    <title>Just testing</title>
</head>
<body>
    <h1>Just testing</h1>
    <div class="block">
      <h2>Some links</h2>
      <p>Hi there!</p>
      <ul id="data">
        <li class="blue"><a href="https://example1.com">Example 1</a></li>
        <li class="red"><a href="https://example2.com">Example 2</a></li>
        <li class="gold"><a href="https://example3.com">Example 3</a></li>
      </ul>
    </div>
    <div class="block">
      <h2>Formulario</h2>
      <form action="" method="post">
        <label for="POST-name">Nombre:</label>
        <input id="POST-name" type="text" name="name">
        <input type="submit" value="Save">
      </form>
    </div>
    <div class="footer">
      This is the footer
      <span class="inline"><p>This is span 1</p></span>
      <span class="inline"><p>This is span 2</p></span>
      <span class="inline"><p>This is span 2</p></span>
    </div>
</body>
</html>
```

Para empezar a trabajar con _Beautiful Soup_ es necesario construir un objeto de tipo [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/api/bs4.html#bs4.BeautifulSoup) que reciba el contenido a «parsear»:

```pycon
>>> from bs4 import BeautifulSoup

>>> contents = """
... <html lang="en">
... <head>
...     <title>Just testing</title>
... </head>
... <body>
...     <h1>Just testing</h1>
...     <div class="block">
...       <h2>Some links</h2>
...       <p>Hi there!</p>
...       <ul id="data">
...         <li class="blue"><a href="https://example1.com">Example 1</a></li>
...         <li class="red"><a href="https://example2.com">Example 2</a></li>
...         <li class="gold"><a href="https://example3.com">Example 3</a></li>
...       </ul>
...     </div>
...     <div class="block">
...       <h2>Formulario</h2>
...       <form action="" method="post">
...         <label for="POST-name">Nombre:</label>
...         <input id="POST-name" type="text" name="name">
...         <input type="submit" value="Save">
...       </form>
...     </div>
...     <div class="footer">
...       This is the footer
...       <span class="inline"><p>This is span 1</p></span>
...       <span class="inline"><p>This is span 2</p></span>
...       <span class="inline"><p>This is span 2</p></span>
...     </div>
... </body>
... </html>
... """

>>> soup = BeautifulSoup(contents, 'html.parser')#(1)!
```
{ .annotate }

1. Lo más habitual es usar el «parser» HTML, pero existen [otros](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser).

## Localizar elementos { #locate-elements }

En esta sección veremos distintas formas de localizar elementos en base a la naturaleza de la consulta.

### Selectores CSS { #css-selectors }

A continuación se muestran, mediante <span class="example">ejemplos:material-flash:</span>, distintas fórmulas para localizar elementos dentro del DOM utilizando para ello [selectores CSS](https://www.w3schools.com/cssref/css_selectors.php) mediante el método [`select()`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/api/bs4.html#bs4.Tag.select):

- [x] Localizar **todos los enlaces**:

```pycon
>>> soup.select('a')
[<a href="https://example1.com">Example 1</a>,
 <a href="https://example2.com">Example 2</a>,
 <a href="https://example3.com">Example 3</a>]
```

- [x] Localizar **todos los elementos con la clase `inline`**:

```pycon
>>> soup.select('.inline')
[<span class="inline"><p>This is span 1</p></span>,
 <span class="inline"><p>This is span 2</p></span>,
 <span class="inline"><p>This is span 2</p></span>]
```

- [x] Localizar **todos los `div` con la clase `footer`**:

```pycon
>>> soup.select('div.footer')
[<div class="footer">
       This is the footer
       <span class="inline"><p>This is span 1</p></span>
 <span class="inline"><p>This is span 2</p></span>
 <span class="inline"><p>This is span 2</p></span>
 </div>]
```

- [x] Localizar **todos los elementos cuyo atributo `type` tenga el valor `text`**:

```pycon
>>> soup.select('[type="text"]')
[<input id="POST-name" name="name" type="text"/>]
```

- [x] Localizar **todos los `input` y todos los `span`**:

```pycon
>>> soup.select('input,span')
[<input id="POST-name" name="name" type="text"/>,
 <input type="submit" value="Save"/>,
 <span class="inline"><p>This is span 1</p></span>,
 <span class="inline"><p>This is span 2</p></span>,
 <span class="inline"><p>This is span 2</p></span>]
```

- [x] Localizar **todos los párrafos que estén dentro del pie de página**:

```pycon
>>> soup.select('.footer p')
[<p>This is span 1</p>, <p>This is span 2</p>, <p>This is span 2</p>]
```

!!! tip "Un único elemento"

    Existe la opción de localizar **un único elemento** a través del método [`select_one()`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/api/bs4.html#bs4.Tag.select_one):

    ```pycon
    >>> soup.select_one('.footer p')
    <p>This is span 1</p>
    ```

### Reglas avanzadas { #advanced-rules }

A continuación se muestran, mediante <span class="example">ejemplos:material-flash:</span>, distintas fórmulas para localizar elementos dentro del DOM con reglas avanzadas mediante el método [`find_all()`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/api/bs4.html#bs4.element.Tag.find_all):

- [x] Localizar **todos los `h2` que contengan el texto `Formulario`**:

```pycon
>>> soup.find_all('h2', string='Formulario')
[<h2>Formulario</h2>]
```

- [x] Localizar **todos los elementos de título `h1`, `h2`, `h3`, ...**:

```pycon
>>> import re

>>> soup.find_all(re.compile(r'^h\d+.*'))#(1)!
[<h1>Just testing</h1>, <h2>Some links</h2>, <h2>Formulario</h2>]
```
{ .annotate }

1. Utilizamos [expresiones regulares](../../stdlib/text-processing/re.md) para resolver este problema.

:material-check-all:{ .blue } Se podría decir que la función `find_all()` es un superconjunto de `select()` ya que permite hacer lo mismo (también se pueden utilizar selectores CSS) pero abarca reglas avanzadas.

!!! tip "Un único elemento"

    Existe la opción de localizar **un único elemento** a través del método [`find()`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/api/bs4.html#bs4.Tag.find):

    ```pycon
    >>> soup.find('h2', string='Formulario')
    <h2>Formulario</h2>
    ```
  
### Cambiando el origen { #change-origin }

Todas las búsquedas se pueden realizar desde cualquier elemento preexistente, no únicamente desde la raíz del DOM.

- [x] Localizar **todos los «input» que cuelgan del segundo «div» con clase `block`**:

```pycon
>>> _, div2 = soup.select('div.block')#(1)!

>>> type(div2)#(2)!
bs4.element.Tag

>>> div2.select('input')
[<input id="POST-name" name="name" type="text"/>,
 <input type="submit" value="Save"/>]
```
{ .annotate }

1. Devuelve una lista con dos «divs». Nos quedamos con el segundo.
2. Estos objetos son de tipo [`Tag`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/api/bs4.html#bs4.Tag).

### Búsqueda relativa { #relative-search }

Hay definidas una serie de funciones adicionales que permiten hacer búsquedas (localizar elementos) de manera relativa al actual:

<div markdown>
- [x] Localizar **todos los `div` superiores al `li` con clase `blue`**:

```pycon
>>> soup.select_one('li.gold').find_parents('div')#(1)!
[<div class="block">
 <h2>Some links</h2>
 <p>Hi there!</p>
 <ul id="data">
 <li class="blue"><a href="https://example1.com">Example 1</a></li>
 <li class="red"><a href="https://example2.com">Example 2</a></li>
 <li class="gold"><a href="https://example3.com">Example 3</a></li>
 </ul>
 </div>]
```
{ .annotate }

1. También existe la versión de esta función para obtener un único elemento :material-arrow-right-bold: `find_parent()`.
</div>

<div markdown>
- [x] Localizar **todos los elementos «hermanos» siguientes al `li` con clase `blue`**:

```pycon
>>> soup.select_one('li.blue').find_next_siblings()#(1)!
[<li class="red"><a href="https://example2.com">Example 2</a></li>,
 <li class="gold"><a href="https://example3.com">Example 3</a></li>]
```
{ .annotate }

1. También existe la versión de esta función para obtener un único elemento :material-arrow-right-bold: `find_next_sibling()`.
</div>

- [x] Localizar **todos los elementos «hermanos» anteriores al `li` con clase `gold`**:

<div markdown>
```pycon
>>> soup.select_one('li.gold').find_previous_siblings()#(1)!
[<li class="red"><a href="https://example2.com">Example 2</a></li>,
 <li class="blue"><a href="https://example1.com">Example 1</a></li>]
```
{ .annotate }

1. También existe la versión de esta función para obtener un único elemento :material-arrow-right-bold: `find_previous_sibling()`.
</div>

- [x] Localizar **todos los elementos siguientes al `input` que tiene tipo `submit`**:

<div markdown>
```pycon
>>> soup.select_one('input[type="submit"]').find_all_next()#(1)!
[<div class="footer">
       This is the footer
       <span class="inline"><p>This is span 1</p></span>
 <span class="inline"><p>This is span 2</p></span>
 <span class="inline"><p>This is span 2</p></span>
 </div>,
 <span class="inline"><p>This is span 1</p></span>,
 <p>This is span 1</p>,
 <span class="inline"><p>This is span 2</p></span>,
 <p>This is span 2</p>,
 <span class="inline"><p>This is span 2</p></span>,
 <p>This is span 2</p>]
```
{ .annotate }

1. También existe la versión de esta función para obtener un único elemento :material-arrow-right-bold: `find_next()`.
</div>

<div markdown>
- [x] Localizar **todos los elementos `h1` y `h2` previos al `ul` con id `data`**:

```pycon
>>> soup.select_one('ul#data').find_all_previous(['h1', 'h2'])#(1)!
[<h2>Some links</h2>, <h1>Just testing</h1>]
```
{ .annotate }

1. También existe la versión de esta función para obtener un único elemento :material-arrow-right-bold: `find_previous()`.
</div>

## Acceder al contenido { #access-content }

Simplificando, podríamos decir que cada elemento de la famosa «sopa» de _Beautiful Soup_ puede ser un [`bs4.element.Tag`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/api/bs4.html#bs4.Tag) o un «[string](../../core/datatypes/strings.md)».

En el caso de los «tags» existe la posibilidad de acceder a su contenido, al nombre del elemento o a sus atributos.

### Nombre de etiqueta { #name-access }

Podemos conocer el nombre de la etiqueta de un elemento usando el atributo `name`:

```pycon
>>> soup.name
'[document]'

>>> elem = soup.select_one('ul#data')
>>> elem.name
'ul'

>>> elem = soup.select_one('h1')
>>> elem.name
'h1'
```

### Acceso a atributos { #attrs-access }

Los atributos de un elemento están disponibles como claves de un diccionario:

```pycon
>>> elem = soup.select_one('input#POST-name')

>>> elem
<input id="POST-name" name="name" type="text"/>

>>> elem['id']
'POST-name'

>>> elem['name']
'name'

>>> elem['type']
'text'

>>> elem.attrs
{'id': 'POST-name', 'type': 'text', 'name': 'name'}
```

### Contenido textual { #text-access }

Es importante aclarar las distintas opciones que proporciona _Beautiful Soup_ para acceder al contenido textual de los elementos del DOM:

=== "`.text`"
    
    Devuelve una [cadena de texto](../../core/datatypes/strings.md) con todos los contenidos textuales del elemento incluyendo espacios y saltos de línea.

    ```pycon
    >>> footer = soup.select_one('.footer')
    
    >>> footer.text
    '\n      This is the footer\n      This is span 1\nThis is span 2\nThis is span 2\n'
    ```

=== "`.strings`"

    Devuelve un [generador](../../core/modularity/functions.md#generators) de todos los contenidos textuales del elemento incluyendo espacios y saltos de línea.

    ```pycon
    >>> footer = soup.select_one('.footer')

    >>> list(footer.strings)
    ['\n      This is the footer\n      ',
     'This is span 1',
     '\n',
     'This is span 2',
     '\n',
     'This is span 2',
     '\n']
    ```
    
=== "`.stripped_strings`"

    Devuelve un [generador](../../core/modularity/functions.md#generators) de todos los contenidos textuales del elemento eliminando espacios y saltos de línea.

    ```pycon
    >>> footer = soup.select_one('.footer')
    
    >>> list(footer.stripped_strings)
    ['This is the footer', 'This is span 1', 'This is span 2', 'This is span 2']
    ```

=== "`.string`"

    Devuelve una [cadena de texto](../../core/datatypes/strings.md) con el contenido dele elemento, siempre que contenga un único elemento textual.

    ```pycon
    >>> footer = soup.select_one('.footer')

    >>> footer.string#(1)!

    
    >>> footer.span.string#(2)!
    'This is span 1'
    ```
    { .annotate }
    
    1. El «footer» contiene varios elementos.
    2. El «span» sólo contiene un elemento.

#### Mostrando elementos { #display-elements }

Cualquier elemento del DOM que seleccionemos mediante este paquete se representa con el código HTML que contiene:

```pycon
>>> elem = soup.select_one('#data')

>>> elem
<ul id="data">
<li class="blue"><a href="https://example1.com">Example 1</a></li>
<li class="red"><a href="https://example2.com">Example 2</a></li>
<li class="gold"><a href="https://example3.com">Example 3</a></li>
</ul>
```

Existe la posibilidad de mostrar el código HTML en formato «mejorado» a través de la función [`prettify`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/api/bs4.html#bs4.Tag.prettify):

```pycon
>>> print(elem.prettify())
<ul id="data">
 <li class="blue">
  <a href="https://example1.com">
   Example 1
  </a>
 </li>
 <li class="red">
  <a href="https://example2.com">
   Example 2
  </a>
 </li>
 <li class="gold">
  <a href="https://example3.com">
   Example 3
  </a>
 </li>
</ul>
```

## Navegar por el DOM { #dom-browse }

Además de localizar elementos, este paquete permite moverse por los elementos del DOM de manera muy sencilla.

### Descendientes { #descendants }

Para ir profundizando (descendiendo) en el DOM podemos utilizar los **nombres de los «tags» como atributos del objeto**, teniendo en cuenta que si existen múltiples elementos sólo se accederá al primero de ellos:

```pycon
>>> soup.div.p
<p>Hi there!</p>

>>> soup.form.label
<label for="POST-name">Nombre:</label>

>>> type(soup.span)
bs4.element.Tag
```

Existe la opción de **obtener el contenido (como lista) de un determinado elemento**:

```pycon
>>> soup.form.contents#(1)!
['\n',
 <label for="POST-name">Nombre:</label>,
 '\n',
 <input id="POST-name" name="name" type="text"/>,
 '\n',
 <input type="submit" value="Save"/>,
 '\n']
```
{ .annotate }

1. En esta lista hay una mezcla de «strings» y objetos `bs4.element.Tag`.

Si no se quiere explicitar el contenido de un elemento como lista, también es posible usar un [generador](../../core/modularity/functions.md#generators) para **acceder al mismo de forma secuencial**:

- [x] Localizar **todos los elementos hijos del formulario**:

```pycon
>>> soup.form.children
<generator object Tag.children.<locals>.<genexpr> at 0x10740a2c0>

>>> for elem in soup.form.children:
...     if isinstance(elem, bs4.element.Tag):#(1)!
...         print(repr(elem))
...
<label for="POST-name">Nombre:</label>
<input id="POST-name" name="name" type="text"/>
<input type="submit" value="Save"/>
```
{ .annotate }

1.  - Entre los elementos hijos también se encuentran los saltos de línea `#!python '\n'`.
    - Es por ello que planteamos esta condición para quederanos únicamente con objetos de tipo `Tag`.

!!! note "Descendientes"

    Existe la propiedad [`.descendants()`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/api/bs4.html#bs4.Tag.descendants) que itera sobre todos los elementos hijos mediante [búsqueda en anchura](https://es.wikipedia.org/wiki/B%C3%BAsqueda_en_anchura).

### Ascendientes { #ancestor }

Para acceder al elemento superior de otro dado, podemos usar el atributo parent:

- [x] Localizar **el elemento superior al `li` con clase `blue`**:

```pycon
>>> soup.select_one('li.blue').parent
<ul id="data">
<li class="blue"><a href="https://example1.com">Example 1</a></li>
<li class="red"><a href="https://example2.com">Example 2</a></li>
<li class="gold"><a href="https://example3.com">Example 3</a></li>
</ul>
```

- [x] Localizar **todos los elementos superiores (ascendientes) al `li` con clase `blue`**:

```pycon
>>> asc = soup.select_one('li.blue').parents

>>> for elem in asc:
...     print(elem.name)
...
ul
div
body
html
[document]
```

!!! exercise "Ejercicio"

    Escribe un programa en Python que obtenga de https://pypi.org datos estructurados de los «Trending projects» y los muestre por pantalla utilizando el siguiente formato:

    `<nombre-del-paquete>,<versión>,<descripción>,<url>`

    Se recomienda usar el paquete [`requests`](../networking/requests.md) para obtener el código fuente de la página. Hay que tener en cuenta que el listado de paquetes cambia cada pocos segundos, a efectos de comprobación.

    [:material-lightbulb: Solución](files/beautifulsoup/pypi-trend.py)





[^1]: El «scraping» HTML es un proceso automatizado para extraer información de sitios web, utilizando el código HTML como base para identificar y extraer los datos relevantes.
