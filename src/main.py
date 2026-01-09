

import pathlib
import meshio
from model.factory.factory import Factory
from model.point.point import Point
from model.view.createImage import CreateImage
import numpy as np
from model.cells.triangle import Triangle

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



def set_initial_oil_value(center_point, tri):

    midpoint = tri.get_midpoint()
    distance =  (midpoint[0] - center_point[0])**2 + (midpoint[1] - center_point[1])**2
    tri.set_oil_value(np.exp(-distance/0.01))




for triangle in triangle_cells:
    set_initial_oil_value([0.35, 0.45],triangle)




def set_initial_oil_value(center_point, tri):

    midpoint = tri.get_midpoint()
    distance =  (midpoint[0] - center_point[0])**2 + (midpoint[1] - center_point[1])**2
    tri.set_oil_value(np.exp(-distance/0.01))


triangle = [Triangle([Point([0.4,0.7]),Point([0.2,0.5]),Point([0.6,0.6])])]
triangle[0].calc_norm()


fishing_ground = [[0.0, 0.0, 0.45, 0.45, 0.0],[0.0, 0.2, 0.2, 0.0, 0.0]]
#triangle_cells[1].set_oil_value(1.0)
image = CreateImage(triangle)
image.plot_Triangles()
image.plot_normals(triangle[0])
    

#image.plot_line(fishing_ground)
image.show_img()
#image.save_img("resources/output/image.png")

#for i in range(3):
#    p1 = triangle[0].corner_points[i].get_coordinates()
#    p2 = triangle[0].corner_points[(i+1)%3].get_coordinates()
#    midt = [(p1[0]+p2[0])/2.0,(p1[1]+p2[1])/2.0]
#    normvec =[[midt[0],midt[0]+triangle[0].get_norm()[i][0]],[midt[1],midt[1]+triangle[0].get_norm()[i][1]]]
#    image.plot_line(normvec)