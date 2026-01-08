import meshio
from pathlib import Path

from src.resources.mesh_import import Mesh
from src.model.points.point import Point
from src.model.cells.triangle import Triangle

mesh_path = Path(__file__).parent.parent/"resources"
mesh = meshio.read(mesh_path/"bay.msh")

lines = mesh.cells_dict["line"]




'''
Mål: 
- Generere slik at alt her blir til en klasse. 
- Vil hente ut det som er her ved å kalle p_list = FactoryScript.get_point_list() foreks

Factory som lager border elementer
Factory som skiller om det er border element eller noe midt inni

Alt er i samme factory, dette er bare ulike metoder.

'''

"""
A factory class with multiple metods. 
Goal - Achieve to implement, point, triangle and border factories.

"""

class Factory:
    def __init__(self, mesh_name):
        self.mesh = meshio.read(Path(__file__).parent.parent/mesh_name)
        self.triangle_list = None
        self.point_list = None

    def get_point_list(self):
        return self.point_list

    def get_triangle_list(self):
        return self.triangle_list

    def create_triangles(self):

        if self.point_list is None:
            self.create_points()
        triangles = self.mesh.cells_dict["triangle"]
        triangle_list = []

        for triangle in triangles:
            l = []
            for point_id in triangle:
                l.append(self.point_list[point_id])
            x = Triangle(l)
            triangle_list.append(x)

        self.triangle_list = triangle_list

    def create_points(self):
        points = mesh.points

        point_list = []
        for point in points:
            x = Point(point)
            point_list.append(x)

        self.point_list = point_list
    
