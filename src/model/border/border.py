import numpy as np
from src.model.cells.edge import Edge


class Border:
    """
    Border class to represent the 3 borders of a triangle

    Attributes:
        p1 (Point): first edgepoint of the border
        p2 (Point): second edgepoint of the border
        triangle (Triangle): triangle to which the border belongs
        neighbour (Triangle): triangle to which the border borders
        normal (array[float]): vector defining the normal facing
                               outwards of the triangle for this border

    """
    def __init__(self, p1, p2, neighbour=None, tri=None):
        self._p1 = p1
        self._p2 = p2
        self._triangle = tri
        self._neighbour = neighbour
        self._normal = self.calculate_normal()
        if self._neighbour is None:
            self.create_edge()

    def create_edge(self):
        self._neighbour = Edge([self._p1, self._p2])

    def calculate_normal(self):
        """
        Calculates the normal for the current border
        and makes sure it faces outwards
        """
        # Line from p1 to p2
        line_vec = self._p2.get_coordinates() - self._p1.get_coordinates()

        # Create normal by crossing line vector with vector pointing in z dir
        normal = np.cross(line_vec, [0, 0, 1])[0:2]

        # Line from triangle midpoint to p1
        midt_p1 = self._p1.get_coordinates() - self._triangle.get_midpoint()

        # Check if normal is pointing out of triangle
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
