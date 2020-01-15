import datetime

class Building:
    def __init__(self, address, stories):
        self.designer = ""
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, new_owner):
        self.owner = new_owner

    def building_print(self):
        print(f"This building on {self.address} was purchased by {self.owner}, and built {self.date_constructed}. It has {self.stories} stories.")






