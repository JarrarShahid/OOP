# e_commerce.py

import uuid

class Product:
    """Represents a product in the e-commerce system."""
    def __init__(self, name, price, stock):
        self.product_id = str(uuid.uuid4())[:8]  # Unique Product ID
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} (ID: {self.product_id}) - ${self.price} | Stock: {self.stock}"

    def update_stock(self, quantity):
        """Update stock after a purchase."""
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        return False


class User:
    """Represents a user in the system."""
    def __init__(self, name, email):
        self.user_id = str(uuid.uuid4())[:8]  # Unique User ID
        self.name = name
        self.email = email
        self.cart = Cart(self)

    def __str__(self):
        return f"User: {self.name} (Email: {self.email})"


class Cart:
    """Represents a shopping cart."""
    def __init__(self, user):
        self.user = user
        self.items = {}  # {product: quantity}

    def add_product(self, product, quantity=1):
        """Add a product to the cart."""
        if product.stock >= quantity:
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity
            print(f"🛒 {quantity}x {product.name} added to {self.user.name}'s cart.")
        else:
            print(f"⚠️ Not enough stock for {product.name}!")

    def remove_product(self, product):
        """Remove a product from the cart."""
        if product in self.items:
            del self.items[product]
            print(f"❌ {product.name} removed from cart.")

    def view_cart(self):
        """Display cart items."""
        print(f"\n🛍️ {self.user.name}'s Cart:")
        for product, quantity in self.items.items():
            print(f"🔹 {quantity}x {product.name} - ${product.price * quantity}")
        if not self.items:
            print("🛒 Cart is empty!")

    def checkout(self):
        """Proceed to checkout and place an order."""
        if not self.items:
            print("❌ Cannot checkout. Cart is empty!")
            return None

        total = sum(product.price * quantity for product, quantity in self.items.items())

        # Update stock
        for product, quantity in self.items.items():
            product.update_stock(quantity)

        order = Order(self.user, self.items, total)
        self.items = {}  # Clear cart after checkout
        print(f"✅ Order placed for {self.user.name}. Total: ${total:.2f}")
        return order


class Order:
    """Represents an order placed by a user."""
    def __init__(self, user, items, total_price):
        self.order_id = str(uuid.uuid4())[:8]  # Unique Order ID
        self.user = user
        self.items = items
        self.total_price = total_price
        print(f"📦 Order {self.order_id} created for {user.name}. Total: ${total_price:.2f}")

    def view_order(self):
        """Displays order details."""
        print(f"\n📜 Order Details (ID: {self.order_id})")
        for product, quantity in self.items.items():
            print(f"🔹 {quantity}x {product.name} - ${product.price * quantity}")
        print(f"💳 Total Paid: ${self.total_price:.2f}")


# 🎯 Demonstration
if __name__ == "__main__":
    # Create products
    laptop = Product("Laptop", 1200, 5)
    phone = Product("Smartphone", 800, 10)
    headset = Product("Headset", 150, 20)

    # Create users
    alice = User("Alice", "alice@example.com")
    bob = User("Bob", "bob@example.com")

    # Alice adds products to cart
    alice.cart.add_product(laptop, 1)
    alice.cart.add_product(phone, 2)
    alice.cart.view_cart()

    # Alice checks out
    order1 = alice.cart.checkout()

    # Bob buys a headset
    bob.cart.add_product(headset, 3)
    bob.cart.view_cart()
    order2 = bob.cart.checkout()

    # View Orders
    if order1:
        order1.view_order()
    if order2:
        order2.view_order()

