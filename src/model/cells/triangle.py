from src.model.cells.cell import Cell
from src.model.border.border import Border


class Triangle(Cell):
    """
    Represents a cell of the type triangle.

    Attributes(inherited from Cell):
        cell_id (int): The cells id
        corner_points (list[Point]): Instances of the class Point
        oil_value (float): The amount of oil in that cell.
        midpoint (list[float]): Midpoint of the triangle. x and y coordinates.
        flow (list[float]): Flow of the water at the midpoint, x, y vector.
        borders (list[Border]): list with instances of Border

    Attributes(exclusive to Triangle):
        area (float): Area of the triangle.
        in_fg (bool): True if the triangle is inside the fishing grounds
    """

    def __init__(self, corner_points):
        super().__init__(corner_points)
        self._area = self.calculate_area()
        self._in_fg = False

    def get_area(self):
        return self._area

    def calculate_area(self):
        """
        Calculates the area of the triangle.

        Returns:
            float: The area of the triangle.
        """
        (x1, y1), (x2, y2), (x3, y3) = (
            p.get_coordinates() for p in self._corner_points
        )

        return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

    def check_neighbour(self, other_corner_points):
        """
        Cheks if a set of corner points share 2 of the same points as its own.
        Determines if the other cell is bordering itself

        Args:
            other_corner_points(list[Point]): List with instances of Point for the other cells. .

        Returns:
            p1, p2: Instances of the class Point
            if false returns None
        """
        shared = set(self._corner_points) & set(other_corner_points)

        if len(shared) == 2:
            p1, p2 = tuple(shared)
            return p1, p2
        return None

    def finalize_borders(self):
        """
        Method to add the edges of the triangle to the border list.
        Checks which side is without a border, and creates an instance of Border.
        """
        used_edges = set(
            frozenset(border.get_points())
            for border in self._borders
        )

        for p1, p2 in self.get_edges():
            edge_key = frozenset((p1, p2))

            if edge_key not in used_edges:
                self._borders.append(Border(p1, p2, None, self))

    def get_edges(self):
        """
        Used in finalize_borders() to creat a list to iterate over.

        Returns:
            list[Tuples]: Each tuple is the Points for one edge of the triangle.
        """
        p1, p2, p3 = self._corner_points
        return [
            (p1, p2),
            (p2, p3),
            (p3, p1),
        ]

    def is_in_fg(self):
        return self._in_fg

    def calculate_in_fg(self, fg):
        """
        Calculate if triangle is in the fishing grounds.
        And sets the in_fg to True or False.

        Attributes:
            fg (list[float]): The coordinates of the fishing ground.
        """
        x_mid, y_mid = self.get_midpoint()
        if fg[0][0] < x_mid < fg[0][1] and fg[1][0] < y_mid < fg[1][1]:
            self._in_fg = True
