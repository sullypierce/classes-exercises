

class City:
    def __init__(self):
        self.name = ""
        self.mayor = ""
        self.year_established = ""
        self.buildings = list()

    def add_building(self, new_building):
        self.buildings.append(new_building)