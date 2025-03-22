# multiple_inheritance.py

class ElectricCar:
    """Represents an electric car with battery capacity."""
    
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity  # in kWh

    def charge_battery(self):
        return f"Charging the battery with {self.battery_capacity} kWh capacity."


class GasolineCar:
    """Represents a gasoline car with fuel tank capacity."""
    
    def __init__(self, fuel_capacity):
        self.fuel_capacity = fuel_capacity  # in liters

    def refuel_tank(self):
        return f"Refueling the tank with {self.fuel_capacity} liters of gasoline."


class HybridCar(ElectricCar, GasolineCar):
    """Hybrid car that combines both electric and gasoline engines."""
    
    def __init__(self, battery_capacity, fuel_capacity):
        # Call constructors of parent classes
        ElectricCar.__init__(self, battery_capacity)
        GasolineCar.__init__(self, fuel_capacity)

    def drive(self):
        return "Driving using both electric and gasoline power for efficiency."

    def status(self):
        return f"Hybrid Car Status: {self.battery_capacity} kWh battery, {self.fuel_capacity}L fuel."


# Example Usage
if __name__ == "__main__":
    hybrid = HybridCar(battery_capacity=50, fuel_capacity=40)

    print(hybrid.charge_battery())   # Calls ElectricCar method
    print(hybrid.refuel_tank())      # Calls GasolineCar method
    print(hybrid.drive())            # Calls HybridCar method
    print(hybrid.status())           # Displays car details
