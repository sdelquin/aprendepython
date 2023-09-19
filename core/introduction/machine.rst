#######################
Hablando con la máquina
#######################

.. image:: img/garett-mizunaka-xFjti9rYILo-unsplash.jpg

Los ordenadores son dispositivos complejos pero están diseñados para hacer una cosa bien: **ejecutar aquello que se les indica**. La cuestión es cómo indicar a un ordenador lo que queremos que ejecute. Esas indicaciones se llaman técnicamente **instrucciones** y se expresan en un lenguaje. Podríamos decir que **programar** consiste en escribir instrucciones para que sean ejecutadas por un ordenador. El lenguaje que utilizamos para ello se denomina **lenguaje de programación**. [#machine-unsplash]_

**************
Código máquina
**************

Pero aún seguimos con el problema de cómo hacer que un ordenador (o máquina) entienda el lenguaje de programación. A priori podríamos decir que un ordenador sólo entiende un lenguaje muy "simple" denominado `código máquina <https://es.wikipedia.org/wiki/Lenguaje_de_m%C3%A1quina>`__. En este lenguaje se utilizan únicamente los símbolos **0** y **1** en representación de los *niveles de tensión* alto y bajo, que al fin y al cabo, son los estados que puede manejar un circuito digital. Hablamos de `sistema binario`_. Si tuviéramos que escribir programas de ordenador en este formato sería una tarea ardua, pero afortunadamente se han ido creando con el tiempo lenguajes de programación intermedios que, posteriormente, son convertidos a código máquina.

Si intentamos visualizar un programa en código máquina, únicamente obtendríamos una secuencia de ceros y unos:

.. code-block::

    00001000 00000010 01111011 10101100 10010111 11011001 01000000 01100010 
    00110100 00010111 01101111 10111001 01010110 00110001 00101010 00011111 
    10000011 11001101 11110101 01001110 01010010 10100001 01101010 00001111 
    11101010 00100111 11000100 01110101 11011011 00010110 10011111 01010110 

***********
Ensamblador
***********

El primer lenguaje de programación que encontramos en esta "escalada" es **ensamblador**. Veamos un `ejemplo de código en ensamblador`_ del típico programa que se escribe por primera vez, el *"Hello, World"*:

.. code-block:: Nasm

    SYS_SALIDA equ 1

    section .data
        msg db "Hello, World",0x0a
        len equ $ - msg ;longitud de msg

    section .text
    global _start ;para el linker
    _start: ;marca la entrada
        mov eax, 4 ;llamada al sistema (sys_write)
        mov ebx, 1 ;descripción de archivo (stdout)
        mov ecx, msg ;msg a escribir
        mov edx, len ;longitud del mensaje
        int 0x80 ;llama al sistema de interrupciones

    fin: mov eax, SYS_SALIDA ;llamada al sistema (sys_exit)
        int 0x80

Aunque resulte difícil de creer, lo "único" que hace este programa es mostrar en la pantalla de nuestro ordenador la frase "Hello, World", pero además teniendo en cuenta que sólo funcionará para una `arquitectura x86`_.

******
C
******

Aunque el lenguaje ensamblador nos facilita un poco la tarea de desarrollar programas, sigue siendo bastante complicado ya que las instrucciones son muy específicas y no proporcionan una semántica entendible. Uno de los lenguajes que vino a suplir -- en parte -- estos obstáculos fue `C <https://es.wikipedia.org/wiki/C_(lenguaje_de_programaci%C3%B3n)>`__. Considerado para muchas personas como un referente en cuanto a los lenguajes de programación, permite hacer uso de instrucciones más claras y potentes. El mismo ejemplo anterior del programa *"Hello, World"* se escribiría así en lenguaje *C*:

.. code-block:: C

    #include <stdio.h>

    int main() {
        printf("Hello, World");
        return 0;
    }

******
Python
******

Si seguimos "subiendo" en esta lista de lenguajes de programación, podemos llegar hasta `Python <https://es.wikipedia.org/wiki/Python>`__. Se dice que es un lenguaje de *más alto nivel* en el sentido de que sus instrucciones son más entendibles por un humano. Veamos cómo se escribiría el programa *"Hello, World"* en el lenguaje de programación Python::

    print('Hello, World')

¡Pues así de fácil! Hemos pasado de *código máquina* (ceros y unos) a *código Python* en el que se puede entender perfectamente lo que estamos indicando al ordenador. La pregunta que surge es: ¿cómo entiende una máquina lo que tiene que hacer si le pasamos un programa hecho en Python (o cualquier otro lenguaje de alto nivel)? La respuesta es un **compilador**.

************
Compiladores
************

Los `compiladores <https://es.wikipedia.org/wiki/Compilador>`__ son programas que convierten un lenguaje "cualquiera" en *código máquina*. Se pueden ver como traductores, permitiendo a la máquina interpretar lo que queremos hacer.

.. figure:: img/compiler.jpg
    :align: center

    Esquema de funcionamiento de un compilador [#compiler]_

En el caso particular de Python el proceso de compilación genera un código intermedio denominado **bytecode**.

Si partimos del ejemplo anterior::

    print('Hello, World')

el programa se compilaría [#bytecode]_ al siguiente "bytecode"::

      0           0 RESUME                   0

      1           2 PUSH_NULL
                  4 LOAD_NAME                0 (print)
                  6 LOAD_CONST               0 ('Hello, World')
                  8 PRECALL                  1
                 12 CALL                     1
                 22 RETURN_VALUE

A continuación estas instrucciones básicas son ejecutadas por el intérprete de "bytecode" de Python (o máquina virtual):

.. figure:: img/python-execution.png
    :align: center

    Modelo de ejecución de un programa Python [#bytecode_analysis]_

.. note::
    Si queremos ver una diferencia entre un lenguaje compilado como C y un lenguaje "interpretado" como Python es que, aunque ambos realizan un proceso de traducción del código fuente, la compilación de C genera un código objeto que debe ser ejecutado en una segunda fase explícita, mientras que la compilación de Python genera un "bytecode" que se ejecuta (interpreta) de forma "transparente".

.. --------------- Footnotes ---------------

.. [#machine-unsplash] Foto original por `Garett Mizunaka`_ en Unsplash.
.. [#compiler] Iconos originales por `Flaticon`_.
.. [#bytecode] Véase más información sobre `el intérprete de bytecode`_.
.. [#bytecode_analysis] Imagen extraída del artículo `Python bytecode analysis`_.

.. --------------- Hyperlinks ---------------

.. _Flaticon: http://flaticon.com/
.. _Garett Mizunaka: https://unsplash.com/@garett3?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
.. _arquitectura x86: https://es.wikipedia.org/wiki/X86
.. _ejemplo de código en ensamblador: https://medium.com/nabucodonosor-editorial/hola-mundo-ensamblado-x86-ff62789ab9b0
.. _sistema binario: https://es.wikipedia.org/wiki/Sistema_binario
.. _el intérprete de bytecode: https://devguide.python.org/internals/interpreter/
.. _Python bytecode analysis: https://nowave.it/python-bytecode-analysis-1.html
