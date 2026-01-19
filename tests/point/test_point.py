import pytest
import numpy as np

from src.model.point.point import Point

# chosen few point coordinates that include int, float and negative numbers
test_data = [[1, 2], [2, 1], [0.2, 0.1], [-1, 1], [-0.5, -0.1]]


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
    """
    Test function to get coordinates from point class
    """
    p = Point(point)
    coord = p.get_coordinates()

    assert np.array_equal(coord, np.array(point))


@pytest.mark.parametrize('point', test_data)
def test_point_get_x_coordinate(point):
    """
    Test function to get x coordinates from point class
    """
    p = Point(point)
    x = p.get_x_coordinate()

    assert x == pytest.approx(point[0])


@pytest.mark.parametrize('point', test_data)
def test_point_get_y_coordinate(point):
    """
    Test function to get y coordinates from point class
    """
    p = Point(point)
    y = p.get_y_coordinate()
    assert y == pytest.approx(point[1])
