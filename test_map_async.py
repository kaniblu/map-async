import map_async


def square(x):
    return x * x


def test_basic():
    assert (list(map(square, range(10))) ==
            list(map_async.map_async(square, range(10), show_progress=True)))
