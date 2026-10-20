---
icon: material/code-array
tags:
  - Entornos de desarrollo
  - Diagramas
  - Diagrama de clases
---

# Diagrama de clases

Un **diagrama de clases** es un diagrama [UML](https://www.ibm.com/docs/es/iis/11.5.0?topic=types-unified-modeling-language-uml-model) (Lenguaje Unificado de Modelado) que representa la **estructura estática de un sistema**. Permite identificar las clases que lo componen, sus atributos, sus métodos y las relaciones que existen entre ellas.

Se utiliza principalmente durante el diseño de software orientado a objetos para representar cómo se organiza un sistema antes de implementarlo mediante código.

## Elementos

A continuación se detallan los principales elementos que forman parte de un diagrama de clases:

| Elemento | Finalidad |
| --- | --- |
| **Clases** | Representan los elementos del sistema y se dibujan mediante rectángulos que contienen su nombre, atributos y métodos. |
| **Atributos** | Representan las propiedades o los datos de una clase y se definen mediante su nombre, tipo y visibilidad. |
| **Métodos u operaciones** | Representan los comportamientos de una clase e indican las operaciones que pueden realizar sus objetos. |
| **Relaciones entre clases** | Representan las conexiones entre las clases mediante asociaciones, herencia, agregaciones, composiciones o dependencias. |
| **Multiplicidad o cardinalidad** | Indica cuántos objetos de una clase pueden relacionarse con un objeto de otra clase. |
| **Visibilidad** | Indica desde dónde pueden accederse los atributos y métodos mediante los símbolos público (`+`), privado (`-`), protegido (`#`) y de paquete (`~`). |

## Ejemplo

A continuación se presenta un <span class="example">ejemplo:material-flash:</span> de **diagrama de clases** para un _Sistema de gestión de una biblioteca_:

![Ejemplo diagrama de clases](./images/clases/example.svg)

??? success "Código PlantUML"

    [PlantUML](https://plantuml.com/) es un sabor («flavour») de UML para diseñar diagramas mediante código. Su herramienta _online_ [PlantText](https://www.planttext.com/) permite crear y editar los ficheros (diagramas) directamente en el navegador.

    A continuación se muestra el código que ha permitido generar el [diagrama de clases](https://plantuml.com/es/class-diagram) del ejemplo anterior:

    ```linenums="1"
    @startuml

    hide empty members

    title Sistema de gestión de una biblioteca

    class Usuario {
    -id: int
    -nombre: str
    -email: str
    +solicitarLibro()
    +devolverLibro()
    +consultarPrestamos()
    }

    class Prestamo {
    -id: int
    -fechaPrestamo: date
    -fechaDevolucion: date
    -EstadoPrestamo: estado
    +cerrar()
    +bool estaVencido()
    }

    class Libro {
    -id: int
    -titulo: str
    -autor: str
    -isbn: str
    -disponible: bool
    +prestar()
    +devolver()
    +bool esDisponible()
    }

    class Bibliotecario {
    -numeroEmpleado: str
    +registrarLibro()
    +gestionarUsuarios()
    }

    class Lector {
    -numeroCarnet: str
    +reservarLibro()
    }

    class Ejemplar {
    -id: int
    -codigo: str
    -estado: EstadoEjemplar
    +marcarComoPrestado()
    +marcarComoDisponible()
    }

    enum EstadoPrestamo {
    -ACTIVO
    -DEVUELTO
    -VENCIDO
    }

    enum EstadoEjemplar {
    -DISPONIBLE
    -PRESTADO
    -RESERVADO
    -BAJA
    }

    Usuario "1" -- "0..*" Prestamo : realiza
    Prestamo "0..*" -- "1" Libro : corresponde a
    Bibliotecario --|> Usuario
    Lector --|> Usuario
    Libro *-- Ejemplar

    @enduml
    ```
