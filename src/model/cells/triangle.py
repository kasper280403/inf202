from src.model.cells.cell import Cell


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
        flow (list[float]): Flow of the water at the midpoint.
    """

    def __init__(self, corner_points):
        super().__init__(corner_points)
        self.type = "triangle"
        self.midpoint = None
        self.flow = None

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

    def check_neighbour(self, other_corner_points):
        """
        Cheks if a set of corner points share 2 of the same points as its own.
        Determines if the other cell is bordering itself

        Args:
            self.corner_pointd(list[Point]): List with the instances of Point
            other_corner_points(list[Point]): List with instances of Point for the other cells. .

        Returns:
            p1, p2: Instances of the class Point
            if false return None
        """

        shared = set(self.corner_points) & set(other_corner_points)

        if len(shared) == 2:
            p1, p2 = tuple(shared)
            return p1, p2

        return None

    def finalize_neighbors(self):

        used_edges = set(
            frozenset((p1, p2))
            for _, p1, p2 in self.neighbors
        )

        for p1, p2 in self.edges():
            edge_key = frozenset((p1, p2))

            if edge_key not in used_edges:
                self.neighbors.append((None, p1, p2))

        assert len(self.neighbors) == 3

    def edges(self):
        p1, p2, p3 = self.corner_points
        return [
            (p1, p2),
            (p2, p3),
            (p3, p1),
        ]


    def get_flow(self):
        if self.flow is None:
            self.calculate_flow()

        return self.flow

    def calculate_flow(self):
        midpoint = self.get_midpoint()
        flow_x = midpoint[1] - 0.2 * midpoint[0]
        flow_y = - midpoint[1]

        self.flow = [flow_x, flow_y]
