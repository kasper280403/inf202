import itertools

class Cell:
    """
    Represents a cell of any type, parent class

    Attributes:
        id (int): The cells id
        corner_point_ids (list[int]): Corner point ids for this cell
        neighbor_ids (list[int]): IDs of bordering cells.
    """

    id_counter = itertools.count()
    def __init__(self, corner_point_ids):
        self.id = next(self.id_counter)
        self.corner_point_ids = corner_point_ids
        self.neighbor_ids = []

    def get_id(self):
        return self.id

    def get_corner_point_ids(self):
        return self.corner_point_ids

    def get_neighbor_id(self):
        return self.neighbor_ids


    def add_neighbor(self, neighbor_id):
        self.neighbor_ids.append(neighbor_id)


