from shapes.figure import Figure, check_positive


class Square(Figure):
    """Квадрат."""

    def __init__(self, side: float):
        check_positive(side, "Сторона квадрата должна быть больше нуля")
        self.side = side

    @property
    def area(self) -> float:
        return self.side ** 2

    @property
    def perimeter(self) -> float:
        return 4 * self.side
