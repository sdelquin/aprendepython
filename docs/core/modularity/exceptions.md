---
icon: octicons/bug-24
---

# Excepciones { #exceptions }

![Fork](images/exceptions/icecream.jpg)
(1)
{ .annotate }

1. :fontawesome-regular-copyright: [Sarah Kilian](https://unsplash.com/@rojekilian) :material-at: [Unsplash](https://unsplash.com) 

En programación, una excepción es un **evento anómalo o inesperado** que ocurre durante la ejecución de un programa y que **interrumpe su flujo normal**. Generalmente, las excepciones indican errores o situaciones inusuales, como intentos de dividir por cero, acceso a índices fuera de rango o fallos al abrir un archivo inexistente.

## Manejando errores { #handling-errors }

Si una excepción ocurre en algún lugar de nuestro programa y no es capturada en ese punto, va subiendo (burbujeando) hasta que es capturada en alguna función que ha hecho la llamada.

Si en toda la «pila» de llamadas no existe un control de la excepción, Python terminará abortando la ejecución del programa y mostrando un mensaje de error con información adicional:

<div class="grid cards" markdown>

-   
    ```pycon hl_lines="11-20"
    >>> def f3():
    ...     return 1/0
    ...
    >>> def f2():
    ...     return f3()
    ...
    >>> def f1():
    ...     return f2()
    ...
    >>> f1()
    Traceback (most recent call last):
      Cell In[4], line 1
        f1()
      Cell In[3], line 2 in f1
        return f2()
      Cell In[2], line 2 in f2
        return f3()
      Cell In[1], line 2 in f3
        return 1/0
    ZeroDivisionError: division by zero
    ```
  
  -   

      ``` mermaid
      graph
      start[[Start]] --> f1
      f1 --> f2
      f2 --> f3
      f3 -->|1/0| err{{ZeroDivisionError}}
      err -->|Traceback| start
      ```

</div>

Para manejar (capturar) las excepciones podemos usar un bloque de código con las sentencias `#!python try` + `#!python except`.

Supongamos el siguiente <span class="example">ejemplo:material-flash:</span> en el cual queremos controlar una posible división por cero:

```pycon
>>> def intdiv(a: int, b: int) -> int:
...     try:#(1)!
...         return a // b
...     except:#(2)!
...         print('Please do not divide by zero...')
...

>>> intdiv(3, 0)
Please do not divide by zero...
```
{ .annotate }

1. En el bloque `#!python try` irá el código susceptible de generar errores.
2. En el bloque `#!python except` irá el código a ejecutar cuando se produce un error.

!!! tip "Especificar la excepción"

    No es una buena práctica usar un bloque `#!python except` sin indicar el tipo de excepción que estamos gestionando, no sólo porque puedan existir varias excepciones que capturar sino porque, como dice el Zen de Python: «explícito» es mejor que «implícito».

### Especificando excepciones { #specify-exceptions }

En el siguiente <span class="example">ejemplo:material-flash:</span> mejoraremos el código anterior, capturando distintos tipos de [excepciones predefinidas](https://docs.python.org/es/3/library/exceptions.html#concrete-exceptions):

- [x] `TypeError` por si los operandos no permiten la división.
- [x] `ZeroDivisionError` por si el denominador es cero.
- [x] `Exception` para cualquier otro error que se pueda producir.

Veamos su implementación:

```pycon
>>> def intdiv(a, b):
...     try:
...         result = a // b
...     except TypeError:
...         print('Check operands. Some of them seems strange...')
...     except ZeroDivisionError:
...         print('Please do not divide by zero...')
...     except Exception:
...         print('Ups. Something went wrong...')
...

>>> intdiv(3, 0)
Please do not divide by zero...

>>> intdiv(3, '0')
Check operands. Some of them seems strange...
```

#### Excepciones predefinidas { #builtin-exceptions }

Las [excepciones predefinidas](https://docs.python.org/es/3/library/exceptions.html#concrete-exceptions) en Python cubren un amplio rango de posibilidades y no hace falta importarlas previamente. Se pueden usar directamente.

Conocerlas es importante ya que nos permitirá gestionar mejor los posibles errores y dar respuesta a situaciones inesperadas. Veamos a continuación algunas de las más relevantes:

| Excepción | Significado | Ejemplo |
| --- | --- | --- |
| `AttributeError` | Referencia a atributo/método inexistente | `#!python 'hello'.splik()` |
| `IndexError` | Subíndice de secuencia fuera de rango | `#!python (2, 3)[5]` |
| `KeyError` | Clave de diccionario no encontrada | `#!python {'x': 1, 'y': 2}['z']` |
| `TypeError` | Operación sobre un objeto de tipo inapropiado | `#!python 'x' / 3` |
| `ValueError` | Operación sobre un objeto de tipo correcto pero valor inapropiado | `#!python int('x')` |
| `ZeroDivisionError` | Segundo argumento de división o módulo es cero | `#!python 1 / 0` |
| `FileNotFoundError` | Error al abrir (modo lectura) un fichero que no existe | `#!python open('data.txt')` |
| `RecursionError` | Alcanzado el máximo nivel de recursión | `#!python while True:` |
| `StopIteration` | Fin del protocolo de iteración | `#!python for item in items:` |
| `NotImplementedError` | La operación debe ser implementada | `#!python def method(self):` |

#### Agrupando excepciones { #group-exceptions }

Si nos interesa tratar distintas excepciones con el mismo comportamiento, es posible agruparlas en una única línea:

```pycon hl_lines="4"
>>> def intdiv(a, b):
...     try:
...         result = a // b
...     except (TypeError, ZeroDivisionError):
...         print('Check operands: Some of them caused errors...')
...     except Exception:
...         print('Ups. Something went wrong...')
...

>>> intdiv(3, 0)
Check operands: Some of them caused errors...
```

### Cláusulas adicionales { #additional-clauses }

Existen dos cláusulas adicionales que Python proporciona para el bloque `try-except`:

- `#!python else`: Se ejecuta cuando no ha habido ningún error en el bloque de código definido por `#!python try`
- `#!python finally`: Se ejecuta siempre, independientemente de si ha habido algún error o no.

Veamos un <span class="example">ejemplo:material-flash:</span> de aplicación de ambas cláusulas en el acceso a una lista:

=== "Con error"

    ```pycon hl_lines="6 10"
    >>> values = [4, 2, 7]

    >>> try:
    ...     r = values[3]
    ... except IndexError:
    ...     print('Error: Index not in list')
    ... else:
    ...     print(f'Your wishes are my command: {r}')
    ... finally:
    ...     print('Have a good day!')
    ...
    Error: Index not in list
    Have a good day!
    ```

=== "Sin error"

    ```pycon hl_lines="8 10"
    >>> values = [4, 2, 7]

    >>> try:
    ...     r = values[2]
    ... except IndexError:
    ...     print('Error: Index not in list')
    ... else:
    ...     print(f'Your wishes are my command: {r}')
    ... finally:
    ...     print('Have a good day!')
    ...
    Your wishes are my command: 7
    Have a good day!
    ```
    
!!! exercise "Ejercicio"

    [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `getint-iterative`

!!! exercise "Ejercicio"

    [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `getint-recursive`

### Instancias de excepción { #exception-instance }

En este punto sabemos capturar excepciones (por su naturaleza/tipo). Pero Python también permite recuperar la instancia de cada excepción capturada.

Para ello tendremos que hacer uso de la palabra reservada `#!python as` junto a un nombre de variable que contendrá el objeto de la excepción.

Lo más habitual al recuperar el objeto de error es mostrar (o manipular) los mensajes de error. Veamos un <span class="example">ejemplo:material-flash:</span> siguiendo con el acceso a una lista:

```pycon hl_lines="5"
>>> values = [4, 2, 7]

>>> try:
...     print(values[3])
... except IndexError as err:
...     print(f'Something went wrong: {err}')#(1)!
...
Something went wrong: list index out of range
```
{ .annotate }

1. Lo que ocurre en este caso es una llamada implícita a `#!python err.__str__()` como se explicó [aquí](./oop.md#str).

### Elevando excepciones { #raise-exceptions }

Es bastante común que nuestro programa tenga que lanzar (elevar o levantar) una excepción (predefinida o propia). Para ello tendremos que hacer uso de la sentencia `#!python raise`.

Supongamos por <span class="example">ejemplo:material-flash:</span> una función que suma dos valores enteros. En el caso de que alguno de los operandos no sea entero, elevaremos una excepción indicando esta circunstancia:

```pycon hl_lines="4"
>>> def add(a: int, b: int) -> int:
...     if isinstance(a, int) and isinstance(b, int):
...         return a + b
...     raise TypeError('Operands must be integers')
...

>>> add(4, 3)#(1)!
7

>>> add('x', 'y')#(2)!
Traceback (most recent call last):
  Cell In[3], line 1
    add('x', 'y')
  Cell In[1], line 4 in add
    raise TypeError('Operands must be integers')
TypeError: Operands must be integers
```
{ .annotate }

1. Situación en la que todo va bien.
2. Situación de error debido al tipo de los argumentos.

### Jerarquía de excepciones { #exception-hierarchy }

Todas las excepciones predefinidas en Python heredan de la clase `Exception` y de la clase `BaseException` (más allá de heredar, obviamente, de `object`).

Podemos «visitar» algunas [excepciones predefinidas](#builtin-exceptions) y comprobar este comportamiento:

```pycon
>>> TypeError.mro()
[TypeError, Exception, BaseException, object]

>>> ZeroDivisionError.mro()
[ZeroDivisionError, ArithmeticError, Exception, BaseException, object]

>>> IndexError.mro()
[IndexError, LookupError, Exception, BaseException, object]

>>> FileNotFoundError.mro()
[FileNotFoundError, OSError, Exception, BaseException, object]
```

A continuación se detalla la **jerarquía completa de excepciones predefinidas** en Python:

```
BaseException
├── BaseExceptionGroup
├── GeneratorExit
├── KeyboardInterrupt
├── SystemExit
└── Exception
    ├── ArithmeticError
    │    ├── FloatingPointError
    │    ├── OverflowError
    │    └── ZeroDivisionError
    ├── AssertionError
    ├── AttributeError
    ├── BufferError
    ├── EOFError
    ├── ExceptionGroup [BaseExceptionGroup]
    ├── ImportError
    │    └── ModuleNotFoundError
    ├── LookupError
    │    ├── IndexError
    │    └── KeyError
    ├── MemoryError
    ├── NameError
    │    └── UnboundLocalError
    ├── OSError
    │    ├── BlockingIOError
    │    ├── ChildProcessError
    │    ├── ConnectionError
    │    │    ├── BrokenPipeError
    │    │    ├── ConnectionAbortedError
    │    │    ├── ConnectionRefusedError
    │    │    └── ConnectionResetError
    │    ├── FileExistsError
    │    ├── FileNotFoundError
    │    ├── InterruptedError
    │    ├── IsADirectoryError
    │    ├── NotADirectoryError
    │    ├── PermissionError
    │    ├── ProcessLookupError
    │    └── TimeoutError
    ├── ReferenceError
    ├── RuntimeError
    │    ├── NotImplementedError
    │    └── RecursionError
    ├── StopAsyncIteration
    ├── StopIteration
    ├── SyntaxError
    │    └── IndentationError
    │         └── TabError
    ├── SystemError
    ├── TypeError
    ├── ValueError
    │    └── UnicodeError
    │         ├── UnicodeDecodeError
    │         ├── UnicodeEncodeError
    │         └── UnicodeTranslateError
    └── Warning
        ├── BytesWarning
        ├── DeprecationWarning
        ├── EncodingWarning
        ├── FutureWarning
        ├── ImportWarning
        ├── PendingDeprecationWarning
        ├── ResourceWarning
        ├── RuntimeWarning
        ├── SyntaxWarning
        ├── UnicodeWarning
        └── UserWarning
```

## Excepciones propias { #custom-exceptions }

Python ofrece una gran cantidad de [excepciones predefinidas](https://docs.python.org/es/3/library/exceptions.html#concrete-exceptions). Hasta ahora hemos visto cómo gestionar y manejar este tipo de excepciones.

Pero hay ocasiones en las que nos puede interesar **crear nuestras propias excepciones**. Para ello simplemente tendremos que crear una clase que herede de `Exception` —la clase base para todas las excepciones— o de cualquier otra que cubra la necesidad demandada.

Veamos un <span class="example">ejemplo:material-flash:</span> en el que creamos una ^^excepción propia^^ para controlar que el valor dado sea un número entero:

```pycon
>>> class NotIntError(Exception):
...     pass
...
```

Ahora prepararemos una función que obtiene el siguiente valor de una serie de números enteros, pero si alguno de los valores no es entero, elevaremos la excepción propia definida previamente:

```pycon
>>> def get_next_int(*values) -> list[int]:
...     next_values = []
...     for value in values:
...         if isinstance(value, int):
...             next_values.append(value + 1)
...         else:
...             raise NotIntError(value)
...     return next_values
...
```

Probemos la implementación anterior con un par de casos:

```pycon hl_lines="10"
>>> get_next_int(1, 8, 2, 3)#(1)!
[2, 9, 3, 4]

>>> get_next_int(1, 8, 2.4, 3)
Traceback (most recent call last):
  Cell In[2], line 1
    get_next_int(1, 8, 2.4, 3)
  Cell In[1], line 7 in get_next_int
    raise NotIntError(value)
NotIntError: 2.4
```
{ .annotate }

1. Situación en la que todo va bien.
2. Situación de error debido al tipo de los argumentos.

### Personalizar la excepción { #customize-exception }

La excepción propia no deja de ser una clase «ordinaria» escrita en Python que podemos personalizar según necesidad.

Veamos a continuación varios <span class="example">ejemplos:material-flash:</span> de personalización:

=== "Mensaje por defecto"

    ```pycon hl_lines="10 16"
    >>> class NotIntError(Exception):
    ...     def __init__(self, message='This module only works with integers'):
    ...         super().__init__(message)
    ...

    >>> raise NotIntError()#(1)!
    Traceback (most recent call last):
      Cell In[1], line 1
        raise NotIntError()
    NotIntError: This module only works with integers
    
    >>> raise NotIntError(2.4)#(2)!
    Traceback (most recent call last):
      Cell In[1], line 1
        raise NotIntError(2.4)
    NotIntError: 2.4    
    ```
    { .annotate }
    
    1. Si no se aporta un mensaje, la excepción mostrará uno predefinido.
    2. Si se aporta un mensaje, la excepción lo mostrará.

=== "Creación de atributos"

    ```pycon
    >>> class NotIntError(Exception):
    ...     def __init__(self, value):
    ...         super().__init__(value)
    ...         self.value = value#(1)!
    ...
    
    >>> try:
    ...     raise NotIntError(2.4)
    ... except NotIntError as err:
    ...     print(err.value)#(2)!
    ...
    2.4
    ```
    { .annotate }
    
    1. Creamos un atributo en la propia excepción para almacenar el valor «molesto».
    2. Una vez capturada la excepción, podemos acceder a dicho valor (para cualquier otro procesamiento posterior).

=== "Creación de métodos"

    ```pycon
    >>> class NotIntError(Exception):
    ...     def notify(self):#(1)!
    ...         print('Notifying admin...')
    ...         telegram.send('admin@example.com', 'NotIntError raised at your codebase')
    ...

    >>> try:
    ...     raise NotIntError(2.4)
    ... except NotIntError as err:
    ...     err.notify()#(2)!
    ...
    Notifying admin...
    ```
    { .annotate }
    
    1. Creamos un método que permite notificar al administrador de que se ha lanzado una excepción de este tipo.
    2. Realizamos la notificación del error una vez capturada la excepción.

## Aserciones { #asserts }

Si hablamos de control de errores hay que citar una sentencia en Python denominada `#!python assert`. Esta sentencia nos permite comprobar si se están cumpliendo las «expectativas» de nuestro programa, y en caso contrario, lanza una excepción informativa.

Su sintaxis es muy simple. Únicamente tendremos que indicar una expresión de comparación después de la sentencia:

```pycon
>>> result = 1
>>> assert result > 0#(1)!

>>> result = -1
>>> assert result > 0#(2)!
Traceback (most recent call last):
  Cell In[4], line 1
    assert result > 0
AssertionError
```
{ .annotate }

1. Si la condición se cumple no obtendremos ninguna salida.
2. Si la condición no se cumple se lanza una excepción de tipo `AssertionError`.

Es posible añadir un **mensaje informativo** a la excepción:

```pycon
>>> result = -1
>>> assert result > 0, 'Result must be positive'
Traceback (most recent call last):
  Cell In[2], line 1
    assert result > 0, 'Result must be positive'
AssertionError: Result must be positive
```

## Ejercicios { #exercises }

1. [pypas](https://pypas.es) &nbsp;:fontawesome-solid-hand-holding-heart:{ .slide } `poker-card`
