# SOLID Principles in OOP

SOLID is a set of five principles that improve software design.

## 1. Single Responsibility Principle (SRP)
A class should have only one reason to change.

```python
class ReportGenerator:
    def generate_report(self):
        return "Generating Report..."
```

## 2. Open/Closed Principle (OCP)
Software entities should be open for extension but closed for modification.

```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
```

## 3. Liskov Substitution Principle (LSP)
Subtypes must be substitutable for their base types.

```python
class Bird:
    def fly(self):
        return "I can fly"

class Penguin(Bird):
    def fly(self):
        return "I cannot fly"
```

## 4. Interface Segregation Principle (ISP)
Clients should not be forced to depend on interfaces they do not use.

```python
class Printer:
    def print_document(self):
        pass

class Scanner:
    def scan_document(self):
        pass
```

## 5. Dependency Inversion Principle (DIP)
High-level modules should not depend on low-level modules.

```python
class Database:
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        return "Connected to MySQL"
```

---