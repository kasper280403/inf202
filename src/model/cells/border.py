from model.cells.cell import Cell


class Border(Cell):

    def __init__(self, corner_points):
        super().__init__(corner_points)
        self.type = "border"




