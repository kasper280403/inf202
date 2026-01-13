import numpy as np
from src.model.border.border import Border


def g_function(oil_i, oil_ngh, v_normal, u):
    dot = np.dot(v_normal, u)

    if dot > 0:
        return oil_i * dot
    else:
        return oil_ngh * dot


class Controller:
    def __init__(self, triangle_list, center_point):
        self.triangle_list = triangle_list
        self.center_point = center_point
        self.timeline = []
        self.next_oil_value = {}
        self.timestep = 0
        self.timestep_length = 1

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
        self.timestep += self.timestep_length

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
                    border = Border(points[0], points[1], other)
                    triangle.add_border(border)


            if triangle.get_n_neighbors() < 3:
                triangle.finalize_borders()

    def calculate_timestep(self):

        self.update_timestep()


        for triangle in self.triangle_list:
            self.calculate_oil_triangle(triangle)

        for triangle in self.triangle_list:
            triangle.set_oil_value(self.next_oil_value.get(triangle.get_id()))





    def calculate_oil_triangle(self, triangle):


        area_i = triangle.get_area()
        flow_i = triangle.get_flow()
        oil_i = triangle.get_oil_value()

        flux_list =  []
        for border in triangle.get_borders():
            if border.get_neighbors() is not None:
                flux = self.calculate_flux_triangle_edge(border, area_i, flow_i, oil_i)
                flux_list.append(flux)
            else:
                if border.get_border_type() == "ocean":
                    flux = self.calculate_flux_edge(border, area_i, flow_i, oil_i)
                    flux_list.append(flux)
                elif border.get_border_type() == "coast":
                    continue


        oil_value_new = oil_i
        for flux in flux_list:
            oil_value_new = oil_value_new + flux

        self.next_oil_value[triangle.get_id()] = oil_value_new

    def calculate_flux_triangle_edge(self, border, area_i, flow_i, oil_i):
        p_1 = - self.timestep_length / area_i

        v_normal = border.get_normal()
        oil_ngh = border.get_neighbor().get_oil_value()
        flow_ngh = border.get_neighbor().get_flow()

        p_2 = g_function(oil_i, oil_ngh, v_normal, (flow_i - flow_ngh)/2)

        return p_1 * p_2

    def calculate_flux_edge(self, border, area_i, flow_i, oil_i):

        p_1 = - self.timestep_length / area_i

        v_normal = border.get_normal()
        oil_ngh = 0
        flow_ngh = [0.0,0.0]

        p_2 = g_function(oil_i, oil_ngh, v_normal, (flow_i - flow_ngh) / 2)

        return p_1 * p_2