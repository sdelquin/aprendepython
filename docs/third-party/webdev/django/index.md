---
icon: simple/django
tags:
  - Paquetes de terceros
  - Desarrollo web
  - Django
---

# Django

![Banner](images/banner.jpg)
///caption
Imagen generada con Inteligencia Artificial
///

Django :simple-django:{ .green .beat } es un framework de desarrollo web de código abierto, escrito en Python, que respeta el patrón de diseño conocido como modelo–vista–controlador (MVC). Fue desarrollado originalmente para gestionar páginas web orientadas a noticias de la World Company de Lawrence, Kansas, y fue liberada al público bajo una licencia BSD en julio de 2005; el framework fue nombrado en alusión al guitarrista de jazz gitano Django Reinhardt.

---

Los contenidos de esta sección están organizados de la siguiente manera:

:one: [Django básico](#basic)  
:two: [Django intermedio](#intermediate)  
:three: [Django avanzado](#advanced)  
:four: [Django especializado](#specialized)

Los contenidos de cada bloque se identifican por una **insignia**. Existe una secuenciación de los epígrafes que es relevante, ya que se establece un orden lógico en el desarrollo de los contenidos.

## Django básico { #basic }

<span class="dj-level">:material-signal-cellular-1: Django básico</span>

- [Puesta en marcha](setup.md)
- [Aplicaciones](apps.md)
- [Modelos](models.md)
- [Interfaz administrativa](admin.md)
- [URLs](urls.md)
- [Vistas](views.md)
- [Plantillas](templates.md)
- [Formularios](forms.md)
- [Estáticos](static.md)

## Django intermedio { #intermediate }

<span class="dj-level">:material-signal-cellular-2: Django intermedio</span>

- URLs
    - [URLs desde nombre](urls.md#reverse)
    - [Accesos directos en primer nivel](urls.md#main-shortcuts)
- Formularios
    - [Widgets](forms.md#widgets)
    - [Guardar de forma personalizada (sin claves ajenas)](forms.md#override-save-no-fk)
- Autenticación
    - [Autenticación](auth.md)
- Modelos
    - [Claves ajenas (1:N y 1:1)](models.md#foreign-keys)
    - [Campos de fichero](models.md#file-fields)
    - [Guardar modelos de forma personalizada](models.md#override-save)
    - [URL canónica](models.md#canonical-url)
    - [Ordenación por defecto](models.md#default-ordering)
    - [Valores únicos juntos](models.md#unique-together)
- Formularios
    - [Guardar de forma personalizada (con claves ajenas)](forms.md#override-save-fk)
- Vistas
    - [Tipos de respuestas HTTP](views.md#response-types)
- URLs
    - [Conversores personalizados](urls.md#custom-path-converters)
    - [Pasar argumentos a una vista](urls.md#args-to-view)
- Middleware
    - [Middleware](middleware.md)
- Interfaz administrativa
    - [Claves ajenas](admin.md#foreign-key)
    - [Acciones de administración](admin.md#admin-actions)

## Django avanzado { #advanced }

<span class="dj-level">:material-signal-cellular-3: Django avanzado</span>

- Modelos
    - [Tipos enumerados](models.md#enums)
    - [Relaciones muchos a muchos](models.md#many-to-many)
    - [Relaciones muchos a muchos (con modelo intermedio)](models.md#many-to-many-with-intermediary)
    - [Señales](models.md#signals)
    - [Validadores](models.md#validators)
- Interfaz administrativa
    - [Relaciones muchos a muchos](admin.md#many-to-many)
    - [Comandos de gestión](admin.md#management-commands)
- URLs
    - [Expresiones regulares](urls.md#regex)
- Plantillas
    - [Etiquetas personalizadas](templates.md#custom-tags)
    - [Filtros personalizados](templates.md#custom-filters)
    - [Procesadores de contexto](templates.md#context-processors)
- Formularios
    - [Validación de formularios](forms.md#validation)
- Estáticos
    - [Bootstrap](static.md#bootstrap)
- Internacionalización
    - [Internacionalización](i18n.md)
- Extras
    - [Django Reload](extras.md#django-reload)
    - [Crispy Forms](extras.md#crispy-forms)
    - [Sorl Thumbnail](extras.md#sorl-thumbnail)
    - [Django Markdownify](extras.md#django-markdownify)
    - [Django-RQ](extras.md#django-rq)
    - [Enviar correo](extras.md#sending-email)
    - [Django ColorField](extras.md#django-colorfield)
- Paquetes de terceros
    - [Prettyconf](../../config/prettyconf.md)
    - [WeasyPrint](../../pdf/weasyprint.md)
- Middleware
    - [Middleware personalizado](middleware.md#custom-middleware)

## Django especializado { #specialized }

<span class="dj-level">:material-target-variant: Django especializado</span>

- [API](api.md)
