import numpy as np
import pytest

from src.model.border.border import Border
from src.model.point.point import Point
from src.model.cells.triangle import Triangle


def test_border_vector():
    p1 = Point((0, 0))
    p2 = Point((1, 0))
    p3 = Point((0, 1))
    tri = Triangle([p1, p2, p3])

    border = Border(p1, p2, None, tri)

    v = p2.get_coordinates() - p1.get_coordinates()
    n = border.get_normal()

    dot = np.dot(v, n)
    assert dot == pytest.approx(0.0)


