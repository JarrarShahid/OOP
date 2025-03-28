# Object-Oriented Programming (OOP) Concepts

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of objects, which encapsulate data and behavior. Python supports OOP through classes and objects.

## Key OOP Principles

### 1. Encapsulation
Encapsulation is the practice of bundling data (variables) and methods (functions) that operate on the data into a single unit (class). It also restricts direct access to some of the object's components.

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        self.__balance += amount
        return self.__balance
```

### 2. Inheritance
Inheritance allows a class to derive properties and behavior from another class, promoting code reuse.

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Bark!"
```

### 3. Polymorphism
Polymorphism enables a single interface to represent different types.

```python
def make_animal_speak(animal):
    return animal.speak()

class Cat:
    def speak(self):
        return "Meow!"

print(make_animal_speak(Dog()))  # Output: Bark!
print(make_animal_speak(Cat()))  # Output: Meow!
```

### 4. Abstraction
Abstraction hides implementation details and shows only essential features.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Engine started!"
```

---





