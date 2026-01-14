from src.model.cells.cell import Cell
from src.model.cells.triangle import Triangle
from src.model.cells.edge import Edge


class Factory:
    _registry = {
        "triangle": Triangle,
        "border": Edge,
    }

    @staticmethod
    def create_cell(cell_type: str, **kwargs) -> Cell:
        try:
            return Factory._registry[cell_type](**kwargs)
        except ValueError:
            raise ValueError("Unknown cell type '{}'".format(cell_type))
