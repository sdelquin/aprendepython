---
icon: material/file-document-arrow-right-outline
---

# WeasyPrint { #weasyprint }

[WeasyPrint](https://doc.courtbouillon.org/weasyprint/stable/) es un paquete Python que permite generar ficheros PDF. Pensado especialmente para entornos de desarrollo, convierte ficheros HTML en formato PDF.

## Instalación { #install }

La instalación del paquete es muy sencilla:

=== "*venv* :octicons-package-24:{.blue}"

    ```console
    $ pip install weasyprint
    ```

=== "*uv* &nbsp;:simple-uv:{.uv}"

    ```console
    $ uv add weasyprint
    ```

### Requisitos del sistema

Este paquete necesita ciertos paquetes de sistema para su correcto funcionamiento:

=== ":simple-linux: Linux"

    ```console
    $ sudo apt-get install -y libglib2.0-0 libpango-1.0-0 libpangoft2-1.0-0
    ```

=== ":simple-apple: macOS"

    ```console
    $ brew install pango glib
    ```

    ??? example "Enlaces simbólicos"

        Si aparecen problemas, es posible que haya que realizar algunos [ajustes de enlaces simbólicos](https://github.com/Kozea/WeasyPrint/issues/1448#issuecomment-925549118):

        ```console
        sudo ln -s /opt/homebrew/opt/glib/lib/libgobject-2.0.0.dylib /usr/local/lib/gobject-2.0
        sudo ln -s /opt/homebrew/opt/pango/lib/libpango-1.0.dylib /usr/local/lib/pango-1.0
        sudo ln -s /opt/homebrew/opt/harfbuzz/lib/libharfbuzz.dylib /usr/local/lib/harfbuzz
        sudo ln -s /opt/homebrew/opt/fontconfig/lib/libfontconfig.1.dylib /usr/local/lib/fontconfig-1
        sudo ln -s /opt/homebrew/opt/pango/lib/libpangoft2-1.0.dylib /usr/local/lib/pangoft2-1.0
        ```

## Modo de uso { #usage }

Aunque existen [otros casos de uso](https://doc.courtbouillon.org/weasyprint/stable/common_use_cases.html), aquí cubriremos el más habitual. Partiendo de un fichero HTML lo convertiremos a PDF.

Para ello vamos a hacer uso de la clase [`HTML`](https://doc.courtbouillon.org/weasyprint/stable/api_reference.html#weasyprint.HTML) que proporciona _WeasyPrint_:

```pycon
>>> from weasyprint import HTML#(1)!

>>> html_content = """
... <h1>This is WeasyPrint</h1>
... <p>A powerfull package to generate PDF from HTML</p>
... """#(2)!

>>> HTML(string=html_content).write_pdf('report.pdf')#(3)!
```
{ .annotate }

1. Importamos la clase `HTML`.
2. Creamos una cadena de texto con código HTML.
3.  - También es posible invocar la clase `HTML` usando un único **parámetro posicional**. En ese caso _WeasyPrint_ tratará de averiguar si se trata de un nombre de fichero, de una URL absoluta o de un [`file object`](https://docs.python.org/3/glossary.html#term-file-object).
    - Usamos el método [`write_pdf()`](https://doc.courtbouillon.org/weasyprint/stable/api_reference.html#weasyprint.HTML.write_pdf) para generar el PDF de salida, indicando su ruta.

### URL base { #base-url }

Si queremos usar **rutas relativas** dentro del fichero HTML y no son relativas a la carpeta «actual» de trabajo, hay que especificarlo utilizando el parámetro `base_url` que pasaremos al constructor de la clase `HTML`.

Su uso depende del tipo de aplicación que estemos desarrolando:

=== "Aplicaciones de escritorio"

    ```pycon
    >>> from weasyprint import HTML

    >>> base_url = f'file://{absolute_path_to_assets}/'#(1)!
    >>> HTML('input.html', base_url=base_url).write_pdf('output.pdf')
    ```
    { .annotate }
    
    1. Fundamental acabar la ruta con barra `/`

=== "Aplicaciones web"

    ```pycon
    >>> from weasyprint import HTML

    >>> base_url = f'http://{absolute_path_to_assets}/'#(1)!
    >>> HTML('input.html', base_url=base_url).write_pdf('output.pdf')
    ```
    { .annotate }
    
    1. Fundamental acabar la ruta con barra `/`

    !!! tip "Django"
    
        En [Django](../webdev/django/webdev.md#django) podemos utilizar la función [`request.build_absolute_uri()`](https://docs.djangoproject.com/en/stable/ref/request-response/#django.http.HttpRequest.build_absolute_uri) para este cometido:

        ```python title="views.py"
        from weasyprint import HTML

        def make_report(request):
            HTML('input.html', base_url=request.build_absolute_uri()).write_pdf('output.pdf')
        ```
