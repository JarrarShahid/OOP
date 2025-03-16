from abc import ABC, abstractmethod

# Step 1: Define the Strategy Interface
class PaymentStrategy(ABC):
    """Abstract Strategy class for different payment methods."""
    
    @abstractmethod
    def pay(self, amount: float):
        pass

# Step 2: Implement Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    """Concrete Strategy for credit card payments."""
    
    def __init__(self, card_number: str, card_holder: str):
        self.card_number = card_number
        self.card_holder = card_holder

    def pay(self, amount: float):
        print(f"[Credit Card] {self.card_holder} paid ${amount:.2f} using card {self.card_number[-4:]}.")

class PayPalPayment(PaymentStrategy):
    """Concrete Strategy for PayPal payments."""
    
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float):
        print(f"[PayPal] {self.email} paid ${amount:.2f} via PayPal.")

class BitcoinPayment(PaymentStrategy):
    """Concrete Strategy for Bitcoin payments."""
    
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def pay(self, amount: float):
        print(f"[Bitcoin] Payment of ${amount:.2f} sent to BTC wallet {self.wallet_address}.")

# Step 3: Define the Context Class
class PaymentContext:
    """Context class that selects and executes a payment strategy."""
    
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy  # The selected payment strategy

    def set_strategy(self, strategy: PaymentStrategy):
        """Dynamically change the payment strategy."""
        self._strategy = strategy

    def checkout(self, amount: float):
        """Execute the selected payment strategy."""
        self._strategy.pay(amount)

# Step 4: Demonstration
if __name__ == "__main__":
    # User selects a payment method
    credit_card = CreditCardPayment("1234-5678-9876-5432", "Alice Johnson")
    paypal = PayPalPayment("alice@example.com")
    bitcoin = BitcoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")

    # Context to use different strategies
    payment = PaymentContext(credit_card)
    payment.checkout(100)  # Paying with Credit Card

    payment.set_strategy(paypal)
    payment.checkout(200)  # Paying with PayPal

    payment.set_strategy(bitcoin)
    payment.checkout(500)  # Paying with Bitcoin
