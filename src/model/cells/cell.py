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
        self.neighbors = []
        self.oil_value = 0.0
        self.flux = None
        self.type = None
        self.borders = []

    def get_id(self):
        return self.cell_id

    def get_corner_points(self):
        return self.corner_points

    def get_neighbors(self):
        return self.neighbors

    def get_n_neighbors(self):
        return len(self.neighbors)

    def get_oil_value(self):
        return self.oil_value

    def get_type(self):
        return self.type

    def add_neighbor(self, neighbor, p1, p2):
        self.neighbors.append([neighbor, p1, p2])

    def set_oil_value(self, oil_value):
        self.oil_value = oil_value

    def has_point(self, point):
        return point in self.corner_points

    def add_border(self, border):
        self.borders.append(border)

    def get_borders(self):
        return self.borders

    def clear_flux(self):
        self.flux = None

    def get_flux(self):
        return self.flux

    def set_flux(self, flux):
        self.flux = flux

    def get_midpoint(self):
        """
        Getter for the midpoint of the cell.
        If the midpoint == -1 is not yet calculateted, the calculate_midpoint is called.

        Returns:
             list[int]: Midpoint of the cell, x, y coordinates.
        """
        if self.midpoint is None:
            self.calculate_midpoint()

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

        x_mid = sum(x_coordinates) / 3
        y_mid = sum(y_coordinates) / 3

        self.midpoint = [x_mid, y_mid]
