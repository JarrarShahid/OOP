from abc import ABC, abstractmethod

# Step 1: Create an abstract base class
class Shape(ABC):
    """Abstract base class for different shapes."""
    
    @abstractmethod
    def draw(self):
        """Abstract method to draw a shape."""
        pass

# Step 2: Create concrete shape classes
class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"

class Rectangle(Shape):
    def draw(self):
        return "Drawing a Rectangle"

# Step 3: Implement the Factory class
class ShapeFactory:
    """Factory class for creating Shape objects."""
    
    @staticmethod
    def get_shape(shape_type: str) -> Shape:
        shapes = {
            "circle": Circle(),
            "square": Square(),
            "rectangle": Rectangle()
        }
        return shapes.get(shape_type.lower(), None)

# Step 4: Demonstration
if __name__ == "__main__":
    factory = ShapeFactory()

    shape1 = factory.get_shape("circle")
    shape2 = factory.get_shape("square")
    shape3 = factory.get_shape("rectangle")
    shape4 = factory.get_shape("triangle")  # Not in factory

    print(shape1.draw() if shape1 else "Invalid Shape")  # Output: Drawing a Circle
    print(shape2.draw() if shape2 else "Invalid Shape")  # Output: Drawing a Square
    print(shape3.draw() if shape3 else "Invalid Shape")  # Output: Drawing a Rectangle
    print(shape4.draw() if shape4 else "Invalid Shape")  # Output: Invalid Shape
