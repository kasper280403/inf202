import itertools

class Cell:
    id_counter = itertools.count()

    def __init__(self, corner_point_ids):
        self.id = next(self.id_counter)
        self.corner_point_ids = corner_point_ids

    def get_id(self):
        return self.id

    def get_corner_point_ids(self):
        return self.corner_point_ids

