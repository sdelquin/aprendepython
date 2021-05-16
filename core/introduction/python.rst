######
Python
######

.. image:: img/marketa-marcellova-Bjm9JmpNfd0-unsplash.jpg

`Python <https://www.python.org/>`__ es un lenguaje de programación de :ref:`alto nivel <core/introduction/machine:Python>` creado a finales de los 80/principios de los 90 por `Guido van Rossum`_, holandés que trabajaba por aquella época en el *Centro para las Matemáticas y la Informática* de los Países Bajos. Sus instrucciones están muy cercanas al **lenguaje natural** en inglés y se hace hincapié en la **legibilidad** del código. Toma su nombre de los `Monty Python`_, grupo humorista de los 60 que gustaban mucho a Guido. Python fue creado como sucesor del lenguaje ``ABC``. [#python-unsplash]_

****************************
Características del lenguaje
****************************

A partir de su `definición de la Wikipedia <https://es.wikipedia.org/wiki/Python>`_:

* Python es un lenguaje de programación **interpretado** cuya filosofía hace hincapié en una sintaxis que favorezca un **código legible**.
* Se trata de un lenguaje de programación **multiparadigma**, ya que soporta **orientación a objetos, programación imperativa** y, en menor medida, programación funcional. Usa **tipado dinámico** y es **multiplataforma**.
* Añadiría, como característica destacada, que se trata de un lenguaje de **propósito general**.

Ventajas
========

* Libre y gratuito (OpenSource).
* Fácil de leer, parecido a pseudocódigo.
* Aprendizaje relativamente fácil y rápido: claro, intuitivo....
* Alto nivel.
* Alta Productividad: simple y rápido.
* Tiende a producir un buen código: orden, limpieza, elegancia, flexibilidad, ...
* Multiplataforma. Portable.
* Multiparadigma: programación imperativa, orientada a objetos, funcional, ...
* Interactivo, modular, dinámico.
* Librerías extensivas ("pilas incluídas").
* Gran cantidad de librerías de terceros.
* Extensible (C++, C, ...) y "embebible".
* Gran comunidad, amplio soporte.
* Interpretado.
* Fuertemente tipado, tipado dinámico.
* Hay diferentes implementaciones: CPython, PyPy, Jython, IronPython, MicroPython, ...

Desventajas
===========

* Interpretado (velocidad de ejecución, multithread vs GIL, etc.).
* Consumo de memoria.
* Errores durante la ejecución.
* Dos versiones mayores no del todo compatibles (v2 vs v3).
* Desarrollo móvil.
* Documentación a veces dispersa e incompleta.
* Varios módulos para la misma funcionalidad.
* Librerías de terceros no siempre del todo maduras.

*************
Uso de Python
*************

Al ser un lenguaje de propósito general, podemos encontrar aplicaciones prácticamente en todos los campos científico-tecnológicos:

* Análisis de datos.
* Aplicaciones de escritorio.
* Bases de datos relacionales / NoSQL
* Buenas prácticas de programación / Patrones de diseño.
* Concurrencia.
* Criptomonedas / Blockchain.
* Desarrollo de aplicaciones multimedia.
* Desarrollo de juegos.
* Desarrollo en dispositivos embebidos.
* Desarrollo móvil.
* Desarrollo web.
* DevOps / Administración de sistemas / Scripts de automatización.
* Gráficos por ordenador.
* Inteligencia artificial.
* Internet de las cosas.
* Machine Learning.
* Programación de parsers / scrapers / crawlers.
* Programación de redes.
* Propósitos educativos.
* Prototipado de software.
* Seguridad.
* Tests automatizados.

De igual modo son muchas las empresas, instituciones y organismos que utilizan Python en su día a día para mejorar sus sistemas de información. Veamos algunas de las más relevantes:

.. figure:: img/who-uses-python.png
    :align: center
    
    Grandes empresas y organismos que usan Python

Existen ránkings y estudios de mercado que sitúan a Python como uno de los lenguajes más *usados* y la vez, más *amados* dentro del mundo del desarrollo de software. En el momento de la escritura de este documento, la última actualización del `Índice TIOBE`_ es de *agosto de 2020* en la que Python ocupa el **tercer lugar de los lenguajes de programación más usados**, sólo por detrás de *C* y *Java*. Igualmente en la `encuesta a desarrolladores de Stack Overflow`_ hecha en 2020, Python ocupa el **cuarto puesto de los lenguajes de programación más usados**, sólo por detrás de *Javascript*, *HTML/CSS* y *SQL*.

******************
Python2 vs Python3
******************

En el momento de la escritura de este material, se muestra a continuación la evolución de las versiones mayores de Python a lo largo de la historia: [#python-versions]_

.. csv-table::
    :file: tables/python_versions.csv
    :widths: 15, 30
    :header-rows: 1
    :class: longtable

El cambio de **Python 2** a **Python 3** fue bastante "traumático" ya que se **perdió la compatibilidad** en muchas de las estructuras del lenguaje. Los "*core-developers*" [#core-developers]_, con *Guido van Rossum* a la cabeza, vieron la necesidad de aplicar estas modificaciones en beneficio del rendimiento y expresividad del lenguaje de programación. Este cambio implicaba que el código escrito en Python 2 no funcionaría (de manera inmediata) en Python 3.

El pasado **1 de enero de 2020** finalizó oficialmente el **soporte a la versión 2.7** del lenguaje de programación Python. Es por ello que se recomienda lo siguiente:

- Si aún desarrollas aplicaciones escritas en Python 2, deberías migrar a Python 3.
- Si vas a desarrollar una nueva aplicación, deberías hacerlo directamente en Python 3.

.. important:: Únete a **Python 3** y aprovecha todas sus ventajas.

*************
Zen de Python
*************

Existen una serie de *reglas* "filosóficas" que indican una manera de hacer y de pensar dentro del mundo **pitónico** [#pithonic]_ creadas por `Tim Peters`_, llamadas el `Zen de Python <https://www.python.org/dev/peps/pep-0020/>`__ y que se pueden aplicar incluso más allá de la programación::

    >>> import this
    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

En su `traducción de la Wikipedia <https://es.wikipedia.org/wiki/Zen_de_Python>`_:

* Bello es mejor que feo.
* Explícito es mejor que implícito.
* Simple es mejor que complejo.
* Complejo es mejor que complicado.
* Plano es mejor que anidado.
* Espaciado es mejor que denso.
* La legibilidad es importante.
* Los casos especiales no son lo suficientemente especiales como para romper las reglas.
* Sin embargo la practicidad le gana a la pureza.
* Los errores nunca deberían pasar silenciosamente.
* A menos que se silencien explícitamente.
* Frente a la ambigüedad, evitar la tentación de adivinar.
* Debería haber una, y preferiblemente solo una, manera obvia de hacerlo.
* A pesar de que esa manera no sea obvia a menos que seas Holandés.
* Ahora es mejor que nunca.
* A pesar de que nunca es muchas veces mejor que *ahora* mismo.
* Si la implementación es difícil de explicar, es una mala idea.
* Si la implementación es fácil de explicar, puede que sea una buena idea.
* Los espacios de nombres son una gran idea, ¡tengamos más de esos!



.. --------------- Footnotes ---------------

.. [#python-unsplash] Foto original por `Markéta Marcellová`_ en Unsplash.
.. [#pithonic] Dícese de algo/alguien que sigue las convenciones de Python.
.. [#python-versions] Fuente: `python.org <https://www.python.org/doc/versions/>`_.
.. [#core-developers] Término que se refiere a los/las desarrolladores/as principales del lenguaje de programación.

.. --------------- Hyperlinks ---------------

.. _Markéta Marcellová: https://unsplash.com/@ketdee?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
.. _Guido van Rossum: https://es.wikipedia.org/wiki/Guido_van_Rossum
.. _Monty Python: https://es.wikipedia.org/wiki/Monty_Python
.. _Tim Peters: https://en.wikipedia.org/wiki/Tim_Peters_(software_engineer)
.. _Índice TIOBE: https://www.tiobe.com/tiobe-index/
.. _encuesta a desarrolladores de Stack Overflow: https://insights.stackoverflow.com/survey/2020#most-popular-technologies
