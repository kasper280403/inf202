from src.model.cells.cell import Cell


class Edge(Cell):

    def __init__(self, corner_points):
        super().__init__(corner_points)
        self.midpoint = self.calculate_midpoint()


    def calculate_midpoint(self):
