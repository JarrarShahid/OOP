from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract class representing an Animal.
    """
    
    @abstractmethod
    def make_sound(self):
        """Abstract method to be implemented by subclasses"""
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow! Meow!"

# Demonstration of Abstraction
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    
    print("Dog says:", dog.make_sound())
    print("Cat says:", cat.make_sound())
 
