# operator_overloading.py

class Vector:
    """Represents a 2D vector with operator overloading for arithmetic operations."""
    
    def __init__(self, x, y):
        """Initialize vector with x and y coordinates."""
        self.x = x
        self.y = y

    def __add__(self, other):
        """Overloads the + operator to add two vectors."""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Operand must be an instance of Vector.")

    def __sub__(self, other):
        """Overloads the - operator to subtract two vectors."""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        raise TypeError("Operand must be an instance of Vector.")

    def __mul__(self, scalar):
        """Overloads the * operator to multiply a vector by a scalar."""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        raise TypeError("Scalar multiplier must be an int or float.")

    def __repr__(self):
        """Returns a string representation of the vector."""
        return f"Vector({self.x}, {self.y})"


# Example Usage
if __name__ == "__main__":
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    print(f"v1: {v1}")                  # Vector(3, 4)
    print(f"v2: {v2}")                  # Vector(1, 2)

    print(f"Addition: {v1 + v2}")        # Vector(4, 6)
    print(f"Subtraction: {v1 - v2}")     # Vector(2, 2)
    print(f"Multiplication: {v1 * 2}")   # Vector(6, 8)
