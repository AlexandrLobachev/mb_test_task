import pytest

from geometria import Triangle, Circle


def test_triangle_empty():
    with pytest.raises(TypeError):
        Triangle()
    with pytest.raises(TypeError):
        Triangle(1)
    with pytest.raises(TypeError):
        Triangle(1, 2)


def test_triangle_wrong_args():
    with pytest.raises(TypeError):
        Triangle([1], 2, 2)
    with pytest.raises(TypeError):
        Triangle({1}, 2, 2)
    with pytest.raises(TypeError):
        Triangle('1', 2, 2)
    with pytest.raises(TypeError):
        Triangle(1, 2, 2, 2)


def test_triangle_not_exist():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)
    with pytest.raises(ValueError):
        Triangle(0, 2, 2)
    with pytest.raises(ValueError):
        Triangle(-1, 2, 2)


def test_triangle_correct():
    assert Triangle(1, 2, 2).__class__ == Triangle


def test_triangle_area(area_triangle):
    assert Triangle(10, 10, 10).get_area() == area_triangle


def test_right_triangle():
    assert Triangle(6, 8, 10).is_right_triangle() == True
    assert Triangle(10, 6, 8).is_right_triangle() == True
    assert Triangle(8, 10, 6).is_right_triangle() == True


def test_not_right_triangle():
    assert Triangle(6, 6, 10).is_right_triangle() == False


def test_circle_empty():
    with pytest.raises(TypeError):
        Circle()


def test_circle_wrong_arg():
    with pytest.raises(TypeError):
        Circle([1])
    with pytest.raises(TypeError):
        Circle({1})
    with pytest.raises(TypeError):
        Circle('1')
    with pytest.raises(TypeError):
        Circle(1, 2)


def test_circle_not_exist():
    with pytest.raises(ValueError):
        Circle(0)
    with pytest.raises(ValueError):
        Circle(-1)


def test_circle_correct():
    assert Circle(1).__class__ == Circle


def test_circle_area(area_circle):
    assert Circle(10).get_area() == area_circle
