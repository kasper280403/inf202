import numpy as np


class Point:
    """
    Represents a 2D point in the mesh

    Attributes:
        _x (int): x coordinate of this point
        _y (int): y coordinate of this point
    """

    def __init__(self, cord):
        """Creates a point from a coordinate pair x and y"""
        self._x = cord[0]
        self._y = cord[1]

    def get_coordinates(self):
        """Returns coordinates as a numpy array"""
        return np.array([self._x, self._y])

    def get_y_coordinate(self) -> float:
        """Returns the y coordinate"""
        return self._y

    def get_x_coordinate(self) -> float:
        """Returns the x coordinate"""
        return self._x

    def __eq__(self, other):
        """Points are equal if x and y coordinates are equal"""
        if not isinstance(other, Point):
            return NotImplemented
        return self._x == other._x and self._y == other._y

    def __hash__(self):
        """Hash based on x and y coordinates are equal"""
        return hash((self._x, self._y))
