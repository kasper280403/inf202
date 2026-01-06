from src.model.cells.cell import Cell


class Triangle(Cell):
    def __init__(self, id, corner_point_ids, neighbor_ids):
        super().__init__(id)
        super().__init__(corner_point_ids)
        super().__init__(neighbor_ids)


    def check_neighbour(self, test_corner_point_ids):
        n_equal = 0

        for i in self.corner_point_ids:
            if i in test_corner_point_ids:
                n_equal += 1

        if n_equal > 1:
            return True
        else:
            return False

