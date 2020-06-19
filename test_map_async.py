import itertools
import map_async


def square(x):
    return x * x


def add(a, b):
    return a + b


def test_basic():
    assert (list(map(square, range(10))) ==
            list(map_async.map_async(square, range(10), show_progress=True)))


def test_starmap():
    items = list(zip(range(10), range(10, 20)))
    assert (list(itertools.starmap(add, items)) ==
            list(map_async.starmap_async(add, items, show_progress=True)))
