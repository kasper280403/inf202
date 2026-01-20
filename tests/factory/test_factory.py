import pytest

from src.model.factory.factory import Factory
from src.model.point.point import Point
from src.model.cells.triangle import Triangle
from src.model.cells.edge import Edge
from src.model.cells.cell import Cell


def make_points(n):
    """
    Creates a list of n Point instances with simple coordinates.
    """
    return [Point((i, i)) for i in range(n)]


def test_create_triangle():
    """
    Test that Factory creates a Triangle when cell_type is 'triangle'. 
    """
    points = make_points(3)

    cell = Factory.create_cell("triangle", corner_points=points)

    assert isinstance(cell, Triangle)
    assert isinstance(cell, Cell)


def test_create_edge():
    """
    Test that Factory creates on a Edge when cell_type is 'edge'. 
    """
    points = make_points(2)

    cell = Factory.create_cell("edge", corner_points=points)

    assert isinstance(cell, Edge)
    assert isinstance(cell, Cell)


def test_factory_passes_arguments_correctly():
    """
    Test that Factory forwards constructor arguments to create cells.
    """
    points = make_points(3)

    cell = Factory.create_cell("triangle", corner_points=points)

    assert cell.get_corner_points() is points
    

def test_uknown_cell_type_raises_key_error():
    """
    Test that Factory raises KeyError for unknown cell types.
    """
    points = make_points(3)

    with pytest.raises(KeyError):
        Factory.create_cell("unknown_type", corner_points=points)