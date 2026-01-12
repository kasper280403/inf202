import numpy as np


class Border:

    def __init__(self, p1, p2, neighbour):
        self.type = "border"
        self.p1 = p1
        self.p2 = p2
        self.neighbour = neighbour
        self.length = self.calculate_length()
        self.normal = self.calculate_normal()

    def calculate_length(self):
        d = np.sqrt((self.p1.get_x_coordinate() - self.p2.get_x_coordinate()) ** 2 +
                    (self.p1.get_y_coordinate() - self.p2.get_y_coordinate()) ** 2)
        return abs(d)

    def calculate_normal(self):
        line_vec = self.p2.get_coordinates() - self.p1.get_coordinates()
        normal = np.cross(line_vec,[0,0,1])[0:2]
        if self.neighbour != None:
            midt_p1 = self.neighbour.get_midpoint() - self.p1.get_coordinates()
            theta = np.arccos(np.inner(normal, midt_p1) / (np.linalg.norm(normal) * np.linalg.norm(midt_p1)))
            if theta > np.pi/2:
                normal = normal *(-1)
        return normal

    def get_points(self):
        return [self.p1, self.p2]

    def get_neighbour(self):
        return self.neighbour
    
    def get_normal(self):
        return self.normal

