from building import Building
from city import City 

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


megalopolis = City()
megalopolis.add_building(building_five)
megalopolis.add_building(eight_hundred_eighth)
megalopolis.add_building(building_four)
megalopolis.add_building(building_three)
megalopolis.add_building(building_two)

for building in megalopolis.buildings:
    building.building_print() 