from math_series import __version__
from math_series.math_series import fibonacci, lucas, sum_series


def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci():
    expected_0 = 0
    expected_1 = 1
    expected_2 = 1
    expected_3 = 2
    expected_4 = 3
    expected_5 = 5
    expected_6 = 8
    expected_7 = 13

    actual_0 = fibonacci(0)
    actual_1 = fibonacci(1)
    actual_2 = fibonacci(2)
    actual_3 = fibonacci(3)
    actual_4 = fibonacci(4)
    actual_5 = fibonacci(5)
    actual_6 = fibonacci(6)
    actual_7 = fibonacci(7)

    assert actual_0 == expected_0
    assert actual_1 == expected_1
    assert actual_2 == expected_2
    assert actual_3 == expected_3
    assert actual_4 == expected_4
    assert actual_5 == expected_5
    assert actual_6 == expected_6
    assert actual_7 == expected_7


def test_lucas():
    expected_0 = 2
    expected_1 = 1
    expected_2 = 3
    expected_3 = 4
    expected_4 = 7
    expected_5 = 11
    expected_6 = 18
    expected_7 = 29

    actual_0 = lucas(0)
    actual_1 = lucas(1)
    actual_2 = lucas(2)
    actual_3 = lucas(3)
    actual_4 = lucas(4)
    actual_5 = lucas(5)
    actual_6 = lucas(6)
    actual_7 = lucas(7)

    assert actual_0 == expected_0
    assert actual_1 == expected_1
    assert actual_2 == expected_2
    assert actual_3 == expected_3
    assert actual_4 == expected_4
    assert actual_5 == expected_5
    assert actual_6 == expected_6
    assert actual_7 == expected_7


def test_sum_series():
    expected_fibo_0 = 0
    expected_fibo_1 = 1
    expected_fibo_2 = 1

    expected_lucas_0 = 2
    expected_lucas_1 = 1
    expected_lucas_2 = 3


    actual_fibo_0 = sum_series(0)
    actual_fibo_1 = sum_series(1)
    actual_fibo_2 = sum_series(2)

    actual_lucas_0 = sum_series(0, 2, 1)
    actual_lucas_1 = sum_series(1, 2, 1)
    actual_lucas_2 = sum_series(2, 2, 1)


    assert actual_fibo_0 == expected_fibo_0 
    assert actual_fibo_1 == expected_fibo_1
    assert actual_fibo_2 == expected_fibo_2
    assert actual_lucas_0 == expected_lucas_0
    assert actual_lucas_1 == expected_lucas_1
    assert actual_lucas_2 == expected_lucas_2


def test_other_series():
    expected_0 = 3
    expected_1 = 5
    expected_2 = 8

    actual_0 = sum_series(0, 3, 5)
    actual_1 = sum_series(1, 3, 5)
    actual_2 = sum_series(2, 3, 5)

    assert actual_0 == expected_0
    assert actual_1 == expected_1
    assert actual_2 == expected_2