from abc import ABC, abstractmethod


class Figure(ABC):
    """Базовый класс геометрической фигуры."""

    @property
    @abstractmethod
    def area(self) -> float:
        """Площадь фигуры."""

    @property
    @abstractmethod
    def perimeter(self) -> float:
        """Периметр фигуры."""

    def add_area(self, other: "Figure") -> float:
        """Возвращает сумму площадей этой и другой фигуры."""
        if not isinstance(other, Figure):
            raise TypeError("Передана не геометрическая фигура")
        return self.area + other.area


def check_positive(value: float, message: str) -> None:
    """Бросает ValueError, если значение не больше нуля."""
    if value <= 0:
        raise ValueError(message)
