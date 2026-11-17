# Francisco Huesca
# Module 3 Case Study - Lists, Functions, and Classes
# This program collects information about a car
# and displays the vehicle information.

# Create vehicle superclass and automobile subclass

class Vehicle:

    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):

    def __init__(self, year, make, model, doors, roof):
        Vehicle.__init__(self, "car")

        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Get vehicle information from the user

year = input("Enter the year: ")
make = input("Enter the make: ")
model = input("Enter the model: ")
doors = input("Enter the number of doors (2 or 4): ")
roof = input("Enter the type of roof (solid or sun roof): ")

# Create an automobile object

my_car = Automobile(year, make, model, doors, roof)

# Display vehicle information

print("\nVehicle Information")
print("-------------------")
print("Vehicle type:", my_car.vehicle_type)
print("Year:", my_car.year)
print("Make:", my_car.make)
print("Model:", my_car.model)
print("Number of doors:", my_car.doors)
print("Type of roof:", my_car.roof)