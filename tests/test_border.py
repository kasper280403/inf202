import pytest
import numpy as np

from src.model.border.border import Border
from src.model.point.point import Point
from src.model.cells.triangle import Triangle


@pytest.mark.parametrize("point1, point2, point3",
                         [([0, 0], [1, 0], [0, 1]),
                          ([0.2, 0.4], [1, 1], [0, 0]),
                          ([1, 1], [0, 1], [0.5, 0.5]),
                          ([0.4, .3], [0.1, 0.8], [0.2, 0.5])])
def test_border_vector():
    p1 = Point(point1)
    p2 = Point(point2)
    p3 = Point(point3)
    tri = Triangle([p1, p2, p3])

    border = Border(p1, p2, None, tri)

    v = p2.get_coordinates() - p1.get_coordinates()
    n = border.get_normal()

    dot = np.dot(v, n)
    assert dot == pytest.approx(0.0)
