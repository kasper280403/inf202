

import pathlib
import meshio
from model.factory.factory import Factory
from model.point.point import Point
from model.cells.cell import Cell
from model.cells.triangle import Triangle
from model.cells.border import Border
from model.view.createImage import CreateImage

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
















image = CreateImage(triangle_cells)
image.plot_Triangles()
#image.save_img("resources/output/image.png")