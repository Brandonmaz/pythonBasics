class Vehicle:
    # these variables should not be changed outside of the class specification
    # this is a class attribute
    color = ['red', 'blue']
    vehicle_counter = 0

    def __init__(self, body_type, make):
        self.vehicle_body = body_type
        self.vehicle_make = make
        Vehicle.vehicle_counter += 1

    def get_vehicle_count(self):  # must have self before any arguments
        return Vehicle.vehicle_counter

    def drive(self):
        print("car driving...")

# in order to inherite the Vehicle class attributes, it goes in as an argument

# Truck is a sub or child class of Vehicle


class Truck(Vehicle):
    # Overriding the method defined in the Vehicle class, drive()
    def drive(self):
        print("truck driving...")


class Motorcycle(Vehicle):
    # Overriding the method defined in the Vehicle class, drive()
    def drive(self):
        print("motorcycle driving...")
