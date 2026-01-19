import pytest
import numpy as np

from src.model.point.point import Point

# chosen few point coordinates that include int, float and negative numbers
test_data = [[1, 2], [2, 1], [0.2, 0.1], [1, 1], [-1, 1], [-0.5, -0.1]]


@pytest.mark.parametrize('point', test_data)
def test_point_equality(point):
    """
    Test equality function in Point class
    """
    p1 = Point(point)
    p2 = Point(point)

    assert p1 == p2


@pytest.mark.parametrize('point', test_data)
def test_point_hashing(point):
    """
    Test hashing function in Point class
    """
    p1 = Point(point)
    p2 = Point(point)

    s = {p1, p2}

    assert len(s) == 1


@pytest.mark.parametrize('point', test_data)
def test_point_get_coordinates(point):
    p = Point(point)
    coord = p.get_coordinates()

    assert np.array_equal(coord, np.array(point))
