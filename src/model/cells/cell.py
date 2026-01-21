import itertools
from abc import ABC


class Cell(ABC):
    """
    Represents a cell of any type, parent class

    Attributes:
        _cell_id (int): The cells id
        _corner_points (list[Point]): Instances of the class Point
        _oil_value (float): The amount of oil in that cell.
        _midpoint (list[float]): Midpoint of the triangle. x and y coordinates.
        _flow (list[float]): Flow of the water at the midpoint, x, y vector.
        _borders (list[Border]): list with instances of Border
    """
    id_counter = itertools.count()

    def __init__(self, corner_points):
        self._cell_id = next(self.id_counter)
        self._corner_points = corner_points
        self._oil_value = 0.0
        self._midpoint = self.calculate_midpoint()
        self._flow = self.calculate_flow()
        self._borders = []

    def get_id(self):
        return self._cell_id

    def get_corner_points(self):
        return self._corner_points

    def get_oil_value(self):
        return self._oil_value

    def set_oil_value(self, oil_value):
        self._oil_value = oil_value

    def add_border(self, border):
        self._borders.append(border)

    def get_borders(self):
        return self._borders

    def get_midpoint(self):
        return self._midpoint

    def get_flow(self):
        return self._flow

    def get_n_borders(self):
        """
        Counts the number of borders belonging to the cell.

        Returns:
            int: The number of borders in the cell.
        """
        return len(self._borders)

    def calculate_midpoint(self):
        """
        Calculates the midpoint of the cell.
        Exctracts the x, y coordinates, from the instances Point class
        Sets the self.midpoint

        Returns:
            list[float]: The midpoint of the cell, x, y coordinates.
        """
        x_coordinates = []
        y_coordinates = []

        for point in self._corner_points:
            x_coordinates.append(point.get_x_coordinate())
            y_coordinates.append(point.get_y_coordinate())

        x_mid = sum(x_coordinates) / len(x_coordinates)
        y_mid = sum(y_coordinates) / len(y_coordinates)

        return [x_mid, y_mid]

    def calculate_flow(self):
        """
        Calculates the flow of the cell.

        Returns:
            list[float]: The flow of the cell, x, y vector.
        """
        midpoint = self._midpoint
        flow_x = midpoint[1] - 0.2 * midpoint[0]
        flow_y = - midpoint[0]

        return [flow_x, flow_y]
