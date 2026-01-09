import itertools
from abc import ABC, abstractmethod
import pickle

class Cell(ABC):
    """
    Represents a cell of any type, parent class

    Attributes:
        cell_id (int): The cells id
        corner_points (list[Point]): Instances of the class Point
        neighbor_ids (list[int]): IDs of bordering cells.
        oil_value (float): The amount of oil in that cell.
    """
    id_counter = itertools.count()

    def __init__(self, corner_points):
        self.cell_id = next(self.id_counter)
        self.corner_points = corner_points
        self.neighbors = []
        self.oil_value = 0.0
        self.type = None

    def get_id(self):
        return self.cell_id

    def get_corner_points(self):
        return self.corner_points

    def get_neighbors(self):
        return self.neighbor

    def get_oil_value(self):
        return self.oil_value

    def get_type(self):
        return self.type

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def set_oil_value(self, oil_value):
        self.oil_value = oil_value



