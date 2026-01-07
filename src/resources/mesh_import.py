import meshio
from pathlib import Path
from typing import Optional


class Mesh:
	"""
	This will load the `bay.msh` file located next to this module.
	Instantiate with `Mesh()` or `Mesh('path/to/file.msh')`.
	"""

	def __init__(self, mesh_path: Optional[str | Path] = None, read_on_init: bool = True):
		if mesh_path is None:
			mesh_path = Path(__file__).parent / "bay.msh"
		self.mesh_path = Path(mesh_path)
		self._mesh = None
		if read_on_init:
			self.load(self.mesh_path)

	def load(self, mesh_path: Optional[str | Path] = None):
		"""Load the mesh using meshio and return the mesh object.

		Raises FileNotFoundError if the file does not exist.
		"""
		if mesh_path is not None:
			self.mesh_path = Path(mesh_path)
		if not self.mesh_path.exists():
			raise FileNotFoundError(f"Mesh file not found: {self.mesh_path}")
		self._mesh = meshio.read(self.mesh_path)
		return self._mesh

	def get_mesh(self):
		"""Return the loaded meshio object."""
		if self._mesh is None:
			self.load()
		return self._mesh

	def get_points(self):
		"""Return the points array from the mesh."""
		return self.get_mesh().points

	def get_cells(self):
		"""Return the raw cells list from the mesh."""
		return self.get_mesh().cells

	def get_cells_dict(self):
		"""Return a mapping from cell-type to arrays."""
		mesh = self.get_mesh()
		if hasattr(mesh, "cells_dict"):
			return mesh.cells_dict
		# meshio older versions may store cells differently
		return {c.type: c.data for c in mesh.cells}

	def get_triangles(self):
		"""Return triangle connectivity or an empty list if none."""
		return self.get_cells_dict().get("triangle", [])

	def get_lines(self):
		"""Return line connectivity (edges/borders) or an empty list if none."""
		return self.get_cells_dict().get("line", [])

	def __repr__(self):
		return f"<Mesh path={self.mesh_path} loaded={self._mesh is not None}>"


if __name__ == "__main__":
	m = Mesh()
	print(m)
	print("Points:", len(m.get_points()))
	print("Triangles:", len(m.get_triangles()))
	print("Lines:", len(m.get_lines()))
