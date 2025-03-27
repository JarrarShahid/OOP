import pytest

# ---------------------- Common Assertions ----------------------

def assert_positive_number(value, msg="Value should be positive"):
    """Ensures that a number is positive."""
    assert value >= 0, msg

def assert_instance(obj, cls, msg="Object is not an instance of expected class"):
    """Checks if an object is an instance of a specific class."""
    assert isinstance(obj, cls), msg

def assert_list_not_empty(lst, msg="List should not be empty"):
    """Ensures a list is not empty."""
    assert len(lst) > 0, msg


# ---------------------- Mock Classes for Testing ----------------------

class MockBankAccount:
    """Mock class to simulate BankAccount behavior."""
    def __init__(self, owner="Test User", balance=1000):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount


class MockShoppingCart:
    """Mock class to simulate ShoppingCart behavior."""
    def __init__(self):
        self.items = []

    def add_product(self, product_name, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.items.append({"name": product_name, "price": price})

    def total_price(self):
        return sum(item["price"] for item in self.items)

