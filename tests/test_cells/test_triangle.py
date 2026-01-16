from pytest import approx

from src.model.border.border import Border
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
    triangle2 = Triangle([p1_shared, Point((9, 9)), Point((2, 2))])

    assert set(triangle.check_neighbour(triangle1.get_corner_points())) == {p1_shared, p2_shared}
    assert triangle.check_neighbour(triangle2.get_corner_points()) is None
    assert triangle.check_neighbour(triangle.get_corner_points()) is None


def test_finalize_borders():
    triangle1 = Triangle([Point((0, 0)), Point((10, 0)), Point((5, 5))])
    triangle2 = Triangle([Point((0, 0)), Point((10, 0)), Point((5, 5))])
    triangle3 = Triangle([Point((0, 0)), Point((10, 0)), Point((5, 5))])
    border1 = Border(Point((0, 0)), Point((10, 0)), None, triangle1)
    border2 = Border(Point((0, 0)), Point((5, 5)), None, triangle1)
    border3 = Border(Point((5, 5)), Point((10, 0)), None, triangle1)
    triangle1.add_border(border1)
    triangle2.add_border(border1)
    triangle2.add_border(border2)
    triangle3.add_border(border1)
    triangle3.add_border(border2)
    triangle3.add_border(border3)

    triangle1.finalize_borders()
    triangle2.finalize_borders()
    triangle3.finalize_borders()

    assert triangle1.get_n_borders() == 3
    assert triangle2.get_n_borders() == 3
    assert triangle3.get_n_borders() == 3


def test_get_edges():
    triangle = Triangle([
        Point((0, 0)),
        Point((10, 0)),
        Point((5, 5)),
    ])

    edge1 = (Point((0, 0)), Point((10, 0)))
    edge2 = (Point((0, 0)), Point((5, 5)))
    edge3 = (Point((5, 5)), Point((10, 0)))

    expected = {normalize_edge(edge1), normalize_edge(edge2), normalize_edge(edge3)}

    result = {
        normalize_edge(edge)
        for edge in triangle.get_edges()
    }

    assert result == expected


def normalize_edge(edge):
    return tuple(
        sorted(edge, key=lambda p: (p.get_coordinates()[0], p.get_coordinates()[1]))
    )
