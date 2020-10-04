***********************
Hablando con la máquina
***********************

.. image:: img/garett-mizunaka-xFjti9rYILo-unsplash.jpg

Los ordenadores son dispositivos complejos pero están diseñados para hacer una cosa bien: **ejecutar aquello que se les indica**. La cuestión es cómo indicar a un ordenador lo que queremos que ejecute. Esas indicaciones se llaman técnicamente **instrucciones** y se expresan en un lenguaje. Podríamos decir que **programar** consiste en escribir instrucciones para que sean ejecutadas por un ordenador. El lenguaje que utilizamos para ello se denomina **lenguaje de programación**. [#machine-unsplash]_

Código máquina
==============

Pero aún seguimos con el problema de cómo hacer que un ordenador (o máquina) entienda el lenguaje de programación. A priori podríamos decir que un ordenador sólo entiende un lenguaje muy "simple" denominado `código máquina <https://es.wikipedia.org/wiki/Lenguaje_de_m%C3%A1quina>`__. En este lenguaje se utilizan únicamente los símbolos **0** y **1** en representación de los *niveles de tensión* alto y bajo, que al fin y al cabo, son los estados que puede manejar un circuito digital. Hablamos de `sistema binario`_. Si tuviéramos que escribir programas de ordenador en este formato sería una tarea ardua, pero afortunadamente se han ido creando con el tiempo lenguajes de programación intermedios que, posteriormente, son convertidos a código máquina.

Si intentamos visualizar un programa en código máquina, únicamente obtendríamos una secuencia de ceros y unos:

.. code-block:: raw

    00001000 00000010 01111011 10101100 10010111 11011001 01000000 01100010 
    00110100 00010111 01101111 10111001 01010110 00110001 00101010 00011111 
    10000011 11001101 11110101 01001110 01010010 10100001 01101010 00001111 
    11101010 00100111 11000100 01110101 11011011 00010110 10011111 01010110 

Ensamblador
===========

El primer lenguaje de programación que encontramos en esta "escalada" es **ensamblador**. Veamos un `ejemplo de código en ensamblador`_ del típico programa que se escribe por primera vez, el *"Hello, World"*:

.. code-block:: Nasm

             global    _start

             section   .text
    _start:  mov       rax, 1              ; system call for write
             mov       rdi, 1              ; file handle 1 is stdout
             mov       rsi, message        ; address of string to output
             mov       rdx, 13             ; number of bytes
             syscall                       ; invoke OS to do the write
             mov       rax, 60             ; system call for exit
             xor       rdi, rdi            ; exit code 0
             syscall                       ; invoke OS to exit

             section   .data
    message: db        "Hello, World", 10  ; note the newline at the end

Aunque resulte difícil de creer, lo "único" que hace este programa es mostrar en la pantalla de nuestro ordenador la frase "Hello, World", pero además teniendo en cuenta que sólo funcionará para una `arquitectura x86`_.

C
=

Aunque el lenguaje ensamblador nos facilita un poco la tarea de desarrollar programas, sigue siendo bastante complicado ya que las instrucciones son muy específicas y no proporcionan una semántica entendible. Uno de los lenguajes que vino a suplir -- en parte -- estos obstáculos fue `C <https://es.wikipedia.org/wiki/C_(lenguaje_de_programaci%C3%B3n)>`__. Considerado para muchas personas como un referente en cuanto a los lenguajes de programación, permite hacer uso de instrucciones más claras y potentes. El mismo ejemplo anterior del programa *"Hello, World"* se escribiría así en lenguaje *C*:

.. code-block:: C

    #include <stdio.h>

    int main() {
        printf("Hello, World");
        return 0;
    }

Python
======

Si seguimos "subiendo" en esta lista de lenguajes de programación, podemos llegar hasta `Python <https://es.wikipedia.org/wiki/Python>`__. Se dice que es un lenguaje de *más alto nivel* en el sentido de que sus instrucciones son más entendibles por un humano. Veamos cómo se escribiría el programa *"Hello, World"* en el lenguaje de programación Python::

    print('Hello, World')

¡Pues así de fácil! Hemos pasado de *código máquina* (ceros y unos) a *código Python* en el que se puede entender perfectamente lo que estamos indicando al ordenador. La pregunta que surge es: ¿cómo entiende una máquina lo que tiene que hacer si le pasamos un programa hecho en Python (o cualquier otro lenguaje de alto nivel)? La respuesta es un **compilador**.

Compiladores
============

Los `compiladores <https://es.wikipedia.org/wiki/Compilador>`__ son programas que convierten un lenguaje "cualquiera" en *código máquina*. Se pueden ver como traductores, permitiendo a la máquina interpretar lo que queremos hacer.

.. figure:: img/compiler.png

    Esquema de funcionamiento de un compilador [#compiler]_

.. note::

    Para ser más exactos, en Python hablamos de un **intérprete** en vez de un compilador, pero a los efectos es prácticamente lo mismo. La diferencia está en que el intérprete realiza la "compilación" (*interpretación*) y la "ejecución" de una vez, mientras que el compilador genera un formato "ejecutable" (*código objeto*) que se ejecuta en otra fase posterior.



.. --------------- Footnotes ---------------

.. [#machine-unsplash] Foto original por `Garett Mizunaka`_ en Unsplash.
.. [#compiler] Iconos originales por `Flaticon`_.

.. --------------- Hyperlinks ---------------

.. _Flaticon: http://flaticon.com/
.. _Garett Mizunaka: https://unsplash.com/@garett3?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
.. _arquitectura x86: https://es.wikipedia.org/wiki/X86
.. _ejemplo de código en ensamblador: https://cs.lmu.edu/~ray/notes/x86assembly/
.. _sistema binario: https://es.wikipedia.org/wiki/Sistema_binario
