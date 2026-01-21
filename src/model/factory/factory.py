from src.model.cells.cell import Cell
from src.model.cells.triangle import Triangle
from src.model.cells.edge import Edge


class Factory:
    """
    Factory class responsible for making Cell instances.
    """
    _registry = {
        "triangle": Triangle,
        "edge": Edge,
    }

    @staticmethod
    def create_cell(cell_type: str, **kwargs) -> Cell:
        """
        Method that creates either a Triangle or Edge depending on attributes

        Attributes:
            cell_type (str): The name of the cell type, from the registry
            kwargs (dict): Keyword arguments, passed along to the Cell

        Returns:
            Cell: The created cell
        """
        try:
            return Factory._registry[cell_type](**kwargs)
        except ValueError:
            raise ValueError("Unknown cell type '{}'".format(cell_type))
