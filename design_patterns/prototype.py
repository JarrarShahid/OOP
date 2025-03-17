# prototype.py

import copy
from abc import ABC, abstractmethod


# Step 1: Prototype Interface
class Prototype(ABC):
    """Abstract prototype with a clone method."""

    @abstractmethod
    def clone(self):
        """Creates a copy of the object."""
        pass


# Step 2: Concrete Prototype
class Car(Prototype):
    """Concrete class implementing the Prototype pattern."""

    def __init__(self, brand, model, engine, features=None):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.features = features if features else []

    def add_feature(self, feature):
        """Adds a feature to the car."""
        self.features.append(feature)

    def clone(self):
        """Creates a deep copy of the object."""
        return copy.deepcopy(self)

    def __str__(self):
        return f"Car: {self.brand} {self.model}, Engine: {self.engine}, Features: {self.features}"


# Step 3: Demonstration
if __name__ == "__main__":
    print("🚗 Creating the original car prototype...")
    original_car = Car("Tesla", "Model S", "Electric", ["Autopilot", "Self-parking"])
    print(original_car)

    print("\n📋 Cloning the car...")
    cloned_car = original_car.clone()
    print(cloned_car)

    print("\n🔧 Modifying the cloned car...")
    cloned_car.add_feature("Wireless Charging")
    print("Original Car:", original_car)
    print("Cloned Car:", cloned_car)
