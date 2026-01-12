import pathlib
import meshio
from model.factory.factory import Factory
from model.point.point import Point
from model.view.createImage import CreateImage
from src.controller import Controller
import time

start_time = time.time()

mesh_path = pathlib.Path(__file__).parent / "resources" / "bay.msh"
mesh = meshio.read(mesh_path)

point_cells = [] # list with Point
for point in mesh.points:
    point_cells.append(Point(point))

factory = Factory()

triangle_cells = []  # list with instances of Triangle
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

stop_time = time.time()
print("Time:", start_time - stop_time, "seconds")


start_time = time.time()
controller = Controller(triangle_cells, [0.35, 0.45])
stop_time = time.time()
print("Time:", start_time - stop_time, "seconds")


start_time = time.time()
controller.set_initial_oil_values()
stop_time = time.time()
print("Time:", start_time - stop_time, "seconds")

start_time = time.time()
controller.set_neighbours()
stop_time = time.time()
print("Time:", start_time - stop_time, "seconds")




fishing_ground = [[0.0, 0.0, 0.45, 0.45, 0.0], [0.0, 0.2, 0.2, 0.0, 0.0]]
# triangle_cells[1].set_oil_value(1.0)
image = CreateImage(triangle_cells)
image.plot_Triangles()
image.plot_line(fishing_ground)
image.show_img()
# image.save_img("resources/output/image.png")
