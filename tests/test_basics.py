import pytest
from basics.encapsulation import EncapsulatedClass
from basics.inheritance import ParentClass, ChildClass
from basics.polymorphism import Animal, Dog, Cat
from basics.abstraction import AbstractShape, Circle

# Test Encapsulation
def test_encapsulation():
    obj = EncapsulatedClass("secret")
    assert obj.get_hidden_value() == "secret"
    obj.set_hidden_value("new_secret")
    assert obj.get_hidden_value() == "new_secret"
    
    # Ensure private variable is truly inaccessible
    with pytest.raises(AttributeError):
        _ = obj.__hidden_value

# Test Inheritance
def test_inheritance():
    child = ChildClass("Test")
    assert child.get_name() == "Test"
    assert child.child_method() == "Child method executed"

# Test Polymorphism
def test_polymorphism():
    dog = Dog()
    cat = Cat()
    
    assert dog.speak() == "Woof!"
    assert cat.speak() == "Meow!"
    
    # Ensure base class does not override derived behavior
    animal_list = [Dog(), Cat()]
    sounds = [animal.speak() for animal in animal_list]
    assert sounds == ["Woof!", "Meow!"]

# Test Abstraction
def test_abstraction():
    circle = Circle(5)
    assert round(circle.area(), 2) == 78.54  # π * r^2 (approx.)
    assert round(circle.perimeter(), 2) == 31.42  # 2 * π * r (approx.)
    
    # Ensure abstract class cannot be instantiated
    with pytest.raises(TypeError):
        _ = AbstractShape()
