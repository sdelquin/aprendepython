from __future__ import annotations

import re
import sqlite3

DB_PATH = 'twitter.db'

TWEET_EMOJI = '🐦'
RETWEET_EMOJI = '🔁'
MAX_TWEET_LENGTH = 280


def create_db(db_path: str = DB_PATH) -> None:
    """Crea la base de datos y las siguientes tablas:
    - user (id, username, password, bio)
    - tweet (id, content, user_id, retweet_from)
        └ user_id es clave ajena de user(id)
        └ retweet_from es clave ajena de tweet(id)"""
    pass


class User:
    def __init__(self, username: str, password: str, bio: str = '', user_id: int = 0):
        """Constructor de la clase User.
        - Crea los atributos con y cur para la conexión a la base de datos (con factoría Row).
        - Crea los atributos username, password, bio, id y logged.
        """
        pass

    def save(self) -> None:
        """Guarda en la base de datos un objeto de tipo User.
        Además actualiza el atributo "id" del objeto a partir de lo que devuelve la inserción."""
        pass

    def login(self, password: str) -> None:
        """Realiza el login del usuario.
        Comprueba si existe este usuario con el password pasado por parámetro en la BBDD
        y actualiza los atributos correspondientes."""
        pass

    def tweet(self, content: str) -> Tweet:
        """Crea un tweet con el contenido indicado y lo almacena en la base de datos.
        - Utiliza el método save propio de la clase Tweet.
        - Hay que retornar el tweet creado.
        - Si el usuario no está logeado hay que lanzar una excepción de tipo TwitterError
        con el mensaje: User <usuario> is not logged in!
        - Si el tweet supera el límite de caracteres hay que lanzar una excepción de tipo
        TwitterError con el mensaje: Tweet hasta more than 280 chars!"""
        pass

    def retweet(self, tweet_id: int) -> Tweet:
        """Crea un retweet con el contenido indicado y lo almacena en la base de datos.
        - Utiliza el método save propio de la clase Tweet.
        - Hay que retornar el tweet creado.
        - Si el usuario no está logeado hay que lanzar una excepción de tipo TwitterError
        con el mensaje: User <usuario> is not logged in!
        - Si tweet_id no existe en la base de datos hay que lanzar una excepción de tipo
        TwitterError con el mensaje: Tweet with id <id> does not exist!"""
        pass

    @property
    def tweets(self):
        """Función generadora que devuelve todos los tweets propios del usuario.
        - Lo que se devuelven son objetos de tipo Tweet (usar el método from_db_row)."""
        pass

    def __repr__(self):
        """Representa un usuario con el formato:
        <usuario>: <bio>"""
        pass

    @classmethod
    def from_db_row(cls, row: sqlite3.Row):
        """Crea un objeto de tipo User a partir de una fila de consulta SQL"""
        pass


class Tweet:
    def __init__(self, content: str = '', retweet_from: int = 0, tweet_id: int = 0):
        """Constructor de la clase Tweet.
        - Crea los atributos con y cur para la conexión a la base de datos (con factoría Row)
        - Crea los atributos _content, retweet_from e id.
        - retweet_from indica el id del tweet que se retuitea.
          Un id válido debe ser mayor o igual que 1.
        - Si es un retweet el contenido debe ser la cadena vacía.
        """
        pass

    @property
    def is_retweet(self) -> bool:
        """Indica si el tweet es un retweet."""
        pass

    @property
    def content(self) -> str:
        """Devuelve el contenido del tweet.
        - Si es un retweet el contenido habrá que buscarlo en el tweet retuiteado."""
        pass

    def save(self, user: User) -> None:
        """Guarda el tweet en la base de datos.
        - El parámetro user es el usuario que escribe el tweet.
        Además actualiza el atributo "id" del objeto a partir de lo que devuelve la inserción."""
        pass

    def __repr__(self):
        """Representa un tweet con el formato:
        <emoji> <content> (id=<id>)"""
        pass

    @classmethod
    def from_db_row(cls, row: sqlite3.Row) -> Tweet:
        """Crea un objeto de tipo Tweet a partir de una fila de consulta SQL"""
        pass


class Twitter:
    def __init__(self):
        """Constructor de la clase Twitter.
        - Crea los atributos con y cur para la conexión a la base de datos (con factoría Row)
        """
        pass

    def add_user(self, username: str, password: str, bio: str = '') -> User:
        """Crea un objeto de tipo User y lo guarda en la base de datos.
        - Haz uso de los métodos ya creados.
        - Hay que retornar el objeto creado.
        - La contraseña debe seguir el siguiente formato:
          * Empezar con una arroba o un signo igual.
          * Continuar con 2, 3 o 4 dígitos.
          * Continuar con 2, 3 o 4 letras de la A-Z (incluyendo minúsculas).
          * Terminar con una exclamación o un asterisco.
        Si no sigue este formato hay que elevar una excepción de tipo TwitterError
        con el mensaje: Password does not follow security rules!"""
        pass

    def get_user(self, user_id: int) -> User:
        """Devuelve el usuario con el user_id indicado.
        Si el usuario no existe hay elevar una excepción de tipo TwitterError con el mensaje:
        User with id <id> does not exist!"""
        pass


class TwitterError(Exception):
    pass
