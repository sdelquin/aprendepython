from __future__ import annotations

import sqlite3

DB_PATH = 'todo.db'
TASK_DONE_SYMBOL = '✔'
TASK_PENDING_SYMBOL = '⎕'


class Task:
    '''Crear atributos de clase:
    - con: para la conexión a la base de datos.
    - cur: para el cursor de manejo.'''

    # <hide>
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    # </hide>

    def __init__(self, name: str, done: bool = False, id: int = -1):
        '''Crea los atributos homónimos a los parámetros'''
        # <hide>
        self.name = name
        self.done = done
        self.id = id
        # </hide>

    def save(self):
        '''Guarda esta tarea en la base de datos.
        El identificador asignado en la base de datos se debe usar para actualizar el
        atributo id de la tarea.'''
        # <hide>
        sql = 'INSERT INTO tasks(name, done) VALUES(?, ?)'
        self.cur.execute(sql, (self.name, self.done))
        self.id = self.cur.lastrowid
        self.con.commit()
        # </hide>

    def update(self):
        '''Actualiza la tarea (nombre y estado) en la base de datos'''
        # <hide>
        sql = 'UPDATE tasks SET name=?, done=? WHERE id=?'
        self.cur.execute(sql, (self.name, self.done, self.id))
        self.con.commit()
        # </hide>

    def check(self):
        '''Marca la tarea como completada. Haz uso también de .update()'''
        # <hide>
        self.done = True
        self.update()
        # </hide>

    def uncheck(self):
        '''Marca la tarea como no completada. Haz uso también de .update()'''
        # <hide>
        self.done = False
        self.update()
        # </hide>

    def __repr__(self):
        '''Muestra la tarea en formato:
        <SYMBOL> <name> (id=<id>)'''
        # <hide>
        symbol = TASK_DONE_SYMBOL if self.done else TASK_PENDING_SYMBOL
        return f'{symbol} {self.name} (id={self.id})'
        # </hide>

    @classmethod
    def from_db_row(cls, row: sqlite3.Row) -> Task:
        '''Construye una nueva tarea a partir de una fila de consulta devuelta por execute()'''
        # <hide>
        return Task(row['name'], row['done'], row['id'])
        # </hide>

    @classmethod
    def get(cls, task_id: int) -> Task:
        '''Devuelve un objeto Task desde la consulta a la base de datos'''
        # <hide>
        sql = 'SELECT * FROM tasks WHERE id=?'
        result = cls.cur.execute(sql, (task_id,))
        return cls.from_db_row(result.fetchone())
        # </hide>


class ToDo:
    '''Crear atributos de clase:
    - con: para la conexión a la base de datos.
    - cur: para el cursor de manejo.'''

    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def create_db(self):
        '''Crea la base de datos con los campos "id", "name" y "done"'''
        # <hide>
        sql = '''CREATE TABLE tasks (
            id INTEGER PRIMARY KEY,
            name CHAR,
            done INTEGER)'''
        self.cur.execute(sql)
        self.con.commit()
        # </hide>

    def get_tasks(self, *, done: int = -1):
        '''Devuelve todas las tareas como objetos de tipo Task consultando la BBDD.
        - Si done = 0 se devuelven las tareas pendientes.
        - Si done = 1 se devuelven las tareas completadas.
        Ojo! Esto es una función generadora.'''
        # <hide>
        sql = 'SELECT * FROM tasks'
        if done != -1:
            sql += f' WHERE done={done}'
        result = self.cur.execute(sql)
        for row in result.fetchall():
            yield Task.from_db_row(row)
        # </hide>

    def add_task(self, name: str):
        '''Añade la tarea con nombre "name"'''
        # <hide>
        task = Task(name)
        task.save()
        # </hide>

    def complete_task(self, task_id: int):
        '''Marca la tarea con identificador "task_id" como completada'''
        # <hide>
        task = Task.get(task_id)
        task.check()
        # </hide>

    def reopen_task(self, task_id: int):
        '''Marca la tarea con identificador "task_id" como pendiente'''
        # <hide>
        task = Task.get(task_id)
        task.uncheck()
        # </hide>
