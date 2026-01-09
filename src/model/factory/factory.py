from model.cells.cell import Cell
from model.cells.triangle import Triangle
from model.cells.border import Border


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
