import pytest
from real_world_examples.bank_management import BankAccount
from real_world_examples.e_commerce import Product, ShoppingCart

# ---------------------- Bank Management Tests ----------------------

def test_bank_account_creation():
    account = BankAccount("John Doe", 1000)
    assert account.owner == "John Doe"
    assert account.balance == 1000

def test_bank_deposit():
    account = BankAccount("Alice", 500)
    account.deposit(300)
    assert account.balance == 800

def test_bank_withdrawal():
    account = BankAccount("Bob", 1000)
    account.withdraw(400)
    assert account.balance == 600

def test_bank_insufficient_funds():
    account = BankAccount("Charlie", 200)
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(300)

# ---------------------- E-Commerce Tests ----------------------

def test_product_creation():
    product = Product("Laptop", 1500)
    assert product.name == "Laptop"
    assert product.price == 1500

def test_shopping_cart_add_product():
    cart = ShoppingCart()
    product = Product("Phone", 800)
    cart.add_product(product)
    assert len(cart.items) == 1
    assert cart.items[0].name == "Phone"

def test_shopping_cart_total():
    cart = ShoppingCart()
    cart.add_product(Product("Tablet", 600))
    cart.add_product(Product("Headphones", 200))
    assert cart.total_price() == 800

def test_shopping_cart_empty():
    cart = ShoppingCart()
    assert cart.total_price() == 0

