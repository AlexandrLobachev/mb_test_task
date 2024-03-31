import abc
import math


class Figure(abc.ABC):
    """Базовый класс геометрической фигуры."""

    @abc.abstractmethod
    def get_area(self):
        """Вычислить площадь фигуры."""
        pass

    def check_args(self, *args):
        """Проверка параметров геометрической фигуры."""
        for param in args:
            if type(param) not in (int, float):
                raise TypeError("Не верный тип данных!")
            if param <= 0:
                raise ValueError("Параметр фигуры не может быть меньше или равен 0!")


class Triangle(Figure):
    """Класс треугольника."""

    def __init__(self, side_a, side_b, side_c):
        self.sides = (side_a, side_b, side_c)
        self.check_args(*self.sides)
        self.check_exist_triangle()

    def check_exist_triangle(self):
        """Проверка существования треугольника."""
        side_a = self.sides[0]
        side_b = self.sides[1]
        side_c = self.sides[2]
        if (side_a + side_b <= side_c
                or side_a + side_c <= side_b
                or side_b + side_c <= side_a):
            raise ValueError("Треугольник не существует!")

    def get_area(self) -> float:
        p = sum(self.sides) / 2
        return math.sqrt(math.prod([p] + [p - s for s in self.sides]))

    def is_right_triangle(self)-> bool:
        """Являеться ли треугольник прямоугольным."""
        side_a = self.sides[0]
        side_b = self.sides[1]
        side_c = self.sides[2]
        return (side_c ** 2 == side_a ** 2 + side_b ** 2
            or side_a ** 2 == side_b ** 2 + side_c ** 2
            or side_b ** 2 == side_a ** 2 + side_c ** 2)


class Circle(Figure):
    """Класс окружности."""
    def __init__(self, radius):
        self.radius = radius
        self.check_args(self.radius)

    def get_area(self) -> float:
        return math.pi * self.radius ** 2
