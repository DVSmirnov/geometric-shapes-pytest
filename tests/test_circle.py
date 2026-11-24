from math import pi

import pytest

from shapes import Circle


@pytest.mark.parametrize(
    "radius, expected_area",
    [(1, pi), (2, 4 * pi), (0.5, pi / 4)],
)
def test_circle_area(radius, expected_area):
    assert Circle(radius).area == pytest.approx(expected_area)


@pytest.mark.parametrize(
    "radius, expected_perimeter",
    [(1, 2 * pi), (5, 10 * pi)],
)
def test_circle_perimeter(radius, expected_perimeter):
    assert Circle(radius).perimeter == pytest.approx(expected_perimeter)


@pytest.mark.parametrize("radius", [0, -1, -0.1])
def test_circle_invalid_radius(radius):
    with pytest.raises(ValueError, match="Радиус"):
        Circle(radius)
