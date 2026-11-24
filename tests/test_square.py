import pytest

from shapes import Square


@pytest.mark.parametrize("side, expected_area", [(1, 1), (7, 49), (2.5, 6.25)])
def test_square_area(side, expected_area):
    assert Square(side).area == pytest.approx(expected_area)


@pytest.mark.parametrize("side, expected_perimeter", [(1, 4), (7, 28)])
def test_square_perimeter(side, expected_perimeter):
    assert Square(side).perimeter == pytest.approx(expected_perimeter)


@pytest.mark.parametrize("side", [0, -5, -0.1])
def test_square_invalid_side(side):
    with pytest.raises(ValueError, match="Сторона квадрата"):
        Square(side)
