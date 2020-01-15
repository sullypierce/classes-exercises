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


    
eight_hundred_eighth = Building("800 8th Street", 12 )

building_two = Building("2nd st", 17)
building_three = Building("3rd st", 5)
building_four = Building("4th ave", 23)
building_five = Building("5th blvd", 11)

building_five.purchase("Fred")
building_four.purchase("Fredward")
building_three.purchase("Freddifer")
building_two.purchase("Freddy")
eight_hundred_eighth.purchase("Fredegar")


building_five.construct()
eight_hundred_eighth.construct()
building_four.construct()
building_three.construct()
building_two.construct()

building_five.building_print()
building_four.building_print()
eight_hundred_eighth.building_print()
building_three.building_print()
building_two.building_print()



