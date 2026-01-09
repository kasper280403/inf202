import pathlib
import meshio
from model.factory.factory import Factory
from model.point.point import Point
from model.view.createImage import CreateImage
import numpy as np
import pickle

with open("resources/oil_distribution/oil.bin", "wb"):
    pass

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



def set_initial_oil_value(center_point, tri, timestep):

    midpoint = tri.get_midpoint()
    distance =  (midpoint[0] - center_point[0])**2 + (midpoint[1] - center_point[1])**2
    oil_value = np.exp(-distance/0.01)
    tri.set_oil_value(oil_value)
    timestep[tri.get_id()] = oil_value






currenttimestep = 0
timestep={}

for triangle in triangle_cells:
    set_initial_oil_value([0.35, 0.45],triangle, timestep)

    for n_triangle in triangle_cells:
        if triangle.check_neighbour(n_triangle.get_corner_points()):
            triangle.add_neighbor(n_triangle)


with open("resources/oil_distribution/oil.bin", "ab") as f:
    pickle.dump((currenttimestep, timestep), f, protocol=pickle.HIGHEST_PROTOCOL)








fishing_ground = [[0.0, 0.0, 0.45, 0.45, 0.0],[0.0, 0.2, 0.2, 0.0, 0.0]]
#triangle_cells[1].set_oil_value(1.0)
image = CreateImage(triangle_cells)
image.plot_Triangles()
image.plot_line(fishing_ground)
image.show_img()
#image.save_img("resources/output/image.png")