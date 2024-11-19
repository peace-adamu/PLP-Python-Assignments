"""
Activity 2: Polymorphism Challenge! 🎭

Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).
"""

# Definition
class  Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


# Subclass definition
class car(Vehicle):
    def move(self):
        print("Driving")

class plane(Vehicle):
    def move(self):
        print("Flying")

class bicycle(Vehicle):
    def move(self):
        print("Pedaling") 


 # polymorphism demonstration:
def demonstrate_movement(vehicle):
    vehicle.move()         


# creating objects and calling method
car = car()
plane = plane()
bicycle = bicycle()

Vehicles = [car, plane, bicycle]
for vehicle in Vehicles:
    demonstrate_movement(vehicle)