class Point:
    '''
    Represents a point

    Attributes:
        x (int) x coordinate of this point
        y (int) y coordinate of this point
    '''
    def __init__(self,cord):
        self._x = cord[0]
        self._y = cord[1]

    def get_coordinates(self) -> list[float]:
        '''Return a list with the x and y coordinate'''
        return([self._x,self._y])
    
    def get_ycoordinates(self) -> float:
        '''Return y coordinate of point'''
        return(self._y)
    
    def get_xcoordinates(self) -> float:
        '''Return x coordinate of point'''
        return(self._x)
    
    def __hash__(self):
        hash((self._x,self._y))

    def __str__(self):
        return(f'Point with coordinates x = {self._x}, y = {self._y}')
    
