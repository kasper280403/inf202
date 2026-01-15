import pytest
import numpy as np

from src.model.point.point import Point

def test_point_equality():
    p1 = Point((1, 2))
    p2 = Point((1, 2))

    assert p1 == p2


def test_point_hashing():
    p1 = Point((1, 2))
    p2 = Point((1, 2))

    s = {p1, p2}

    assert len(s) == 1

def test_point_get_coordinates():
    p = Point((3, 4))
    coord = p.get_coordinates()
        

    assert np.array_equal(coord, np.array([3, 4]))

