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

:one: [Django básico](#django-basico)  
:two: [Django intermedio](#django-intermedio)  
:three: [Django avanzado](#django-avanzado)  
:four: [Django especializado](#django-especializado)

Los contenidos de cada bloque se identifican por una **insignia**. Existe una secuenciación de los epígrafes que es relevante, ya que se establece un orden lógico en el desarrollo de los contenidos.

## Django básico

<span class="dj-level">:material-signal-cellular-1: Django básico</span>

- [Puesta en marcha](arranque.md)
- [Aplicaciones](aplicaciones.md)
- [Modelos](modelos.md)
- [Interfaz administrativa](admin.md)
- [URLs](urls.md)
- [Vistas](vistas.md)
- [Plantillas](plantillas.md)
- [Formularios](formularios.md)
- [Estáticos](estaticos.md)

## Django intermedio

<span class="dj-level">:material-signal-cellular-2: Django intermedio</span>

- URLs
    - [URLs desde nombre](urls.md#url-desde-nombre)
    - [Accesos directos en primer nivel](urls.md#accesos-directos-en-primer-nivel)
- Formularios
    - [Widgets](formularios.md#widgets)
    - [Guardar de forma personalizada (sin claves ajenas)](formularios.md#guardar-de-forma-personalizada)
- Autenticación
    - [Autenticación](autenticacion.md)
- Modelos
    - [Claves ajenas (1:N y 1:1)](modelos.md#claves-ajenas)
    - [Campos de fichero](modelos.md#campos-de-fichero)
    - [Guardar modelos de forma personalizada](modelos.md#guardar-de-forma-personalizada)
    - [URL canónica](modelos.md#url-canonica)
    - [Ordenación por defecto](modelos.md#ordenacion-por-defecto)
    - [Valores únicos juntos](modelos.md#valores-unicos-juntos)
- Formularios
    - [Guardar de forma personalizada (con claves ajenas)](formularios.md#escenario-con-claves-ajenas)
- Vistas
    - [Tipos de respuestas HTTP](vistas.md#tipos-de-respuestas)
- URLs
    - [Conversores personalizados](urls.md#conversores-personalizados)
    - [Pasar argumentos a una vista](urls.md#pasar-argumentos-a-una-vista)
- Middleware
    - [Middleware](middleware.md)
- Interfaz administrativa
    - [Claves ajenas](admin.md#claves-ajenas)
    - [Acciones de administración](admin.md#acciones-de-administracion)

## Django avanzado

<span class="dj-level">:material-signal-cellular-3: Django avanzado</span>

- Modelos
    - [Tipos enumerados](modelos.md#tipos-enumerados)
    - [Relaciones muchos a muchos](modelos.md#relaciones-muchos-a-muchos)
    - [Relaciones muchos a muchos (con modelo intermedio)](modelos.md#relaciones-muchos-a-muchos-con-modelo-intermedio)
    - [Señales](modelos.md#senales)
    - [Validación](modelos.md#validacion)
    - [Fixtures](modelos.md#fixtures)
    - [Migraciones manuales](modelos.md#migraciones-manuales)
    - [Managers](modelos.md#managers)
    - [Funciones](modelos.md#funciones)
- Interfaz administrativa
    - [Relaciones muchos a muchos](admin.md#relaciones-muchos-a-muchos)
    - [Comandos de gestión](admin.md#comandos-de-gestion)
- URLs
    - [Expresiones regulares](urls.md#expresiones-regulares)
- Plantillas
    - [Etiquetas personalizadas](plantillas.md#etiquetas-personalizadas)
    - [Filtros personalizados](plantillas.md#filtros-personalizados)
    - [Procesadores de contexto](plantillas.md#procesadores-de-contexto)
- Formularios
    - [Validación de formularios](formularios.md#validacion)
- Estáticos
    - [Bootstrap](estaticos.md#bootstrap)
- Internacionalización
    - [Internacionalización](i18n.md)
- Extras
    - [Django Reload](extras.md#django-reload)
    - [Crispy Forms](extras.md#crispy-forms)
    - [Sorl Thumbnail](extras.md#sorl-thumbnail)
    - [Django Markdownify](extras.md#django-markdownify)
    - [Django-RQ](extras.md#django-rq)
    - [Enviar correo](extras.md#enviar-correo)
    - [Django ColorField](extras.md#django-colorfield)
- Paquetes de terceros
    - [Prettyconf](../../config/prettyconf.md)
    - [WeasyPrint](../../pdf/weasyprint.md)
- Middleware
    - [Middleware personalizado](middleware.md#middleware-personalizado)

## Django especializado

<span class="dj-level">:material-target-variant: Django especializado</span>

- [API](api.md)
