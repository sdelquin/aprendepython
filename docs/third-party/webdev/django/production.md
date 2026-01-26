---
icon: fontawesome/solid/industry
tags:
  - Paquetes de terceros
  - Desarrollo web
  - Django
---

# Producción { #production }

En esta sección vamos a tratar de aclarar distintos aspectos relevantes a la hora de **poner en producción un proyecto Django** (que en principio ya tenemos funcionando en _desarrollo_).

## Requisitos previos { #requirements }

### Hosting { #hosting }

Obviamente lo primero que necesitaremos para poder subir nuestro proyecto «a la nube» es disponer de alguna zona de _hosting_ (hospedaje).

Existen multitud de empresas en el mercado que permiten disponer de VPS. Sin querer hacer publicidad gratuita a nadie, y basándome en mi experiencia, las opciones que ofrece [Hetzner](https://www.hetzner.com/cloud) son muy interesantes.

Vamos a suponer que ya disponemos de un VPS con sistema operativo Linux :simple-linux: y acceso por SSH.

### Dominio { #domain }

También será necesario disponer de un dominio (o subdominio) que será la URL base para desplegar nuestro proyecto.

Al igual que ocurre con el _hosting_ (o incluso más aún) existen una grandísima cantidad de empresas que ofrecen servicios de compra de dominios. Sin querer hacer publicidad gratuita a nadie, y basándome en mi experiencia, las opciones que ofrece [DonDominio](https://www.dondominio.com/es/buscar/) son muy interesantes.

Vamos a suponer que ya disponemos de un dominio y que lo hemos configurado en _gestión de DNS_ con un registro A[^1] para que apunte a la IP del VPS anteriormente descrito.

## Despliegue { #deploy }

A partir de aquí vamos a suponer que el acceso al VPS se realiza mediante el nombre DNS `vps` y que el proyecto Django es un «blog» situado (`git clone`) en la carpeta remota `/home/sdelquin/blog`. El nombre de dominio asociado será `blog.com`

### Scripts { #scripts }

Aunque no es estrictamente obligatorio, sí que es muy recomendable implementar algunos _scripts_ en nuestro proyecto para facilitar la puesta en marcha en producción.

#### Script de servicio { #service-script }

Necesitamos implementar un _script_ que permita levantar el proceso que sirve el proyecto Django (como aplicación Python).

Para ello crearemos el siguiente fichero en el _raíz de nuestro proyecto_:

```bash title="run.sh"
#!/bin/bash

cd $(dirname $0)
source .venv/bin/activate
exec gunicorn -b unix:/tmp/blog.sock main.wsgi:application
```

??? info "Permisos de ejecución"

    Recuerda dar **permisos de ejecución** al _script_ anterior:

    ```console
    chmod u+x run.sh
    ```

Como te habrás dado cuenta, en el _script_ estamos utilizando [Gunicorn](https://gunicorn.org/) que es uno de muchos servidores WSGI que se encargan de servir aplicaciones Python.

Por lo tanto, tendremos que añadir esta dependencia a nuestro proyecto:

=== "*venv* :octicons-package-24:{.blue}"

    ```console
    $ pip install gunicorn
    ```

=== "*uv* &nbsp;:simple-uv:{.uv}"

    ```console
    $ uv add --group prod gunicorn #(1)!
    ```
    { .annotate }
    
    1. _uv_ permite añadir dependencias a grupos específicos. En este caso al grupo de producción.

#### Script de despliegue { #deploy-script }

A la hora de automatizar el proceso de despliegue, es necesario llevar a cabo varios pasos.

A continuación se muestra una propuesta de _script_ de despliegue con las distinas acciones (suponiendo un entorno _uv_):

=== "*venv* :octicons-package-24:{.blue}"

    ```bash title="deploy.sh"
    #!/bin/bash

    cd ~/blog
    git pull
    source .venv/bin/activate
    pip install -r requirements.txt
    ./manage.py migrate
    npm install --no-audit --no-fund
    ./manage.py collectstatic --no-input
    supervisorctl restart blog
    ```

=== "*uv* &nbsp;:simple-uv:{.uv}"

    ```bash title="deploy.sh"
    #!/bin/bash

    cd ~/blog
    git pull
    uv sync --no-dev --group prod
    uv run ./manage.py migrate
    npm install --no-audit --no-fund
    uv run ./manage.py collectstatic --no-input
    supervisorctl restart blog
    ```

??? info "Permisos de ejecución"

    Recuerda dar **permisos de ejecución** al _script_ anterior:

    ```console
    chmod u+x deploy.sh
    ```

### Servidor Web { #webserver }

En el VPS necesitaremos instalar un **servidor web** que nos de soporte a las peticiones provenientes desde clientes web (navegadores).

En este caso nos centraremos en [Nginx :simple-nginx:](https://nginx.org/) que es un _servidor web_ + _proxy inverso_ muy eficiente y sencillo de configurar.

Una vez instalado debemos definir un nuevo _virtual host_ que nos permita desplegar la aplicación web:

```nginx title="/etc/nginx/conf.d/blog.conf"
server {
    server_name blog.com;#(1)!

    location /static {#(2)!
        root /home/sdelquin/blog;
    }

    location /media {#(3)!
        root /home/sdelquin/blog;
    }

    location / {#(4)!
        proxy_pass http://unix:/tmp/blog.sock;
        proxy_set_header Host $http_host;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    access_log /var/log/nginx/blog.access.log;#(5)!
    error_log /var/log/nginx/blog.error.log;#(6)!
    client_max_body_size 10M;#(7)!
}
```
{ .annotate }

1. Nombre del dominio donde se expone la aplicación web.
2. Los ficheros estáticos se sirven (en producción) directamente por el servidor web.
3. Los ficheros «media» se sirven (en producción) directamente por el servidor web.
4. Zona «proxy inverso» donde se derivan las peticiones a un proceso que «entiende» Python.
5. Fichero de _log_ para registrar accesos.
6. Fichero de _log_ para registrar errores.
7. Máximo tamaño de petición.

Una vez hechos estos cambios es importante recargar la configuración del servidor web:

```console
$ sudo systemctl reload nginx
```

#### Certbot { #certbot }

[Certbot](https://certbot.eff.org/) es una herramienta que permite asignar HTTPS a nuestro dominio de forma muy sencilla y totalmente gratuita.

Una vez instalado en la máquina de producción, podemos generar el certificado de seguridad de la siguiente manera:

```console
$ sudo certbot -d blog.com
```

El comando anterior se encargará de modificar las líneas correspondientes del _virtual host_ de _Nginx_ para añadir las configuraciones de seguridad correspondientes en `/etc/nginx/conf.d/blog.conf`. Además añade una redirección automática, de manera que el acceso a `http` se convierte en `https`.

### Supervisor { #supervisor }

Es bastante recomendable disponer de algún artefacto _supervisor_ que se encargue de gestionar el proceso WSGI que levanta el propio proyecto Django.

Se recomienda utilizar [Supervisor](https://supervisord.org/) que es un software desarrollado en Python precisamente para controlar procesos en sistemas operativos tipo UNIX.

Una vez instalado debemos crear el fichero de configuración correspondiente a nuestro proyecto:


```ini title="/etc/supervisor/conf.d/blog.conf"
[program:blog]
user = sdelquin#(1)!
command = /home/sdelquin/blog/run.sh#(2)!
autostart = true
autorestart = true
stopsignal = INT
killasgroup = true
stderr_logfile = /var/log/supervisor/blog.err.log
stdout_logfile = /var/log/supervisor/blog.out.log
```
{ .annotate }

1. Usuario «propietario» del proceso.
2. Comando a ejecutar.

Para añadir el proceso al conjuno de procesos de _supervisor_ debemos hacer lo siguiente:

```console
$ supervisorctl reread
$ supervisorctl add blog
```

### Automatización { #deploy-automation }

Tal y como tenemos diseñado nuestro proyecto, podríamos automatizar el despliegue lanzando un único comando:

```console
$ ssh vps ~/blog/deploy.sh
```

Pero existe una forma aún más desatendida, que se encarga de desplegar el proyecto una vez que hacemos `git push` al repositorio remoto. Para ello se utilizan (entre otras) las [GitHub Actions](https://github.com/features/actions).

#### GitHub Actions { #github-actions }

Se trata de un conjunto de artefactos de software que permiten automatizar tareas frente a ciertos eventos en repositorios GitHub.

A continuación se presenta una _propuesta_ para automatizar el despliegue del proyecto Django del «blog»:

```yaml title=".github/workflows/ci.yml"
name: CI
on:
  push:
    branches:
      - main
  workflow_dispatch:
jobs:
  deploy:
    name: Deploy project
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      - name: Execute remote deploy commands
        uses: appleboy/ssh-action@master
        with:
          host: blog.com
          username: ${{ secrets.PRODUCTION_SSH_USERNAME }}
          key: ${{ secrets.PRODUCTION_SSH_KEY }}
          script: ~/blog/deploy.sh
```

##### Secretos { #github-secrets }

Para poder almacenar de manera segura credenciales o datos confidenciales, GitHub proporciona los [secretos](https://docs.github.com/es/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets) para sus acciones. En el <span class="example">ejemplo:material-flash:</span> anterior tendremos que dar de alta, al menos, los dos siguientes:

- `PRODUCTION_SSH_USERNAME`: Nombre de usuario con el que conectarnos al VPS.
- `PRODUCTION_SSH_KEY`: Clave privada para conectarnos al VPS.

Mediante `ssh-keygen` debemos crear un par de claves SSH: la pública se almacenará en el servidor VPS correspondiente, y la privada se almacenará en los secretos de la _GitHub Action_ para que se pueda conectar al servidor.

## Logging { #logging }

Cuando desplegamos un proyecto Django (o cualquier otro) a producción es realmente conveniente disponer de un sistema de [logging](https://docs.djangoproject.com/en/stable/topics/logging/) para registrar errores o mensajes de depuración que nos puedan ayudar a conocer el estado del sistema o a solucionar posibles problemas que surjan.

En este sentido, vamos a añadir un bloque de _logging_ en el fichero de configuraciones del proyecto:

```python title="main/settings.py"
if not DEBUG:#(1)!
    LOG_DIR = config('LOGS_DIR', default=BASE_DIR / 'logs', cast=Path)#(2)!
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    LOG_FILENAME = config('LOG_FILENAME', default=f'{PROJECT_NAME}.log')#(3)!
    LOG_PATH = LOG_DIR / LOG_FILENAME
    LOG_SIZE = config('LOG_SIZE', default=2, cast=int) * 1024 * 1024#(4)!
    LOG_ROTATE = config('LOG_ROTATE', default=3, cast=int)#(5)!
    LOG_LEVEL = config('LOG_LEVEL', default='ERROR')
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'formatter': 'verbose',
                'class': 'logging.handlers.RotatingFileHandler',
                'level': LOG_LEVEL,
                'filename': LOG_PATH,
                'maxBytes': LOG_SIZE,
                'backupCount': LOG_ROTATE,
            },
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(message)s',
                'datefmt': '%d/%m/%Y %H:%M:%S',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': LOG_LEVEL,
                'propagate': True,
            },
        },
    }
```
{ .annotate }

1. Solo aplicamos este _logging_ en producción.
2. Carpeta de _logging_.
3. Nombre base de los ficheros de _logging_.
4. Por defecto el tamaño de cada fichero de _logging_ no puede superar los 2MB.
5. Se mantienen 3 rotaciones de los ficheros de _logging_.


[^1]: Un registro A de DNS (Address Record) es el tipo de registro fundamental que mapea un nombre de dominio (como ejemplo.com) a una dirección IPv4 específica (como 192.0.2.1), permitiendo que tu navegador encuentre el servidor correcto para un sitio web, y es esencial para la navegación en internet al traducir nombres legibles por humanos a números de máquina.
