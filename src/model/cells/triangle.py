from src.model.cells.cell import Cell


class Triangle(Cell):
    """
    Represents a cell of the type triangle.

    Attributes(inherited from Cell):
        id (int): Uniqie identifier of the cell.
        corner_point_ids (list[int]): Corner points of the cell.
        neighbor_ids (list[int]): IDs of bordering cells.
    """
    def __init__(self, id, corner_point_ids, neighbor_ids):
        super().__init__(id)
        super().__init__(corner_point_ids)
        super().__init__(neighbor_ids)


    def check_neighbour(self, test_corner_point_ids):
        """
        Cheks if a setg of corner points share have 2 of the same points its own.
        Determines if the other cell is bordering itself

        Args:
            self.corner_point_ids: Corner points of the cell.
            test_corner_point_ids(list[int]): Corner points of the other cells. .

        Returns:
            bool: True if the cell is bordering itself
        """
        return len(set(self.corner_point_ids) & set(test_corner_point_ids)) == 2

