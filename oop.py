# Base class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

    def move(self):
        return "This vehicle moves in its own way."

# Subclass: Car
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def move(self):
        return "Driving on the road 🚗"

# Subclass: Plane
class Plane(Vehicle):
    def __init__(self, make, model, year, wingspan):
        super().__init__(make, model, year)
        self.wingspan = wingspan

    def move(self):
        return "Flying in the sky ✈️"

# Subclass: Boat
class Boat(Vehicle):
    def __init__(self, make, model, year, length):
        super().__init__(make, model, year)
        self.length = length

    def move(self):
        return "Sailing on the water 🚤"
