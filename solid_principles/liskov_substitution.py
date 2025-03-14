# liskov_substitution.py

from abc import ABC, abstractmethod

# Base class for all birds
class Bird(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def move(self):
        pass

# Subclass for birds that can fly
class FlyingBird(Bird):
    def move(self):
        print(f"{self.name} is flying high in the sky! ✈️")

# Subclass for birds that cannot fly (like Ostrich)
class FlightlessBird(Bird):
    def move(self):
        print(f"{self.name} is running on the ground! 🏃")

# Specific bird classes
class Sparrow(FlyingBird):
    pass

class Eagle(FlyingBird):
    pass

class Ostrich(FlightlessBird):
    pass

# Demonstration
if __name__ == "__main__":
    sparrow = Sparrow("Sparrow")
    eagle = Eagle("Eagle")
    ostrich = Ostrich("Ostrich")

    birds = [sparrow, eagle, ostrich]

    for bird in birds:
        bird.move()
