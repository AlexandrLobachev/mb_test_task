import pytest

from geometria import Triangle, Circle


def test_triangle_empty():
    with pytest.raises(TypeError):
        Triangle()


def test_triangle_with_one_arg():
    with pytest.raises(TypeError):
        Triangle(1)


def test_triangle_with_two_args():
    with pytest.raises(TypeError):
        Triangle(1, 2)


def test_triangle_with_four_args():
    with pytest.raises(TypeError):
        Triangle(1, 2, 2, 2)


def test_triangle_list_in_args():
    with pytest.raises(TypeError):
        Triangle([1], 2, 2)


def test_triangle_dict_in_args():
    with pytest.raises(TypeError):
        Triangle({1}, 2, 2)


def test_triangle_str_in_args():
    with pytest.raises(TypeError):
        Triangle('1', 2, 2)


def test_triangle_not_exist():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)


def test_triangle_side_is_null():
    with pytest.raises(ValueError):
        Triangle(0, 2, 2)


def test_triangle_side_is_negative():
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


def test_circle_list_in_arg():
    with pytest.raises(TypeError):
        Circle([1])


def test_circle_dict_in_arg():
    with pytest.raises(TypeError):
        Circle({1})


def test_circle_str_in_arg():
    with pytest.raises(TypeError):
        Circle('1')


def test_circle_with_two_args():
    with pytest.raises(TypeError):
        Circle(1, 2)


def test_circle_radius_is_null():
    with pytest.raises(ValueError):
        Circle(0)


def test_circle_negative_radius():
    with pytest.raises(ValueError):
        Circle(-1)


def test_circle_correct():
    assert Circle(1).__class__ == Circle


def test_circle_area(area_circle):
    assert Circle(10).get_area() == area_circle
