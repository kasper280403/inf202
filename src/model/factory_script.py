import meshio
from pathlib import Path

from src.model.points.point import Point
from src.model.cells.triangle import Triangle


mesh_path = Path(__file__).parent.parent/"resources"
mesh = meshio.read(mesh_path/"bay.msh")


lines = mesh.cells_dict["line"]


# Should become a method------
points = mesh.points

point_list = []
for point in points:
    x = Point(point)
    point_list.append(x)
#-----------------------------

#method----------------------------------
triangles = mesh.cells_dict["triangle"]
triangle_list = []

for triangle in triangles:
    l = []
    for point_id in triangle:
        l.append(point_list[point_id])
    x = Triangle(l)
    triangle_list.append(x)

#------------------------------------
triangle20 = triangle_list[19]



#need method for borders as well

