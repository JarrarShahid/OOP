# open_closed.py

from abc import ABC, abstractmethod

# Abstract base class for payment methods
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete implementations for different payment methods
class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card.")

class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal.")

class BitcoinPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using Bitcoin.")

# Payment processor that follows the Open/Closed Principle
class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process_payment(self, amount):
        self.payment_method.pay(amount)


# Demonstration
if __name__ == "__main__":
    credit_card = CreditCardPayment()
    paypal = PayPalPayment()
    bitcoin = BitcoinPayment()

    processor1 = PaymentProcessor(credit_card)
    processor2 = PaymentProcessor(paypal)
    processor3 = PaymentProcessor(bitcoin)

    processor1.process_payment(100)
    processor2.process_payment(200)
    processor3.process_payment(300)
