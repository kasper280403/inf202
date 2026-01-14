from src.model.cells.cell import Cell


class Edge(Cell):
    """
    Represents a cell of the type border

    Attributes(inherited from Cell):
        id (int): Unique identifier of the cell.
        corner_points (list[Point]): Instances of the class Point
        neighbor_ids (list[int]): IDs of bordering cells.
        oil_value (float): The amount of oil in that cell.
        borders (list[Border]): list with instances of Border
        oil_value (float): The amount of oil in that cell.

    """
    def __init__(self, corner_points):
        super().__init__(corner_points)


    def set_oil_value(self, oil_value):
        self.oil_value = 0.0