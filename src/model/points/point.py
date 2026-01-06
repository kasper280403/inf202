

class Point:
    """
    Represents a point in the mesh

    Attributes:
        _x (int): x coordinate of this point
        _y (int): y coordinate of this point
    """
    def __init__(self,cord):
        self._x = cord[0]
        self._y = cord[1]

    def get_coordinates(self) -> list[float]:
        return[self._x, self._y]
    
    def get_y_coordinate(self) -> float:
        return self._y
    
    def get_x_coordinate(self) -> float:
        return self._x
    
    def __hash__(self):
        hash((self._x, self._y))

    def __str__(self):
        return f"Point with coordinates x = {self._x}, y = {self._y}"
    
