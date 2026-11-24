import pytest

from shapes import Rectangle


@pytest.mark.parametrize(
    "width, height, expected_area",
    [(2, 5, 10), (5, 5, 25), (1.5, 2, 3.0)],
)
def test_rectangle_area(width, height, expected_area):
    assert Rectangle(width, height).area == pytest.approx(expected_area)


@pytest.mark.parametrize(
    "width, height, expected_perimeter",
    [(2, 5, 14), (5, 5, 20)],
)
def test_rectangle_perimeter(width, height, expected_perimeter):
    assert Rectangle(width, height).perimeter == pytest.approx(expected_perimeter)


@pytest.mark.parametrize(
    "width, height",
    [(0, 5), (5, 0), (-1, 5), (5, -1), (0, 0)],
)
def test_rectangle_invalid_sides(width, height):
    with pytest.raises(ValueError, match="Стороны прямоугольника"):
        Rectangle(width, height)
