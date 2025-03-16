# Method 1: Singleton using a Metaclass
class SingletonMeta(type):
    """ A metaclass for creating Singleton classes. """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class SingletonClass(metaclass=SingletonMeta):
    """ Example class using the Singleton pattern via metaclass. """
    def __init__(self, value: str):
        self.value = value

# Method 2: Singleton using a Decorator
def singleton(cls):
    """ A decorator to implement Singleton pattern. """
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class DecoratorSingleton:
    """ Example class using the Singleton pattern via decorator. """
    def __init__(self, value: str):
        self.value = value

# Demonstration
if __name__ == "__main__":
    # Testing metaclass-based Singleton
    obj1 = SingletonClass("First Instance")
    obj2 = SingletonClass("Second Instance")

    print(f"Metaclass Singleton: {obj1.value}")  # Output: First Instance
    print(f"Are obj1 and obj2 the same? {obj1 is obj2}")  # Output: True

    # Testing decorator-based Singleton
    obj3 = DecoratorSingleton("First Decorated Instance")
    obj4 = DecoratorSingleton("Second Decorated Instance")

    print(f"Decorator Singleton: {obj3.value}")  # Output: First Decorated Instance
    print(f"Are obj3 and obj4 the same? {obj3 is obj4}")  # Output: True
