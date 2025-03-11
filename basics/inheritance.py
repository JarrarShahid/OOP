class Vehicle:
    """
    Superclass representing a generic vehicle.
    """
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        """Displays basic vehicle information."""
        return f"{self.year} {self.brand} {self.model}"

    def start_engine(self):
        return "Engine started. Ready to go!"


class Car(Vehicle):
    """
    Subclass representing a car, inheriting from Vehicle.
    """
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def honk(self):
        return "Car horn: Beep beep!"

    def display_info(self):
        """Overrides display_info to include doors."""
        return f"{super().display_info()} - {self.num_doors} doors"


class Bike(Vehicle):
    """
    Subclass representing a bike, inheriting from Vehicle.
    """
    def __init__(self, brand, model, year, bike_type):
        super().__init__(brand, model, year)
        self.bike_type = bike_type  # e.g., Mountain, Road, Hybrid

    def ring_bell(self):
        return "Bike bell: Ring ring!"

    def display_info(self):
        """Overrides display_info to include bike type."""
        return f"{super().display_info()} - {self.bike_type} bike"


# Demonstration
if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2022, 4)
    bike = Bike("Giant", "Escape 3", 2023, "Road")

    print(car.display_info())  # Output: 2022 Toyota Camry - 4 doors
    print(car.start_engine())  # Output: Engine started. Ready to go!
    print(car.honk())  # Output: Car horn: Beep beep!

    print(bike.display_info())  # Output: 2023 Giant Escape 3 - Road bike
    print(bike.start_engine())  # Output: Engine started. Ready to go!
    print(bike.ring_bell())  # Output: Bike bell: Ring ring!
