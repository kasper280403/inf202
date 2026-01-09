from model.cells.cell import Cell
import numpy as np


class Triangle(Cell):
    """
    Represents a cell of the type triangle.

    Attributes(inherited from Cell):
        id (int): Unique identifier of the cell.
        corner_points (list[Point]): Instances of the class Point
        neighbor_ids (list[int]): IDs of bordering cells.
        oil_value (float): The amount of oil in that cell.

    Attributes(exclusive to Triangle):
        midpoint (list[float]): Midpoint of the triangle. x and y coordinates.
    """

    def __init__(self, corner_points):
        super().__init__(corner_points)
        self.type = "triangle"
        self.midpoint = None

    def get_midpoint(self):
        """
        Getter for the midpoint of the cell.
        If the midpoint == -1 is not yet calculateted, the calculate_midpoint is called.

        Returns:
             list[int]: Midpoint of the cell, x, y coordinates.
        """
        if self.midpoint is None:
            self.calculate_midpoint()

        return self.midpoint

    def calculate_midpoint(self):
        """
        Calculates the midpoint of the cell.
        Exctracts the x, y coordinates, from the instances Point class
        Sets the self.midpoint
        """
        x_coordinates = []
        y_coordinates = []

        for point in self.corner_points:
            x_coordinates.append(point.get_x_coordinate())
            y_coordinates.append(point.get_y_coordinate())

        x_mid = sum(x_coordinates) / 3
        y_mid = sum(y_coordinates) / 3

        self.midpoint = [x_mid, y_mid]

    def check_neighbour(self, test_corner_points):
        """
        Cheks if a set of corner points share 2 of the same points as its own.
        Determines if the other cell is bordering itself

        Args:
            self.corner_pointd(list[Point]): List with the instances of Point
            test_corner_points(list[Point]): List with instances of Point for the other cells. .

        Returns:
            bool: True if the cell is bordering itself
        """

        return len(set(self.corner_points) & set(test_corner_points)) == 2
    
    def calc_norm(self):
        for i in range(len(self.corner_points)):
            p1 = self.corner_points[i].get_coordinates()
            p2 = self.corner_points[(i+1)%3].get_coordinates()
            line_vec = [p2[0]-p1[0], p2[1]-p1[1],0]
            normal = np.cross(line_vec,[0,0,1])[0:2]
            midt_p1 = [p1[0]-self.get_midpoint()[0], p1[1]-self.get_midpoint()[1]]
            theta = np.arccos(np.inner(normal, midt_p1) / (np.linalg.norm(normal) * np.linalg.norm(midt_p1)))
            if theta > np.pi/2:
                normal = normal *(-1)
            self.norm.append(normal)


