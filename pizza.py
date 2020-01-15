

class Pizza:
    def __init__(self):
        self.size = ""
        self.style = ""
        self.toppings = list()

    def add_topping(self, topping):
        self.toppings.append(topping)

    def print_order(self):
        topping_string = ""
        for topping in self.toppings:
            topping_string += topping
            
            if self.toppings.index(topping) == (len(self.toppings)-2):
                topping_string += ", and "
            elif self.toppings.index(topping) < (len(self.toppings)-1):
                topping_string += ", "
            else:
                topping_string += "."
        print(f"We have for you a {self.size} inch, {self.style} pizza pie with {topping_string}") 

meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.style = "Deep dish"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Olives")
meat_lovers.add_topping("sausage")
meat_lovers.print_order()