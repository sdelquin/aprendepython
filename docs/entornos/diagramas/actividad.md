---
icon: material/arrow-decision-outline
tags:
  - Entornos de desarrollo
  - Diagramas
  - Diagrama de actividad
---

# Diagrama de actividad

Un **diagrama de actividad** es un diagrama [UML](https://www.ibm.com/docs/es/iis/11.5.0?topic=types-unified-modeling-language-uml-model) (Lenguaje Unificado de Modelado) que representa el **flujo de trabajo de un proceso**, mostrando las actividades que se realizan, el orden en que se ejecutan y las decisiones que pueden modificar el recorrido.

Se utiliza para describir el comportamiento de un sistema mediante una secuencia de acciones, desde un punto de inicio hasta uno o varios puntos de finalización. Es especialmente útil para representar procesos de negocio, algoritmos y flujos de trabajo de una aplicación.

A diferencia del [diagrama de secuencia](secuencia.md), que se centra en los mensajes intercambiados entre participantes a lo largo del tiempo, el diagrama de actividad se centra en las **acciones que componen un proceso** y el flujo que las conecta.

## Elementos

A continuación se detallan los principales elementos que forman parte de un diagrama de actividad:

| Elemento | Finalidad |
|---|---|
| **Nodo inicial** | Indica el punto de comienzo del flujo de actividades y se representa mediante un círculo negro. |
| **Actividades o acciones** | Representan las tareas o pasos que se ejecutan durante un proceso y se dibujan mediante rectángulos con las esquinas redondeadas. |
| **Flujos de control** | Representan el orden de ejecución de las actividades mediante flechas que conectan los distintos elementos. |
| **Nodos de decisión** | Permiten elegir entre diferentes caminos del flujo en función de una condición y se representan mediante un rombo. |
| **Nodos de fusión** | Unifican diferentes caminos alternativos del flujo en uno solo y se representan mediante un rombo. |
| **Nodos de bifurcación y unión** | Permiten dividir el flujo en actividades paralelas y sincronizar su finalización, respectivamente, y se representan mediante una barra gruesa. |
| **Nodo final de actividad** | Indica la finalización completa de la actividad y se representa mediante un círculo negro rodeado por otro círculo. |
| **Carriles («swimlanes»)** | Organizan las actividades en regiones que indican qué actor, persona o componente es responsable de ejecutarlas. |

## Ejemplo

A continuación se presenta un <span class="example">ejemplo:material-flash:</span> de **diagrama de casos de uso** para un _Sistema de gestión de una biblioteca_:

![Ejemplo diagrama de actividad](./images/actividad/example.svg)

??? success "Código PlantUML"

    [PlantUML](https://plantuml.com/) es un sabor («flavour») de UML para diseñar diagramas mediante código. Su herramienta _online_ [PlantText](https://www.planttext.com/) permite crear y editar los ficheros (diagramas) directamente en el navegador.

    A continuación se muestra el código que ha permitido generar el [diagrama de actividad](https://plantuml.com/es/activity-diagram-beta) del ejemplo anterior:

    ```linenums="1"
    @startuml

    title Solicitar un préstamo en una biblioteca

    |Usuario|
    start
    :Solicitar un préstamo de un libro;
    |Sistema|
    :Buscar libro en el catálogo;
    :Comprobar disponibilidad;
    |Servicio de préstamos|
    :Consultar disponibilidad del libro;
    |Sistema|
    if (¿Libro disponible?) then (No)
    |Usuario|
    :Mostrar mensaje de no disponible;
    :Ver mensaje informativo;
    :Ver confirmación del préstamo;
    else (Sí)
    |Sistema|
    :Registrar préstamo;
    |Servicio de préstamos|
    :Guardar préstamo en la base de datos;
    |Sistema|
    :Actualizar disponibilidad del libro;
    :Mostrar confirmación del préstamo;
    endif
    stop

    @enduml
    ```
