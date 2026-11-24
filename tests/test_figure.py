import pytest

from shapes import Figure


def test_figure_is_abstract():
    with pytest.raises(TypeError):
        Figure()


def test_add_area_for_all_pairs(first_shape, second_shape):
    first, first_area = first_shape
    second, second_area = second_shape

    assert first.add_area(second) == pytest.approx(first_area + second_area)


def test_add_area_is_commutative(first_shape, second_shape):
    first, _ = first_shape
    second, _ = second_shape

    assert first.add_area(second) == pytest.approx(second.add_area(first))


@pytest.mark.parametrize("not_a_figure", ["str", 5, 3.14, None, [1, 2]])
def test_add_area_rejects_non_figure(first_shape, not_a_figure):
    shape, _ = first_shape

    with pytest.raises(TypeError, match="не геометрическая фигура"):
        shape.add_area(not_a_figure)
