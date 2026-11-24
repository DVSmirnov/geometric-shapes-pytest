from math import sqrt

import pytest

from shapes import Triangle


@pytest.mark.parametrize(
    "a, b, c, expected_area",
    [
        (3, 4, 5, 6),                    # прямоугольный
        (13, 14, 15, 84),                # разносторонний
        (10, 10, 10, 25 * sqrt(3)),      # равносторонний
    ],
)
def test_triangle_area(a, b, c, expected_area):
    assert Triangle(a, b, c).area == pytest.approx(expected_area)


@pytest.mark.parametrize(
    "a, b, c, expected_perimeter",
    [(3, 4, 5, 12), (10, 10, 10, 30)],
)
def test_triangle_perimeter(a, b, c, expected_perimeter):
    assert Triangle(a, b, c).perimeter == pytest.approx(expected_perimeter)


@pytest.mark.parametrize(
    "a, b, c",
    [(0, 1, 1), (-1, 1, 1), (10, 10, -10), (10, 10, 0)],
)
def test_triangle_non_positive_side(a, b, c):
    with pytest.raises(ValueError, match="должны быть больше нуля"):
        Triangle(a, b, c)


@pytest.mark.parametrize(
    "a, b, c",
    [
        (5, 15, 25),   # одна сторона больше суммы двух других
        (1, 2, 10),
        (2, 3, 5),     # вырожденный: сумма равна третьей стороне
        (5, 5, 10),
    ],
)
def test_triangle_inequality_violated(a, b, c):
    with pytest.raises(ValueError, match="строго больше"):
        Triangle(a, b, c)
