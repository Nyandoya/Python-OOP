class Car:
    def __init__(self, make, model, year, doors):
        self.make = make
        self.model = model
        self.year = year
        self.doors = doors

    def display_info(self):
        return f"Car: {self.make} {self.model}, Year: {self.year}, Doors: {self.doors}"

    def move(self):
        return "Driving on the road"

def vehicle_moves_demo(vehicles):
    for vehicle in vehicles:
        print(vehicle.display_info())
        print("Action:", vehicle.move())
        print("-" * 30)

class Plane:
    def __init__(self, make, model, year, wingspan):
        self.make = make
        self.model = model
        self.year = year
        self.wingspan = wingspan

    def display_info(self):
        return f"Plane: {self.make} {self.model}, Year: {self.year}, Wingspan: {self.wingspan}"

    def move(self):
        return "Flying in the sky"

class Boat:
    def __init__(self, make, model, year, length):
        self.make = make
        self.model = model
        self.year = year
        self.length = length

    def display_info(self):
        return f"Boat: {self.make} {self.model}, Year: {self.year}, Length: {self.length}"

    def move(self):
        return "Sailing on the water"

# Create objects
car1 = Car("Toyota", "Corolla", 2020, 4)
plane1 = Plane("Boeing", "747", 2018, "68.5m")
boat1 = Boat("Yamaha", "212X", 2022, "21ft")

# Demonstrate polymorphism
vehicle_list = [car1, plane1, boat1]
vehicle_moves_demo(vehicle_list)
