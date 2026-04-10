# Changelog

Las versiones siguen [versionado semántico](https://semver.org/) (`<major>.<minor>.<patch>`).

## Version X.X.X

Publicada el DD-MM-YYYY

## Version 3.2.5

Publicada el 10-04-2026

- Estructuras de datos: Tuplas
	- Se traslada ejercicio `dec2bin` desde listas.
- Django: Puesta en marcha
	- Añade diagrama sobre contenido de carpeta `.venv`
- Django: Modelos
	- Añade nota final al revertir migraciones.

## Version 3.2.4

Publicada el 08-04-2026

- Actualiza la versión de Zensical a [0.0.32](https://github.com/zensical/zensical/releases/tag/v0.0.32).
- Corrige render de fórmulas matemáticas en anotaciones de código: [zensical/ui](https://github.com/zensical/ui/issues/93)
- Django: Interfaz administrativa
	- Corrige typo en registro de modelo.
- Django: Producción
	- Añade documentación sobre seguridad.
- Acceso a datos: sqlite
	- Mejora documentación sobre tipos de datos en SQLite.
- Modularidad: Objetos y clases
	- Aclara uso de anotaciones dentro de clase.
- Tipos de datos: Cadenas de texto
	- Añade funciones para identificar espacios.
- Modularidad: Excepciones
	- Mejora documentación.
- Django: Justfile
	- Corrige algunas recetas para Django.
- Entornos de desarrollo: Contexto real
	- Añade notas sobre instalación de uv.

## Version 3.2.3

Publicada el 22-03-2026

- Actualiza la versión de Zensical a [0.0.28](https://github.com/zensical/zensical/releases/tag/v0.0.28).
- Modularidad: Programación orientada a objetos
	- Cambia su nombre a "Objetos y clases".
- Django: API
	- Arregla acceso por `pk` en vez de `id` (donde aplique).
	- Mejora apuntes en toda la sección.
- Django: Plantillas
	- Añade pequeña sobre sobre localización de plantillas.
- Django: Puesta en marcha
	- Añade diagrama de flujo de procesos.
- Django: Desarrollo web
	- Actualiza tabla de versiones de Django.

## Version 3.2.2

Publicada el 16-03-2026

- Configuración Zensical
	- Eliminar el resaltado de búsqueda.
- Django: API
	- Corrige errores menores.
	- Añade documentación sobre error 409.
- Modularidad: Funciones
	- Corrige errores menores.
- Tipos de datos: Cadenas de texto.
	- Añade opciones de `count()`
- Django: Justfile
	- Añade instrucciones de instalación.
	- Añade receta para `dbcmd`.
- Django: Aplicaciones
	- Añade configuración de app `shared`.
- Django: Modelos
	- Añade notas sobre instalación de cliente SQLite.
	- Añade receta `just` para lanzar comando de base de datos.
	- Añade documentación sobre revertir migraciones.
- Modularidad: Programación orientada a objetos.
	- Corrige ejemplos de métodos mágicos en operadores.
	- Corrige ejemplos de gestores de contexto.
- Django: URLs
	- Corrige error ortográfico.
- Django: Formularios
	- Mejora ejemplos de formularios.
	- Añade nota sobre campos opcionales.
- Estructuras de datos: Ficheros
	- Añade notas sobre los modos de apertura extendidos.
- Django: Puesta en marcha
	- Mejora contenido del `.gitignore` para proyectos Django.

## Version 3.2.1

Publicada el 15-03-2026

- Actualiza la versión de Zensical a [0.0.27](https://github.com/zensical/zensical/releases/tag/v0.0.27).

## Version 3.2.0

Publicada el 11-03-2026

- Django: API
  - Migración de apuntes a [Django Ninja](https://django-ninja.dev/).

## Version 3.1.6

Publicada el 03-03-2026

- Introducción: Python
	- Actualiza rankings.
	- Añade fondo de pantalla personalizado sobre Zen de Python.
- Entornos de desarrollo: Contexto real
	- Corrige errores menores.
- Entornos de desarrollo: Visual Studio Code
	- Añade configuraciones vscode, ruff y ty.
- Tipos de datos: Datos
	- Añade documentación sobre precarga de datos.
- Tipos de datos: Números
	- Corrige notas sobre precedencia de operadores.

## Version 3.1.5

Publicada el 01-03-2026

Corrige ruta de _assets_ JavaScript para MathJax.

## Version 3.1.4

Publicada el 26-02-2026

- Modularidad: Funciones
  - Arregla código de algunas funciones.
- Actualiza la versión de Zensical a [0.0.24](https://github.com/zensical/zensical/releases/tag/v0.0.24).

## Version 3.1.3

Publicada el 04-02-2026

- Estructuras de datos: Ficheros
  - Añade documentación sobre `writelines()`.
  - Añade documentación sobre apertura de múltiples ficheros con contextos.
  - Añade nuevo ejercicio de ficheros `split-file`.

## Version 3.1.2

Publicada el 02-02-2026

- Actualiza la versión de Zensical a [0.0.20](https://github.com/zensical/zensical/releases/tag/v0.0.20).
- Django: Modelos
  - Añade documentación sobre `editable`
  - Añade forma correcta de comprobar la pertenencia de un valor enumerado.
- Django: API
  - Añade aclaración sobre serialización de campos `Decimal`.

## Version 3.1.1

Publicada el 26-01-2026

- Django: Modelos
  - Añade notas sobre _fixtures_.

## Version 3.1.0

Publicada el 26-01-2026

- Desechar el viejo fichero de configuración `mkdocs.yml`.
- Django: Producción
  - Añade notas sobre Django en producción.

## Version 3.0.7

Publicada el 23-01-2026

- Estructuras de datos: Diccionarios
  - Añade función `setdefault()`
- Django: Extras
  - Añade gestión de miniaturas en Sorl Thumbnail.
- Django: Estáticos
  - Añade creación de modales con Bootstrap.
- Django: Formularios
  - Nota informativa sobre accesos a campos desde constructor.
- Django: Modelos
  - Añade validación cruzada de campos de modelo.

## Version 3.0.6

Publicada el 22-01-2026

- Django: API
  - Mejora implementación de comprobación de métodos HTTP.

## Version 3.0.5

Publicada el 19-01-2026

Actualiza la versión de Zensical a [0.0.17](https://github.com/zensical/zensical/releases/tag/v0.0.17).

## Version 3.0.4

Publicada el 15-01-2026

Actualiza la versión de Zensical a [0.0.16](https://github.com/zensical/zensical/releases/tag/v0.0.16).

## Version 3.0.3

Publicada el 14-01-2026

- Django: Modelos
  - Añade otra manera de añadir objetos en muchos a muchos.
- Django: API
  - Mejora de documentación con más código y explicaciones.

## Version 3.0.2

Publicada el 12-01-2026

- Estructuras de datos: Listas
  - Añade ejercicios al principio del capítulo.
- Django: API
  - Añade nuevo contenido y corrige errores.

## Version 3.0.1

Publicada el 08-01-2026

- pypas
  - Añade documentación de nuevos comandos.

## Version 3.0.0

Publicada el 06-01-2026

- Migración de todo el sitio web a Zensical.

## Version 2.2.4

Publicada el 03-12-2025

- Django: Extras
  - Corrige configuración de Brevo.
- Configuraciones: Pretty Conf
  - Añade documentación sobre valores por defecto.
- PDF: WeasyPrint
  - Añade documentación sobre CSS.
- Django: Middleware
  - Corrige errores menores.

## Version 2.2.3

Publicada el 02-12-2025

- Django: Internacionalización
  - Añade documentación de poedit.
  - Añade receta justfile para poedit.
- Django: Extras
  - Completa documentación y corrige errores menores.
- Django: Middleware
  - Cambia ejemplo de middleware personalizado.

## Version 2.2.2

Publicada el 01-12-2025

Completa documentación de:
  - Django: Estáticos
    - Corrige errores menores.
  - Django: Plantillas
    - Corrige errores menores.
  - Django: Internacionalización
    - Traducción en URLs.
    - Etiqueta personalizada para selección de idioma.

## Version 2.2.1

Publicada el 27-11-2025

Completa documentación de:
  - Django: Modelos
    - Corrige typos.
  - Django: Extras
    - Corrige pequeños detalles en documentación.
    - Elimina indicación recurrente de activación de entorno virtual.
  - Django: Justfile
    - Añade receta para Django-RQ.
  - Estructuras de datos: Listas
    - Corrige typos.
  - Django: Interfaz administrativa
    - Corrige typos.
  - Django: Plantillas
    - Corrige typos.
  - Django: URLs
    - Corrige typos.
  - Configuraciones: Pretty Conf
    - Corrige pequeños errores.
  - PDF: Weasyprint
    - Corrige errores.
    - Mejora documentación.

## Version 2.2.0

Publicada el 25-11-2025

Completa documentación de:
  - Modularidad: Programación orientada a objetos
    - Corrige typos.
  - Modularidad: Excepciones
    - Corrige excepciones predefinidas.
  - Estructuras de datos: Listas
    - Corrige ubicación de sección de extender listas.
  - Django: Modelos
    - Corrige relaciones muchos a muchos.
  - Django: Interfaz administrativa
    - Amplía claves ajenas para admin.
  - Django: URLs
    - Completa URLs con expresiones regulares.
  - Django: Plantillas
    - Corrige etiquetas y filtros personalizados.
  - Django: Formularios
    - Corrigue validación.
  - Django: Estáticos
    - Corrige fallos menores en Bootstrap.
  - Django: Internacionalización
    - Amplía y corrige ficheros de idioma.

## Version 2.1.3

Publicada el 13-11-2025

Completa documentación de:
  - Entornos de desarrollo: Contexto real
    - Corrección sobre uv.
  - Estructuras de datos: Tuplas
    - Aclaración sobre funciones.
  - Django: Plantillas
    - Etiquetas personalizadas.
    - Filtros personalizados.
  - Django: Justfile
    - Receta para generar "secret key".

## Version 2.1.2

Publicada el 31-10-2025

Crea documentación de:
  - Estructuras de datos: Listas
    - splitlines()
  - Django: Vistas
    - Vistas de error personalizadas.
    - Decorando vistas.
  - Django: Índice de contenidos
  - Django: Interfaz administrativa
    - Campos de búsqueda.
    - Filtros de lista.
    - Campos autocompletados.
    - Acciones de administración.

Completa documentación de:
  - Estructuras de datos: Conjuntos
    - Teoría de conjuntos.
  - Django: URLs
    - Aclaración de conversores personalizados.
  - Django: Autenticación
    - Atributos del modelo User.

## Version 2.1.1

Publicada el 29-10-2025

Completa documentación de:
  - Fundamentos del lenguaje: Bucles.
  - Django: Autenticación.
  - Django: Modelos.
  - Django: Plantillas.
  - Django: Formularios.
  - Django: URLs.
  - Django: Middleware.
  - Django: Justfile.

## Version 2.1.0

Publicada el 24-10-2025

Crea documentación de:
  - API: Middleware.

Completa documentación de:
  - Fundamentos del lenguaje: Cadenas de texto.
  - Django: API.
  - Django: Autenticación.
  - Django: Estáticos.
  - Django: Extras.
  - Django: Formularios.
  - Django: Justfile.
  - Django: Modelos.
  - Django: Plantillas.
  - Django: Puesta en marcha.
  - Django: URLs.

## Version 2.0.10

Publicada el 08-10-2025

- Añade documentación específica de `justfile` para Django.
- Completa documentación de:
  - Fundamentos del lenguaje: Algo de historia.
  - Fundamentos del lenguaje: Números.
  - Fundamentos del lenguaje: Cadenas de texto.
  - Django: Aplicaciones.
  - Django: Formularios.
  - Django: Modelos.
  - Django: Puesta en marcha.
  - Django: Estáticos.

## Version 2.0.9

Publicada el 07-10-2025

- Completa documentación de:
  - Django: Modelos.
  - Django: URLs.
  - Django: Plantillas.
  - Django: Formularios.
  - Django: Estáticos.

## Version 2.0.8

Publicada el 06-10-2025

- Completa documentación de:
  - Django: Formularios.
  - Django: Plantillas.

## Version 2.0.7

Publicada el 03-10-2025

- Completa documentación de:
  - Django: Formularios.
  - Django: Plantillas.
  - Django: URLs.
  - Django: Vistas.
- Añade abreviaturas.

## Version 2.0.6

Publicada el 01-10-2025

- Completa documentación de:
  - Django: Puesta en marcha.
  - Django: Aplicaciones.
  - Django: Modelos.
  - Django: URLs.
  - Django: Vistas.

## Version 2.0.5

Publicada el 30-09-2025

- Completa documentación de:
  - Django: Puesta en marcha.
  - Django: Aplicaciones.
  - Django: Modelos.

## Version 2.0.4

Publicada el 29-09-2025

- Completa documentación de:
  - Django: Puesta en marcha.
  - Django: Aplicaciones.
  - Django: Modelos.

## Version 2.0.3

Publicada el 26-09-2025

- Completa documentación de:
  - Historia de la computación.
  - Hablando con la máquina.
  - Introducción a Python.
  - Puesta en marcha.

## Version 2.0.2

Publicada el 22-09-2025

- Completa documentación de:
    - Fundamentos del lenguaje.
    - Expresiones regulares.
    - sqlite.
    - Desarrollo web.

## Version 2.0.1

Publicada el 19-05-2025

- Añade bloques de contenido en la página principal.
- Añade `README.md` en el repositorio de código.
