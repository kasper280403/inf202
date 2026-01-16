import itertools
from abc import ABC


class Cell(ABC):
    """
    Represents a cell of any type, parent class

    Attributes:
        cell_id (int): The cells id
        corner_points (list[Point]): Instances of the class Point
        oil_value (float): The amount of oil in that cell.
        midpoint (list[float]): Midpoint of the triangle. x and y coordinates.
        flow (list[float]): Flow of the water at the midpoint, x, y vector.
        borders (list[Border]): list with instances of Border
    """
    id_counter = itertools.count()

    def __init__(self, corner_points):
        self.cell_id = next(self.id_counter)
        self.corner_points = corner_points
        self.oil_value = 0.0
        self.midpoint = self.calculate_midpoint()
        self.flow = self.calculate_flow()
        self.borders = []

    def get_id(self):
        return self.cell_id

    def get_corner_points(self):
        return self.corner_points

    def get_oil_value(self):
        return self.oil_value

    def set_oil_value(self, oil_value):
        self.oil_value = oil_value

    def add_border(self, border):
        self.borders.append(border)

    def get_borders(self):
        return self.borders

    def get_midpoint(self):
        return self.midpoint

    def get_flow(self):
        return self.flow

    def get_n_borders(self):
        """
        Returns the number of borders in the cell.

        Returns:
            int: The number of borders in the cell.
        """
        return len(self.borders)

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

        for point in self.corner_points:
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
        midpoint = self.midpoint
        flow_x = midpoint[1] - 0.2 * midpoint[0]
        flow_y = - midpoint[0]

        return [flow_x, flow_y]
