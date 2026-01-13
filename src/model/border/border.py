import numpy as np


class Border:

    def __init__(self, p1, p2, neighbour):
        self.p1 = p1
        self.p2 = p2
        self.neighbour = neighbour
        self.length = self.calculate_length()
        self.normal = self.calculate_normal()
        self.border_type = "ocean"

    def calculate_length(self):
        d = np.sqrt((self.p1.get_x_coordinate() - self.p2.get_x_coordinate()) ** 2 +
                    (self.p1.get_y_coordinate() - self.p2.get_y_coordinate()) ** 2)
        return abs(d)

    def calculate_normal(self):
        return None

    def get_points(self):
        return [self.p1, self.p2]

    def get_neighbour(self):
        return self.neighbour

    def get_normal(self):
        return self.normal

    def get_border_type(self):
        return self.border_type
