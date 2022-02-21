########
requests
########

.. image:: img/frame-harirak-2oBDlim9r98-unsplash.jpg

El paquete `requests <https://docs.python-requests.org/>`__ es uno de los paquetes más famosos del ecosistema Python. Como dice su lema "HTTP for Humans" permite realizar peticiones HTTP de una forma muy sencilla y realmente potente. [#plane-unsplash]_

.. code-block:: console

    $ pip install requests

*********************
Realizar una petición
*********************

Realizar una petición HTTP mediante *requests* es realmente sencillo::

    >>> import requests

    >>> response = requests.get('https://pypi.org')

Hemos ejecutado una :ref:`solicitud GET <pypi/scraping/requests:Tipos de peticiones>` al sitio web https://pypi.org. La respuesta se almacena en un objeto de tipo ``requests.models.Response`` muy rica en métodos y atributos que veremos a continuación::

    >>> type(response)
    requests.models.Response

Quizás lo primero que nos interese sea ver el contenido de la respuesta. En este sentido *requests* nos provee del atributo ``text`` que contendrá el **contenido html** del sitio web en cuestión como cadena de texto::

    >>> response.text
    '\n\n\n\n\n\n<!DOCTYPE html>\n<html lang="en" dir="ltr">\n  <head>\n    <meta charset="utf-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n\n    <meta name="defaultLanguage" content="en">\n    <meta name="availableLanguages" content="en, es, fr, ja, pt_BR, uk, el, de, zh_Hans, zh_Hant, ru, he, eo">\n\n    \n\n    <title>PyPI · The Python Package Index</title>\n    <meta name="description" content="The Python Package Index (PyPI) is a repository of software for the Python programming language.">\n\n    <link rel="stylesheet" href="/static/css/warehouse-ltr.69ee0d4e.css">\n    <link rel="stylesheet" href="/static/css/fontawesome.6002a161.css">\n    <link rel="stylesheet" href="/static/css/regular.98fbf39a.css">\n    <link rel="stylesheet" href="/static/css/solid.c3b5f0b5.css">\n    <link rel="stylesheet" href="/static/css/brands.2c303be1.css">\n    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400italic,600,600italic,700,700italic%7CSource+Code+Pro:500">\n    <noscript>\n      <link rel="stylesheet" href="/static/css/noscript.d4ce1e76.css">\n'

.. note:: Se ha recortado la salida a efectos visuales.

Algo que es realmente importante en una petición HTTP es comprobar el estado de la misma. Por regla general, si todo ha ido bien, deberíamos obtener un **código 200**, pero existen muchos otros `códigos de estado de respuesta HTTP <https://developer.mozilla.org/es/docs/Web/HTTP/Status>`_::

    >>> response.status_code
    200

.. tip:: Para evitar la comparación directa con el literal 200, existe la variable ``requests.codes.ok``.

*******************
Tipos de peticiones
*******************

Con *requests* podemos realizar peticiones mediante cualquier método HTTP [#http-methods]_. Para ello, simplemente usamos el método correspondiente del paquete:

+--------------+------------------------+
| Método HTTP  | Llamada                |
+==============+========================+
| GET          | ``requests.get()``     |
+--------------+------------------------+
| POST         | ``requests.post()``    |
+--------------+------------------------+
| PUT          | ``requests.put()``     |
+--------------+------------------------+
| DELETE       | ``requests.delete()``  |
+--------------+------------------------+
| HEAD         | ``requests.head()``    |
+--------------+------------------------+
| OPTIONS      | ``requests.options()`` |
+--------------+------------------------+

*****************
Usando parámetros
*****************

Cuando se realiza una petición HTTP es posible incluir parámetros. Veamos distintas opciones que nos ofrece *requests* para ello.

Query string
============

En una petición GET podemos incluir parámetros en el llamado "query string". Los parámetros se definen mediante un :ref:`diccionario <core/datastructures/dicts:Diccionarios>` con nombre y valor de parámetro.

Veamos un ejemplo sencillo. Supongamos que queremos **buscar paquetes de Python** que contengan la palabra "astro"::

    >>> payload = {'q': 'astro'}

    >>> response = requests.get('https://pypi.org', params=payload)

    >>> response.url
    'https://pypi.org/?q=astro'

.. tip:: El atributo ``url`` nos devuelve la URL a la se ha accedido. Útil en el caso de paso de parámetros.

Parámetros POST
===============

Una petición POST, por lo general, siempre va acompañada de una serie de parámetros que típicamente podemos encontrar en un formulario web. Es posible realizar estas peticiones en *requests* adjuntando los parámetros que necesitemos en el mismo formato de diccionario que hemos visto para "query string".

Supongamos un ejemplo en el que tratamos de **logearnos en la página de GIPHY** con nombre de usuario y contraseña. Para ello, lo primero que debemos hacer es inspeccionar [#inspect-tools]_ los elementos del formulario e identificar los nombres ("name") de los campos. En este caso los campos son ``email`` y ``password``::

    >>> url = 'https://giphy.com/login'
    >>> payload = {'email': 'sdelquin@gmail.com', 'password': '1234'}

    >>> response = requests.post(url, data=payload)
    >>> response.status_code
    403

Hemos obtenido un código de estado 403 indicando que el acceso está prohibido.

Envío de cabeceras
==================

Hay veces que necesitamos modificar o añadir determinados campos en las cabeceras [#http-headers]_ de la petición. Su tratamiento también se realiza a base de diccionarios que son pasados al método correspondiente.

Uno de los usos más típicos de las cabeceras es el "user agent"[#user-agent]_ donde se especifica el tipo de navegador que realiza la petición. Supongamos un ejemplo en el que queremos especificar que **el navegador corresponde con un Google Chrome corriendo sobre Windows 10**::

    >>> user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    >>> headers = {'user-agent': user_agent}

    >>> response = requests.get('https://pypi.org', headers=headers)

    >>> response.status_code
    200

***********************
Analizando la respuesta
***********************

A continuación analizaremos distintos **elementos que forman parte de la respuesta HTTP** tras realizar la petición.

Contenido JSON
==============

El formato `JSON`_ es ampliamente utilizado para el intercambio de datos entre aplicaciones. Hay ocasiones en las que la respuesta a una petición viene en dicho formato. Para facilitar su tratamiento *requests* nos proporciona un método que convierte el contenido JSON a un diccionario de Python.

Supongamos que queremos tener un **pronóstico del tiempo** en `Santa Cruz de Tenerife`_. Existen múltiples servicios online que ofrecen datos meteorológicos. En este caso vamos a usar https://open-meteo.com/. La cuestión es que *los datos que devuelve esta API son en formato JSON*. Así que aprovecharemos para convertirlos de forma apropiada:

.. code-block::
    :emphasize-lines: 10

    >>> sc_tfe = (28.4578025, -16.3563748)
    >>> params = dict(latitude=sc_tfe[0], longitude=sc_tfe[1], hourly='temperature_2m')
    >>> url = 'https://api.open-meteo.com/v1/forecast'

    >>> response = requests.get(url, params=params)

    >>> response.url
    'https://api.open-meteo.com/v1/forecast?latitude=28.4578025&longitude=-16.3563748&hourly=temperature_2m'

    >>> data = response.json()

    >>> type(data)
    dict

    >>> data.keys()
    dict_keys(['utc_offset_seconds', 'elevation', 'latitude', 'hourly_units', 'longitude', 'generationtime_ms', 'hourly'])

Ahora podríamos mostrar la predicción de temperatures de una manera algo más visual. Según la documentación de la API sabemos que la respuesta contiene 168 medidas de temperatura correspondientes a todas las horas durante 7 días. Supongamos que sólo queremos **mostrar la predicción de temperaturas hora a hora para el día de mañana**::

    >>> temperatures = data['hourly']['temperature_2m']

    >>> # Las temperaturas también incluyen el día de hoy
    >>> for i, temp in enumerate(temperatures[24:48], start=1):
    ...     print(f'{temp:4.1f}', end=' ')
    ...     if i % 6 == 0:
    ...         print()
    ...
    12.0 11.9 11.9 11.8 11.8 11.7
    11.7 11.7 11.6 12.0 12.8 13.6
    13.9 14.0 14.1 13.9 13.7 13.3
    12.8 12.2 11.8 11.7 11.6 11.5

Cabeceras de respuesta
======================

Tras una petición HTTP es posible recuperar las cabeceras que vienen en la respuesta a través del atributo ``headers`` como un diccionario::

    >>> response = requests.get('https://pypi.org')
    >>> response.status_code
    200

    >>> response.headers.get('Content-Type')
    'text/html; charset=UTF-8'

    >>> response.headers.get('Server')
    'nginx/1.13.9'

Cookies
=======

Si una respuesta contiene "cookies"[#http-cookies]_ es posible acceder a ellas mediante el diccionario ``cookies``::

    >>> response = requests.get('https://github.com')

    >>> response.cookies.keys()
    ['_octo', 'logged_in', '_gh_sess']

    >>> response.cookies.get('logged_in')
    'no'

.. note:: Las cookies también se pueden enviar en la petición usando ``requests.get(url, cookies=cookies)``.

.. admonition:: Ejercicio
    :class: exercise

    Utilizando el paquete *requests*, haga una petición GET a https://twitter.com y obtenga los siguientes campos:

    - Código de estado.
    - Longitud de la respuesta.
    - Valor de la cookie ``guest_id``
    - Valor de la cabecera ``content-encoding``

    .. only:: html
    
        |solution| :download:`req.py <files/req.py>`

********************
Descargar un fichero
********************

Hay ocasiones en las que usamos *requests* para descargar un fichero, bien sea en texto plano o binario. Veamos cómo proceder para cada tipo.

Ficheros en texto plano
=======================

El procedimiento que utilizamos es descargar el contenido desde la url y :ref:`volcarlo a un fichero <core/datastructures/files:Escritura en un fichero>` de manera estándar::

    >>> url = 'https://www.ine.es/jaxi/files/tpx/es/csv_bdsc/50155.csv'

    >>> response = requests.get(url)

    >>> response.status_code
    200

    >>> with open('data.csv', 'w') as f:
    ...     f.write(response.text)
    ...

.. hint::
    Usamos ``response.text`` para obtener el contenido ya que nos interesa en formato "unicode".

Podemos comprobar que el fichero se ha creado satisfactoriamente:

.. code-block:: console

    $ file data.csv
    plain_text.csv: UTF-8 Unicode text, with CRLF line terminators

Ficheros binarios
=================

Para descargar ficheros binarios seguimos la misma estructura que para ficheros en texto plano, pero indicando el tipo binario a la hora de escribir en disco::

    >>> url = 'https://www.ine.es/jaxi/files/tpx/es/xlsx/50155.xlsx'

    >>> response = requests.get(url)

    >>> response.status_code
    200

    >>> with open('data.xlsx', 'wb') as f:
    ...     f.write(response.content)
    ...

.. hint::
    Usamos ``response.content`` para obtener el contenido ya que nos interesa en formato "bytes".

Podemos comprobar que el fichero se ha creado satisfactoriamente:

.. code-block:: console

    $ file data.xlsx
    data.xlsx: Microsoft OOXML

Nombre de fichero
=================

En los ejemplos anteriores hemos puesto el nombre de fichero "a mano". Pero podría darse la situación de necesitar el nombre de fichero que descargamos. Para ello existen dos aproximaciones en función de si aparece o no la clave "attachment" en las cabeceras de respuesta.

Podemos escribir la siguiente función para ello::

    >>> def get_filename(response):
    ...     try:
    ...         return response.headers['Content-Disposition'].split(';')[1].split('=')[1]
    ...     except (KeyError, IndexError):
    ...         return response.url.split('/')[-1]
    ...

Caso para el que no disponemos de la cabecera adecuada::

    >>> url = 'https://media.readthedocs.org/pdf/pytest/latest/pytest.pdf'
    >>> response = requests.get(url)
    >>> 'attachment' in response.headers.get('Content-Disposition')
    False

    >>> get_filename(response)
    'pytest.pdf'

Caso para el que sí disponemos de la cabecera adecuada::

    >>> url = 'https://www.ine.es/jaxi/files/tpx/es/csv_bdsc/45070.csv'
    >>> response = requests.get(url)
    >>> 'attachment' in response.headers.get('Content-Disposition')
    True

    >>> get_filename(response)
    '45070.csv'



.. --------------- Footnotes ---------------

.. [#plane-unsplash] Foto original de portada por `Frame Harirak`_ en Unsplash.
.. [#http-methods] Métodos de `petición HTTP`_.
.. [#inspect-tools] Herramientas para desarrolladores en el navegador. Por ejemplo `Chrome Dev Tools`_.
.. [#http-headers] Las `cabeceras HTTP`_ permiten al cliente y al servidor enviar información adicional junto a una petición o respuesta.
.. [#user-agent] El `agente de usuario`_ del navegador permite que el servidor identifique el sistema operativo y las características del navegador.
.. [#http-cookies] Una `cookie HTTP`_ es una pequeña pieza de datos que un servidor envía al navegador web del usuario.

.. --------------- Hyperlinks ---------------

.. _Frame Harirak: https://unsplash.com/@framemily?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
.. _petición HTTP: https://developer.mozilla.org/es/docs/Web/HTTP/Methods
.. _Chrome Dev Tools: https://developer.chrome.com/docs/devtools/
.. _cabeceras HTTP: https://developer.mozilla.org/es/docs/Web/HTTP/Headers
.. _agente de usuario: https://developer.mozilla.org/es/docs/Web/HTTP/Headers/User-Agent
.. _JSON: https://developer.mozilla.org/es/docs/Learn/JavaScript/Objects/JSON
.. _Santa Cruz de Tenerife: https://es.wikipedia.org/wiki/Santa_Cruz_de_Tenerife
.. _cookie HTTP: https://developer.mozilla.org/es/docs/Web/HTTP/Cookies
