import pytest
import numpy as np
from src.model.border.border import Border
from src.model.point.point import Point
from src.model.cells.triangle import Triangle


test_data = [([0, 0], [1, 0], [0, 1]),
             ([0, 1], [0, 0], [1, 0]),
             ([1, 0], [0, 1], [0, 0]),
             ([0.3, 0.3], [0.1, 0.8], [0.5, 0.5]),
             ([0.5, 0.5], [0.3, 0.3], [0.1, 0.8]),
             ([0.1, 0.8], [0.5, 0.5], [0.3, 0.3])]


@pytest.fixture(params=test_data)
def create_Borders(request):
    point1, point2, point3 = request.param
    p1 = Point(point1)
    p2 = Point(point2)
    p3 = Point(point3)
    tri = Triangle([p1, p2, p3])
    border = Border(p1, p2, None, tri)
    v = p2.get_coordinates() - p1.get_coordinates()
    n = border.get_normal()
    return n, v, border, tri, p1


def test_border_normal(create_Borders):
    n, v, border, tri, p1 = create_Borders
    dot = np.dot(v, n)
    assert dot == pytest.approx(0.0)


def test_normal_length(create_Borders):
    n, v, border, tri, p1 = create_Borders
    len_v = np.sqrt(v[0]**2+v[1]**2)
    len_n = np.sqrt(n[0]**2+n[1]**2)
    assert len_v == pytest.approx(len_n)


def test_normal_dir(create_Borders):
    n, v, border, tri, p1 = create_Borders
    tri_mid = tri.get_midpoint()
    mid_p1 = p1.get_coordinates() - tri_mid
    theta = np.arccos(np.inner(n, mid_p1) /
                      (np.linalg.norm(mid_p1)*np.linalg.norm(n)))
    assert theta < np.pi/2
