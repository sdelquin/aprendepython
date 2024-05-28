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
    # <hide>
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    sql = """
    CREATE TABLE user (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT,
        bio TEXT
    );

    CREATE TABLE tweet (
        id INTEGER PRIMARY KEY,
        content TEXT,
        user_id INTEGER,
        retweet_from INTEGER,
        FOREIGN KEY (user_id) REFERENCES user(id),
        FOREIGN KEY (retweet_from) REFERENCES tweet(id)
    );
    """
    cur.executescript(sql)
    con.commit()
    # </hide>


class User:
    def __init__(self, username: str, password: str, bio: str = '', user_id: int = 0):
        """Constructor de la clase User.
        - Crea los atributos con y cur para la conexión a la base de datos (con factoría Row).
        - Crea los atributos username, password, bio, id y logged.
        """
        # <hide>
        self.con = sqlite3.connect(DB_PATH)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

        self.username = username
        self.password = password
        self.bio = bio
        self.id = user_id
        self.logged = False
        # </hide>

    def save(self) -> None:
        """Guarda en la base de datos un objeto de tipo User.
        Además actualiza el atributo "id" del objeto a partir de lo que devuelve la inserción."""
        # <hide>
        sql = 'INSERT INTO user (username, password, bio) VALUES (?, ?, ?)'
        params = (self.username, self.password, self.bio)
        self.cur.execute(sql, params)
        self.con.commit()
        self.id = self.cur.lastrowid
        # </hide>

    def login(self, password: str) -> None:
        """Realiza el login del usuario.
        Comprueba si existe este usuario con el password pasado por parámetro en la BBDD
        y actualiza los atributos correspondientes."""
        # <hide>
        sql = 'SELECT COUNT(*) FROM user WHERE username=? and password=?'
        params = (self.username, password)
        result = self.cur.execute(sql, params)
        row = result.fetchone()
        self.logged = row[0] == 1
        # </hide>

    def tweet(self, content: str) -> Tweet:
        """Crea un tweet con el contenido indicado y lo almacena en la base de datos.
        - Utiliza el método save propio de la clase Tweet.
        - Hay que retornar el tweet creado.
        - Si el usuario no está logeado hay que lanzar una excepción de tipo TwitterError
        con el mensaje: User <usuario> is not logged in!
        - Si el tweet supera el límite de caracteres hay que lanzar una excepción de tipo
        TwitterError con el mensaje: Tweet hasta more than 280 chars!"""
        # <hide>
        if not self.logged:
            raise TwitterError(f'User {self.username} is not logged in!')
        if len(content) > MAX_TWEET_LENGTH:
            raise TwitterError(f'Tweet has more than {MAX_TWEET_LENGTH} chars!')
        t = Tweet(content)
        t.save(self)
        return t
        # </hide>

    def retweet(self, tweet_id: int) -> Tweet:
        """Crea un retweet con el contenido indicado y lo almacena en la base de datos.
        - Utiliza el método save propio de la clase Tweet.
        - Hay que retornar el tweet creado.
        - Si el usuario no está logeado hay que lanzar una excepción de tipo TwitterError
        con el mensaje: User <usuario> is not logged in!
        - Si tweet_id no existe en la base de datos hay que lanzar una excepción de tipo
        TwitterError con el mensaje: Tweet with id <id> does not exist!"""
        # <hide>
        if not self.logged:
            raise TwitterError(f'User {self.username} is not logged in!')

        sql = 'SELECT COUNT(*) FROM tweet where id=?'
        result = self.cur.execute(sql, (tweet_id,))
        row = result.fetchone()
        if row[0] == 0:
            raise TwitterError(f'Tweet with id {tweet_id} does not exist!')

        t = Tweet(retweet_from=tweet_id)
        t.save(self)
        return t
        # </hide>

    @property
    def tweets(self):
        """Función generadora que devuelve todos los tweets propios del usuario.
        - Lo que se devuelven son objetos de tipo Tweet (usar el método from_db_row)."""
        # <hide>
        sql = 'SELECT * FROM tweet WHERE user_id=?'
        result = self.cur.execute(sql, (self.id,))
        for row in result:
            yield Tweet.from_db_row(row)
        # </hide>

    def __repr__(self):
        """Representa un usuario con el formato:
        <usuario>: <bio>"""
        # <hide>
        return f'{self.username}: {self.bio}'
        # </hide>

    @classmethod
    def from_db_row(cls, row: sqlite3.Row):
        """Crea un objeto de tipo User a partir de una fila de consulta SQL"""
        # <hide>
        return cls(row['username'], row['password'], row['bio'], row['id'])
        # </hide>


class Tweet:
    def __init__(self, content: str = '', retweet_from: int = 0, tweet_id: int = 0):
        """Constructor de la clase Tweet.
        - Crea los atributos con y cur para la conexión a la base de datos (con factoría Row)
        - Crea los atributos _content, retweet_from e id.
        - retweet_from indica el id del tweet que se retuitea.
          Un id válido debe ser mayor o igual que 1.
        - Si es un retweet el contenido debe ser la cadena vacía.
        """
        # <hide>
        self.con = sqlite3.connect(DB_PATH)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

        self.retweet_from = retweet_from
        self._content = '' if self.is_retweet else content
        self.id = tweet_id
        # </hide>

    @property
    def is_retweet(self) -> bool:
        """Indica si el tweet es un retweet."""
        # <hide>
        return self.retweet_from > 0
        # </hide>

    @property
    def content(self) -> str:
        """Devuelve el contenido del tweet.
        - Si es un retweet el contenido habrá que buscarlo en el tweet retuiteado."""
        # <hide>
        if self.is_retweet:
            sql = 'SELECT content FROM tweet WHERE id=?'
            result = self.cur.execute(sql, (self.retweet_from,))
            return result.fetchone()['content']
        return self._content
        # </hide>

    def save(self, user: User) -> None:
        """Guarda el tweet en la base de datos.
        - El parámetro user es el usuario que escribe el tweet.
        Además actualiza el atributo "id" del objeto a partir de lo que devuelve la inserción."""
        # <hide>
        sql = 'INSERT INTO tweet (content, user_id, retweet_from) VALUES (?, ?, ?)'
        params = (self._content, user.id, self.retweet_from)
        self.cur.execute(sql, params)
        self.con.commit()
        self.id = self.cur.lastrowid
        # </hide>

    def __repr__(self):
        """Representa un tweet con el formato:
        <emoji> <content> (id=<id>)"""
        # <hide>
        emoji = RETWEET_EMOJI if self.is_retweet else TWEET_EMOJI
        return f'{emoji} {self.content} (id={self.id})'
        # </hide>

    @classmethod
    def from_db_row(cls, row: sqlite3.Row) -> Tweet:
        """Crea un objeto de tipo Tweet a partir de una fila de consulta SQL"""
        # <hide>
        return cls(row['content'], row['retweet_from'], row['id'])
        # </hide>


class Twitter:
    def __init__(self):
        """Constructor de la clase Twitter.
        - Crea los atributos con y cur para la conexión a la base de datos (con factoría Row)
        """
        # <hide>
        self.con = sqlite3.connect(DB_PATH)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
        # </hide>

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
        # <hide>
        if not re.match(r'^[@=]\d{2,4}[A-Za-z]{2,4}[!*]$', password):
            raise TwitterError('Password does not follow security rules!')
        user = User(username, password, bio)
        user.save()
        return user
        # </hide>

    def get_user(self, user_id: int) -> User:
        """Devuelve el usuario con el user_id indicado.
        Si el usuario no existe hay elevar una excepción de tipo TwitterError con el mensaje:
        User with id <id> does not exist!"""
        # <hide>
        sql = 'SELECT * FROM user WHERE id=?'
        result = self.cur.execute(sql, (user_id,))
        if row := result.fetchone():
            return User.from_db_row(row)
        raise TwitterError(f'User with id {user_id} does not exist!')
        # </hide>


class TwitterError(Exception):
    pass
