import itertools

class Cell:
    """
    Represents a cell of any type, parent class

    Attributes:
        id (int): The cells id
        corner_points (list[Point]): Instances of the class Point
        neighbor_ids (list[int]): IDs of bordering cells.
    """

    id_counter = itertools.count()
    def __init__(self, corner_points):
        self.id = next(self.id_counter)
        self.corner_points = corner_points
        self.neighbor_ids = []

    def get_id(self):
        return self.id

    def get_corner_points(self):
        return self.corner_points

    def get_neighbor_id(self):
        return self.neighbor_ids

    def add_neighbor(self, neighbor_id):
        self.neighbor_ids.append(neighbor_id)


