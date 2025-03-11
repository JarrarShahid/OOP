from math import pi

class Shape:
    """
    Base class for different shapes.
    """
    def area(self):
        raise NotImplementedError("Subclasses must implement the area method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Demonstrating Polymorphism
def print_area(shape):
    print(f"The area of the {shape.__class__.__name__} is: {shape.area():.2f}")

if __name__ == "__main__":
    shapes = [Circle(5), Rectangle(4, 6)]
    for shape in shapes:
        print_area(shape)

