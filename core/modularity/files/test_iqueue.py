from pathlib import Path

import pytest
from iqueue import IntegerQueue, IntegerQueueIterator


@pytest.fixture
def queue1():
    return IntegerQueue()


@pytest.fixture
def queue2():
    return IntegerQueue(max_size=2)


@pytest.fixture
def queue3():
    s = IntegerQueue(max_size=3)
    s.items = [10, 100, 1000]
    return s


@pytest.fixture
def queue4():
    s = IntegerQueue(max_size=4)
    s.items = [50, 500, 5000, 50_000]
    return s


def test_build_queue(queue1: IntegerQueue, queue2: IntegerQueue):
    assert isinstance(queue1, IntegerQueue)
    assert queue1.items == []
    assert queue1.max_size == 10

    assert isinstance(queue2, IntegerQueue)
    assert queue2.items == []
    assert queue2.max_size == 2


def test_enqueue_item(queue1: IntegerQueue):
    assert queue1.enqueue(1) is True
    assert queue1.items[0] == 1

    assert queue1.enqueue(2) is True
    assert queue1.items == [1, 2]

    assert queue1.enqueue(3) is True
    assert queue1.items == [1, 2, 3]


def test_push_item_fails_when_reaches_max_size(queue2: IntegerQueue):
    assert queue2.enqueue(1) is True
    assert queue2.items[0] == 1

    assert queue2.enqueue(2) is True
    assert queue2.items == [1, 2]

    assert queue2.enqueue(3) is False
    assert queue2.items == [1, 2]


def test_dequeue_item(queue3: IntegerQueue):
    assert queue3.dequeue() == 10
    assert queue3.dequeue() == 100
    assert queue3.dequeue() == 1000


def test_dequeue_item_fails_when_empty_queue(queue1: IntegerQueue):
    with pytest.raises(IndexError):
        queue1.dequeue()


def test_head_item(queue3: IntegerQueue):
    assert queue3.head() == 10


def test_queue_is_empty(queue1: IntegerQueue, queue3: IntegerQueue):
    assert queue1.is_empty() is True
    assert queue3.is_empty() is False


def test_queue_is_full(queue1: IntegerQueue, queue3: IntegerQueue):
    assert queue1.is_full() is False
    assert queue3.is_full() is True


def test_expand_queue(queue2: IntegerQueue):
    assert queue2.max_size == 2
    queue2.expand()
    assert queue2.max_size == 4
    queue2.expand(4)
    assert queue2.max_size == 16


def test_getitem(queue3: IntegerQueue):
    assert queue3[0] == 10
    assert queue3[1] == 100
    assert queue3[2] == 1000


def test_getitem_fails_when_out_of_range(queue3: IntegerQueue):
    with pytest.raises(IndexError):
        queue3[4]


def test_setitem(queue3: IntegerQueue):
    queue3[0] = 1
    queue3[1] = 2
    queue3[2] = 3
    assert queue3.items == [1, 2, 3]


def test_setitem_fails_when_no_item(queue1: IntegerQueue):
    with pytest.raises(IndexError):
        queue1[0] = 0


def test_queue_length(queue1: IntegerQueue, queue3: IntegerQueue):
    assert len(queue1) == 0
    assert len(queue3) == 3


def test_queue_string_representation(queue3: IntegerQueue):
    assert str(queue3) == '''10,100,1000'''


def test_add_queues(queue3: IntegerQueue, queue4: IntegerQueue):
    queue = queue3 + queue4
    assert queue.max_size == 7
    assert queue.items == [10, 100, 1000, 50, 500, 5000, 50_000]


def test_iterate_queue(queue3: IntegerQueue):
    queue_iterator = iter(queue3)
    assert isinstance(queue_iterator, IntegerQueueIterator)
    assert next(queue_iterator) == 10
    assert next(queue_iterator) == 100
    assert next(queue_iterator) == 1000
    with pytest.raises(StopIteration):
        next(queue_iterator)


def test_dump_queue_to_file(queue3: IntegerQueue):
    try:
        path = Path('queue.dat')
        queue3.dump_to_file(path)
        assert path.read_text() == str(queue3)
    except Exception as err:
        raise err
    finally:
        path.unlink(missing_ok=True)


def test_load_queue_from_file():
    try:
        path = Path('queue.dat')
        items = list(range(1, 26))
        path.write_text(','.join(str(item) for item in items))
        queue = IntegerQueue.load_from_file(path)
        assert queue.items == items
        assert queue.max_size == 40
    except Exception as err:
        raise err
    finally:
        path.unlink(missing_ok=True)
