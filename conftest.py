import pytest
import math


@pytest.fixture
def area_triangle():
    p = (10 + 10 + 10) / 2
    return (p * (p - 10) * (p - 10) * (p - 10)) ** 0.5


@pytest.fixture
def area_circle():
    math.pi * 10 ** 2
    return math.pi * 10 ** 2