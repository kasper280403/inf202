import pytest
from src.model.cells.triangle import Triangle
from src.model.point.point import Point

def test_triangle_area():
    p1 = Point((0, 0))
    p2 = Point((1, 0))
    p3 = Point((0, 1))

    tri = Triangle([p1, p2, p3])

    assert tri.get_area() == pytest.approx(0.5)


