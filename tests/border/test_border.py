import pytest
import numpy as np
from src.model.border.border import Border
from src.model.point.point import Point
from src.model.cells.triangle import Triangle

# points in 2 triangles, where the points move location at a time
test_data = [([0, 0], [1, 0], [0, 1], 1),  # p1, p2, p3
             ([0, 1], [0, 0], [1, 0], 2),  # p3, p1, p2
             ([1, 0], [0, 1], [0, 0], 3),  # p2, p3, p1
             # using floats:
             ([0.3, 0.3], [0.1, 0.8], [0.5, 0.5], 4),
             ([0.5, 0.5], [0.3, 0.3], [0.1, 0.8], 5),
             ([0.1, 0.8], [0.5, 0.5], [0.3, 0.3], 6)]


@pytest.fixture(params=test_data)
def create_Borders(request):
    """
    parameterized fixture to create the borders with all the
    points, normals, and coresponding triangle.
    """
    point1, point2, point3, neigbour = request.param
    p1 = Point(point1)
    p2 = Point(point2)
    p3 = Point(point3)
    tri = Triangle([p1, p2, p3])
    border = Border(p1, p2, neigbour, tri)
    v = p2.get_coordinates() - p1.get_coordinates()
    n = border.get_normal()
    return n, v, border, tri, [p1, p2, p3], neigbour


def test_border_normal(create_Borders):
    """
    Test to check if normal matches the current edge and that it is a normal
    """
    n, v, *_ = create_Borders
    dot = np.dot(v, n)
    assert dot == pytest.approx(0.0)


def test_normal_length(create_Borders):
    """
    Test to check if the length of the normal vector matches the side length
    """
    n, v, *_ = create_Borders
    len_v = np.sqrt(v[0]**2+v[1]**2)
    len_n = np.sqrt(n[0]**2+n[1]**2)
    assert len_v == pytest.approx(len_n)


def test_normal_direction(create_Borders):
    """
    Test to check if the normal vector is facing out of the triangle
    """
    n, _, _, tri, points, _ = create_Borders
    p1 = points[0]
    tri_mid = tri.get_midpoint()
    mid_p1 = p1.get_coordinates() - tri_mid
    theta = np.arccos(np.inner(n, mid_p1) /
                      (np.linalg.norm(mid_p1)*np.linalg.norm(n)))
    assert theta < np.pi/2


def test_neighbours(create_Borders):
    """
    Test to check if the correct neighbour gets returned
    """
    result = create_Borders
    border = result[2]
    neighbour = result[5]
    assert border.get_neighbour() == neighbour
