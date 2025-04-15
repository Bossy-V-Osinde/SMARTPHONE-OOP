# Base class: Animal
class Animal:
    def move(self):
        print("The animal is moving.")

# Derived class: Dog
class Dog(Animal):
    def move(self):
        print("The dog is running!")

# Derived class: Bird
class Bird(Animal):
    def move(self):
        print("The bird is flying!")

# Base class: Vehicle
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

# Derived class: Car
class Car(Vehicle):
    def move(self):
        print("The car is driving!")

# Derived class: Plane
class Plane(Vehicle):
    def move(self):
        print("The plane is flying!")

# Test Polymorphism
animals = [Dog(), Bird()]
for animal in animals:
    animal.move()  # Polymorphism in action!

vehicles = [Car(), Plane()]
for vehicle in vehicles:
    vehicle.move()  # Polymorphism in action!
