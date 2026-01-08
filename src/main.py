import pathlib
import meshio
from model.factory.factory import Factory
from model.point.point import Point
import numpy as np

mesh_path = pathlib.Path(__file__).parent / "resources" / "bay.msh"
mesh = meshio.read(mesh_path)


point_cells = [] # list with Point
for point in mesh.points:
    point_cells.append(Point(point))

factory = Factory()

triangle_cells = [] # list with instances of Triangle
for m in mesh.cells:
    if m.type == "triangle":
        for t in m.data:
            triangle_cell = factory.create_cell(
                "triangle",
                corner_points=[
                    point_cells[t[0]],
                    point_cells[t[1]],
                    point_cells[t[2]],
                ]
            )
            triangle_cells.append(triangle_cell)



def set_inital_oil_values(center_point, triangle):
    center_point = [0.35, 0.45]
    midpoint = triangle.get_midpoint()

    distance =  (midpoint[0] - center_point[0])**2 + (midpoint[1] - center_point[1])**2

    return np.exp(-distance/0.01)








