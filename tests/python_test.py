def test_array():
    a = [1, 2, 3]
    b = a
    b[1] = 100
    c = a

    assert c[1] == 100

    try:
        _ = c.index(2)
    except ValueError as err:
        print(err)
    else:
        assert False


def test_array_deepcopy():
    a = [1, 2, 3]
    from copy import deepcopy

    b = deepcopy(a)
    b[1] = 100
    c = deepcopy(a)

    assert c[1] != 100

    try:
        _ = c.index(2)
    except ValueError as err:
        print(err)
        assert False
    else:
        assert True
