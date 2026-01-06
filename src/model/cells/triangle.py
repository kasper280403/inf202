from src.model.cells.cell import Cell


class Triangle(Cell):
    """
    Represents a cell of the type triangle.

    Attributes(inherited from Cell):
        id (int): Unique identifier of the cell.
        corner_points (list[Point]): Instances of the class Point
        neighbor_ids (list[int]): IDs of bordering cells.
    """
    def __init__(self, id, corner_points, neighbor_ids):
        super().__init__(id)
        super().__init__(corner_points)
        super().__init__(neighbor_ids)
        self.midpoint = -1


    def check_neighbour(self, test_corner_points):
        """
        Cheks if a set of corner points share 2 of the same points as its own.
        Determines if the other cell is bordering itself
''''
        Args:
            self.corner_pointd(list[Point]): List with the instances of Point
            test_corner_points(list[Point]): List with instances of Point for the other cells. .

        Returns:
            bool: True if the cell is bordering itself
        """

        return len(set(self.corner_points) & set(test_corner_points)) == 2

    def get_midpoint(self):
        """
        Getter for the midpoint of the cell.
        If the midpoint == -1 is not yet calculateted, the calculate_midpoint is called.

        Returns:
             list[int]: Midpoint of the cell, x, y coordinates.
        """
        if self.midpoint == -1:
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
            x_coordinates.append(point.get_x_coordinate)
            x_coordinates.append(point.get_y_coordinate)

        x_mid = 1/3 * sum(x_coordinates)
        y_mid = 1/3 * sum(y_coordinates)

        self.midpoint =  [x_mid, y_mid]



