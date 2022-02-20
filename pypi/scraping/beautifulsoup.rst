#############
beautifulsoup
#############

.. image:: img/ella-olsson-fxJTl_gDh28-unsplash.jpg

El paquete `Beautiful Soup <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`__ es ampliamente utilizado en técnicas de "scraping" permitiendo "parsear"[#html-parsing]_ principalmente código HTML. [#soup-unsplash]_

.. code-block:: console

    $ pip install beautifulsoup4

****************
Haciendo la sopa
****************

Para empezar a trabajar con *Beautiful Soup* es necesario construir un objeto de tipo ``BeautifulSoup`` que reciba el contenido a "parsear"::

    >>> from bs4 import BeautifulSoup

    >>> contents = '''
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
    ... '''

    >>> soup = BeautifulSoup(contents, features='html.parser')

.. attention:: Importar el paquete usando ``bs4``. Suele llevar a equívoco por el nombre original.

A partir de aquí se abre un abanico de posibilidades que iremos desgranando en los próximos epígrafes.

*******************
Localizar elementos
*******************

Una de las tareas más habituales en técnicas de "scraping" y en "parsing" de contenido es la localización de determinadas elementos de interés.

Fórmulas de localización
========================

A continuación se muestran, mediante ejemplos, distintas fórmulas para localizar elementos dentro del DOM [#html-dom]_:

- Localizar **todos los enlaces**::

    >>> soup.find_all('a')
    [<a href="https://example1.com">Example 1</a>,
     <a href="https://example2.com">Example 2</a>,
     <a href="https://example3.com">Example 3</a>]

  El primer :ref:`argumento posicional <core/modularity/functions:Argumentos posicionales>` de ``find_all()`` es el nombre del "tag" que queremos localizar.

- Localizar todos los **elementos con la clase** ``inline``::

    >>> soup.find_all(class_='inline')
    [<span class="inline"><p>This is span 1</p></span>,
     <span class="inline"><p>This is span 2</p></span>,
     <span class="inline"><p>This is span 2</p></span>]

  Los :ref:`argumentos nominales <core/modularity/functions:Argumentos nominales>` de ``find_all()`` se utilizan para localizar elementos que contengan el atributo referenciado.

  .. tip::
      Si el atributo a localizar tiene guiones medios (por ejemplo ``aria-label``) no podremos usarlo como nombre de argumento (error sintáctico). Pero sí podemos usar un diccionario en su lugar::

          soup.find_all(attrs={'aria-label': 'box'})

- Localizar todos los "divs" con la clase ``footer``::
  
    >>> soup.find_all('div', class_='footer')  # ≈ soup.find_all('div', 'footer')
    [<div class="footer">
           This is the footer
           <span class="inline"><p>This is span 1</p></span>
     <span class="inline"><p>This is span 2</p></span>
     <span class="inline"><p>This is span 2</p></span>
     </div>]

- Localizar todos los elementos cuyo atributo ``type`` tenga el valor ``text``::
  
    >>> soup.find_all(type='text')
    [<input id="POST-name" name="name" type="text"/>]

- Localizar todos los elementos de título ``h1, h2, h3, ...``::
  
    >>> soup.find_all(re.compile(r'^h\d+.*'))
    [<h1>Just testing</h1>, <h2>Some links</h2>, <h2>Formulario</h2>]
  
  Es posible incluir **expresiones regulares** a la hora de localizar elementos.

- Localizar todos los "input" y todos los "span"::

    >>> soup.find_all(['input', 'span'])
    [<input id="POST-name" name="name" type="text"/>,
     <input type="submit" value="Save"/>,
     <span class="inline"><p>This is span 1</p></span>,
     <span class="inline"><p>This is span 2</p></span>,
     <span class="inline"><p>This is span 2</p></span>]
  
- Localizar todos los párrafos que están dentro del pie de página (usando **selectores CSS**)::
  
    >>> soup.select('.footer p')
    [<p>This is span 1</p>, <p>This is span 2</p>, <p>This is span 2</p>]

  .. note::
      En este caso se usa el método ``select()``.

Localizar único elemento
========================

Hasta ahora hemos visto las funciones ``find_all()`` y ``select()`` que localizan un conjunto de elementos. Incluso en el caso de encontrar sólo un elemento, se devuelve una lista con ese único elemento.

*Beautiful Soup* nos proporciona la función ``find()`` que trata de **localizar un único elemento**. Hay que tener en cuenta dos circunstancias:

- En caso de que el elemento buscado no exista, se devuelve :ref:`None <core/controlflow/conditionals:Valor nulo>`.
- En caso de que existan múltiples elementos, se devuelve el primero.

Veamos algunos ejemplos de esto::

    >>> soup.find('form')
    <form action="" method="post">
    <label for="POST-name">Nombre:</label>
    <input id="POST-name" name="name" type="text"/>
    <input type="submit" value="Save"/>
    </form>

    >>> # Elemento que no existe
    >>> soup.find('strange-tag')
    >>>

    >>> # Múltiples "li". Sólo se devuelve el primero
    >>> soup.find('li')
    <li class="blue"><a href="https://example1.com">Example 1</a></li>

Localizar desde elemento
========================

Todas las búsquedas se pueden realizar desde cualquier elemento preexistente, no únicamente desde la raíz del DOM.

Veamos un ejemplo de ello. Si tratamos de **localizar todos los títulos "h2"** vamos a encontrar dos de ellos::

    >>> soup.find_all('h2')
    [<h2>Some links</h2>, <h2>Formulario</h2>]

Pero si, previamente, nos ubicamos en el segundo bloque de contenido, sólo vamos a encontrar uno de ellos::

    >>> second_block = soup.find_all('div', 'block')[1]

    >>> second_block
    <div class="block">
    <h2>Formulario</h2>
    <form action="" method="post">
    <label for="POST-name">Nombre:</label>
    <input id="POST-name" name="name" type="text"/>
    <input type="submit" value="Save"/>
    </form>
    </div>

    >>> second_block.find_all('h2')
    [<h2>Formulario</h2>]

Otras funciones de búsqueda
===========================

Hay definidas una serie de funciones adicionales de búsqueda para cuestiones más particulares:

- Localizar los **"div" superiores** a partir de un elemento concreto::
  
    >>> gold = soup.find('li', 'gold')

    >>> gold.find_parents('div')
    [<div class="block">
     <h2>Some links</h2>
     <p>Hi there!</p>
     <ul id="data">
     <li class="blue"><a href="https://example1.com">Example 1</a></li>
     <li class="red"><a href="https://example2.com">Example 2</a></li>
     <li class="gold"><a href="https://example3.com">Example 3</a></li>
     </ul>
     </div>]
    
  Se podría decir que la función ``find_all()`` busca en *descendientes* y que la función ``find_parents()`` busca en *ascendientes*.
  
  También existe la versión de esta *función que devuelve un único elemento*: ``find_parent()``.

- Localizar los **elementos hermanos siguientes** a uno dado::
  
    >>> blue_li = soup.find('li', 'blue')

    >>> blue_li.find_next_siblings()
    [<li class="red"><a href="https://example2.com">Example 2</a></li>,
    <li class="gold"><a href="https://example3.com">Example 3</a></li>]

  Al igual que en las anteriores, es posible aplicar un filtro al usar esta función.
  
  También existe la versión de esta *función que devuelve un único elemento*: ``find_next_sibling()``.

- Localizar los **elementos hermanos anteriores** a uno dado::

    >>> gold_li = soup.find('li', 'gold')

    >>> gold_li.find_previous_siblings()
    [<li class="red"><a href="https://example2.com">Example 2</a></li>,
    <li class="blue"><a href="https://example1.com">Example 1</a></li>]

  Al igual que en las anteriores, es posible aplicar un filtro al usar esta función.
  
  También existe la versión de esta *función que devuelve un único elemento*: ``find_previous_sibling()``.

- Localizar **todos los elementos a continuación** de uno dado::

    >>> submit = soup.find('input', type='submit')

    >>> submit.find_all_next()
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

  Al igual que en las anteriores, es posible aplicar un filtro al usar esta función.
  
  También existe la versión de esta *función que devuelve un único elemento*: ``find_next()``.

- Localizar **todos los elementos previos** a uno dado::

    >>> ul_data = soup.find('ul', id='data')

    >>> ul_data.find_all_previous(['h1', 'h2'])
    [<h2>Some links</h2>, <h1>Just testing</h1>]

  También existe la versión de esta *función que devuelve un único elemento*: ``find_previous()``.

  Si hubiéramos hecho esta búsqueda usando ``find_parents()`` no habríamos obtenido el mismo resultado ya que los elementos de título no son elementos superiores de "ul"::

    >>> ul_data.find_parents(['h1', 'h2'])
    []

Atajo para búsquedas
====================

Dado que la función ``find_all()`` es la más utilizada en *Beautiful Soup* se ha implementado un atajo para llamarla:

.. code-block::
    :emphasize-lines: 6

    >>> soup.find_all('span')
    [<span class="inline"><p>This is span 1</p></span>,
     <span class="inline"><p>This is span 2</p></span>,
     <span class="inline"><p>This is span 2</p></span>]

    >>> soup('span')
    [<span class="inline"><p>This is span 1</p></span>,
     <span class="inline"><p>This is span 2</p></span>,
     <span class="inline"><p>This is span 2</p></span>]

Aunque uno de los preceptos del :ref:`Zen de Python <core/introduction/python:Zen de Python>` es "Explicit is better than implicit", el uso de estos atajos puede estar justificado en función de muchas circunstancias.

********************
Acceder al contenido
********************

Simplificando, podríamos decir que cada elemento de la famosa "sopa" de *Beautiful Soup* puede ser un ``bs4.element.Tag`` o un "string".

Para el caso de los "tags" existe la posibilidad de acceder a su contenido, al nombre del elemento o a sus atributos.

Nombre de etiqueta
==================

Podemos conocer el nombre de la etiqueta de un elemento usando el atributo ``name``::

    >>> soup.name
    '[document]'

    >>> elem = soup.find('ul', id='data')
    >>> elem.name
    'ul'

    >>> elem = soup.find('h1')
    >>> elem.name
    'h1'

.. tip::
    Es posible modificar el nombre de una etiqueta con una simple asignación.

Acceso a atributos
==================

Los atributos de un elemento están disponibles como claves de un diccionario::

    >>> elem = soup.find('input', id='POST-name')

    >>> elem
    <input id="POST-name" name="name" type="text"/>

    >>> elem['id']
    'POST-name'

    >>> elem['name']
    'name'

    >>> elem['type']
    'text'

Exite una forma de acceder al diccionario completo de atributos::

    >>> elem.attrs
    {'id': 'POST-name', 'type': 'text', 'name': 'name'}

.. tip::
    Es posible modificar el valor de un atributo con una simple asignación.

Contenido textual
=================

Es necesario aclarar las distintas opciones que proporciona *Beautiful Soup* para acceder al contenido textual de los elementos del DOM.

+----------------------+------------------------------------------------------------------------------------------------------------+
| Atributo             | Devuelve                                                                                                   |
+======================+============================================================================================================+
| ``text``             | Una cadena de texto con todos los contenidos textuales del elemento incluyendo espacios y saltos de línea  |
+----------------------+------------------------------------------------------------------------------------------------------------+
| ``strings``          | Un generador de todos los contenidos textuales del elemento incluyendo espacios y saltos de línea          |
+----------------------+------------------------------------------------------------------------------------------------------------+
| ``stripped_strings`` | Un generador de todos los contenidos textuales del elemento eliminando espacios y saltos de línea          |
+----------------------+------------------------------------------------------------------------------------------------------------+
| ``string``           | Una cadena de texto con el contenido del elemento, siempre que contenga un único elemento textual          |
+----------------------+------------------------------------------------------------------------------------------------------------+

Ejemplos::

    >>> footer = soup.find(class_='footer')

    >>> footer.text
    '\n      This is the footer\n      This is span 1\nThis is span 2\nThis is span 2\n'

    >>> list(footer.strings)
    ['\n      This is the footer\n      ',
     'This is span 1',
     '\n',
     'This is span 2',
     '\n',
     'This is span 2',
     '\n']

    >>> list(footer.stripped_strings)
    ['This is the footer', 'This is span 1', 'This is span 2', 'This is span 2']

    >>> footer.string       # El "footer" contiene varios elementos

    >>> footer.span.string  # El "span" sólo contiene un elemento
    'This is span 1'

Mostrando elementos
-------------------

Cualquier elemento del DOM que seleccionemos mediante este paquete se representa con el código HTML que contiene. Por ejemplo::

    >>> data = soup.find(id='data')

    >>> data
    <ul id="data">
    <li class="blue"><a href="https://example1.com">Example 1</a></li>
    <li class="red"><a href="https://example2.com">Example 2</a></li>
    <li class="gold"><a href="https://example3.com">Example 3</a></li>
    </ul>

Existe la posibilidad de mostrar el código HTML en formato "mejorado" a través de la función ``prettify()``::

    >>> pretty_data = data.prettify()

    >>> print(pretty_data)
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

******************
Navegar por el DOM
******************

Además de localizar elementos, este paquete permite moverse por los elementos del DOM de manera muy sencilla.

Moverse hacia abajo
===================

Para ir profundizando en el DOM podemos utilizar los **nombres de los "tags" como atributos del objeto**, teniendo en cuenta que si existen múltiples elementos sólo se accederá al primero de ellos::

    >>> soup.div.p
    <p>Hi there!</p>

    >>> soup.form.label
    <label for="POST-name">Nombre:</label>

    >>> type(soup.span)
    bs4.element.Tag

Existe la opción de obtener el **contenido (como lista) de un determinado elemento**:

.. code-block::
    :emphasize-lines: 4

    >>> type(soup.form)  # todos los elementos del DOM son de este tipo
    bs4.element.Tag

    >>> soup.form.contents
    ['\n',
     <label for="POST-name">Nombre:</label>,
     '\n',
     <input id="POST-name" name="name" type="text"/>,
     '\n',
     <input type="submit" value="Save"/>,
     '\n']

    >>> type(soup.form.contents)
    list

.. warning::
    En la lista que devuelve ``contents`` hay mezcla de "strings" y objetos ``bs4.element.Tag``.

Si no se quiere explicitar el contenido de un elemento como lista, también es posible usar un :ref:`generador <core/modularity/functions:Generadores>` para **acceder al mismo de forma secuencial**::

    >>> soup.form.children
    <list_iterator at 0x106643100>

    >>> for elem in soup.form.children:
    ...     print(repr(elem))
    ...
    '\n'
    <label for="POST-name">Nombre:</label>
    '\n'
    <input id="POST-name" name="name" type="text"/>
    '\n'
    <input type="submit" value="Save"/>
    '\n'

El atributo ``contents`` sólo tiene en cuenta descendientes directos. Si queremos **acceder a cualquier elemento descendiente (de manera recursiva)** tenemos que usar ``descendants``::

    >>> block = soup.find_all('div')[1]

    >>> block.contents
    ['\n',
     <h2>Formulario</h2>,
     '\n',
     <form action="" method="post">
     <label for="POST-name">Nombre:</label>
     <input id="POST-name" name="name" type="text"/>
     <input type="submit" value="Save"/>
     </form>,
     '\n']

    >>> block.descendants
    <generator object Tag.descendants at 0x10675d200>

    >>> list(block.descendants)
    ['\n',
     <h2>Formulario</h2>,
     'Formulario',
     '\n',
     <form action="" method="post">
     <label for="POST-name">Nombre:</label>
     <input id="POST-name" name="name" type="text"/>
     <input type="submit" value="Save"/>
     </form>,
     '\n',
     <label for="POST-name">Nombre:</label>,
     'Nombre:',
     '\n',
     <input id="POST-name" name="name" type="text"/>,
     '\n',
     <input type="submit" value="Save"/>,
     '\n',
     '\n']

.. important::
    Tener en cuenta que ``descendants`` es un generador que devuelve un iterable.

Moverse hacia arriba
====================

Para acceder al **elemento superior de otro dado**, podemos usar el atributo ``parent``::

    >>> li = soup.find('li', 'blue')

    >>> li.parent
    <ul id="data">
    <li class="blue"><a href="https://example1.com">Example 1</a></li>
    <li class="red"><a href="https://example2.com">Example 2</a></li>
    <li class="gold"><a href="https://example3.com">Example 3</a></li>
    </ul>

También podemos acceder a **todos los elementos superiores (ascendientes)** usando el generador ``parents``::

    >>> for elem in li.parents:
    ...     print(elem.name)
    ...
    ul
    div
    body
    html
    [document]

Otros movimientos
=================

En la siguiente tabla se recogen el resto de atributos que nos permiten movernos a partir de un elemento del DOM:

+-----------------------+--------------------------------------------------------+
|       Atributo        |                      Descripción                       |
+=======================+========================================================+
| ``next_sibling``      | Obtiene el siguiente elemento "hermano"                |
+-----------------------+--------------------------------------------------------+
| ``previous_sibling``  | Obtiene el anterior elemento "hermano"                 |
+-----------------------+--------------------------------------------------------+
| ``next_siblings``     | Obtiene los siguientes elementos "hermanos" (iterador) |
+-----------------------+--------------------------------------------------------+
| ``previous_siblings`` | Obtiene los anteriores elementos "hermanos" (iterador) |
+-----------------------+--------------------------------------------------------+
| ``next_element``      | Obtiene el siguiente elemento                          |
+-----------------------+--------------------------------------------------------+
| ``previous_element``  | Obtiene el anterior elemento                           |
+-----------------------+--------------------------------------------------------+

.. warning::
    Con estos accesos también se devuelven los saltos de línea ``'\n'`` como elementos válidos. Si se quieren evitar, es preferible usar las :ref:`funciones definidas aquí <pypi/scraping/beautifulsoup:Localizar elementos>`.

.. admonition:: Ejercicio
    :class: exercise

    Escriba un programa en Python que obtenga de https://pypi.org datos estructurados de los "Trending projects" y los muestre por pantalla utilizando el siguiente formato:

    ``<nombre-del-paquete>,<versión>,<descripción>,<url>``

    Se recomienda usar el paquete :ref:`requests <pypi/scraping/requests:requests>` para obtener el código fuente de la página. Hay que tener en cuenta que el listado de paquetes cambia cada pocos segundos, a efectos de comprobación.

    .. only:: html
    
        |solution| :download:`pypi-trend.py <files/pypi-trend.py>`

.. --------------- Footnotes ---------------

.. [#soup-unsplash] Foto original de portada por `Ella Olsson`_ en Unsplash.
.. [#html-parsing] Analizar y convertir una entrada en un formato interno que el entorno de ejecución pueda realmente manejar.
.. [#html-dom] Document Object Model en español Modelo de Objetos del Documento.

.. --------------- Hyperlinks ---------------

.. _Ella Olsson: https://unsplash.com/@ellaolsson?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
