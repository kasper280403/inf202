from src.model.cells.cell import Cell


class Edge(Cell):

    def __init__(self, corner_points):
        super().__init__(corner_points)


    def set_oil_value(self, oil_value):
        self.oil_value = 0.0