import pytest

import formulas

test_data = [(0, 0),
             (1, 1),
             (2, 1),
             (3, 2),
             (4, 3),
             (5, 5),
             (6, 7),
             (7, 13),
             (8, 21)]


@pytest.mark.parametrize("test_input,expected", test_data)
def test_fibonacci(test_input, expected):
    assert formulas.fibonacci(test_input) == expected


def test_fibonacci_negative():
    with pytest.raises(ValueError):
        formulas.fibonacci(-1)
