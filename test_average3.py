def test_add_three():
    from average3 import add_three
    s = add_three(1, 1, 10)
    assert s == 12


def test_divide_three():
    from average3 import divide_three
    d = divide_three(12)
    assert d == 4
