import numpy as np


class Point:
    """
    Represents a 2D point in the mesh

    Attributes:
        _x (float): x coordinate of this point
        _y (float): y coordinate of this point
    """

    def __init__(self, cord):
        self._x = cord[0]
        self._y = cord[1]

    def get_coordinates(self):
        """
        Returns:
            np.array(float): Coordinates as a numpy array
        """
        return np.array([self._x, self._y])

    def get_y_coordinate(self) -> float:
        return self._y

    def get_x_coordinate(self) -> float:
        return self._x

    def __eq__(self, other):
        """
        Determine whether this Point is equal to another object.
        Two Point instances are considered equal if their _x and _y
        coordinates have the same values.

        Returns:
            bool: True if the points are equal, False otherwise.
            NotImplemented: If the other object is not an instance of Point.
        """
        if not isinstance(other, Point):
            return NotImplemented
        return self._x == other._x and self._y == other._y

    def __hash__(self):
        """
        Compute a hash value for this Point.
        The hash is based on the _x, _y values
        Ensuring correct behavior when Point instances are used in hash-based
        collections(sets or dictionaries).

        Returns:
            int: The hash value
        """
        return hash((self._x, self._y))
