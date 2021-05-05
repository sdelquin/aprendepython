# Aprende Python

![Logo - AprendePython](_static/img/logo-solo-aprendepython-small.png)

Curso gratuito para aprender el lenguaje de programación **Python** con un enfoque **práctico**, incluyendo **ejercicios** y cobertura para distintos **niveles de conocimiento**.

## Desarrollo

Asegúrate de que tienes instalado _Docker_ y _docker-compose_.

Construir la imagen del proyecto:

```console
$ docker-compose build
```

### Documentación en `html` para desarrollo

Renderizar la documentación en `html` con **live-reload**:

```console
$ docker-compose up
```

Una vez que salgan por pantalla los siguientes mensajes:

```console
Serving on http://0.0.0.0:8000
Start watching changes
Start detecting changes
```

, ya se podrá acceder a http://127.0.0.1:8000/ para ver la documentación.

### Documentación en `html` para producción

Renderizar la documentación completa en `html`:

```console
$ docker-compose run aprendepython make dirhtml
```

Al terminar la ejecución, se podrá encontrar la documentación del curso en: `_build/dirhtml/`.

### Documentación en `pdf`

Generar la documentación en `pdf` a través de _Latex_:

```console
$ docker-compose run aprendepython make latexpdf
```

> ℹ️️ &nbsp; Este proceso toma su tiempo ya que la documentación es extensa.

Al terminar la ejecución, se podrá encontrar la documentación en: `_build/latex/aprendepython.pdf`
