from pytest import approx
from src.model.cells.triangle import Triangle
from src.model.point.point import Point
from hypothesis import given
from hypothesis.strategies import integers
from hypothesis.strategies import floats


@given(
    floats(-1e6, 1e6),
    floats(-1e6, 1e6),
    floats(-1e6, 1e6),
    floats(-1e6, 1e6),
    floats(-1e6, 1e6),
    floats(-1e6, 1e6),
)
def test_calculate_area(x1, y1, x2, y2, x3, y3):
    p1 = Point((x1, y1))
    p2 = Point((x2, y2))
    p3 = Point((x3, y3))
    tri = Triangle([p1, p2, p3])
    expected = approx(abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)

    assert tri.get_area() == expected


def test_caculate_area_direct():
    triangle = Triangle([Point((0, 0)), Point((0, 5)), Point((5, 0))])
    triangle1 = Triangle([Point((0, 0)), Point((0, 10)), Point((5, 5))])
    triangle2 = Triangle([Point((0, 0)), Point((0, -5)), Point((5, 0))])
    assert triangle.get_area() == approx(12.5)
    assert triangle1.get_area() == approx(25)
    assert triangle2.get_area() == approx(12.5)


def test_check_neighbour():
    p1_shared = Point((0, 0))
    p2_shared = Point((9, 5))
    triangle = Triangle([p1_shared, p2_shared, Point((17, 3))])
    triangle1 = Triangle([p1_shared, p2_shared, Point((1, 1))])
    triangle2 = Triangle([p1_shared, Point((9,9)), Point((2, 2))])

    assert set(triangle.check_neighbour(triangle1.get_corner_points())) == {p1_shared, p2_shared}
    assert triangle.check_neighbour(triangle2.get_corner_points()) is None
    assert triangle.check_neighbour(triangle.get_corner_points()) is None
