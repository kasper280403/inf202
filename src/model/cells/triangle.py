from src.model.cells.cell import Cell


class Triangle(Cell):
    """
    Represents a cell of the type triangle.

    Attributes(inherited from Cell):
        id (int): Unique identifier of the cell.
        corner_point_ids (list[int]): Corner points of the cell.
        neighbor_ids (list[int]): IDs of bordering cells.
    """
    def __init__(self, id, corner_point_ids, neighbor_ids, midpoint):
        super().__init__(id)
        super().__init__(corner_point_ids)
        super().__init__(neighbor_ids)
        self.midpoint = -1


    def check_neighbour(self, test_corner_point_ids):
        """
        Cheks if a set of corner points share 2 of the same points as its own.
        Determines if the other cell is bordering itself

        Args:
            self.corner_point_ids: Corner points of the cell.
            test_corner_point_ids(list[int]): Corner points of the other cells. .

        Returns:
            bool: True if the cell is bordering itself
        """
        return len(set(self.corner_point_ids) & set(test_corner_point_ids)) == 2

    def get_midpoint(self):
        if self.midpoint == -1:
            self.set_midpoint()

        return self.midpoint


    def set_midpoint(self):
        x_coordinates = []
        y_coordinates = []

        for point in self.corner_point_ids:
            coordinates = Point.get_coordinates(point)
            x_coordinates.append(coordinates[0])
            y_coordinates.append(coordinates[1])

        x_mid = 1/3 * sum(x_coordinates)
        y_mid = 1/3 * sum(y_coordinates)

        self.midpoint =  [x_mid, y_mid]



