from shapes.figure import Figure, check_positive


class Rectangle(Figure):
    """Прямоугольник."""

    def __init__(self, width: float, height: float):
        check_positive(width, "Стороны прямоугольника должны быть больше нуля")
        check_positive(height, "Стороны прямоугольника должны быть больше нуля")
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
