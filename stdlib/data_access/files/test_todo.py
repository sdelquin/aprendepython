import sqlite3
import typing
from pathlib import Path

import pytest
from todo import Task, ToDo, create_db

TEST_DB_PATH = 'test_todo.db'

# **************************************************************
# FIXTURES
# **************************************************************


@pytest.fixture(autouse=True)
def create_test_database():
    try:
        create_db(TEST_DB_PATH)
        yield
    except Exception as err:
        raise err
    finally:
        Path(TEST_DB_PATH).unlink(missing_ok=True)


@pytest.fixture(autouse=True)
def make_db_attrs_use_test_database(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(Task, 'con', sqlite3.connect(TEST_DB_PATH))
    monkeypatch.setattr(Task.con, 'row_factory', sqlite3.Row)
    monkeypatch.setattr(Task, 'cur', Task.con.cursor())

    monkeypatch.setattr(ToDo, 'con', sqlite3.connect(TEST_DB_PATH))
    monkeypatch.setattr(ToDo.con, 'row_factory', sqlite3.Row)
    monkeypatch.setattr(ToDo, 'cur', ToDo.con.cursor())


@pytest.fixture
def task1():
    return Task('Estudiar programación')


@pytest.fixture
def task2():
    return Task('Estudiar bases de datos', True)


@pytest.fixture
def task3():
    return Task('Estudiar sistemas informáticos', True, 55)


@pytest.fixture
def todo():
    return ToDo()


@pytest.fixture
def db_con():
    con = sqlite3.connect(TEST_DB_PATH)
    con.row_factory = sqlite3.Row
    yield con
    con.close()


# **************************************************************
# TESTS
# **************************************************************


def test_task_class_has_db_attrs():
    assert isinstance(Task.con, sqlite3.Connection)
    assert Task.con.row_factory == sqlite3.Row
    assert isinstance(Task.cur, sqlite3.Cursor)


def test_build_task(task1: Task, task2: Task, task3: Task):
    assert task1.name == 'Estudiar programación'
    assert task1.done is False
    assert task1.id == -1

    assert task2.name == 'Estudiar bases de datos'
    assert task2.done is True
    assert task2.id == -1

    assert task3.name == 'Estudiar sistemas informáticos'
    assert task3.done is True
    assert task3.id == 55


def test_save_task(task1: Task, task2: Task, task3: Task):
    assert task1.id == -1
    task1.save()
    assert task1.id == 1

    assert task2.id == -1
    task2.save()
    assert task2.id == 2

    assert task3.id == 55
    task3.save()
    assert task3.id == 3


def test_update_task(task1: Task):
    task1.save()
    task_id = task1.id
    task1.name = 'Refactorizar código'
    task1.done = True
    task1.update()
    assert task1.name == 'Refactorizar código'
    assert task1.done is True
    assert task1.id == task_id


def test_check_task(task1: Task, db_con: sqlite3.Connection):
    task1.save()
    assert task1.done is False
    task1.check()
    assert task1.done is True
    cur = db_con.cursor()
    result = cur.execute('SELECT * FROM tasks WHERE id=?', (task1.id,))
    assert result.fetchone()['done'] == 1


def test_uncheck_task(task2: Task, db_con: sqlite3.Connection):
    task2.save()
    assert task2.done is True
    task2.uncheck()
    assert task2.done is False
    cur = db_con.cursor()
    result = cur.execute('SELECT * FROM tasks WHERE id=?', (task2.id,))
    assert result.fetchone()['done'] == 0


def test_task_representation(task1: Task, task2: Task, task3: Task):
    task1.save()
    assert repr(task1) == '⎕ Estudiar programación (id=1)'

    task2.save()
    assert repr(task2) == '✔ Estudiar bases de datos (id=2)'

    task3.save()
    assert repr(task3) == '✔ Estudiar sistemas informáticos (id=3)'


def test_build_task_from_db_row(task1: Task, db_con: sqlite3.Connection):
    cur = db_con.cursor()
    sql = 'INSERT INTO tasks(name, done) VALUES(?, ?)'
    cur.execute(sql, (task1.name, task1.done))
    sql = 'SELECT * FROM tasks WHERE id=?'
    result = cur.execute(sql, (1,))
    row = result.fetchone()
    task1_copy = Task.from_db_row(row)
    assert task1.name == task1_copy.name
    assert task1.done == task1_copy.done


def test_get_task(task1: Task, task2: Task, task3: Task):
    TASKS = (task1, task2, task3)
    for task_id, task in enumerate(TASKS, start=1):
        task.save()
        tested_task = Task.get(task_id)
        assert task.name == tested_task.name
        assert task.done == tested_task.done
        assert task.id == tested_task.id


def test_todo_class_has_db_attrs():
    assert isinstance(ToDo.con, sqlite3.Connection)
    assert ToDo.con.row_factory == sqlite3.Row
    assert isinstance(ToDo.cur, sqlite3.Cursor)


def test_get_all_tasks(task1: Task, task2: Task, task3: Task, todo: ToDo):
    TASKS = (task1, task2, task3)
    for task in TASKS:
        task.save()
    all_tasks = todo.get_tasks()
    assert isinstance(all_tasks, typing.Generator)
    for task, tested_task in zip(TASKS, all_tasks):
        assert task.name == tested_task.name
        assert task.done == tested_task.done
        assert task.id == tested_task.id


def test_get_done_tasks(task1: Task, task2: Task, task3: Task, todo: ToDo):
    TASKS = (task1, task2, task3)
    for task in TASKS:
        task.save()
    DONE_TASKS = (task2, task3)
    all_tasks = todo.get_tasks(done=1)
    assert isinstance(all_tasks, typing.Generator)
    for task, tested_task in zip(DONE_TASKS, all_tasks):
        assert task.name == tested_task.name
        assert task.done == tested_task.done
        assert task.id == tested_task.id


def test_get_pending_tasks(task1: Task, task2: Task, task3: Task, todo: ToDo):
    TASKS = (task1, task2, task3)
    for task in TASKS:
        task.save()
    PENDING_TASKS = (task1,)
    all_tasks = todo.get_tasks(done=0)
    assert isinstance(all_tasks, typing.Generator)
    for task, tested_task in zip(PENDING_TASKS, all_tasks):
        assert task.name == tested_task.name
        assert task.done == tested_task.done
        assert task.id == tested_task.id


def test_add_task(todo: ToDo, db_con: sqlite3.Connection):
    todo.add_task('Test1')
    result = db_con.cursor().execute('SELECT * FROM tasks WHERE name=?', ('Test1',))
    assert len(result.fetchall()) == 1


def test_complete_task(todo: ToDo, task1: Task, db_con: sqlite3.Connection):
    assert task1.done is False
    task1.save()
    todo.complete_task(1)
    result = db_con.cursor().execute('SELECT * FROM tasks WHERE id=1')
    assert result.fetchone()['done'] == 1


def test_reopen_task(todo: ToDo, task2: Task, db_con: sqlite3.Connection):
    assert task2.done is True
    task2.save()
    todo.reopen_task(1)
    result = db_con.cursor().execute('SELECT * FROM tasks WHERE id=1')
    assert result.fetchone()['done'] == 0
