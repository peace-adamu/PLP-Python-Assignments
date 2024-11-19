"""
###
Assignment 1: Design Your Own Class! 🏗️
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation.
Activity 2: Polymorphism Challenge! 🎭

Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).
###
"""

# Defination amd construction a class smartphone
class smartphone:
    def __init__(self, product, battery_capacity):
        self.product = product
        self.__battery_capacity = battery_capacity  # Private variable

    # Methods for displaying specification
    def display_specs(self):
        print(f"Product: {self.product}")
        print(f"Battery Capacity: {self.__battery_capacity}mAh")
    
    # Encapsulation with Getter and Setter Methods:
    # method to access private battery capacity attribute
    def get_battery_capacity(self):
        return self.__battery_capacity

    def set_battery_capacity(self, capacity):
        if capacity > 0:
            self.__battery_capacity = capacity
        else:
            print("Invalid capacity")


# Inheritance and Polymorphism
# Defining a subclass AndroidPhone
class AndroidPhone(smartphone):
    def __init__(self, product, battery_capacity, os_version):
        super().__init__(product, battery_capacity)
        self.os_version = os_version


    def display_specs(self):
        super().display_specs()
        print(f"OS Version: {self.os_version}")

# creating objects and using methods:
my_smartphone = smartphone("Generic phone", 3000)
my_smartphone.display_specs()
print(f"Battery Capacity (accessed through method): {my_smartphone.get_battery_capacity()}")     
    
my_android = AndroidPhone("Android Phone", 4000, "Android 12")
my_android.display_specs()