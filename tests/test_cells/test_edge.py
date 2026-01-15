from pytest import approx
from src.model.cells.edge import Edge
from src.model.point.point import Point
from hypothesis import given
from hypothesis.strategies import floats

point_a = Point([0, 0])
point_b = Point([1, 1])


@given(floats(min_value=-1e6, max_value=1e6))
def test_set_oil_value(oil_value):
    edge = Edge([point_a, point_b])
    edge.set_oil_value(oil_value)

    assert edge.oil_value == 0.0


@given(
    floats(allow_nan=False, allow_infinity=False),
    floats(allow_nan=False, allow_infinity=False),
    floats(allow_nan=False, allow_infinity=False),
    floats(allow_nan=False, allow_infinity=False)
)
def test_calculate_midpoint(p1_x, p2_x, p1_y, p2_y):
    point_1 = Point([p1_x, p1_y])
    point_2 = Point([p2_x, p2_y])
    cell = Edge([point_1, point_2])
    mid = cell.calculate_midpoint()

    assert mid[0] * 2 == approx(p1_x + p2_x)
    assert mid[1] * 2 == approx(p1_y + p2_y)


@given(
    floats(allow_nan=False, allow_infinity=False),
    floats(allow_nan=False, allow_infinity=False),
    floats(allow_nan=False, allow_infinity=False),
    floats(allow_nan=False, allow_infinity=False)
)
def test_calculate_flow(x_1, y_1, x_2, y_2):
    point_1 = Point([x_1, y_1])
    point_2 = Point([x_2, y_2])
    cell = Edge([point_1, point_2])
    flow = cell.calculate_flow()
    midpoint = cell.calculate_midpoint()

    assert flow[0] == approx(midpoint[1] - 0.2 * midpoint[0])
    assert flow[1] == approx(-midpoint[0])
