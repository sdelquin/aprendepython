from pathlib import Path

import pytest
from istack import IntegerStack, IntegerStackIterator


@pytest.fixture
def stack1():
    return IntegerStack()


@pytest.fixture
def stack2():
    return IntegerStack(max_size=2)


@pytest.fixture
def stack3():
    s = IntegerStack(max_size=3)
    s.items = [10, 100, 1000]
    return s


@pytest.fixture
def stack4():
    s = IntegerStack(max_size=4)
    s.items = [50, 500, 5000, 50_000]
    return s


def test_build_stack(stack1: IntegerStack, stack2: IntegerStack):
    assert isinstance(stack1, IntegerStack)
    assert stack1.items == []
    assert stack1.max_size == 10

    assert isinstance(stack2, IntegerStack)
    assert stack2.items == []
    assert stack2.max_size == 2


def test_push_item(stack1: IntegerStack):
    assert stack1.push(1) is True
    assert stack1.items[0] == 1

    assert stack1.push(2) is True
    assert stack1.items == [2, 1]

    assert stack1.push(3) is True
    assert stack1.items == [3, 2, 1]


def test_push_item_fails_when_reaches_max_size(stack2: IntegerStack):
    assert stack2.push(1) is True
    assert stack2.items[0] == 1

    assert stack2.push(2) is True
    assert stack2.items == [2, 1]

    assert stack2.push(3) is False
    assert stack2.items == [2, 1]


def test_pop_item(stack3: IntegerStack):
    assert stack3.pop() == 10
    assert stack3.pop() == 100
    assert stack3.pop() == 1000


def test_pop_item_fails_when_empty_stack(stack1: IntegerStack):
    with pytest.raises(IndexError):
        stack1.pop()


def test_top_item(stack3: IntegerStack):
    assert stack3.top() == 10


def test_stack_is_empty(stack1: IntegerStack, stack3: IntegerStack):
    assert stack1.is_empty() is True
    assert stack3.is_empty() is False


def test_stack_is_full(stack1: IntegerStack, stack3: IntegerStack):
    assert stack1.is_full() is False
    assert stack3.is_full() is True


def test_expand_stack(stack2: IntegerStack):
    assert stack2.max_size == 2
    stack2.expand()
    assert stack2.max_size == 4
    stack2.expand(4)
    assert stack2.max_size == 16


def test_getitem(stack3: IntegerStack):
    assert stack3[0] == 10
    assert stack3[1] == 100
    assert stack3[2] == 1000


def test_getitem_fails_when_out_of_range(stack3: IntegerStack):
    with pytest.raises(IndexError):
        stack3[4]


def test_setitem(stack3: IntegerStack):
    stack3[0] = 1
    stack3[1] = 2
    stack3[2] = 3
    assert stack3.items == [1, 2, 3]


def test_setitem_fails_when_no_item(stack1: IntegerStack):
    with pytest.raises(IndexError):
        stack1[0] = 0


def test_stack_length(stack1: IntegerStack, stack3: IntegerStack):
    assert len(stack1) == 0
    assert len(stack3) == 3


def test_stack_string_representation(stack3: IntegerStack):
    assert (
        str(stack3)
        == '''10
100
1000'''
    )


def test_add_stacks(stack3: IntegerStack, stack4: IntegerStack):
    stack = stack3 + stack4
    assert stack.max_size == 7
    assert stack.items == [50, 500, 5000, 50_000, 10, 100, 1000]


def test_iterate_stack(stack3: IntegerStack):
    stack_iterator = iter(stack3)
    assert isinstance(stack_iterator, IntegerStackIterator)
    assert next(stack_iterator) == 10
    assert next(stack_iterator) == 100
    assert next(stack_iterator) == 1000
    with pytest.raises(StopIteration):
        next(stack_iterator)


def test_dump_stack_to_file(stack3: IntegerStack):
    try:
        path = Path('stack.dat')
        stack3.dump_to_file(path)
        assert path.read_text() == str(stack3)
    except Exception as err:
        raise err
    finally:
        path.unlink(missing_ok=True)


def test_load_stack_from_file():
    try:
        path = Path('stack.dat')
        items = list(range(1, 26))
        path.write_text('\n'.join(str(item) for item in items))
        stack = IntegerStack.load_from_file(path)
        assert stack.items == items
        assert stack.max_size == 40
    except Exception as err:
        raise err
    finally:
        path.unlink(missing_ok=True)
