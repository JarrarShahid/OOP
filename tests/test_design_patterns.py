import pytest
from design_patterns.singleton import Singleton
from design_patterns.factory import AnimalFactory
from design_patterns.observer import Subject, Observer

# Test Singleton Pattern
def test_singleton():
    instance1 = Singleton()
    instance2 = Singleton()
    assert instance1 is instance2, "Singleton instances should be the same object"

# Test Factory Pattern
def test_factory():
    dog = AnimalFactory.create_animal("dog")
    cat = AnimalFactory.create_animal("cat")
    
    assert dog.speak() == "Woof!", "Dog should say Woof!"
    assert cat.speak() == "Meow!", "Cat should say Meow!"
    
    with pytest.raises(ValueError):
        AnimalFactory.create_animal("fish")  # Should raise an exception for an unknown type

# Test Observer Pattern
def test_observer():
    subject = Subject()
    observer1 = Observer("Observer1")
    observer2 = Observer("Observer2")
    
    subject.attach(observer1)
    subject.attach(observer2)
    
    subject.notify("Event Occurred")
    
    assert observer1.last_notification == "Observer1 received: Event Occurred"
    assert observer2.last_notification == "Observer2 received: Event Occurred"
    
    subject.detach(observer1)
    subject.notify("Another Event")
    
    assert observer1.last_notification == "Observer1 received: Event Occurred", "Detached observer should not receive updates"
    assert observer2.last_notification == "Observer2 received: Another Event"

if __name__ == "__main__":
    pytest.main()