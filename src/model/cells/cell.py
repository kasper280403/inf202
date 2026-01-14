import itertools
from abc import ABC


class Cell(ABC):
    """
    Represents a cell of any type, parent class

    Attributes:
        cell_id (int): The cells id
        corner_points (list[Point]): Instances of the class Point
        borders (list[Border]): list with instances of Border
        oil_value (float): The amount of oil in that cell.
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

    def get_n_borders(self):
        return len(self.borders)

    def get_oil_value(self):
        return self.oil_value

    def set_oil_value(self, oil_value):
        self.oil_value = oil_value

    def has_point(self, point):
        return point in self.corner_points

    def add_border(self, border):
        self.borders.append(border)

    def get_borders(self):
        return self.borders

    def get_midpoint(self):
        return self.midpoint

    def calculate_midpoint(self):
        """
        Calculates the midpoint of the cell.
        Exctracts the x, y coordinates, from the instances Point class
        Sets the self.midpoint
        """
        x_coordinates = []
        y_coordinates = []

        for point in self.corner_points:
            x_coordinates.append(point.get_x_coordinate())
            y_coordinates.append(point.get_y_coordinate())

        x_mid = sum(x_coordinates) / len(x_coordinates)
        y_mid = sum(y_coordinates) / len(y_coordinates)

        return [x_mid, y_mid]

    def get_flow(self):
        return self.flow

    def calculate_flow(self):
        midpoint = self.midpoint
        flow_x = midpoint[1] - 0.2 * midpoint[0]
        flow_y = - midpoint[0]

        return [flow_x, flow_y]
