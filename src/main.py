import pathlib
import meshio
from model.factory.factory import Factory
from model.point.point import Point
from model.view.createImage import CreateImage
from model.controller import Controller
import time

start_time = time.time()  # Timer

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

stop_time = time.time(); print("Time:", stop_time - start_time, "seconds") # Time: 0.010102987289428711 seconds


start_time = time.time()  # Timer
controller = Controller(triangle_cells, [0.35, 0.45])
stop_time = time.time(); print("Time:", stop_time - start_time, "seconds") # Time: 1.1920928955078125e-06 seconds


start_time = time.time()  # Timer
controller.set_initial_oil_values()
stop_time = time.time(); print("Time:", stop_time - start_time, "seconds") # Time: 0.0043277740478515625 seconds

start_time = time.time() # Timer
controller.set_neighbours()
stop_time = time.time(); print("Time:", stop_time - start_time, "seconds") # Time: 9.529622077941895 seconds



start_time = time.time()
fishing_ground = [[0.0, 0.0, 0.45, 0.45, 0.0], [0.0, 0.2, 0.2, 0.0, 0.0]]
# triangle_cells[1].set_oil_value(1.0)
image = CreateImage(triangle_cells)
image.plot_Triangles()
image.plot_line(fishing_ground)
image.show_img()
# image.save_img("resources/output/image.png")
stop_time = time.time()
print("Time:", stop_time - start_time, "seconds")