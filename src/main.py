from model.cells.triangle import Triangle
from model.factory.factory import Factory

import pathlib
import meshio
mesh_path = pathlib.Path(__file__).parent / "resources" / "bay.msh"

msh = meshio.read(mesh_path) #read the mesh

points = msh.points #get all the points in the mesh
cells = msh.cells #connect the cell structure
triangle_list = []

    

