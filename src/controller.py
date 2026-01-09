

class Controller:
    def __init__(self, triangle_list):
        self.triangle_list = triangle_list

    def set_initial_oil_values(self):
        for triangle in self.triangle_list:
