import numpy as np
from src.model.border.border import Border

class Controller:
    def __init__(self, triangle_list, center_point):
        self.triangle_list = triangle_list
        self.center_point = center_point
        self.timeline = []
        self.timestep = 0

    def set_initial_oil_values(self):
        value_dict = {}

        for triangle in self.triangle_list:
            midpoint = triangle.get_midpoint()
            distance = (midpoint[0] - self.center_point[0]) ** 2 + (midpoint[1] - self.center_point[1]) ** 2
            oil_value = np.exp(-distance / 0.01)
            triangle.set_oil_value(oil_value)
            value_dict[triangle.get_id] = oil_value

        self.timeline.append(value_dict)

    def update_timestep(self):
        self.timestep += 1

    def update_oil_values(self):
        for triangle in self.triangle_list:
            cell_id = triangle.get_id()
            oil_value = self.timeline[self.timestep].get(cell_id)
            triangle.set_oil_value(oil_value)

    def set_neighbours(self):

        for triangle in self.triangle_list:
            for other in self.triangle_list:

                if triangle is other:
                    continue
                elif triangle.get_n_neighbors() == 3:
                    break
                elif other.get_n_neighbors() == 3:
                    break
                elif points := triangle.check_neighbour(other.get_corner_points()):
                    triangle.add_neighbor(other, points[0], points[1])

                    triangle.add_neighbor(other, points[2], points[3])


            if triangle.get_n_neighbors() < 3:
                triangle.finalize_neighbors()

    def calculate_timestep(self):
        None
