import numpy as np
import pytest

from src.model.border.border import Border
from src.model.point.point import Point

def test_border_vector():
    p1 = Point((0,0))
    p2 = Point((1,0))

    border = Border(p1, p2, neighbour=None)

    v = p2.get_coordinates() - p1.get_coordinates()
    n = border.get_normal()

    dot = np.dot(v, n)
    assert dot == pytest.approx(0.0)



    