from math import sqrt

from shapes.figure import Figure, check_positive


class Triangle(Figure):
    """Треугольник по трём сторонам."""

    def __init__(self, a: float, b: float, c: float):
        for side in (a, b, c):
            check_positive(side, "Стороны треугольника должны быть больше нуля")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError(
                "Сумма двух сторон должна быть строго больше третьей стороны"
            )
        self.a = a
        self.b = b
        self.c = c

    @property
    def area(self) -> float:
        """Площадь по формуле Герона."""
        p = self.perimeter / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    @property
    def perimeter(self) -> float:
        return self.a + self.b + self.c
