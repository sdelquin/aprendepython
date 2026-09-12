---
icon: octicons/cpu-24
tags:
  - Entornos de desarrollo
  - Desarrollo de software
  - Hablando con la máquina
---

# Hablando con la máquina { #talking-to-machine }

![Banner](images/machine/banner.jpg)
/// caption
Imagen generada con Inteligencia Artificial
///

Los ordenadores son dispositivos complejos pero están diseñados para hacer una cosa bien: **ejecutar aquello que se les indica**. La cuestión radica en cómo indicarle a una máquina lo que queremos que haga. Esas indicaciones se llaman técnicamente **instrucciones** y se expresan en un **lenguaje**. Podríamos decir que _programar consiste en escribir instrucciones para que sean ejecutadas por un ordenador_. El lenguaje que utilizamos para ello se denomina _lenguaje de programación_.

## Código máquina { #machine-code }

Pero aún no hemos resuelto el problema de cómo hacer que un ordenador (o máquina) entienda un lenguaje de programación. A priori se podría decir que un ordenador sólo entiende un lenguaje muy «simple» denominado [código máquina](https://es.wikipedia.org/wiki/Lenguaje_de_m%C3%A1quina). En este lenguaje se utilizan únicamente los símbolos <span class="red">0</span> y <span class="green">1</span> en representación de los niveles de tensión alto y bajo, que al fin y al cabo, son los estados que puede manejar un [circuito digital](https://es.wikipedia.org/wiki/Circuito_digital). En este contexto, por tanto, hablamos de [sistema binario](https://es.wikipedia.org/wiki/Sistema_binario). Si tuviéramos que escribir programas de ordenador en este formato sería una tarea ardua, pero afortunadamente con el tiempo se han ido creando lenguajes de programación intermedios que, posteriormente, son convertidos a código máquina.

Si intentamos visualizar un programa en código máquina, únicamente obtendríamos una secuencia de ceros y unos:

```
00001000 00000010 01111011 10101100 10010111 11011001 01000000 01100010
00110100 00010111 01101111 10111001 01010110 00110001 00101010 00011111
10000011 11001101 11110101 01001110 01010010 10100001 01101010 00001111
11101010 00100111 11000100 01110101 11011011 00010110 10011111 01010110
```

## Ensamblador { #assembly }

El primer lenguaje de programación que encontramos en esta «escalada» es **ensamblador**. Veamos a continuación un [ejemplo de código en ensamblador](https://medium.com/nabucodonosor-editorial/hola-mundo-ensamblado-x86-ff62789ab9b0) del típico programa que se escribe por primera vez, el _«Hello, World»_:

```asm
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
```

Aunque resulte difícil de creer, lo «único» que hace este programa es mostrar en la pantalla de nuestro ordenador el texto `Hello, World`.

Un detalle fundamental es que sólo funcionará para una [arquitectura x86](https://es.wikipedia.org/wiki/X86), ya que las instrucciones en ensamblador están vinculadas con el tipo de arquitectura del procesador.

## C { #c }

Aunque el lenguaje ensamblador nos facilita un poco la tarea de desarrollar programas, sigue siendo bastante complicado ya que las instrucciones son muy específicas y no proporcionan una semántica entendible. Uno de los lenguajes que vino a suplir – en parte – estos obstáculos fue [C](<https://es.wikipedia.org/wiki/C_(lenguaje_de_programaci%C3%B3n)>). Considerado para muchas personas como un referente en cuanto a los lenguajes de programación, permite hacer uso de instrucciones más claras y potentes. El mismo ejemplo anterior del programa _«Hello, World»_ se escribiría así en lenguaje C:

```c
#include <stdio.h>

int main() {
    printf("Hello, World");
    return 0;
}
```

## Python { #python }

Si seguimos «subiendo» en esta lista de lenguajes de programación, podemos llegar hasta [Python](https://es.wikipedia.org/wiki/Python). Se dice que es un lenguaje de más alto nivel en el sentido de que sus instrucciones son más entendibles por un humano. Veamos cómo se escribiría el programa _«Hello, World»_ en el lenguaje de programación Python:

```python
print('Hello, World')
```

¡Pues así de fácil! :material-robot-happy-outline:{.hl} Hemos pasado de _código máquina_ (ceros y unos) a código Python en el que se puede entender perfectamente lo que estamos indicando al ordenador. La pregunta que surge es: ¿cómo entiende una máquina lo que tiene que hacer si le pasamos un programa hecho en Python (o cualquier otro lenguaje de programación de alto nivel)? La respuesta es un **compilador**.

## Compiladores { #compilers }

Los [compiladores](https://es.wikipedia.org/wiki/Compilador) son programas que convierten un lenguaje «cualquiera» en _código máquina_. Se pueden ver como traductores, permitiendo a la máquina interpretar lo que queremos hacer.

```mermaid
sequenceDiagram
  autonumber
  actor User
  User -->> CPU: Please run: file.py
  CPU -->> User: I don't know how!
  create participant Compiler
  User ->> Compiler: Compile it!
  Compiler -->> CPU: Here you have: 10110101011
  CPU -->> User: Done!
```

### Compilación en C { #c-compilation }

En el caso particular de **C** el proceso de compilación genera un código intermedio denominado **object code**.

Si partimos del <span class="example">ejemplo:material-flash:</span> anterior:

```c title="helloworld.c"
#include <stdio.h>

int main() {
    printf("Hello, World");
    return 0;
}
```

Podemos compilarlo de la siguiente manera:

```console
$ gcc -c helloworld.c
```

??? info "gcc"

    [gcc](https://gcc.gnu.org/) es el compilador de C más utilizado. Está soportado por la [GNU](https://www.gnu.org/home.es.html) y su código es «opensource» disponible desde [este repositorio](https://github.com/gcc-mirror/gcc).

Esto genera un nuevo archivo `helloworld.o` que en mi máquina tiene la siguiente especificación:

```console
$ file helloworld.o
helloworld.o: Mach-O 64-bit object arm64
```

Podemos comprobar que el archivo «objeto» es **dependiente de la arquitectura** de la máquina. En este caso es ARM.

??? note "Arquitecturas"

    La siguiente tabla es un pequeño resumen de las arquitecturas que nos podemos encontrar hoy en día:

    | Arquitectura | Características | Uso habitual |
    |---|---|---|
    | **x86** | Arquitectura tradicional de Intel y AMD. Históricamente asociada a CISC. | PC y servidores 32 bits |
    | **x86-64 (AMD64)** | Extensión de x86 a 64 bits. | PC y servidores actuales |
    | **ARM** | Arquitectura RISC, eficiente y de bajo consumo. | Móviles, tablets, dispositivos embebidos y servidores |
    | **AArch64 (ARM64)** | Versión de ARM para 64 bits. | Smartphones, Raspberry Pi, Apple Silicon y servidores |
    | **RISC-V** | Arquitectura RISC abierta y basada en un estándar abierto. | Sistemas embebidos, investigación y dispositivos |
    | **MIPS** | Arquitectura RISC utilizada tradicionalmente en sistemas embebidos y educativos. | Sistemas embebidos y enseñanza |

Como último paso debemos utilizar un «linker» (enlazador) el cual combina los archivos de código objeto y las bibliotecas necesarias, resolviendo las referencias entre ellos para generar el archivo ejecutable final:

```console
$ gcc helloworld.o -o helloworld
$ file helloworld
helloworld: Mach-O 64-bit executable arm64
```

De nuevo el ejecutable generado es **dependiente de la arquitectura** de la máquina. Ahora sí que podemos lanzar el programa y comprobar su resultado:

```console
$ ./helloworld
Hello, World
```


### Compilación en Python { #python-compilation }

En el caso particular de **Python** el proceso de compilación genera un código intermedio denominado **bytecode**.

Si partimos del <span class="example">ejemplo:material-flash:</span> anterior:

```python title="helloworld.py"
print('Hello, World')
```

el programa se compilaría[^1] al siguiente «bytecode»:

```asm
0           0 RESUME                   0

1           2 PUSH_NULL
            4 LOAD_NAME                0 (print)
            6 LOAD_CONST               0 ('Hello, World')
            8 PRECALL                  1
           12 CALL                     1
           22 RETURN_VALUE
```

??? tip "Detalles sobre compilación"

    El programa `helloworld.py` se puede ~~compilar~~ ejecutar sencillamente con:

    ```console
    $ python helloworld.py
    ```

    Si queremos revelar el archivo «bytecode» podemos hacerlo con:

    ```console
    $ python -m py_compile helloworld.py
    __pycache__/helloworld.cpython-313.pyc
    ```

    Si queremos revelar el propio «bytecode» podemos hacerlo con:

    ```console
    $ python -m dis helloworld.py
    ```

A continuación estas instrucciones básicas son ejecutadas por el intérprete de «bytecode» de Python (o máquina virtual)[^2]:

```mermaid
graph LR
  py[.py] --> compiler[Compiler]
  subgraph interpreter[Python Interpreter]
  compiler --> bytecode[Bytecode]
  bytecode --> vm[Python VM]
  end
  vm --> exec[Code execution]
  bytecode -.-> pyc[.pyc]
```

!!! tip ".pyc"

    Los ficheros `.pyc` (del inglés «Python compiled») contienen _bytecode_ en formato binario[^3]. Son generados por el compilador de Python. Su objetivo principal es optimizar la ejecución de un programa, ya que si el código fuente no cambia, no es necesario volver a recompilar.

??? question "JVM"

    La Máquina Virtual de Java JVM es el componente encargado de ejecutar el bytecode generado al compilar un programa Java. La JVM actúa como una capa intermedia entre el programa y el sistema operativo, permitiendo que un mismo bytecode pueda ejecutarse en diferentes arquitecturas y sistemas siempre que exista una JVM compatible. Durante la ejecución, la JVM puede interpretar el bytecode o utilizar técnicas como la compilación JIT (Just-In-Time) para traducirlo a código máquina y mejorar el rendimiento.

## Compilado vs Interpretado

Si queremos ver una diferencia entre un lenguaje compilado como C y un lenguaje «interpretado» como Python es que, aunque ambos realizan un proceso de traducción del código fuente, la compilación de C genera un código objeto que debe ser ejecutado en una segunda fase explícita, mientras que la compilación de Python genera un «bytecode» que se ejecuta (interpreta) de forma «transparente».

[^1]: Consulta aquí más información sobre el [intérprete de bytecode](https://devguide.python.org/internals/interpreter/).
[^2]: Imagen basada en el artículo [Python bytecode analysis](https://nowave.it/python-bytecode-analysis-1.html).
[^3]: Es posible incluso obtener el _bytecode_ (legible) desde un fichero `.pyc`. Aquí tienes este [post](https://mathspp.com/blog/til/read-bytecode-from-a-pyc-file) donde se explica claramente.
