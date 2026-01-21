from src.model.cells.cell import Cell


class Edge(Cell):
    """
    Represents a cell of the type border

    Attributes(inherited from Cell):
        cell_id (int): The cells id
        corner_points (list[Point]): Instances of the class Point
        oil_value (float): The amount of oil in that cell.
        midpoint (list[float]): Midpoint of the triangle. x and y coordinates.
        flow (list[float]): Flow of the water at the midpoint, x, y vector.
        borders (list[Border]): list with instances of Border

    """

    def __init__(self, corner_points):
        super().__init__(corner_points)

    def set_oil_value(self, oil_value):
        """
        Overides the get_oil_value method in parent class.
        Task descriptions says oil that excites the map should just disapear.

        Args:
            oil_value (float): The amount of oil in that cell.

        Returns:
             float == 0.0
        """
        self._oil_value = 0.0
