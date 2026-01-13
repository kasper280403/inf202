from src.model.cells.cell import Cell
from src.model.cells.triangle import Triangle
from src.model.cells.edge import Border


class Factory:
    _registry = {
        "triangle": Triangle,
        "border": Border,
    }

    @staticmethod
    def create_cell(cell_type: str, **kwargs) -> Cell:
        try:
            return Factory._registry[cell_type](**kwargs)
        except ValueError:
            raise ValueError("Unknown cell type '{}'".format(cell_type))
