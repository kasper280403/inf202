import numpy as np
from src.model.cells.edge import Edge


class Border:
    """
    Border class to represent the 3 borders of a triangle

    Attributes:
        _p1 (Point): first edgepoint of the border
        _p2 (Point): second edgepoint of the border
        _triangle (Triangle): triangle to which the border belongs
        _neighbour (Cell): Cell to which the triangle borders, can be Edge or Triangle
        _normal (np.array[float]): nomral vector facing outwards of the triangle on this edge
    """

    def __init__(self, p1, p2, neighbour=None, tri=None):
        self._p1 = p1
        self._p2 = p2
        self._triangle = tri
        self._neighbour = neighbour
        self._normal = self.calculate_normal()
        if self._neighbour is None:
            self.create_edge()

    def calculate_normal(self):
        """
        Calculates the normal and chooses direction outwards

        Return:
            np.array[float]: normal vector facing outwards of the border
        """

        line_vec = self._p2.get_coordinates() - self._p1.get_coordinates()
        normal = np.cross(line_vec, [0, 0, 1])[0:2]
        midt_p1 = self._p1.get_coordinates() - self._triangle.get_midpoint()
        theta = np.arccos(np.inner(normal, midt_p1) /
                          (np.linalg.norm(normal) * np.linalg.norm(midt_p1)))
        if theta > np.pi / 2:
            normal = normal * (-1)

        return normal

    def get_points(self):
        return np.array([self._p1, self._p2])

    def get_neighbour(self):
        return self._neighbour

    def get_normal(self):
        return self._normal

    def create_edge(self):
        """
        Creates Edge neigbour if the Border is created without Triangle neighbour
        """
        self._neighbour = Edge([self._p1, self._p2])
