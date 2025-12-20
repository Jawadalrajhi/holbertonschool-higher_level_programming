from abc import ABC, abstractmethod


# Step 1: Set up the Abstract Class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


# Step 2: Implement the Subclasses
class Dog(Animal):

    def sound(self):
        return "Bark"


class Cat(Animal):

    def sound(self):
        return "Meow"


# Testing the classes
dog = Dog()
cat = Cat()

print(dog.sound())  # Output: Bark
print(cat.sound())  # Output: Meow
