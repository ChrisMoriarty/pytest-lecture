import formulas
import pytest


def test_fibonacci():
    assert formulas.fibonacci(0) == 0
    assert formulas.fibonacci(1) == 1
    assert formulas.fibonacci(2) == 1
    assert formulas.fibonacci(3) == 2
    assert formulas.fibonacci(8) == 21

    with pytest.raises(ValueError):
        formulas.fibonacci(-1)
