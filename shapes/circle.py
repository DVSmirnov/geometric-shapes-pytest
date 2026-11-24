from math import pi

from shapes.figure import Figure, check_positive


class Circle(Figure):
    """Круг."""

    def __init__(self, radius: float):
        check_positive(radius, "Радиус должен быть больше нуля")
        self.radius = radius

    @property
    def area(self) -> float:
        return pi * self.radius ** 2

    @property
    def perimeter(self) -> float:
        return 2 * pi * self.radius
