from math import pi

import pytest

from shapes import Circle, Rectangle, Square, Triangle

# Фабрика фигуры и её площадь, посчитанная вручную (не кодом проекта!).
SHAPE_CASES = {
    "circle": (lambda: Circle(1), pi),
    "rectangle": (lambda: Rectangle(2, 5), 10),
    "square": (lambda: Square(3), 9),
    "triangle": (lambda: Triangle(3, 4, 5), 6),
}


def _build(name):
    factory, expected_area = SHAPE_CASES[name]
    return factory(), expected_area


@pytest.fixture(params=SHAPE_CASES, ids=list(SHAPE_CASES))
def first_shape(request):
    """Пара (фигура, ожидаемая площадь). Перебирает все типы фигур."""
    return _build(request.param)


@pytest.fixture(params=SHAPE_CASES, ids=list(SHAPE_CASES))
def second_shape(request):
    """Вторая такая же пара: вместе с first_shape даёт все 16 комбинаций."""
    return _build(request.param)
