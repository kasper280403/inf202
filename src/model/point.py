class Point:
    def __init__(self,cord):
        self._x = cord[0]
        self._y = cord[1]
        self._id = id

    def get_coordinates(self):
        return([self._x,self._y])
    
    def get_ycoordinates(self):
        return(self._y)
    
    def get_xcoordinates(self):
        return(self._x)
    
    def __hash__(self):
        hash((self._x,self._y))

    def __str__(self):
        return(f'Point with coordinates x = {self._x}, y = {self._y}')
    
