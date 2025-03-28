# Design Patterns

Design patterns are reusable solutions to common software design problems.

## 1. Singleton Pattern
Ensures a class has only one instance and provides a global point of access.

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
```

## 2. Factory Pattern
Provides an interface for creating objects without specifying their concrete types.

```python
class AnimalFactory:
    @staticmethod
    def get_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
```

## 3. Observer Pattern
Defines a dependency between objects so that when one object changes state, all its dependents are notified.

```python
class Observer:
    def update(self, message):
        pass

class Subscriber(Observer):
    def update(self, message):
        print(f"Received: {message}")
```

These documents explain fundamental OOP concepts, SOLID principles, and key design patterns used in Python development.