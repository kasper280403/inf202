import numpy as np


class Controller:
    def __init__(self, triangle_list, center_point):
        self.triangle_list = triangle_list
        self.center_point = center_point
        self.timeline = []

    def set_initial_oil_values(self):
        value_dict = {}

        for triangle in self.triangle_list:
            midpoint = triangle.get_midpoint()
            distance = (midpoint[0] - self.center_point[0]) ** 2 + (midpoint[1] - self.center_point[1]) ** 2
            oil_value = np.exp(-distance / 0.01)
            triangle.set_oil_value(oil_value)
            value_dict[triangle.get_id] = oil_value

        self.timeline.append(value_dict)
